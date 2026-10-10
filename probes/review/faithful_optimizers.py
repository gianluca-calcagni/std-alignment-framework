"""What misalignment charges to optimizers of the right objective (NOTES.md §15). Exploratory, not a check.
Usage: python3 probes/review/faithful_optimizers.py

200 random instances (|X| from 4 to 20, q from a flat Dirichlet, F standard normal), seed 20261010. Two optimizers that
pursue the TRUE objective F, with no proxy at all, by a route that is not an exact tilt:
(a) vanilla policy gradient on softmax logits for E_p[F], exact gradient, step 0.01, no KL term, from q;
(b) best-of-n by F (F is continuous, so there are no ties).
Printed: the departure KL(p‖q), the misalignment M under the standard specification of F ([D3], [P5]) and the misaligned
share M/KL(p‖q); and, for (a) at step 1600, the share under the ordinal specification of F ([P36]).
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1].parent))
import stdalign as sa                                                                # noqa: E402


def best_of_n(q, F, n):
    """The law of the best of n draws of q by F, ties split as q splits them ([P36](i))."""
    order = np.argsort(F); qs = q[order]; Fs = F[order]
    p = np.zeros_like(q); A = 0.0; i = 0
    while i < len(Fs):
        j = i
        while j + 1 < len(Fs) and Fs[j + 1] == Fs[i]:
            j += 1
        mass = qs[i:j + 1].sum(); new = A + mass
        p[order[i:j + 1]] = (new ** n - A ** n) * qs[i:j + 1] / mass
        A = new; i = j + 1
    return p


def isotonic(y, w):
    """Weighted least-squares non-decreasing fit of y with weights w (pool adjacent violators)."""
    out = []
    for b in ([y[i] * w[i], w[i], 1] for i in range(len(y))):
        out.append(b)
        while len(out) > 1 and out[-2][0] / out[-2][1] > out[-1][0] / out[-1][1]:
            s, ww, k = out.pop(); out[-1][0] += s; out[-1][1] += ww; out[-1][2] += k
    return np.concatenate([[s / ww] * k for s, ww, k in out])


def ordinal_misalignment(p, q, F):
    """M_ord of [P36](ii): KL(p‖q·r°), r° the q-weighted isotonic regression of the level ratios on the order of F."""
    levels = np.unique(F); idx = np.searchsorted(levels, F)
    pL, qL = np.bincount(idx, p), np.bincount(idx, q)
    return sa.kl(p, q * isotonic(pL / qL, qL)[idx])


def main():
    rng = np.random.default_rng(20261010)
    rows_pg, rows_bon, ordinal = [], [], []
    for _ in range(200):
        K = rng.integers(4, 21)
        q = rng.dirichlet(np.ones(K)); F = rng.normal(size=K)
        th = np.log(q).copy()
        for step in range(1, 4001):
            p = np.exp(th - th.max()); p /= p.sum()
            th += 0.01 * p * (F - p @ F)
            if step in (100, 400, 1600, 4000):
                a = sa.assess(p, q, F)
                rows_pg.append((step, a.departure, a.misalignment))
            if step == 1600:
                ordinal.append(ordinal_misalignment(p, q, F) / sa.kl(p, q))
        for n in (2, 4, 16, 64):
            a = sa.assess(best_of_n(q, F, n), q, F)
            rows_bon.append((n, a.departure, a.misalignment))
    for name, rows in (("vanilla PG (step)", rows_pg), ("best-of-n (n)", rows_bon)):
        r = np.array(rows)
        for k in np.unique(r[:, 0]):
            s = r[r[:, 0] == k]; share = s[:, 2] / s[:, 1]
            print(f"{name} {int(k):5d}: median departure {np.median(s[:, 1]):.3f} nats, median M {np.median(s[:, 2]):.4f}, "
                  f"misaligned share median {np.median(share):.3f} (90th percentile {np.quantile(share, .9):.3f})")
    print(f"vanilla PG at step 1600, share under the ordinal specification: median {np.median(ordinal):.4f}, "
          f"max {np.max(ordinal):.4f}")


if __name__ == "__main__":
    main()
