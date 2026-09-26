import time, pickle, sys
from t2_r6 import *
which = sys.argv[1]; beta = None if which == 'VPG' else 30.0
q, F, E1, E2 = v5_pair(); Gs = {'F': F, 'E1': F+E1, 'E2': F+E2}
paths = {}
for k, G in Gs.items():
    t0 = time.time(); ts, P = flow_path(q, G, beta=beta, T=1e8, npts=6000)
    paths[k] = P; print(which, k, 'time', round(time.time()-t0, 1), 'final KL', KL(P[-1], q), 'n pts', len(P), flush=True)
pickle.dump(paths, open(f'paths_{which}.pkl', 'wb'))
