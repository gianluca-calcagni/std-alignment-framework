"""B7. Attention as misalignment against 'ignoring the situation': the mutual information between condition and action."""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(7)
kl = lambda a, b: float(np.sum(a * np.log(a / b)))
worst = 0.0
for _ in range(20):
    C, X = 4, 5
    rho = rng.dirichlet(np.ones(C)); P = rng.dirichlet(np.ones(X), size=C)
    avg = rho @ P
    mi = float(np.sum(rho[:, None] * P * np.log(P / avg)))
    obj = lambda z: sum(r * kl(p, np.exp(z) / np.exp(z).sum()) for r, p in zip(rho, P))
    best = min((minimize(obj, rng.normal(size=X), method="BFGS", options={"gtol": 1e-12}) for _ in range(3)), key=lambda r: r.fun)
    worst = max(worst, abs(best.fun - mi), abs(obj(np.log(avg)) - mi))
print(f"B7: largest gap between the misalignment against 'ignoring the situation' and the mutual information: {worst:.1e}")
