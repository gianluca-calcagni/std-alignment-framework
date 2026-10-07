"""T6. Lock-in: a Polya urn against independent fair draws. Each run has a rate; the rate is a random variable."""
import numpy as np
from math import log
rng = np.random.default_rng(6)
runs, n = 400, 20000
rates, gaps = [], []
for _ in range(runs):
    red, blue, logp = 1, 1, 0.0
    draws = rng.random(n)
    for u in draws:
        pr = red / (red + blue)
        if u < pr: logp += log(pr); red += 1
        else: logp += log(1 - pr); blue += 1
    share = (red - 1) / n
    rate = (logp - n * log(0.5)) / n
    klv = share * log(share / 0.5) + (1 - share) * log((1 - share) / 0.5) if 0 < share < 1 else log(2)
    rates.append(rate); gaps.append(abs(rate - klv))
rates = np.array(rates)
print(f"T6: largest |rate - KL(share||1/2)| {max(gaps):.2e} (predicted < 1e-3); rates mean {rates.mean():.4f} "
      f"(predicted {log(2) - 0.5:.4f} ± 0.02), sd {rates.std():.4f} (predicted > 0.05)")
