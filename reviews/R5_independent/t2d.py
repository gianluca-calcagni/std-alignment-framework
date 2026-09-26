import numpy as np
from scipy.optimize import minimize_scalar
from t2 import KL, gibbs, bon, vpg_path
rng=np.random.default_rng(1); cov=lambda q,a,b: q@(a*b)-(q@a)*(q@b)
print('[T-B, VPG] q-covariance positive, q^2-weighted covariance negative')
M=1000; K=5; w=np.r_[np.full(K,12.0),np.ones(M-K)]; q=w/w.sum()
F=rng.normal(size=M); Fh=F+0.2*rng.normal(size=M)       # light states: aligned
F[:K]=np.array([3,-3,3,-3,3.]); Fh[:K]=-F[:K]*1.0         # heavy states: strongly anti-aligned
qq=q**2/np.sum(q**2)
print(f'  mass on heavy states: q {q[:K].sum():.3f}, q^2-weights {qq[:K].sum():.3f}')
print(f'  Cov_q(Fh,F) = {cov(q,Fh,F):+.3f}   Cov_q2(Fh,F) = {cov(qq,Fh,F):+.3f}')
P=vpg_path(q,Fh,eta=0.5,steps=201,every=1)
print(f'  Gibbs gain, beta=1e-3: {gibbs(q,Fh,1e-3)@F-q@F:+.2e}   (predicts help)')
print(f'  VPG gain after 1, 10, 200 steps: {P[1]@F-q@F:+.2e}, {P[10]@F-q@F:+.2e}, {P[200]@F-q@F:+.2e}')
print(f'  exact VPG initial velocity sum_x q_x^2 (F-EqF)(Fh-EqFh) = {np.sum(q**2*(F-q@F)*(Fh-q@Fh)):+.2e}')

print('\n[T-C] zero value regret, positive detection exponent (BoN)')
N=500; q=np.ones(N)/N; lev=rng.integers(0,5,size=N).astype(float); F=lev      # 5 tied levels
E=0.3*rng.uniform(size=N)                                               # |E|<gap: reorders only WITHIN levels
def chern(p,s):
    m=(p>0)&(s>0); r=minimize_scalar(lambda l: np.log(np.sum(p[m]**l*s[m]**(1-l))),bounds=(0,1),method='bounded'); return -r.fun
# BoN with ties: bon() breaks ties by index order; for the intended actor use uniform tie-breaking within level
def bon_ties(q,G,n):
    vals=np.unique(G); p=np.zeros_like(q)
    for v in vals:
        m=G==v; U=q[G<=v].sum(); Um=q[G<v].sum(); p[m]=(U**n-Um**n)*q[m]/q[m].sum()
    return p
for n in [2,8,64]:
    ps=bon_ties(q,F,n); ph=bon(q,F+E,n)
    print(f'  n={n:2d}: value regret {ps@F-ph@F:+.1e}   Chernoff {chern(ph,ps):.3f} nats/sample   KL(ph||p*) {KL(ph,ps):.3f}')
b=2.0; ps,ph=gibbs(q,F,b),gibbs(q,F+E,b)
print(f'  Gibbs beta={b}: value regret dF {ps@F-ph@F:+.2e};  beta*R_J = KL(ph||p*) = {KL(ph,ps):.4f};  Chernoff {chern(ph,ps):.4f}')
print('  -> for Gibbs the bound holds because R_J charges the information cost; dF can be ~0 or negative.')

print('\n[T-D, VPG] Gaussian joint, uniform q, traced path')
N=20000; x=rng.normal(size=(N,2)); rho=0.6; Fh=x[:,0]; F=rho*x[:,0]+np.sqrt(1-rho**2)*x[:,1]; q=np.ones(N)/N
P=vpg_path(q,Fh,eta=40.0,steps=6000,every=600)
print('  sqrt(KL) / gold gain / gold:proxy  ->  '+'; '.join(f'{np.sqrt(KL(p,q)):.2f}/{p@F-q@F:.3f}/{(p@F-q@F)/(p@Fh-q@Fh):.3f}' for p in P[1:]))
# non-uniform q correlated with the residual: does VPG overoptimize?
res=x[:,1]; qn=np.exp(0.8*res); qn/=qn.sum()
print(f'  non-uniform q ∝ exp(0.8·residual): under this q, F and Fh are no longer jointly Gaussian-with-independent-residual; skipped as out of B4 scope')
