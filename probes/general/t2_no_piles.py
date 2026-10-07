"""T2. A step-by-step KL-pursuer of an endpoint threshold produces exactly the endpoint tilt: no pile."""
import numpy as np
from math import comb, log
n, c, phi = 16, 4, 2.0                    # 16 fair +-1 steps; objective 1{S_n < c}; intensity phi
ends = np.arange(-n, n + 1, 2)
g = (ends < c).astype(float)
# backward recursion: h(s, k) = E[exp(phi·g(S_n)) | S_k = s]; the controlled step up has probability 0.5·h(s+1)/h(s)
h = {n: {s: np.exp(phi * (s < c)) for s in ends}}
for k in range(n - 1, -1, -1):
    h[k] = {s: 0.5 * h[k + 1][s + 1] + 0.5 * h[k + 1][s - 1] for s in range(-k, k + 1, 2)}
law = {0: 1.0}
for k in range(n):
    new = {}
    for s, m in law.items():
        up = 0.5 * h[k + 1][s + 1] / h[k][s]
        new[s + 1] = new.get(s + 1, 0) + m * up
        new[s - 1] = new.get(s - 1, 0) + m * (1 - up)
    law = new
controlled = np.array([law[s] for s in ends])
default = np.array([comb(n, (s + n) // 2) / 2 ** n for s in ends])
tilted = default * np.exp(phi * g); tilted /= tilted.sum()
print(f"T2: max |log ratio| controlled vs endpoint tilt = {np.max(np.abs(np.log(controlled / tilted))):.2e}  (predicted < 1e-12)")
print(f"    density ratio to the default, below and above the threshold: "
      f"{np.unique(np.round(controlled / default, 12))}")
