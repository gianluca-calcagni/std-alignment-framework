"""Checks of P10: a wrong default moves misalignment by at most the spread of the log-ratio between defaults; an error in
the objective moves it by at most the error's spread times the revealed intensity."""
import numpy as np
from .common import EXACT, rng, simplex_interior, with_zeros, kl, tilt
from .test_misalignment import misalignment


def test_default_error_moves_misalignment_by_at_most_its_spread():
    r = rng(701); ratios = []
    for _ in range(800):
        n = int(r.integers(2, 10)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        ph = with_zeros(r, n) if r.random() < 0.3 else simplex_interior(r, n)
        q2 = tilt(q, r.normal(0, float(r.uniform(0.01, 1)), n)); spread = np.ptp(np.log(q2 / q))
        d = abs(misalignment(ph, q2, F)[0] - misalignment(ph, q, F)[0])
        assert d <= spread * (1 + 1e-9) + 1e-12
        ratios.append(d / spread)
    assert max(ratios) > 0.9                                                    # the bound is nearly attained


def test_objective_error_matters_in_proportion_to_intensity():
    r = rng(702); used = 0
    for _ in range(800):
        n = int(r.integers(2, 10)); q = simplex_interior(r, n); F = r.normal(0, 1, n)
        g = r.normal(0, float(r.uniform(0.01, 0.5)), n); ph = simplex_interior(r, n)
        M1, t1 = misalignment(ph, q, F); M2, t2 = misalignment(ph, q, F + g)
        if np.isfinite(t1):
            assert M2 <= M1 + t1 * np.ptp(g) + 1e-9 * (1 + M1); used += 1
        if np.isfinite(t2):
            assert M1 <= M2 + t2 * np.ptp(g) + 1e-9 * (1 + M2)
    assert used >= 500
    # the general step: for any r, h, |KL(p || tilt(r, h)) - KL(p || r)| <= osc(h)
    for _ in range(500):
        n = int(r.integers(2, 10)); rr = simplex_interior(r, n); h = r.normal(0, 2, n)
        p = with_zeros(r, n) if r.random() < 0.3 else simplex_interior(r, n)
        assert abs(kl(p, tilt(rr, h)) - kl(p, rr)) <= np.ptp(h) * (1 + 1e-12) + EXACT
