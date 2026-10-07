"""B3. Rational inattention (rate-distortion): an agent with an information cost optimizes its own default, and the
optimized default is discrete. Each state's behaviour is still a tilt of that default: the piles live in the default."""
import numpy as np
from math import log, sqrt
s = np.linspace(0, 1, 1001); rho = np.full(s.size, 1 / s.size)    # uniform states
a = np.linspace(0, 1, 1001)                                        # actions, on the same grid
L = (a[None, :] - s[:, None]) ** 2                                 # squared loss

def blahut_arimoto(beta, iters=20000, tol=1e-13):
    pa = np.full(a.size, 1 / a.size)
    K = np.exp(-beta * (L - L.min(1, keepdims=True)))
    for _ in range(iters):
        cond = K * pa; cond /= cond.sum(1, keepdims=True)              # each state's behaviour: tilt of the default
        new = rho @ cond
        if np.abs(new - pa).max() < tol: pa = new; break
        pa = new
    return pa, cond

def atoms(pa, thresh=1e-4):
    """Count separated groups of mass: maxima of the default holding more than thresh within +-0.02."""
    mass = np.convolve(pa, np.ones(41), mode="same")
    peaks = [i for i in range(1, a.size - 1) if pa[i] >= pa[i - 1] and pa[i] > pa[i + 1] and mass[i] > thresh]
    return peaks

def kl_cells(pa, N):
    idx = np.minimum((a * N).astype(int), N - 1); m = np.bincount(idx, weights=pa, minlength=N)
    k = m > 0
    return float(np.sum(m[k] * np.log(m[k] * N)))

for beta in (3.0, 5.5, 6.5, 8.0, 30.0, 100.0, 300.0):
    pa, cond = blahut_arimoto(beta)
    pk = atoms(pa)
    spread = float(np.sqrt(np.sum(pa * (a - np.sum(pa * a)) ** 2)))
    tilt_err = np.abs(cond - (np.exp(-beta * L) * pa) / (np.exp(-beta * L) * pa).sum(1, keepdims=True)).max()
    print(f"beta={beta:6.1f}: atoms {len(pk):2d} at {np.round(a[pk], 3)}; spread of the default {spread:.4f}; "
          f"max |behaviour - tilt of default| {tilt_err:.1e}; predicted atoms ~ {sqrt(beta / 6):.1f}")
pa, _ = blahut_arimoto(30.0)
print(f"dimension slope of the optimized default at beta=30, w 0.1 -> 0.01: "
      f"{(kl_cells(pa, 100) - kl_cells(pa, 10)) / log(10):.3f}  (predicted > 0.9)")
