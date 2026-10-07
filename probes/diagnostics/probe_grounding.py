"""Probe for the numbers in the Notes of [P50] and [P51]: how much the trainer's optimum on a signal evaluator tampers,
how its share of the departure moves away from the small-intensity limit 1 − R², and, for an actor that measures each
world n times and keeps the best signal, how much of its tampering the signals alone, the fall on re-measurement and an
exact audit reveal. Random channels from 4 worlds to 5 signals. Exploratory, not a check.
Usage: python3 probes/diagnostics/probe_grounding.py
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from checks.common import kl, tilt, simplex_interior                               # noqa: E402
from checks.test_identifiability import var                                        # noqa: E402
from checks.test_diagnostics import pairs, tampering, least_tampering, remeasured   # noqa: E402


def best_of(K, Fh, n):
    """The channel of an actor that measures each world n times through K and keeps the signal that Fh scores highest."""
    order = np.argsort(Fh); below = np.cumsum(K[:, order], 1); best = np.zeros_like(K)
    best[:, order] = below ** n - np.c_[np.zeros(len(K)), below[:, :-1]] ** n
    return best / best.sum(1, keepdims=True)


def main():
    r = np.random.default_rng(5001); W, S = 4, 5
    T2, shares, signals, fall = [], {t: [] for t in (0.01, 0.5, 2.0, 8.0)}, {n: [] for n in (2, 4, 16)}, []
    for _ in range(200):
        qW = simplex_interior(r, W); K = np.array([simplex_interior(r, S) for _ in range(W)]); q = pairs(qW, K)
        Fh = r.normal(0, 1, S); FhX = np.tile(Fh, W); R2 = var(qW, K @ Fh) / var(q.ravel(), FhX)
        for t in shares:
            pt = tilt(q.ravel(), t * FhX)
            shares[t].append(tampering(pt.reshape(W, S), K) / kl(pt, q.ravel()) - (1 - R2))
        T2.append(tampering(tilt(q.ravel(), 2 * FhX).reshape(W, S), K))
        for n in signals:
            p = pairs(qW, best_of(K, Fh, n)); T = tampering(p, K)
            signals[n].append(least_tampering(p.sum(0), K)[0] / T)
            if n == 4:
                fall.append(2 * remeasured(p, K, Fh, qW)[1] ** 2 / (Fh.max() - Fh.min()) ** 2 / T)
    print("trainer's optimum at intensity 2: tampering, min", f"{min(T2):.2f}", "median", f"{np.median(T2):.2f}",
          "max", f"{max(T2):.2f}", "nats")
    for t, d in shares.items():
        print(f"intensity {t}: tampering's share of the departure minus 1 − R², median {np.median(d):+.3f},",
              f"range {min(d):+.3f} to {max(d):+.3f}")
    for n, v in signals.items():
        print(f"best of {n} measurements: signals alone reveal a median {np.median(v):.0%} of the tampering",
              f"(range {min(v):.0%} to {max(v):.0%})")
    print("best of 4: the fall on re-measurement, through Pinsker, reveals a median", f"{np.median(fall):.0%}",
          f"(range {min(fall):.0%} to {max(fall):.0%}); an exact audit reveals all of it ([P51](iii))")


if __name__ == "__main__":
    main()
