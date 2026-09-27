"""B1 brainstorm — toy tests (light protocol, rule 12; not pre-registered, no core claim rests on them).
T1 G0/H12: the measure splits into exact, attributable terms.   T2 G2: retention cost in closed form.
T3 G3/C1: a within-cell (length) exploit and what a coarse declaration hides.   T4 I1: Bradley-Terry offsets.
T5 L4: execution slips are charged more at higher intensity."""
import sys, numpy as np
from scipy.optimize import minimize
sys.path.insert(0, '.')
from verify import gibbs, lgibbs, KL, KLl, lam_to_kl, _mfree_mm, _that_full, _seg_free
rng = np.random.default_rng(1)
cells = lambda p, lab, m: np.bincount(lab, p, m)
def inst(m=4, size=3):
    lab = np.repeat(np.arange(m), size); q = rng.dirichlet(np.ones(m*size)); return lab, q, np.log(q)

# T1: M_seg_free = W + KL(pG || p_that) + KL(p_that || p_t*)  (Prop 36(b) with Prop 35(a))
e = 0.0
for _ in range(300):
    lab, q, lq = inst(); m = lab.max() + 1; FG = rng.normal(size=m); F = FG[lab]; r, s = 0.3, 1.5
    ph = rng.dirichlet(np.ones(len(q))); pG, qG = cells(ph, lab, m), cells(q, lab, m); lqG = np.log(qG)
    W = KL(ph, q) - KL(pG, qG); th = _that_full(pG, lqG, FG); ts = min(max(th, r), s)
    terms = W + KLl(np.log(pG), lgibbs(lqG, FG, th)) + KLl(lgibbs(lqG, FG, th), lgibbs(lqG, FG, ts))
    e = max(e, abs(_seg_free(ph, lq, F, r, s) - terms))
print(f"T1 three-term split (within-cell + off-ray + intensity), 300 instances: max error {e:.1e}")

# T2: retention. Agent can only move mass between cells of H (p/q H-measurable). F not H-measurable.
# Claim: min over such p of KL(p||p_(F,lam(k))) at budget k equals lam(k)*(m_F(k) - m_G(k)), G = E_q[F|H].
def mean_at(lq, G, k):
    l = lam_to_kl(lq, G, k); return gibbs(lq, G, l)@G
e2 = 0.0; mono = True; rows = []
for j in range(100):
    lab, q, lq = inst(); m = lab.max() + 1; F = rng.normal(size=len(q)); qG = cells(q, lab, m)
    G = (np.bincount(lab, q*F, m)/qG)[lab]
    prev = -1
    for k in (0.05, 0.2, 0.5):
        lam = lam_to_kl(lq, F, k)
        if not np.isfinite(lam) or not np.isfinite(lam_to_kl(lq, G, k)): continue
        closed = lam*(gibbs(lq, F, lam)@F - mean_at(lq, G, k))
        tgt = gibbs(lq, F, lam); P = lambda z: (lambda w: q*w/(q@w))(np.exp(z - z.max())[lab])
        cons = {'type': 'eq', 'fun': lambda z: KL(P(z), q) - k}
        num = min((r.fun for r in (minimize(lambda z: KL(P(z), tgt), rng.normal(size=m), method='SLSQP', constraints=[cons], options={'ftol': 1e-13, 'maxiter': 500}) for _ in range(5)) if r.success and abs(KL(P(r.x), q) - k) < 1e-8), default=np.nan)
        e2 = max(e2, abs(num - closed)) if np.isfinite(num) else e2; mono &= closed > prev; prev = closed
        if j == 0: rows.append((k, closed))
print(f"T2 retention cost: closed form vs constrained minimisation, max gap {e2:.1e} (SLSQP, 5 starts); increasing in k: {mono}; example {[(k, round(c, 4)) for k, c in rows]}")

# T3: length exploit. Target F on 'content' cells; evaluator adds E that varies only inside cells (length).
sh = []
for _ in range(300):
    lab, q, lq = inst(m=3, size=4); m = 3; F = rng.normal(size=m)[lab]; E = rng.uniform(0.5, 2)*rng.normal(size=len(q))
    E = E - (np.bincount(lab, q*E, m)/cells(q, lab, m))[lab]           # centred inside each cell: pure 'style'
    ph = gibbs(lq, F + E, 1.0); pG, qG = cells(ph, lab, m), cells(q, lab, m)
    Mf = _mfree_mm(ph, lq, F); MG = _mfree_mm(pG, np.log(qG), F[np.searchsorted(lab, np.arange(m))]); W = KL(ph, q) - KL(pG, qG)
    sh.append((W/Mf, MG/Mf))
sh = np.array(sh)
print(f"T3 Gibbs actor on F + style: share of M carried by W: median {np.median(sh[:,0]):.3f} (min {sh[:,0].min():.3f}); left visible under 'style free': median {np.median(sh[:,1]):.3f}")

# T4: Bradley-Terry identifies F up to a constant per context. Agent acts on F + a_c over the joint space.
res = []
for _ in range(200):
    lab, q, lq = inst(m=2, size=5); F = rng.normal(size=len(q)); a = rng.normal(size=2)*1.0
    ph = gibbs(lq, F + a[lab], 1.0); within = max(_mfree_mm(ph[lab == c]/ph[lab == c].sum(), np.log(q[lab == c]/q[lab == c].sum()), F[lab == c]) for c in (0, 1))
    res.append((_mfree_mm(ph, lq, F), within))
res = np.array(res)
print(f"T4 BT offsets: joint M_free median {np.median(res[:,0]):.3f}; within-context max {res[:,1].max():.1e}")

# T5: slips. p_hat = (1-eps) p_(F,t) + eps*uniform; charged M_free as intensity t grows.
lab, q, lq = inst(m=6, size=1); F = np.linspace(0, 1, 6); u = np.ones(6)/6
print("T5 slips eps=0.01, M_free by intensity t:", [(t, round(_mfree_mm(0.99*gibbs(lq, F, t) + 0.01*u, lq, F), 4)) for t in (1, 5, 10, 20, 40)])
