# stdalign

The quantities of the framework's reporting standard (`STANDARD.md`), one implementation each, on finite outcomes. Every
function names the item of `CORE.md` or `derived/` it computes, and the checks in `checks/` verify those items' claims
on this code, so what a case imports is what the framework proved and tested. Version 0.2: the interface may change
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

## The diagnostics

Each function computes one quantity of a diagnostic result, on behaviours known exactly; with draws, a case estimates
them by the plug-in and a bootstrap, as `examples/quickstart.py` does.

| Result | What it computes | Functions |
|---|---|---|
| [P43] | the terms of misalignment at an intensity; several conditions at one shared intensity, and the excess over their own misalignments | `intensity_terms`, `shared_intensity` |
| [P44] | misalignment split into the part named objectives explain and the part they leave | `named_pursuit`, `named_split` |
| [P45], [P46] | the drift of several runs from their average; the reproducible and run-specific differences of two conditions | `drift`, `condition_split` |
| [P47] | the moments of the weights that reweight draws of one behaviour to stand for another | `reweighting_moments` |
| [P48] | the most charitable principal in a family of targets, and the interval of misalignment over the family | `most_charitable`, `uncertain_target_interval` |
| [P49] | outer misalignment at the training's intensity, and the split of a principal's misalignment by the trainer's evaluator | `outer_misalignment`, `inner_split` |
| [P50], [P51] | behaviour on world–signal pairs, its tampering, the grounded pursuit, the interval of tampering consistent with the signals, and a re-measurement | `pairs`, `tampering`, `grounded_pursuit`, `least_tampering`, `most_tampering`, `remeasured` |
| [P15] | the I-projection onto a linear feasible set | `project_linear` |

## The report as data

`stdalign.report.validate(report)` lists the ways a report, as a dict with the three sections of `STANDARD.md`, breaks
the standard: a field missing, an estimate without its interval, one number for a quantity not identified, or a
confirmatory report whose declaration came after its data. It needs only the standard library. `STANDARD.md`, "The
report as data", gives the forms of an entry; `cases/w1-best-of-n-slope/standard-report.json` and
`examples/quickstart.py` are two reports that keep it.

## What is not here yet

Stakes ([D5], [P9]), the evaluator's results ([P18]–[P20], [P25], [P26], [P29], [P33], [P34]) and feasibility beyond
the projection ([P15]–[P17]) are still computed by helpers inside `checks/` (`ROADMAP.md`, step E1(c)). Outcomes that
are not finite are not covered.
