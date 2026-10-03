"""Checks of SCENARIO.md: the identities its numbers rest on hold, and it quotes every number as scenario/compute.py
computes it. Tolerances: the scenario's quantities are of order 1 to 10; the bisections behind t*, λ and the peak stop
at a width far below 1e-12, so the identities hold to 1e-9, and the quoted numbers are compared as printed strings."""
import re, sys
from pathlib import Path
import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from compute import (compute, quoted, declared, evaluator_curve, regression, DEFAULT, VALUE, RATING, FIXED_RATING,   # noqa: E402
                     TUNED_INTENSITY)

TOL = 1e-9


@pytest.fixture(scope="module")
def v():
    return compute()


def test_every_number_the_scenario_quotes_is_computed(v):
    """Each computed value appears in SCENARIO.md, and every amount in euros, nats or stars there is a computed value or
    a declared input."""
    text = (Path(__file__).resolve().parents[1] / "SCENARIO.md").read_text(encoding="utf-8")
    values = quoted(v)
    missing = {name: s for name, s in values.items() if s not in text}
    assert not missing, missing
    amounts = re.findall(r"−?€[\d,]+(?:\.\d+)?(?: thousand| million)?|\d+\.\d+ nats|\d\.\d\d stars", text)
    stray = sorted({a for a in amounts} - set(values.values()) - declared()
                   - {w for s in values.values() for w in re.findall(r"−?€[\d.]+|\d+\.\d+ nats", s)})
    assert not stray, stray


def test_the_identities_the_numbers_rest_on(v):
    assert abs(v["departure"] - v["pursuit_part"] - v["M"]) < TOL                        # [P6]
    assert abs(v["lambda"] * v["S"] - v["M"] - v["under_pursuit"]) < 1e-8                 # [P9](ii), no anti-pursuit
    assert v["value_tuned"] > v["value_default"]
    assert v["chernoff"] <= v["M"]                                                        # [P22](iii)
    assert v["value_matched"] >= v["fixed_value_same_departure"]                          # [P9](i)
    assert abs(v["ratio_tuned"] - v["ratio_default"]) < 0.01                              # [P8](i): split as q does
    assert abs(v["value_tuned"] - v["counts"] @ regression(RATING) / v["counts"].sum()) < 0.01   # [P18](i)
    assert v["M_low"] < v["M"] < v["M_high"] and v["S_low"] < v["S"] < v["S_high"]


def test_the_rating_overoptimizes_and_the_repaired_rating_cannot(v):
    value_at, cov_at, peak, limit = evaluator_curve(RATING)
    assert abs(cov_at(peak)) < TOL and cov_at(TUNED_INTENSITY) < 0                        # [P20](i): past the peak
    ts = np.linspace(0, 40, 4001)
    curve = np.array([value_at(t) for t in ts])
    falls, rises = np.diff(curve) < -1e-12, np.diff(curve) > 1e-12
    assert falls.any() and not rises[np.argmax(falls):].any()                             # [P25](iii): no rise after a fall
    assert abs(curve[-1] - limit) < 1e-3 and limit == VALUE[RATING.argmax()]               # [P20](ii)
    fixed_at, _, _, _ = evaluator_curve(FIXED_RATING)
    fixed = np.array([fixed_at(t) for t in ts])
    assert v["fixed_regression_monotone"] and np.all(np.diff(fixed) >= -1e-12)            # [P19]
    assert abs(fixed[0] - DEFAULT @ VALUE) < TOL
