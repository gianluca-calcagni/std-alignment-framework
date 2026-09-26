import numpy as np
from scipy.special import logsumexp
np.set_printoptions(precision=4, suppress=True)
def KL(p,q):
    m=p>0; return float(np.sum(p[m]*np.log(p[m]/q[m])))
def gibbs(q,G,t):
    l=np.log(q)+t*G; return np.exp(l-logsumexp(l))
def bon(q,G,n):
    """exact best-of-n law on finite X (ties broken uniformly within a value level)"""
    o=np.argsort(G,kind='stable'); qs=q[o]; U=np.cumsum(qs); Um=U-qs
    p=np.empty_like(q); p[o]=U**n-Um**n; return p
def vpg_path(q,G,eta=0.5,steps=60000,every=50):
    th=np.log(q).copy(); out=[]
    for k in range(steps):
        p=np.exp(th-logsumexp(th))
        if k%every==0: out.append(p.copy())
        th+=eta*p*(G-p@G)
    return out
def at_kl(path,q,d):
    ks=np.array([KL(p,q) for p in path]); i=np.searchsorted(ks,d)
    if i==0 or i>=len(ks): return None
    a=(d-ks[i-1])/(ks[i]-ks[i-1]); return (1-a)*path[i-1]+a*path[i]

# ---------------- T-A: crossing on the V5 pair ----------------
if __name__=="__main__":
    rng=np.random.default_rng(5); N=2000; q=np.ones(N)/N; F=rng.normal(size=N)
    E1=rng.normal(size=N)*0.6; E2=np.zeros(N); E2[11]=6.0
    print('[T-A] V5 pair: Var_q E1=%.3f  Var_q E2=%.4f  osc E1=%.2f osc E2=%.1f'%(q@E1**2-(q@E1)**2, q@E2**2-(q@E2)**2, np.ptp(E1), np.ptp(E2)))
    print('  BoN:   n      KL      R(E1)     R(E2)    ratio')
    for n in [2,4,16,64,256,1024,4096,2**14,2**16,2**18,2**20]:
        pF=bon(q,F,n); R=[pF@F - bon(q,F+E,n)@F for E in (E1,E2)]
        print(f'  {n:8d} {KL(pF,q):7.3f} {R[0]:9.5f} {R[1]:9.5f} {R[0]/max(R[1],1e-300):9.3g}')
    print('  VPG (unregularized, early-stopped, matched KL):')
    pathF=vpg_path(q,F); paths=[vpg_path(q,F+E) for E in (E1,E2)]
    for d in [0.01,0.05,0.2,0.5,1,2,3,4,5]:
        pf=at_kl(pathF,q,d); ps=[at_kl(P,q,d) for P in paths]
        if pf is None or any(x is None for x in ps): print(f'   d={d}: out of path range'); continue
        R=[pf@F-p@F for p in ps]; print(f'   d={d:5}: R(E1)={R[0]:.5f} R(E2)={R[1]:.5f} ratio={R[0]/R[1]:.3g}')
