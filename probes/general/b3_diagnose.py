"""B3 diagnosis: is the optimized default at beta = 30 discrete, with Blahut-Arimoto merely slow, or truly spread?"""
import numpy as np
from math import log
s = np.linspace(0, 1, 1001); rho = np.full(s.size, 1 / s.size); a = np.linspace(0, 1, 1001)
L = (a[None, :] - s[:, None]) ** 2
beta = 30.0; K = np.exp(-beta * (L - L.min(1, keepdims=True)))
def kl_cells(pa, N):
    m = np.bincount(np.minimum((a * N).astype(int), N - 1), weights=pa, minlength=N); k = m > 0
    return float(np.sum(m[k] * np.log(m[k] * N)))
pa = np.full(a.size, 1 / a.size); done = 0
for checkpoint in (2_000, 20_000, 100_000, 300_000):
    for _ in range(checkpoint - done):
        z = K @ pa; pa = pa * ((rho / z) @ K)
    done = checkpoint
    core = [(pa[(a > lo) & (a < hi)] @ a[(a > lo) & (a < hi)] / pa[(a > lo) & (a < hi)].sum(),
             np.sqrt(pa[(a > lo) & (a < hi)] @ (a[(a > lo) & (a < hi)] - pa[(a > lo) & (a < hi)] @ a[(a > lo) & (a < hi)] / pa[(a > lo) & (a < hi)].sum()) ** 2 / pa[(a > lo) & (a < hi)].sum()))
            for lo, hi in ((0.0, 0.35), (0.35, 0.65), (0.65, 1.0))]
    rate = float(np.sum(rho[:, None] * (K * pa / (K @ pa)[:, None]) * np.log(K / (K @ pa)[:, None] + 1e-300)))
    print(f"iterations {checkpoint:7d}: atom widths {[round(float(w), 4) for _, w in core]}, "
          f"slope w 0.1->0.01 {(kl_cells(pa, 100) - kl_cells(pa, 10)) / log(10):.3f}, mass of grid points above 1e-3: "
          f"{int(np.sum(pa > 1e-3))}")
