"""Shared helpers for the checks.

Tolerance. The checked identities are exact; the instances have at most 12 outcomes and log-ratios of order 10, so a
sum computed in float64 carries a rounding error of order 12 * 10 * 2.2e-16, about 3e-14. EXACT = 1e-10 leaves a margin
of more than 1000 above that, and stays far below the gaps the negative checks require (at least 1e-3).
"""
import numpy as np

EXACT = 1e-10


def rng(seed):
    return np.random.default_rng(seed)


def simplex_interior(r, n):
    """A random full-support distribution on n outcomes, with some small masses (down to about 1e-3)."""
    p = r.dirichlet(np.full(n, 0.7))
    p = np.maximum(p, 1e-3)
    return p / p.sum()


def with_zeros(r, n):
    """A random distribution on n outcomes with at least one zero mass and at least one positive mass."""
    p = r.dirichlet(np.ones(n))
    p[r.choice(n, size=r.integers(1, n), replace=False)] = 0.0
    return p / p.sum()


def kl(p, r):
    """KL(p || r) in nats, for r of full support; terms with p(x) = 0 contribute 0."""
    m = p > 0
    return float(np.sum(p[m] * np.log(p[m] / r[m])))


def tilt(r, F):
    """The tilt of r by F: r * exp(F), normalized. Computed with the maximum subtracted, so large F does not overflow."""
    w = np.log(r) + F
    w = np.exp(w - w.max())
    return w / w.sum()


def random_partition(r, n):
    """Cell labels 0..k-1 for a random partition of n outcomes into k >= 2 non-empty cells."""
    k = int(r.integers(2, n))
    labels = np.concatenate([np.arange(k), r.integers(0, k, n - k)])
    return r.permutation(labels)


def coarse(p, labels):
    return np.array([p[labels == c].sum() for c in range(labels.max() + 1)])


def log_normalizer(q, c):
    """Λ(c) = log E_q[e^c], computed stably."""
    w = np.log(q) + c
    m = w.max()
    return float(m + np.log(np.exp(w - m).sum()))


def kl_tilts(q, a, b):
    """KL(tilt(q, a) || tilt(q, b)) = E_{p_a}[a - b] - Λ(a) + Λ(b): finite and accurate even where the tilts underflow."""
    return float(tilt(q, a) @ (a - b) - log_normalizer(q, a) + log_normalizer(q, b))
