# POST-HOC (not pre-registered): re-read BoN at exactly matched KL with a randomized actor (mixture of BoN_n, BoN_{n+1})
import pickle, glob
from t2_r6 import *
from scipy.optimize import brentq
o = []
for f in sorted(glob.glob('p12_*_*.pkl')): o += pickle.load(open(f, 'rb'))
bad = sorted({r['i'] for r in o if min(r['BoN_KL']) < -1e-9})
dg = np.geomspace(0.05, 3, 10)
def bon_at_kl(q, G, d, nmax=10**7):
    n = 1
    while KL(bon(q, G, 2*n), q) <= d and n < nmax: n *= 2
    lo, hi = n, 2*n                                   # KL(lo) <= d < KL(hi): bisect to adjacent integers
    while hi - lo > 1:
        mid = (lo+hi)//2
        if KL(bon(q, G, mid), q) <= d: lo = mid
        else: hi = mid
    a0, a1 = bon(q, G, lo), bon(q, G, hi)
    if KL(a1, q) < d: return None
    f = lambda a: KL((1-a)*a0 + a*a1, q) - d
    a = 0.0 if f(0) >= 0 else brentq(f, 0, 1, xtol=1e-14)
    return (1-a)*a0 + a*a1, lo
real = 0; rows = []
for i, (q, F, Fh) in enumerate(v25_instances()):
    if i > max(bad): break
    if i not in bad: continue
    sat = min(np.log(1/q[np.argmax(F)]), np.log(1/q[np.argmax(Fh)])); worst = (0, 0)
    for d in [x for x in dg if x < sat - 1e-6]:
        A = bon_at_kl(q, Fh, d); B = bon_at_kl(q, F, d)
        if A is None or B is None: continue
        mid = A[0]@Fh - B[0]@Fh; R = B[0]@F - A[0]@F
        worst = (min(worst[0], mid), min(worst[1], R))
        if mid < -1e-9 or R < -1e-9: rows.append((i, round(d, 3), A[1], B[1], f'{mid:+.2e}', f'{R:+.2e}'))
    real += (worst[0] < -1e-9) or (worst[1] < -1e-9)
print(f'BoN matched-KL violators under interpolated readout: {len(bad)}; still violating with exact randomized BoN at KL = d: {real}')
for r in rows[:12]: print('  inst, d, n(F-hat), n(F), middle, R:', r)
