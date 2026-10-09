"""Misalignment under the standard specification of an objective, and the split of the departure ([P5], [P6]).

The standard specification of `F` is "pursue `F` from the default `q` at some intensity": its intended behaviours are
the pursuits p_{F,t} = tilt(q, t·F), t ≥ 0 ([D3]). The misalignment of a behaviour `p` is its KL divergence from the
nearest of them, reached at the revealed intensity t* ([P5](iv)); the departure KL(p‖q) splits into the pursuit part
KL(p°‖q) and the misalignment ([P6]).
"""
from dataclasses import dataclass
import numpy as np
from .core import as_distribution, as_objective, kl, tilt

DEFAULT, PURSUIT, BEST_OUTCOMES = "default", "pursuit", "best outcomes"     # the three cases of [P5](iv)


def _inputs(p, q, F):
    p = as_distribution(p, "p")
    q = as_distribution(q, "q", full_support=True)
    if q.size != p.size:
        raise ValueError(f"p and q must have the same outcomes: {p.size} and {q.size} masses")
    return p, q, as_objective(F, p.size)


def best_outcomes(q, F):
    """q conditioned on the outcomes where F is largest: the limit of the pursuit of F as t → ∞."""
    A = F >= F.max()
    return np.where(A, q, 0.0) / q[A].sum()


def _intensity(p, q, F):
    """t* of [P5](iv), without the checks of the public functions: 0 if E_p F ≤ E_q F; ∞ if E_p F = max F; otherwise
    the root of E_{p_{F,t}} F = E_p F, found by bisection, since E_{p_{F,t}} F increases with t."""
    target = p @ F
    if target <= q @ F:
        return 0.0
    if target >= F.max() - 1e-12 * (1 + np.abs(F).max()):
        return np.inf
    lo, hi = 0.0, 1.0
    while tilt(q, hi * F) @ F < target:
        hi *= 2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if tilt(q, mid * F) @ F < target else (lo, mid)
    return 0.5 * (lo + hi)


def _nearest(q, F, t):
    return best_outcomes(q, F) if np.isinf(t) else tilt(q, t * F)


def revealed_intensity(p, q, F):
    """The revealed intensity t* of `p` under the standard specification of `F` from `q` ([P5](iv)): 0, a positive
    number, or ∞ when `p` puts all its mass on the outcomes where `F` is largest. A constant `F` gives 0."""
    return _intensity(*_inputs(p, q, F))


def nearest_intended(p, q, F):
    """The nearest intended behaviour p°: `q` at t* = 0, p_{F,t*} for 0 < t* < ∞, and `q` conditioned on the best
    outcomes of `F` at t* = ∞, the limit of the ray, approached and not attained ([P5](iv))."""
    p, q, F = _inputs(p, q, F)
    return _nearest(q, F, _intensity(p, q, F))


def misalignment(p, q, F):
    """M(p), in nats, under the standard specification of `F` from `q` ([D3], [P5])."""
    p, q, F = _inputs(p, q, F)
    return kl(p, _nearest(q, F, _intensity(p, q, F)))


@dataclass(frozen=True)
class Assessment:
    """What `STANDARD.md` reports for a behaviour known exactly: misalignment, the revealed intensity and its case, the
    nearest intended behaviour, and the departure split into its pursuit part and misalignment ([P5], [P6])."""
    misalignment: float
    revealed_intensity: float
    case: str
    nearest: np.ndarray
    departure: float
    pursuit_part: float


def assess(p, q, F):
    """The `Assessment` of a behaviour `p` against the standard specification of `F` from the default `q`."""
    p, q, F = _inputs(p, q, F)
    t = _intensity(p, q, F)
    po = _nearest(q, F, t)
    M, departure = kl(p, po), kl(p, q)
    case = DEFAULT if t == 0 else BEST_OUTCOMES if np.isinf(t) else PURSUIT
    return Assessment(M, t, case, po, departure, kl(po, q))
