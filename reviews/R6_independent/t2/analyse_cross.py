import pickle
from t2_r6 import *
q, F, E1, E2 = v5_pair(); dgrid = np.geomspace(1e-3, 7.5, 200)
res = pickle.load(open('cross_part1.pkl', 'rb'))
for which in ('VPG', 'KLPG') + (('NPG',) if __import__('os').path.exists('paths_NPG.pkl') else ()):
    P = pickle.load(open(f'paths_{which}.pkl', 'rb'))
    mono = {k: bool(np.all(np.diff([KL(p, q) for p in P[k]]) >= -1e-12)) for k in P}
    R = {'E1': [], 'E2': []}
    for d in dgrid:
        pf = at_kl(P['F'], q, d)
        for k in ('E1', 'E2'):
            pe = at_kl(P[k], q, d); R[k].append(np.nan if pf is None or pe is None else pf@F - pe@F)
    res[which] = R; print(which, 'KL monotone along path:', mono)
print(f"{'actor':6s} {'d* (KL)':>9s} | ratio R(E1)/R(E2) at d = 1e-3, 0.01, 0.1, 1, 5, 7")
for a, R in res.items():
    r1, r2 = np.array(R['E1']), np.array(R['E2']); ds = crossing(dgrid, r1, r2)
    sel = [np.argmin(abs(dgrid-x)) for x in (1e-3, 0.01, 0.1, 1, 5, 7)]
    print(f"{a:6s} {('%.4f' % ds) if ds else 'none':>9s} | " + '  '.join(f'{r1[i]/r2[i]:.3g}' for i in sel), '  signs flips:', int(np.sum(np.diff(np.sign(r1-r2)) != 0)))
pickle.dump(res, open('cross_all.pkl', 'wb'))
