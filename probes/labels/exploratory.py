"""L1, after its verdicts: not registered, seen. The outer misalignment of the order-preserving evaluator e^F, under the
standard specification of F, at intensities below the registered one (RESULTS.md, Exploratory). Run from the
repository's root: python3 probes/labels/exploratory.py   (a second)
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import stdalign as sa                                                                    # noqa: E402
from stdalign.diagnostics import outer_misalignment                                     # noqa: E402

q = np.full(4, 0.25)
F = np.array([0.0, 1.0, 2.0, 3.0])
for t in (0.02, 0.05, 0.1, 0.2, 0.5, 1.0):
    o = outer_misalignment(q, F, np.exp(F), t)
    d = sa.kl(sa.pursuit(q, np.exp(F), t), q)
    print(f"t = {t:4}: O(t) = {o:.4f} nats, departure {d:.4f}, share {o / d:.3f}")
