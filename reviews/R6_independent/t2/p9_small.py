# POST-HOC (not pre-registered): KL-PG plateau and eventual convergence on small instances with the V5 structure
from t2_r6 import *
b = 30.0
for n, seed in ((20, 1), (50, 2), (200, 3)):
    rng = np.random.default_rng(seed); q = np.ones(n)/n; G = rng.normal(size=n)
    ps = tilt(q, G, b); ts, P = flow_path(q, G, beta=b, T=1e18, npts=400)
    dist = np.array([np.abs(p - ps).max() for p in P]); kl = np.array([KL(p, q) for p in P])
    o = np.argsort(G)[::-1]; minp2 = min(p[o[1]] for p in P)
    hit = next((ts[i] for i, x in enumerate(dist) if x <= 1e-8 and ts[i] > 0), None)
    print(f'n={n:3d}: gap top-runner-up {G[o[0]]-G[o[1]]:.3f}; p*(runner-up)={ps[o[1]]:.3f}, min along path={minp2:.1e}; '
          f'KL(p*)={KL(ps,q):.3f}, max KL on path={kl.max():.3f}; first t with max|p-p*|<=1e-8: '
          + (f'{hit:.2e}' if hit else f'none by T=1e18 (final {dist[-1]:.1e})'), flush=True)
