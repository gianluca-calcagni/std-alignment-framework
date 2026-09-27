# R7-7 post-hoc diagnosis of the predictions that failed as registered (P6, P7, P8, P10; D4).
# NOT pre-registered, and NOT a verify.py block. It regenerates V35's instances exactly (same code, same seed)
# and prints the failing cases. Run from the repository root: python3 "70 Project/R7/r77_diagnose.py"
import inspect, sys, os
sys.path.insert(0, os.getcwd())
import numpy as np
import verify as Vf
src = inspect.getsource(Vf.V35)
src = src.replace("R.append(dict(kind=kind,", "R.append(dict(q=q, F=F, ph=ph, k_=k_, lam=lam, a=a, b=b, C=C, kind=kind,")
src = src.replace("    K = lambda *ks:", "    return R\n    K = lambda *ks:", 1)
src = src.replace('print("\\n[V35]', 'print("\\n[V35 regenerated for diagnosis]')
ns = dict(vars(Vf)); exec(src, ns); R = ns['V35']()
sat = lambda r: np.log(1/r['b'][-1])
print("\nP6 (cardinal part): kind-A instances, >= 3 levels, where M_free is unchanged under psi")
a3 = [r for r in R if r['kind'] == 'A' and r['m'] >= 3]
anti = [r['ph']@r['F'] <= r['q']@r['F'] for r in a3]; moved = [r['dMf'] > 1e-6 for r in a3]
print(f"  anti-aligned (E_p_hat F <= E_q F, so t_hat+ = 0 and M_free = KL(p_hat||q) whatever F): {sum(anti)} of {len(a3)}")
print(f"  moved among the aligned: {np.mean([m for m, x in zip(moved, anti) if not x]):.3f}; among the anti-aligned: {np.mean([m for m, x in zip(moved, anti) if x]):.3f}")
print("\nP7 (cardinal part): kinds C, D with >= 3 levels and M_free <= 1e-6")
for r in [r for r in R if r['kind'] in 'CD' and r['m'] >= 3 and r['Mf'] <= 1e-6][:8]:
    print(f"  {r['kind']} {r['par']}: levels {r['m']}, M_free {r['Mf']:.1e}, p_hat mass on the top level {r['a'][-1]:.6f}")
print("\nP7 (ordinal budget part) and D4: kinds C, D with M_budget_ord > 1e-8")
bad = [r for r in R if r['kind'] in 'CD' and r['Mbo'] is not None and r['Mbo'] > 1e-8]
print(f"  {len(bad)} of {sum(1 for r in R if r['kind'] in 'CD' and r['Mbo'] is not None)}")
for r in bad:
    print(f"  {r['kind']} {r['par']}: levels {r['m']}, M_budget_ord {r['Mbo']:.1e}, budget k {r['k_']:.4f} vs saturation {sat(r):.4f}, "
          f"min level ratio {min(r['a']/r['b']):.1e}, starts agree: {r['agree']}")
print("\nP8 (strict part): M_ord > 1e-9 but M_budget_ord - M_ord <= 1e-12")
for r in [r for r in R if r['Mbo'] is not None and r['Mord'] > 1e-9 and r['Mbo'] - r['Mord'] <= 1e-12]:
    print(f"  {r['kind']} {r['par']}: M_ord {r['Mord']:.2e}, gap {r['Mbo'] - r['Mord']:.1e}, k {r['k_']:.4f} vs saturation {sat(r):.4f}")
print("\nP10 (implementation part): |M_budget(target-set code) - M_budget(Def. 10 reference code)| > 1e-10")
for r in [r for r in R if r['p10b'] is not None and r['p10b'] > 1e-10]:
    print(f"  {r['kind']} {r['par']}: diff {r['p10b']:.1e}, M_budget {r['Mb']:.3e}, lambda {r['lam']:.3e}, k {r['k_']:.6f} vs saturation {sat(r):.6f}")
print("\nP8, the scaling of the gap: (M_budget_ord - M_ord) / M_ord^2 where the five starts agree, by the size of M_ord")
for lo, hi in ((1e-9, 1e-6), (1e-6, 1e-4), (1e-4, 1e-2), (1e-2, 1e2)):
    g = [(r['Mbo'] - r['Mord'])/r['Mord']**2 for r in R if r['Mbo'] is not None and r['agree'] and lo < r['Mord'] <= hi]
    gl = [(r['Mbo'] - r['Mord'])/r['Mord'] for r in R if r['Mbo'] is not None and r['agree'] and lo < r['Mord'] <= hi]
    if g: print(f"  M_ord in ({lo:.0e}, {hi:.0e}]: {len(g)} instances; gap/M_ord^2 median {np.median(g):.2f} [p10 {np.percentile(g, 10):.2f}, p90 {np.percentile(g, 90):.2f}]; gap/M_ord median {np.median(gl):.1e}")
print("\nP10, relative size of the implementation difference")
for r in [r for r in R if r['p10b'] is not None and r['p10b'] > 1e-10]:
    print(f"  relative difference {r['p10b']/r['Mb']:.1e}")
