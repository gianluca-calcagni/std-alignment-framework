"""W3 calibration, before registration, on synthetic contexts only (seeds 31000 + ..., not used by the test).
z = t*r + a_c + noise, or z = t*s(p) + ..., where p = sigmoid(k*r) stands for the classifier's probability. Reports the
pooled within-context R2 of z on r and on p, and the bootstrap interval of their difference, over 300 contexts with
32 + 32 samples each, as registered. Usage: python3 synthetic.py"""
import numpy as np

C, K, BOOT = 300, 64, 1000


def pooled(z, x):
    """Pooled within-context R2 of z on x: per-context least squares with its own intercept."""
    zc = z - z.mean(1, keepdims=True); xc = x - x.mean(1, keepdims=True)
    slope = (zc * xc).sum(1) / (xc ** 2).sum(1)
    ssr = ((zc - slope[:, None] * xc) ** 2).sum(1); sst = (zc ** 2).sum(1)
    return ssr, sst


def run(truth, noise, seed, k=1.6, t=3.0):
    r_ = np.random.default_rng(seed)
    mu = r_.normal(0, 1.0, C)[:, None]
    r = mu + r_.normal(0, 1.5, (C, K))
    p = 1 / (1 + np.exp(-k * r))
    signal = t * r if truth == "logit" else t * 6 * p
    z = signal + r_.normal(0, 1, (C, 1)) + noise * r_.normal(0, 1, (C, K))
    ssr_r, sst = pooled(z, r); ssr_p, _ = pooled(z, p)
    R2r, R2p = 1 - ssr_r.sum() / sst.sum(), 1 - ssr_p.sum() / sst.sum()
    boots = []
    for _ in range(BOOT):
        i = r_.integers(0, C, C)
        boots.append((1 - ssr_r[i].sum() / sst[i].sum(), 1 - ssr_p[i].sum() / sst[i].sum()))
    boots = np.array(boots)
    lo_r = np.percentile(boots[:, 0], 2.5)
    lo_d, hi_d = np.percentile(boots[:, 0] - boots[:, 1], [2.5, 97.5])
    return R2r, lo_r, R2p, lo_d, hi_d


for truth in ("logit", "probability"):
    for noise in (0.0, 2.0, 4.5, 8.0):
        R2r, lo_r, R2p, lo_d, hi_d = run(truth, noise, 31000 + int(noise * 10) + (0 if truth == "logit" else 500))
        print(f"truth {truth:11s} noise {noise:4.1f}: R2(r) {R2r:.3f} (lower {lo_r:.3f}), R2(p) {R2p:.3f}, "
              f"difference 95% [{lo_d:+.3f}, {hi_d:+.3f}]")
