"""Checks of P4: misalignment is attained, zero exactly on the intended set, at most the departure from the reference when
the reference is intended; and its closed form under the standard declaration (the pursuit ray)."""
import numpy as np
from .common import EXACT, rng, simplex_interior, kl, tilt


def ray_minimizer(ph, q, F):
    """t* of P4(iv): 0 if E_ph F <= E_q F, else the root of E_{p_t} F = E_ph F (bisection; E_{p_t} F increases in t)."""
    target = ph @ F
    if target <= q @ F:
        return 0.0
    lo, hi = 0.0, 1.0
    while tilt(q, hi * F) @ F < target:
        hi *= 2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if tilt(q, mid * F) @ F < target else (lo, mid)
    return 0.5 * (lo + hi)


def test_minimum_on_the_ray_is_attained_at_the_closed_form():
    r = rng(401)
    for _ in range(300):
        n = int(r.integers(2, 13)); q, ph = simplex_interior(r, n), simplex_interior(r, n); F = r.normal(0, 1, n)
        ts = ray_minimizer(ph, q, F); m = kl(ph, tilt(q, ts * F))
        assert ts >= 0                                                            # the minimizer is on the half-ray
        grid = np.concatenate([np.linspace(0, 2 * ts + 5, 2001), [10 * ts + 50]])
        values = np.array([kl(ph, tilt(q, t * F)) for t in grid])
        assert m <= values.min() + EXACT * (1 + m)                               # nothing on the grid does better
        assert values[-1] > m + 1e-6                                              # far along the ray is worse: attained
        # first-order condition: at an interior minimum the means match; at t* = 0 the actual mean is not above q's
        if ts > 0:
            assert abs(tilt(q, ts * F) @ F - ph @ F) <= 1e-9 * (1 + np.abs(F).max())
        else:
            assert ph @ F <= q @ F


def test_zero_exactly_on_the_intended_set():
    r = rng(402)
    for _ in range(300):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n); t0 = float(r.uniform(0, 3))
        on = tilt(q, t0 * F)
        assert kl(on, tilt(q, ray_minimizer(on, q, F) * F)) <= 1e-9
        off = tilt(q, t0 * F + r.normal(0, 0.5, n))                             # a transverse departure
        if np.linalg.matrix_rank(np.stack([np.log(off / q) - np.log(off / q).mean(), F - F.mean()]), tol=1e-3) == 2:
            assert kl(off, tilt(q, ray_minimizer(off, q, F) * F)) > 1e-6


def test_bounded_by_departure_from_reference():
    r = rng(403)
    for _ in range(300):
        n = int(r.integers(2, 13)); q, ph = simplex_interior(r, n), simplex_interior(r, n); F = r.normal(0, 1, n)
        m = kl(ph, tilt(q, ray_minimizer(ph, q, F) * F))
        assert m <= kl(ph, q) + EXACT * (1 + kl(ph, q))


def test_the_ray_leaves_every_compact_set():
    """P4(iv), closedness: the mass at an outcome where F is smallest obeys the bound, so it tends to 0 along the ray."""
    r = rng(404)
    for _ in range(300):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        lo, hi = int(np.argmin(F)), int(np.argmax(F)); osc = F[hi] - F[lo]
        for t in (0.0, 1.0, 10.0, 100.0):
            mass, bound = tilt(q, t * F)[lo], q[lo] / q[hi] * np.exp(-t * osc)
            assert mass <= bound * (1 + EXACT) + 1e-300
        # far enough along, as small as we like (the bound is tight for two outcomes: same relative margin as above)
        assert tilt(q, 100.0 / osc * F)[lo] <= q[lo] / q[hi] * np.exp(-100.0) * (1 + EXACT)
