# stdalign

The quantities of the framework's reporting standard (`STANDARD.md`), one implementation each, on finite outcomes. Every
function names the item of `CORE.md` or `derived/` it computes, and the checks in `checks/` verify those items' claims
on this code, so what a case imports is what the framework proved and tested. Version 0.1: the interface may change
until 1.0.

Install from the repository's root with `pip install -e .`; it needs NumPy and SciPy only.

## A behaviour known exactly

```python
import numpy as np, stdalign as sa
q = np.array([0.5, 0.3, 0.2])            # the default
F = np.array([0.0, 1.0, 2.0])            # the objective of the standard specification, "pursue F"
p = np.array([0.30, 0.38, 0.32])         # the actor's behaviour
a = sa.assess(p, q, F)
a.misalignment, a.revealed_intensity, a.case    # [P5]: M in nats, t*, and which of the three cases holds
a.departure, a.pursuit_part                     # [P6]: KL(p‖q) = pursuit part + misalignment
```

## A behaviour known from draws

Declare the access before looking at the draws (`STANDARD.md`, field Access), and report the estimate with its interval
(field Uncertainty). The standard errors are those of [P52]'s limit laws, for an actor off the ray at an interior
revealed intensity.

| Access | What is known of each draw | Function |
|---|---|---|
| counts | its outcome; the default and the objective on every outcome | `from_counts(counts, q, F)` |
| log-ratios | `log(p(x)/q(x))` and `F(x)`, as for a language model scored by both policies | `from_log_ratios(log_ratio, objective)` |
| two samples | the same, with draws of the default and their `F` | `from_two_samples(log_ratio, objective, reference_objective)` |

Near the ray, log-ratios give a far smaller variance than counting; far from it, the reweighting they hide costs more
than counting, and draws of the default are needed ([P52], Notes). Each `Estimate` reports `effective_draws`, the
effective number of draws behind that reweighting ([P47]); a small one means the interval is not to be trusted. With
counts, the `chi2_*` fields give [P23]'s reference for the hypothesis that the actor does pursue `F`.

## What is not here yet

The diagnostics ([P43]–[P51]), the evaluator's results, feasibility and stakes are still computed by helpers inside
`checks/`; they move here one at a time (`ROADMAP.md`, step E1). Outcomes that are not finite are not covered.
