# R7-6 go/no-go probe: a distributional target (the principal wants behaviour distributed as p_T).
# Exploratory, NOT pre-registered, not a verify.py block. Seeded. Run: python3 "70 Project/R7/r76_probe.py"
import numpy as np
from scipy.special import logsumexp
from scipy.optimize import minimize, minimize_scalar
rng = np.random.default_rng(7606)
def lt(lq, G, t): l = lq + t*G; return l - logsumexp(l)
def kl(lp, lr): p = np.exp(lp); return float(p @ (lp - lr))
def inf_path(lh, path, hi=200.0):
    ts = np.concatenate([[0.0], np.logspace(-3, np.log10(hi), 400)])
    v = [kl(lh, path(t)) for t in ts]; t0 = ts[int(np.argmin(v))]
    r = minimize_scalar(lambda t: kl(lh, path(t)), bounds=(0, max(2*t0, 1e-3)), method='bounded', options={'xatol': 1e-12})
    return min(r.fun, min(v))
rows = {k: [] for k in ('exact', 'collapsed t=3', 'collapsed t=10', 'over-diffuse t=0.5', 'random')}; geo = 0.0
for _ in range(300):
    n = int(rng.integers(3, 12)); lq = np.log(rng.dirichlet(np.ones(n))); lT = np.log(rng.dirichlet(np.ones(n)))
    F = lT - lq                                                   # linear target whose tilt at t = 1 is p_T
    ray = lambda t: lt(lq, F, t)                                  # the current intent half-ray
    geo_path = lambda t: lt(lq, F, t/(1 + t))                     # argmax_p [-KL(p||p_T) - KL(p||q)/t], claimed
    # check the claimed maximizer of the non-linear objective with a generic optimizer, at one t
    t = float(rng.uniform(0.2, 5)); obj = lambda z: (kl(z - logsumexp(z), lT) + kl(z - logsumexp(z), lq)/t)
    z = minimize(obj, np.zeros(n), method='BFGS', options={'gtol': 1e-10}).x; geo = max(geo, np.abs((z - logsumexp(z)) - geo_path(t)).max())
    for k, lh in (('exact', lT), ('collapsed t=3', ray(3.0)), ('collapsed t=10', ray(10.0)), ('over-diffuse t=0.5', ray(0.5)),
                  ('random', np.log(rng.dirichlet(np.ones(n))))):
        rows[k].append((inf_path(lh, ray), inf_path(lh, geo_path, 1e6), kl(lh, lT)))
print(f"claimed intent path p_t ∝ q^(1/(1+t)) p_T^(t/(1+t)) vs generic optimizer: max log-prob error {geo:.1e} (300 instances)")
print("behaviour            | linear free measure (ray of log(p_T/q)) | non-linear free measure (path to p_T) | KL(p_hat||p_T)")
for k, v in rows.items():
    a = np.array(v); med = np.median(a, 0)
    print(f"{k:20s} | median {med[0]:.3f}, > 1e-6 in {np.mean(a[:,0] > 1e-6):.2f} | median {med[1]:.3f}, > 1e-6 in {np.mean(a[:,1] > 1e-6):.2f} | median {med[2]:.3f}")
