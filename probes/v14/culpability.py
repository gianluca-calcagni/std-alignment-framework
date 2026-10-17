"""Q61, NOTES.md §25: the excess E = M_A(p) − M_A(𝓕) against the evidence K = KL(p‖f*) that the actor is not doing the
best it could, on random feasible sets (mixtures of three behaviours) that cannot avoid a breach of a rate limit.
Exploratory, not a check. Run from the repository's root: python3 probes/v14/culpability.py   (a few seconds)
"""
import numpy as np
from scipy.optimize import minimize
rng=np.random.default_rng(7)
def kl(p,a):
    m=p>0
    return np.inf if np.any(a[m]<=0) else float(np.sum(p[m]*np.log(p[m]/a[m])))
def kl2(u,v): return kl(np.array([u,1-u]),np.array([v,1-v]))
viol=0; tot=0; worst=-np.inf
for _ in range(400):
    n=5; C=np.array([1,1,0,0,0],bool); eps=0.1
    MA=lambda a: kl2(a[C].sum(),eps) if a[C].sum()>eps else 0.0
    V=rng.dirichlet(np.ones(n),size=3)          # feasible set: mixtures of three behaviours
    V[:,C]+=0.3; V/=V.sum(1,keepdims=True)      # push them to breach
    mix=lambda w: (np.abs(w)/np.abs(w).sum())@V
    r = min((minimize(lambda w: MA(mix(w)), rng.random(3), method="Nelder-Mead",
                      options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 4000}) for _ in range(5)),
            key=lambda r: r.fun)
    fstar=mix(r.x); unavoid=r.fun
    if unavoid<1e-9: continue
    w=rng.dirichlet(np.ones(3)); p=w@V
    E = MA(p) - unavoid; Cu = kl(p, fstar)   # f*: the best feasible behaviour found; K against it
    tot+=1; worst=max(worst,E-Cu); viol+= E>Cu+1e-7
print(f"{tot} instances with an unavoidable breach: excess > evidence against the best feasible in {viol}; "
      f"largest excess − evidence {worst:.3g}")
