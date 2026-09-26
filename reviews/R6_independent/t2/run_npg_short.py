import time, pickle
from t2_r6 import *
q, F, E1, E2 = v5_pair(); Gs = {'F': F, 'E1': F+E1, 'E2': F+E2}; eta = 0.02; out = {}; dev = {}
for k, G in Gs.items():
    t0 = time.time(); P = npg_path(q, G, eta=eta, steps=1000)
    dv = np.array([np.abs(P[i] - tilt(q, G, i*eta)).max() for i in range(len(P))]); kl = np.array([KL(p, q) for p in P])
    out[k] = P; dev[k] = (dv, kl)
    j = int(np.argmax(dv > 1e-8)) if np.any(dv > 1e-8) else None
    print(f'NPG {k}: max dev (t<=20) {dv.max():.2e}; first step with dev>1e-8: {j} (KL there {kl[j] if j is not None else float("nan"):.3f}); final KL {kl[-1]:.3f}; secs {time.time()-t0:.0f}', flush=True)
pickle.dump(out, open('paths_NPG.pkl', 'wb')); pickle.dump(dev, open('npg_dev.pkl', 'wb'))
