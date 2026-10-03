"""Every number of SCENARIO.md, computed with the helpers that the checks use (checks/common.py and the checks of [P5],
[P9]). Usage: python3 scenario/compute.py   (prints each quoted value under its name)

scenario/test_scenario.py recomputes these values, checks the identities they rest on, and checks that SCENARIO.md
quotes each of them as printed here.
"""
import sys
from pathlib import Path
import numpy as np
from scipy.stats import chi2

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from checks.common import kl, tilt                                     # noqa: E402
from checks.test_misalignment import misalignment                      # noqa: E402
from checks.test_stakes import shortfall                               # noqa: E402

OUTCOMES = ["resolved", "handed over", "wrong", "vague", "credit"]
DEFAULT = np.array([0.40, 0.15, 0.15, 0.25, 0.05])                    # the pilot, before tuning
VALUE = np.array([10.0, 2.0, -20.0, -2.0, -5.0])                      # euros per conversation, declared by the company
RATING = np.array([4.0, 2.0, 4.0, 1.0, 5.0])                          # the rating model's predicted stars
TUNED_INTENSITY = 0.6                                                 # how hard the assistant was tuned on the rating
SAMPLE = 2000                                                         # live conversations reviewed after launch
LEAK = 0.10                                                           # nats: how far the assistant can tell tests apart
FIXED_RATING = np.array([4.0, 3.0, 0.0, 2.0, 1.0])                    # a rating model that orders outcomes as the value
PER_MONTH = 1_000_000
BOOTSTRAP, SEED = 4000, 20261003


def bisect(f, lo, hi, n=200):
    """The root of an increasing f on [lo, hi]."""
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    return 0.5 * (lo + hi)


def counts():
    """The reviewed sample: the tuned behaviour times the sample size, rounded by largest remainders."""
    exact = tilt(DEFAULT, TUNED_INTENSITY * RATING) * SAMPLE
    c = np.floor(exact).astype(int)
    c[np.argsort(exact - c)[::-1][: SAMPLE - c.sum()]] += 1
    return c


def chernoff(p, r):
    lams = np.linspace(0, 1, 100001)
    return float(-min(np.log(np.sum(p ** l * r ** (1 - l))) for l in lams))


def evaluator_curve(rating):
    """The target's average along the pursuit of a rating model, its peak ([P20](i)) and its limit ([P20](ii))."""
    value_at = lambda t: float(tilt(DEFAULT, t * rating) @ VALUE)
    cov_at = lambda t: float(tilt(DEFAULT, t * rating) @ (rating * VALUE) - (tilt(DEFAULT, t * rating) @ rating) *
                             (tilt(DEFAULT, t * rating) @ VALUE))
    top = rating >= rating.max()
    limit = float(DEFAULT[top] @ VALUE[top] / DEFAULT[top].sum())
    peak = bisect(lambda t: -cov_at(t), 0.0, 5.0) if cov_at(0.0) > 0 and cov_at(5.0) < 0 else None
    return value_at, cov_at, peak, limit


def regression(rating):
    """The cell average of the value on the rating's level sets ([D10]), as a function on the outcomes."""
    m = np.empty_like(VALUE)
    for v in np.unique(rating):
        cell = rating == v
        m[cell] = DEFAULT[cell] @ VALUE[cell] / DEFAULT[cell].sum()
    return m


def leak_bounds(p_a, eps):
    """[P17](ii): the range of the value's average in a condition the assistant can tell apart by eps nats."""
    out = []
    for sign in (+1, -1):
        g = lambda lam: kl(tilt(p_a, sign * lam * VALUE), p_a) - eps
        lam = bisect(g, 0.0, 50.0)
        out.append(float(tilt(p_a, sign * lam * VALUE) @ VALUE))
    return out[1], out[0]


def compute():
    c = counts()
    p = c / SAMPLE
    v = {}
    v["counts"] = c
    v["value_default"], v["value_tuned"] = float(DEFAULT @ VALUE), float(p @ VALUE)
    v["rating_default"], v["rating_tuned"] = float(DEFAULT @ RATING), float(p @ RATING)
    v["ratio_default"], v["ratio_tuned"] = DEFAULT[0] / DEFAULT[2], c[0] / c[2]
    v["departure"] = kl(p, DEFAULT)
    v["M"], v["t_star"] = misalignment(p, DEFAULT, VALUE)
    nearest = tilt(DEFAULT, v["t_star"] * VALUE)
    v["nearest"], v["pursuit_part"], v["value_nearest"] = nearest, kl(nearest, DEFAULT), float(nearest @ VALUE)
    v["S"], v["lambda"] = shortfall(p, DEFAULT, VALUE)
    matched = tilt(DEFAULT, v["lambda"] * VALUE)
    v["matched"], v["value_matched"] = matched, float(matched @ VALUE)
    v["under_pursuit"] = kl(nearest, matched)
    v["chi2_stat"] = 2 * SAMPLE * v["M"]
    v["chi2_p"] = float(chi2.sf(v["chi2_stat"], len(VALUE) - 2))
    v["chi2_999"] = float(chi2.ppf(0.999, len(VALUE) - 2))
    v["n_for_999"] = int(np.ceil(v["chi2_999"] / (2 * v["M"])))
    v["chernoff"] = chernoff(p, nearest)
    v["n_for_1pct"] = int(np.ceil(np.log(100) / v["chernoff"]))
    r = np.random.default_rng(SEED)
    boot_M, boot_S = [], []
    for _ in range(BOOTSTRAP):
        pb = r.multinomial(SAMPLE, p) / SAMPLE
        boot_M.append(misalignment(pb, DEFAULT, VALUE)[0]); boot_S.append(shortfall(pb, DEFAULT, VALUE)[0])
    v["M_low"], v["M_high"] = np.percentile(boot_M, [2.5, 97.5])
    v["S_low"], v["S_high"] = np.percentile(boot_S, [2.5, 97.5])
    revealed = np.log(p / DEFAULT)
    fit = lambda f: np.linalg.lstsq(np.c_[f, np.ones_like(f)], revealed, rcond=None)
    spread = float(np.sum((revealed - revealed.mean()) ** 2))
    v["revealed_slope"] = float(fit(RATING)[0][0])
    v["revealed_fit_rating"] = float(1 - fit(RATING)[1][0] / spread)
    v["revealed_fit_value"] = float(1 - fit(VALUE)[1][0] / spread)
    m = regression(RATING)
    v["regression"] = m
    resid = VALUE - m
    var = lambda f: float(DEFAULT @ f ** 2 - (DEFAULT @ f) ** 2)
    v["residual_share"] = var(resid) / var(VALUE)
    value_at, cov_at, peak, limit = evaluator_curve(RATING)
    v["peak_t"], v["peak_value"], v["limit_value"] = peak, value_at(peak), limit
    v["cov_now"] = cov_at(TUNED_INTENSITY)
    v["value_t1"], v["value_t2"] = value_at(1.0), value_at(2.0)
    v["rating_t1"], v["rating_t2"] = float(tilt(DEFAULT, RATING) @ RATING), float(tilt(DEFAULT, 2 * RATING) @ RATING)
    v["leak_low"], v["leak_high"] = leak_bounds(p, LEAK)
    fixed_at, _, fixed_peak, fixed_limit = evaluator_curve(FIXED_RATING)
    v["fixed_regression_monotone"] = bool(np.all(np.diff(regression(FIXED_RATING)[np.argsort(FIXED_RATING)]) >= 0))
    v["fixed_t1"], v["fixed_t2"], v["fixed_limit"] = fixed_at(1.0), fixed_at(2.0), fixed_limit
    v["fixed_departure_t"] = bisect(lambda t: kl(tilt(DEFAULT, t * FIXED_RATING), DEFAULT) - v["departure"], 0, 10)
    v["fixed_value_same_departure"] = fixed_at(v["fixed_departure_t"])
    return v


def quoted(v):
    """The strings SCENARIO.md quotes, as it quotes them."""
    e2 = lambda x: f"€{x:.2f}" if x >= 0 else f"−€{-x:.2f}"
    return {
        "counts": " · ".join(f"{n} {o}" for n, o in zip(v["counts"], OUTCOMES)),
        "value_default": e2(v["value_default"]), "value_tuned": e2(v["value_tuned"]),
        "rating_default": f"{v['rating_default']:.2f} stars", "rating_tuned": f"{v['rating_tuned']:.2f} stars",
        "ratio_default": f"{v['ratio_default']:.2f}", "ratio_tuned": f"{v['ratio_tuned']:.2f}",
        "departure": f"{v['departure']:.3f} nats", "M": f"{v['M']:.3f} nats", "t_star": f"{v['t_star']:.4f}",
        "pursuit_part": f"{v['pursuit_part']:.3f} nats", "value_nearest": e2(v["value_nearest"]),
        "S": e2(v["S"]), "lambda": f"{v['lambda']:.4f}", "value_matched": e2(v["value_matched"]),
        "under_pursuit": f"{v['under_pursuit']:.3f} nats",
        "chi2_stat": f"{v['chi2_stat']:.0f}", "chi2_999": f"{v['chi2_999']:.1f}", "n_for_999": f"{v['n_for_999']}",
        "chernoff": f"{v['chernoff']:.3f} nats", "n_for_1pct": f"{v['n_for_1pct']}",
        "M_interval": f"{v['M_low']:.3f} to {v['M_high']:.3f} nats", "S_low": e2(v["S_low"]), "S_high": e2(v["S_high"]),
        "leak": f"{LEAK:.2f} nats", "nats_for_ten_to_one": f"{np.log(10):.1f} nats",
        "revealed_slope": f"{v['revealed_slope']:.2f}",
        "revealed_fit_rating": f"{v['revealed_fit_rating']:.4f}",
        "revealed_fit_value": f"{v['revealed_fit_value']:.2f}",
        "regression_cell": f"{v['regression'][0]:.2f}", "regression_cell_euros": e2(v["regression"][0]),
        "residual_share": f"{100 * v['residual_share']:.0f}%",
        "peak_t": f"{v['peak_t']:.2f}", "peak_value": e2(v["peak_value"]), "limit_value": e2(v["limit_value"]),
        "cov_now": f"{v['cov_now']:.2f}".replace("-", "−"),
        "value_t1": e2(v["value_t1"]), "value_t2": e2(v["value_t2"]),
        "rating_t1": f"{v['rating_t1']:.2f} stars", "rating_t2": f"{v['rating_t2']:.2f} stars",
        "leak_low": e2(v["leak_low"]), "leak_high": e2(v["leak_high"]),
        "fixed_t1": e2(v["fixed_t1"]), "fixed_t2": e2(v["fixed_t2"]), "fixed_limit": e2(v["fixed_limit"]),
        "fixed_value_same_departure": e2(v["fixed_value_same_departure"]),
        "monthly_gain": f"€{(v['value_tuned'] - v['value_default']) * PER_MONTH / 1000:,.0f} thousand",
        "monthly_shortfall": f"€{v['S'] * PER_MONTH / 1e6:.1f} million",
    }


def declared():
    """The declared values, as SCENARIO.md quotes them: inputs, not results."""
    return {f"€{x:.0f}" if x >= 0 else f"−€{-x:.0f}" for x in VALUE}


if __name__ == "__main__":
    for name, text in quoted(compute()).items():
        print(f"{name:28s} {text}")
