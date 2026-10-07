"""W1 calibration, before registration, on synthetic Gaussian prompts only (seeds 98000 + ..., not used by the
test): the registered procedure, run where the theory holds, to see how often it would declare a refutation.
Usage: python3 registered_procedure.py"""
import numpy as np
from scipy.special import gammaln
N, P, NMAX, BOOT = 12600, 1000, 12500, 1000
grid = np.unique(np.round(10 ** (np.arange(200) * np.log10(NMAX) / 199)).astype(int))
d = np.sqrt(np.log(grid) - (grid - 1) / grid)
i = np.arange(1, N + 1)
logw = (gammaln(i[None, :]) - gammaln(grid[:, None]) - gammaln(i[None, :] - grid[:, None] + 1)
        - (gammaln(N + 1) - gammaln(grid[:, None] + 1) - gammaln(N - grid[:, None] + 1)))
W = np.where(i[None, :] >= grid[:, None], np.exp(logw), 0.0)
G = np.log((i - 0.5) / N); G -= G.mean(); sG = G.std()
A = np.c_[d[1:], -d[1:] ** 2]
def fit(curve):
    return np.linalg.lstsq(A, curve[1:] - curve[0], rcond=None)[0][0]
def one(rho, seed):
    r = np.random.default_rng(seed)
    curves = np.empty((P, len(grid))); covs = np.empty(P)
    for p in range(P):
        x = r.standard_normal(N); F = rho * x + np.sqrt(1 - rho ** 2) * r.standard_normal(N)
        Fs = F[np.argsort(x, kind="stable")]
        curves[p] = W @ Fs; covs[p] = np.mean(G * (Fs - Fs.mean())) / sG
    D = fit(curves.mean(0)) - np.sqrt(2) * covs.mean()
    Ds = []
    for _ in range(BOOT):
        idx = r.integers(0, P, P)
        Ds.append(fit(curves[idx].mean(0)) - np.sqrt(2) * covs[idx].mean())
    lo, hi = np.percentile(Ds, [2.5, 97.5])
    return D, lo, hi, np.sqrt(2) * covs.mean()
for rho in (0.2, 0.4):
    for seed in range(3):
        D, lo, hi, ap = one(rho, 98000 + 10 * seed + int(rho * 10))
        print(f"rho {rho} seed {seed}: a_pred {ap:.4f}  D {D:+.4f}  95% [{lo:+.4f}, {hi:+.4f}]  {'held' if lo <= 0 <= hi else 'REFUTED'}", flush=True)
