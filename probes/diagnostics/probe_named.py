"""Probe for the Notes of P44: outside small changes, the share of the departure that is pursuit ([P6]) is not the R² of
the revealed objective log(p/q) on F, under p or under q. Exploratory, not a check.

Random instances on 30 outcomes: a default q, an objective F, and a behaviour p = tilt(q, scale·H) whose revealed
objective H correlates with F (H = 0.4·F + noise). For each scale, the median departure, the median pursuit share
1 − M/KL(p||q), and the median gap between that share and the two R². Usage: python3 probes/diagnostics/probe_named.py
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from checks.common import kl, tilt, simplex_interior                                # noqa: E402
from checks.test_misalignment import misalignment                                  # noqa: E402


def r2(H, X, w):
    """The R² of H on X with an intercept, under the weights w."""
    A = np.column_stack([np.ones_like(H), X]); s = np.sqrt(w)
    beta = np.linalg.lstsq(A * s[:, None], H * s, rcond=None)[0]
    Hc = H - w @ H
    return 1 - (w @ (H - A @ beta) ** 2) / (w @ Hc ** 2)


def main():
    r = np.random.default_rng(4403)
    print("scale  departure  share  R²(p)  R²(q)  |share−R²(p)|  |share−R²(q)|   (medians over 200 instances)")
    for scale in (0.1, 0.5, 2.0, 5.0):
        rows = []
        for _ in range(200):
            n = 30; q = simplex_interior(r, n); F = r.normal(0, 1, n); H = 0.4 * F + r.normal(0, 1, n)
            p = tilt(q, scale * H); dep = kl(p, q); M, t = misalignment(p, q, F)
            if not np.isfinite(t) or dep < 1e-12:
                continue
            z = np.log(p / q); share = 1 - M / dep
            rows.append((dep, share, r2(z, F, p), r2(z, F, q)))
        a = np.median(np.array(rows), axis=0)
        gaps = np.median([[abs(x[1] - x[2]), abs(x[1] - x[3])] for x in rows], axis=0)
        print(f"{scale:5}  {a[0]:9.3f}  {a[1]:5.3f}  {a[2]:5.3f}  {a[3]:5.3f}  {gaps[0]:12.3f}  {gaps[1]:12.3f}")


if __name__ == "__main__":
    main()
