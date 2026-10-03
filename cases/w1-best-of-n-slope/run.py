"""Case W1: the best-of-n slope on unseen answers. Computes exactly what REGISTRATION.md says.

Usage: python3 run.py <folder holding validation/split_1.json ... split_10.json>   (writes output.json next to this file)
Prompts are numbered k = 0, ..., 999 in the order split_1, split_2, ..., split_10, records in file order.
"""
import hashlib, json, sys, time
from pathlib import Path
import numpy as np
from scipy.special import gammaln
from train_proxy import features

HERE = Path(__file__).resolve().parent
PROXY_SHA256 = "a58685aed890c8e9d677cee13ea200271fb810488824fc6f3d9be9d0fc0310ea"
N, NMAX, SEED, BOOT = 12600, 12500, 20261003, 2000
GRID = np.unique(np.round(10 ** (np.arange(200) * np.log10(NMAX) / 199)).astype(int))
D = np.sqrt(np.log(GRID) - (GRID - 1) / GRID)
I = np.arange(1, N + 1)
LOGW = (gammaln(I[None, :]) - gammaln(GRID[:, None]) - gammaln(I[None, :] - GRID[:, None] + 1)
        - (gammaln(N + 1) - gammaln(GRID[:, None] + 1) - gammaln(N - GRID[:, None] + 1)))
W = np.where(I[None, :] >= GRID[:, None], np.exp(np.where(I[None, :] >= GRID[:, None], LOGW, 0.0)), 0.0)
G = np.log((I - 0.5) / N); G = G - G.mean(); SG = G.std()
A = np.c_[D[1:], -D[1:] ** 2]


def fit(curve, mask=None):
    m = np.ones(len(GRID) - 1, bool) if mask is None else mask
    return np.linalg.lstsq(A[m], (curve[1:] - curve[0])[m], rcond=None)[0]


def main(folder):
    proxy = HERE / "proxy.npz"
    assert hashlib.sha256(proxy.read_bytes()).hexdigest() == PROXY_SHA256, "the proxy is not the registered one"
    weights = np.load(proxy)["weights"]
    curves, c, corr, ties, k, start = [], [], [], [], 0, time.time()
    for j in range(1, 11):
        records = json.loads((Path(folder) / "validation" / f"split_{j}.json").read_text())
        for rec in records:
            answers, F = rec["answers"], np.asarray(rec["gold_scores"], dtype=float)
            assert len(answers) == N and len(F) == N
            r = features(answers) @ weights
            perm = np.random.default_rng(SEED + k).permutation(N)
            order = perm[np.argsort(r[perm], kind="stable")]
            Fs = F[order]
            c.append(float(np.mean(G * (Fs - Fs.mean())) / SG))
            curves.append(W @ Fs)
            corr.append(float(np.corrcoef(r, F)[0, 1]))
            ties.append(int(N - len(np.unique(r))))
            k += 1
        print(f"split_{j}: {k} prompts, {time.time() - start:.0f}s", flush=True)
    curves, c = np.array(curves), np.array(c)
    a_pred = float(np.sqrt(2) * c.mean())
    a_fit, b_fit = (float(x) for x in fit(curves.mean(0)))
    rng = np.random.default_rng(SEED)
    boot = []
    for _ in range(BOOT):
        idx = rng.integers(0, len(c), len(c))
        boot.append((fit(curves[idx].mean(0))[0], np.sqrt(2) * c[idx].mean()))
    boot = np.array(boot)
    diffs = boot[:, 0] - boot[:, 1]
    lo, hi = (float(x) for x in np.percentile(diffs, [2.5, 97.5]))
    g = curves.mean(0)
    near = GRID[1:] <= 16
    result = {
        "registered": {"a_pred": a_pred, "a_fit": a_fit, "b_fit": b_fit, "D": a_fit - a_pred,
                       "D_interval_95": [lo, hi], "verdict": "held" if lo <= 0 <= hi else "refuted"},
        "reported": {"a_pred_interval_95": [float(x) for x in np.percentile(boot[:, 1], [2.5, 97.5])],
                     "a_fit_interval_95": [float(x) for x in np.percentile(boot[:, 0], [2.5, 97.5])],
                     "a_fit_n_le_16": float(fit(g, near)[0]),
                     "peak_n": int(GRID[np.argmax(g)]), "gain_at_peak": float(g.max() - g[0]),
                     "gain_at_n_max": float(g[-1] - g[0]), "falls_by_n_max": bool(g[-1] < g.max()),
                     "proxy_gold_correlation_mean": float(np.mean(corr)),
                     "prompts_with_ties": int(np.sum(np.array(ties) > 0)), "tied_answers_total": int(np.sum(ties)),
                     "prompts": int(len(c))},
        "curve": {"n": GRID.tolist(), "d": D.tolist(), "gold_mean": g.tolist()},
        "per_prompt": {"c": c.tolist(), "proxy_gold_correlation": corr, "ties": ties},
    }
    (HERE / "output.json").write_text(json.dumps(result, indent=1))
    print(json.dumps({k: result[k] for k in ("registered", "reported")}, indent=1))


if __name__ == "__main__":
    main(sys.argv[1])
