"""Case W3: is a PPO-tuned model the pursuit of its reward? Computes exactly what REGISTRATION.md says.

Needs torch, transformers and datasets; downloads the three public models and the IMDB training split from Hugging
Face. Usage: python3 run.py   (writes output.json next to this file, aggregates only)
"""
import json, os, time
from pathlib import Path
import numpy as np
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoModelForSequenceClassification, AutoTokenizer

HERE = Path(__file__).resolve().parent
POLICY, REFERENCE, CLASSIFIER = "lvwerra/gpt2-imdb-pos-v2", "lvwerra/gpt2-imdb", "lvwerra/distilbert-imdb"
SEED, CONTEXTS, K, BOOT, S0_TOL = 20261004, 300, 32, 1000, 1e-4
SCRATCH = Path(os.environ.get("W3_SCRATCH", Path.home() / ".cache" / "w3"))   # per-context values, outside the repo


def contexts(tokenizer):
    reviews = [t for t in load_dataset("stanfordnlp/imdb", split="train")["text"] if len(t) > 200]
    rng = np.random.default_rng(SEED)
    chosen = rng.choice(len(reviews), CONTEXTS, replace=False)
    out = []
    for i in chosen:
        k, L = int(rng.integers(2, 8)), int(rng.integers(4, 16))
        ids = tokenizer.encode(reviews[i])[:k]
        out.append((ids, tokenizer.decode(ids), L))
    return out


@torch.no_grad()
def sample(model, prompt_ids, L, generator):
    """K continuations of exactly L tokens from the full softmax, and their log-probabilities summed while sampling.
    Uses the key-value cache: the same computation as a full pass per token, which S0 checks against the scorer."""
    ids = torch.tensor([prompt_ids] * K)
    out = model(ids, use_cache=True)
    past, logits = out.past_key_values, out.logits[:, -1, :]
    logp = torch.zeros(K, dtype=torch.float64)
    for step in range(L):
        lp = torch.log_softmax(logits.double(), -1)
        nxt = torch.multinomial(lp.exp(), 1, generator=generator)
        logp += lp.gather(1, nxt).squeeze(1)
        ids = torch.cat([ids, nxt], 1)
        if step < L - 1:
            out = model(nxt, past_key_values=past, use_cache=True)
            past, logits = out.past_key_values, out.logits[:, -1, :]
    return ids, logp


@torch.no_grad()
def score(model, ids, n_prompt):
    lp = torch.log_softmax(model(ids).logits.double(), -1)
    return lp[:, n_prompt - 1:-1, :].gather(2, ids[:, n_prompt:].unsqueeze(2)).squeeze(2).sum(1)


def fit(z, x):
    """Least squares of z on x with an intercept: (slope, SSR, SST). Where x does not vary, the fitted line is the
    mean of z, its slope is undefined (NaN), and SSR = SST: the exact least-squares value, which the first run, by
    dividing 0 by 0, turned into NaN."""
    zc, xc = z - z.mean(), x - x.mean()
    sxx = float((xc ** 2).sum())
    if sxx == 0.0:
        return float("nan"), float((zc ** 2).sum()), float((zc ** 2).sum())
    slope = float((zc * xc).sum() / sxx)
    return slope, float(((zc - slope * xc) ** 2).sum()), float((zc ** 2).sum())


def main():
    torch.set_num_threads(4)
    tok = AutoTokenizer.from_pretrained(REFERENCE)
    # double precision, so that sampling with the key-value cache and scoring by a full pass agree far inside S0's 1e-4
    pol = AutoModelForCausalLM.from_pretrained(POLICY, dtype=torch.float64).eval()
    ref = AutoModelForCausalLM.from_pretrained(REFERENCE, dtype=torch.float64).eval()
    ctok = AutoTokenizer.from_pretrained(CLASSIFIER)
    clf = AutoModelForSequenceClassification.from_pretrained(CLASSIFIER).eval()
    assert clf.config.id2label[1] == "POSITIVE"
    rows, s0_worst, start = [], 0.0, time.time()
    for c, (prompt_ids, prompt_text, L) in enumerate(contexts(tok)):
        n = len(prompt_ids)
        ids_ref, lp_ref_sampled = sample(ref, prompt_ids, L, torch.Generator().manual_seed(SEED + 2 * c))
        ids_pol, lp_pol_sampled = sample(pol, prompt_ids, L, torch.Generator().manual_seed(SEED + 2 * c + 1))
        ids = torch.cat([ids_ref, ids_pol])
        lp_ref, lp_pol = score(ref, ids, n), score(pol, ids, n)
        s0_worst = max(s0_worst, float((lp_ref[:K] - lp_ref_sampled).abs().max()),
                       float((lp_pol[K:] - lp_pol_sampled).abs().max()))
        z = (lp_pol - lp_ref).numpy()
        texts = [prompt_text + tok.decode(y[n:]) for y in ids]
        with torch.no_grad():
            enc = ctok(texts, return_tensors="pt", padding=True, truncation=True, max_length=512)
            logits = clf(**enc).logits.double()
        r, r_neg = logits[:, 1].numpy(), logits[:, 0].numpy()
        p = torch.softmax(logits, -1)[:, 1].numpy()
        row = {"z": z, "r": r, "p": p, "logodds": r - r_neg, "L": L}
        for name in ("r", "p", "logodds"):
            row[f"slope_{name}"], row[f"ssr_{name}"], row["sst"] = fit(z, row[name])
        rows.append(row)
        if (c + 1) % 25 == 0:
            print(f"{c + 1} contexts, {time.time() - start:.0f}s", flush=True)

    import pickle                     # per-context values stay outside the repository (README, working agreements)
    SCRATCH.mkdir(parents=True, exist_ok=True)
    (SCRATCH / "w3_rows.pkl").write_bytes(pickle.dumps(rows))
    flat = {name: sum(1 for w in rows if np.ptp(w[name]) == 0) for name in ("r", "p", "logodds")}
    print("contexts where the regressor does not vary:", flat, flush=True)
    sst = np.array([w["sst"] for w in rows])
    ssr = {name: np.array([w[f"ssr_{name}"] for w in rows]) for name in ("r", "p", "logodds")}
    R2 = {name: float(1 - ssr[name].sum() / sst.sum()) for name in ssr}
    rng = np.random.default_rng(SEED)
    boots = []
    for _ in range(BOOT):
        i = rng.integers(0, len(rows), len(rows))
        a, b = 1 - ssr["r"][i].sum() / sst[i].sum(), 1 - ssr["p"][i].sum() / sst[i].sum()
        boots.append((a, b, a - b))
    boots = np.array(boots)
    ci = lambda col: [float(x) for x in np.percentile(boots[:, col], [2.5, 97.5])]
    ci_r, ci_d = ci(0), ci(2)
    s1 = "held" if ci_r[0] > 0.5 else ("refuted" if ci_r[1] < 0.5 else "undecided")
    s2 = "held" if ci_d[0] > 0 else "refuted"

    # reported without a prediction
    zc = np.concatenate([w["z"] - w["z"].mean() for w in rows]); rc = np.concatenate([w["r"] - w["r"].mean() for w in rows])
    t_shared = float((zc * rc).sum() / (rc ** 2).sum())
    R2_shared = float(1 - ((zc - t_shared * rc) ** 2).sum() / sst.sum())
    slopes = np.array([w["slope_r"] for w in rows])
    departure = np.array([w["z"][K:].mean() for w in rows])
    r_ref, r_pol = np.array([w["r"][:K].mean() for w in rows]), np.array([w["r"][K:].mean() for w in rows])
    t_star, pursuit = [], []
    for w in rows:
        rr, target = w["r"][:K], w["r"][K:].mean()
        mean_at = lambda t: float(np.sum(np.exp(t * (rr - rr.max())) * rr) / np.sum(np.exp(t * (rr - rr.max()))))
        if target <= rr.mean():
            t_star.append(0.0); pursuit.append(0.0); continue
        if target >= rr.max():
            t_star.append(float("inf")); pursuit.append(float("nan")); continue
        lo, hi = 0.0, 1.0
        while mean_at(hi) < target:
            hi *= 2
        for _ in range(100):
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if mean_at(mid) < target else (lo, mid)
        t = (lo + hi) / 2
        log_mean_exp = float(np.log(np.mean(np.exp(t * (rr - rr.max())))) + t * rr.max())
        t_star.append(t); pursuit.append(t * mean_at(t) - log_mean_exp)
    t_star, pursuit = np.array(t_star), np.array(pursuit)
    ok = np.isfinite(pursuit)
    out = {
        "registered": {"S0": {"worst_abs_difference": s0_worst, "held": s0_worst <= S0_TOL},
                       "S1": {"R2_r": R2["r"], "interval_95": ci_r, "verdict": s1},
                       "S2": {"R2_r": R2["r"], "R2_p": R2["p"], "difference": R2["r"] - R2["p"],
                              "interval_95": ci_d, "verdict": s2}},
        "reported": {"R2_p_interval_95": ci(1), "R2_logodds": R2["logodds"],
                     "shared_slope": t_shared, "R2_shared_slope": R2_shared,
                     "slope_quartiles": [float(x) for x in np.nanpercentile(slopes, [25, 50, 75])],
                     "contexts_where_the_regressor_does_not_vary": flat,
                     "mean_reward_reference": float(r_ref.mean()), "mean_reward_policy": float(r_pol.mean()),
                     "departure_mean": float(departure.mean()),
                     "departure_quartiles": [float(x) for x in np.percentile(departure, [25, 50, 75])],
                     "t_star_median_finite": float(np.median(t_star[np.isfinite(t_star)])),
                     "t_star_share_infinite": float(np.mean(np.isinf(t_star))),
                     "pursuit_part_mean_where_estimable": float(pursuit[ok].mean()),
                     "departure_mean_where_estimable": float(departure[ok].mean()),
                     "contexts_estimable": int(ok.sum()), "contexts": len(rows)},
    }
    (HERE / "output.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
