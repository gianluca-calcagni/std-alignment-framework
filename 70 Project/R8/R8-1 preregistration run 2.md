---
id: "R8-1 preregistration run 2"
type: "report"
updated: "2026-09-27"
---
# R8-1 — pre-registration, run 2 (after D2 stopped run 1; before any run-2 computation)

**Run 1** ([[R8-1 preregistration]]; output `r81_run1_output.txt`) stopped on its registered D2. P1's off-ray bound
`ΔV > 10⁻⁹` failed on one instance, at `ΔV = 8.3·10⁻¹⁰`. P2–P4 held on both SIMD paths.
- **Diagnosis:** that behaviour was nearly on the ray (`M_budget = 2.3·10⁻⁹`), so the threshold had no derived scale.
  This is NOTES §1's failure mode again.
- **Found in the diagnosis:** across all run-1 instances, `ΔV/M_budget = 1/λ`.
- **Proof:** below saturation, `KL(p_{F,λ}‖q) = KL(p̂‖q) = k`, so `M_budget = KL(p̂‖p_{F,λ}) = k − λE_{p̂}F + log Z(λ)`,
  and `0 = k − λE_{p_{F,λ}}F + log Z(λ)`. Subtracting gives **`M_budget = λ·ΔV`**. This is Thm 1 at price `λ`, where
  the two KL terms cancel.

## Revised claim (Prop. 37(a′)), replacing (a)

Below saturation, `ΔV = M_budget/λ` (for `λ > 0`). Hence `ΔV ≥ 0`, with `ΔV = 0` iff `M_budget = 0` iff `p̂ = p_{F,λ}`.
At saturation, `ΔV = max F − E_{p̂}F ≥ 0`. (b), (c) and (d) are unchanged.

**Reading.** The value shortfall is not a new measure. It is the budget measure converted to the units of `F` by the
budget-matched exchange rate. The core carried stakes implicitly all along.

## Check V41, run 2 (seed 4141, same instances). All predictions are verification.

| # | Prediction | Falsified if |
|---|---|---|
| P1′ | `\|ΔV − M_budget/λ\| ≤ 10⁻⁹·max(1, ΔV)` wherever `λ > 10⁻³` and below saturation; `ΔV ≥ −10⁻¹²` everywhere; `ΔV > 0` wherever `M_budget > 10⁻¹²` | any exception |
| P2–P4 | as in run 1 | as in run 1 |

**D1** as in run 1. **D2:** if P1′ fails, R8-1 stops.
