---
id: "T7-2b preregistration"
type: "report"
updated: "2026-09-27"
---
# T7 case 2b — pre-registration: is the default a floor? (a follow-up of T7-2's post-hoc pattern)

**Why.** [[T7-2 results]] passed B12's structural test, but after the fact its rows showed a pattern in Company B.
Under automatic enrollment, "below default" stayed suppressed relative to "above default", and more so at longer
tenure. That reads as the default acting as a floor (endorsement or anchoring): a failure of exclusion that B12 itself
names. This step tests that pattern **on two companies that played no part in finding it**, choosing the PI's option
(b).

**Rule 13.** It changes a verdict. If the pattern replicates, the default does more than shift the reference: it also
changes what people value below it, and B12's identification is biased there. If it does not replicate, the
reference-shift reading stands. **Rule 11:** labels below.

**Seen before.** The two figures' titles, axis labels and legends, digits masked; the count of numeric tokens and
vector drawings on their pages; no bar value.

## Data (from the PDFs already hashed in [[T7-2 preregistration]])

- **M&S:** Madrian & Shea (2001), NBER w7682, **Figure 4C**, "Distribution of 401(k) Contribution Rates for the WINDOW
  and NEW Cohorts Including Non-Participation". Two series: WINDOW (opt-in; default non-participation) and NEW
  (automatic enrollment at the plan's default rate).
- **CC:** Choi, Laibson, Madrian & Metrick (2004), NBER w8651, **Figure 3C**, Company C, participants only. Two
  series: hired before automatic enrollment, observed before it; and hired after it.
- The default contribution rate of each plan is read from the paper's text or plan table. It is a design parameter,
  not an outcome.

**Extraction rule.**
- Bars are the filled vector rectangles of each legend series. Their heights are converted to fractions by a linear
  fit through the y-axis tick labels; their positions are assigned to the x-axis category labels.
- **Integrity check:** each series sums to 1 within ±0.03, and the tick-label fit has `R² > 0.999`.
- **D2:** if either figure fails, stop and re-register.
- The extracted values are committed as `t72b_figures.csv`.

## Quantities

- `+0.005` is added to every fraction before any logarithm. For each contribution-rate bin `x`,
  `ℓ(x) = log(p_AE(x)/p_noAE(x))`.
- **Non-default bins** are all rate bins other than the default rate. For M&S, non-participation is also excluded,
  because it is the other regime's default. Rate bins with less than 0.01 in both series are dropped.
- `Δ_<` and `Δ_>` are computed as in T7-2, on the pooled bins below and above the default, and `δ = Δ_< − Δ_>`.

## Predictions

| # | Label | Prediction | Falsified if |
|---|---|---|---|
| P1 | **empirical, the replication** | the default acts as a floor: `δ < 0` in **both** M&S and CC | `δ ≥ 0` in either |
| P2 | empirical | the effect is not tiny: `δ < −log 1.25` in at least one of the two | `δ ≥ −log 1.25` in both |
| P3 | **empirical, the finer test** | among non-default bins, the ratio falls with distance *below* the default and not above it: Spearman `ρ(ℓ(x), default − x) < 0` over the bins below the default, pooled over both datasets, with at least 3 such bins | `ρ ≥ 0`, or fewer than 3 bins (then reported as untestable) |

**Reported, not predicted.** Every bin's `ℓ(x)`; T7-2's exclusion statistic `|δ|` against `log 1.5` for each dataset;
the default pull `π_D`.

**Competing reading, stated in advance.** Exclusion alone (B12 unbiased) predicts `δ ≈ 0` and no trend in P3. So P1
and P3 failing together would support B12's clean reading, and T7-2's pattern would count as noise.

**Decision rules.** D1: a failed prediction is recorded; corrected analyses are new and labelled post hoc. D2 as above.

**Not shown.**
- Tenure widening cannot be tested: each figure covers one tenure window.
- The two figures differ in what they condition on (M&S includes non-participants; CC shows participants only). The
  ratio test is valid under both, but the pull `π` is not comparable across them.
- No standard errors are published.
