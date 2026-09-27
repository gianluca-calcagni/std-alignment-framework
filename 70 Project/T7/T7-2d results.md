---
id: "T7-2d results"
type: "report"
updated: "2026-09-27"
---
# T7 case 2d — results: is the default's pull local? Two defaults in one company

Pre-registered in [[T7-2d preregistration]] (sha256 `13707f14…`, commit `47c5b7a`) before any bar value was read.
Data: Beshears, Choi, Laibson & Madrian (NBER w12009), Figure 3, Company A, a chemicals company not used before. It
compares new hires under a 3% automatic-enrollment default with new hires under a 6% one. Script `t72d_run.py`;
output `t72d_output.txt`; values `t72d_figure3.csv`. Integrity: series sums 0.999 and 1.000; tick fit
`R² = 0.999999`.

## Predictions

| # | Label | Result | Verdict |
|---|---|---|---|
| P1 | empirical, local pull | Spearman `ρ(ℓ, r)` = **−0.791** over 5 bins (predicted > 0.5) | **fails, in the opposite direction** |
| P2 | empirical, neighbour | `ℓ(4–5%)` = −0.27 against `ℓ(1–2%)` = +1.83 (predicted the reverse) | **fails** |
| P3 | empirical, B12's point mass | max `\|ℓ − mean\|` = **1.51** against `log 1.5` = 0.41 | **fails** |

| Bin | 0% | 1–2% | 3% | 4–5% | 6% | 7–10% | 11–15% |
|---|---|---|---|---|---|---|---|
| 3% default | 0.042 | 0.006 | 0.275 | 0.030 | 0.239 | 0.179 | 0.227 |
| 6% default | 0.085 | 0.064 | 0.042 | 0.022 | 0.489 | 0.170 | 0.127 |
| `ℓ = log(p₆/p₃)` | +0.65 | **+1.83** | — | −0.27 | — | −0.05 | −0.56 |

## What it shows

- **Both reference families fail on the cleanest test available.** Both regimes are automatic enrollment, so neither
  default is non-participation, and every rate outside {3%, 6%} is a test bin. B12's point-mass family predicts one
  common ratio; the ratios span 2.4 nats. The local-pull hypothesis from [[T7-2b results]] predicts the opposite of
  what happened.
- **What happened instead: a higher default pushes some people down.** Under the 6% default, the share at 1–2% rises
  tenfold (0.6% → 6.4%) and non-participation doubles (4.2% → 8.5%). The shares above 6% fall. That is a
  direction-dependent response. Employees for whom the default is too high opt out downward, and a reweighting of one
  fixed evaluator cannot produce it.
- **So exclusion fails here, clearly.** The default changes what people choose away from it, not just where they start.
  B12's identification of the reference relies on exclusion, so it would be biased on this company. B12 itself names
  this failure; this is the case where it is large.

## Caveats

- **The match confound.** The employer matches 100% up to 6%, so the 6% default coincides with the match kink. Under
  the 3% default, 24% of new hires move to exactly 6%.
- The two cohorts were hired at different times.
- One tenure window; no standard errors.

## Verdict for T7 case 2 (with 2b, 2d)

| Company | B12's constant-ratio structure | Source |
|---|---|---|
| Choi et al. 2004 A | holds loosely | [[T7-2 results]] |
| Choi et al. 2004 B | holds loosely, with a post-hoc drift | [[T7-2 results]] |
| Madrian & Shea | holds (`\|δ\|` 0.27) | [[T7-2b results]] |
| Choi et al. 2004 C | fails (on a 1–2-point cell) | [[T7-2b results]] |
| Beshears et al. A (two defaults) | **fails clearly** (spread 1.51 nats) | this note |

The framework's human actor is a logit with a default-dependent reference and a fixed evaluator. **It holds roughly when
one regime is opt-in, and it fails when two participation defaults are compared**, which is the cleanest test. Both
post-hoc patterns (the floor, the local pull) failed when registered.

**The diagnostic value is real, and negative.** The framework's structure made a sharp prediction that the data
rejected, and it located the rejection: the default moves the evaluator (downward opt-outs from a high default). A
model with direction-dependent deviation costs, or a default that enters the evaluator, is what B12 would need. That
is an explanation-layer change, recorded for the PI, not made here.
