---
id: "T7-2d preregistration"
type: "report"
updated: "2026-09-27"
---
# T7 case 2d — pre-registration: is the default's pull local? (before any bar value is read)

**Why.** [[T7-2b results]] found, post hoc and in both of its companies, that automatic enrollment suppresses the
rates just above the default most. That suggests the default's pull is **local** (a kernel around the default), not
the point mass of B12's family `q_d = (1−α)u + α·1_d`. The PI chose to test it (option (b)), on a paper the PI supplied.

**Rule 13.** It changes a verdict. If the pull is local, B12's constant-ratio prediction holds only for rates outside
the kernel's reach, and the reference family must change. If it is not, the point-mass family stands. **Rule 11:**
labels below.

**Seen before.**
- The paper's table and figure titles, digits masked.
- Figure 3's legend, title and x-axis bin labels.
- Text passages identifying the company and its defaults.
- No bar value and no data label.

**Design parameters, read before registering** (NOTES §1: read what a test depends on first):
- Company A of Beshears, Choi, Laibson & Madrian (NBER w12009) is a chemicals company. It is **fresh**: Choi et al.
  2004's companies are office equipment, health services and food products, and Madrian & Shea's is another firm.
- Figure 3 compares new hires under automatic enrollment at a **3%** default with new hires under a **6%** default
  (15–24 months of tenure). The outcome is the fraction of employees in each bin: 0%, 1–2%, 3%, 4–5%, 6%, 7–10%,
  11–15%.
- **Confound, from the paper's text:** the employer matches 100% up to 6% of pay, so the 6% default coincides with the
  match threshold.

## Data and extraction

Source: w12009 (sha256 `9b46de36…`; supplied by the PI; not committed), Figure 3 (p. 37). Extraction uses the same rule
as [[T7-2c amendment]]:
- bars are the filled rectangles of each legend colour whose bottom edge lies within 3 pixels of the zero line;
- heights are calibrated on the y-axis tick labels;
- bins are assigned by the nearest x-axis label.

**Integrity:** each series sums to 1 within ±0.03, and the tick fit has `R² > 0.999`. **D2:** if either fails, stop and
re-register. Values are committed as `t72d_figure3.csv`. The printed data labels, if any, are reported as a check.

## Quantities

- **Test bins:** those outside both defaults: 0%, 1–2%, 4–5%, 7–10%, 11–15%. Add 0.005 to every fraction; drop a bin
  under 0.01 in both series.
- For each test bin `x`: `ℓ(x) = log(p_6%(x)/p_3%(x))`.
- **Relative proximity:** `r(x) = d₃(x) − d₆(x)`, using bin midpoints (0, 1.5, 4.5, 8.5, 13) and distances to 3 and 6.
  That gives `r` = −3, −3, 0, +3, +3.

## Predictions

| # | Label | Prediction | Falsified if |
|---|---|---|---|
| P1 | **empirical, the local-pull test** | bins nearer the 6% default gain under the 6% regime and bins nearer 3% gain under the 3% regime: Spearman `ρ(ℓ(x), r(x)) > 0.5` over the test bins | `ρ ≤ 0.5` |
| P2 | empirical, the neighbour test | the bin just above 3% (4–5%) is closer to the 6% side than the bin just below it: `ℓ(4–5%) > ℓ(1–2%)` | `≤` |
| P3 | empirical, B12's point-mass family (competing) | the test bins share one ratio: `max_x \|ℓ(x) − mean ℓ\| ≤ log 1.5` | `>` |

**P1/P2 against P3.** The local pull predicts P1 and P2 hold and P3 fails. The point-mass family predicts P3 holds, with
`ρ` near 0. All three are registered; the pattern of results decides.

**Degenerate cases, checked in advance.**
- With 5 test bins, and ties in `r`, Spearman is coarse: a `ρ > 0.5` needs broad agreement.
- The 0% bin is non-participation in both regimes, so it is a legitimate test bin. It may behave differently from the
  rate bins (opting out is a different act), so it is reported separately as well.
- The match threshold at 6% favours 6% and nearby rates under **both** regimes. That cancels in `ℓ` only if it acts
  the same way under both defaults.

**Decision rules.** D1: a failed prediction is recorded; corrected analyses are new and labelled post hoc. D2 as above.
**Falsifier of the local-pull reading:** P1 and P2 both fail.

**Not shown.**
- One company and one tenure window; no standard errors.
- The two cohorts were hired at different times.
