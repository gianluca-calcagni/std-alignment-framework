"""R7-10, P5 diagnosis (after the registered run; changes no verdict).
P5 failed on 'M^G constant to 1e-12' (observed 7.3e-12). Hypothesis: floating-point summation when the cell masses
are rebuilt from 2^16 sub-outcomes, not a dependence of M^G on n. Test: rebuild the masses with exact summation
(math.fsum) and compare with np.bincount, on five instances built as in V40's P5."""
import math, sys, numpy as np
sys.path.insert(0, '.')
from verify import _mfree_mm, _cells
# P5's construction, re-created with its own generator (replaying V40's stream up to P5 is costly)
rng = np.random.default_rng(40105)
worst_bin = worst_fsum = worst_mass_bin = worst_mass_fsum = 0.0
for j in range(5):
    m = 4; qG = rng.dirichlet(np.ones(m)); lqG = np.log(qG); FG = rng.normal(size=m); pG = rng.dirichlet(np.ones(m)*3)
    cG = _mfree_mm(pG, lqG, FG)
    for e in range(1, 17):
        k = 2**e; lab = np.repeat(np.arange(m), k); ph = np.empty(m*k)
        for c in range(m):
            blk = np.full(k, pG[c]*1e-6/(k - 1)); blk[0] = pG[c]*(1 - 1e-6); ph[c*k:(c + 1)*k] = blk
        mb = _cells(ph, lab, m); mf = np.array([math.fsum(ph[c*k:(c + 1)*k]) for c in range(m)])
        worst_mass_bin = max(worst_mass_bin, np.abs(mb - pG).max()); worst_mass_fsum = max(worst_mass_fsum, np.abs(mf - pG).max())
        worst_bin = max(worst_bin, abs(_mfree_mm(mb, lqG, FG) - cG)); worst_fsum = max(worst_fsum, abs(_mfree_mm(mf, lqG, FG) - cG))
print(f"cell masses rebuilt: bincount max error {worst_mass_bin:.1e}, fsum max error {worst_mass_fsum:.1e}")
print(f"M^G change over n = 2..2^16: with bincount masses {worst_bin:.1e}; with fsum masses {worst_fsum:.1e}")
