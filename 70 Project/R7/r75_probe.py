# R7-5 go/no-go probe: is there a real case where the KL-based measurement layer gives a wrong verdict?
# Exploratory probe, NOT pre-registered (R7-5 go/no-go, v7.3.1). Seeded; run: python3 r75_probe.py; python3 r75_c5.py
# Case under test: best-of-n and quantilizers run on the TRUE target F (common in practice).
import numpy as np
from scipy.optimize import brentq, minimize
from scipy.special import logsumexp
rng = np.random.default_rng(7505)

def ltilt(q, F, t):
    l = np.log(q) + t * F; return l - logsumexp(l)
def tilt(q, F, t): return np.exp(ltilt(q, F, t))
def kl(p, r, lr=None):
    m = p > 0; lr = np.log(r) if lr is None else lr
    return float(np.sum(p[m] * (np.log(p[m]) - lr[m])))
def m_free(ph, q, F):
    # M(t) convex; stationary point where E_{p_t}F = E_ph F; t >= 0
    target = ph @ F
    if target <= q @ F: return kl(ph, q), 0.0
    g = lambda t: tilt(q, F, t) @ F - target
    hi = 1.0
    while g(hi) < 0 and hi < 1e9: hi *= 2
    if g(0) >= 0: return kl(ph, q), 0.0
    t = brentq(g, 0, hi, xtol=1e-12) if g(hi) >= 0 else hi
    return kl(ph, None, ltilt(q, F, t)), t
def bon(q, F, n):
    o = np.argsort(F); Q = np.cumsum(q[o]); Qm = np.concatenate([[0], Q[:-1]])
    p = np.empty_like(q); p[o] = Q**n - Qm**n; return p
def quant(q, F, a, eps=1e-3):
    o = np.argsort(F)[::-1]; p = np.zeros_like(q); left = a
    for i in o:
        take = min(q[i], left); p[i] = take; left -= take
        if left <= 0: break
    p = p / a; return (1 - eps) * p + eps * q
def pava(y, w):
    # weighted isotonic (non-decreasing) regression
    blocks = []
    for yi, wi in zip(y, w):
        blocks.append([yi * wi, wi, 1])
        while len(blocks) > 1 and blocks[-2][0] / blocks[-2][1] > blocks[-1][0] / blocks[-1][1]:
            s, ww, c = blocks.pop(); blocks[-1][0] += s; blocks[-1][1] += ww; blocks[-1][2] += c
    out = []
    for s, ww, c in blocks: out += [s / ww] * c
    return np.array(out)
def ord_proj(ph, q, F):
    o = np.argsort(F); r = pava(ph[o] / q[o], q[o]); p = np.empty_like(q); p[o] = q[o] * r; return p
def m_ord(ph, q, F):
    p0 = ord_proj(ph, q, F); return kl(ph, p0), p0
def generic_ord(ph, q, F):
    # generic check: min over log-ratios g, non-decreasing in F order, of KL(ph || q e^g / Z)
    o = np.argsort(F); n = len(q)
    def obj(g):
        l = np.log(q[o]) + g; lp = l - logsumexp(l); return -np.sum(ph[o] * lp)
    cons = [{'type': 'ineq', 'fun': (lambda g, k=k: g[k + 1] - g[k])} for k in range(n - 1)]
    best = np.inf
    for s in range(3):
        g0 = np.sort(rng.normal(size=n))
        r = minimize(obj, g0, constraints=cons, method='SLSQP', options={'ftol': 1e-14, 'maxiter': 2000})
        best = min(best, r.fun)
    return best + np.sum(ph[o] * np.log(ph[o]))   # = KL at the optimum

# ---- C2: PAVA solves the ordinal projection (vs a generic constrained optimizer)
gaps = []
for _ in range(60):
    n = rng.integers(4, 12); q = rng.dirichlet(np.ones(n)); F = rng.normal(size=n)
    ph = rng.dirichlet(np.ones(n))
    gaps.append(generic_ord(ph, q, F) - m_ord(ph, q, F)[0])
print(f"C2 PAVA vs generic optimizer, 60 instances: min(generic - PAVA) = {min(gaps):.1e} (negative would refute), max = {max(gaps):.1e}")

# ---- C1: best-of-n and quantilizer on the TRUE target: M_free > 0, M_ord = 0
rows = []
for _ in range(400):
    n = rng.integers(5, 60); q = rng.dirichlet(np.ones(n) * rng.choice([0.3, 1, 3])); F = rng.normal(size=n) * rng.choice([0.5, 1, 3])
    for kind, ph in (('bon4', bon(q, F, 4)), ('bon16', bon(q, F, 16)), ('bon64', bon(q, F, 64)), ('quant0.1', quant(q, F, 0.1)), ('quant0.3', quant(q, F, 0.3))):
        ph = np.maximum(ph, 1e-300); ph /= ph.sum()
        mf, _ = m_free(ph, q, F); mo, _ = m_ord(ph, q, F); kq = kl(ph, q)
        # budget-matched tilt and its target gain vs the actor's
        rows.append((kind, mf, mo, kq, mf / kq if kq > 0 else np.nan))
import collections
by = collections.defaultdict(list)
for r in rows: by[r[0]].append(r)
for k, v in by.items():
    v = np.array([x[1:] for x in v], dtype=float)
    print(f"C1 {k:9s}: M_free median {np.median(v[:,0]):.3f} [p5 {np.percentile(v[:,0],5):.3f}, p95 {np.percentile(v[:,0],95):.3f}]; "
          f"M_free/KL(p||q) median {np.nanmedian(v[:,3]):.2f}; M_free>1e-6 in {np.mean(v[:,0]>1e-6):.3f}; max M_ord {v[:,1].max():.1e}")

# ---- C3: misdirected actors: M_ord > 0 when the evaluator reorders; = 0 when it is a monotone transform
res = []
for _ in range(400):
    n = rng.integers(5, 40); q = rng.dirichlet(np.ones(n)); F = rng.normal(size=n); b = rng.uniform(0.5, 5)
    Fh_mono = np.exp(F) * rng.uniform(0.3, 3)                     # strictly increasing transform of F
    Fh_err = F + rng.normal(size=n) * rng.uniform(0.1, 1.0)       # an evaluator error that reorders
    ph1 = tilt(q, Fh_mono, b); ph2 = tilt(q, Fh_err, b)
    res.append((m_ord(ph1, q, F)[0], m_free(ph1, q, F)[0], m_ord(ph2, q, F)[0], m_free(ph2, q, F)[0]))
res = np.array(res)
print(f"C3 monotone-transform evaluator: max M_ord {res[:,0].max():.1e}; M_free median {np.median(res[:,1]):.3f} (>1e-6 in {np.mean(res[:,1]>1e-6):.2f})")
print(f"C3 reordering evaluator: M_ord > 1e-9 in {np.mean(res[:,2]>1e-9):.3f}; median M_ord/M_free {np.median(res[:,2]/res[:,3]):.2f}")

# ---- C4: does D_perp split? M_free(ph) vs M_ord(ph) + M_free(p0), p0 the ordinal projection
d = []
for _ in range(1000):
    n = rng.integers(3, 30); q = rng.dirichlet(np.ones(n)); F = rng.normal(size=n)
    ph = rng.dirichlet(np.ones(n) * rng.choice([0.3, 1, 3]))
    mo, p0 = m_ord(ph, q, F); mf, _ = m_free(ph, q, F); mf0, _ = m_free(p0, q, F)
    d.append(mf - (mo + mf0))
d = np.array(d)
print(f"C4 M_free - (M_ord + M_free(p0)) over 1000 instances: min {d.min():.2e}, max {d.max():.2e}, |.|<1e-10 in {np.mean(np.abs(d)<1e-10):.3f}")
