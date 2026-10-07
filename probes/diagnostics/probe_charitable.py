"""Probe for what became [P48] (first NOTES.md section 7, H32): when the principal's objective is known only to lie in the span
of given functions F, G_1, ..., G_k, the least misalignment any such principal finds is the unexplained misalignment of
[P44], KL(p || p~), attained by the principal whose objective is the named pursuit's exponent; the largest is the
departure KL(p || q). Exploratory, not a check. Usage: python3 probes/diagnostics/probe_charitable.py
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from checks.common import kl, simplex_interior                                     # noqa: E402
from checks.test_misalignment import misalignment                                   # noqa: E402
from checks.test_diagnostics import named_pursuit                                   # noqa: E402


def main():
    r = np.random.default_rng(4801); gaps, below, top = [], 0, []
    for _ in range(200):
        n = int(r.integers(6, 11)); k = int(r.integers(1, 3)); q = simplex_interior(r, n); p = simplex_interior(r, n)
        F = r.normal(0, 1, n); Gs = list(r.normal(0, 1, (k, n))); Phi = np.vstack([F, *Gs])
        pt = named_pursuit(p, q, F, Gs); unexplained = kl(p, pt)
        B = np.column_stack([np.ones(n), Phi.T]); coef = np.linalg.lstsq(B, np.log(pt / q), rcond=None)[0][1:]
        gaps.append(abs(misalignment(p, q, coef @ Phi)[0] - unexplained))           # the most charitable principal
        values = [misalignment(p, q, c @ Phi)[0] for c in r.normal(0, 1, (200, k + 1))]
        below += sum(v < unexplained - 1e-9 for v in values)
        top.append(abs(max(values) - kl(p, q)))
    print("principal at the named pursuit's exponent: worst |M − unexplained| =", f"{max(gaps):.1e}")
    print("random principals in the span below the unexplained misalignment:", below, "of", 200 * 200)
    print("largest misalignment among random principals vs the departure: worst gap", f"{max(top):.1e}")


if __name__ == "__main__":
    main()
