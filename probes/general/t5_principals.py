"""T5. Several principals: gridlock without floors; with floors, the compromise is a pursuit of a weighted sum."""
import numpy as np
from scipy.optimize import minimize, minimize_scalar
rng = np.random.default_rng(5)
X = 6; q = rng.dirichlet(np.ones(X) * 2); Fs = rng.normal(size=(3, X)); w = np.array([0.2, 0.5, 0.3])
tilt = lambda r, f: r * np.exp(f - f.max()) / np.sum(r * np.exp(f - f.max()))
kl = lambda a, b: float(np.sum(a * np.log(a / b)))
def nearest(p, F, floor):
    res = minimize_scalar(lambda s: kl(p, tilt(q, (floor + np.exp(s)) * F)), bounds=(-30, 5), method="bounded")
    at_floor = kl(p, tilt(q, floor * F))
    return (at_floor, floor) if at_floor <= res.fun else (res.fun, floor + np.exp(res.x))
def avg(z, floors):
    p = tilt(q, z)
    return sum(wk * nearest(p, F, fl)[0] for wk, F, fl in zip(w, Fs, floors))
for floors in ((0.0, 0.0, 0.0), (0.5, 1.0, 1.5)):
    best = min((minimize(avg, rng.normal(size=X), args=(floors,), method="Nelder-Mead",
                         options={"xatol": 1e-11, "fatol": 1e-14, "maxiter": 40000, "maxfev": 40000}) for _ in range(6)),
               key=lambda r: r.fun)
    p = tilt(q, best.x); ts = [nearest(p, F, fl)[1] for F, fl in zip(Fs, floors)]
    y = np.log(p / q); A = np.column_stack([np.ones(X)] + list(Fs))
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = np.linalg.norm(y - A @ coef) / np.linalg.norm(y - y.mean()) if np.ptp(y) > 1e-9 else 0.0
    print(f"T5 floors {floors}: weighted misalignment {best.fun:.3e}; KL(p*||q) {kl(p, q):.3e}; relative residual {resid:.2e}")
    if max(floors) > 0:
        print(f"    coefficients {coef[1:].round(4)} against w·t {np.array([wk * tk for wk, tk in zip(w, ts)]).round(4)} (nearest intensities {np.round(ts, 4)})")
