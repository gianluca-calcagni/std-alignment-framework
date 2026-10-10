"""Tests of the diagnostics' interface: their checks on inputs, and the identities a report relies on, on a few
instances. The items' claims are tested in checks/test_diagnostics.py, on this same code."""
import numpy as np
import pytest
import stdalign as sa

R = np.random.default_rng(9101)


def instance(k=6):
    q = R.dirichlet(np.ones(k)); F = R.normal(0, 1, k)
    return sa.tilt(q, 0.8 * F + R.normal(0, 0.7, k)), q, F


def test_the_splits_add_up():
    for _ in range(20):
        p, q, F = instance()
        G = R.normal(0, 1, p.size)
        unexplained, named = sa.named_split(p, q, F, [G])                     # [P44](ii)
        assert unexplained + named == pytest.approx(sa.misalignment(p, q, F), rel=1e-7, abs=1e-10)
        least, most = sa.uncertain_target_interval(p, q, np.vstack([F, G]))   # [P48](iii): every principal in the span
        for c in R.normal(0, 1, (5, 2)):
            M = sa.misalignment(p, q, c[0] * F + c[1] * G)
            assert least - 1e-9 <= M <= most + 1e-9
        terms = sa.intensity_terms(p, q, F)                                   # [P43](i)
        for t in (0.0, 0.5, 2.0):
            assert sum(terms.at(t)) == pytest.approx(sa.kl(p, sa.pursuit(q, F, t)), rel=1e-9, abs=1e-12)


def test_runs_and_conditions():
    ps = [instance()[0] for _ in range(3)]; w = np.array([0.2, 0.3, 0.5])
    D, pbar = sa.drift(ps, w)                                                 # [P45]
    assert 0 <= D <= -(w @ np.log(w)) and np.allclose(pbar, sum(a * b for a, b in zip(w, ps)))
    assert sa.drift([ps[0], ps[0]], [0.5, 0.5])[0] == pytest.approx(0, abs=1e-15)
    rep, spec = sa.condition_split(ps, ps[::-1], w)                           # [P46](i)
    avg = sum(a * sa.kl(u, e) for a, e, u in zip(w, ps, ps[::-1]))
    assert rep + spec == pytest.approx(avg, rel=1e-9)
    with pytest.raises(ValueError, match="weight"):
        sa.drift(ps, [0.5, 0.5])
    with pytest.raises(ValueError, match="frequencies"):
        sa.shared_intensity(ps, ps, [np.ones(6)] * 3, [0.5, 0.5])


def test_one_shared_intensity_costs_nothing_when_the_intensities_agree():
    k = 5; qs = [R.dirichlet(np.ones(k)) for _ in range(3)]; F = R.normal(0, 1, k)
    s = sa.shared_intensity([sa.pursuit(qc, F, 1.2) for qc in qs], qs, [F] * 3, [0.3, 0.3, 0.4])
    assert s.misalignment == pytest.approx(0, abs=1e-9) and abs(s.excess) <= 1e-9
    s = sa.shared_intensity([sa.pursuit(qc, F, t) for qc, t in zip(qs, (0.3, 1.0, 3.0))], qs, [F] * 3, [0.3, 0.3, 0.4])
    assert s.own == pytest.approx(0, abs=1e-9) and s.excess > 1e-4


def test_tampering_of_a_grounded_behaviour_is_zero_and_the_bounds_hold():
    W, S = 3, 4
    qW = R.dirichlet(np.ones(W)); K = R.dirichlet(np.ones(S), size=W); Fh = R.normal(0, 1, S)
    g = sa.grounded_pursuit(qW, K, Fh, 1.5)                                  # [P50](iv): grounded
    assert sa.tampering(g, K) == pytest.approx(0, abs=1e-12)
    p = R.dirichlet(np.ones(W * S)).reshape(W, S)
    L, gap, _ = sa.least_tampering(p.sum(0), K)                               # [P51](i), (ii)
    assert L - gap - 1e-12 <= sa.tampering(p, K) <= sa.most_tampering(p.sum(0), K) + 1e-12
    honest, channel, again = sa.remeasured(g, K, Fh, qW)                     # [P51](iv): no channel gain if grounded
    assert channel == pytest.approx(0, abs=1e-12) and again.sum() == pytest.approx(1)


def test_projection_refuses_mismatched_shapes():
    with pytest.raises(ValueError, match="one row per average"):
        sa.project_linear(np.full(3, 1 / 3), np.ones((2, 4)), np.ones(2))
