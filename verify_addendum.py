"""
verify_addendum.py — checks for the new claims in MESSAGE_to_previous_executor.md (review R3).
Run: python3 verify_addendum.py   (numpy, scipy; < 1 min)
 [W1] Theorem 1 generalizes: for J(p) = E_pF - phi(p)/beta with phi strictly convex,
      J(p*) - J(p) = B_phi(p,p*)/beta at an interior optimum, and >= at a boundary optimum (chi^2 example).
 [W2] The exchange rate is a shadow price: lambda_delta = 1 / V'(delta), V(delta) = sup_{KL<=delta} E_p G.
 [W3] The counterfactual matters: holding the price (beta) fixed vs holding the budget (delta) fixed
      gives different regrets, and can reverse which of two errors is worse.
 [W4] Stacked tilts compose additively in the exponent (sequential stages = one tilt by the weighted sum).
"""
import numpy as np
from scipy.special import logsumexp
from scipy.optimize import brentq
rng = np.random.default_rng(0)
def gibbs(lq, G, t): l = lq + t*G; return np.exp(l - logsumexp(l))
def KL(p, r): m = p > 0; return float(np.sum(p[m]*np.log(p[m]/r[m])))

# W1: chi^2-regularized actor
def chi2_actor(q, F, b):
    f = lambda nu: np.sum(q*np.maximum(0, (b/2)*(F - nu))) - 1
    nu = brentq(f, F.min() - 10/b - 10, F.max())
    return q*np.maximum(0, (b/2)*(F - nu))
print("[W1] chi^2 regularizer: J(p*)-J(p) vs B_phi(p,p*)/beta")
eq_int = []; ineq_bnd = []; viol = 0
for _ in range(4000):
    n = rng.integers(3, 25); q = rng.dirichlet(np.ones(n)); F = rng.normal(size=n); b = rng.uniform(0.05, 6)
    ps = chi2_actor(q, F, b); phi = lambda p: float(np.sum(p*p/q) - 1)
    J = lambda p: float(p@F) - phi(p)/b
    p = rng.dirichlet(np.ones(n))
    B = float(np.sum((p-ps)**2/q))
    gap = J(ps) - J(p) - B/b
    if np.all(ps > 1e-12): eq_int.append(abs(gap))
    else: ineq_bnd.append(gap)
    viol += gap < -1e-10
print(f"  interior optima: n={len(eq_int)}, max |gap| = {max(eq_int):.1e}   boundary optima: n={len(ineq_bnd)}, min gap = {min(ineq_bnd):.2e} (>= 0), violations = {viol}")

# W2: shadow price
print("[W2] lambda_delta = 1/V'(delta)")
err = 0
for _ in range(500):
    n = rng.integers(3, 30); q = rng.dirichlet(np.ones(n)); lq = np.log(q); G = rng.normal(size=n)
    lam = rng.uniform(0.1, 5); p = gibbs(lq, G, lam); d = KL(p, q)
    h = 1e-6
    V = lambda dd: gibbs(lq, G, brentq(lambda t: KL(gibbs(lq, G, t), q) - dd, 0, 200))@G
    dV = (V(d+h) - V(d-h))/(2*h)
    err = max(err, abs(1/dV - lam)/lam)
print(f"  max relative |1/V'(delta) - lambda| = {err:.1e}")

# W3: fixed price vs fixed budget
print("[W3] same-price vs same-budget counterfactual intended actor")
def regs(lq, q, F, E, b):
    ph = gibbs(lq, F+E, b); d = KL(ph, q); pp = gibbs(lq, F, b)
    lam = brentq(lambda t: KL(gibbs(lq, F, t), q) - d, 0, 1e5); pb = gibbs(lq, F, lam)
    return pp@F - ph@F, pb@F - ph@F
rng3 = np.random.default_rng(1); rev = tot = 0; diff = []
for _ in range(1500):
    n = rng3.integers(4, 30); q = rng3.dirichlet(np.ones(n)); lq = np.log(q); F = rng3.normal(size=n); b = rng3.uniform(0.5, 8)
    E1 = rng3.uniform(0.2, 2)*rng3.normal(size=n); E2 = rng3.uniform(0.2, 2)*rng3.normal(size=n)
    try: a1, c1 = regs(lq, q, F, E1, b); a2, c2 = regs(lq, q, F, E2, b)
    except ValueError: continue
    tot += 1; diff.append(abs(c1 - a1)); rev += (a1-a2)*(c1-c2) < 0 and min(abs(a1-a2), abs(c1-c2)) > 1e-3
print(f"  pairs of errors: {tot}; ranking by raw regret reverses between the two counterfactuals in {rev} ({rev/tot:.1%});"
      f" median |difference| for one error = {np.median(diff):.3f}")

# W4: stacked tilts
n = 50; q = rng.dirichlet(np.ones(n)); lq = np.log(q); G1, G2 = rng.normal(size=n), rng.normal(size=n)
p1 = gibbs(lq, G1, 1.3); p12 = gibbs(np.log(p1), G2, 0.7); pj = gibbs(lq, 1.3*G1 + 0.7*G2, 1.0)
print(f"[W4] max |tilt(tilt(q,G1),G2) - tilt(q, 1.3 G1 + 0.7 G2)| = {np.abs(p12 - pj).max():.1e}")

# W5: one curve. M(t) = KL(p_hat || p_{F,t}). Same-price regret: beta*R_J = M(beta). Same-budget raw regret
#     (intended actor with KL(p_{F,lam}||q) = KL(p_hat||q)) = M(lam)/lam. Transverse error D_perp = min_t M(t).
print("[W5] all regret notions are points on the convex curve M(t) = KL(p_hat || p_{F,t})")
rng5 = np.random.default_rng(5); e1 = e2 = e3 = 0
for _ in range(500):
    n = rng5.integers(4, 30); q = rng5.dirichlet(np.ones(n)); lq = np.log(q); F = rng5.normal(size=n)
    E = rng5.uniform(0.1, 1.5)*rng5.normal(size=n); b = rng5.uniform(0.3, 6)
    ph = gibbs(lq, F+E, b); lph = np.log(ph)
    def M(t):
        l = lq + t*F; l = l - logsumexp(l); return float(np.sum(ph*(lph - l)))
    ps = gibbs(lq, F, b); RJ = (ps@F - KL(ps, q)/b) - (ph@F - KL(ph, q)/b)
    e1 = max(e1, abs(b*RJ - M(b)))
    d = KL(ph, q)
    try: lam = brentq(lambda t: KL(gibbs(lq, F, t), q) - d, 0, 1e5)
    except ValueError: continue
    e2 = max(e2, abs((gibbs(lq, F, lam)@F - ph@F) - M(lam)/lam))
    ts = np.linspace(-10, 20, 301); Ms = np.array([M(t) for t in ts])
    e3 = max(e3, np.max(Ms[:-2] - 2*Ms[1:-1] + Ms[2:]) * -1)   # convexity: second differences >= 0
print(f"  max|beta R_J - M(beta)| = {e1:.1e};  max|same-budget raw regret - M(lam)/lam| = {e2:.1e};  max convexity violation = {max(e3,0):.1e}")
