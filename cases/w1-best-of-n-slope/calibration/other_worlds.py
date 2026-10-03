"""W1 calibration, before registration, on synthetic prompts only: the registered procedure in worlds where the
literature's form fits badly (gold falling at the top proxy ranks) and with heavy-tailed noise. Seeds 97000 + ..., not
used by the test. Usage: python3 other_worlds.py"""
import numpy as np
exec(open("registered_procedure.py").read().split("for rho in (0.2, 0.4):")[0])


def world(kind, rho, seed):
    r = np.random.default_rng(seed)
    curves = np.empty((P, len(grid))); covs = np.empty(P)
    for p in range(P):
        x = r.standard_normal(N)
        if kind == "falls at the top":
            F = rho * x - 0.5 * np.maximum(0, x - 2.0) ** 2 + np.sqrt(1 - rho ** 2) * r.standard_normal(N)
        else:
            F = rho * x + np.sqrt(1 - rho ** 2) * r.standard_t(3, N) / np.sqrt(3)
        Fs = F[np.argsort(x, kind="stable")]
        curves[p] = W @ Fs; covs[p] = np.mean(G * (Fs - Fs.mean())) / sG
    D = fit(curves.mean(0)) - np.sqrt(2) * covs.mean()
    Ds = [fit(curves[idx].mean(0)) - np.sqrt(2) * covs[idx].mean() for idx in (r.integers(0, P, P) for _ in range(BOOT))]
    lo, hi = np.percentile(Ds, [2.5, 97.5])
    print(f"{kind}, rho {rho}: D {D:+.4f}, 95% [{lo:+.4f}, {hi:+.4f}], {'held' if lo <= 0 <= hi else 'refuted'}")


for kind in ("falls at the top", "heavy-tailed noise"):
    for rho in (0.2, 0.4):
        world(kind, rho, 97000 + int(rho * 10) + (0 if kind.startswith("falls") else 5))
