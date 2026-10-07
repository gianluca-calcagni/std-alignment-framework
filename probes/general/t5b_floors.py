"""T5b. Does the compromise of principals with floors always sit at their floors?"""
import numpy as np
from scipy.optimize import minimize, minimize_scalar
rng = np.random.default_rng(55)
tilt = lambda r, f: r * np.exp(f - f.max()) / np.sum(r * np.exp(f - f.max()))
kl = lambda a, b: float(np.sum(a * np.log(a / b)))
def run(q, Fs, w, floors):
    def nearest(p, F, fl):
        res = minimize_scalar(lambda s: kl(p, tilt(q, (fl + np.exp(s)) * F)), bounds=(-30, 5), method="bounded")
        a = kl(p, tilt(q, fl * F))
        return (a, fl) if a <= res.fun else (res.fun, fl + np.exp(res.x))
    obj = lambda z: sum(wk * nearest(tilt(q, z), F, fl)[0] for wk, F, fl in zip(w, Fs, floors))
    best = min((minimize(obj, rng.normal(size=len(q)), method="BFGS") for _ in range(3)), key=lambda r: r.fun)
    p = tilt(q, best.x)
    return [nearest(p, F, fl)[1] - fl for F, fl in zip(Fs, floors)]
X = 6
for label, rho in (("independent objectives", 0.0), ("nearly identical objectives", 0.98)):
    at_floor = 0
    for _ in range(20):
        q = rng.dirichlet(np.ones(X) * 2); common = rng.normal(size=X)
        Fs = [rho * common + np.sqrt(1 - rho ** 2) * rng.normal(size=X) for _ in range(3)]
        excess = run(q, Fs, rng.dirichlet(np.ones(3)), (0.5, 1.0, 1.5))
        at_floor += all(e < 1e-3 for e in excess)
    print(f"T5b {label}: all principals exactly at their floors in {at_floor} of 20 instances")
