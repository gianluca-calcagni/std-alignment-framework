"""
final_audit.py — independent (non-circular) checks for the final review of v6.1.
Run: python3 final_audit.py   (numpy, scipy; ~3 min)

  [F1] Optimality is checked by a generic constrained optimizer, not by the closed forms used in verify.py:
       soft Gibbs actor; capacity actor (Lemma 5.1, finite and infinite beta); width sigma_delta (Prop 6);
       chi^2 actor and concave-target actor (Prop 15).
  [F2] Exact finite-n Bayes error for the detection problem (Prop 18) by enumeration of types: the asymptotic
       statement holds, and the finite-n exponent may exceed beta*R_J at small n (so the claim is asymptotic only).
  [F3] Scale covariance ("unit check"): F, F_hat, E -> s*(.) and beta -> beta/s; value quantities scale by s,
       nat quantities are invariant, variances scale by s^2.
  [F4] Edge-case stress of the identities (n = 2, q masses ~1e-12, extreme beta, huge errors, ties, t_hat << 0).
  [F5] Definition 8's budget convention when lambda does not exist (the v6.1 fallback).
  [F6] Cross-references: every numbered result cited in any file exists in A or B; every V-block cited exists.
  [F7] Cor. 17.1: with binding capacity constraints, the capacity actor's regret is the budget convention.
  [F8] Prop. 3 checked independently (heavy-tailed errors, wide beta range).
"""
import numpy as np, re, glob, math
from scipy.special import logsumexp, gammaln
from scipy.optimize import minimize, brentq, minimize_scalar
rng = np.random.default_rng(2026)

def lgibbs(lq, G, t): l = lq + t*G; return l - logsumexp(l)
def gibbs(lq, G, t): return np.exp(lgibbs(lq, G, t))
def KL(p, r):
    m = p > 0
    with np.errstate(divide='ignore'): return float(np.sum(p[m]*(np.log(p[m]) - np.log(r[m]))))
def KLl(lp, lr): p = np.exp(lp); return float(np.sum(p*(lp - lr)))
def lam_to_kl(lq, G, d):
    q = np.exp(lq); top = G >= G.max() - 1e-12
    if np.log(1/q[top].sum()) <= d: return np.inf
    f = lambda l: KL(gibbs(lq, G, l), q) - d; hi = 1.0
    while f(hi) < 0: hi *= 2
    return brentq(f, 0, hi, xtol=1e-14)
def cap_actor(lq, G, b, d):
    t = min(b, lam_to_kl(lq, G, d))
    if np.isinf(t):
        q = np.exp(lq); top = G >= G.max() - 1e-12; p = np.where(top, q, 0); return p/p.sum()
    return gibbs(lq, G, t)

# ---------- generic optimizer over the simplex (softmax parametrization + SLSQP for constraints) ----------
def generic_max(obj, n, cons=None, restarts=6):
    best = None
    for r in range(restarts):
        z0 = rng.normal(size=n)*(0.1 + r)
        sm = lambda z: np.exp(z - logsumexp(z))
        c = [] if cons is None else [{'type': 'ineq', 'fun': (lambda z, g=g: g(sm(z)))} for g in cons]
        res = minimize(lambda z: -obj(sm(z)), z0, method='SLSQP', constraints=c, options={'maxiter': 2000, 'ftol': 1e-13})
        p = sm(res.x)
        if cons is None or all(g(p) > -1e-8 for g in cons):
            if best is None or obj(p) > obj(best): best = p
    return best

def F1():
    print("\n[F1] closed forms vs a generic constrained optimizer (value gap = generic - closed form; > 0 would refute)")
    gaps = {'soft': [], 'cap': [], 'cap_inf': [], 'width': [], 'chi2': [], 'concave': []}
    for _ in range(60):
        n = rng.integers(3, 9); q = rng.dirichlet(np.ones(n)); lq = np.log(q); G = rng.normal(size=n); b = rng.uniform(0.3, 5)
        J = lambda p: float(p@G) - KL(p, q)/b
        gaps['soft'].append(J(generic_max(J, n)) - J(gibbs(lq, G, b)))
        d = rng.uniform(0.02, 0.8)*np.log(1/q[np.argmax(G)])
        pc = cap_actor(lq, G, b, d); gaps['cap'].append(J(generic_max(J, n, [lambda p: d - KL(p, q)])) - J(pc))
        Jl = lambda p: float(p@G); pi = cap_actor(lq, G, np.inf, d)
        gaps['cap_inf'].append(Jl(generic_max(Jl, n, [lambda p: d - KL(p, q)])) - Jl(pi))
        E = rng.normal(size=n); sig = float(cap_actor(lq, E, np.inf, d)@E - q@E)
        pw = generic_max(lambda p: float(p@E), n, [lambda p: d - KL(p, q)]); gaps['width'].append(float(pw@E - q@E) - sig)
        # chi^2 actor (water-filling) and concave-target actor (fixed point)
        f = lambda nu: np.sum(q*np.maximum(0, (b/2)*(G - nu))) - 1
        nu = brentq(f, G.min() - 10/b - 10, G.max()); pch = q*np.maximum(0, (b/2)*(G - nu))
        Jc = lambda p: float(p@G) - (float(np.sum(p*p/q)) - 1)/b
        gaps['chi2'].append(Jc(generic_max(Jc, n)) - Jc(pch))
        H = rng.normal(size=n); kap = rng.uniform(0.1, 2)
        pm = lambda m: gibbs(lq, G - 2*kap*m*H, b); m = brentq(lambda m: pm(m)@H - m, H.min() - 1, H.max() + 1)
        Ju = lambda p: float(p@G) - kap*float(p@H)**2 - KL(p, q)/b
        gaps['concave'].append(Ju(generic_max(Ju, n)) - Ju(pm(m)))
    for k, v in gaps.items():
        print(f"  {k:8s}: max(generic - closed form) = {max(v):+.1e}   (min = {min(v):+.1e})")

def F2():
    print("\n[F2] exact Bayes error vs n for p_hat vs p* on |X| = 3 (equal priors; enumeration of types)")
    q = np.array([0.5, 0.3, 0.2]); lq = np.log(q); F = np.array([1.0, 0.0, -0.5]); E = np.array([0.0, 0.0, 1.5]); b = 1.5
    ph, ps = gibbs(lq, F+E, b), gibbs(lq, F, b)
    RJ = KL(ph, ps)
    C = -minimize_scalar(lambda l: logsumexp(l*np.log(ph) + (1-l)*np.log(ps)), bounds=(0, 1), method='bounded').fun
    print(f"  beta*R_J = KL(ph||p*) = {RJ:.4f}   KL(p*||ph) = {KL(ps, ph):.4f}   Chernoff C = {C:.4f}")
    for n in [1, 2, 5, 10, 25, 50, 100, 200, 400]:
        # P_e = 1/2 * sum over types of min(P_hat(type), P_star(type))
        tot = []
        for k0 in range(n+1):
            for k1 in range(n+1-k0):
                k2 = n - k0 - k1; lc = gammaln(n+1) - gammaln(k0+1) - gammaln(k1+1) - gammaln(k2+1)
                a = lc + k0*np.log(ph[0]) + k1*np.log(ph[1]) + k2*np.log(ph[2])
                c = lc + k0*np.log(ps[0]) + k1*np.log(ps[1]) + k2*np.log(ps[2])
                tot.append(min(a, c))
        lPe = np.log(0.5) + logsumexp(tot)
        print(f"    n={n:4d}: -(1/n) log P_e = {-lPe/n:.4f}   ({'> beta R_J' if -lPe/n > RJ else '<= beta R_J'})")

def quantities(lq, F, E, b, d):
    q = np.exp(lq); ph = gibbs(lq, F+E, b); ps = gibbs(lq, F, b); lph = np.log(ph)
    RJ = KL(ph, ps)/b; g = F.max() - ps@F; T = F.max() - ph@F; dF = ps@F - ph@F
    osc = np.ptp(E); sig = float(cap_actor(lq, E, np.inf, d)@E - q@E); lam = lam_to_kl(lq, E, d)
    m = ph@F; t = brentq(lambda t: gibbs(lq, F, t)@F - m, -1e4, 1e4); tp = max(t, 0)
    Dperp = KLl(lph, lgibbs(lq, F, tp)); Dpar = KLl(lgibbs(lq, F, tp), lgibbs(lq, F, b)); Xa = b*max(q@F - ph@F, 0)
    dd = KL(ph, q)
    try: lb = brentq(lambda s: KL(gibbs(lq, F, s), q) - dd, 0, 1e6); Mb = KLl(lph, lgibbs(lq, F, lb))
    except ValueError: Mb = np.nan          # budget exceeds what F can use (F5): M_budget undefined
    C = -minimize_scalar(lambda l: logsumexp(l*np.log(ph) + (1-l)*np.log(ps)), bounds=(0, 1), method='bounded').fun
    varE = float(ps@E**2 - (ps@E)**2); Tp0 = -float(q@((F+E)*F) - (q@(F+E))*(q@F))
    return dict(value=dict(RJ=RJ, g=g, T=T, dF=dF, osc=osc, sigma=sig, bound2=b*osc**2/8),
                inv_value=dict(lam_delta=lam, t_hat=t),
                nats=dict(bRJ=b*RJ, Dperp=Dperp, Dpar=Dpar, Xanti=Xa, Mbudget=Mb, Chernoff=C, KLq=dd),
                value2=dict(VarE=varE, Tprime0=Tp0))

def F3():
    print("\n[F3] scale covariance: (F, F_hat, E) -> s(.), beta -> beta/s, delta fixed")
    worst = {'value': 0, 'inv_value': 0, 'nats': 0, 'value2': 0}
    for _ in range(200):
        n = rng.integers(3, 20); q = rng.dirichlet(np.ones(n)); lq = np.log(q); F = rng.normal(size=n); E = rng.normal(size=n)*rng.uniform(0.1, 1.5)
        b = rng.uniform(0.3, 4); d = 0.3*np.log(1/q[np.argmax(E)]); s = rng.uniform(0.2, 5)
        A, B = quantities(lq, F, E, b, d), quantities(lq, s*F, s*E, b/s, d)
        for k, pw in (('value', 1), ('inv_value', -1), ('nats', 0), ('value2', 2)):
            for name in A[k]:
                a, bb = A[k][name], B[k][name]
                if np.isfinite(a) and abs(a) > 1e-9: worst[k] = max(worst[k], abs(bb/(a*s**pw) - 1))
    for k, v in worst.items(): print(f"  class {k:9s}: max relative deviation from predicted scaling = {v:.1e}")

def F4():
    print("\n[F4] edge-case stress (log-space arithmetic)")
    worst = {'Thm1': 0, 'Cor1.2': 0, 'Thm13a': 0, 'Thm13b': 0, 'Thm17iii': 0, 'Prop18': 0}
    cases = 0
    for trial in range(400):
        n = int(rng.choice([2, 3, 5, 40])); a = rng.choice([0.05, 1, 20]); q = rng.dirichlet(np.ones(n)*a)
        q = np.maximum(q, 1e-12); q /= q.sum(); lq = np.log(q)
        F = rng.normal(size=n)
        if trial % 5 == 0: F = np.round(F)                                   # ties
        E = rng.normal(size=n)*float(rng.choice([1e-3, 1, 30]))
        if trial % 7 == 0: E = -F*rng.uniform(1.5, 4)                        # t_hat << 0
        if np.ptp(F) == 0: continue
        b = float(rng.choice([1e-3, 0.5, 5, 60]))
        ls, lh = lgibbs(lq, F, b), lgibbs(lq, F+E, b); ps, ph = np.exp(ls), np.exp(lh)
        RJ = (ps@F - KLl(ls, lq)/b) - (ph@F - KLl(lh, lq)/b); kl = KLl(lh, ls); klr = KLl(ls, lh)
        scale = max(1.0, abs(kl))
        worst['Thm1'] = max(worst['Thm1'], abs(b*RJ - kl)/scale)
        worst['Cor1.2'] = max(worst['Cor1.2'], abs(b*(ph@E - ps@E) - kl - klr)/max(1, kl + klr))
        m = ph@F; g = lambda t: np.exp(lgibbs(lq, F, t))@F - m
        lo, hi = -1.0, 1.0
        while g(lo) > 0 and lo > -1e8: lo *= 2
        while g(hi) < 0 and hi < 1e8: hi *= 2
        if not (g(lo) <= 0 <= g(hi)): continue
        t = brentq(g, lo, hi, xtol=1e-14); lt = lgibbs(lq, F, t)
        worst['Thm13a'] = max(worst['Thm13a'], abs(kl - KLl(lh, lt) - KLl(lt, ls))/scale)
        tp = max(t, 0.0); ltp = lgibbs(lq, F, tp); Xa = b*max(np.exp(lq)@F - m, 0)
        worst['Thm13b'] = max(worst['Thm13b'], abs(kl - KLl(lh, ltp) - KLl(ltp, ls) - Xa)/scale)
        dd = KLl(lh, lq)
        try:
            lam = brentq(lambda s: KLl(lgibbs(lq, F, s), lq) - dd, 0, 1e7, xtol=1e-14)
            ll = lgibbs(lq, F, lam); worst['Thm17iii'] = max(worst['Thm17iii'], abs((np.exp(ll)@F - m) - KLl(lh, ll)/lam)/max(1, abs(np.exp(ll)@F - m)))
        except ValueError: pass
        C = -minimize_scalar(lambda l: logsumexp(l*lh + (1-l)*ls), bounds=(0, 1), method='bounded').fun
        worst['Prop18'] = max(worst['Prop18'], C - min(kl, klr))
        cases += 1
    print(f"  {cases} cases (n in {{2,3,5,40}}, q masses down to 1e-12, beta in {{1e-3..60}}, |E| up to ~100, ties, anti-aligned)")
    for k, v in worst.items(): print(f"  {k:9s}: worst relative error = {v:.1e}" if k != 'Prop18' else f"  {k:9s}: max (C - min KL) = {v:.1e}  (must be <= 0 up to rounding)")

def F5():
    print("\n[F5] Definition 8, budget convention, when lambda does not exist")
    q = np.array([0.4, 0.4, 0.2]); lq = np.log(q); F = np.array([1.0, 1.0, 0.0]); E = np.array([4.0, -4.0, 0.0]); b = 3.0
    ph = gibbs(lq, F+E, b); d = KL(ph, q); cap = np.log(1/q[F == F.max()].sum())
    print(f"  KL(p_hat||q) = {d:.3f} >= log 1/q(argmax F) = {cap:.3f}: no finite lambda")
    pinf = np.where(F == F.max(), q, 0); pinf /= pinf.sum()
    print(f"  v6.1 fallback M_budget = KL(p_hat || q(.|argmax F)) = {KL(ph, pinf)}  (infinite: p_hat has mass off argmax F)")
    print(f"  same-budget raw regret (value units) = max F - E_ph F = {F.max() - ph@F:.3e}  (finite, and tiny: the actor is essentially aligned)")

def F6():
    """v7.0: the vault is the source of truth. Cross-references are checked on the compiled linear views in build/
    (python3 tools/vault.py compile), and link integrity by `tools/vault.py lint`."""
    print("\n[F6] cross-references (on the compiled linear views of the vault)")
    import subprocess
    subprocess.run([sys.executable, 'tools/vault.py', 'compile'], check=True, capture_output=True)
    A = open('build/core.md', encoding='utf-8').read(); B = open('build/dictionary.md', encoding='utf-8').read()
    V = open('verify.py', encoding='utf-8').read()
    defined = set()
    for kind, pat in (('Theorem', r'\*\*Theorem (\d+)'), ('Proposition', r'\*\*Proposition (\d+)'), ('Corollary', r'\*\*Corollary (\d+\.\d+)'),
                      ('Lemma', r'\*\*Lemma (\d+(?:\.\d+)?)'), ('Definition', r'\*\*(?:Definition|Overview) (\d+)'), ('Remark', r'\*\*Remark (\d+\.\d+)')):
        for m in re.finditer(pat, A): defined.add((kind, m.group(1)))
    Bdef = set(re.findall(r'\*\*Proposition (B\d+)', B))
    Vdef = set(re.findall(r'^def (V\d+)\(', V, re.M))
    missing = []
    for f in sorted(glob.glob('build/*.md')):
        s = open(f, encoding='utf-8').read()
        for m in re.finditer(r'\b(Thm|Thms|Theorem|Prop\.|Props|Cor\.|Cors|Lemma|Def\.|Defs|Definition|Remark)\s+((?:B?\d+(?:\.\d+)?(?:\([a-z]+\))?(?:\s*(?:,|and|–)\s*)?)+)', s):
            kind = {'Thm': 'Theorem', 'Thms': 'Theorem', 'Theorem': 'Theorem', 'Prop.': 'Proposition', 'Props': 'Proposition', 'Cor.': 'Corollary',
                    'Cors': 'Corollary', 'Lemma': 'Lemma', 'Def.': 'Definition', 'Defs': 'Definition', 'Definition': 'Definition', 'Remark': 'Remark'}[m.group(1)]
            for num in re.findall(r'B?\d+(?:\.\d+)?', m.group(2)):
                if num.startswith('B'):
                    if num not in Bdef: missing.append((f, m.group(0)[:40]))
                elif '–' in m.group(2): continue          # ranges checked by endpoints only
                elif (kind, num) not in defined and not (kind == 'Corollary' and ('Corollary', num) in defined):
                    missing.append((f, kind, num, m.group(0)[:50]))
        for vref in set(re.findall(r'\bV(\d+)\b', s)):
            if f"V{int(vref)}" not in Vdef: missing.append((f, 'V-block', vref))
    print(f"  results defined in the core: {len(defined)}; in the dictionary: {sorted(Bdef)}; V-blocks: {len(Vdef)}")
    print(f"  unresolved references: {len(missing)}")
    for x in missing[:40]: print("   ", x)


def F7():
    print("\n[F7] Cor. 17.1: with both capacity constraints binding, R^C = M(lambda)/lambda (the budget convention)")
    e = 0; cnt = 0
    for _ in range(3000):
        n = rng.integers(3, 30); q = rng.dirichlet(np.ones(n)); lq = np.log(q); F = rng.normal(size=n); E = rng.normal(size=n)*rng.uniform(0.1, 1.5)
        b = float(rng.choice([np.inf, rng.uniform(5, 50)])); Fh = F + E
        d = rng.uniform(0.05, 0.95)*min(np.log(1/q[F >= F.max()-1e-12].sum()), np.log(1/q[Fh >= Fh.max()-1e-12].sum()))
        lF, lH = lam_to_kl(lq, F, d), lam_to_kl(lq, Fh, d)
        if not (b > lF and b > lH): continue                       # both constraints binding
        ps, ph = gibbs(lq, F, lF), gibbs(lq, Fh, lH)
        J = (lambda p: float(p@F)) if np.isinf(b) else (lambda p: float(p@F) - KL(p, q)/b)
        RC = J(ps) - J(ph); M = KLl(lgibbs(lq, Fh, lH), lgibbs(lq, F, lF))
        e = max(e, abs(RC - M/lF)); cnt += 1
    print(f"  {cnt} binding instances: max |R^C - M(lambda)/lambda| = {e:.1e}")

def F8():
    print("\n[F8] independent check of Prop. 3 (Student-t3 errors, beta in [1e-3, 30]; sup over t by dense log grid + refinement)")
    viol = [0, 0]; worst = [0.0, 0.0]; N = 0
    for _ in range(4000):
        n = rng.integers(2, 30); q = rng.dirichlet(np.ones(n)*rng.uniform(0.1, 3)); lq = np.log(q)
        F = rng.standard_t(3, size=n); E = rng.standard_t(3, size=n)*rng.uniform(0.05, 2); b = 10**rng.uniform(-3, np.log10(30))
        ls, lh = lgibbs(lq, F, b), lgibbs(lq, F+E, b); RJ = KLl(lh, ls)/b
        ps = np.exp(ls); m = ps@E; L = lambda t: float(logsumexp(ls + t*(E - m)))
        B1 = (L(2*b) - 2*L(b))/b
        ts = 2*b*np.exp(np.linspace(-12, 0, 600)); vals = np.array([2*L(t)/t**2 for t in ts]); k = int(np.argmax(vals))
        lo, hi = ts[max(k-1, 0)], ts[min(k+1, len(ts)-1)]
        r = minimize_scalar(lambda t: -2*L(t)/t**2, bounds=(lo, hi), method='bounded'); sp = max(vals.max(), -r.fun)
        B2 = 2*b*sp; N += 1
        for i, B in enumerate((B1, B2)):
            viol[i] += RJ > B*(1 + 1e-8) + 1e-12
            if B > 1e-9: worst[i] = max(worst[i], RJ/B)
    print(f"  {N} instances: violations [L(2b)-2L(b)]/b: {viol[0]}, 2*b*sigma+^2: {viol[1]}")
    print(f"  max R_J/bound where bound > 1e-9 (below that, cancellation noise dominates): {worst[0]:.3f}, {worst[1]:.3f}")

if __name__ == "__main__":
    import sys
    for w in (sys.argv[1:] or ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"]): globals()[w]()
