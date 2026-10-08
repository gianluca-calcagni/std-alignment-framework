"""Probe for the Notes of [P52], what a sample certifies about misalignment by access, on finite outcomes. Exploratory,
not a check. Usage: python3 probes/diagnostics/probe_access.py

(a) Five actors near the ray of a random F: n·Var of each estimate over 3,000 samples of 4,000 draws (and as many draws
    of the default in regime (iii)), against its limit law; and how much smaller the variance is with log-ratios than by
    counting.
(b) A survey of random actors, near and far from the ray: in what share knowing the log-ratios gives the smaller
    variance, by the size of the misalignment and of χ²(p°‖p), the reweighting the estimate hides.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from checks.common import tilt, simplex_interior                                   # noqa: E402
from checks.test_misalignment import misalignment                                   # noqa: E402
from checks.test_estimation import by_counts, by_log_ratios, by_two_samples        # noqa: E402


def var(g, d):
    return d @ g ** 2 - (d @ g) ** 2


def laws(p, q, F):
    M, ts = misalignment(p, q, F); po = tilt(q, ts * F); w = po / p
    return M, ts, po, w, var(np.log(w), p), var(w - np.log(w), p), var(po / q, q)


def main():
    r = np.random.default_rng(5202); R, n = 3000, 4000; found = 0
    print("(a) n·Var, simulated / predicted; and Var by counting over Var with log-ratios (predicted)")
    while found < 5:
        k = int(r.integers(3, 7)); q = simplex_interior(r, k); F = r.normal(0, 1, k); p = tilt(q, F + r.normal(0, 0.6, k))
        M, ts, po, w, vA, vB, vq = laws(p, q, F)
        if not (0 < ts < np.inf and M > 1e-3):
            continue
        found += 1; l = np.log(p / q)
        C = r.multinomial(n, p, size=R).astype(float); Cq = r.multinomial(n, q, size=R).astype(float)
        MA, tA = by_counts(C, q, F)
        print(f"  |X| = {k}, M = {M:.4f}, t* = {ts:.3f}: counts {n * MA.var():.4f} / {vA:.4f}; "
              f"log-ratios {n * by_log_ratios(C, l, F).var():.5f} / {vB:.5f}; "
              f"two samples {n * by_two_samples(C, Cq, l, F).var():.4f} / {vA + vq:.4f}; ratio {vA / vB:.1f}")
    print("(b) share of actors for which log-ratios give the smaller variance")
    rows = []
    while len(rows) < 4000:
        k = int(r.integers(3, 8)); q = simplex_interior(r, k); F = r.normal(0, 2, k)
        p = tilt(q, F + r.normal(0, r.uniform(0.1, 3.5), k))
        if p.min() < 1e-12:
            continue
        with np.errstate(all="ignore"):
            M, ts, po, w, vA, vB, vq = laws(p, q, F)
        if 0 < ts < np.inf and M > 0 and po.min() > 1e-12 and np.isfinite(vA / vB):
            rows.append((M, var(w, p), vA / vB))
    o = np.array(rows)
    for lo, hi in [(0, .01), (.01, .03), (.03, .1), (.1, .3), (.3, 1), (1, np.inf)]:
        s = o[(o[:, 0] >= lo) & (o[:, 0] < hi)]
        print(f"  M in [{lo}, {hi}): {len(s)} actors, log-ratios better in {np.mean(s[:, 2] > 1):.2f}, "
              f"median ratio {np.median(s[:, 2]):.2f}")
    for lo, hi in [(0, .5), (.5, 1), (1, 2), (2, np.inf)]:
        s = o[(o[:, 1] >= lo) & (o[:, 1] < hi)]
        print(f"  χ²(p°‖p) in [{lo}, {hi}): {len(s)} actors, log-ratios better in {np.mean(s[:, 2] > 1):.2f}")


if __name__ == "__main__":
    main()
