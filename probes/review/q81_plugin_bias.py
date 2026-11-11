"""What a record identifies of misalignment against an overall rate limit when conditions are repeated K times
(NOTES.md §39, Q81). Exploratory, not a check; simulated data only, nothing from case M1's data.
Usage: python3 probes/review/q81_plugin_bias.py [bias | edge]   (both by default)

bias  The shape of case M1 (mvp/cases/m1-decoding-toxicity): P = 400 conditions of equal weight, limit eps = 0.10,
      overall breach rate 0.326. Four truths with that overall rate, from no heterogeneity between conditions to a
      breach rate of 0 or 1 in each; for each, the true misalignment (R10 on the true rates) and the mean plug-in
      (R10 on rates estimated from K draws per condition), K = 1, 4, 16, 64, 256, over 200 simulated records. The two
      ends a record leaves open when no condition is repeated: kl(ubar‖eps), the conditions merged, and
      ubar·log(ubar/eps), every condition deterministic. Seed 7. About ten seconds.
edge  `stdalign.spec.overall_rate_limit` at a breach rate that is tiny and positive in one condition: the smaller
      root of R10's quadratic is computed by a difference that cancels, the nearest rate comes out 0, and the
      divergence infinite, where the value at a rate of exactly 0 is finite. A second.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1].parent))
from stdalign.spec import overall_rate_limit, kl_binary                              # noqa: E402

P, EPS, UBAR, REPS, KS = 400, 0.10, 0.326, 200, (1, 4, 16, 64, 256)


def bias():
    rng = np.random.default_rng(7)
    w = np.full(P, 1.0 / P)
    M = lambda u: overall_rate_limit(w, u, EPS)[0]                                   # noqa: E731
    print(f"conditions merged      kl(ubar‖eps)       = {kl_binary(UBAR, EPS):.4f}")
    print(f"conditions deterministic ubar·log(ubar/eps) = {UBAR * np.log(UBAR / EPS):.4f}\n")
    rest = (1 - UBAR) / UBAR
    truths = {
        "the same rate in every condition": lambda: np.full(P, UBAR),
        "rates Beta(1, 2.07)": lambda: np.clip(rng.beta(1.0, rest, P), 1e-9, 1 - 1e-9),
        "rates Beta(0.3, 0.62)": lambda: np.clip(rng.beta(0.3, 0.3 * rest, P), 1e-9, 1 - 1e-9),
        "rate 0 or 1 in each condition": lambda: (rng.random(P) < UBAR).astype(float),
    }
    print(f"{'truth':34s} {'true M':>8s} " + " ".join(f"{'K=' + str(k):>8s}" for k in KS))
    for name, draw in truths.items():
        true, est = [], {k: [] for k in KS}
        for _ in range(REPS):
            u = draw()
            true.append(M(u))
            for k in KS:
                est[k].append(M(rng.binomial(k, u) / k))
        print(f"{name:34s} {np.mean(true):8.4f} " + " ".join(f"{np.mean(est[k]):8.4f}" for k in KS))


def edge():
    w = np.full(4, 0.25)
    for tiny in (0.0, 1e-300, 1e-17, 1e-12, 1e-9):
        print(f"rates (0.5, 0.5, {tiny:g}, 0.9), eps = 0.1:  M = {overall_rate_limit(w, [0.5, 0.5, tiny, 0.9], 0.1)[0]}")


if __name__ == "__main__":
    which = sys.argv[1:] or ["bias", "edge"]
    for name in which:
        print(f"== {name} ==")
        {"bias": bias, "edge": edge}[name]()
        print()
