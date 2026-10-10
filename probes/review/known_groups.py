"""Does misalignment tell a wrong objective from an imperfect optimizer? (NOTES.md §15). Exploratory, not a check.
Usage: python3 probes/review/known_groups.py

Known groups, judged against the standard specification of the target F ([D3]) and against its ordinal specification
([P36]):
  A: best-of-n by F itself: the right objective, by a route that is not an exact tilt;
  B: the exact pursuit of a proxy F + noise·N(0, 1), at A's departure: the wrong objective, by the exact route;
  C: best-of-n by the proxy: the wrong objective, by the inexact route.
300 instances per row (|X| from 6 to 29, q from a flat Dirichlet, F standard normal), seed 20261011; an instance is
skipped when the proxy's pursuit cannot reach A's departure. Printed: the median misaligned share M/KL(p‖q) of each
group, and the AUC, the chance that a random member of B (or C) has the larger share than a random member of A; then the
same for the ordinal share. An AUC near 1 separates; 0.5 does not; below 0.5 ranks the groups the wrong way round.
The ordinal share of A is 0 by [P36](i); what the probe adds is how the standard share ranks A against B.
"""
import sys
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
sys.path.insert(0, str(Path(__file__).resolve().parents[1].parent))
import stdalign as sa                                                                # noqa: E402
from probes.review.faithful_optimizers import isotonic                              # noqa: E402


def best_of_n(q, F, n):
    """Best of n draws of q by F, for F with no ties."""
    o = np.argsort(F, kind="stable"); A = np.concatenate([[0], np.cumsum(q[o])]); p = np.zeros_like(q)
    p[o] = A[1:] ** n - A[:-1] ** n
    return p


def auc(x, y):
    """The chance that a member of y exceeds a member of x, ties counted half."""
    x, y = np.asarray(x), np.asarray(y)
    return float(np.mean(y[:, None] > x[None, :]) + 0.5 * np.mean(y[:, None] == x[None, :]))


def ordinal_misalignment(p, q, F):
    """M_ord of [P36](ii), for F with no ties."""
    o = np.argsort(F); po = q.copy(); po[o] = q[o] * isotonic(p[o] / q[o], q[o])
    return sa.kl(p, po)


def main():
    rng = np.random.default_rng(20261011)
    for noise in (0.3, 0.7):
        for n in (4, 16):
            a, b, c, a_ord, b_ord = [], [], [], [], []
            for _ in range(300):
                K = int(rng.integers(6, 30)); q = rng.dirichlet(np.ones(K)); F = rng.normal(size=K)
                P = F + noise * rng.normal(size=K)
                pa = best_of_n(q, F, n); d = sa.kl(pa, q)
                if d >= -np.log(q[P >= P.max()].sum()) or sa.kl(sa.pursuit(q, P, 1e3), q) < d:
                    continue
                t = brentq(lambda t: sa.kl(sa.pursuit(q, P, t), q) - d, 0, 1e3)
                pb = sa.pursuit(q, P, t); pc = best_of_n(q, P, n)
                a.append(sa.misalignment(pa, q, F) / d); b.append(sa.misalignment(pb, q, F) / sa.kl(pb, q))
                c.append(sa.misalignment(pc, q, F) / sa.kl(pc, q))
                a_ord.append(ordinal_misalignment(pa, q, F) / d); b_ord.append(ordinal_misalignment(pb, q, F) / sa.kl(pb, q))
            print(f"proxy noise {noise}, n={n:2d} ({len(a)} instances): standard share, median A {np.median(a):.3f}, "
                  f"B {np.median(b):.3f}, C {np.median(c):.3f}; AUC A vs B {auc(a, b):.2f}, A vs C {auc(a, c):.2f}. "
                  f"Ordinal share: A at most {np.max(a_ord):.1e}, B median {np.median(b_ord):.3f}; AUC A vs B "
                  f"{auc(a_ord, b_ord):.2f}")


if __name__ == "__main__":
    main()
