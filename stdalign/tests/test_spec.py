"""Unit tests of `stdalign/spec.py`'s interface: declarations, edge cases, and the shape of what it returns. The
mathematics is checked against `mvp/CORE.md` in `mvp/checks/`."""
import numpy as np
import pytest

from stdalign import spec as S


def test_declarations():
    lim = S.rate_limit([0, 2], 0.1, 4)
    assert lim.g == (1.0, 0.0, 1.0, 0.0) and lim.b == 0.1 and lim.cell is None
    assert S.forbidden([1], 3).b == 0.0
    assert S.rate_limit(np.array([True, False]), 0.2).g == (1.0, 0.0)
    with pytest.raises(ValueError):
        S.rate_limit([0], 0.1)                       # indices need the number of outcomes
    lims = S.no_worse_than(np.array([0.5, 0.5]), [np.array([1.0, 0.0])])
    assert lims[0].g == (-1.0, -0.0) and lims[0].b == -0.5


def test_misalignment_returns_a_certified_interval():
    p = np.array([0.3, 0.3, 0.4])
    m = S.misalignment(p, [S.rate_limit([0], 0.1, 3)])
    assert m.lower <= m.value == m.upper
    assert m.upper - m.lower < 1e-6
    assert m.nearest.sum() == pytest.approx(1.0) and m.nearest[0] <= 0.1 + 1e-9
    assert m.consistent and not m.infinite


def test_misalignment_zero_inside_and_flags():
    p = np.array([0.05, 0.95])
    assert S.misalignment(p, [S.rate_limit([0], 0.1, 2)]).value == pytest.approx(0.0, abs=1e-9)
    inf = S.misalignment(np.array([0.5, 0.5]), [S.forbidden([0], 2)])
    assert inf.infinite and inf.consistent and inf.value == np.inf
    inc = S.misalignment(np.array([0.5, 0.5]), [S.rate_limit([0], 0.1, 2)], world=np.array([0, 1]))
    assert inc.value == np.inf and not inc.consistent


def test_closed_forms_edges():
    assert S.rate_limit_misalignment(0.1, 0.1) == 0.0
    assert S.rate_limit_misalignment(0.2, 0.0) == np.inf
    assert S.budget_misalignment(np.array([1.0, 0.0]), np.array([0.0, 1.0]), 0.5) == (0.0, 0.0)
    val, theta, v = S.overall_rate_limit([0.5, 0.5], [0.01, 0.02], 0.1)
    assert val == 0.0 and theta == 0.0


def test_bet_test_and_bounds():
    bt = S.bet_test(np.zeros(100), 0.1, 0.0)
    assert not bt.convicted and bt.at is None and bt.wealth.shape == (100,)
    assert np.all(bt.wealth <= 1.0 + 1e-12)          # betting on breaches that never come never gains
    bt = S.bet_test(np.ones(50), 0.1, 0.0)
    assert bt.convicted and bt.at is not None
    bt = S.bet_test(np.r_[np.ones(30), np.zeros(60)], 0.1, 0.0, alpha=1e-12)
    assert np.all(bt.wealth >= 0)                    # a bet never stakes more than the wealth
    bt = S.bet_test(np.r_[np.full(50, 0.15), np.zeros(50)], 0.1, 0.0, alpha=1e-12)
    assert np.all(bt.wealth >= 0)                    # small, steady overruns push the fraction to its cap


def test_bet_lower_bound_scales_an_unfair_bet():
    p = np.array([0.3, 0.7])
    lims = [S.rate_limit([0], 0.1, 2)]
    h = np.array([3.0, 1.0])                         # costs 1.2 under the acceptable behaviour a(0) = 0.1
    want = 0.3 * np.log(3.0) - np.log(1.2)
    assert S.bet_lower_bound(p, h, lims) == pytest.approx(want)
    assert S.bet_lower_bound(p, h, lims) <= S.misalignment(p, lims).value
    with pytest.raises(ValueError):
        S.average_bounds(np.array([0.5, 2.0]))
    bd = S.average_bounds(np.full(1000, 0.2), 0.05)
    assert np.all(bd.lower <= 0.2) and np.all(bd.upper >= 0.2)
    assert bd.upper[-1] - bd.lower[-1] == pytest.approx(2 * np.sqrt(np.log(2 / 0.05) / (2 * 1000)))
    assert S.pooled_verdict(np.full(10, 0.5), 0.1)[0] == "neither"


def test_splits_add_up():
    p = np.array([0.4, 0.3, 0.2, 0.1])
    lims = [S.rate_limit([0], 0.1, 4)]
    vals, inc = S.resolution_split(p, lims, [np.array([0, 0, 1, 1]), None])
    assert vals[0] + sum(inc) == pytest.approx(vals[-1])
    V = np.array([[0.4, 0.3, 0.2, 0.1], [0.05, 0.45, 0.4, 0.1]])
    f = S.factorization(V[0], [V, V[:1]], lims)
    assert f["unavoidable"] == pytest.approx(0.0, abs=1e-6)
    assert f["unavoidable"] + sum(f["increments"]) + f["avoidable_excess"] == pytest.approx(f["total"])
    culp, E, m = S.culpable(V[0], V, lims, 0.01)
    assert culp and E > 0.01
