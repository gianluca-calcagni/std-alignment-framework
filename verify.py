"""
verify.py — numerical verification of every theorem, proposition and measured number in the vault's core and
dictionary (one check note per block in `40 Checks/`) (package v6.4; V12-V17 added in R3, V18-V23 in the final audit and R4, V24-V26 in R5, V27-V29 in R6). Run: python3 verify.py   (numpy, scipy; a few minutes).
Each block prints the quantity the text quotes. Theorems are checked for violations AND the distribution of
slack is printed (rule: checks are reportable, not pass/fail).
Setting for all finite checks: X finite, q with full support.
"""
import numpy as np
from scipy.special import logsumexp
from scipy.optimize import brentq, minimize_scalar, minimize
from scipy.integrate import quad

# ---------- primitives ----------
def lgibbs(lq, G, t):
    l = lq + t*G; return l - logsumexp(l)
def gibbs(lq, G, t): return np.exp(lgibbs(lq, G, t))
def KLl(lp, lr):                         # KL from log-probabilities (no underflow)
    p = np.exp(lp); return float(np.sum(p*(lp - lr)))
def KL(p, r):
    m = p > 1e-300; return float(np.sum(p[m]*(np.log(p[m]) - np.log(r[m]))))
def J(p, G, q, b):                       # b = np.inf -> pure capacity actor, J = E_p G
    return float(p@G) - (0.0 if np.isinf(b) else KL(p, q)/b)
def lam_to_kl(lq, G, d):
    """lambda >= 0 with KL(p_{G,lambda}||q) = d; np.inf if d >= log 1/q(argmax G)."""
    q = np.exp(lq); top = G >= G.max()-1e-12
    if np.log(1/q[top].sum()) <= d: return np.inf
    f = lambda l: KL(gibbs(lq, G, l), q) - d
    hi = 1.0
    while f(hi) < 0: hi *= 2
    return brentq(f, 0, hi, xtol=1e-13)
def cap_actor(lq, G, b, d):
    """argmax of J_G over C_d = {KL(p||q) <= d}: Gibbs at temperature min(b, lambda_d(G)) (D5)."""
    lam = lam_to_kl(lq, G, d); t = min(b, lam)
    if np.isinf(t):
        q = np.exp(lq); top = G >= G.max()-1e-12; p = np.where(top, q, 0); return p/p.sum()
    return gibbs(lq, G, t)
def sigma_d(lq, E, d):                  # sup_{KL<=d} E_p E - E_q E  (attained by the tilt)
    q = np.exp(lq); return float(cap_actor(lq, E, np.inf, d)@E - q@E)
def width(lq, E, d): return sigma_d(lq, E, d) + sigma_d(lq, -E, d)
def cgf_c(lq, E, t):                    # centred CGF of E under q
    q = np.exp(lq); m = q@E; return float(logsumexp(lq + t*(E-m)))
def rand_inst(rng, n=None, esc=(0.01, 1.5), b=(0.2, 6)):
    n = n or rng.integers(3, 40); q = rng.dirichlet(np.ones(n)*rng.uniform(0.2, 3)); lq = np.log(q)
    F = rng.normal(size=n); E = rng.uniform(*esc)*rng.normal(size=n); return q, lq, F, E, rng.uniform(*b)
def pct(x, ps=(5, 50, 95)): return np.percentile(x, ps).round(3)

# ---------- V1: Theorem 1 and Corollaries 1.2-1.4 ----------
def V1():
    print("\n[V1] Thm 1: beta*R_J = KL(p_hat||p*);  Cor 1.2: E_ph E - E_p* E = Jeffreys/beta;  Cor 1.3 integral forms;  Cor 1.4 ratio")
    rng = np.random.default_rng(0); e1 = e2 = e3 = e4 = 0; ratio = []
    for i in range(20000):
        q, lq, F, E, b = rand_inst(rng)
        ps, ph = gibbs(lq, F, b), gibbs(lq, F+E, b)
        RJ = J(ps, F, q, b) - J(ph, F, q, b); gap = ph@E - ps@E
        e1 = max(e1, abs(b*RJ - KL(ph, ps))); e2 = max(e2, abs(b*gap - KL(ph, ps) - KL(ps, ph)))
        ratio.append(RJ/gap)
        if i < 300:   # integral forms by quadrature
            lps = np.log(ps)
            V = lambda t: (lambda pt: float(pt@E**2 - (pt@E)**2))(gibbs(lps, E, t))
            e3 = max(e3, abs(quad(lambda t: t*V(t), 0, b, epsabs=1e-12)[0] - b*RJ))
            e4 = max(e4, abs(quad(V, 0, b, epsabs=1e-12)[0] - gap))
    print(f"  max|beta R_J - KL(ph||p*)| = {e1:.1e}   max|beta*gap - Jeffreys| = {e2:.1e}")
    print(f"  max|int t Var dt - beta R_J| = {e3:.1e}   max|int Var dt - gap| = {e4:.1e}   (300 instances)")
    print(f"  Cor 1.4 ratio R_J/gap  p5/p50/p95 = {pct(ratio)}  min = {min(ratio):.3f}  max = {max(ratio):.3f}")

# ---------- V2: Prop 2 (Popoviciu) and Prop 3 (upper tail) ----------
def V2():
    print("\n[V2] Prop 2: R_J <= beta*osc^2/8;  Prop 3: R_J <= [L(2b)-2L(b)]/b <= 2*beta*s+^2 (upper-tail proxy under p*)")
    rng = np.random.default_rng(1); v = [0, 0, 0]; s2, s3a, s3b, cap = [], [], [], []
    for _ in range(20000):
        q, lq, F, E, b = rand_inst(rng)
        ps, ph = gibbs(lq, F, b), gibbs(lq, F+E, b); RJ = KL(ph, ps)/b; lps = np.log(ps)
        B2 = b*np.ptp(E)**2/8
        L = lambda t: cgf_c(lps, E, t); B3a = (L(2*b) - 2*L(b))/b
        ts = np.linspace(1e-4, 2*b, 200); sp = max(2*L(t)/t**2 for t in ts); B3b = 2*b*sp
        d = max(KL(ps, q), KL(ph, q)); C = np.ptp(E)*np.sqrt(2*d)
        v[0] += RJ > B2+1e-12; v[1] += RJ > B3a+1e-12; v[2] += RJ > B3b+1e-9
        s2.append(RJ/B2); s3a.append(RJ/B3a); s3b.append(RJ/B3b); cap.append(RJ/C)
    print(f"  violations: Prop2 {v[0]}, Prop3a {v[1]}, Prop3b {v[2]}  / 20000")
    print(f"  slack R/bound p5/p50/p95:  Prop2 {pct(s2)}  Prop3a {pct(s3a)}  Prop3b {pct(s3b)}  old normal form osc*sqrt(2d) {pct(cap)}")
    print(f"  frac Prop2 tighter than old normal form: {np.mean(np.array(s2) > np.array(cap)):.3f}")

# ---------- V3: Prop 4 (single region) ----------
def V3():
    print("\n[V3] Prop 4: E = M*1_A  =>  beta*R_J = kl(p_hat(A)||p*(A)); limits log 1/p*(A) (M->+inf), log 1/(1-p*(A)) (M->-inf)")
    rng = np.random.default_rng(2); n = 30; q = rng.dirichlet(np.ones(n)); lq = np.log(q); F = rng.normal(size=n); b = 2.0
    A = np.zeros(n, bool); A[[3, 7, 11]] = True; ps = gibbs(lq, F, b); a = ps[A].sum()
    kl2 = lambda x, y: x*np.log(x/y) + (1-x)*np.log((1-x)/(1-y))
    err = 0
    for M in [-40, -5, -1, 1, 5, 40]:
        ph = gibbs(lq, F + M*A, b); err = max(err, abs(KL(ph, ps) - kl2(ph[A].sum(), a)))
    print(f"  p*(A) = {a:.4f}; max|KL - binary kl| = {err:.1e}")
    print(f"  M=+40: beta R_J = {KL(gibbs(lq,F+40*A,b),ps):.4f}  vs log 1/p*(A) = {np.log(1/a):.4f}")
    print(f"  M=-40: beta R_J = {KL(gibbs(lq,F-40*A,b),ps):.4f}  vs log 1/(1-p*(A)) = {np.log(1/(1-a)):.4f}")

# ---------- V4: capacity actor ----------
def V4():
    print("\n[V4] Thm 5: R^C <= w_d(E), with equality in sup over intents (beta=inf);  Prop 6: DV formula and limits;  Prop 7 realized-reference bound")
    rng = np.random.default_rng(3); viol = 0; sl = []; att = []; dv = 0
    for _ in range(3000):
        n = rng.integers(3, 30); q = rng.dirichlet(np.ones(n)); lq = np.log(q)
        F = rng.normal(size=n); E = rng.uniform(0.05, 1.5)*rng.normal(size=n)
        b = rng.choice([rng.uniform(1, 20), np.inf]); d = 10**rng.uniform(-3, 0.5)
        ps, ph = cap_actor(lq, F, b, d), cap_actor(lq, F+E, b, d)
        R = J(ps, F, q, b) - J(ph, F, q, b); w = width(lq, E, d)
        viol += R > w + 1e-10; sl.append(R/w)
        # minimax attainment for beta = inf: F = -cE, c -> 1
        c = 0.999; pa, pb = cap_actor(lq, -c*E, np.inf, d), cap_actor(lq, (1-c)*E, np.inf, d)
        att.append((J(pa, -c*E, q, np.inf) - J(pb, -c*E, q, np.inf))/w)
        # DV: sigma_d = inf_l (d + L(l))/l
        r = minimize_scalar(lambda s: (d + cgf_c(lq, E, np.exp(s)))/np.exp(s), bounds=(-12, 12), method='bounded')
        dv = max(dv, abs(r.fun - sigma_d(lq, E, d)) if np.isfinite(lam_to_kl(lq, E, d)) else 0)
    print(f"  Thm5 violations {viol}/3000; R^C/w p5/p50/p95 = {pct(sl)};  attainment R(F=-0.999E)/w: min {min(att):.4f} max {max(att):.4f}")
    print(f"  Prop6 DV: max|inf_l (d+L(l))/l - sigma_d| = {dv:.1e}")
    q = np.ones(50)/50; lq = np.log(q); E = np.random.default_rng(9).normal(size=50)
    for d in [1e-4, 1e-3, 1e-2]:
        print(f"  small-d: d={d:g} sigma_d/sqrt(2 d Var) = {sigma_d(lq,E,d)/np.sqrt(2*d*E.var()):.4f}")
    print(f"  large-d: d=log 50 -> sigma_d = {sigma_d(lq,E,np.log(50)):.4f}  max E - E_q E = {E.max()-E.mean():.4f}")
    # Prop 7
    rng = np.random.default_rng(4); v7 = 0; s7 = []; tight = []
    def sp(lq, E, sgn):
        return max(2*cgf_c(lq, sgn*E, l)/l**2 for l in np.exp(np.linspace(-7, 5, 400)))
    for _ in range(3000):
        q, lq, F, E, b = rand_inst(rng)
        ps, ph = gibbs(lq, F, b), gibbs(lq, F+E, b); R = KL(ph, ps)/b
        B = np.sqrt(2*sp(lq, E, 1)*KL(ph, q)) + np.sqrt(2*sp(lq, E, -1)*KL(ps, q))
        C = np.ptp(E)*np.sqrt(2*max(KL(ps, q), KL(ph, q)))
        v7 += R > B+1e-9; s7.append(R/B); tight.append(B <= C+1e-12)
    print(f"  Prop7 violations {v7}/3000; slack p5/p50/p95 = {pct(s7)}; never looser than osc*sqrt(2d): {np.mean(tight):.3f}")
    # retraction record: the three readings of osc_delta
    rng = np.random.default_rng(1); rec = []
    for _ in range(4000):
        n = rng.integers(3, 30); q = rng.dirichlet(np.ones(n)); lq = np.log(q)
        F = rng.normal(size=n); E = rng.uniform(0.05, 1.5)*rng.normal(size=n); b = rng.uniform(1, 20); d = 10**rng.uniform(-3, 0.5)
        R = J(cap_actor(lq, F, b, d), F, q, b) - J(cap_actor(lq, F+E, b, d), F, q, b); k = np.sqrt(2*d)
        S = q >= np.exp(-d); ob = np.ptp(E[S]) if S.any() else 0.0
        rec.append((d, R > width(lq, E, d)*k + 1e-10, R > ob*k + 1e-10, R > np.ptp(E)*k + 1e-10))
    R = np.array(rec)
    for lo, hi in [(1e-3, 1e-2), (1e-2, 1e-1), (1e-1, 1), (1, 4)]:
        m = (R[:, 0] >= lo) & (R[:, 0] < hi)
        print(f"  [retraction record] d in [{lo:g},{hi:g}): violation rate of osc_d*sqrt(2d) with reading (a) {R[m,1].mean():.2f}  (b) {R[m,2].mean():.2f}  (c) {R[m,3].mean():.2f}")

# ---------- V5: non-separability ----------
def V5():
    print("\n[V5] Lemma 8 / Thm 9: width ratio limits; R^C rank reversal")
    rng = np.random.default_rng(5); n = 200; q = rng.dirichlet(np.ones(n)*2); lq = np.log(q)
    E1 = rng.normal(size=n); i = int(np.argmin(q)); A = np.zeros(n); A[i] = 1.0; r = q[i]
    v1 = float(q@E1**2 - (q@E1)**2)
    lim0 = np.sqrt(v1/(r*(1-r))); limI = np.ptp(E1)
    for d in [1e-6, 1e-5]:
        print(f"  d={d:g}: w(E1)/w(1_A) = {width(lq,E1,d)/width(lq,A,d):.4f}   predicted limit {lim0:.4f}")
    big = 1.01*max(np.log(1/r), np.log(1/(1-r)), np.log(1/q[np.argmax(E1)]), np.log(1/q[np.argmin(E1)]))
    print(f"  d={big:.2f}: w(E1)/w(1_A) = {width(lq,E1,big)/width(lq,A,big):.4f}   predicted osc(E1) = {limI:.4f}")
    print(f"  K >= {lim0/limI:.1f}  => any separable (E,d)-bound on worst-case regret is >= {np.sqrt(lim0/limI):.1f}x loose")
    # R^C example (regularised capacity actor, fixed intent)
    rng = np.random.default_rng(5); n = 2000; q = np.ones(n)/n; lq = np.log(q); F = rng.normal(size=n)
    E1 = rng.normal(size=n)*0.6; E2 = np.zeros(n); E2[11] = 6.0; b = 30.0; rat = []
    for d in [0.002, 0.01, 0.05, 0.2, 0.5, 1, 2, 3, 5, 7]:
        ps = cap_actor(lq, F, b, d); R = [J(ps, F, q, b) - J(cap_actor(lq, F+E, b, d), F, q, b) for E in (E1, E2)]
        rat.append(R[0]/R[1])
    print(f"  fixed-intent example: R(E1)/R(E2) over d in [0.002,7]: {rat[0]:.2f} -> {rat[-1]:.2f}; span x{max(rat)/min(rat):.0f}")

# ---------- V6: divergence-norm conjugacy ----------
def V6():
    print("\n[V6] Prop 10: four pairings;  Prop 11: KL exposure infinite under sub-exponential tails, chi^2 finite")
    rng = np.random.default_rng(6); v = np.zeros(4, int)
    for _ in range(20000):
        n = rng.integers(3, 30); q = rng.dirichlet(np.ones(n)); p = rng.dirichlet(np.ones(n)*rng.uniform(0.3, 5))
        E = rng.standard_t(3, size=n); diff = p@E - q@E; mq = q@E
        tv = 0.5*np.abs(p-q).sum(); chi2 = float(((p-q)**2/q).sum()); Dinf = np.log((p/q).max())
        kl = KL(p, q)
        r = minimize_scalar(lambda s: (kl + cgf_c(np.log(q), E, np.exp(s)))/np.exp(s), bounds=(-12, 12), method='bounded')
        v[0] += abs(diff) > np.ptp(E)*tv + 1e-12
        v[1] += diff > r.fun + 1e-9
        v[2] += abs(diff) > np.sqrt(chi2*float(q@(E-mq)**2)) + 1e-12
        v[3] += p@np.abs(E) > np.exp(Dinf)*(q@np.abs(E)) + 1e-12
    print(f"  violations (TV-osc, KL-CGF, chi2-Var, Dinf-L1): {v.tolist()} / 20000")
    a, dl = 3.0, 0.1                      # Pareto(a) on [1,inf): Var finite for a > 2
    EqE = a/(a-1); var = a/(a-2) - EqE**2
    print(f"  Pareto a={a}: Var_q E = {var:.3f}; chi2-exposure bound sqrt(d Var) at d={dl}: {np.sqrt(dl*var):.3f}")
    for m in [1e2, 1e4, 1e8, 1e16]:
        r = m**(-a); eps = min(1.0, dl/np.log(1/r))
        k = (1-eps)*(1-r)*np.log(1-eps) + ((1-eps)*r + eps)*np.log((1-eps) + eps/r)   # exact KL of the mixture
        gain = (1-eps)*EqE + eps*a*m/(a-1) - EqE
        print(f"    m={m:.0e}: KL(p||q) = {k:.4f} (<= {dl})   E_p E - E_q E = {gain:.3e}")

# ---------- V7: identification and the intent ray ----------
def V7():
    print("\n[V7] Thm 13: beta R_J = D_perp + D_par (Pythagorean);  rescaling;  affine invariance of D_perp;  second order")
    rng = np.random.default_rng(7); e = 0; neg = 0; inv = 0
    def that(lq, F, ph):
        m = ph@F; g = lambda t: gibbs(lq, F, t)@F - m
        lo, hi = -1.0, 1.0
        while g(lo) > 0: lo *= 2
        while g(hi) < 0: hi *= 2
        return brentq(g, lo, hi, xtol=1e-13)
    for _ in range(5000):
        q, lq, F, E, b = rand_inst(rng)
        ls, lh = lgibbs(lq, F, b), lgibbs(lq, F+E, b); ph = np.exp(lh); t = that(lq, F, ph); lt = lgibbs(lq, F, t)
        e = max(e, abs(KLl(lh, ls) - KLl(lh, lt) - KLl(lt, ls))); neg += t < 0
        a0, c0 = rng.choice([-1, 1])*rng.uniform(0.2, 3), rng.normal()   # D_perp invariant under F -> aF + c (a != 0)
        F2 = a0*F + c0; t2 = that(lq, F2, ph); inv = max(inv, abs(KLl(lh, lgibbs(lq, F2, t2)) - KLl(lh, lt)))
    print(f"  max|KL(ph||p*) - D_perp - D_par| = {e:.1e};  instances with t_hat < 0: {neg}/5000;  max change of D_perp under F->aF+c: {inv:.1e}")
    q, lq, F, E, b = rand_inst(np.random.default_rng(8)); s = 1.7
    ph = gibbs(lq, s*F, b); t = that(lq, F, ph)
    print(f"  rescaling F_hat = {s}F: t_hat/beta = {t/b:.6f}, D_perp = {KL(ph, gibbs(lq,F,t)):.1e}, beta R_J = D_par = {KL(ph, gibbs(lq,F,b)):.4f}")
    print("  second order: E = eps*E0 (fixed E0), a = Cov_p*(E,F)/Var_p*(F), E_perp = E - aF")
    E0 = rng.normal(size=len(F))
    for eps in [0.3, 0.1, 0.03, 0.01, 0.003]:
        E = eps*E0; ps = gibbs(lq, F, b); ph = gibbs(lq, F+E, b); t = that(lq, F, ph); pt = gibbs(lq, F, t)
        cv = lambda x, y: float(ps@(x*y) - (ps@x)*(ps@y)); a = cv(E, F)/cv(F, F); Ep = E - a*F
        print(f"    eps={eps}: D_perp/[(b^2/2)Var(E_perp)] = {KL(ph,pt)/(b*b/2*cv(Ep,Ep)):.4f}   D_par/[(b^2/2)a^2 Var F] = {KL(pt,ps)/(b*b/2*a*a*cv(F,F)):.4f}")

# ---------- V8: capability trade ----------
def V8():
    print("\n[V8] Prop 14: T'(0) = -Cov_q(F_hat,F); T(inf) = max F - E_{q|argmax F_hat} F;  measured frequencies")
    rng = np.random.default_rng(10); e0 = eI = 0
    for _ in range(2000):
        q, lq, F, E, b = rand_inst(rng); Fh = F + E; T = lambda t: F.max() - gibbs(lq, Fh, t)@F
        h = 1e-5; e0 = max(e0, abs((T(h)-T(0))/h + (q@(Fh*F) - (q@Fh)*(q@F))))
        M = Fh >= Fh.max()-1e-12; lim = F.max() - (q[M]@F[M])/q[M].sum(); eI = max(eI, abs(T(1e4) - lim))
    print(f"  max|finite-diff T'(0) + Cov_q(F_hat,F)| = {e0:.1e};   max|T(1e4) - limit| = {eI:.1e}")
    betas = 2.0**np.arange(-2, 12, 0.25)
    for sc in [0.2, 1, 4, 8]:
        c = dict(dn=0, up=0, it=0, nm=0, neg=0, s=0, sdn=0); N = 300; opt = []
        for _ in range(N):
            n = rng.integers(5, 40); q = rng.dirichlet(np.ones(n)); lq = np.log(q)
            F = rng.normal(size=n); E = sc*rng.normal(size=n)
            tot = np.array([F.max() - gibbs(lq, F+E, b)@F for b in betas])
            ar = np.array([gibbs(lq, F, b)@F - gibbs(lq, F+E, b)@F for b in betas]); dt = np.diff(tot)
            dn = np.all(dt <= 1e-9); up = np.all(dt >= -1e-9) and not dn
            c['dn'] += dn; c['up'] += up; c['it'] += (not dn) and (not up) and 0 < np.argmin(tot) < len(tot)-1
            c['nm'] += not (np.all(np.diff(ar) >= -1e-9) or np.all(np.diff(ar) <= 1e-9)); c['neg'] += ar.min() < -1e-9
            s = np.argmax(F+E) == np.argmax(F); c['s'] += s; c['sdn'] += s and dn; opt.append(betas[np.argmin(tot)])
        print(f"  scale {sc}: mono-good {c['dn']/N:.2f} mono-bad {c['up']/N:.2f} interior {c['it']/N:.2f} | raw align. regret non-monotone {c['nm']/N:.2f}, "
              f"negative somewhere {c['neg']/N:.2f} | P(mono-good|argmax agrees) {c['sdn']/max(c['s'],1):.2f} | median argmin beta {np.median(opt):g}")

# ---------- V9: dictionary derivations ----------
def V9():
    print("\n[V9] Dictionary: Holmstrom (exact independence cost; second-order optimal weight);  Gaussian Gibbs linearity (Gao slope);  Conant-Fano")
    rng = np.random.default_rng(11); nc, nl = 30, 12; c = rng.normal(size=nc); L = np.linspace(-1, 1, nl)
    F = np.repeat(c, nl); N = np.tile(L, nc); q = np.ones(nc*nl)/(nc*nl); lq = np.log(q)
    E = 0.8*N + 0.3*rng.normal(size=nc*nl)
    for b in [4.0, 1.0, 0.25, 0.05]:
        ps = gibbs(lq, F, b); RJ = lambda X: KL(gibbs(lq, F+X, b), ps)/b
        cs = -((ps@(E*N))-(ps@E)*(ps@N))/((ps@(N*N))-(ps@N)**2); ws = np.linspace(-2, 1, 3001)
        wb = ws[np.argmin([RJ(E+w*N) for w in ws])]
        print(f"  beta={b}: R_J(E)={RJ(E):.4f} R_J(E-0.8N)={RJ(E-0.8*N):.4f} | c* (2nd order) = {cs:.3f}  numerical argmin = {wb:.3f}")
    b = 4.0; ps = gibbs(lq, F, b); E0 = np.repeat(0.5*rng.normal(size=nc), nl); qN = np.ones(nl)/nl
    add = KL(gibbs(lq, F+E0+N, b), ps)/b - KL(gibbs(lq, F+E0, b), ps)/b
    print(f"  independence (product space): added regret {add:.8f} = KL(tilt_N||q_N)/beta {KL(gibbs(np.log(qN),L,b),qN)/b:.8f}")
    # Gaussian: behaviours = grid in R^2 with q ~ N(0,I) discretised; F = u.x, F_hat = w.x
    g = np.linspace(-9, 9, 361); X, Y = np.meshgrid(g, g); X, Y = X.ravel(), Y.ravel()
    lq = -(X**2+Y**2)/2; lq -= logsumexp(lq); q = np.exp(lq)
    u = np.array([1.0, 0.0]); w = np.array([0.6, 0.8]); Fg = u[0]*X+u[1]*Y; Fh = w[0]*X+w[1]*Y
    rho = (u@w)/np.linalg.norm(u)/np.linalg.norm(w)
    for bb in [0.2, 1, 2, 3]:
        p = gibbs(lq, Fh, bb); d = np.sqrt(KL(p, q)); gain = p@Fg - q@Fg
        print(f"    Gaussian Gibbs path: d={d:.3f}  gold gain/d = {gain/d:.4f}   sqrt(2)*rho*sd(F) = {np.sqrt(2)*rho:.4f}")
    # Conant + Fano: Z = (D + R) mod k injective in D for fixed R  =>  H(Z) >= H(D) - I(D;R)
    rng = np.random.default_rng(12); viol = 0; slack = []
    H = lambda p: -float(np.sum(p[p > 0]*np.log(p[p > 0])))
    for _ in range(5000):
        k = rng.integers(2, 12); pD = rng.dirichlet(np.ones(k)); PR = rng.dirichlet(np.ones(k)*rng.uniform(0.05, 3), size=k)
        joint = pD[:, None]*PR; pR = joint.sum(0); I = H(pD) + H(pR) - H(joint.ravel())
        pZ = np.zeros(k)
        for dd in range(k):
            for rr in range(k): pZ[(dd+rr) % k] += joint[dd, rr]
        viol += H(pZ) < H(pD) - I - 1e-12; slack.append(H(pZ) - (H(pD) - I))
    print(f"  Conant: violations of H(Z) >= H(D) - I(D;R): {viol}/5000; slack p5/p50/p95 = {pct(slack)}")

# ---------- V10: dynamic form ----------
def V10():
    print("\n[V10] Delayed correction e' = c(t) - u(t - tau): P at the margin vs PI; bandwidth")
    def sim(tau, c, kp, ki, T, dt=0.002, cf=None):
        n = int(T/dt); lag = int(tau/dt); e = np.zeros(n); I = np.zeros(n)
        for t in range(1, n):
            j = t-1-lag; ed = e[j] if j >= 0 else 0.0; Id = I[j] if j >= 0 else 0.0
            e[t] = e[t-1] + dt*((c if cf is None else cf(t*dt)) - kp*ed - ki*Id); I[t] = I[t-1] + dt*e[t-1]
        return e[-n//4:]
    for tau in [0.5, 1, 2, 4]:
        a = sim(tau, 1, np.pi/(2*tau), 0, 200*tau); p = sim(tau, 1, 0.4/tau, 0.08/tau**2, 600*tau)
        print(f"  tau={tau}: P at k=pi/(2tau): mean {a.mean():.3f} (2tau/pi = {2*tau/np.pi:.3f}), peak-to-peak {np.ptp(a):.3f} | PI: mean {p.mean():+.1e}, max|e| {np.abs(p).max():.1e}")
    for w in [0.03, 0.3, 1, 3]:
        e = sim(1.0, 0, 0.4, 0.08, max(600, 60/w), cf=lambda t: np.sin(w*t))
        print(f"  sinusoidal creation, tau=1, w={w}: closed-loop amplitude {np.ptp(e)/2:.3f}  open-loop {1/w:.3f}")

# ---------- V11: H2 equipartition (retraction evidence) ----------
def V11():
    print("\n[V11] H2 repair attempt: <R_J>*2beta'/(n-1) under Boltzmann refinement of E at rate beta' (predicted ~1)")
    rng = np.random.default_rng(4); n = 6; q = rng.dirichlet(np.ones(n)*2); lq = np.log(q); F = rng.normal(size=n)
    for b in [0.5, 2, 8]:
        ps = gibbs(lq, F, b); out = []
        for bp in [20, 200, 2000]:
            E = np.zeros(n); cur = 0.0; acc = []; st = 1/np.sqrt(bp*b*0.05)
            for t in range(40000):
                Ep = E + st*rng.normal(size=n); Ep -= Ep.mean(); new = KL(gibbs(lq, F+Ep, b), ps)/b
                if np.log(rng.uniform()) < -bp*(new-cur) - (Ep@Ep - E@E)/200: E, cur = Ep, new
                if t > 8000 and t % 10 == 0: acc.append(cur)
            out.append(np.mean(acc)*2*bp/(n-1))
        print(f"  actor beta={b}: " + "  ".join(f"beta'={bp}: {o:.2f}" for bp, o in zip([20, 200, 2000], out)) + f"   (exp H(p*) = {np.exp(-np.sum(ps*np.log(ps))):.2f})")


# =====================================================================================================
# v6.1 blocks (review R3): Props 15-19, Cors 1.5 & 5.2, Thm 13(b), Thm 17, B §11
# =====================================================================================================

# ---------- V12: Prop 15 (general regularizer, concave target) ----------
def V12():
    print("\n[V12] Prop 15: J(p*) - J(p) = B_Psi(p,p*) (interior) and >= (boundary)")
    rng = np.random.default_rng(12)
    def chi2_actor(q, F, b):
        f = lambda nu: np.sum(q*np.maximum(0, (b/2)*(F - nu))) - 1
        nu = brentq(f, F.min() - 10/b - 10, F.max()); return q*np.maximum(0, (b/2)*(F - nu))
    eq, bd, viol = [], [], 0
    for _ in range(4000):
        n = rng.integers(3, 25); q = rng.dirichlet(np.ones(n)); F = rng.normal(size=n); b = rng.uniform(0.05, 6)
        ps = chi2_actor(q, F, b); J = lambda p: float(p@F) - (float(np.sum(p*p/q)) - 1)/b
        p = rng.dirichlet(np.ones(n)); gap = J(ps) - J(p) - float(np.sum((p-ps)**2/q))/b
        (eq if np.all(ps > 1e-12) else bd).append(gap); viol += gap < -1e-10
    print(f"  (a) chi^2 regularizer, linear target: interior n={len(eq)} max|gap|={max(map(abs,eq)):.1e}; boundary n={len(bd)} min gap={min(bd):.1e}; violations {viol}")
    e = 0
    for _ in range(3000):
        n = rng.integers(3, 30); q = rng.dirichlet(np.ones(n)); lq = np.log(q)
        F, G = rng.normal(size=n), rng.normal(size=n); b = rng.uniform(0.2, 5); kap = rng.uniform(0.1, 3)
        pm = lambda m: gibbs(lq, F - 2*kap*m*G, b)
        m = brentq(lambda m: pm(m)@G - m, G.min() - 1, G.max() + 1); ps = pm(m)
        J = lambda p: float(p@F) - kap*float(p@G)**2 - KL(p, q)/b
        p = rng.dirichlet(np.ones(n))
        e = max(e, abs(J(ps) - J(p) - (KL(p, ps)/b + kap*(float(p@G) - m)**2)))
    print(f"  (b) KL regularizer, concave target U = E_pF - k(E_pG)^2: max|J(p*)-J(p) - [KL(p||p*)/b + k(E_pG-E_p*G)^2]| = {e:.1e}")

# ---------- V13: Cor 5.2 (shadow price) ----------
def V13():
    print("\n[V13] Cor 5.2: lambda_delta = 1/V'(delta)")
    rng = np.random.default_rng(13); err = 0
    for _ in range(500):
        n = rng.integers(3, 30); q = rng.dirichlet(np.ones(n)); lq = np.log(q); G = rng.normal(size=n)
        lam = rng.uniform(0.1, 5); d = KL(gibbs(lq, G, lam), q); h = 1e-6
        V = lambda dd: gibbs(lq, G, brentq(lambda t: KL(gibbs(lq, G, t), q) - dd, 0, 200))@G
        err = max(err, abs(1/((V(d+h) - V(d-h))/(2*h)) - lam)/lam)
    print(f"  max relative |1/V'(delta) - lambda_delta| = {err:.1e}")

# ---------- V14: Thm 13(b) half-ray, Thm 17 one curve, Prop 16 invariance, conventions ----------
def V14():
    print("\n[V14] Thm 13(b): half-ray decomposition;  Thm 17: one curve;  Prop 16: invariance;  price vs budget conventions")
    rng = np.random.default_rng(14); e_dec = e_curve = e_budget = e_inv = e_price_inv = 0; nneg = 0
    def that(lq, F, ph):
        m = ph@F; g = lambda t: gibbs(lq, F, t)@F - m; lo, hi = -1.0, 1.0
        while g(lo) > 0: lo *= 2
        while g(hi) < 0: hi *= 2
        return brentq(g, lo, hi, xtol=1e-13)
    def Mfun(lq, F, lph):
        ph = np.exp(lph); return lambda t: float(np.sum(ph*(lph - lgibbs(lq, F, t))))
    def budget_point(lq, F, d):
        q = np.exp(lq); return brentq(lambda t: KL(gibbs(lq, F, t), q) - d, 0, 1e5)
    for i in range(3000):
        q, lq, F, E, b = rand_inst(rng)
        if i % 3 == 0: E = -F*rng.uniform(1.2, 3) + 0.2*E            # force some anti-aligned actors
        lph = lgibbs(lq, F+E, b); ph = np.exp(lph); M = Mfun(lq, F, lph)
        t = that(lq, F, ph); tp = max(t, 0.0); nneg += t < 0
        Dperp = M(tp); Dpar = KLl(lgibbs(lq, F, tp), lgibbs(lq, F, b)); X = b*max(q@F - ph@F, 0.0)
        e_dec = max(e_dec, abs(M(b) - Dperp - Dpar - X))
        ts = np.linspace(0, 3*b + 5, 400); e_curve = max(e_curve, max(0.0, Dperp - min(M(s) for s in ts)))
        d = KL(ph, q)
        try: lam = budget_point(lq, F, d)
        except ValueError: continue
        e_budget = max(e_budget, abs((gibbs(lq, F, lam)@F - ph@F) - M(lam)/lam))
        a0, c0 = rng.uniform(0.2, 4), rng.normal(); F2 = a0*F + c0; M2 = Mfun(lq, F2, lph)
        t2 = max(that(lq, F2, ph), 0.0); lam2 = budget_point(lq, F2, d)
        e_inv = max(e_inv, abs(M2(t2) - Dperp), abs(M2(lam2) - M(lam)))
        e_price_inv = max(e_price_inv, abs(M2(b) - M(b)))
    print(f"  max|beta R_J - (D_perp + D_par + X_anti)| = {e_dec:.1e}  (t_hat < 0 in {nneg}/3000)")
    print(f"  D_perp is the minimum of M on [0,inf): max excess over grid minimum = {e_curve:.1e}")
    print(f"  same-budget raw regret = M(lambda)/lambda: max error {e_budget:.1e}")
    print(f"  invariance under F -> aF + c (a > 0): max change of D_perp and of M(lambda) = {e_inv:.1e};  max change of M(beta) = {e_price_inv:.2f} (not invariant)")
    rng3 = np.random.default_rng(1); rev = tot = 0
    def regs(lq, q, F, E, b):
        ph = gibbs(lq, F+E, b); d = KL(ph, q); pp = gibbs(lq, F, b); pb = gibbs(lq, F, budget_point(lq, F, d))
        return pp@F - ph@F, pb@F - ph@F
    for _ in range(1500):
        n = rng3.integers(4, 30); q = rng3.dirichlet(np.ones(n)); lq = np.log(q); F = rng3.normal(size=n); b = rng3.uniform(0.5, 8)
        E1 = rng3.uniform(0.2, 2)*rng3.normal(size=n); E2 = rng3.uniform(0.2, 2)*rng3.normal(size=n)
        try: a1, c1 = regs(lq, q, F, E1, b); a2, c2 = regs(lq, q, F, E2, b)
        except ValueError: continue
        tot += 1; rev += (a1-a2)*(c1-c2) < 0 and min(abs(a1-a2), abs(c1-c2)) > 1e-3
    print(f"  price vs budget convention: ranking of error pairs by raw regret reverses in {rev}/{tot} = {rev/tot:.1%}")

# ---------- V15: Cor 1.5 (stacked stages) ----------
def V15():
    print("\n[V15] Cor 1.5: stacked entropic stages = one stage with beta = sum beta_k, error = beta-weighted mean")
    rng = np.random.default_rng(15); n = 60; q = rng.dirichlet(np.ones(n)); lq = np.log(q)
    F = rng.normal(size=n); E1, E2 = rng.normal(size=n), rng.normal(size=n); b1, b2 = 1.3, 0.7; B = b1 + b2
    ph_seq = gibbs(np.log(gibbs(lq, F+E1, b1)), F+E2, b2); ph_one = gibbs(lq, F + (b1*E1 + b2*E2)/B, B)
    print(f"  max|sequential - single| = {np.abs(ph_seq - ph_one).max():.1e}")
    ps = gibbs(lq, F, B)
    for eps in [0.1, 0.03, 0.01]:
        S = eps*(b1*E1 + b2*E2); ph = gibbs(lq, F + S/B, B)
        v = float(ps@S**2 - (ps@S)**2)
        print(f"    eps={eps}: B*R_J / [Var_p*(sum b_k E_k)/2] = {KL(ph, ps)/(v/2):.4f}")

# ---------- V16: Prop 18 (detection), Prop 19 (contexts) ----------
def V16():
    print("\n[V16] Prop 18: Chernoff information C <= min(KL(ph||p*), KL(p*||ph)) <= beta R_J;  Prop 19: evaluation gap")
    rng = np.random.default_rng(16); viol = 0; r1 = []; r2 = []
    for _ in range(5000):
        q, lq, F, E, b = rand_inst(rng); ph, ps = gibbs(lq, F+E, b), gibbs(lq, F, b)
        c = -minimize_scalar(lambda l: logsumexp(l*np.log(ph) + (1-l)*np.log(ps)), bounds=(0, 1), method='bounded').fun
        k1, k2 = KL(ph, ps), KL(ps, ph); viol += c > min(k1, k2) + 1e-10
        r1.append(c/k1); r2.append(min(k1, k2)/k1)
    print(f"  violations {viol}/5000;  C/(beta R_J) p5/p50/p95 = {pct(r1)};  min(KL,KL_rev)/(beta R_J) p50 = {np.median(r2):.3f}")
    nC, n = 5, 20; q = rng.dirichlet(np.ones(n), size=nC); F = rng.normal(size=(nC, n)); E = np.zeros((nC, n)); E[4] = 3*rng.normal(size=n); b = 2.0
    rev = np.array([0.24, 0.24, 0.24, 0.24, 0.04]); rdep = np.array([0.1, 0.1, 0.1, 0.1, 0.6])
    kl_c = np.array([KL(gibbs(np.log(q[c]), F[c]+E[c], b), gibbs(np.log(q[c]), F[c], b)) for c in range(nC)])
    Pj = np.concatenate([rev[c]*gibbs(np.log(q[c]), F[c]+E[c], b) for c in range(nC)])
    Qj = np.concatenate([rev[c]*gibbs(np.log(q[c]), F[c], b) for c in range(nC)])
    print(f"  per-context KL = {np.round(kl_c,4).tolist()};  KL of eval joints = {KL(Pj, Qj):.4f} = E_ev KL_c = {rev@kl_c:.4f}")
    print(f"  deployment harm E_dep KL_c = {rdep@kl_c:.4f};  evaluation gap Gamma = {rdep@kl_c - rev@kl_c:.4f}")

# ---------- V17: B §11 (Price identity) ----------
def V17():
    print("\n[V17] B §11: E_p F - E_q F = Cov_q(dp/dq, F) for any p (Price selection term); first order gives Prop 14(ii)")
    rng = np.random.default_rng(17); e = 0
    for _ in range(5000):
        n = rng.integers(3, 30); q = rng.dirichlet(np.ones(n)); p = rng.dirichlet(np.ones(n)); F = rng.normal(size=n); w = p/q
        e = max(e, abs((p@F - q@F) - (q@(w*F) - (q@w)*(q@F))))
    print(f"  max|E_pF - E_qF - Cov_q(w,F)| = {e:.1e}")


# ---------- V18: Cor 17.1 (capacity actor regret = budget convention) ----------
def V18():
    print("\n[V18] Cor 17.1: with both capacity constraints binding, R^C = M(lambda)/lambda")
    rng = np.random.default_rng(18); e = 0; cnt = 0
    for _ in range(3000):
        n = rng.integers(3, 30); q = rng.dirichlet(np.ones(n)); lq = np.log(q); F = rng.normal(size=n); E = rng.normal(size=n)*rng.uniform(0.1, 1.5)
        b = float(rng.choice([np.inf, rng.uniform(5, 50)])); Fh = F + E
        d = rng.uniform(0.05, 0.95)*min(np.log(1/q[F >= F.max()-1e-12].sum()), np.log(1/q[Fh >= Fh.max()-1e-12].sum()))
        lF, lH = lam_to_kl(lq, F, d), lam_to_kl(lq, Fh, d)
        if not (b > lF and b > lH): continue
        ps, ph = gibbs(lq, F, lF), gibbs(lq, Fh, lH)
        RC = J(ps, F, np.exp(lq), b) - J(ph, F, np.exp(lq), b); M = KLl(lgibbs(lq, Fh, lH), lgibbs(lq, F, lF))
        e = max(e, abs(RC - M/lF)); cnt += 1
    print(f"  {cnt} binding instances: max |R^C - M(lambda)/lambda| = {e:.1e}")

# ---------- V19: Def 8 saturation ----------
def V19():
    print("\n[V19] Def 8 saturation: budget beyond log 1/q(argmax F)")
    q = np.array([0.4, 0.4, 0.2]); lq = np.log(q); F = np.array([1.0, 1.0, 0.0]); E = np.array([4.0, -4.0, 0.0]); b = 3.0
    ph = gibbs(lq, F+E, b); d = KL(ph, q); cap = np.log(1/q[F == F.max()].sum())
    pinf = np.where(F == F.max(), q, 0); pinf /= pinf.sum()
    with np.errstate(divide='ignore'): Minf = float(np.sum(ph*(np.log(ph) - np.log(pinf))))
    print(f"  KL(p_hat||q) = {d:.3f} >= {cap:.3f}; KL(p_hat || q(.|argmax F)) = {Minf}; raw regret max F - E_ph F = {F.max()-ph@F:.3e}")


# =====================================================================================================
# v6.2 blocks (review R4): Prop 20 (tier-1 identities), B7(e) (rational-inattention regret), B §12 (defaults)
# =====================================================================================================

# ---------- V20: Prop 20 (actor-agnostic identities) ----------
def V20():
    print("\n[V20] Prop 20: for ANY actor p << q (best-of-n, top-k, arbitrary):  E_pF - E_qF = Cov_q(w,F_hat) - Cov_q(w,E);"
          "  E_p1 F - E_p2 F = Cov_q(w1 - w2, F)")
    rng = np.random.default_rng(20); e1 = e2 = 0
    def cov(q, a, b): return float(q@(a*b) - (q@a)*(q@b))
    for _ in range(3000):
        n = rng.integers(3, 40); q = rng.dirichlet(np.ones(n)); F = rng.normal(size=n); E = rng.normal(size=n)*rng.uniform(0.1, 2); Fh = F + E
        # best-of-k on the proxy (exact distribution of the argmax of k i.i.d. draws from q; ties broken by index)
        k = rng.integers(1, 30); order = np.argsort(-Fh, kind='stable'); cdf_above = np.concatenate([[0], np.cumsum(q[order])])
        pb = np.zeros(n); pb[order] = (1 - cdf_above[:-1])**k - (1 - cdf_above[1:])**k
        # top-m selection: q restricted to the m proxy-best behaviours
        m = rng.integers(1, n+1); pt = np.zeros(n); pt[order[:m]] = q[order[:m]]; pt /= pt.sum()
        pa = rng.dirichlet(np.ones(n))                                   # arbitrary
        for p in (pb, pt, pa):
            w = p/q; e1 = max(e1, abs((p@F - q@F) - (cov(q, w, Fh) - cov(q, w, E))))
        w1, w2 = pb/q, pa/q; e2 = max(e2, abs((pb@F - pa@F) - cov(q, w1 - w2, F)))
    print(f"  max error (Goodhart as covariance) = {e1:.1e};  max error (regret between two actors) = {e2:.1e}")

# ---------- V21: B7(e) rational-inattention regret identity (endogenous reference) ----------
def V21():
    print("\n[V21] B7(e): reference optimized (capacity = mutual information); for pi_w << pi*_w:"
          " J(pi*) - J(pi) = lam*[E_w KL(pi_w||pi*_w) - KL(pibar||pibar*)]")
    rng = np.random.default_rng(21); e = 0; gaps = []; opt = 0
    def J(P, F, rho, lam):
        qa = rho@P; return float(np.sum(rho[:, None]*P*F)) - lam*float(np.sum(rho[:, None]*P*(np.log(P) - np.log(qa)[None, :])))
    for _ in range(2000):
        nW, nA = rng.integers(2, 6), rng.integers(2, 7); rho = rng.dirichlet(np.ones(nW)); lam = rng.uniform(0.2, 4)
        # construct an exact full-support RI optimum: choose pi*, set q* = rho pi*, F = lam log(pi*/q*) + c_w
        Ps = rng.dirichlet(np.ones(nA)*2, size=nW); qs = rho@Ps
        F = lam*np.log(Ps/qs[None, :]) + rng.normal(size=(nW, 1))
        P = rng.dirichlet(np.ones(nA)*rng.uniform(0.3, 3), size=nW)          # any other policy (full support)
        lhs = J(Ps, F, rho, lam) - J(P, F, rho, lam)
        ekl = float(np.sum(rho[:, None]*P*np.log(P/Ps))); qa = rho@P; mkl = float(np.sum(qa*np.log(qa/qs)))
        e = max(e, abs(lhs - lam*(ekl - mkl))); gaps.append(mkl/ekl); opt += lhs >= -1e-12
    print(f"  max |identity error| = {e:.1e};  pi* beats every other policy in {opt}/2000 (it is the global optimum)")
    print(f"  marginal correction KL(pibar||pibar*) / E_w KL(pi_w||pi*_w): median {np.median(gaps):.3f}, max {max(gaps):.3f}  (<= 1 by data processing)")

# ---------- V22: B §12 default manipulation identifies the reference under exclusion ----------
def V22():
    print("\n[V22] B §12: two defaults identify the reference's default weight iff the default does not move the evaluator")
    rng = np.random.default_rng(22); n = 6; u = np.ones(n)/n; b = 2.0
    def qd(alpha, d): v = (1 - alpha)*u.copy(); v[d] += alpha; return v
    def estimate_alpha(p0, p1, d0, d1):
        # log(p0/p1) - log(q0/q1) is constant across x under exclusion; solve for alpha by matching the two default options
        f = lambda a: (np.log(p0[d0]/p1[d0]) - np.log(qd(a, d0)[d0]/qd(a, d1)[d0])) - (np.log(p0[2]/p1[2]) - np.log(qd(a, d0)[2]/qd(a, d1)[2]))
        return brentq(f, 1e-9, 1 - 1e-9)
    for gamma in [0.0, 0.3, 1.0]:
        errs = []
        for _ in range(200):
            Fh = rng.normal(size=n); alpha = rng.uniform(0.05, 0.9); d0, d1 = 0, 1
            e0 = np.zeros(n); e0[d0] = gamma; e1 = np.zeros(n); e1[d1] = gamma          # endorsement: the default moves F_hat
            p0 = gibbs(np.log(qd(alpha, d0)), Fh + e0, b); p1 = gibbs(np.log(qd(alpha, d1)), Fh + e1, b)
            try: errs.append(abs(estimate_alpha(p0, p1, d0, d1) - alpha))
            except ValueError: errs.append(np.nan)
        print(f"  endorsement effect gamma = {gamma}: median |alpha_hat - alpha| = {np.nanmedian(errs):.2e}  (failed fits: {int(np.isnan(errs).sum())}/200)")


# ---------- V23: B §13 potential games under log-linear learning (Blume 1993) ----------
def V23():
    print("\n[V23] B §13: log-linear learning in a potential game has stationary law prod_i q_i(x_i) * exp(beta*Phi(x))")
    import itertools
    rng = np.random.default_rng(23); err = 0
    for _ in range(200):
        n = rng.integers(2, 4); A = [int(rng.integers(2, 4)) for _ in range(n)]; b = rng.uniform(0.2, 3)
        prof = list(itertools.product(*[range(a) for a in A])); idx = {x: k for k, x in enumerate(prof)}
        Phi = {x: rng.normal() for x in prof}
        # utilities: u_i = Phi + h_i(x_{-i}) (any exact potential game has this form)
        h = [{tuple(x[j] for j in range(n) if j != i): rng.normal() for x in prof} for i in range(n)]
        u = lambda i, x: Phi[x] + h[i][tuple(x[j] for j in range(n) if j != i)]
        qs = [rng.dirichlet(np.ones(a)) for a in A]
        T = np.zeros((len(prof), len(prof)))
        for x in prof:
            for i in range(n):
                alts = [x[:i] + (a,) + x[i+1:] for a in range(A[i])]
                w = np.array([np.log(qs[i][a]) + b*u(i, y) for a, y in enumerate(alts)]); w = np.exp(w - logsumexp(w))
                for a, y in enumerate(alts): T[idx[x], idx[y]] += w[a]/n
        vals, vecs = np.linalg.eig(T.T); pi = np.real(vecs[:, np.argmin(np.abs(vals - 1))]); pi /= pi.sum()
        g = np.array([np.sum([np.log(qs[i][x[i]]) for i in range(n)]) + b*Phi[x] for x in prof]); g = np.exp(g - logsumexp(g))
        err = max(err, np.abs(pi - g).max())
    print(f"  max |stationary law - tilt of the joint reference by the potential| = {err:.1e}  (200 random games, 2-3 players)")
    # linear public goods, n = 3, binary contributions: Phi = (m/n - c) sum x, W = (m - c) sum x
    n, m, c, b = 3, 2.0, 1.0, 1.5
    prof = list(itertools.product([0, 1], repeat=n)); S = np.array([sum(x) for x in prof], float)
    Phi, W = (m/n - c)*S, (m - c)*S; lq = np.full(len(prof), -np.log(len(prof)))
    ph = gibbs(lq, Phi, b); t = brentq(lambda t: gibbs(lq, W, t)@W - ph@W, -50, 50)
    Dperp_half = KL(ph, np.exp(lq)); Xanti = b*max(np.exp(lq)@W - ph@W, 0)
    Dpar = KL(np.exp(lq), gibbs(lq, W, b)); total = KL(ph, gibbs(lq, W, b))
    print(f"  public goods (m/n < c < m): t_hat/beta = {t/b:.4f} (= (m/n-c)/(m-c) = {(m/n-c)/(m-c):.4f}); half-ray D_perp = KL(ph||q) = {Dperp_half:.4f}, "
          f"X_anti = {Xanti:.4f}, D_par = {Dpar:.4f}; sum = {Dperp_half+Xanti+Dpar:.4f} = beta R_J = {total:.4f}")


# =====================================================================================================
# v6.3 blocks (review R5): Prop 21 (affine regression => no overoptimization for F_hat-measurable actors),
# Prop 22 (first-order effect of any smooth optimizer), Remark 13.5 (rescaling under the three conventions; BoN)
# =====================================================================================================

def _bon(q, G, n):
    """exact best-of-n law on finite X; ties broken by index (stable order)"""
    o = np.argsort(G, kind='stable'); U = np.cumsum(q[o]); Um = U - q[o]; p = np.empty_like(q); p[o] = U**n - Um**n; return p

# ---------- V24: Prop 21 ----------
def V24():
    print("\n[V24] Prop 21: if E_q[F|F_hat] = a + b F_hat and w = dp/dq depends on x only through F_hat, gold gain = b * proxy gain")
    rng = np.random.default_rng(24); e = 0; ratio_nonmeas = []
    for _ in range(500):
        k, m = rng.integers(3, 30), rng.integers(2, 6)
        f = rng.normal(size=k); b = rng.normal(); eps = rng.normal(size=m); eps = np.concatenate([eps, -eps])  # symmetric residual
        qf = rng.dirichlet(np.ones(k)); qe = np.ones(2*m)/(2*m)
        Fh = np.repeat(f, 2*m); F = b*Fh + np.tile(eps, k); q = np.repeat(qf, 2*m)*np.tile(qe, k); lq = np.log(q)
        actors = [gibbs(lq, Fh, rng.uniform(0.1, 4))]                                   # Gibbs: w = e^{beta F_hat}/Z
        thr = np.quantile(f, rng.uniform(0.2, 0.9)); pt = q*(Fh >= thr); actors.append(pt/pt.sum())   # top selection
        h = rng.uniform(0, 1, size=k); w = np.repeat(h, 2*m); pa = q*w; actors.append(pa/pa.sum())   # arbitrary F_hat-measurable
        for p in actors:
            e = max(e, abs((p@F - q@F) - b*(p@Fh - q@Fh)))
        # a non-measurable actor (weights depend on the residual): the identity fails
        pn = q*np.exp(0.8*np.tile(eps, k)); pn /= pn.sum(); ratio_nonmeas.append(abs((pn@F - q@F) - b*(pn@Fh - q@Fh)))
    print(f"  F_hat-measurable actors (Gibbs, top selection, arbitrary): max |gold gain - b*proxy gain| = {e:.1e}")
    print(f"  an actor whose weights use the residual: median violation {np.median(ratio_nonmeas):.3f} (the condition is needed)")

# ---------- V25: Prop 22 (first-order effect of any smooth optimizer) ----------
def V25():
    print("\n[V25] Prop 22: d/dt E_{p_t}F at t=0 = sum_x v_x F_x = Cov_q(v/q, F); vanilla softmax gradient gives eta*sum_x q_x^2 (F - E_qF)(F_hat - E_qF_hat)")
    rng = np.random.default_rng(25); e_g = e_v = 0; flips = 0; tot = 0
    for _ in range(2000):
        n = rng.integers(3, 40); q = rng.dirichlet(np.ones(n)*rng.uniform(0.1, 3)); lq = np.log(q)
        F = rng.normal(size=n); Fh = F + rng.normal(size=n)*rng.uniform(0.2, 3); h = 1e-7
        # Gibbs path
        d_g = (gibbs(lq, Fh, h)@F - q@F)/h; e_g = max(e_g, abs(d_g - (q@(Fh*F) - (q@Fh)*(q@F))))
        # vanilla policy gradient on logits theta = log q, exact gradient of E_p F_hat, step eta = h
        th = lq + h*q*(Fh - q@Fh); pv = np.exp(th - logsumexp(th)); d_v = (pv@F - q@F)/h
        pred = float(np.sum(q**2*(F - q@F)*(Fh - q@Fh))); e_v = max(e_v, abs(d_v - pred)/max(1e-12, abs(pred)))
        tot += 1; flips += np.sign(d_g) != np.sign(pred)
    print(f"  Gibbs: max |finite-difference - Cov_q(F_hat,F)| = {e_g:.1e};  VPG: max relative error vs q^2-weighted formula = {e_v:.1e}")
    print(f"  random instances where the two optimizers' initial effects have opposite signs: {flips}/{tot}")

# ---------- V26: Remark 13.5 (rescaling under conventions) and best-of-n facts ----------
def V26():
    print("\n[V26] Remark 13.5: F_hat = sF under the three conventions; best-of-n is invariant to monotone transforms and puts weight <= n q(x) on any state")
    rng = np.random.default_rng(26); n = 40; q = rng.dirichlet(np.ones(n)); lq = np.log(q); F = rng.normal(size=n); b = 2.0
    for s in [0.5, 1.7, 3.0]:
        ph = gibbs(lq, s*F, b); d = KL(ph, q)
        lam = brentq(lambda t: KL(gibbs(lq, F, t), q) - d, 0, 1e4)
        Mprice = KL(ph, gibbs(lq, F, b)); Mbudget = KL(ph, gibbs(lq, F, lam))
        print(f"  s={s}: price convention M(beta) = {Mprice:.4f};  budget convention M(lambda) = {Mbudget:.1e} (lambda/beta = {lam/b:.4f}; the budget point is p_hat itself, so free D_perp = 0 too)")
    e_inv = 0; e_bd = 0
    for _ in range(500):
        n = rng.integers(3, 60); q = rng.dirichlet(np.ones(n)*rng.uniform(0.2, 3)); G = rng.normal(size=n); k = int(rng.integers(1, 200))
        e_inv = max(e_inv, np.abs(_bon(q, G, k) - _bon(q, np.exp(G) + 3*G**3 + 7, k)).max())
        e_bd = max(e_bd, np.max(_bon(q, G, k) - k*q))
    print(f"  best-of-n: max change under a strictly increasing transform = {e_inv:.1e};  max (p_BoN(x) - n q(x)) = {e_bd:.1e} (<= 0)")


# =====================================================================================================
# v6.4 blocks (review R6): tier-1 status in the actual actor (Thm 1, Thm 13, Thm 17, Prop 18);
# Prop 23 (coupled selectors at equal budget, tier 2'); Prop 15 without concavity of U
# =====================================================================================================

def _vpg(q, G, eta, steps):
    th = np.log(q).copy()
    for _ in range(steps):
        p = np.exp(th - logsumexp(th)); th += eta*p*(G - p@G)
    return np.exp(th - logsumexp(th))

# ---------- V27: identities in an arbitrary actual actor ----------
def V27():
    print("\n[V27] Thm 1, Thm 13(b), Thm 17(iii) and Prop 18's cap hold for an ARBITRARY full-support actual actor (best-of-n, early-stopped VPG, random); only the intended actor is Gibbs")
    rng = np.random.default_rng(27); e1 = e13 = e17 = 0; viol18 = 0; cnt = 0
    for _ in range(1500):
        n = rng.integers(3, 30); q = rng.dirichlet(np.ones(n)); lq = np.log(q); F = rng.normal(size=n); Fh = F + rng.normal(size=n)*rng.uniform(0.2, 2)
        b = rng.uniform(0.3, 5); ls = lgibbs(lq, F, b); ps = np.exp(ls)
        actors = [_bon(q, Fh, int(rng.integers(2, 50))), _vpg(q, Fh, 0.5, int(rng.integers(1, 200))), rng.dirichlet(np.ones(n))]
        for ph in actors:
            ph = np.maximum(ph, 1e-300); ph /= ph.sum(); lh = np.log(ph)
            RJ = (ps@F - KL(ps, q)/b) - (ph@F - KL(ph, q)/b)
            e1 = max(e1, abs(b*RJ - KLl(lh, ls)))
            m = ph@F; g = lambda t: gibbs(lq, F, t)@F - m; lo, hi = -1.0, 1.0
            while g(lo) > 0: lo *= 2
            while g(hi) < 0: hi *= 2
            t = brentq(g, lo, hi, xtol=1e-13); tp = max(t, 0.0); ltp = lgibbs(lq, F, tp)
            e13 = max(e13, abs(KLl(lh, ls) - KLl(lh, ltp) - KLl(ltp, ls) - b*max(q@F - m, 0.0)))
            d = KL(ph, q)
            try: lam = brentq(lambda s: KL(gibbs(lq, F, s), q) - d, 0, 1e5)
            except ValueError: continue
            ll = lgibbs(lq, F, lam); e17 = max(e17, abs((np.exp(ll)@F - m) - KLl(lh, ll)/lam))
            C = -minimize_scalar(lambda l: logsumexp(l*lh + (1-l)*ls), bounds=(0, 1), method='bounded').fun
            viol18 += C > KLl(lh, ls) + 1e-10; cnt += 1
    print(f"  {cnt} actor instances: max |beta R_J - KL(ph||p*)| = {e1:.1e};  max Thm 13(b) error = {e13:.1e};  max Thm 17(iii) error = {e17:.1e};  Prop 18 cap violations = {viol18}")

# ---------- V28: Prop 23 (coupled selectors at equal budget) ----------
def V28():
    print("\n[V28] Prop 23: argmax selectors on a COMMON random candidate set (best-of-n at equal n): 0 <= R <= E_ph E - E_p* E")
    rng = np.random.default_rng(28); v1 = v2 = 0; N = 0
    for _ in range(20000):
        m = rng.integers(2, 40); q = rng.dirichlet(np.ones(m)*rng.uniform(0.1, 3)); F = rng.normal(size=m); E = rng.normal(size=m)*rng.uniform(0.05, 2)
        if rng.random() < 0.3: F = np.round(F); E = np.round(E*2)/2
        prio = rng.permutation(m).astype(float); k = int(rng.integers(1, 200))
        def bon_t(G):
            o = np.lexsort((prio, G)); U = np.cumsum(q[o]); Um = U - q[o]; p = np.empty_like(q); p[o] = U**k - Um**k; return p
        ps, ph = bon_t(F), bon_t(F + E); R = ps@F - ph@F; gap = ph@E - ps@E
        v1 += R < -1e-12; v2 += R > gap + 1e-12; N += 1
    print(f"  {N} instances (30 % with ties; common tie-breaking): R < 0 in {v1};  R > E_ph E - E_p* E in {v2}")

# ---------- V29: Prop 15 without concavity of U ----------
def V29():
    print("\n[V29] Prop 15 with a NON-concave target U(p) = E_pF + k(E_pG)^2 (k > 0), where Psi = KL/beta - U is still convex")
    rng = np.random.default_rng(29); e = 0; used = 0
    for _ in range(3000):
        n = rng.integers(3, 20); q = rng.dirichlet(np.ones(n)*2); lq = np.log(q); F, G = rng.normal(size=n), rng.normal(size=n)
        b = rng.uniform(0.2, 2); kap = rng.uniform(0.01, 0.1)/(b*np.max(G**2)/q.min())   # small enough for convexity of Psi
        pm = lambda m: gibbs(lq, F + 2*kap*m*G, b)
        m = brentq(lambda m: pm(m)@G - m, G.min() - 1, G.max() + 1); ps = pm(m)
        Jf = lambda p: float(p@F) + kap*float(p@G)**2 - KL(p, q)/b
        p = rng.dirichlet(np.ones(n))
        e = max(e, abs(Jf(ps) - Jf(p) - (KL(p, ps)/b - kap*(float(p@G) - m)**2))); used += 1
    print(f"  {used} instances: max |J(p*) - J(p) - B_Psi(p,p*)| = {e:.1e}  (B_Psi = KL(p||p*)/beta - k (E_pG - E_p*G)^2)")


# =====================================================================================================
# R7-0 block: the misalignment contract (Def. 11) evaluated on the v6.4 measures (Prop. 24)
# =====================================================================================================
def _measures(lq, F, ph, beta):
    q = np.exp(lq); lh = np.log(ph)
    Mp = KLl(lh, lgibbs(lq, F, beta))
    d = KL(ph, q); sat = np.log(1/q[np.argmax(F)])
    Mb = None
    if d < sat - 1e-9:
        lam = 0.0 if d < 1e-15 else brentq(lambda t: KL(gibbs(lq, F, t), q) - d, 0, 1e6, xtol=1e-14)
        Mb = KLl(lh, lgibbs(lq, F, lam))
    ts = np.concatenate([[0.0], np.logspace(-4, 4, 400)])
    t0 = ts[np.argmin([KLl(lh, lgibbs(lq, F, t)) for t in ts])]
    r = minimize_scalar(lambda t: KLl(lh, lgibbs(lq, F, t)), bounds=(0, max(2*t0, 1e-3)), method='bounded', options={'xatol': 1e-12})
    Mf = min(r.fun, KLl(lh, lgibbs(lq, F, 0.0)), KLl(lh, lgibbs(lq, F, t0)))
    dF = gibbs(lq, F, beta)@F - ph@F
    return Mp, Mb, Mf, dF

def V30():
    print("\n[V30] Def. 11 contract on the v6.4 measures (Prop. 24): M1 identity, M2 >= 0, M3 representation invariance, M5 intensity is not misdirection, M8 per context; sanity suite M9")
    rng = np.random.default_rng(30); tol = 1e-8
    viol = {k: 0 for k in ['M1 budget', 'M1 free', 'M1 price', 'M2 any KL measure', 'M3 budget', 'M3 free', 'M3 price(beta/a)', 'M5 budget', 'M5 free']}
    m5_price = []; neg_dF = 0; N = 0
    for _ in range(600):
        n = rng.integers(3, 25); q = rng.dirichlet(np.ones(n)); lq = np.log(q); F = rng.normal(size=n); beta = rng.uniform(0.3, 3)
        # M1: the intended behaviour itself gives zero
        Mp, _, _, _ = _measures(lq, F, gibbs(lq, F, beta), beta); viol['M1 price'] += Mp > tol
        # M5: an agent pursuing F itself at another intensity
        t = beta*rng.choice([0.25, 0.5, 2.0, 4.0]); ph = gibbs(lq, F, t)
        Mp, Mb, Mf, dF = _measures(lq, F, ph, beta)
        if Mb is not None: viol['M5 budget'] += Mb > 1e-7; viol['M1 budget'] += Mb > 1e-7
        viol['M5 free'] += Mf > 1e-7; viol['M1 free'] += Mf > 1e-7; m5_price.append(Mp); neg_dF += dF < -1e-12
        # M2 and M3 on a random actual behaviour
        ph = rng.dirichlet(np.ones(n)); Mp, Mb, Mf, dF = _measures(lq, F, ph, beta); N += 1
        viol['M2 any KL measure'] += min(Mp, Mf, Mb if Mb is not None else 0) < -1e-12
        viol['M1 free'] += Mf < 1e-10; viol['M1 price'] += Mp < 1e-10          # 'only if': a random behaviour is off the ray
        if Mb is not None: viol['M1 budget'] += Mb < 1e-10
        a, c = rng.uniform(0.2, 5), rng.normal()
        Mp2, Mb2, Mf2, _ = _measures(lq, a*F + c, ph, beta/a)
        viol['M3 price(beta/a)'] += abs(Mp - Mp2) > 1e-7; viol['M3 free'] += abs(Mf - Mf2) > 1e-6
        if Mb is not None and Mb2 is not None: viol['M3 budget'] += abs(Mb - Mb2) > 1e-6
    print("  violations over 600 instances each: " + "; ".join(f"{k}: {v}" for k, v in viol.items()))
    print(f"  M5 for the price measure (an agent pursuing F itself at 1/4, 1/2, 2 or 4 times the price): positive in {sum(x > 1e-7 for x in m5_price)}/{len(m5_price)}, median {np.median(m5_price):.3f} nats -> the price measure FAILS M5")
    print(f"  raw value regret dF negative for an over-optimizing, right-target agent in {neg_dF}/600 -> dF fails M2")
    # M9 sanity suite on one instance
    n = 12; q = rng.dirichlet(np.ones(n)*2); lq = np.log(q); F = np.linspace(-1, 1, n) + 0.3*rng.normal(size=n); beta = 1.5
    cases = [('aligned (the intended actor)', gibbs(lq, F, beta)), ('weaker, right target (t = beta/2)', gibbs(lq, F, beta/2)),
             ('stronger, right target (t = 3 beta)', gibbs(lq, F, 3*beta)), ('inactive: stays at the default q', q.copy()),
             ('sign-flipped (F_hat = -F)', gibbs(lq, -F, beta)), ('random behaviour', rng.dirichlet(np.ones(n))),
             ('a different target, same budget', gibbs(lq, rng.normal(size=n), beta))]
    print("  sanity suite M9 (budget | free | price, in nats):")
    for name, ph in cases:
        Mp, Mb, Mf, dF = _measures(lq, F, ph, beta)
        z = lambda v: 0.0 if abs(v) < 5e-9 else v
        print(f"    {name:36s} {('%.4f' % z(Mb)) if Mb is not None else 'saturated':>9s} | {z(Mf):.4f} | {z(Mp):.4f}")
    # M8: aligned under evaluation, misaligned in deployment
    ev, dep = gibbs(lq, F, beta), gibbs(lq, -0.5*F + rng.normal(size=n), beta)
    _, be, fe, _ = _measures(lq, F, ev, beta); _, bd, fd, _ = _measures(lq, F, dep, beta)
    print(f"    context case: evaluation budget/free = {abs(be):.0e}/{abs(fe):.0e}; deployment = {bd:.3f}/{fd:.3f} -> per-context measures separate the two")


# =====================================================================================================
# R7-1 block: mechanism-relative comparison (Def. 14) against the contract (Prop. 25)
# =====================================================================================================
def _bonp(q, G, k, prio):
    o = np.lexsort((prio, G)); U = np.cumsum(q[o]); Um = U - q[o]; p = np.empty_like(q); p[o] = U**k - Um**k; return p

def V31():
    print("\n[V31] Prop. 25: M_own = KL(ph || A(F; r)) and R_own = E_{A(F;r)}F - E_ph F against the contract")
    rng = np.random.default_rng(31)
    # (c) M4 fails: one behaviour, two attributions under the entropic model (Prop. 12)
    n = 15; q = rng.dirichlet(np.ones(n)); lq = np.log(q); F = rng.normal(size=n); Fh = F + 0.7*rng.normal(size=n); b = 1.5; sc = 2.0
    ph = gibbs(lq, Fh, b)                                          # = gibbs(lq, sc*Fh, b/sc)
    m1, m2 = KL(ph, gibbs(lq, F, b)), KL(ph, gibbs(lq, F, b/sc))
    print(f"  (c) same behaviour attributed as (F_hat, beta) or ({sc} F_hat, beta/{sc}): M_own = {m1:.3f} vs {m2:.3f} nats; behaviours identical to {np.abs(ph - gibbs(lq, sc*Fh, b/sc)).max():.0e}")
    # (d) M1 fails for R_own: an evaluator that only reorders equal-target behaviours
    n = 12; q = rng.dirichlet(np.ones(n)); F = np.repeat([0.0, 1.0, 2.0], 4); prio = np.arange(n, dtype=float); k = 6
    Fh = F + 0.01*rng.normal(size=n)                               # breaks ties differently; never crosses levels
    pint, pact = _bonp(q, F, k, prio), _bonp(q, Fh, k, prio)
    print(f"  (d) reorder-only evaluator, best-of-{k}: R_own = {pint@F - pact@F:.1e}, while KL(ph || A(F)) = {KL(pact, pint):.3f} nats  -> R_own fails M1")
    # (d) M2 fails for R_own: VPG with the same steps on F_hat = 2F
    neg = 0
    for _ in range(200):
        n = rng.integers(3, 30); q = rng.dirichlet(np.ones(n)); F = rng.normal(size=n); eta = rng.uniform(0.05, 0.5); steps = int(rng.integers(1, 60))
        neg += _vpg(q, F, eta, steps)@F - _vpg(q, 2*F, eta, steps)@F < -1e-12
    print(f"  (d) vanilla policy gradient, same steps, F_hat = 2F: R_own < 0 in {neg}/200  -> R_own fails M2")
    # (a) M5' and (b) M3 for best-of-n; (e) the detection cap
    e5 = e3 = 0; viol = 0
    for _ in range(1000):
        n = rng.integers(3, 30); q = rng.dirichlet(np.ones(n)); F = rng.normal(size=n); Fh = F + rng.normal(size=n)*rng.uniform(0.1, 2)
        prio = rng.permutation(n).astype(float); k = int(rng.integers(2, 40))
        pint = _bonp(q, F, k, prio); e5 = max(e5, KL(_bonp(q, F, k, prio), pint))
        a, c = rng.uniform(0.1, 10), rng.normal(); pact = _bonp(q, Fh, k, prio)
        e3 = max(e3, abs(KL(pact, pint) - KL(pact, _bonp(q, a*F + c, k, prio))))
        lh, li = np.log(pact), np.log(pint)
        C = -minimize_scalar(lambda l: logsumexp(l*lh + (1-l)*li), bounds=(0, 1), method='bounded').fun
        viol += C > KL(pact, pint) + 1e-10
    print(f"  (a) M_own for best-of-n run on the target at the actor's n: max {e5:.0e};  (b) change under positive affine maps: max {e3:.0e};  (e) detection-cap violations: {viol}/1000")


# =====================================================================================================
# R7-2 block: Prop 26 (reference misspecification), the rejected alternative, and Prop 25's reference attribution
# =====================================================================================================
def _mfree(lh, lq, F):
    ts = np.concatenate([[0.0], np.logspace(-4, 4, 300)]); v = [KLl(lh, lgibbs(lq, F, t)) for t in ts]; t0 = ts[int(np.argmin(v))]
    r = minimize_scalar(lambda t: KLl(lh, lgibbs(lq, F, t)), bounds=(0, max(2*t0, 1e-3)), method='bounded', options={'xatol': 1e-13})
    return min(r.fun, min(v))
def _mbud(lh, lref, F):
    d = KLl(lh, lref); sat = -lref[np.argmax(F)]
    if d >= sat - 1e-9: return None
    lam = 0.0 if d < 1e-15 else brentq(lambda t: KLl(lgibbs(lref, F, t), lref) - d, 0, 1e6, xtol=1e-14)
    return KLl(lh, lgibbs(lref, F, lam))

def V32():
    print("\n[V32] Prop. 26: an actor entropic from its own reference q_A = q e^h; the measures use the declared q")
    rng = np.random.default_rng(32); z = lambda v: 0.0 if abs(v) < 5e-9 else v
    ea = 0
    for _ in range(2000):
        n = rng.integers(3, 30); lq = np.log(rng.dirichlet(np.ones(n))); h = rng.normal(size=n)*rng.uniform(0.1, 2)
        lqa = lq + h; lqa -= logsumexp(lqa); Fh = rng.normal(size=n); b = rng.uniform(0.2, 5)
        ea = max(ea, np.abs(lgibbs(lqa, Fh, b) - lgibbs(lq, Fh + h/b, b)).max())
    print(f"  (a) absorption p^(q_A)_(F_hat,beta) = p_(F_hat + h/beta, beta): max log-probability error {ea:.0e} over 2000 instances")
    res = {'random h': [], 'h = aF + c, a > -beta': [], 'h = aF + c, a < -beta': []}
    for _ in range(600):
        n = rng.integers(3, 25); lq = np.log(rng.dirichlet(np.ones(n))); F = rng.normal(size=n); b = rng.uniform(0.3, 3)
        cases = {'random h': rng.normal(size=n), 'h = aF + c, a > -beta': rng.uniform(-b + 0.05, 3)*F + rng.normal(),
                 'h = aF + c, a < -beta': rng.uniform(-b - 3, -b - 0.05)*F + rng.normal()}
        for k, h in cases.items():
            lh = lgibbs(lq, F + h/b, b); res[k].append((_mfree(lh, lq, F), _mbud(lh, lq, F)))
    for k, v in res.items():
        mf = np.array([x[0] for x in v]); mb = np.array([x[1] for x in v if x[1] is not None])
        print(f"  (c) F_hat = F, {k:22s}: M_free in [{mf.min():.1e}, {mf.max():.2g}]; M_budget in [{mb.min():.1e}, {mb.max():.3g}] (defined in {len(mb)}/600)")
    n = 20; lq = np.log(rng.dirichlet(np.ones(n)*2)); F = rng.normal(size=n); b = 1.3; h0 = rng.normal(size=n)
    ps = np.exp(lgibbs(lq, F, b)); a0 = (ps@(h0*F) - (ps@h0)*(ps@F))/(ps@F**2 - (ps@F)**2); hp = h0 - a0*F; var = ps@hp**2 - (ps@hp)**2
    print("  (d) M_free / ((eps^2/2) Var_p*(h0_perp)):", '  '.join(f"eps={e}: {_mfree(lgibbs(lq, F + e*h0/b, b), lq, F)/(e**2/2*var):.4f}" for e in (0.3, 0.1, 0.03, 0.01)))
    n = 25; lq = np.log(rng.dirichlet(np.ones(n))); F = rng.normal(size=n); h = rng.normal(size=n); bs = [0.25, 0.5, 1, 2, 4, 8, 16, 32, 64]
    lqa = lq + h; lqa -= logsumexp(lqa); lim0 = _mfree(lqa, lq, F)
    print("  (e) one instance, M_free vs beta:", '  '.join(f"{b}: {z(_mfree(lgibbs(lq, F + h/b, b), lq, F)):.3f}" for b in bs), f"| beta -> 0 limit inf_t KL(q_A||p_F,t) = {lim0:.3f}")
    peak = 0; vanish = 0; N = 200
    for _ in range(N):
        n = rng.integers(4, 25); lq = np.log(rng.dirichlet(np.ones(n))); F = rng.normal(size=n); h = rng.normal(size=n)
        m = [_mfree(lgibbs(lq, F + h/b, b), lq, F) for b in bs]
        peak += 0 < int(np.argmax(m)) < len(bs) - 1; vanish += m[-1] < 0.01*max(m)
    print(f"  (e) {N} random instances, beta in [0.25, 64]: interior maximum in {peak}/{N}; M_free(64) < 1% of its maximum in {vanish}/{N}")
    diffs = []
    for _ in range(300):
        n = rng.integers(3, 20); lq = np.log(rng.dirichlet(np.ones(n))); F = rng.normal(size=n); Fh = F + 0.8*rng.normal(size=n); b = 1.5
        h = rng.normal(size=n); lqa = lq + h; lqa -= logsumexp(lqa); lh = lgibbs(lq, Fh, b)
        assert np.abs(lh - lgibbs(lqa, Fh - h/b, b)).max() < 1e-10
        x, y = _mbud(lh, lq, F), _mbud(lh, lqa, F)
        if x is not None and y is not None: diffs.append(abs(x - y))
    print(f"  rejected alternative (budget matched on the actor's own reference): one behaviour, two attributions -> the measure differs by median {np.median(diffs):.2f}, max {max(diffs):.1f} nats ({len(diffs)} instances)")
    dm = []
    for _ in range(300):
        n = rng.integers(3, 20); lq = np.log(rng.dirichlet(np.ones(n))); F = rng.normal(size=n); Fh = F + 0.8*rng.normal(size=n); b = 1.5
        h = rng.normal(size=n); lqa = lq + h; lqa -= logsumexp(lqa); lh = lgibbs(lq, Fh, b)
        dm.append(abs(KLl(lh, lgibbs(lq, F, b)) - KLl(lh, lgibbs(lqa, F, b))))
    print(f"  Prop 25 (reference attribution): M_own under (q, F_hat) vs (q_A, F_hat - h/beta), same behaviour: differs in {sum(d > 1e-9 for d in dm)}/300, median {np.median(dm):.2f} nats")


# =====================================================================================================
# R7-3 block: Lemma 5.1, the measurement-layer facts about the Gibbs family (never numerically checked before R7-3)
# =====================================================================================================
def V33():
    print("\n[V33] Lemma 5.1: t -> KL(p_{G,t}||q) strictly increasing to log 1/q(argmax G); t -> E_{p_{G,t}}G strictly increasing with derivative Var_{p_{G,t}}(G)")
    rng = np.random.default_rng(33); ed = 0; eda = 0; el = 0; fails = 0; pts = 0; skipped = 0
    for _ in range(2000):
        n = rng.integers(3, 40); q = rng.dirichlet(np.ones(n)*rng.uniform(0.2, 3)); lq = np.log(q); G = rng.normal(size=n)*rng.uniform(0.2, 3)
        top = G >= G.max() - 1e-12; L = np.log(1/q[top].sum()); srt = np.sort(np.unique(G))[::-1]; gap = srt[0] - srt[1]
        ts = np.concatenate([[0.0], np.logspace(-3, 2.5, 60)])
        kl = np.array([KL(gibbs(lq, G, t), q) for t in ts]); mu = np.array([gibbs(lq, G, t)@G for t in ts])
        ok = L - kl[1:] > 1e-8                       # resolvable: not yet within 1e-8 of the limit in floating point
        skipped += int((~ok).sum()); pts += int(ok.sum())
        fails += int(((np.diff(kl) <= 0) & ok).sum() + ((np.diff(mu) <= 0) & ok).sum())
        for t in rng.uniform(-3, 3, size=3):
            h = 1e-6; p = gibbs(lq, G, t); var = p@G**2 - (p@G)**2; d = (gibbs(lq, G, t + h)@G - gibbs(lq, G, t - h)@G)/(2*h)
            eda = max(eda, abs(d - var))
            if var > 1e-4: ed = max(ed, abs(d - var)/var)
        el = max(el, abs(KL(gibbs(lq, G, 60/gap), q) - L))
    print(f"  2000 instances, {pts} resolvable grid steps: steps where KL or the mean fails to increase strictly: {fails} ({skipped} steps skipped: within 1e-8 of the limit, saturated in floating point)")
    print(f"  d/dt E_(p_(G,t)) G vs Var_(p_(G,t)) G (central finite difference): max absolute error {eda:.1e}; max relative error where Var > 1e-4: {ed:.1e}")
    print(f"  limit: max |KL(p_(G,t)||q) - log 1/q(argmax G)| at t = 60/gap(G): {el:.1e}")


# =====================================================================================================
# R7-4 block: external reward and the agent's own objective (Def 16, Props 27-30). Pre-registration: 70 Project/R7/R7-4 preregistration (sha256 07a947ec...)
# =====================================================================================================
def _log_phi(D):
    D = np.asarray(D, float); out = np.full(D.shape, -np.inf); nz = D != 0; sm = nz & (np.abs(D) < 1e-3); bg = nz & ~sm
    out[sm] = np.log(D[sm]**2/2*(1 - D[sm]/3 + D[sm]**2/12)); out[bg] = np.log(np.expm1(-D[bg]) + D[bg]); return out
def _log_kl_peaked(lp1, lp2, xr):
    """log KL(p1||p2) for two distributions concentrating on xr, as a sum of non-negative terms in log space"""
    off = np.arange(len(lp1)) != xr; lt = logsumexp(lp1[off] + _log_phi(lp1[off] - lp2[off]))
    le1, le2 = logsumexp(lp1[off]), logsumexp(lp2[off])
    if max(le1, le2) < np.log(1e-8):
        d = abs(le1 - le2); lr = 2*(max(le1, le2) + np.log(-np.expm1(-d))) - np.log(2) if d > 0 else -np.inf
    else:
        e1, e2 = np.exp(le1), np.exp(le2); v = (e1 - e2) + (1 - e1)*(np.log1p(-e1) - np.log1p(-e2)); lr = np.log(v) if v > 0 else -np.inf
    return np.logaddexp(lt, lr)
def _log_seldiff(lp1, lp2, R, xr):
    off = np.arange(len(R)) != xr; D = lp1[off] - lp2[off]; w = R[off] - R[xr]
    val, _ = logsumexp(lp1[off] + np.log(np.abs(np.expm1(-D)) + 1e-300) + np.log(np.abs(w)), b=np.sign(-np.expm1(-D))*np.sign(w), return_sign=True)
    return val

def V34():
    print("\n[V34] Props 27-30: external reward R, contingency m, persistence coupling; instrumental tracking, masking, selection, fake-alignment gap")
    rng = np.random.default_rng(34)
    # ---- Prop 27(b),(c): the Dinkelbach tilt vs a generic optimizer (analytic gradient) over stationary policies
    def inst():
        nc = int(rng.integers(1, 5)); nx = int(rng.integers(2, 7))
        I = dict(nc=nc, nx=nx, lq=[np.log(rng.dirichlet(np.ones(nx))) for _ in range(nc)], G=[rng.normal(size=nx) + 1.0 for _ in range(nc)],
                 R=[rng.normal(size=nx) for _ in range(nc)], m=rng.integers(0, 2, size=nc).astype(float), rho=rng.dirichlet(np.ones(nc)),
                 b=rng.uniform(0.5, 3), g=rng.uniform(0.5, 0.97))
        I['nu'] = rng.uniform(0.1, 1.0)/max(np.ptp(r) for r in I['R']); return I
    def AB(I, P, LP=None):
        LP = LP if LP is not None else [np.log(p) for p in P]
        A = sum(I['rho'][c]*(P[c]@I['G'][c] - np.sum(P[c]*(LP[c] - I['lq'][c]))/I['b']) for c in range(I['nc']))
        B = 1 - I['g']*sum(I['rho'][c]*(1 - I['nu']*I['m'][c]*(I['R'][c].max() - P[c]@I['R'][c])) for c in range(I['nc']))
        return A, B
    def tilt(I):
        b, g, nu = I['b'], I['g'], I['nu']
        h = lambda V: sum(I['rho'][c]*(logsumexp(I['lq'][c] + b*(I['G'][c] + g*V*nu*I['m'][c]*I['R'][c]))/b + g*V*(1 - nu*I['m'][c]*I['R'][c].max())) for c in range(I['nc'])) - V
        lo, hi = -1.0, 1.0
        while h(lo) < 0: lo *= 2
        while h(hi) > 0: hi *= 2
        V = brentq(h, lo, hi, xtol=1e-14)
        return V, [np.exp(lgibbs(I['lq'][c], I['G'][c] + g*V*nu*I['m'][c]*I['R'][c], b)) for c in range(I['nc'])]
    def generic(I, starts=4):
        nx, nc = I['nx'], I['nc']; best = (-np.inf, None)
        def lunpack(z): return [z[c*nx:(c+1)*nx] - logsumexp(z[c*nx:(c+1)*nx]) for c in range(nc)]
        def unpack(z): return [np.exp(l) for l in lunpack(z)]
        def f(z):
            LP = lunpack(z); P = [np.exp(l) for l in LP]; A, B = AB(I, P, LP); V = A/B; grad = []
            for c in range(nc):
                gA = I['rho'][c]*(I['G'][c] - (LP[c] - I['lq'][c] + 1)/I['b']); gB = -I['g']*I['rho'][c]*I['nu']*I['m'][c]*I['R'][c]
                gp = (gA - V*gB)/B; grad.append(P[c]*(gp - P[c]@gp))
            return -V, -np.concatenate(grad)
        for _ in range(starts):
            r = minimize(f, rng.normal(size=nc*nx)*2, jac=True, method='BFGS', options={'gtol': 1e-12, 'maxiter': 10000})
            if -r.fun > best[0]: best = (-r.fun, unpack(r.x))
        return best
    gaps = []; pdiff = []; worse_when_differs = True; p2 = 0.0; kap = []
    for _ in range(80):
        I = inst(); V, P = tilt(I); A, B = AB(I, P); Vg, Pg = generic(I)
        gaps.append(Vg - A/B); d = max(np.abs(P[c] - Pg[c]).max() for c in range(I['nc'])); pdiff.append(d)
        if d > 1e-4 and not (Vg < A/B - 1e-12): worse_when_differs = False
        for c in range(I['nc']):
            if I['m'][c] == 0: p2 = max(p2, np.abs(P[c] - np.exp(lgibbs(I['lq'][c], I['G'][c], I['b']))).max())
        kap.append(I['g']*I['nu']*V)
    print(f"  Prop 27(b) [P1]: 80 instances: generic optimizer minus the tilt solution, value: max {max(gaps):.1e}; policies agree to median {np.median(pdiff):.0e}; "
          f"where they differ by > 1e-4 the generic value is lower: {worse_when_differs}")
    print(f"  Prop 27(c) [P2]: contexts with m_c = 0: max |p_c - own-objective tilt| = {p2:.0e};  derived kappa/m = gamma*nu*V*: median {np.median(kap):.2f}, range [{min(kap):.2f}, {max(kap):.2f}] (negative iff V* < 0)")
    # ---- Prop 27(a): general concave coupling W(y) = a(1 - e^{-k(y - y0)})
    g3 = []
    for _ in range(150):
        nx = int(rng.integers(2, 8)); lq = np.log(rng.dirichlet(np.ones(nx))); G = rng.normal(size=nx); R = rng.normal(size=nx); b = rng.uniform(0.5, 3)
        a, k = rng.uniform(0.2, 3), rng.uniform(0.2, 3); y0 = R.min(); W = lambda y: a*(1 - np.exp(-k*(y - y0))); Wp = lambda y: a*k*np.exp(-k*(y - y0))
        obj = lambda p, lp=None: p@G - np.sum(p*((np.log(p) if lp is None else lp) - lq))/b + W(p@R)
        fk = lambda kk: kk - Wp(np.exp(lgibbs(lq, G + kk*R, b))@R); kk = brentq(fk, 0, a*k + 1e-9) if fk(0) < 0 else 0.0
        pt = np.exp(lgibbs(lq, G + kk*R, b)); best = -np.inf
        for _ in range(4):
            def f(z):
                lp = z - logsumexp(z); p = np.exp(lp); gp = G - (lp - lq + 1)/b + Wp(p@R)*R; return -obj(p, lp), -p*(gp - p@gp)
            r = minimize(f, rng.normal(size=nx)*2, jac=True, method='BFGS', options={'gtol': 1e-12}); best = max(best, -r.fun)
        g3.append(best - obj(pt))
    print(f"  Prop 27(a) [P3]: general concave coupling, 150 instances: generic minus fixed-point tilt value: max {max(g3):.1e}")
    # ---- Props 28, 29 [P4, P5, P8]: masking and the selection differential
    rk, rs, reg_in10, reg_n, nonmono = [], [], 0, 0, 0
    for _ in range(300):
        nx = int(rng.integers(3, 10)); lq = np.log(rng.dirichlet(np.ones(nx))); R = rng.normal(size=nx); G1, G2 = rng.normal(size=nx), rng.normal(size=nx); b = rng.uniform(0.5, 3)
        xr = int(np.argmax(R)); srt = np.sort(R)[::-1]; gR = srt[0] - srt[1]
        kw = np.linspace(30, 60, 31)/(b*gR)                       # asymptotic window: beta*kappa*gap_R in [30, 60]
        L = [(lgibbs(lq, G1 + k*R, b), lgibbs(lq, G2 + k*R, b)) for k in kw]
        lk = np.array([_log_kl_peaked(a1, a2, xr) for a1, a2 in L]); ls = np.array([_log_seldiff(a1, a2, R, xr) for a1, a2 in L])
        for arr, out in ((lk, rk), (ls, rs)):
            ok = np.isfinite(arr)
            if ok.sum() > 10: out.append(np.polyfit(kw[ok], arr[ok], 1)[0]/(-b*gR))
        kg = np.linspace(0, 40, 81); klg = np.array([KL(np.exp(lgibbs(lq, G1 + k*R, b)), np.exp(lgibbs(lq, G2 + k*R, b))) for k in kg])
        nonmono += klg[1:].max() > klg[0]*(1 + 1e-9)
        tail = (kg > 20/(b*gR)) & (klg > 1e-250)                  # the registered fixed-grid test, naive arithmetic
        if tail.sum() > 5:
            reg_n += 1; reg_in10 += abs(np.polyfit(kg[tail], np.log(klg[tail]), 1)[0]/(-b*gR) - 1) <= 0.1
    rk, rs = np.array(rk), np.array(rs)
    print(f"  Prop 28 [P4]: KL between two types' behaviour, log-slope / (-beta gap_R) in the window beta*kappa*gap_R in [30, 60]: min {rk.min():.4f}, max {rk.max():.4f}, "
          f"within 10%: {np.mean(np.abs(rk - 1) <= 0.1):.3f} (n={len(rk)}); as registered (fixed kappa <= 40, naive KL): within 10% in {reg_in10}/{reg_n}")
    print(f"  Prop 28 [P5]: KL(kappa) > KL(0) for some kappa in (0, 40]: {nonmono}/300 = {nonmono/300:.2f}")
    print(f"  Prop 29 [P8]: selection differential log-slope / (-beta gap_R) in the same window: min {rs.min():.4f}, max {rs.max():.4f}, within 10%: {np.mean(np.abs(rs - 1) <= 0.1):.3f} (n={len(rs)})")
    # ---- Prop 30 [P6, P7]: the fake-alignment gap, free measure per context
    def mfree(lh, lq, F):
        ts = np.concatenate([[0.0], np.logspace(-4, 5, 300)]); v = [KLl(lh, lgibbs(lq, F, t)) for t in ts]; i = int(np.argmin(v))
        r = minimize_scalar(lambda t: KLl(lh, lgibbs(lq, F, t)), bounds=(ts[max(i-1, 0)], ts[min(i+1, len(ts)-1)]), method='bounded', options={'xatol': 1e-12})
        return max(0.0, min(r.fun, min(v)))
    ks = [0, 3, 30, 300]; out = {}
    for kind in ('aligned argmax', 'hacked argmax'):
        rat = []; mev_last = []; lim_err = 0.0; depchg = 0.0
        for _ in range(60):
            nx = int(rng.integers(3, 8)); b = rng.uniform(0.5, 3); lq = np.log(rng.dirichlet(np.ones(nx))); F = rng.normal(size=nx); G = rng.normal(size=nx); R = rng.normal(size=nx)
            xF = int(np.argmax(F))
            if kind == 'aligned argmax': R[xF] = np.max(np.delete(R, xF)) + rng.uniform(0.2, 1.0)
            else:
                xR = int(rng.choice([x for x in range(nx) if x != xF])); R[xR] = np.max(np.delete(R, xR)) + rng.uniform(0.2, 1.0)
            mev = [mfree(lgibbs(lq, G + k*R, b), lq, F) for k in ks]; rat.append(mev[-1]/max(mev[0], 1e-300)); mev_last.append(mev[-1])
            if kind == 'hacked argmax':
                sup = max(np.exp(lgibbs(lq, F, t))[int(np.argmax(R))] for t in np.concatenate([[0.0], np.logspace(-4, 4, 2000)]))
                lim_err = max(lim_err, abs(mfree(lgibbs(lq, G + 3000*R, b), lq, F) - (-np.log(sup))))
        out[kind] = (np.array(rat), np.array(mev_last), lim_err)
    ra, ma, _ = out['aligned argmax']; rh, mh, le = out['hacked argmax']
    print(f"  Prop 30(a,b) [P6]: argmax R = argmax F in evaluation: M_free(kappa=300)/M_free(0) < 1% in {np.mean(ra < 0.01):.3f} of 60; deployment is kappa-free by construction (Prop 27(c))")
    print(f"  Prop 30(c) [P7]: argmax R != argmax F: min M_free(kappa=300) = {mh.min():.3f}; median M_free(300)/M_free(0) = {np.median(rh):.2f}; "
          f"limit -log sup_t p_(F,t)(argmax R) matched at kappa = 3000 to {le:.1e}")

# =====================================================================================================
# R7-7 block: target sets and the ordinal target (Def. 17, Props 31-32). Pre-registered in
# `70 Project/R7/R7-7 preregistration.md` (P1-P10, D1-D4, X1-X3) before any computation.
# =====================================================================================================
def _pava(y, w):
    """weighted non-decreasing isotonic regression (pool-adjacent-violators); fitted values and block labels"""
    blocks = []
    for i, (yi, wi) in enumerate(zip(y, w)):
        blocks.append([yi*wi, wi, [i]])
        while len(blocks) > 1 and blocks[-2][0]/blocks[-2][1] > blocks[-1][0]/blocks[-1][1]:
            s_, w_, ix = blocks.pop(); blocks[-1][0] += s_; blocks[-1][1] += w_; blocks[-1][2] += ix
    fit = np.empty(len(y)); lab = np.empty(len(y), int)
    for k, (s_, w_, ix) in enumerate(blocks): fit[ix] = s_/w_; lab[ix] = k
    return fit, lab
def _lev(ph, q, F):
    """levels of F (exact ties), level masses a (actual) and b (reference), level index per state"""
    vals, inv = np.unique(F, return_inverse=True); m = len(vals)
    return vals, inv, np.bincount(inv, ph, m), np.bincount(inv, q, m)
def _ordproj(ph, q, F):
    """Prop. 32(b): p0 = q r0, r0 the q-weighted isotonic regression of the level means of p_hat/q"""
    vals, inv, a, b = _lev(ph, q, F); fit, lab = _pava(a/b, b)
    return q*fit[inv], fit, lab[inv], lab
def _mfree_mm(ph, lq, F):
    """M_free([F]+) by the moment condition of Thm 13: KL(p_hat || p_(F, t_hat+))"""
    q = np.exp(lq); tgt = ph@F; lh = np.log(ph)
    g = lambda t: gibbs(lq, F, t)@F - tgt; hi = 1.0
    if tgt <= q@F or g(0.0) >= 0: return KLl(lh, lq)
    while g(hi) < 0: hi *= 2
    return KLl(lh, lgibbs(lq, F, brentq(g, 0, hi, xtol=1e-14)))
def _mbud_card(ph, lq, F):
    """M_budget([F]+) (Def. 10), tie-aware saturation; None when undefined"""
    q = np.exp(lq); lam = lam_to_kl(lq, F, KL(ph, q))
    return None if np.isinf(lam) else KLl(np.log(ph), lgibbs(lq, F, lam)), lam
def _slsqp_levels(a, b, C, k, starts):
    """min_r C - a.log r over non-decreasing level ratios r (r = T v, v = (r_1, increments)) with b.r = 1, and,
    if k is not None, b.(r log r) = k. Returns the objective values of the feasible end points."""
    m = len(a); T = np.tril(np.ones((m, m)))
    f = lambda v: C - a@np.log(T@v)
    fj = lambda v: T.T@(-a/(T@v))
    cons = [{'type': 'eq', 'fun': lambda v: b@(T@v) - 1, 'jac': lambda v: T.T@b}]
    if k is not None:
        cons.append({'type': 'eq', 'fun': lambda v: b@((T@v)*np.log(T@v)) - k, 'jac': lambda v: T.T@(b*(np.log(T@v) + 1))})
    out = []
    for r0 in starts:
        v0 = np.concatenate([[r0[0]], np.diff(r0)])
        with np.errstate(all='ignore'):
            r = minimize(f, v0, jac=fj, constraints=cons, method='SLSQP', bounds=[(1e-12, None)] + [(0, None)]*(m - 1),
                         options={'ftol': 1e-15, 'maxiter': 2000})
        rr = T@r.x
        if np.all(rr > 0) and abs(b@rr - 1) < 1e-9 and (k is None or abs(b@(rr*np.log(rr)) - k) < 1e-9*max(1, k)):
            out.append(float(f(r.x)))
    return out
def _rand_ratio(rng, b):
    r = np.sort(np.exp(rng.normal(size=len(b))*rng.uniform(0.2, 2))); return r/(b@r)

def V35():
    print("\n[V35] R7-7: target sets and the ordinal target (Def. 17, Props 31-32), against the pre-registration (P1-P10, D1, X1-X3)")
    rng = np.random.default_rng(3507); kinds = 'ABCDEF'; R = []
    for i in range(1200):
        kind = kinds[i % 6]
        n = int(rng.integers(3, 13))
        while True:
            q = rng.dirichlet(np.ones(n))
            if q.min() >= 1e-3: break
        while True:
            F = rng.normal(size=n) if rng.uniform() < 0.5 else rng.integers(0, max(1, n//2) + 1, size=n).astype(float)
            if len(np.unique(F)) >= 2: break
        lq = np.log(q); vals, inv, _, bq = _lev(q, q, F); m = len(vals)
        par = ''
        if kind == 'A':
            while True:
                ph = rng.dirichlet(np.ones(n))
                if ph.min() >= 1e-4: break
        elif kind == 'B':
            psi = np.cumsum(np.exp(rng.normal(size=m))); ph = gibbs(lq, psi[inv], rng.uniform(0, 3))
        elif kind == 'C':
            k = int(rng.choice([2, 4, 16, 64])); Q = np.cumsum(bq); Qm = np.concatenate([[0.0], Q[:-1]])
            ph = q*((Q**k - Qm**k)/bq)[inv]; par = f"k={k}"
        elif kind == 'D':
            al = float(rng.choice([0.1, 0.3])); take = np.zeros(m); left = al
            for j in range(m - 1, -1, -1):
                take[j] = min(bq[j], left); left -= take[j]
                if left <= 0: break
            ph = (1 - 1e-3)*q*(take/bq/al)[inv] + 1e-3*q; par = f"alpha={al}"
        elif kind == 'E':
            sg = float(rng.choice([0.05, 0.3, 1.0])); l = lgibbs(lq, F, rng.uniform(0, 3)) + sg*rng.normal(size=n)
            ph = np.exp(l - logsumexp(l)); par = f"sigma={sg}"
        else:
            ph = gibbs(lq, -F, rng.uniform(0.1, 3))
        ph = ph/ph.sum(); lh = np.log(ph)
        vals, inv, a, b = _lev(ph, q, F)
        p0, r0, blk, lab = _ordproj(ph, q, F); Mord = KL(ph, p0); C = float(ph@(lh - lq))
        # P2: block formula
        bf = sum(ph[blk == B].sum()*KL(ph[blk == B]/ph[blk == B].sum(), q[blk == B]/q[blk == B].sum()) for B in np.unique(blk))
        # P3: budget split
        k_ = KL(ph, q); split = k_ - Mord - KL(p0, q)
        # P1: generic optimizer for M_ord (3 random starts)
        gen = _slsqp_levels(a, b, C, None, [_rand_ratio(rng, b) for _ in range(3)])
        # P4: cross term for 20 random p in C_F; the corollaries (d)
        cross = min(KL(ph, q*rr[inv]) - Mord - KL(p0, q*rr[inv]) for rr in (_rand_ratio(rng, b) for _ in range(20)))
        Mf = _mfree_mm(ph, lq, F); d_free = Mf - Mord - _mfree_mm(p0, lq, F)
        mb = _mbud_card(ph, lq, F); Mb, lam = mb if mb[0] is not None else (None, None)
        d_bud = None if Mb is None else Mb - Mord - KLl(np.log(p0), lgibbs(lq, F, lam))
        # P5: independent membership test for C_F
        yb = a/b; wl = np.max(np.abs(ph/q - yb[inv])/yb[inv])
        in_cone = bool(np.all(np.diff(yb) >= -1e-10*yb[:-1]) and wl <= 1e-10)
        # P6: strong M3 under a fresh strictly increasing psi; the cardinal M_free under the same psi
        psi = np.cumsum(np.exp(rng.normal(size=len(vals)))); F2 = psi[inv]
        Mord2 = KL(ph, _ordproj(ph, q, F2)[0]); Mf2 = _mfree_mm(ph, lq, F2)
        # budget ordinal (P7, P8, D1): 5 starts, the cardinal budget point first, none of them p_hat
        Mbo, agree = None, None
        if Mb is not None:
            st = [np.exp(lam*vals - logsumexp(lam*vals + np.log(b)))] + [_rand_ratio(rng, b) for _ in range(4)]
            vs = sorted(_slsqp_levels(a, b, C, k_, st))
            if vs: Mbo = vs[0]; agree = len(vs) >= 2 and vs[1] - vs[0] <= 1e-7
        # P10 (implementation cross-check): the target-set code for [F]+ against Def. 10's reference code
        uniq_top = np.sum(F == F.max()) == 1
        ref_f = _mfree(lh, lq, F); ref_b = _mbud(lh, lq, F) if uniq_top else None
        R.append(dict(kind=kind, par=par, m=m, Mord=Mord, bf=bf, split=split, gen=gen, cross=cross, d_free=d_free, d_bud=d_bud,
                      in_cone=in_cone, dMord=abs(Mord2 - Mord), dMf=abs(Mf2 - Mf), Mf=Mf, Mb=Mb, Mbo=Mbo, agree=agree,
                      pooled=len(np.unique(lab)) < len(vals), ties=len(vals) < n,
                      p10f=abs(Mf - ref_f), p10b=None if (ref_b is None or Mb is None) else abs(Mb - ref_b)))
    K = lambda *ks: [r for r in R if r['kind'] in ks]
    ok = lambda c: "holds" if c else "FAILS"
    nt = sum(r['ties'] for r in R)
    # P1
    worst = max(r['Mord'] - min(r['gen']) for r in R if r['gen']); ngen = sum(1 for r in R if r['gen'])
    print(f"  P1 (R) closed form: generic optimum below the isotonic value by at most {worst:.1e} (1,200 instances, {nt} with tied levels; "
          f"{ngen} with a feasible generic end point) -> {ok(worst <= 1e-9)}")
    e2 = max(abs(r['Mord'] - r['bf'])/max(1, r['Mord']) for r in R); e3 = max(abs(r['split']) for r in R)
    print(f"  P2 block formula: max difference {e2:.1e} -> {ok(e2 <= 1e-12)}")
    print(f"  P3 budget split KL(p_hat||q) = M_ord + KL(p0||q): max difference {e3:.1e} -> {ok(e3 <= 1e-12)}")
    cmin = min(r['cross'] for r in R); dfm = min(r['d_free'] for r in R); dbm = min(r['d_bud'] for r in R if r['d_bud'] is not None)
    print(f"  P4 (R) cross term min {cmin:.1e} (20 random p in C_F per instance); (d) slack min: free {dfm:.1e}, budget {dbm:.1e} "
          f"-> {ok(cmin >= -1e-12 and dfm >= -1e-10 and dbm >= -1e-10)}")
    dis = sum((r['Mord'] <= 1e-12) != r['in_cone'] for r in R); zBCD = all(r['Mord'] <= 1e-12 for r in K('B', 'C', 'D'))
    posF = min(r['Mord'] for r in K('F'))
    print(f"  P5 M1: M_ord <= 1e-12 disagrees with the independent cone test in {dis} of 1,200; kinds B, C, D all zero: {zBCD}; "
          f"kind F min M_ord {posF:.2e} -> {ok(dis == 0 and zBCD and posF > 1e-9)}")
    dmo = max(r['dMord'] for r in R); a3 = [r for r in K('A') if r['m'] >= 3]; sh6 = np.mean([r['dMf'] > 1e-6 for r in a3])
    print(f"  P6 strong M3: M_ord moves by at most {dmo:.1e} under a random increasing map; the cardinal M_free moves by > 1e-6 in "
          f"{sh6:.3f} of {len(a3)} kind-A instances with >= 3 levels -> {ok(dmo <= 1e-12 and sh6 >= 0.95)}")
    cd = K('C', 'D'); mo7 = max(r['Mord'] for r in cd); bo7 = [r['Mbo'] for r in cd if r['Mbo'] is not None]
    cd3 = [r for r in cd if r['m'] >= 3]; sh7 = np.mean([r['Mf'] > 1e-6 for r in cd3])
    print(f"  P7 R7-5's cases (best-of-k, quantilizers on F; {len(cd)} instances): max M_ord {mo7:.1e} (R); budget ordinal defined and "
          f"solved in {len(bo7)}, max {max(bo7):.1e}; cardinal M_free > 1e-6 in {sh7:.3f} of {len(cd3)} with >= 3 levels (R) "
          f"-> {ok(mo7 <= 1e-12 and max(bo7) <= 1e-8 and sh7 >= 0.90)}")
    for ks in ('C', 'D'):
        for pv in sorted({r['par'] for r in K(ks)}):
            rr = [r for r in K(ks) if r['par'] == pv and r['m'] >= 3]
            print(f"      {ks} {pv}: cardinal M_free median {np.median([r['Mf'] for r in rr]):.3f}, > 1e-6 in {np.mean([r['Mf'] > 1e-6 for r in rr]):.3f} of {len(rr)}")
    bd = [r for r in R if r['Mbo'] is not None]
    lo = min(r['Mbo'] - r['Mord'] for r in bd); hi = max(r['Mbo'] - r['Mb'] for r in bd)
    strict = all(r['Mbo'] - r['Mord'] > 1e-12 for r in bd if r['Mord'] > 1e-9)
    print(f"  P8 where defined and solved ({len(bd)}): min (M_budget_ord - M_ord) {lo:.1e}; max (M_budget_ord - M_budget) {hi:.1e}; "
          f"strict above M_ord whenever M_ord > 1e-9: {strict} -> {ok(lo >= -1e-9 and hi <= 1e-9 and strict)}")
    defd = [r for r in R if r['Mb'] is not None]; ag = np.mean([bool(r['agree']) for r in defd])
    print(f"  D1 budget ordinal: defined in {len(defd)}; the best two of five starts agree to 1e-7 in {ag:.3f} (rule: >= 0.90) -> "
          f"{'numbers quotable' if ag >= 0.9 else 'NOT quotable: ordinal target under the free convention only'}")
    # P9: a context-split agent, ordinal-aligned in evaluation, sign-flipped in deployment (M8)
    ev = [r['Mord'] for r in K('B', 'C')][:200]; dp = [r['Mord'] for r in K('F')][:200]
    agg_ev = [1.0*e + 0.0*d for e, d in zip(ev, dp)]; agg_dep = [0.5*e + 0.5*d for e, d in zip(ev, dp)]
    print(f"  P9 M8, 200 two-context agents (rho_ev = (1, 0), rho_dep = (1/2, 1/2)): max evaluation M_ord {max(agg_ev):.1e}, "
          f"min deployment M_ord {min(agg_dep):.2e} -> {ok(max(agg_ev) <= 1e-12 and min(agg_dep) > 1e-9)}")
    pf = max(r['p10f'] for r in R); pb = max(r['p10b'] for r in R if r['p10b'] is not None)
    print(f"  P10 (implementation part) target-set code for [F]+ against Def. 10's reference code: M_free {pf:.1e}, M_budget {pb:.1e} "
          f"-> {ok(pf <= 1e-10 and pb <= 1e-10)}; the reproduction part is tools/reproduce.py on V1-V34 and F1-F8")
    ae = [r for r in K('A', 'E') if r['Mbo'] is not None and r['Mord'] > 1e-9]
    x1a = np.array([r['Mbo']/r['Mord'] for r in ae]); x1b = np.array([r['Mbo']/r['Mb'] for r in ae])
    print(f"  X1 kinds A, E ({len(ae)}): M_budget_ord / M_ord median [p10, p90] {np.median(x1a):.2f} {np.percentile(x1a, [10, 90]).round(2)}; "
          f"M_budget_ord / M_budget {np.median(x1b):.2f} {np.percentile(x1b, [10, 90]).round(2)}")
    for sg in ('sigma=0.05', 'sigma=0.3', 'sigma=1.0'):
        x2 = np.array([r['Mord']/r['Mf'] for r in K('E') if r['par'] == sg and r['Mf'] > 1e-12])
        print(f"  X2 kind E {sg}: share of the cardinal M_free that is ordering, M_ord / M_free, median [p10, p90] {np.median(x2):.2f} {np.percentile(x2, [10, 90]).round(2)} ({len(x2)})")
    x3 = np.mean([r['pooled'] for r in K('A', 'E')])
    print(f"  X3 kinds A, E: p0 pools more than one level in {x3:.3f}")

# =====================================================================================================
# R7-6a block: intensity caps and distributional targets (Def. 18, Prop. 33). Pre-registered in
# `70 Project/R7/R7-6a preregistration.md` (P1-P7) before any computation.
# =====================================================================================================
def _that(ph, lq, F):
    """t_hat of Thm 13 (moment condition), clipped at 0 from below"""
    tgt = ph@F; g = lambda t: gibbs(lq, F, t)@F - tgt
    if g(0.0) >= 0: return 0.0
    hi = 1.0
    while g(hi) < 0: hi *= 2
    return brentq(g, 0, hi, xtol=1e-14)
def _cap_free(ph, lq, F, s):
    return KLl(np.log(ph), lgibbs(lq, F, min(_that(ph, lq, F), s)))
def _cap_budget(ph, lq, F, s):
    q = np.exp(lq); k = KL(ph, q); ks = np.inf if np.isinf(s) else KLl(lgibbs(lq, F, s), lq)
    if k > ks: return KLl(np.log(ph), lgibbs(lq, F, s))
    lam = lam_to_kl(lq, F, k)
    return None if np.isinf(lam) else KLl(np.log(ph), lgibbs(lq, F, lam))

def V36():
    print("\n[V36] R7-6a: intensity caps and distributional targets (Def. 18, Prop. 33), against the pre-registration (P1-P7)")
    rng = np.random.default_rng(3606); ok = lambda c: "holds" if c else "FAILS"
    e1 = e2 = e4 = e5 = e6 = e7 = 0.0; on_max = 0.0; off_min = np.inf; ordv = np.inf; n_dec = 0; col = []
    for i in range(900):
        n = int(rng.integers(3, 13))
        while True:
            q = rng.dirichlet(np.ones(n)); pT = rng.dirichlet(np.ones(n))
            if min(q.min(), pT.min()) >= 1e-3: break
        lq = np.log(q)
        if i < 600: F = np.log(pT) - lq; s = 1.0
        else: F = rng.normal(size=n); s = float(rng.uniform(0.2, 5))
        kind = i % 4
        if kind == 0:
            while True:
                ph = rng.dirichlet(np.ones(n))
                if ph.min() >= 1e-4: break
        elif kind == 1: ph = gibbs(lq, F, rng.uniform(0, s))
        elif kind == 2: ph = gibbs(lq, F, rng.uniform(1.05*s, 4*s))
        else:
            l = lgibbs(lq, F, rng.uniform(1.05*s, 4*s)) + 0.3*rng.normal(size=n); ph = np.exp(l - logsumexp(l))
        lh = np.log(ph); mf = _cap_free(ph, lq, F, s); mb = _cap_budget(ph, lq, F, s)
        # P1: closed form vs grid + bounded minimisation over [0, s]
        ts = np.linspace(0, s, 400); v = [KLl(lh, lgibbs(lq, F, t)) for t in ts]; t0 = ts[int(np.argmin(v))]
        r = minimize_scalar(lambda t: KLl(lh, lgibbs(lq, F, t)), bounds=(max(0, t0 - s/399), min(s, t0 + s/399)), method='bounded', options={'xatol': 1e-13})
        e1 = max(e1, abs(mf - min(r.fun, min(v))))
        # P2: decomposition when t_hat > s
        th = _that(ph, lq, F)
        if th > s:
            n_dec += 1; e2 = max(e2, abs(mf - (KLl(lh, lgibbs(lq, F, th)) + KLl(lgibbs(lq, F, th), lgibbs(lq, F, s)))))
        # P3: M1 and the capped M5
        if kind == 1: on_max = max(on_max, mf, mb if mb is not None else 0.0)
        else: off_min = min(off_min, mf, mb if mb is not None else np.inf)
        # P4: M3 under F -> aF + c, s -> s/a
        a, c = rng.uniform(0.2, 5), rng.normal()
        e4 = max(e4, abs(_cap_free(ph, lq, a*F + c, s/a) - mf))
        mb2 = _cap_budget(ph, lq, a*F + c, s/a)
        if mb is not None and mb2 is not None: e4 = max(e4, abs(mb2 - mb))
        # P5: order, and s = infinity reproduces Def. 10
        if mb is not None: ordv = min(ordv, mb - mf)
        uniq = np.sum(F == F.max()) == 1
        e5 = max(e5, abs(_cap_free(ph, lq, F, np.inf) - _mfree(lh, lq, F)))
        if uniq:
            b0, bref = _cap_budget(ph, lq, F, np.inf), _mbud(lh, lq, F)
            if b0 is not None and bref is not None: e5 = max(e5, abs(b0 - bref))
        if i < 600:
            # P6: the regularised path of U = -KL(p||p_T) against a generic optimiser
            t = float(rng.uniform(0.2, 5)); lT = np.log(pT)
            obj = lambda z: KLl(z - logsumexp(z), lT) + KLl(z - logsumexp(z), lq)/t
            z = minimize(obj, np.zeros(n), method='BFGS', options={'gtol': 1e-12}).x
            e6 = max(e6, np.abs((z - logsumexp(z)) - lgibbs(lq, F, t/(1 + t))).max())
            # P7 (R): collapsed agents on distributional targets
            pc = gibbs(lq, F, rng.uniform(1.05, 10))
            col.append((_mfree_mm(pc, lq, F), _cap_free(pc, lq, F, 1.0), KL(pc, pT)))
    col = np.array(col); e7 = np.abs(col[:, 1] - col[:, 2]).max()
    print(f"  P1 closed form M(min(t_hat+, s)) against grid + bounded minimisation over [0, s]: max difference {e1:.1e} -> {ok(e1 <= 1e-9)}")
    print(f"  P2 overshoot decomposition D_perp + KL(p_(F,t_hat)||p_max), {n_dec} instances with t_hat > s: max difference {e2:.1e} -> {ok(e2 <= 1e-10)}")
    print(f"  P3 M1 and capped M5: on-segment max {on_max:.1e}; overshoot and off-ray min {off_min:.2e} -> {ok(on_max <= 1e-10 and off_min > 1e-9)}")
    print(f"  P4 M3 under F -> aF + c, s -> s/a: max change {e4:.1e} -> {ok(e4 <= 1e-9)}")
    print(f"  P5 M_free_cap <= M_budget_cap: min gap {ordv:.1e}; s = infinity against Def. 10's reference code: max difference {e5:.1e} -> {ok(ordv >= -1e-10 and e5 <= 1e-10)}")
    print(f"  P6 path of -KL(p||p_T) against a generic optimiser: max log-probability difference {e6:.1e} -> {ok(e6 <= 1e-4)}")
    print(f"  P7 (R) collapsed agents (600): uncapped M_free max {col[:,0].max():.1e}; capped = KL(p_hat||p_T) to {e7:.1e}, min {col[:,1].min():.3f}, median {np.median(col[:,1]):.3f} "
          f"-> {ok(col[:,0].max() <= 1e-10 and e7 <= 1e-10 and col[:,1].min() > 1e-9)}")

# =====================================================================================================
# R7-9 block: the core as a declared intended set; log-convex sets (Def. 19, Prop. 34). Pre-registered in
# `70 Project/R7/R7-9 preregistration.md` (P1-P4) before any computation. All predictions are verification.
# =====================================================================================================
def _hull_proj(lh, L, starts, bounds=None, free_const=False):
    """M over {p ∝ exp(sum_k w_k L[k])}: w in the simplex (bounds None) or w >= 0 (conic, bounds given).
    Convex in w (log-sum-exp). Returns (value, log p°) for each start."""
    ph = np.exp(lh); K = L.shape[0]
    def lp(w): l = w@L; return l - logsumexp(l)
    f = lambda w: float(ph@(lh - lp(w)))
    def g(w):
        p = np.exp(lp(w)); return -(L@ph) + L@p
    out = []
    for w0 in starts:
        if bounds is None:
            cons = [{'type': 'eq', 'fun': lambda w: w.sum() - 1, 'jac': lambda w: np.ones(K)}]
            r = minimize(f, w0, jac=g, constraints=cons, bounds=[(0, 1)]*K, method='SLSQP', options={'ftol': 1e-15, 'maxiter': 3000})
        else:
            r = minimize(f, w0, jac=g, bounds=bounds, method='L-BFGS-B', options={'ftol': 1e-15, 'gtol': 1e-13, 'maxiter': 5000})
        out.append((float(r.fun), lp(r.x)))
    return out

def V37():
    print("\n[V37] R7-9: the core as a declared intended set; log-convex sets (Def. 19, Prop. 34), against the pre-registration (P1-P4)")
    rng = np.random.default_rng(3709); ok = lambda c: "holds" if c else "FAILS"
    d1 = 0.0; p2 = np.inf
    for i in range(400):
        n = int(rng.integers(3, 11)); K = [2, 3, 5][i % 3]
        L = np.log(rng.dirichlet(np.ones(n), size=K)); lh = np.log(rng.dirichlet(np.ones(n)))
        res = _hull_proj(lh, L, [rng.dirichlet(np.ones(K)) for _ in range(5)])
        best = min(res, key=lambda x: x[0]); lp0 = best[1]
        d1 = max(d1, max(np.abs(np.exp(r[1]) - np.exp(lp0)).max() for r in res))
        for _ in range(20):
            w = rng.dirichlet(np.ones(K)); l = w@L; lpp = l - logsumexp(l)
            p2 = min(p2, KLl(lh, lpp) - best[0] - KLl(lp0, lpp))
    print(f"  P1 uniqueness on 400 generic log-convex hulls (K = 2, 3, 5): the minimizers from 5 starts agree to {d1:.1e} -> {ok(d1 <= 1e-6)}")
    print(f"  P2 Pythagorean inequality KL(p_hat||p) - M - KL(p°||p), 20 members per hull: min {p2:.1e} -> {ok(p2 >= -1e-8)}")
    e_cap = e_ord = 0.0
    for i in range(300):
        n = int(rng.integers(3, 11))
        while True:
            q = rng.dirichlet(np.ones(n))
            if q.min() >= 1e-3: break
        lq = np.log(q); lh = np.log(rng.dirichlet(np.ones(n)))
        F = rng.normal(size=n) if i % 2 else rng.integers(0, 4, size=n).astype(float)
        if len(np.unique(F)) < 2: F[0] += 1.0
        s = float(rng.uniform(0.2, 5)); ph = np.exp(lh)
        L = np.vstack([lq, lgibbs(lq, F, s)])
        v = min(r[0] for r in _hull_proj(lh, L, [np.array([a, 1 - a]) for a in (0.1, 0.5, 0.9)]))
        e_cap = max(e_cap, abs(v - _cap_free(ph, lq, F, s)))
        vals = np.unique(F); steps = np.array([(F >= v_).astype(float) for v_ in vals[1:]])
        Lc = np.vstack([lq, steps]); bnds = [(1.0, 1.0)] + [(0, None)]*len(steps)
        vo = min(r[0] for r in _hull_proj(lh, Lc, [np.concatenate([[1.0], rng.uniform(0, 2, len(steps))]) for _ in range(3)], bounds=bnds))
        e_ord = max(e_ord, abs(vo - KL(ph, _ordproj(ph, q, F)[0])))
    print(f"  P3 generic code reproduces the capped free measure (two-point hull {{q, p_(F,s)}}): {e_cap:.1e}; the ordinal measure (conic hull of level steps): {e_ord:.1e} -> {ok(e_cap <= 1e-8 and e_ord <= 1e-8)}")
    dis = 0; tot = 0
    for i in range(200):
        n = int(rng.integers(3, 11))
        while True:
            q = rng.dirichlet(np.ones(n))
            if q.min() >= 1e-3: break
        lq = np.log(q); ph = rng.dirichlet(np.ones(n)); lh = np.log(ph); k = KL(ph, q)
        G = rng.normal(size=n); F = rng.normal(size=n); s = float(rng.uniform(0.5, 4))
        # the budget sphere {KL(p||q) = k} intersected with the log-convex set {p ∝ q e^(aF + bG), a, b >= 0}: not log-convex
        def lp(z): l = lq + z[0]*F + z[1]*G; return l - logsumexp(l)
        f = lambda z: KLl(lh, lp(z)); cons = [{'type': 'eq', 'fun': lambda z: KLl(lp(z), lq) - k}]
        ends = []
        for _ in range(5):
            r = minimize(f, rng.uniform(0, 3, 2), constraints=cons, bounds=[(0, None)]*2, method='SLSQP', options={'ftol': 1e-14, 'maxiter': 2000})
            if r.success and abs(KLl(lp(r.x), lq) - k) < 1e-8: ends.append(r.fun)
        if len(ends) >= 2:
            tot += 1; dis += (max(ends) - min(ends) > 1e-6)
    print(f"  P4 (exploratory) budget sphere intersected with a log-convex cone: 5 starts end more than 1e-6 apart in {dis} of {tot} instances with >= 2 feasible end points")

# =====================================================================================================
# R7-9 run 2: corrected checks (Def. 19, Prop. 34). Pre-registered in
# `70 Project/R7/R7-9 preregistration run 2.md` (Q1-Q3) before any run-2 computation. All verification.
# =====================================================================================================
def _that_full(ph, lq, F):
    """t_hat on the full ray (t in R): the moment condition E_{p_(F,t)} F = E_{p_hat} F"""
    tgt = ph@F; g = lambda t: gibbs(lq, F, t)@F - tgt; lo, hi = -1.0, 1.0
    while g(lo) > 0: lo *= 2
    while g(hi) < 0: hi *= 2
    return brentq(g, lo, hi, xtol=1e-14)

def V38():
    print("\n[V38] R7-9 run 2: corrected checks (Def. 19, Prop. 34), against the run-2 pre-registration (Q1-Q3)")
    rng = np.random.default_rng(3809); ok = lambda c: "holds" if c else "FAILS"
    below = -np.inf; conv = []; q2 = np.inf; q3 = 0.0
    for i in range(300):
        n = int(rng.integers(3, 11))
        while True:
            q = rng.dirichlet(np.ones(n))
            if q.min() >= 1e-3: break
        lq = np.log(q); ph = rng.dirichlet(np.ones(n)); lh = np.log(ph)
        F = rng.normal(size=n) if i % 2 else rng.integers(0, 4, size=n).astype(float)
        if len(np.unique(F)) < 2: F[0] += 1.0
        s = float(rng.uniform(0.2, 5))
        # Q1: the refuting side of the reduction, 20 starts each
        cf_cap = _cap_free(ph, lq, F, s)
        g_cap = min(r[0] for r in _hull_proj(lh, np.vstack([lq, lgibbs(lq, F, s)]), [np.array([a, 1 - a]) for a in rng.uniform(0, 1, 20)]))
        p0, r0, blk, lab = _ordproj(ph, q, F); cf_ord = KL(ph, p0)
        vals = np.unique(F); steps = np.array([(F >= v_).astype(float) for v_ in vals[1:]])
        g_ord = min(r[0] for r in _hull_proj(lh, np.vstack([lq, steps]), [np.concatenate([[1.0], rng.uniform(0, 3, len(steps))]) for _ in range(20)],
                                             bounds=[(1.0, 1.0)] + [(0, None)]*len(steps)))
        below = max(below, cf_cap - g_cap, cf_ord - g_ord)
        conv += [g_cap - cf_cap <= 1e-8, g_ord - cf_ord <= 1e-8]
        # Q2 (i): capped segment, exact projection (Prop. 33(a))
        lp0 = lgibbs(lq, F, min(_that(ph, lq, F), s)); M = KLl(lh, lp0)
        for t in rng.uniform(0, s, 20):
            lp = lgibbs(lq, F, t); a = KLl(lh, lp); q2 = min(q2, (a - M - KLl(lp0, lp)) / max(1.0, a))
        # Q2 (ii): ordinal cone, exact projection (Prop. 32(b))
        _, inv, _, b = _lev(ph, q, F); lp0o = np.log(p0)
        for _ in range(20):
            rr = _rand_ratio(rng, b); lp = lq + np.log(rr[inv]); a = KLl(lh, lp)
            q2 = min(q2, (a - cf_ord - KLl(lp0o, lp)) / max(1.0, a))
        # Q3: full ray, the equality case (Thm 13(a))
        lpf = lgibbs(lq, F, _that_full(ph, lq, F)); Mf = KLl(lh, lpf)
        for t in rng.uniform(-3, 3, 20):
            lp = lgibbs(lq, F, t); a = KLl(lh, lp); q3 = max(q3, abs(a - Mf - KLl(lpf, lp)) / max(1.0, a))
    print(f"  Q1 the refuting side: largest amount by which a generic value (20 starts) is below the closed form, 600 projections: {below:.1e} -> {ok(below <= 1e-10)}")
    print(f"  Q1 (reported) the best of 20 starts is within 1e-8 of the closed form in {np.mean(conv):.3f} of 600 projections")
    print(f"  Q2 Pythagorean inequality on exact projections (capped segment, ordinal cone), relative slack min {q2:.1e} -> {ok(q2 >= -1e-12)}")
    print(f"  Q3 equality on the full ray (Thm 13(a)), relative |slack| max {q3:.1e} -> {ok(q3 <= 1e-12)}")
    dis = tot = 0
    for i in range(200):
        n = int(rng.integers(3, 11))
        while True:
            q = rng.dirichlet(np.ones(n))
            if q.min() >= 1e-3: break
        lq = np.log(q); ph = rng.dirichlet(np.ones(n)); lh = np.log(ph); k = KL(ph, q); G = rng.normal(size=n); F = rng.normal(size=n)
        def lp(z): l = lq + z[0]*F + z[1]*G; return l - logsumexp(l)
        f = lambda z: KLl(lh, lp(z)); cons = [{'type': 'eq', 'fun': lambda z: KLl(lp(z), lq) - k}]; ends = []
        for _ in range(5):
            r = minimize(f, rng.uniform(0, 3, 2), constraints=cons, bounds=[(0, None)]*2, method='SLSQP', options={'ftol': 1e-14, 'maxiter': 2000})
            if r.success and abs(KLl(lp(r.x), lq) - k) < 1e-8: ends.append(r.fun)
        if len(ends) >= 2: tot += 1; dis += (max(ends) - min(ends) > 1e-6)
    print(f"  (reported) budget sphere intersected with a log-convex cone: 5 starts end more than 1e-6 apart in {dis} of {tot} instances")

# =====================================================================================================
# R7-6b block: minimum intensity, the intended segment (Def. 20, Prop. 35). Pre-registered in
# `70 Project/R7/R7-6b preregistration.md` (P1-P5) before any computation. All verification.
# =====================================================================================================
def _seg_free(ph, lq, F, r, s):
    return KLl(np.log(ph), lgibbs(lq, F, min(max(_that_full(ph, lq, F), r), s)))
def _seg_budget(ph, lq, F, r, s):
    q = np.exp(lq); k = KL(ph, q); lh = np.log(ph)
    kr = 0.0 if r == 0 else KLl(lgibbs(lq, F, r), lq)
    ks = np.inf if np.isinf(s) else KLl(lgibbs(lq, F, s), lq)
    if k < kr: return KLl(lh, lgibbs(lq, F, r))
    if k > ks: return KLl(lh, lgibbs(lq, F, s))
    lam = 0.0 if k < 1e-15 else lam_to_kl(lq, F, k)
    return None if np.isinf(lam) else KLl(lh, lgibbs(lq, F, lam))

def V39():
    print("\n[V39] R7-6b: minimum intensity, the intended segment (Def. 20, Prop. 35), against the pre-registration (P1-P5)")
    rng = np.random.default_rng(3909); ok = lambda c: "holds" if c else "FAILS"
    e1 = e3 = e4 = 0.0; on_max = 0.0; off_min = np.inf; ordv = np.inf; base_w = np.inf; base_wo = 0.0; eps_err = 0.0; nthr = 0
    for i in range(600):
        n = int(rng.integers(3, 11))
        while True:
            q = rng.dirichlet(np.ones(n))
            if q.min() >= 1e-3: break
        lq = np.log(q)
        if i % 2 == 0:
            F = rng.normal(size=n); r = float(rng.uniform(0.1, 2)); s = r + float(rng.uniform(0.2, 3))
        else:
            nthr += 1; H = np.zeros(n, bool); H[rng.choice(n, int(rng.integers(1, n)), replace=False)] = True
            F = -H.astype(float); qH = q[H].sum(); eps = float(rng.uniform(0.1, 0.9))*qH
            r = float(np.log(qH*(1 - eps)/(eps*(1 - qH)))); s = np.inf
            eps_err = max(eps_err, abs(gibbs(lq, F, r)[H].sum() - eps))
            # P5: the untouched base model
            base_w = min(base_w, _seg_free(q, lq, F, r, s), _seg_budget(q, lq, F, r, s))
            base_wo = max(base_wo, _seg_free(q, lq, F, 0.0, np.inf), _seg_budget(q, lq, F, 0.0, np.inf))
        hi = s if np.isfinite(s) else r + 3.0
        kind = i % 5
        if kind == 0:
            while True:
                ph = rng.dirichlet(np.ones(n))
                if ph.min() >= 1e-4: break
        elif kind == 1: ph = gibbs(lq, F, rng.uniform(r, hi))
        elif kind == 2: ph = gibbs(lq, F, rng.uniform(0, 0.95*r))
        elif kind == 3: ph = gibbs(lq, F, rng.uniform(1.05*s, 2*s + 1)) if np.isfinite(s) else gibbs(lq, F, rng.uniform(0, 0.95*r))
        else:
            l = lgibbs(lq, F, rng.uniform(r, hi)) + 0.3*rng.normal(size=n); ph = np.exp(l - logsumexp(l))
        lh = np.log(ph); mf = _seg_free(ph, lq, F, r, s); mb = _seg_budget(ph, lq, F, r, s)
        # P1: formula vs grid + bounded minimisation over [r, s]
        top = s if np.isfinite(s) else max(r, _that_full(ph, lq, F)) + 5.0
        ts = np.linspace(r, top, 400); v = [KLl(lh, lgibbs(lq, F, t)) for t in ts]; t0 = ts[int(np.argmin(v))]; h = (top - r)/399
        rr = minimize_scalar(lambda t: KLl(lh, lgibbs(lq, F, t)), bounds=(max(r, t0 - h), min(top, t0 + h)), method='bounded', options={'xatol': 1e-13})
        e1 = max(e1, abs(mf - min(rr.fun, min(v))))
        # P2
        if kind == 1: on_max = max(on_max, mf, mb if mb is not None else 0.0)
        elif kind != 0: off_min = min(off_min, mf, mb if mb is not None else np.inf)
        # P3: order and reductions
        if mb is not None: ordv = min(ordv, mb - mf)
        if np.isfinite(s):
            e3 = max(e3, abs(_seg_free(ph, lq, F, 0.0, s) - _cap_free(ph, lq, F, s)))
            b1, b2 = _seg_budget(ph, lq, F, 0.0, s), _cap_budget(ph, lq, F, s)
            if b1 is not None and b2 is not None: e3 = max(e3, abs(b1 - b2))
        e3 = max(e3, abs(_seg_free(ph, lq, F, 0.0, np.inf) - _mfree(lh, lq, F)))
        if np.sum(F == F.max()) == 1:
            b1, b2 = _seg_budget(ph, lq, F, 0.0, np.inf), _mbud(lh, lq, F)
            if b1 is not None and b2 is not None: e3 = max(e3, abs(b1 - b2))
        # P4: M3
        a, c = rng.uniform(0.2, 5), rng.normal()
        e4 = max(e4, abs(_seg_free(ph, lq, a*F + c, r/a, s/a) - mf))
        m2 = _seg_budget(ph, lq, a*F + c, r/a, s/a)
        if mb is not None and m2 is not None: e4 = max(e4, abs(m2 - mb))
    print(f"  P1 formula KL(p_hat||p_(F,t_hat)) + KL(p_(F,t_hat)||p_(F,t*)) against grid + bounded minimisation over [r, s]: max difference {e1:.1e} -> {ok(e1 <= 1e-9)}")
    print(f"  P2 M1 and M5 within the segment: on-segment max {on_max:.1e}; below-floor, above-cap and off-ray min {off_min:.2e} -> {ok(on_max <= 1e-10 and off_min > 1e-9)}")
    print(f"  P3 M_free_seg <= M_budget_seg: min gap {ordv:.1e}; reductions to Def. 18 (r = 0) and Def. 10 (r = 0, s = inf): max difference {e3:.1e} -> {ok(ordv >= -1e-10 and e3 <= 1e-10)}")
    print(f"  P4 M3 under F -> aF + c, r -> r/a, s -> s/a: max change {e4:.1e} -> {ok(e4 <= 1e-9)}")
    print(f"  P5 threshold policies ({nthr}): base model with the floor min {base_w:.2e}, without max {base_wo:.1e}; floor hits the threshold to {eps_err:.1e} -> {ok(base_w > 1e-9 and base_wo <= 1e-12 and eps_err <= 1e-12)}")

if __name__ == "__main__":
    import sys
    which = sys.argv[1:] or ["V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14","V15","V16","V17","V18","V19","V20","V21","V22","V23","V24","V25","V26","V27","V28","V29","V30","V31","V32","V33","V34","V35","V36","V37","V38","V39"]
    for w in which: globals()[w]()
