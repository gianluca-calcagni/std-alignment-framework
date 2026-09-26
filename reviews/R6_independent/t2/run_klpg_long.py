import time, pickle
from t2_r6 import *
q, F, E1, E2 = v5_pair(); b = 30.0; out = {}
qb, Fb, Fhb = tb_instance()
for name, (qq, G) in {'F': (q, F), 'E1': (q, F+E1), 'E2': (q, F+E2), 'TB_Fh': (qb, Fhb)}.items():
    t0 = time.time(); ts, P = flow_path(qq, G, beta=b, T=1e16, npts=3000)
    ps = tilt(qq, G, b); dist = [np.abs(p-ps).max() for p in P]
    # first time within 1e-8
    hit = next((ts[i] for i, x in enumerate(dist) if x <= 1e-8), None)
    out[name] = (ts, dist)
    print(f'{name}: final max|p-p*| = {dist[-1]:.2e}; KL(p_T||p*) = {KL(P[-1], ps):.2e}; first t with max|p-p*|<=1e-8: {hit}; secs {time.time()-t0:.1f}', flush=True)
pickle.dump(out, open('klpg_long.pkl', 'wb'))
