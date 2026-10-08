"""Tests of the library's interface: its checks on inputs, its three cases, its invariances, and the agreement of its
estimates with the exact quantities. The framework's claims are tested in checks/, on this same code."""
import numpy as np
import pytest
import stdalign as sa

R = np.random.default_rng(9001)


def instance(k=5, t=0.8, noise=0.5):
    q = R.dirichlet(np.ones(k)); F = R.normal(0, 1, k)
    return sa.tilt(q, t * F + R.normal(0, noise, k)), q, F


@pytest.mark.parametrize("p, message", [([0.5, 0.6], "sums to"), ([-0.1, 1.1], "negative"), ([[0.5, 0.5]], "one-dimensional"),
                                        ([np.nan, 1.0], "not finite"), ([], "one-dimensional")])
def test_bad_distributions_are_refused(p, message):
    with pytest.raises(ValueError, match=message):
        sa.assess(p, [0.5, 0.5], [0.0, 1.0])


def test_bad_defaults_objectives_and_samples_are_refused():
    with pytest.raises(ValueError, match="positive mass"):
        sa.assess([0.5, 0.5], [1.0, 0.0], [0.0, 1.0])
    with pytest.raises(ValueError, match="same outcomes"):
        sa.assess([0.5, 0.5], [0.2, 0.3, 0.5], [0.0, 1.0])
    with pytest.raises(ValueError, match="one value per outcome"):
        sa.assess([0.5, 0.5], [0.5, 0.5], [0.0, 1.0, 2.0])
    with pytest.raises(ValueError, match="not finite"):
        sa.assess([0.5, 0.5], [0.5, 0.5], [0.0, np.inf])
    with pytest.raises(ValueError, match="counts"):
        sa.from_counts([3, -1, 2], [0.2, 0.3, 0.5], [0.0, 1.0, 2.0])
    with pytest.raises(ValueError, match="same draws"):
        sa.from_log_ratios([0.1, 0.2, 0.3], [1.0, 2.0])
    with pytest.raises(ValueError, match="level"):
        sa.from_log_ratios([0.1, 0.2, 0.3], [1.0, 2.0, 3.0], level=1.5)
    with pytest.raises(ValueError, match="never reach"):
        sa.from_two_samples([0.1, 0.2], [5.0, 6.0], [0.0, 1.0, 2.0])


def test_the_three_cases():
    p, q, F = instance()
    a = sa.assess(q, q, F)
    assert a.case == sa.DEFAULT and a.revealed_intensity == 0 and a.misalignment == pytest.approx(0, abs=1e-15)
    a = sa.assess(sa.pursuit(q, F, 1.3), q, F)
    assert a.case == sa.PURSUIT and a.revealed_intensity == pytest.approx(1.3, rel=1e-9)
    assert a.misalignment == pytest.approx(0, abs=1e-12)
    best = sa.best_outcomes(q, F)
    a = sa.assess(best, q, F)
    assert a.case == sa.BEST_OUTCOMES and np.isinf(a.revealed_intensity) and a.misalignment == pytest.approx(0, abs=1e-15)
    a = sa.assess(p, q, F)
    assert a.departure == pytest.approx(a.pursuit_part + a.misalignment, rel=1e-9)        # [P6]
    assert sa.misalignment(p, q, F) == a.misalignment
    assert sa.revealed_intensity(p, q, F) == a.revealed_intensity
    assert np.array_equal(sa.nearest_intended(p, q, F), a.nearest)


def test_invariances():
    for _ in range(50):
        p, q, F = instance(k=int(R.integers(3, 9)))
        a = sa.assess(p, q, F)
        b = sa.assess(p, q, F + 7.0)                                     # a constant added to F changes nothing
        c = sa.assess(p, q, 3.0 * F)                                     # a scale divides the intensity
        perm = R.permutation(p.size)
        d = sa.assess(p[perm], q[perm], F[perm])                         # the outcomes' order does not matter
        assert b.misalignment == pytest.approx(a.misalignment, rel=1e-7, abs=1e-12)
        assert c.misalignment == pytest.approx(a.misalignment, rel=1e-7, abs=1e-12)
        if 0 < a.revealed_intensity < np.inf:
            assert c.revealed_intensity == pytest.approx(a.revealed_intensity / 3, rel=1e-7)
        assert d.misalignment == pytest.approx(a.misalignment, rel=1e-9, abs=1e-14)


def test_counts_proportional_to_the_behaviour_give_the_exact_values():
    for _ in range(50):
        p, q, F = instance(k=int(R.integers(3, 9)))
        e, a = sa.from_counts(p * 1e6, q, F), sa.assess(p, q, F)
        assert e.value == pytest.approx(a.misalignment, rel=1e-9, abs=1e-15)
        assert e.revealed_intensity == pytest.approx(a.revealed_intensity, rel=1e-9)
        assert e.departure == pytest.approx(a.departure, rel=1e-9)
        assert e.chi2_df == p.size - 2 and e.chi2_statistic == pytest.approx(2e6 * a.misalignment, rel=1e-9)


def test_estimates_agree_with_the_exact_value():
    """Each access's interval covers the exact misalignment in most of 60 large samples (level 95%: at least 50)."""
    hits = {sa.COUNTS: 0, sa.LOG_RATIOS: 0, sa.TWO_SAMPLES: 0}
    for _ in range(60):
        p, q, F = instance(k=4, t=1.0, noise=0.4)
        M = sa.misalignment(p, q, F)
        x = R.choice(p.size, size=4000, p=p); y = R.choice(q.size, size=4000, p=q)
        l = np.log(p[x] / q[x])
        for e in (sa.from_counts(np.bincount(x, minlength=p.size), q, F), sa.from_log_ratios(l, F[x]),
                  sa.from_two_samples(l, F[x], F[y])):
            assert e.interval[0] <= max(e.value, 0) <= e.interval[1] and e.interval[0] >= 0
            hits[e.access] += e.interval[0] <= M <= e.interval[1]
    assert min(hits.values()) >= 50, hits


def test_effective_draws():
    assert sa.effective_draws(np.zeros(10)) == pytest.approx(10)
    assert sa.effective_draws(np.array([0.0, -50.0, -50.0])) == pytest.approx(1, rel=1e-12)
    assert sa.effective_draws(np.log([1.0, 1.0, 2.0])) == pytest.approx(16 / 6)


def test_infinite_divergences_and_zero_masses_raise_no_warning():
    """KL is infinite where the second behaviour misses an outcome the first uses; tilts keep zero masses at zero; and
    neither warns, so a case's log stays readable."""
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        assert sa.kl([0.5, 0.5], [1.0, 0.0]) == np.inf
        assert sa.kl([1.0, 0.0], [0.5, 0.5]) == pytest.approx(np.log(2))
        assert np.array_equal(sa.tilt([0.5, 0.0, 0.5], np.array([1.0, 2.0, 3.0])) > 0, [True, False, True])
        assert np.isfinite(sa.log_normalizer([0.5, 0.0, 0.5], np.array([1.0, 2.0, 3.0])))


def test_standard_errors_match_the_spread_of_the_estimates():
    """The reported standard errors, averaged over 400 samples, match the spread of the estimates within 12%: for an
    actor near the ray, misalignment under each access and the revealed intensity by counts; for one far from it,
    misalignment by counts and by two samples ([P52]'s laws, by plug-in)."""
    r = np.random.default_rng(9002)
    q = np.array([0.35, 0.25, 0.2, 0.12, 0.08]); F = np.array([0.0, 0.6, 1.1, 1.9, 2.4])
    p = sa.tilt(q, 0.9 * F + np.array([0.3, -0.4, 0.2, -0.3, 0.25]))
    est = {sa.COUNTS: [], sa.LOG_RATIOS: [], sa.TWO_SAMPLES: []}; t_hat, t_se = [], []
    for _ in range(400):
        x = r.choice(5, size=3000, p=p); y = r.choice(5, size=3000, p=q); l = np.log(p[x] / q[x])
        c = sa.from_counts(np.bincount(x, minlength=5), q, F)
        t_hat.append(c.revealed_intensity); t_se.append(c.intensity_standard_error)
        for e in (c, sa.from_log_ratios(l, F[x]), sa.from_two_samples(l, F[x], F[y])):
            est[e.access].append((e.value, e.standard_error))
    for access, rows in est.items():
        v, se = np.array(rows).T
        assert np.mean(se) == pytest.approx(np.std(v), rel=0.12), access
    assert np.mean(t_se) == pytest.approx(np.std(t_hat), rel=0.12)
    p = sa.tilt(q, 0.9 * F + np.array([2.0, -1.5, 0.5, -2.0, 1.5]))     # far from the ray, M = 0.53: the mean of log w
    rows = {sa.COUNTS: [], sa.TWO_SAMPLES: []}                           # matters, and log-ratios are not expected to do well
    for _ in range(400):
        x = r.choice(5, size=3000, p=p); y = r.choice(5, size=3000, p=q); l = np.log(p[x] / q[x])
        for e in (sa.from_counts(np.bincount(x, minlength=5), q, F), sa.from_two_samples(l, F[x], F[y])):
            rows[e.access].append((e.value, e.standard_error))
    for access, values in rows.items():
        v, se = np.array(values).T
        assert np.mean(se) == pytest.approx(np.std(v), rel=0.12), access
