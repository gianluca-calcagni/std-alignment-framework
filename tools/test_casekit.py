"""Tests of tools/casekit.py: each helper keeps the lesson it was written for."""
import numpy as np
import casekit as K


def test_rows_are_saved_and_read_back(tmp_path, monkeypatch):
    monkeypatch.setattr(K, "SCRATCH", tmp_path / "scratch")
    rows = [{"a": np.arange(3), "b": 1.5}, {"a": np.zeros(2), "b": float("nan")}]
    path = K.save_rows(rows, "case")
    assert path.parent == tmp_path / "scratch" and path.exists()
    back = K.load_rows("case")
    assert np.array_equal(back[0]["a"], rows[0]["a"]) and np.isnan(back[1]["b"])


def test_least_squares_is_exact_when_the_regressor_does_not_vary():
    r = np.random.default_rng(1)
    for _ in range(200):
        x, z = r.normal(size=20), r.normal(size=20)
        slope, ssr, sst = K.least_squares(z, x)
        B = np.column_stack([np.ones(20), x]); coef = np.linalg.lstsq(B, z, rcond=None)[0]
        assert abs(slope - coef[1]) <= 1e-10 and abs(ssr - ((z - B @ coef) ** 2).sum()) <= 1e-9
        assert abs(sst - ((z - z.mean()) ** 2).sum()) <= 1e-9
        slope, ssr, sst = K.least_squares(z, np.full(20, 3.0))                   # a constant regressor
        assert np.isnan(slope) and ssr == sst and np.isfinite(sst)


def test_untie_matches_a_selector_that_breaks_ties_at_random():
    """Best-of-n by weights over ranks (Coste et al.'s estimator), untied, against a simulation that breaks ties at
    random; a fixed order is rejected by the same simulation."""
    from scipy.special import gammaln
    N, n, T = 30, 4, 200_000
    r = np.random.default_rng(2)
    scores = np.sort(r.integers(0, 8, N)).astype(float)
    i = np.arange(1, N + 1)
    logw = gammaln(i) - gammaln(n) - gammaln(np.maximum(i - n + 1, 1)) - (gammaln(N + 1) - gammaln(n + 1) - gammaln(N - n + 1))
    w = np.where(i >= n, np.exp(logw), 0.0)
    u = K.untie(w, scores)
    assert abs(u.sum() - w.sum()) <= 1e-12
    draws = np.array([r.choice(N, n, replace=False) for _ in range(T)])
    pick = draws[np.arange(T), (scores[draws] + r.random(draws.shape) * 1e-6).argmax(1)]
    freq = np.bincount(pick, minlength=N) / T
    se = np.sqrt(np.maximum(u * (1 - u), 1e-12) / T)
    assert np.max(np.abs(freq - u) / se) < 5                                       # the untied weights fit
    assert np.max(np.abs(freq - w) / se) > 10                                      # one fixed order does not


def test_log_mean_exp_does_not_underflow():
    a = np.array([-1000.0, -1001.0, -1002.0])
    assert abs(K.log_mean_exp(a) - (-1000 + np.log(np.mean(np.exp([0.0, -1.0, -2.0]))))) <= 1e-12
    b = np.array([[0.0, 800.0], [1.0, 2.0]])
    assert np.allclose(K.log_mean_exp(b, axis=1), [800 - np.log(2) + np.log1p(np.exp(-800)), np.log(np.mean(np.exp([1.0, 2.0])))])


def test_bootstrap_keeps_every_item():
    """Missing values stay in the resamples: the interval comes from the same list of items, and the statistic
    ignores what is missing."""
    values = np.r_[np.arange(10.0), [np.nan] * 3]
    out = K.bootstrap(values, boot=500, seed=3)
    assert out["mean"] == 4.5 and out["interval_95"][0] < 4.5 < out["interval_95"][1]
    assert K.bootstrap(values, boot=500, seed=3) == out                            # reproducible


def test_seconds_per_item_measures():
    import time
    assert 0.009 <= K.seconds_per_item(lambda _: time.sleep(0.01), range(5)) <= 0.1
