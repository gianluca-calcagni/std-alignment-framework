"""R6 Task 2 — tier-4 transfer tests, as pre-registered in R6_T2_preregistration.md (sha256 99fde5a1...).
Actors: Gibbs capacity path, best-of-n (exact law), VPG (exact-gradient flow), NPG (Fisher solved by LSQR
at every step, not the closed form), KL-PG (exact-gradient flow of E_pG - KL/beta)."""
import numpy as np
from scipy.special import logsumexp
from scipy.optimize import brentq
from scipy.integrate import solve_ivp
from scipy.sparse.linalg import LinearOperator, lsqr

def KL(p, r):
    m = p > 0; return float(np.sum(p[m]*(np.log(p[m]) - np.log(r[m]))))
def softmax(th): return np.exp(th - logsumexp(th))
def tilt(q, G, t): return softmax(np.log(q) + t*G)

# ---------------- Gibbs (pure capacity actor) ----------------
def gibbs_at_kl(q, G, d):
    top = G >= G.max() - 1e-12
    if d >= np.log(1/q[top].sum()): raise ValueError('saturated')
    f = lambda lt: KL(tilt(q, G, np.exp(lt)), q) - d
    lo, hi = -30.0, 0.0
    while f(hi) < 0: hi += 1.0
    return tilt(q, G, np.exp(brentq(f, lo, hi, xtol=1e-14)))

# ---------------- best-of-n ----------------
def bon(q, G, n):
    o = np.argsort(G, kind='stable'); U = np.cumsum(q[o]); Um = U - q[o]
    p = np.empty_like(q); p[o] = U**n - Um**n; return p

# ---------------- gradient flows (VPG, KL-PG) ----------------
def flow_path(q, G, beta=None, T=1e7, npts=4000):
    """exact-gradient flow on logits from log q. beta=None: VPG on E_pG; else KL-PG on E_pG - KL(p||q)/beta.
    Returns (times, list of p) on a log time grid."""
    lq = np.log(q)
    def rhs(t, th):
        p = softmax(th); g = G - p@G
        if beta is not None:
            lp = th - logsumexp(th); g = g - (lp - lq - p@(lp - lq))/beta
        return p*g
    ts = np.r_[0.0, np.geomspace(1e-3, T, npts)]
    sol = solve_ivp(rhs, (0, T), lq.copy(), t_eval=ts, method='LSODA', rtol=1e-10, atol=1e-12)
    return sol.t, [softmax(sol.y[:, i]) for i in range(sol.y.shape[1])]

# ---------------- NPG with an explicit Fisher solve ----------------
def npg_path(q, G, eta=0.02, steps=3000, every=1):
    th = np.log(q).copy(); out = [softmax(th)]
    n = len(q)
    for k in range(steps):
        p = softmax(th); g = p*(G - p@G)                       # vanilla gradient of E_pG wrt logits
        fv = lambda v, p=p: p*v - p*(p@v)
        Fop = LinearOperator((n, n), matvec=fv, rmatvec=fv, dtype=float)
        v = lsqr(Fop, g, atol=1e-15, btol=1e-15, iter_lim=10000)[0]  # min-norm solution of Fisher v = g
        th = th + eta*v
        if (k+1) % every == 0: out.append(softmax(th))
    return out

# ---------------- readout at matched KL along a path ----------------
def at_kl(path, q, d):
    ks = np.array([KL(p, q) for p in path])
    idx = np.nonzero(ks >= d)[0]
    if len(idx) == 0 or idx[0] == 0: return None
    i = idx[0]; a = (d - ks[i-1])/(ks[i] - ks[i-1])
    return (1-a)*path[i-1] + a*path[i]

def crossing(dgrid, R1, R2):
    """smallest d where R1 - R2 changes sign from + to - (dense worse -> spike worse); linear interp in log d."""
    s = np.array(R1) - np.array(R2)
    for i in range(1, len(s)):
        if np.isfinite(s[i-1]) and np.isfinite(s[i]) and s[i-1] > 0 >= s[i]:
            x0, x1 = np.log(dgrid[i-1]), np.log(dgrid[i]); return float(np.exp(x0 + (x1-x0)*s[i-1]/(s[i-1]-s[i])))
    return None

def v5_pair():
    rng = np.random.default_rng(5); n = 2000; q = np.ones(n)/n; F = rng.normal(size=n)
    E1 = rng.normal(size=n)*0.6; E2 = np.zeros(n); E2[11] = 6.0
    return q, F, E1, E2

def tb_instance():          # R5 t2d.py T-B instance, reproduced exactly
    rng = np.random.default_rng(1); M = 1000; K = 5; w = np.r_[np.full(K, 12.0), np.ones(M-K)]; q = w/w.sum()
    F = rng.normal(size=M); Fh = F + 0.2*rng.normal(size=M)
    F[:K] = np.array([3, -3, 3, -3, 3.]); Fh[:K] = -F[:K]*1.0
    return q, F, Fh

def v25_instances(N=2000):  # V25 generator, same draws in the same order
    rng = np.random.default_rng(25)
    for _ in range(N):
        n = rng.integers(3, 40); q = rng.dirichlet(np.ones(n)*rng.uniform(0.1, 3))
        F = rng.normal(size=n); Fh = F + rng.normal(size=n)*rng.uniform(0.2, 3)
        yield q, F, Fh

cov = lambda q, a, b: q@(a*b) - (q@a)*(q@b)
