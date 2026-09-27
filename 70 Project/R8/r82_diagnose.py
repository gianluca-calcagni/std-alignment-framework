"""R8-2 post-hoc diagnosis (labelled post hoc): P1's per-instance distances and other mixture weights; P2's cone measure at the known point."""
import numpy as np
src = open("r82_toy.py").read(); exec(src[:src.index("rng = np.random")])
rng = np.random.default_rng(4242); d = []; small = []; cone_exact = 0.0
for inst in range(400):
    n = int(rng.integers(3, 7))
    while True:
        q = rng.dirichlet(np.ones(n))
        if q.min() >= 1e-3: break
    lq = np.log(q); F = rng.normal(size=n); G = rng.normal(size=n)
    e0, e5 = tilt(lq, 0*F)@G, tilt(lq, 5*F)@G; v = 0.5*(e0 + e5)
    p0 = level_point(lq, F, G, v, 0.0)[0]; p5 = level_point(lq, F, G, v, 5.0)[0]
    def mid(w):
        lm = (1-w)*np.log(p0) + w*np.log(p5); return np.exp(lm - logsumexp(lm))
    x = dist_to_L(mid(0.5), lq, F, G, v); d.append(x)
    if x <= 1e-6: small.append((inst, x, max(dist_to_L(mid(w), lq, F, G, v) for w in (0.25, 0.75))))
    t0 = 0.0 if e0 < v else 5.0; ph = tilt(lq, t0*F); cone_exact = max(cone_exact, KL(ph, tilt(lq, t0*F + 0*G)))
d = np.array(d)
print(f"P1 midpoint distances: median {np.median(d):.3e}; > 1e-6 on {np.sum(d > 1e-6)} of 400; <= 1e-6 on {len(small)}")
for s in small: print(f"   instance {s[0]}: w=0.5 {s[1]:.2e}; max over w in (0.25, 0.75) {s[2]:.2e}")
print(f"P2 cone measure evaluated at the known cone point (t0, 0): max {cone_exact:.1e}")
