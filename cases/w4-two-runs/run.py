"""Case W4: is W3's off-reward change systematic or drift? Computes exactly what REGISTRATION.md says.

Needs torch, transformers and datasets; downloads the three language models, the two sentiment classifiers and the
IMDB training split from Hugging Face. Usage:
  python3 run.py            the test: writes output.json next to this file, aggregates only
  python3 run.py --timing   the rehearsal's measurement: two contexts drawn with another seed; records only the time
                            per context and the sampler's agreement with the scorer in rehearsal.json
"""
import json, sys, time
from pathlib import Path
import numpy as np
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoModelForSequenceClassification, AutoTokenizer

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1] / "tools"))
from estimate import context_estimates                                           # noqa: E402
import casekit                                                                    # noqa: E402

RUN_A, RUN_B, REFERENCE = "lvwerra/gpt2-imdb-pos-v2", "lvwerra/gpt2-imdb-pos", "lvwerra/gpt2-imdb"
REWARD_A, REWARD_B = "lvwerra/distilbert-imdb", "lvwerra/bert-imdb"
SEED, TIMING_SEED, CONTEXTS, K, BOOT, S0_TOL = 20261006, 20261007, 200, 64, 1000, 1e-4
PROMPT_TOKENS, LENGTH, MIN_CHARS = 5, 15, 500
MARGINS = json.loads((HERE / "rehearsal.json").read_text()).get("margins", {}) if (HERE / "rehearsal.json").exists() else {}


def contexts(tokenizer, seed, n):
    """n reviews of the IMDB training split longer than MIN_CHARS characters, each cut to its first PROMPT_TOKENS
    tokens: inside both runs' training formats."""
    reviews = [t for t in load_dataset("stanfordnlp/imdb", split="train")["text"] if len(t) > MIN_CHARS]
    chosen = np.random.default_rng(seed).choice(len(reviews), n, replace=False)
    return [(ids := tokenizer.encode(reviews[i])[:PROMPT_TOKENS], tokenizer.decode(ids)) for i in chosen]


@torch.no_grad()
def sample(model, prompt_ids, generator):
    """K continuations of exactly LENGTH tokens from the full softmax, with their log-probabilities summed while
    sampling; the key-value cache in double precision, checked against the scorer by S0 (as in W3)."""
    ids = torch.tensor([prompt_ids] * K)
    out = model(ids, use_cache=True)
    past, logits = out.past_key_values, out.logits[:, -1, :]
    logp = torch.zeros(K, dtype=torch.float64)
    for step in range(LENGTH):
        lp = torch.log_softmax(logits.double(), -1)
        nxt = torch.multinomial(lp.exp(), 1, generator=generator)
        logp += lp.gather(1, nxt).squeeze(1)
        ids = torch.cat([ids, nxt], 1)
        if step < LENGTH - 1:
            out = model(nxt, past_key_values=past, use_cache=True)
            past, logits = out.past_key_values, out.logits[:, -1, :]
    return ids, logp


@torch.no_grad()
def score(model, ids, n_prompt):
    lp = torch.log_softmax(model(ids).logits.double(), -1)
    return lp[:, n_prompt - 1:-1, :].gather(2, ids[:, n_prompt:].unsqueeze(2)).squeeze(2).sum(1)


@torch.no_grad()
def positive_logit(clf, ctok, texts):
    enc = ctok(texts, return_tensors="pt", padding=True, truncation=True, max_length=512)
    return clf(**enc).logits.double()[:, 1].numpy()


def load():
    tok = AutoTokenizer.from_pretrained(REFERENCE)
    lms = [AutoModelForCausalLM.from_pretrained(m, dtype=torch.float64).eval() for m in (RUN_A, RUN_B, REFERENCE)]
    clfs = []
    for m in (REWARD_A, REWARD_B):
        clf = AutoModelForSequenceClassification.from_pretrained(m).eval()
        clfs.append((clf, AutoTokenizer.from_pretrained(m)))
    return tok, lms, clfs


def one_context(c, prompt_ids, prompt_text, tok, lms, clfs, seed):
    """Every draw and score of one context, and its estimates; S0's worst gap on the way."""
    n = len(prompt_ids)
    drawn = [sample(m, prompt_ids, torch.Generator().manual_seed(seed + 3 * c + j)) for j, m in enumerate(lms)]
    ids = torch.cat([d[0] for d in drawn])
    lA, lB, lR = (score(m, ids, n).numpy() for m in lms)
    gap = max(float(np.abs(l[j * K:(j + 1) * K] - drawn[j][1].numpy()).max()) for j, l in enumerate((lA, lB, lR)))
    texts = [prompt_text + tok.decode(y[n:]) for y in ids]
    fA, fB = (positive_logit(clf, ctok, texts) for clf, ctok in clfs)
    src = np.repeat([0, 1, 2], K)
    return {"est": context_estimates(src, lA, lB, lR, fA, fB), "s0_gap": gap}


def timing():
    torch.set_num_threads(4)
    tok, lms, clfs = load()
    cs = contexts(tok, TIMING_SEED, 2)
    start = time.time()
    gaps = [one_context(c, ids, text, tok, lms, clfs, TIMING_SEED)["s0_gap"] for c, (ids, text) in enumerate(cs)]
    per = (time.time() - start) / len(cs)
    path = HERE / "rehearsal.json"; record = json.loads(path.read_text())
    record["timing_on_the_real_models"] = {"seconds_per_context": per, "draws_per_model": K, "contexts": CONTEXTS,
                                           "projected_hours": per * CONTEXTS / 3600, "s0_worst_gap": max(gaps)}
    casekit.write_record(path, record)
    print(json.dumps(record["timing_on_the_real_models"], indent=1))


def aggregate(rows):
    est = [r["est"] for r in rows]
    A = lambda f: [f(e["A"]) if e["A"]["named"] else float("nan") for e in est]
    B = lambda f: [f(e["B"]) if e["B"]["named"] else float("nan") for e in est]
    S = lambda values: casekit.bootstrap(values, boot=BOOT, seed=SEED)
    s0 = max(r["s0_gap"] for r in rows)
    sharpen = S(A(lambda x: x["named"][0]["coef"][1])); other = S(A(lambda x: x["named"][2]["coef"][3]))
    verdict = lambda s, margin: ("held" if s["interval_95"][0] > margin else
                                 ("refuted" if s["interval_95"][1] < margin else "undecided"))
    out = {
        "registered": {
            "S0": {"worst_abs_difference": s0, "held": s0 <= S0_TOL},
            "S1": {"coefficient_of_log_reference": sharpen, "margin": MARGINS["sharpening"],
                   "verdict": verdict(sharpen, MARGINS["sharpening"])},
            "S2": {"coefficient_of_the_other_run": other, "margin": MARGINS["other_run"],
                   "verdict": verdict(other, MARGINS["other_run"])},
        },
        "reported": {
            "departure_A": S([e["A"]["departure"] for e in est]), "departure_B": S([e["B"]["departure"] for e in est]),
            "kl_A_B": S([e["kl_A_B"] for e in est]), "kl_B_A": S([e["kl_B_A"] for e in est]),
            "drift": S([e["drift"] for e in est]),
            "M_share_A": S(A(lambda x: x["M"] / x["departure"])), "M_share_B": S(B(lambda x: x["M"] / x["departure"])),
            "named_share_A": {name: S(A(lambda x, k=k: x["named"][k]["named"] / x["M"]))
                              for k, name in enumerate(["sharpening", "+ other reward", "+ other run"])},
            "named_share_B": {name: S(B(lambda x, k=k: x["named"][k]["named"] / x["M"]))
                              for k, name in enumerate(["sharpening", "+ other reward", "+ other run"])},
            "coefficient_of_log_reference_B": S(B(lambda x: x["named"][0]["coef"][1])),
            "coefficient_of_the_other_run_B": S(B(lambda x: x["named"][2]["coef"][3])),
            "t_star_A_median": float(np.nanmedian([e["A"]["t_star"] for e in est])),
            "t_star_A_infinite": int(sum(not np.isfinite(e["A"]["t_star"]) for e in est)),
            "effective_draws_median_A": float(np.nanmedian(A(lambda x: x["named"][2]["effective_draws"]))),
            "contexts_with_a_flat_reward": int(sum(e["flat_reward"] for e in est)),
            "contexts_with_repeated_draws": int(sum(e["repeated_draws"] > 0 for e in est)),
            "contexts": len(rows),
        },
    }
    return out


def main():
    torch.set_num_threads(4)
    tok, lms, clfs = load()
    rows, start = [], time.time()
    for c, (ids, text) in enumerate(contexts(tok, SEED, CONTEXTS)):
        rows.append(one_context(c, ids, text, tok, lms, clfs, SEED))
        if (c + 1) % 10 == 0:
            casekit.save_rows(rows, "w4_rows")                                      # before any aggregation
            print(f"{c + 1} contexts, {time.time() - start:.0f}s", flush=True)
    casekit.save_rows(rows, "w4_rows")
    out = aggregate(rows)
    casekit.write_record(HERE / "output.json", out)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    timing() if "--timing" in sys.argv else main()
