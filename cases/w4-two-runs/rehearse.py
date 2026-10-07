"""W4's rehearsal (design rule 4), before registration: the estimator of estimate.py run end to end on synthetic
contexts where every quantity is known exactly, with the degenerate cases built in, and timed. Writes rehearsal.json.

Synthetic context: a reference R on N outcomes; a reward fA and a second reward fB = 0.8·fA + 0.6·noise; a shared
off-reward direction S and run-specific directions eA, eB. The runs are tilts of R:
  A ∝ R^{1+b}·exp(t·fA + s·S + d·eA),  B ∝ R^{1+b}·exp(t·fB + s·S + d·eB),
so b is sharpening, s a change both runs share, d drift. Four scenarios switch b and s on and off, with departures near
W3's 7 nats. Truth: the same functions on all N outcomes, with exact averages. Estimates: K draws from each of A, B, R.
Usage: python3 rehearse.py   (about half an hour; the record of the run-time measurement on the real models is added
by run.py --timing)
"""
import json, sys, time
from pathlib import Path
import numpy as np
from scipy.special import logsumexp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1] / "tools"))
from estimate import context_estimates, misalignment_parts                       # noqa: E402
import casekit                                                                    # noqa: E402

SEED, N, K, CONTEXTS = 20261005, 200_000, 64, 120          # K as in run.py
SCENARIOS = {"sharpening and shared": (0.3, 2.2, 2.2), "sharpening, no shared": (0.3, 0.0, 3.1),
             "shared, no sharpening": (0.0, 2.2, 2.2), "neither": (0.0, 0.0, 3.1)}      # (b, s, d), t = 2.0


def world(r, b, s, d, t=2.0, n=N):
    lR = r.normal(size=n); lR -= logsumexp(lR)
    fA = r.normal(size=n); fB = 0.8 * fA + 0.6 * r.normal(size=n)
    S, eA, eB = r.normal(size=(3, n))
    lA = (1 + b) * lR + t * fA + s * S + d * eA; lA -= logsumexp(lA)
    lB = (1 + b) * lR + t * fB + s * S + d * eB; lB -= logsumexp(lB)
    return lA, lB, lR, fA, fB


def exact(lA, lB, lR, fA, fB):
    """The quantities of estimate.py with exact averages over all outcomes: the 'own draws' are every outcome, weighted
    by A, which misalignment_parts receives as a reweighting of the uniform base."""
    n = lR.size
    base = lR + np.log(n)                                                         # mean over outcomes of e^base = 1
    # averages under A: misalignment_parts takes means over flagged draws, so pass A-weighted copies
    A = np.exp(lA)
    def parts():
        dep = float(A @ (lA - lR)); target_f = float(A @ fA)
        from estimate import ray, match
        t, lz = ray(base, fA, target_f)
        out = {"departure": dep, "t_star": t, "M": dep - (t * target_f - lz), "named": []}
        named = [lR, fB, lB - lR]
        for k in range(1, 4):
            Phi = np.vstack([fA] + named[:k]); target = Phi @ A
            c, lz, w, err = match(base, Phi, target)
            un = float(A @ (lA - lR - c @ Phi) + lz)
            out["named"].append({"coef": [float(x) for x in c], "unexplained": un, "named": out["M"] - un})
        return out
    lmix = np.logaddexp(lA, lB) - np.log(2); B = np.exp(lB)
    return {"A": parts(), "drift": float(0.5 * A @ (lA - lmix) + 0.5 * B @ (lB - lmix))}


def draws(r, lA, lB, lR, fA, fB, k=K):
    idx = [r.choice(lR.size, k, p=np.exp(l)) for l in (lA, lB, lR)]
    src = np.repeat([0, 1, 2], k); i = np.concatenate(idx)
    return src, lA[i], lB[i], lR[i], fA[i], fB[i]


def summary(rows, key):
    return casekit.bootstrap([key(x) for x in rows], boot=1000, seed=SEED)


def synthetic():
    r = np.random.default_rng(SEED); out = {}
    for name, (b, s, d) in SCENARIOS.items():
        rows, t0 = [], time.perf_counter()
        for _ in range(CONTEXTS):
            w = world(r, b, s, d)
            rows.append({"truth": exact(*w), "est": context_estimates(*draws(r, *w))})
        get = lambda part, f: (lambda x: f(x[part]))
        out[name] = {
            "seconds_per_context": (time.perf_counter() - t0) / CONTEXTS,
            "departure": {"truth": summary(rows, lambda x: x["truth"]["A"]["departure"]),
                          "estimate": summary(rows, lambda x: x["est"]["A"]["departure"])},
            "M_share_of_departure": {"truth": summary(rows, lambda x: x["truth"]["A"]["M"] / x["truth"]["A"]["departure"]),
                                     "estimate": summary(rows, lambda x: x["est"]["A"]["M"] / x["est"]["A"]["departure"])},
            "drift": {"truth": summary(rows, lambda x: x["truth"]["drift"]), "estimate": summary(rows, lambda x: x["est"]["drift"])},
        }
        for k, label in enumerate(["sharpening", "other reward", "other run"]):
            out[name][f"named_share_after_{label}"] = {
                "truth": summary(rows, lambda x, k=k: x["truth"]["A"]["named"][k]["named"] / x["truth"]["A"]["M"]),
                "estimate": summary(rows, lambda x, k=k: x["est"]["A"]["named"][k]["named"] / x["est"]["A"]["M"]
                                    if x["est"]["A"]["named"] else np.nan)}
        out[name]["coef_sharpening"] = {"truth": summary(rows, lambda x: x["truth"]["A"]["named"][0]["coef"][1]),
                                        "estimate": summary(rows, lambda x: x["est"]["A"]["named"][0]["coef"][1]
                                                            if x["est"]["A"]["named"] else np.nan)}
        out[name]["coef_other_run"] = {"truth": summary(rows, lambda x: x["truth"]["A"]["named"][2]["coef"][3]),
                                       "estimate": summary(rows, lambda x: x["est"]["A"]["named"][2]["coef"][3]
                                                           if x["est"]["A"]["named"] else np.nan)}
        out[name]["effective_draws_median"] = float(np.median([x["est"]["A"]["named"][2]["effective_draws"]
                                                               for x in rows if x["est"]["A"]["named"]]))
        for key, k, j in (("sharpening", 0, 1), ("other_run", 2, 3)):                  # the paired bias of each test
            diff = np.array([x["est"]["A"]["named"][k]["coef"][j] - x["truth"]["A"]["named"][k]["coef"][j]
                             for x in rows if x["est"]["A"]["named"]])
            out[name][f"bias_{key}"] = {"mean": float(diff.mean()), "se": float(diff.std(ddof=1) / np.sqrt(len(diff)))}
        out[name]["_rows"] = rows
        print(name, json.dumps({k: v for k, v in out[name].items() if k.startswith(("coef", "bias"))}), flush=True)
    return out


def margins_and_verdicts(scen):
    """Each test's margin: the largest bias found over the scenarios plus two standard errors, rounded up to 0.01; and
    the verdict each scenario would get with that margin, to show that each test can hold and can fail."""
    margins = {key: float(np.ceil(100 * max(abs(v[f"bias_{key}"]["mean"]) + 2 * v[f"bias_{key}"]["se"]
                                            for v in scen.values())) / 100) for key in ("sharpening", "other_run")}
    verdicts = {}
    for name, v in scen.items():
        verdicts[name] = {}
        for key, ckey in (("sharpening", "coef_sharpening"), ("other_run", "coef_other_run")):
            lo, hi = v[ckey]["estimate"]["interval_95"]
            verdicts[name][key] = "held" if lo > margins[key] else ("refuted" if hi < margins[key] else "undecided")
    return margins, verdicts


def degenerate():
    """The degenerate cases of design rule 4: each must give finite numbers or a flagged NaN, never a crash."""
    r = np.random.default_rng(SEED + 1); res = {}
    w = list(world(r, 0.3, 2.2, 2.2, n=2000)); w[3] = np.zeros_like(w[3])           # a reward that does not vary
    e = context_estimates(*draws(r, *w)); res["flat reward"] = e["flat_reward"] and e["A"]["t_star"] == 0.0
    w = world(r, 0.3, 2.2, 2.2, n=40)                                              # draws repeat
    e = context_estimates(*draws(r, *w)); res["repeated draws"] = e["repeated_draws"] > 0 and np.isfinite(e["A"]["M"])
    lA, lB, lR, fA, fB = world(r, 0.3, 2.2, 2.2, n=2000)                            # A only on the reward's top
    top = fA >= np.sort(fA)[-3]; lA = np.where(top, lA, lA - 1000.0); lA -= logsumexp(lA)   # A: all but e^-1000 on the top
    e = context_estimates(*draws(r, lA, lB, lR, fA, fB))
    res["infinite intensity flagged"] = (not np.isfinite(e["A"]["t_star"]) and np.isnan(e["A"]["M"])) or bool(np.isfinite(e["A"]["M"]))
    lA, lB, lR, fA, fB = world(r, 0.3, 2.2, 2.2, n=2000)                            # log-probabilities near -900
    src, xa, xb, xr, fa, fb = draws(r, lA, lB, lR, fA, fB)
    e1 = context_estimates(src, xa, xb, xr, fa, fb); e2 = context_estimates(src, xa - 900, xb - 900, xr - 900, fa, fb)
    res["log-probabilities near -900"] = bool(abs(e1["A"]["M"] - e2["A"]["M"]) <= 1e-8 and abs(e1["drift"] - e2["drift"]) <= 1e-10)
    return {k: bool(v) for k, v in res.items()}


def main():
    record = {"seed": SEED, "outcomes": N, "draws_per_behaviour": K, "contexts_per_scenario": CONTEXTS,
              "degenerate_cases": degenerate()}
    print(record["degenerate_cases"], flush=True)
    scen = synthetic()
    record["margins"], record["verdicts_in_the_rehearsal"] = margins_and_verdicts(scen)
    record["scenarios"] = {k: {kk: vv for kk, vv in v.items() if kk != "_rows"} for k, v in scen.items()}
    print(json.dumps({"margins": record["margins"], "verdicts": record["verdicts_in_the_rehearsal"]}, indent=1), flush=True)
    path = HERE / "rehearsal.json"
    old = json.loads(path.read_text()) if path.exists() else {}
    record.update({k: v for k, v in old.items() if k == "timing_on_the_real_models"})
    casekit.write_record(path, record)


if __name__ == "__main__":
    main()
