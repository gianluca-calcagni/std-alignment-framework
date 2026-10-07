"""Case W1, the report to STANDARD.md: every result field, computed on W1's data after its verdict (descriptive, not a
test). Each prompt's N answers are its outcomes, and the initial policy's behaviour is their empirical distribution q.
Best-of-n by the proxy, at each n reported, is the actor's behaviour; the specification is the standard one of the gold.
Uses the checked helpers (checks/common.py, the checks of [P5] and [P9]). Keeps only aggregates.
Usage: python3 report.py <folder holding validation/split_*.json>   (needs proxy.npz from train_proxy.py; saves the
per-prompt rows next to that folder, then writes report.json), or python3 report.py --aggregate <saved rows>
"""
import json, sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from checks.common import kl, tilt                                                    # noqa: E402
from checks.test_misalignment import misalignment, best_outcomes_limit                # noqa: E402
from checks.test_stakes import shortfall                                              # noqa: E402
import run as R                                                                       # noqa: E402
from train_proxy import features                                                      # noqa: E402

NS = [2, 16, 128, 1024]
BINS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99, 0.999, 1.0]          # proxy rank, as a quantile
BOOT, SEED = 1000, 20261003
T_GRID = np.r_[0.0, np.logspace(-3, 4, 701)]       # intensities for the specification shared across prompts


def bon_weights(n):
    """The best-of-n probability of the i-th smallest proxy score among N (eq. 8 of Coste et al.)."""
    i = np.arange(1, R.N + 1)
    from scipy.special import gammaln
    logw = gammaln(i) - gammaln(n) - gammaln(np.maximum(i - n + 1, 1)) - (gammaln(R.N + 1) - gammaln(n + 1)
                                                                           - gammaln(R.N - n + 1))
    return np.where(i >= n, np.exp(logw), 0.0)


def untie(w, rs):
    """Best-of-n with ties broken at random: by symmetry, each answer of a block of equal proxy scores gets the block's
    average weight. One fixed order among ties would give the gold curve the same mean, but its divergences would
    charge that order as departure (KL is convex)."""
    starts = np.r_[0, np.flatnonzero(np.diff(rs)) + 1]
    sizes = np.diff(np.r_[starts, len(rs)])
    return np.repeat(np.add.reduceat(w, starts) / sizes, sizes)


def chernoff(p, r):
    lams = np.linspace(0.0, 1.0, 201)
    keep = (p > 0) & (r > 0)
    return float(-min(np.log(np.sum(p[keep] ** l * r[keep] ** (1 - l))) for l in lams))


def per_prompt(Fs, rs, q):
    """Fs: gold scores sorted by the proxy, ascending; rs: the proxy scores, in the same order; q: the empirical
    behaviour (uniform)."""
    from scipy.special import logsumexp
    out = {}
    log_mean_exp = logsumexp(np.outer(T_GRID, Fs), axis=1) - np.log(R.N)       # log E_q[e^{tF}], q uniform
    for n in NS:
        p = untie(bon_weights(n), rs)
        M, t_star = misalignment(p, q, Fs)
        # the boundary cases of [P5](iv) and [P9]: an infinite intensity is the limit q(.|A) on the best outcomes
        nearest = best_outcomes_limit(q, Fs) if np.isinf(t_star) else tilt(q, t_star * Fs)
        S, lam = shortfall(p, q, Fs)
        finite = bool(np.isfinite(lam) and lam > 0)
        pursuit = kl(nearest, q)
        # under-pursuit KL(p° || p_{F,lam}) = KL(p° || q) - lam E_{p°}[F] + log E_q[e^{lam F}], in closed form: at the
        # large matched intensities met here, tilt(q, lam F) underflows to zeros and a direct KL would be infinite
        under = pursuit - lam * float(nearest @ Fs) + float(logsumexp(lam * Fs) - np.log(R.N)) if finite else float("nan")
        out[n] = {"departure": kl(p, q), "M": M, "pursuit": pursuit, "t_star": t_star, "lambda": lam,
                  "S": S, "under": under, "lambda_finite": finite,
                  "gain": float(p @ Fs - q @ Fs),
                  "chernoff": chernoff(p, nearest) if n == 16 else float("nan"),
                  # KL(p || tilt(q, tF)) on the grid: KL(p||q) - t E_p[F] + log E_q[e^{tF}]
                  "kl_on_grid": kl(p, q) - T_GRID * float(p @ Fs) + log_mean_exp}
    u = (np.arange(R.N) + 0.5) / R.N
    out["bins"] = [float(Fs[(u >= a) & (u < b)].mean()) for a, b in zip(BINS[:-1], BINS[1:])]
    m100 = np.repeat([Fs[k * R.N // 100:(k + 1) * R.N // 100].mean() for k in range(100)], R.N // 100)
    out["residual_share"] = float(np.var(Fs - m100) / np.var(Fs))
    out["sd_gold"] = float(Fs.std())
    return out


def main(folder):
    weights = np.load(HERE / "proxy.npz")["weights"]
    q = np.full(R.N, 1.0 / R.N)
    rows, k = [], 0
    for j in range(1, 11):
        for rec in json.loads((Path(folder) / "validation" / f"split_{j}.json").read_text()):
            F = np.asarray(rec["gold_scores"], dtype=float)
            r = features(rec["answers"]) @ weights
            perm = np.random.default_rng(R.SEED + k).permutation(R.N)
            order = perm[np.argsort(r[perm], kind="stable")]
            rows.append(per_prompt(F[order], r[order], q)); k += 1
        print(f"split_{j}", flush=True)
    import pickle                                 # per-prompt rows stay outside the repository (README, working agreements)
    (Path(folder).parent / "w1_report_rows.pkl").write_bytes(pickle.dumps(rows))
    aggregate(rows)


def aggregate(rows):
    rng = np.random.default_rng(SEED)
    idx = [rng.integers(0, len(rows), len(rows)) for _ in range(BOOT)]

    def summary(values):
        values = np.asarray(values, dtype=float)
        boots = [np.nanmean(values[i]) for i in idx]
        return {"mean": float(np.nanmean(values)), "interval_95": [float(x) for x in np.percentile(boots, [2.5, 97.5])]}

    report = {"n": {}, "regression_by_rank": {}, "prompts": len(rows)}
    for n in NS:
        report["n"][str(n)] = {key: summary([row[n][key] for row in rows])
                               for key in ["departure", "M", "pursuit", "S", "gain", "chernoff"]}
        finite = [row[n] for row in rows if row[n]["lambda_finite"]]
        report["n"][str(n)]["prompts_with_finite_lambda"] = len(finite)
        report["n"][str(n)]["prompts_losing_gold"] = int(sum(row[n]["gain"] < 0 for row in rows))
        report["n"][str(n)]["prompts_without_departure"] = int(sum(row[n]["departure"] < 1e-9 for row in rows))
        for key in ["t_star", "lambda"]:
            values = np.array([row[n][key] for row in rows])
            report["n"][str(n)][key] = {"median": float(np.median(values)), "share_infinite": float(np.mean(np.isinf(values))),
                                        "share_zero": float(np.mean(values == 0))}
        report["n"][str(n)]["under"] = summary([row[n]["under"] for row in rows])      # NaN where lambda is infinite
        report["n"][str(n)]["M_share_of_departure"] = summary([row[n]["M"] / row[n]["departure"] for row in rows])
        report["n"][str(n)]["identity_max_error"] = float(max(
            [abs(row[n]["departure"] - row[n]["pursuit"] - row[n]["M"]) for row in rows] +
            [abs(row["lambda"] * row["S"] - row["M"] - row["under"] - row["lambda"] * max(-row["gain"], 0.0))
             for row in finite]))                       # [P9](ii): misalignment, under-pursuit and anti-pursuit
    for b, (a, c) in enumerate(zip(BINS[:-1], BINS[1:])):
        report["regression_by_rank"][f"{a:g}-{c:g}"] = summary([row["bins"][b] for row in rows])
    report["residual_share_100_bins"] = summary([row["residual_share"] for row in rows])
    report["sd_gold"] = summary([row["sd_gold"] for row in rows])
    report["identity_max_error"] = max(report["n"][str(n)]["identity_max_error"] for n in NS)
    # the specification shared across prompts: pursuit of the gold in every prompt at one intensity (derived/estimation.md,
    # the Notes of [P24]): M = min_t of the mean over prompts of KL(p_c || p_{c,F,t}), at least the mean of the M_c
    for n in NS:
        G = np.array([row[n]["kl_on_grid"] for row in rows])
        Mc = np.array([row[n]["M"] for row in rows])
        shared = lambda i: float(G[i].mean(0).min())
        boots = [shared(i) for i in idx]
        k = int(G.mean(0).argmin())
        report["n"][str(n)]["shared"] = {
            "M": {"mean": shared(slice(None)), "interval_95": [float(x) for x in np.percentile(boots, [2.5, 97.5])]},
            "inconsistency": {"mean": shared(slice(None)) - float(Mc.mean()),
                              "interval_95": [float(x) for x in np.percentile(
                                  [b - Mc[i].mean() for b, i in zip(boots, idx)], [2.5, 97.5])]},
            "t": float(T_GRID[k]), "t_at_grid_edge": k in (0, len(T_GRID) - 1),
            "grid_check": float((G.min(1) - Mc).min())}      # each prompt's grid minimum is at least its M_c
    (HERE / "report.json").write_text(json.dumps(report, indent=1))
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    if sys.argv[1] == "--aggregate":           # aggregate again from the saved per-prompt rows, without recomputing
        import pickle
        aggregate(pickle.loads(Path(sys.argv[2]).read_bytes()))
    else:
        main(sys.argv[1])
