"""stdalign: the quantities of the framework's reporting standard (`STANDARD.md`), one implementation each.

Every function names the item of `CORE.md` or `derived/` it computes, and the checks in `checks/` verify those items'
claims on this code. Finite outcomes only, so far; see `stdalign/README.md`.
"""
from .core import as_distribution, as_objective, kl, tilt, pursuit, log_normalizer, kl_tilts, log_mean_exp
from .misalignment import (Assessment, assess, misalignment, revealed_intensity, nearest_intended, best_outcomes,
                           DEFAULT, PURSUIT, BEST_OUTCOMES)
from .estimation import (Estimate, from_counts, from_log_ratios, from_two_samples, effective_draws,
                         COUNTS, LOG_RATIOS, TWO_SAMPLES)
from .projection import project_linear
from .diagnostics import (IntensityTerms, intensity_terms, min_over_intensity, SharedIntensity, shared_intensity,
                          named_pursuit, named_split, drift, condition_split, reweighting_moments, most_charitable,
                          uncertain_target_interval, outer_misalignment, inner_split, pairs, tampering,
                          grounded_pursuit, least_tampering, most_tampering, remeasured)

__version__ = "0.2.0"
