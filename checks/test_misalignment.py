"""Checks of P5: misalignment is attained for full-support behaviour, zero exactly on the closure of the intended set, at
most the departure from the reference when the reference is intended; and its closed form under the standard declaration
(the pursuit ray), in all three cases: below the reference, in between, and at the best outcomes."""
import numpy as np
from .common import EXACT, rng, simplex_interior, with_zeros, kl, tilt


def ray_minimizer(ph, q, F):
    """t* of P5(iv): 0 if E_ph F <= E_q F; inf if E_ph F = max F; otherwise the root of E_{p_t} F = E_ph F (bisection;
    E_{p_t} F increases in t)."""
    target = ph @ F
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


def best_outcomes_limit(q, F):
    """q conditioned on the outcomes where F is largest: the limit of the ray as t -> inf."""
    A = F >= F.max()
    return np.where(A, q, 0.0) / q[A].sum()


def misalignment(ph, q, F):
    ts = ray_minimizer(ph, q, F)
    return (kl(ph, best_outcomes_limit(q, F)) if np.isinf(ts) else kl(ph, tilt(q, ts * F))), ts


def test_minimum_on_the_ray_is_attained_at_the_closed_form():
    r = rng(401)
    for _ in range(300):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        ph = with_zeros(r, n) if r.random() < 0.3 else simplex_interior(r, n)
        if ph @ F >= F.max() - 1e-9:
            continue                                                              # the third case: its own check
        m, ts = misalignment(ph, q, F)
        assert 0 <= ts < np.inf                                                   # the minimizer is on the half-ray
        grid = np.concatenate([np.linspace(0, 2 * ts + 5, 2001), [10 * ts + 50]])
        values = np.array([kl(ph, tilt(q, t * F)) for t in grid])
        assert m <= values.min() + EXACT * (1 + m)                               # nothing on the grid does better
        assert values[-1] > m + 1e-6                                              # far along the ray is worse: attained
        if ts > 0:                                                                # first-order condition: means match
            assert abs(tilt(q, ts * F) @ F - ph @ F) <= 1e-9 * (1 + np.abs(F).max())
        else:
            assert ph @ F <= q @ F


def test_best_outcomes_case():
    """P5(iv), third case: behaviour on the best outcomes. KL decreases along the ray to KL(ph || q(.|best)), not attained;
    zero for a maximizer that splits ties as q does, positive for one that splits them differently."""
    r = rng(405)
    for _ in range(300):
        n = int(r.integers(3, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        top = np.argsort(F)[-2:]; F[top[0]] = F[top[1]]                           # two tied best outcomes
        A = F >= F.max(); gap = F.max() - F[~A].max(); lim = best_outcomes_limit(q, F)
        for ph, zero in ((lim, True), (np.eye(n)[top[1]], False)):               # ties as q splits them; one only
            m, ts = misalignment(ph, q, F)
            assert np.isinf(ts)
            assert (m <= EXACT) == zero
            path = [kl(ph, tilt(q, t * F)) for t in (0.0, 1.0, 5.0, 50.0 / gap)]
            assert all(a >= b - EXACT for a, b in zip(path, path[1:]))           # decreasing along the ray
            assert all(v >= m - EXACT for v in path)                              # never below the limit
            assert path[-1] - m <= (1 - q[A].sum()) / q[A].sum() * np.exp(-50.0) + EXACT   # and approaches it
        # a unique best outcome: the deterministic maximizer is aligned
        F2 = r.normal(0, 1, n); m, _ = misalignment(np.eye(n)[np.argmax(F2)], q, F2)
        assert m <= EXACT


def test_zero_exactly_on_the_intended_set():
    r = rng(402)
    for _ in range(300):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n); t0 = float(r.uniform(0, 3))
        on = tilt(q, t0 * F)
        assert misalignment(on, q, F)[0] <= 1e-9
        off = tilt(q, t0 * F + r.normal(0, 0.5, n))                             # a transverse departure
        if np.linalg.matrix_rank(np.stack([np.log(off / q) - np.log(off / q).mean(), F - F.mean()]), tol=1e-3) == 2:
            assert misalignment(off, q, F)[0] > 1e-6
        # a behaviour with zeros that is not on the closure of the ray is misaligned
        z = with_zeros(r, n)
        if np.abs(z - best_outcomes_limit(q, F)).sum() > 1e-3:
            assert misalignment(z, q, F)[0] > 1e-9


def test_bounded_by_departure_from_reference():
    r = rng(403)
    for _ in range(300):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        ph = with_zeros(r, n) if r.random() < 0.3 else simplex_interior(r, n)
        m, _ = misalignment(ph, q, F)
        assert m <= kl(ph, q) + EXACT * (1 + kl(ph, q))


def test_the_ray_leaves_every_compact_set():
    """P5(iv), closedness: the mass at an outcome where F is smallest obeys the bound, so it tends to 0 along the ray."""
    r = rng(404)
    for _ in range(300):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        lo, hi = int(np.argmin(F)), int(np.argmax(F)); osc = F[hi] - F[lo]
        for t in (0.0, 1.0, 10.0, 100.0):
            mass, bound = tilt(q, t * F)[lo], q[lo] / q[hi] * np.exp(-t * osc)
            assert mass <= bound * (1 + EXACT) + 1e-300
        # far enough along, as small as we like (the bound is tight for two outcomes: same relative margin as above)
        assert tilt(q, 100.0 / osc * F)[lo] <= q[lo] / q[hi] * np.exp(-100.0) * (1 + EXACT)
