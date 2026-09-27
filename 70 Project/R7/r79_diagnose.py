# R7-9 post-hoc diagnosis of P2 and P3 (failed as registered). NOT pre-registered, not a verify.py block.
# Regenerates V37's P3 instances exactly and compares the generic conic-hull value with the closed form.
import sys, os, inspect; sys.path.insert(0, os.getcwd())
import numpy as np
import verify as Vf
from scipy.special import logsumexp
from scipy.optimize import minimize
rng = np.random.default_rng(3709)
# replay the RNG consumption of V37's P1-P2 loop
for i in range(400):
    n = int(rng.integers(3, 11)); K = [2, 3, 5][i % 3]
    L = np.log(rng.dirichlet(np.ones(n), size=K)); lh = np.log(rng.dirichlet(np.ones(n)))
    starts = [rng.dirichlet(np.ones(K)) for _ in range(5)]
    for _ in range(20): rng.dirichlet(np.ones(K))
above = below = 0; worst = []
for i in range(300):
    n = int(rng.integers(3, 11))
    while True:
        q = rng.dirichlet(np.ones(n))
        if q.min() >= 1e-3: break
    lq = np.log(q); lh = np.log(rng.dirichlet(np.ones(n)))
    F = rng.normal(size=n) if i % 2 else rng.integers(0, 4, size=n).astype(float)
    if len(np.unique(F)) < 2: F[0] += 1.0
    s = float(rng.uniform(0.2, 5)); ph = np.exp(lh)
    L = np.vstack([lq, Vf.lgibbs(lq, F, s)])
    Vf._hull_proj(lh, L, [np.array([a, 1 - a]) for a in (0.1, 0.5, 0.9)])
    vals = np.unique(F); steps = np.array([(F >= v_).astype(float) for v_ in vals[1:]])
    Lc = np.vstack([lq, steps]); bnds = [(1.0, 1.0)] + [(0, None)]*len(steps)
    starts = [np.concatenate([[1.0], rng.uniform(0, 2, len(steps))]) for _ in range(3)]
    vo = min(r[0] for r in Vf._hull_proj(lh, Lc, starts, bounds=bnds))
    mo = Vf.KL(ph, Vf._ordproj(ph, q, F)[0])
    # a better generic solve: the conic problem in the unconstrained variables w = exp(u) is smooth; restart from the closed form's weights
    if vo - mo > 1e-8: above += 1
    if mo - vo > 1e-8: below += 1
    worst.append((vo - mo, n, len(vals)))
worst.sort()
print(f"generic minus closed form, over 300 instances: generic above by > 1e-8 in {above}; generic below by > 1e-8 in {below}")
print("largest positive gaps (generic - closed form, n, levels):", [(f'{g:.1e}', a, b) for g, a, b in worst[-5:]])
print("most negative gaps:", [(f'{g:.1e}', a, b) for g, a, b in worst[:3]])

# re-solve the one instance where the generic value is above, from many starts and with a tighter solver
rng2 = np.random.default_rng(3709)
for i in range(400):
    n = int(rng2.integers(3, 11)); K = [2, 3, 5][i % 3]
    rng2.dirichlet(np.ones(n), size=K); rng2.dirichlet(np.ones(n)); [rng2.dirichlet(np.ones(K)) for _ in range(5)]
    for _ in range(20): rng2.dirichlet(np.ones(K))
for i in range(300):
    n = int(rng2.integers(3, 11))
    while True:
        q = rng2.dirichlet(np.ones(n))
        if q.min() >= 1e-3: break
    lq = np.log(q); lh = np.log(rng2.dirichlet(np.ones(n)))
    F = rng2.normal(size=n) if i % 2 else rng2.integers(0, 4, size=n).astype(float)
    if len(np.unique(F)) < 2: F[0] += 1.0
    s = float(rng2.uniform(0.2, 5)); ph = np.exp(lh)
    vals = np.unique(F); steps = np.array([(F >= v_).astype(float) for v_ in vals[1:]])
    starts = [np.concatenate([[1.0], rng2.uniform(0, 2, len(steps))]) for _ in range(3)]
    mo = Vf.KL(ph, Vf._ordproj(ph, q, F)[0])
    if len(vals) == 8 and n == 8:
        Lc = np.vstack([lq, steps]); bnds = [(1.0, 1.0)] + [(0, None)]*len(steps)
        more = [np.concatenate([[1.0], np.random.default_rng(k).uniform(0, 3, len(steps))]) for k in range(40)]
        v3 = min(r[0] for r in Vf._hull_proj(lh, Lc, starts, bounds=bnds))
        if v3 - mo < 1e-8: continue
        v2 = min(r[0] for r in Vf._hull_proj(lh, Lc, more, bounds=bnds))
        print(f"the failing instance (n = 8, 8 levels): closed form {mo:.10f}; the registered 3 starts give {v3:.10f} (+{v3 - mo:.1e}); 40 starts reach {v2:.10f} (difference {v2 - mo:.1e})")
        break
