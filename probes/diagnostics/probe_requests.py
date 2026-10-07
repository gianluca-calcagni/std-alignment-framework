"""Probe for NOTES.md section 10, the framework read against cooperative inverse reinforcement learning and its
variants, on finite outcomes. It checks four statements and prints a toy request, "get rich", made without saying
"ethically". Exploratory, not a check. Usage: python3 probes/diagnostics/probe_requests.py

(a) Maximum-entropy IRL: the reward fitted by maximum likelihood to a behaviour, over the span of given features, from
    a base behaviour q, gives the tilt of [P48], the most charitable principal of that span.
(b) What a request does not mention moves only through its regression on the request under the default: along the
    pursuit of F, the average of any U equals the average of E_q[U | F] ([P18] with U as the target).
(c) CIRL's deployment theorem as [P42](ii): with a posterior over linear targets, the behaviour least far, on posterior
    average, from the pursuits of the possible targets is the pursuit of the posterior-mean target.
(d) The toy: outcomes are wealth levels, each reached honestly or not; under the default, the dishonest way is rarer
    and richer. A request for wealth, pursued harder, buys dishonesty at a rate set by the default.
"""
import sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from checks.common import kl, tilt, simplex_interior                               # noqa: E402
from checks.test_misalignment import misalignment                                   # noqa: E402
from checks.test_diagnostics import most_charitable, outer                          # noqa: E402


def main():
    r = np.random.default_rng(1001); gap_a, gap_b, gap_c = 0.0, 0.0, 0.0
    for _ in range(200):
        n, k = int(r.integers(6, 12)), int(r.integers(2, 4)); q, p = simplex_interior(r, n), simplex_interior(r, n)
        Phi = r.normal(0, 1, (k, n))
        nll = lambda th: -(p @ np.log(tilt(q, th @ Phi)))                            # (a) expected log-likelihood
        th = minimize(nll, np.zeros(k), method="BFGS", options={"gtol": 1e-12}).x
        gap_a = max(gap_a, np.abs(tilt(q, th @ Phi) - most_charitable(p, q, Phi)[0]).max())
        F, U, t = r.integers(0, 4, n).astype(float), r.normal(0, 1, n), float(r.uniform(0.1, 3))   # (b) ties in F
        m = np.array([q[F == f] @ U[F == f] / q[F == f].sum() for f in F])
        gap_b = max(gap_b, abs(tilt(q, t * F) @ U - tilt(q, t * F) @ m))
        thetas, w = r.normal(0, 1, (5, k)), simplex_interior(r, 5)                   # (c) a posterior on 5 targets
        obj = lambda a: sum(wi * kl(np.exp(a - a.max()) / np.exp(a - a.max()).sum(), tilt(q, th_i @ Phi))
                            for wi, th_i in zip(w, thetas))
        best = minimize(obj, np.log(q), method="BFGS", options={"gtol": 1e-12}).x
        gap_c = max(gap_c, np.abs(np.exp(best - best.max()) / np.exp(best - best.max()).sum()
                                  - tilt(q, (w @ thetas) @ Phi)).max())
    print(f"(a) MaxEnt IRL's fit vs P48's most charitable tilt: worst {gap_a:.1e}")
    print(f"(b) pursuit's average of U vs of its regression on F under q: worst {gap_b:.1e}")
    print(f"(c) posterior-weighted compromise vs pursuit of the posterior mean: worst {gap_c:.1e}")

    wealth = np.repeat(np.arange(1.0, 6.0), 2); honest = np.tile([1.0, 0.0], 5)        # (d) the toy
    q = np.where(honest == 1, 1.0, 0.1) * np.exp(-0.5 * wealth); q /= q.sum()
    wealth = wealth + 1.5 * (1 - honest)                                              # the dishonest way is richer
    m = np.array([q[wealth == v] @ (1 - honest[wealth == v]) / q[wealth == v].sum() for v in wealth])
    print("(d) default: dishonest share", round(float(q @ (1 - honest)), 3))
    for t in (0.0, 0.5, 1.0, 2.0, 4.0):
        p = tilt(q, t * wealth)
        target = lambda wgt: wealth - wgt * (1 - honest)                             # the requester's true target
        M = [misalignment(p, q, target(wgt))[0] for wgt in (0.0, 1.0, 3.0, 10.0)]
        print(f"    intensity {t}: dishonest share {p @ (1 - honest):.3f}; average wealth {p @ wealth:.2f};",
              f"departure {kl(p, q):.3f} nats; outer misalignment against wealth − w·dishonest, w = 1, 3, 10:",
              ", ".join(f"{outer(q, target(wgt), wealth, t):.3f}" for wgt in (1.0, 3.0, 10.0)))
    print("    the regression of 'dishonest' on wealth under the default, by wealth level:",
          ", ".join(f"{v:.1f}: {s:.2f}" for v, s in sorted(set(zip(wealth.tolist(), m.round(2).tolist())))))


if __name__ == "__main__":
    main()
