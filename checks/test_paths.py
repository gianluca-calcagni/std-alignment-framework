"""Checks of P2 (every path is a replicator path; the replicator field is the Fisher gradient; the pursuit ray solves the
replicator flow) and P3 (a path keeps a fixed objective iff its log-increments stay in span{F, 1}, and pursues it iff the
coefficient on F is never negative).

Derivatives are taken by the complex step, f'(s) = Im f(s + ih) / h with h = 1e-30: exact to rounding for the analytic
paths used here, so the identities are checked at the EXACT tolerance, not at a finite-difference one."""
import numpy as np
from .common import EXACT, rng, simplex_interior, tilt

H = 1e-30


def softmax_c(z):
    z = z - z.real.max()
    return np.exp(z) / np.exp(z).sum()


def d(f, s):
    return np.imag(f(s + 1j * H)) / H


def moving_path(r, n):
    """p_s = softmax(a + s b + s^2 c): a path whose objective moves (b and c independent)."""
    a, b, c = r.normal(0, 1, n), r.normal(0, 1, n), r.normal(0, 0.5, n)
    return lambda s: softmax_c(a + s * b + s * s * c)


def test_replicator_form_of_any_path():
    r = rng(201)
    for _ in range(300):
        n = int(r.integers(2, 13)); p = moving_path(r, n); s = float(r.uniform(-2, 2))
        ps = p(s).real; dp = d(p, s); Fs = d(lambda u: np.log(p(u)), s)           # two independent derivatives
        assert abs(dp.sum()) <= EXACT
        assert np.max(np.abs(dp - ps * (Fs - ps @ Fs))) <= EXACT * (1 + np.abs(Fs).max())
        # unique up to a constant: F_s + c satisfies the equation, F_s + (non-constant) does not
        c = r.normal(0, 3)
        assert np.max(np.abs(dp - ps * ((Fs + c) - ps @ (Fs + c)))) <= EXACT * (1 + np.abs(Fs).max() + abs(c))
        G = Fs + r.normal(0, 1, n)
        assert np.max(np.abs(dp - ps * (G - ps @ G))) > 1e-8


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
    # constant F: the gradient is zero (the degenerate case the statement excludes from "fastest direction")
    p = simplex_interior(r, 5); F = np.full(5, 2.5)
    assert np.max(np.abs(p * (F - p @ F))) <= EXACT


def test_pursuit_ray_solves_the_replicator_flow():
    r = rng(204)
    for _ in range(300):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        path = lambda s: softmax_c(np.log(q) + s * F)
        for s in r.uniform(0, 4, 3):
            ps = path(s).real
            assert np.max(np.abs(d(path, s) - ps * (F - ps @ F))) <= EXACT * (1 + np.abs(F).max())
        assert np.max(np.abs(path(0.0).real - q)) <= EXACT                         # it starts at the reference


def residual_from_span(v, F):
    """Distance of v from span{F, 1}, relative to the size of v's non-constant part."""
    B = np.stack([F, np.ones_like(F)], 1)
    res = v - B @ np.linalg.lstsq(B, v, rcond=None)[0]
    return np.linalg.norm(res) / max(np.linalg.norm(v - v.mean()), 1e-300)


def coefficient_on(v, F):
    B = np.stack([F, np.ones_like(F)], 1)
    return np.linalg.lstsq(B, v, rcond=None)[0][0]


def test_fixed_objective_iff_span():
    r = rng(202)
    for _ in range(300):
        n = int(r.integers(3, 13)); p0 = simplex_interior(r, n); F = r.normal(0, 1, n)
        for tau, dtau, pursues in ((lambda s: s + 0.5 * np.sin(s), lambda s: 1 + 0.5 * np.cos(s), True),   # tau' > 0
                                   (lambda s: np.sin(s), lambda s: np.cos(s), False)):                  # tau' changes sign
            p = lambda s: softmax_c(np.log(p0) + tau(s) * F)
            coefs = []
            for s in np.linspace(-3, 3, 7):
                inc = d(lambda u: np.log(p(u)), s)
                assert residual_from_span(inc, F) <= EXACT                         # fixed objective: in the span
                a = coefficient_on(inc, F); coefs.append(a)
                assert abs(a - dtau(s)) <= EXACT * (1 + np.abs(F).max())           # the coefficient is tau'(s)
            assert (min(coefs) >= -EXACT) == pursues                               # pursues iff never negative
            s = float(r.uniform(0, 2))
            assert np.max(np.abs(p(s).real - tilt(p0, tau(s) * F))) <= EXACT
        # negative cases: a moving objective and a mixture of two behaviours both leave span{F_0, 1}, for F_0 the
        # objective at s = 0.2, by far more than rounding
        q1 = simplex_interior(r, n)
        for path in (moving_path(r, n), lambda s: (1 - s) * p0 + s * q1):
            F0 = d(lambda u: np.log(path(u)), 0.2)
            worst = max(residual_from_span(d(lambda u: np.log(path(u)), s), F0) for s in (0.5, 0.8))
            assert worst > 1e-3


def test_two_outcomes_always_keep_a_fixed_objective():
    """P3, Notes: with two outcomes span{F, 1} is every function, so even a moving path passes the fixed-objective test."""
    r = rng(205)
    for _ in range(200):
        path = moving_path(r, 2); F = r.normal(0, 1, 2)
        if abs(F[0] - F[1]) < 1e-3:
            continue
        for s in r.uniform(-2, 2, 3):
            assert residual_from_span(d(lambda u: np.log(path(u)), s), F) <= EXACT
