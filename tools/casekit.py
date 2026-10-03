"""Helpers every case script should use: each one is a lesson from a case, written once and tested
(tools/test_casekit.py), so that a new script gets it by default. NOTES.md section 1 has the failure modes.

- save_rows / load_rows: per-item results go to disk, outside the repository, before any aggregation (W1's report lost
  35 minutes at its last step).
- least_squares: the exact fit when the regressor does not vary (W3's second launch divided 0 by 0).
- untie: best-of-n and other selectors break ties at random, so a divergence does not charge a fixed order (W1's report).
- log_mean_exp: averages of exponentials in log space (W1's report: a matched pursuit underflowed).
- bootstrap: resamples every item, missing values included, so the indices always match (W1's report crashed).
- seconds_per_item: a run time measured before a run is launched (W3's first launch was 50 times slower than guessed).
"""
import json, os, pickle, time
from pathlib import Path
import numpy as np

SCRATCH = Path(os.environ.get("CASE_SCRATCH", Path.home() / ".cache" / "cases"))   # outside the repository


def save_rows(rows, name):
    """Write per-item results to SCRATCH/<name>.pkl and return the path."""
    SCRATCH.mkdir(parents=True, exist_ok=True)
    path = SCRATCH / f"{name}.pkl"
    path.write_bytes(pickle.dumps(rows))
    return path


def load_rows(name):
    return pickle.loads((SCRATCH / f"{name}.pkl").read_bytes())


def least_squares(z, x):
    """The least-squares line of z on x with an intercept: (slope, residual sum of squares, total sum of squares).
    Where x does not vary the line is the mean of z: the slope is undefined (NaN) and the residual equals the total."""
    z, x = np.asarray(z, float), np.asarray(x, float)
    zc, xc = z - z.mean(), x - x.mean()
    sxx, sst = float(xc @ xc), float(zc @ zc)
    if sxx == 0.0:
        return float("nan"), sst, sst
    slope = float(zc @ xc) / sxx
    return slope, float(((zc - slope * xc) ** 2).sum()), sst


def untie(weights, scores):
    """Weights of a selector over items sorted by score, with ties broken at random: by symmetry each item of a block of
    equal scores gets the block's average weight. Block masses, and so every average over blocks, are unchanged."""
    scores = np.asarray(scores)
    starts = np.r_[0, np.flatnonzero(np.diff(scores)) + 1]
    sizes = np.diff(np.r_[starts, len(scores)])
    return np.repeat(np.add.reduceat(np.asarray(weights, float), starts) / sizes, sizes)


def log_mean_exp(a, axis=None):
    """log of the mean of exp(a), computed with the maximum taken out, so that no term underflows or overflows."""
    a = np.asarray(a, float)
    m = np.max(a, axis=axis, keepdims=True)
    out = m + np.log(np.mean(np.exp(a - m), axis=axis, keepdims=True))
    return out.item() if axis is None else np.squeeze(out, axis=axis)


def bootstrap(values, boot=1000, seed=0, stat=np.nanmean):
    """The statistic of the items and a 95% percentile interval from boot resamples of all the items. Items whose
    value is missing (NaN) stay in every resample, so resampled indices always refer to the same list; the statistic
    must ignore them (nanmean does)."""
    values = np.asarray(values, float)
    r = np.random.default_rng(seed)
    draws = [stat(values[r.integers(0, len(values), len(values))]) for _ in range(boot)]
    lo, hi = np.percentile(draws, [2.5, 97.5])
    return {"mean": float(stat(values)), "interval_95": [float(lo), float(hi)]}


def seconds_per_item(fn, items):
    """Run fn on each item and return the mean seconds per item, to project a run's time before it is launched."""
    start = time.perf_counter()
    for item in items:
        fn(item)
    return (time.perf_counter() - start) / max(len(items), 1)


def write_record(path, record):
    """Write a JSON record (a rehearsal's, or a result's aggregates) with stable formatting."""
    Path(path).write_text(json.dumps(record, indent=1, sort_keys=True) + "\n")
