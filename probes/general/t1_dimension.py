"""T1. Misalignment against a fixed smooth behaviour grows like (1 - d)·ln(1/w): d is the information dimension."""
import numpy as np
from math import log, pi, sqrt
rng = np.random.default_rng(1)

def kl_cells(masses, ref):
    m = masses > 0
    return float(np.sum(masses[m] * np.log(masses[m] / ref[m])))

def slope(f, w1, w2):
    return (f(w2) - f(w1)) / (log(1 / w2) - log(1 / w1))

# (a) 90% uniform + 10% atom at 1/pi, against uniform on [0, 1]; N cells of width w = 1/N (closed form)
def kl_pile(w):
    N = round(1 / w)
    return (N - 1) * 0.9 * w * log(0.9) + (0.9 * w + 0.1) * log((0.9 * w + 0.1) / w)
# (b) uniform rounded to a grid of spacing 0.1 (offset 1/pi/100 so no atom sits on a cell edge), against uniform
atoms = (np.arange(10) * 0.1 + 0.05 + 1 / pi / 100) % 1.0
def kl_round(w):
    N = round(1 / w); counts = np.bincount((atoms * N).astype(int), minlength=N) * 0.1
    return kl_cells(counts, np.full(N, w))
# (c) the line y = frac(sqrt(2)·x) in the unit square, against uniform; cells w × w; masses by fine sampling
xs = rng.random(4_000_000); ys = (sqrt(2) * xs) % 1.0
def kl_line(w):
    N = round(1 / w); idx = (xs * N).astype(np.int64) * N + (ys * N).astype(np.int64)
    _, c = np.unique(idx, return_counts=True)
    return kl_cells(c / len(xs), np.full(len(c), w * w))
# (d) the Cantor measure against uniform: exact on triadic grids; sampled on decimal grids
def kl_cantor_triadic(k):
    return k * log(3 / 2)
digits = rng.integers(0, 2, size=(1_000_000, 40)) * 2
cx = digits @ (3.0 ** -np.arange(1, 41))
def kl_cantor(w):
    N = round(1 / w); _, c = np.unique((cx * N).astype(np.int64), return_counts=True)
    return kl_cells(c / len(cx), np.full(len(c), w))

print(f"(a) pile 10%:        slope {slope(kl_pile, 1e-4, 1e-6):.4f}   predicted 0.10")
print(f"(b) rounding to 0.1: slope {slope(kl_round, 1e-3, 1e-5):.4f}   predicted 1.00  (KL at w=0.01: {kl_round(0.01):.4f} = ln 10 = {log(10):.4f})")
print(f"(c) a line in 2-D:   slope {slope(kl_line, 1e-2, 1e-3):.4f}   predicted 1.00")
print(f"(d) Cantor, triadic: slope {(kl_cantor_triadic(12) - kl_cantor_triadic(8)) / (4 * log(3)):.4f}   predicted {log(1.5) / log(3):.4f}")
print(f"    Cantor, decimal: slope {slope(kl_cantor, 1e-3, 1e-5):.4f}   predicted {log(1.5) / log(3):.4f} ± 0.03")
