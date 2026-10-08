"""Misalignment estimated from samples, by what is known of each draw ([D11], [P23], [P47], [P52]).

Three accesses, as `STANDARD.md` asks a case to declare before examining behaviour:
- counts: the outcome of each draw of the actor, with the default and the objective known on every outcome;
- log-ratios: for each draw of the actor, only log(p(x)/q(x)) and F(x), as for a language model scored by both
  policies;
- two samples: the same, with draws of the default and their F as well.
Each returns an `Estimate` with the standard error of [P52]'s limit law under that access, computed by plug-in. The
laws are for an actor off the ray at an interior revealed intensity; on the ray, use the χ² reference of [P23] (counts)
or note that the log-ratio estimate is exactly 0 there.
"""
from dataclasses import dataclass
import numpy as np
from scipy.optimize import brentq
from scipy.stats import chi2, norm
from .core import as_distribution, as_objective, kl, log_mean_exp
from .misalignment import _intensity, _nearest

COUNTS, LOG_RATIOS, TWO_SAMPLES = "counts", "log-ratios", "two samples"


@dataclass(frozen=True)
class Estimate:
    """An estimate of misalignment in nats, with its standard error and interval under the declared access ([P52]).

    `interval` is value ± z·standard_error, intersected with [0, ∞), since misalignment is never negative; `value` itself
    can be negative with two samples. `effective_draws` is the effective number of draws behind the reweighting the
    estimate hides ([P47]): of the actor's draws towards its nearest intended behaviour (log-ratios), or of the
    default's draws towards it (two samples); for counts it is the number of draws. The χ² fields are [P23]'s reference
    for an actor that does pursue the objective, counts only."""
    value: float
    standard_error: float
    interval: tuple
    level: float
    access: str
    revealed_intensity: float
    intensity_standard_error: float
    departure: float
    draws: int
    reference_draws: int
    effective_draws: float
    chi2_statistic: float = float("nan")
    chi2_df: int = 0
    chi2_p_value: float = float("nan")


def _interval(value, se, level):
    z = norm.ppf(0.5 + level / 2)
    return (float(max(0.0, value - z * se)), float(max(0.0, value + z * se)))


def effective_draws(log_weights):
    """(Σ w)² / Σ w² for weights given by their logarithms: the number of equally weighted draws worth as much as a
    reweighted sample, at most n·e^{−KL} of n in expectation ([P47], Notes)."""
    a = np.asarray(log_weights, dtype=float)
    m = a.max()
    w = np.exp(a - m)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _level(level):
    if not 0 < level < 1:
        raise ValueError("level must lie strictly between 0 and 1")
    return float(level)


def from_counts(counts, q, F, level=0.95):
    """Misalignment of the empirical behaviour of counted draws, with the default `q` and objective `F` known
    ([P52](i)); the revealed intensity with its standard error; and [P23]'s χ² reference, 2n·M̂ against χ² with
    |X| − 2 degrees of freedom, for the hypothesis that the actor pursues F at an interior intensity."""
    level = _level(level)
    counts = np.asarray(counts, dtype=float)
    if counts.ndim != 1 or np.any(counts < 0) or not np.all(np.isfinite(counts)) or counts.sum() <= 0:
        raise ValueError("counts must be one non-negative count per outcome, with at least one draw")
    n = counts.sum(); ph = counts / n
    q = as_distribution(q, "q", full_support=True)
    if q.size != ph.size:
        raise ValueError(f"counts and q must have the same outcomes: {ph.size} and {q.size}")
    F = as_objective(F, ph.size)
    t = _intensity(ph, q, F); po = _nearest(q, F, t); M = kl(ph, po)
    seen = ph > 0
    lw = np.log(ph[seen] / po[seen]) if np.all(po[seen] > 0) else np.full(seen.sum(), np.inf)
    var_M = ph[seen] @ lw ** 2 - (ph[seen] @ lw) ** 2 if np.all(np.isfinite(lw)) else float("inf")
    se = float(np.sqrt(max(var_M, 0.0) / n))
    if 0 < t < np.inf:
        vF, vFo = ph @ F ** 2 - (ph @ F) ** 2, po @ F ** 2 - (po @ F) ** 2
        t_se = float(np.sqrt(vF / vFo ** 2 / n))
    else:
        t_se = float("nan")
    df = ph.size - 2
    stat = 2 * n * M
    p_value = float(chi2.sf(stat, df)) if df >= 1 and np.isfinite(stat) else float("nan")
    return Estimate(M, se, _interval(M, se, level), level, COUNTS, t, t_se, kl(ph, q), int(round(n)), 0, float(n),
                    float(stat), int(df), p_value)


def _per_draw(log_ratio, objective, names=("log_ratio", "objective")):
    l = np.asarray(log_ratio, dtype=float); f = np.asarray(objective, dtype=float)
    if l.ndim != 1 or l.shape != f.shape or l.size < 2:
        raise ValueError(f"{names[0]} and {names[1]} must be one value per draw, the same draws, at least two")
    if not (np.all(np.isfinite(l)) and np.all(np.isfinite(f))):
        raise ValueError(f"{names[0]} and {names[1]} must be finite")
    return l, f


def _minimize(dphi, f_mean, f_max):
    """The s ≥ 0 minimizing a convex function of s whose derivative `dphi` increases: 0 if dphi(0) ≥ 0, otherwise the
    root, bracketed by doubling (it exists when the draws' largest F exceeds `f_mean`)."""
    if dphi(0.0) >= 0 or f_max - f_mean <= 1e-12 * (1 + abs(f_max)):
        return 0.0
    hi = 1.0
    while dphi(hi) < 0:
        hi *= 2
        if hi > 1e12:
            raise ArithmeticError("no minimizer found: the draws' objective values may be too close")
    return brentq(dphi, 0.0, hi, xtol=1e-14, rtol=4 * np.finfo(float).eps, maxiter=500)


def _weighted_mean(a, f):
    w = np.exp(a - a.max())
    return float(w @ f / w.sum())


def from_log_ratios(log_ratio, objective, level=0.95):
    """Misalignment from the actor's draws alone, with ℓ = log(p/q) and F known for each draw ([P52](ii)):
    min over s ≥ 0 of mean ℓ − s·mean F + log mean e^{s·F − ℓ}. Never negative, and exactly 0 when the ℓ of the draws
    are affine in their F with a non-negative slope."""
    level = _level(level)
    l, f = _per_draw(log_ratio, objective)
    n = l.size; fbar = f.mean()
    s = _minimize(lambda s: _weighted_mean(s * f - l, f) - fbar, fbar, f.max())
    a = s * f - l
    lme = log_mean_exp(a)
    value = l.mean() - s * fbar + lme
    log_w = a - lme                                     # log(p°/p) at the draws, normalizer estimated from them
    g = np.exp(log_w) - log_w
    se = float(np.std(g, ddof=1) / np.sqrt(n))
    return Estimate(float(value), se, _interval(value, se, level), level, LOG_RATIOS, float(s), float("nan"),
                    float(l.mean()), n, 0, effective_draws(log_w))


def from_two_samples(log_ratio, objective, reference_objective, level=0.95):
    """Misalignment from the actor's draws, with ℓ = log(p/q) and F known for each, and draws of the default with their
    F ([P52](iii)): min over s ≥ 0 of mean ℓ − s·mean F + log mean_ref e^{s·F}. It can be negative, by noise."""
    level = _level(level)
    l, f = _per_draw(log_ratio, objective)
    fr = np.asarray(reference_objective, dtype=float)
    if fr.ndim != 1 or fr.size < 2 or not np.all(np.isfinite(fr)):
        raise ValueError("reference_objective must be one finite value per draw of the default, at least two")
    n, m, fbar = l.size, fr.size, f.mean()
    if fbar >= fr.max():
        raise ValueError("the draws of the default never reach the actor's average of F: draw more of the default")
    s = _minimize(lambda s: _weighted_mean(s * fr, fr) - fbar, fbar, fr.max())
    A = log_mean_exp(s * fr)
    value = l.mean() - s * fbar + A
    log_w = s * f - A - l                               # log(p°/p) at the actor's draws
    log_v = s * fr - A                                  # log(p°/q) at the default's draws
    se = float(np.sqrt(np.var(log_w, ddof=1) / n + np.var(np.exp(log_v), ddof=1) / m))
    return Estimate(float(value), se, _interval(value, se, level), level, TWO_SAMPLES, float(s), float("nan"),
                    float(l.mean()), n, m, effective_draws(log_v))
