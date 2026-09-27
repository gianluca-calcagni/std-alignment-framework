---
id: "T7-1b preregistration"
type: "report"
updated: "2026-09-27"
---
# T7 case 1b — pre-registration: RLHF length bias, improved design with an external target

Repeats [[T7-1 preregistration]] at the PI's request ("we can do better"), fixing the weaknesses recorded in
[[T7-1 results]]. Written before any Arena Elo value is read. **Seen before:** everything T7-1 computed (its
results are known), the column names of `notebooks/benchmarks.csv`, and the 56 model names in it (40 match an
AlpacaEval 2 model exactly after normalization). **Rule 11:** labels below.

## What changes, and why

| T7-1 weakness | T7-1b fix |
|---|---|
| the target was the judge's verdict (circular) | an **external target**: Chatbot Arena Elo, human pairwise preferences, the ranking the length-controlled paper validated against |
| length as a yes/no relation to the reference answer | **length magnitude**: quartile bins of the answer's character count, cut on the pooled field |
| a two-cell coarse space made the off-ray term degenerate | a **three-level verdict** (lose, unsure, win), so the ray does not cover the space; checked below |
| unsigned `W` against a signed question | `sW` = `W` with the sign of the model's mean length shift relative to `q` |
| no baseline | the framework's term must beat **raw average length** at explaining the judge's departure |

## Source (pinned)

`tatsu-lab/alpaca_eval` at `cd543a149df89434d8a54582c0151c0b945c3d20`: the T7-1 files, plus `notebooks/benchmarks.csv`
(column `Arena Elo [April 18, 2024]`; `Model`).

## Instance

- **Models:** the 216 used in T7-1 (same integrity check). **Matched set:** those whose `Model` in `benchmarks.csv`
  equals the AlpacaEval name after lowercasing and removing non-alphanumerics, with a non-empty April Elo. No manual
  matches.
- **Outcomes:** `X = {lose, unsure, win} × {L1, L2, L3, L4}`. The verdict of an instruction is `v = preference − 1`:
  lose if `v < 1/3`, win if `v > 2/3`, unsure otherwise. `L1–L4` are the quartiles of the model's answer length
  (characters), with cut-points from all answers of the 216 models. Counts plus `0.5` per cell.
- **Reference `q`:** the pooled behaviour of the 216 models (declared).
- **Target:** `F = (0, ½, 1)` on the verdict; cardinal set. **Resolutions:** finest, and `𝒢` = the verdict.
- **Quantities:** `W_m`, the off-ray term, the intensity term, `Θ_m` (Prop. 36); `sW_m = W_m · sign(mean length bin of
  p̂_m − that of q)`; `D_m = |win_rate − LC win_rate|`; **judge departure** `J_m = rank(win_rate) − rank(Elo)` within the
  matched set (positive: the judge ranks the model above where humans do).

**Design check (before any prediction is read):** the off-ray term exceeds `10⁻⁶` for at least 25 % of the 216 models.
If not, the coarse space is still degenerate and P1's three-term reading is flagged as uninformative.

## Predictions

| # | Label | Prediction | Falsified if |
|---|---|---|---|
| P1 | verification | `M_free = W + off-ray + intensity`, to `10⁻¹²`, for all 216 | any exception |
| P2 | verification | `Θ_m > 0` wherever `W_m > 10⁻⁹` and both budget measures are defined | any exception |
| P3 | empirical | internal, repeating T7-1's failed P3 with the new design: Spearman `ρ(W, D) > 0.3` over the 216 | `ρ ≤ 0.3` |
| P4 | **empirical, the key test** | the framework's length term explains where the judge departs from humans: Spearman `ρ(sW, J) > 0.3` over the matched set | `ρ ≤ 0.3` |
| P5 | empirical | it does so better than raw length: `ρ(sW, J) > ρ(avg_length, J)` over the matched set | `ρ(sW, J) ≤ ρ(avg_length, J)` |

**Reported, not predicted:** the size of the matched set; `ρ(D, J)` (the published correction's own agreement with the
same question); `ρ(win_rate, Elo)` and `ρ(LC, Elo)`; the diagnosis table for the five largest and five smallest `J`.

**Power.** With about 35–40 matched models, `ρ = 0.3` is at the edge of significance (two-sided `p ≈ 0.07`). A pass is
weak evidence; a fail with `ρ` near 0 is informative.

**Decision rules.** D1: a failed prediction is recorded; corrected analyses are new and labelled post hoc. D2: if the
matched set has fewer than 25 models, P4 and P5 are not evaluated. **Falsifier of the purpose:** P4 fails with
`ρ ≤ 0.1` — the framework's style term does not explain the judge's departure from human preference at all.

## Still not shown

Arena Elo carries its own length preference (human raters also favour longer answers), so `J` measures the judge's
length bias *in excess of* humans'. `q` is still a declaration. Instructions differ between the two benchmarks.
