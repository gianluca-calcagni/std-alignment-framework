"""Edges of the library `stdalign` 0.2 found in the review of 2026-10-10 (NOTES.md §15). Exploratory, not a check.
Usage: python3 probes/review/library_edges.py [infinite | boundary | counts | log-ratios]   (all four by default)

infinite    An actor that puts mass e/2, e/2 and 1 − e on outcomes with F = 0, 1, 2 (q = 0.25, 0.25, 0.5) has full
            support, so its misalignment is attained and finite ([P5](i)). The library takes the third case of
            [P5](iv) whenever E_p[F] is within 1e-12·(1 + max|F|) of max F, and returns M = ∞ there. Compared with a
            minimum over a fine grid of intensities. A second of run time.
boundary    The χ² reference of [P23] holds at an interior intensity; at t = 0 the limit is a χ̄² mixture (its Notes).
            `from_counts` returns the χ²(|X| − 2) p-value at every intensity. Its rejection rate at a nominal 5%, for
            actors on the ray at t = 0, 0.05 and 0.5, with |X| = 3, 5, 10, n = 2000, 4000 samples; and the rate of the
            mixture ½χ²(|X| − 2) + ½χ²(|X| − 1). Seed 7. About two minutes.
counts      Coverage of `from_counts`' 95% interval ([P52](i)) off the ray, as M shrinks below the plug-in's bias,
            about (|X| − 2)/(2n): |X| = 10, n = 500 to 10,000, 2000 samples. Seed 11. A few minutes.
log-ratios  Coverage of `from_log_ratios`' 95% interval ([P52](ii)) by distance from the ray and number of draws:
            |X| = 50, n = 32 (W3's and W4's draws per context), 128 and 1024, 2000 samples. Seed 12. A few minutes.
"""
import sys
from pathlib import Path
import numpy as np
from scipy.stats import chi2
sys.path.insert(0, str(Path(__file__).resolve().parents[1].parent))
import stdalign as sa                                                                # noqa: E402


def infinite():
    q = np.array([0.25, 0.25, 0.5]); F = np.array([0.0, 1.0, 2.0]); ts = np.logspace(-2, 3, 20001)
    for e in (1e-6, 1e-10, 1e-12, 1e-13, 1e-14):
        p = np.array([e / 2, e / 2, 1 - e])
        with np.errstate(over="ignore"):
            a = sa.assess(p, q, F)
        with np.errstate(over="ignore"):
            grid = [sa.kl(p, sa.pursuit(q, F, t)) for t in ts]
        print(f"e = {e:g}: library M = {a.misalignment:.6g} (t* = {a.revealed_intensity:.4g}, {a.case}); "
              f"least over the grid {min(grid):.6g}, at t = {ts[int(np.argmin(grid))]:.4g}")


def boundary():
    rng = np.random.default_rng(7)
    for K in (3, 5, 10):
        q = rng.dirichlet(np.ones(K) * 3); F = rng.normal(size=K)
        for t in (0.0, 0.05, 0.5):
            p = sa.pursuit(q, F, t); n = 2000; R = 4000; rej = rej_bar = 0
            for _ in range(R):
                e = sa.from_counts(rng.multinomial(n, p), q, F)
                rej += e.chi2_p_value < 0.05
                s = e.chi2_statistic
                rej_bar += 0.5 * chi2.sf(s, K - 2) + 0.5 * chi2.sf(s, K - 1) < 0.05
            print(f"|X| = {K:2d}, t = {t:4.2f}: rejected at 5% by χ²(|X| − 2) {rej / R:.3f}; by the χ̄² mixture "
                  f"{rej_bar / R:.3f}")


def counts():
    rng = np.random.default_rng(11)
    K = 10; q = rng.dirichlet(np.ones(K) * 3); F = rng.normal(size=K); G = rng.normal(size=K)
    for eps in (0.6, 0.3, 0.15, 0.07):
        p = sa.tilt(q, 0.8 * F + eps * G); M = sa.misalignment(p, q, F)
        for n in (500, 2000, 10000):
            cov = 0; bias = []; R = 2000
            for _ in range(R):
                e = sa.from_counts(rng.multinomial(n, p), q, F)
                cov += e.interval[0] <= M <= e.interval[1]; bias.append(e.value - M)
            print(f"M = {M:.4f}, n = {n:5d}: coverage {cov / R:.3f}; mean bias {np.mean(bias):+.4f} "
                  f"((|X| − 2)/2n = {(K - 2) / (2 * n):.4f})")


def log_ratios():
    rng = np.random.default_rng(12)
    K = 50; q = rng.dirichlet(np.ones(K)); F = rng.normal(size=K); G = rng.normal(size=K)
    for eps in (0.1, 0.4, 1.0, 2.0):
        p = sa.tilt(q, 1.0 * F + eps * G); M = sa.misalignment(p, q, F); ell = np.log(p / q)
        for n in (32, 128, 1024):
            cov = 0; R = 2000; vals = []
            for _ in range(R):
                x = rng.choice(K, n, p=p); e = sa.from_log_ratios(ell[x], F[x])
                cov += e.interval[0] <= M <= e.interval[1]; vals.append(e.value)
            print(f"M = {M:.3f}, n = {n:5d}: coverage {cov / R:.3f}, mean estimate {np.mean(vals):.3f}")


if __name__ == "__main__":
    probes = {"infinite": infinite, "boundary": boundary, "counts": counts, "log-ratios": log_ratios}
    for name in sys.argv[1:] or probes:
        print(f"-- {name}")
        probes[name]()
