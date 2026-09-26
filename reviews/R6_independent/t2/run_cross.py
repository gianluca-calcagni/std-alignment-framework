import time, pickle, sys
from t2_r6 import *
q, F, E1, E2 = v5_pair(); Gs = {'F': F, 'E1': F+E1, 'E2': F+E2}
dgrid = np.geomspace(1e-3, 7.5, 200); res = {}
t0 = time.time()
# Gibbs
R = {k: [] for k in ('E1', 'E2')}
for d in dgrid:
    pf = gibbs_at_kl(q, F, d)
    for k in ('E1', 'E2'): R[k].append(pf@F - gibbs_at_kl(q, Gs[k], d)@F)
res['Gibbs'] = R; print('Gibbs done', time.time()-t0, flush=True)
# BoN: integer n grid, KL identical across objectives (uniform q, no ties); interpolate in log KL
ns = np.unique(np.round(np.geomspace(1, 3e6, 900)).astype(int))
kls = np.array([KL(bon(q, F, n), q) for n in ns])
curves = {k: np.array([bon(q, F, n)@F - bon(q, Gs[k], n)@F for n in ns]) for k in ('E1', 'E2')}
chk = max(abs(KL(bon(q, Gs[k], n), q) - KL(bon(q, F, n), q)) for n in (2, 64, 4096) for k in ('E1', 'E2'))
m = kls > 0
res['BoN'] = {k: list(np.interp(np.log(dgrid), np.log(kls[m]), curves[k][m], left=np.nan, right=np.nan)) for k in ('E1', 'E2')}
print('BoN done; max KL mismatch across objectives at equal n:', chk, ' max KL reached', kls.max(), flush=True)
pickle.dump(res, open('cross_part1.pkl', 'wb'))
