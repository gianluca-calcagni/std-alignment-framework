import pickle, glob, numpy as np
o = []
for f in sorted(glob.glob('p12_*_*.pkl')): o += pickle.load(open(f, 'rb'))
o = sorted({r['i']: r for r in o}.values(), key=lambda r: r['i'])
print(f'instances analysed: {len(o)}  (index range {o[0]["i"]}..{o[-1]["i"]})')
for a in ('Gibbs', 'BoN_n', 'BoN_KL', 'VPG'):
    mid = np.array([r[a][0] for r in o]); R = np.array([r[a][1] for r in o]); ok = np.isfinite(mid)
    vm, vr = np.sum(mid[ok] < -1e-9), np.sum(R[ok] < -1e-9); both = np.sum((mid[ok] < -1e-9) | (R[ok] < -1e-9))
    print(f'{a:7s} tested {ok.sum():4d}: middle-ineq violated {vm:3d} ({100*vm/ok.sum():.1f} %, min {mid[ok].min():+.2e});  '
          f'R<0 {vr:3d} ({100*vr/ok.sum():.1f} %, min {R[ok].min():+.2e});  either {both} ({100*both/ok.sum():.1f} %)')
