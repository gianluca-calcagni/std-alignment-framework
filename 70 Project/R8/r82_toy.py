"""R8-2 toy: a rule written as a level constraint inside the intended set (R8-2 preregistration, P1-P2)."""
import numpy as np
from scipy.optimize import brentq, minimize_scalar, minimize
from scipy.special import logsumexp

def tilt(lq, h):
    l = lq + h; return np.exp(l - logsumexp(l))
def KL(p, r): return float(np.sum(p*(np.log(p) - np.log(r))))

def level_point(lq, F, G, v, t):
    p = tilt(lq, t*F)
    if p@G >= v: return p, 0.0
    f = lambda mu: tilt(lq, t*F + mu*G)@G - v
    hi = 1.0
    while f(hi) < 0: hi *= 2
    mu = brentq(f, 0.0, hi, xtol=1e-13, rtol=1e-15)
    return tilt(lq, t*F + mu*G), mu

def dist_to_L(m, lq, F, G, v):
    ts = np.linspace(0, 5, 2001)
    d = [KL(m, level_point(lq, F, G, v, t)[0]) for t in ts]
    i = int(np.argmin(d)); a, b = ts[max(i-1, 0)], ts[min(i+1, 2000)]
    r = minimize_scalar(lambda t: KL(m, level_point(lq, F, G, v, t)[0]), bounds=(a, b), method="bounded",
                        options={"xatol": 1e-12})
    return min(d[i], r.fun)

rng = np.random.default_rng(4242)
kept = 0; p1_min = np.inf; p2_ok = 0; p2_worst = []; fines = []
for inst in range(400):
    n = int(rng.integers(3, 7))
    while True:
        q = rng.dirichlet(np.ones(n))
        if q.min() >= 1e-3: break
    lq = np.log(q); F = rng.normal(size=n); G = rng.normal(size=n)
    e0, e5 = tilt(lq, 0*F)@G, tilt(lq, 5*F)@G
    if abs(e0 - e5) < 1e-9: continue
    v = 0.5*(e0 + e5); kept += 1
    p0, mu0 = level_point(lq, F, G, v, 0.0); p5, mu5 = level_point(lq, F, G, v, 5.0)
    lm = 0.5*(np.log(p0) + np.log(p5)); m = np.exp(lm - logsumexp(lm))
    p1_min = min(p1_min, dist_to_L(m, lq, F, G, v))
    t0 = 0.0 if e0 < v else 5.0; ph = tilt(lq, t0*F)
    mfree = minimize_scalar(lambda t: KL(ph, tilt(lq, t*F)), bounds=(0, 50), method="bounded", options={"xatol": 1e-12}).fun
    cone = minimize(lambda x: KL(ph, tilt(lq, x[0]*F + x[1]*G)), x0=[t0 + 0.1, 0.1], bounds=[(0, 60), (0, 60)],
                    method="L-BFGS-B", options={"ftol": 1e-15, "gtol": 1e-12}).fun
    comp = ph@G - v; lev = dist_to_L(ph, lq, F, G, v)
    ok = max(mfree, 0) <= 1e-12 and max(cone, 0) <= 1e-12 and comp < 0 and lev > 1e-6
    p2_ok += ok
    if not ok: p2_worst.append((inst, mfree, cone, comp, lev))
    mu, t = (mu5, 5.0) if mu5 > 0 else (mu0, 0.0)
    if t > 0: fines.append(mu/t)
print(f"kept {kept} of 400")
print(f"P1 level-form set not log-convex: min KL distance of the endpoint midpoint to L {p1_min:.3e} -> {'holds' if p1_min > 1e-6 else 'FAILS'}")
print(f"P2 rule-13 agent: {p2_ok} of {kept} as predicted -> {'holds' if p2_ok == kept else 'FAILS'}")
for w in p2_worst[:5]: print("   exception", w)
if fines: print(f"reported: implicit fine mu/t at t = 5 where binding: median {np.median(fines):.3f}, range [{min(fines):.3f}, {max(fines):.3f}] over {len(fines)}")
