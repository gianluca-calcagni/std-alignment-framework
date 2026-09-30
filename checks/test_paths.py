"""Checks of P2: every path of behaviours is a pursuit with a moving objective; the objective is fixed iff the
log-increments stay in span{F, 1}; for a fixed objective, the replicator field is the Fisher gradient of E_p F.

Derivatives are taken by the complex step, f'(t) = Im f(t + ih) / h with h = 1e-30: exact to rounding for the
analytic paths used here, so the identities are checked at the EXACT tolerance, not at a finite-difference one."""
import numpy as np
from .common import EXACT, rng, simplex_interior, tilt

H = 1e-30


def softmax_c(z):
    z = z - z.real.max()
    return np.exp(z) / np.exp(z).sum()


def d(f, t):
    return np.imag(f(t + 1j * H)) / H


def moving_path(r, n):
    """p_t = softmax(a + t b + t^2 c): a path whose objective moves (b and c independent)."""
    a, b, c = r.normal(0, 1, n), r.normal(0, 1, n), r.normal(0, 0.5, n)
    return lambda t: softmax_c(a + t * b + t * t * c)


def test_replicator_form_of_any_path():
    r = rng(201)
    for _ in range(300):
        n = int(r.integers(2, 13)); p = moving_path(r, n); t = float(r.uniform(-2, 2))
        pt = p(t).real; dp = d(p, t); Ft = d(lambda s: np.log(p(s)), t)          # two independent derivatives
        assert abs(dp.sum()) <= EXACT
        assert np.max(np.abs(dp - pt * (Ft - pt @ Ft))) <= EXACT * (1 + np.abs(Ft).max())
        # unique up to a constant: F_t + c satisfies the equation, F_t + (non-constant) does not
        c = r.normal(0, 3)
        assert np.max(np.abs(dp - pt * ((Ft + c) - pt @ (Ft + c)))) <= EXACT * (1 + np.abs(Ft).max() + abs(c))
        G = Ft + r.normal(0, 1, n)
        assert np.max(np.abs(dp - pt * (G - pt @ G))) > 1e-8


def residual_from_span(v, F):
    """Distance of v from span{F, 1}, relative to the size of v's non-constant part."""
    B = np.stack([F, np.ones_like(F)], 1)
    res = v - B @ np.linalg.lstsq(B, v, rcond=None)[0]
    return np.linalg.norm(res) / max(np.linalg.norm(v - v.mean()), 1e-300)


def test_fixed_objective_iff_span():
    r = rng(202)
    for _ in range(300):
        n = int(r.integers(3, 13)); p0 = simplex_interior(r, n); F = r.normal(0, 1, n)
        tau = lambda t: t + 0.5 * np.sin(t)                                      # tau' = 1 + 0.5 cos t > 0
        p = lambda t: softmax_c(np.log(p0) + tau(t) * F)
        for t in r.uniform(-3, 3, 4):
            inc = d(lambda s: np.log(p(s)), t)
            assert residual_from_span(inc, F) <= EXACT
            B = np.stack([F, np.ones(n)], 1); a = np.linalg.lstsq(B, inc, rcond=None)[0][0]
            assert abs(a - (1 + 0.5 * np.cos(t))) <= EXACT * (1 + np.abs(F).max())   # the coefficient is tau'(t) > 0
        # a path through the same p_0 as a tilt must match the closed form
        t = float(r.uniform(0, 2))
        assert np.max(np.abs(p(t).real - tilt(p0, tau(t) * F))) <= EXACT
        # negative cases: a moving objective and a mixture of two behaviours both leave span{F_0, 1} for F_0 = the
        # objective at t = 0, by far more than rounding
        q1 = simplex_interior(r, n)
        for path in (moving_path(r, n), lambda s: (1 - s) * p0 + s * q1):
            F0 = d(lambda s: np.log(path(s)), 0.2)
            worst = max(residual_from_span(d(lambda s: np.log(path(s)), t), F0) for t in (0.5, 0.8))
            assert worst > 1e-3


def test_replicator_is_fisher_gradient():
    r = rng(203)
    for _ in range(300):
        n = int(r.integers(2, 13)); p = simplex_interior(r, n); F = r.normal(0, 2, n)
        v = p * (F - p @ F); fisher = lambda u, w: np.sum(u * w / p)
        norm_v = np.sqrt(fisher(v, v))
        for _ in range(20):
            u = r.normal(0, 1, n); u -= u.mean()                                  # a tangent direction: sum u = 0
            assert abs(fisher(v, u) - F @ u) <= EXACT * (1 + np.abs(F).max() * np.abs(u).sum())
            u /= np.sqrt(fisher(u, u))
            assert F @ u <= norm_v + EXACT * (1 + norm_v)                          # no unit direction climbs faster
        assert abs(F @ (v / norm_v) - norm_v) <= EXACT * (1 + norm_v)              # and v's direction attains it
