"""Primitives on finite outcomes: KL divergence, tilts and log-normalizers ([D1], [D2], [A4] of CORE.md).

These are the building blocks every other quantity is computed from. They are kept lean: they assume their inputs are
already arrays of the right shape (see `as_distribution` and `as_objective` for the checks done at the entry points of
the library), and they are written in log space where an exponential could overflow.
"""
import numpy as np

SUM_TOLERANCE = 1e-9          # a distribution's masses may miss 1 by this much per outcome (rounding of normalized input)


def as_distribution(p, name="p", full_support=False):
    """`p` as a float array, after checking that it is a distribution on finitely many outcomes.

    Raises ValueError, naming `name`, if `p` is not one-dimensional, has a mass that is negative or not finite, does not
    sum to 1 within `SUM_TOLERANCE` per outcome, or, with `full_support`, has a zero mass."""
    p = np.asarray(p, dtype=float)
    if p.ndim != 1 or p.size == 0:
        raise ValueError(f"{name} must be a one-dimensional array of masses, one per outcome")
    if not np.all(np.isfinite(p)) or np.any(p < 0):
        raise ValueError(f"{name} has a mass that is negative or not finite")
    if abs(p.sum() - 1.0) > SUM_TOLERANCE * p.size:
        raise ValueError(f"{name} sums to {p.sum()!r}, not 1")
    if full_support and np.any(p == 0):
        raise ValueError(f"{name} must give every outcome a positive mass")
    return p


def as_objective(F, n, name="F"):
    """`F` as a float array of one finite value per outcome, after checking its shape against `n` outcomes."""
    F = np.asarray(F, dtype=float)
    if F.shape != (n,):
        raise ValueError(f"{name} must have one value per outcome: shape ({n},), not {F.shape}")
    if not np.all(np.isfinite(F)):
        raise ValueError(f"{name} has a value that is not finite")
    return F


def _log(r):
    """log r, with log 0 = −∞ and no warning; the common case of full support takes the fast path."""
    r = np.asarray(r, dtype=float)
    if r.min() > 0:
        return np.log(r)
    with np.errstate(divide="ignore"):
        return np.log(r)


def kl(p, r):
    """KL(p‖r) in nats; outcomes with p(x) = 0 contribute 0, and the divergence is infinite if r(x) = 0 < p(x)."""
    p, r = np.asarray(p, dtype=float), np.asarray(r, dtype=float)
    m = p > 0
    pm, rm = p[m], r[m]
    if rm.min() <= 0:
        return float("inf")
    return float(np.sum(pm * np.log(pm / rm)))


def tilt(r, F):
    """The tilt of `r` by `F`: r·e^F, normalized ([D2]). Computed with the maximum subtracted, so a large `F` does not
    overflow; outcomes with r(x) = 0 keep mass 0."""
    w = _log(r) + F
    w = np.exp(w - w.max())
    return w / w.sum()


def pursuit(q, F, t):
    """The pursuit of `F` from the default `q` at intensity `t`: p_{F,t} = tilt(q, t·F) ([D2])."""
    return tilt(q, t * np.asarray(F, dtype=float))


def log_normalizer(q, c):
    """Λ(c) = log E_q[e^c], computed stably."""
    w = _log(q) + c
    m = w.max()
    return float(m + np.log(np.exp(w - m).sum()))


def kl_tilts(q, a, b):
    """KL(tilt(q, a) ‖ tilt(q, b)) = E_{p_a}[a − b] − Λ(a) + Λ(b): finite and accurate even where the tilts underflow."""
    return float(tilt(q, a) @ (a - b) - log_normalizer(q, a) + log_normalizer(q, b))


def log_mean_exp(a):
    """log of the average of e^a over a one-dimensional array, computed stably."""
    a = np.asarray(a, dtype=float)
    m = a.max()
    return float(m + np.log(np.mean(np.exp(a - m))))
