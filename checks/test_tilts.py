"""Checks of P1: every full-support behaviour is a tilt of any other, with an objective unique up to a constant."""
import numpy as np
from .common import EXACT, rng, simplex_interior, tilt


def test_every_behaviour_is_a_tilt():
    r = rng(101)
    for _ in range(500):
        n = int(r.integers(2, 13)); q, p = simplex_interior(r, n), simplex_interior(r, n)
        assert np.max(np.abs(tilt(q, np.log(p / q)) - p)) <= EXACT


def test_tilt_objective_unique_up_to_constant():
    r = rng(102)
    for _ in range(500):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F = r.normal(0, 3, n); c = r.normal(0, 5)
        # adding a constant changes nothing ...
        assert np.max(np.abs(tilt(q, F + c) - tilt(q, F))) <= EXACT
        # ... and the objective is recovered from the tilt up to a constant: log(p/q) - F is constant
        d = np.log(tilt(q, F) / q) - F
        assert np.ptp(d) <= EXACT * (1 + np.abs(F).max())
        # a non-constant change of objective changes the tilt (the negative case): log(tilt_G / tilt_F) = G - F + const,
        # so its spread equals the spread of G - F, which is at least 1e-2 here
        G = F + r.normal(0, 1, n)
        if np.ptp(G - F) > 1e-2:
            assert np.ptp(np.log(tilt(q, G) / tilt(q, F))) > 1e-2 - EXACT


def test_tilts_compose():
    r = rng(103)
    for _ in range(500):
        n = int(r.integers(2, 13)); q = simplex_interior(r, n); F, G = r.normal(0, 2, n), r.normal(0, 2, n)
        assert np.max(np.abs(tilt(tilt(q, F), G) - tilt(q, F + G))) <= EXACT
        assert np.max(np.abs(tilt(q, np.zeros(n)) - q)) <= EXACT
