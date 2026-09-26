import sys, pickle, time
from t2_r6 import *
lo, hi = int(sys.argv[1]), int(sys.argv[2]); dg = np.geomspace(0.05, 3, 10); tol = 1e-9
out = []
def bon_curves(q, G, H, nmax=200000):
    ns = np.unique(np.round(np.geomspace(1, nmax, 400)).astype(int))
    ks = np.array([KL(bon(q, G, n), q) for n in ns]); eH = np.array([bon(q, G, n)@H for n in ns])
    return ks, eH
t0 = time.time()
for i, (q, F, Fh) in enumerate(v25_instances()):
    if i < lo: continue
    if i >= hi: break
    rec = {'i': i}
    sat = min(np.log(1/q[np.argmax(F)]), np.log(1/q[np.argmax(Fh)]))
    ds = [d for d in dg if d < sat - 1e-6]
    # Gibbs capacity actor
    mid, R = [], []
    for d in ds:
        a, b_ = gibbs_at_kl(q, Fh, d), gibbs_at_kl(q, F, d); mid.append(a@Fh - b_@Fh); R.append(b_@F - a@F)
    rec['Gibbs'] = (min(mid, default=np.inf), min(R, default=np.inf))
    # BoN at matched KL (interpolation in KL between integer n) and at equal n
    kh, fhh = bon_curves(q, Fh, Fh); kf, ffh = bon_curves(q, F, Fh); _, fhf = bon_curves(q, Fh, F); _, fff = bon_curves(q, F, F)
    mid, R = [], []
    for d in ds:
        if d > kh.max() or d > kf.max(): continue
        mid.append(np.interp(d, kh, fhh) - np.interp(d, kf, ffh)); R.append(np.interp(d, kf, fff) - np.interp(d, kh, fhf))
    rec['BoN_KL'] = (min(mid, default=np.inf), min(R, default=np.inf))
    rec['BoN_n'] = (float(np.min(fhh - ffh)), float(np.min(fff - fhf)))
    # VPG exact-gradient flow at matched KL
    ph = flow_path(q, Fh, T=1e7, npts=800)[1]; pf = flow_path(q, F, T=1e7, npts=800)[1]
    mid, R = [], []
    for d in ds:
        a, b_ = at_kl(ph, q, d), at_kl(pf, q, d)
        if a is None or b_ is None: continue
        mid.append(a@Fh - b_@Fh); R.append(b_@F - a@F)
    rec['VPG'] = (min(mid, default=np.inf), min(R, default=np.inf))
    out.append(rec)
pickle.dump(out, open(f'p12_{lo}_{hi}.pkl', 'wb'))
print(f'chunk {lo}-{hi}: {len(out)} instances in {time.time()-t0:.0f}s')
