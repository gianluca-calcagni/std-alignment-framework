---
id: "R7-10 preregistration"
type: "report"
updated: "2026-09-27"
---
# R7-10 — pre-registration: declared resolution (written before any R7-10 computation)

Merges the "split inside cells" candidate (ROADMAP §6 G1, G4) with R7-8 (resolution): both are a declared partition
of `X`. Approved by the PI after v7.7, together with §4b; this is the last core step before T7.

**Rule 13.** Passes, with three examples.
- *Style free, free convention.* `X = {wrong, right} × {style A, style B}`, `F` = correctness. An agent that pursues
  correctness exactly as `p_{F,t}` but answers in style B is charged `W`, the divergence inside the cells, though the
  principal declared style irrelevant.
- *Style drift, budget convention.* The same agent is also charged an overshoot: the information it spends on style is
  read as pursuit of `F`. In the go/no-go probe (4 outcomes, true `t = 1`), the budget-matched intensity was 2.62 and
  the excess over `W` was 0.19 nats. This misreads the diagnosis even for a principal who does care about style.
- *Deterministic control on a continuous `X`* (R7-5 case 5): every divergence saturates; a declared resolution
  keeps the measure finite.

**Rule 11:** every prediction is *verification*. **Seen before:** only the go/no-go probe above (one instance, not
committed).

## Definitions under test (measurement layer)

**Def. 21 (declared resolution).** A **resolution** is a partition `𝒢 = {C_1, …, C_m}` of `X` into non-empty cells.
Every member of the declared target set is constant on each cell (the declared resolution keeps every distinction
the target makes). Write `p_𝒢` for the cell masses of `p`, and the **coarse instance** for `(𝒢, q_𝒢, 𝒯_𝒢, κ, floor, cap)`.
- The **measure at resolution 𝒢** is `M^𝒢(p̂) = M(p̂_𝒢)`, the declared measure of the coarse instance. Under the budget
  convention its budget is `k_𝒢 = KL(p̂_𝒢‖q_𝒢)`.
- Its **intended set** is the preimage `{p ∈ Δ° : p_𝒢 intended in the coarse instance}`: inside a cell, every split is
  intended.
- **Default:** the finest partition, which is the current core. **Elicitation:** "Which differences between behaviours
  matter to you at all?"
- The **within-cell divergence** is `W = Σ_C p̂(C)·KL(p̂(·|C)‖q(·|C)) = KL(p̂‖q) − KL(p̂_𝒢‖q_𝒢)`.

## Claimed results (Prop. 36)

- (a) **Reduction.** `M^𝒢(p̂) = inf over the intended preimage of KL(p̂‖p)`, attained with `p(·|C) = p̂(·|C)`. So `M^𝒢`
  is a declared-intended-set measure (Def. 19).
- (b) **Free-type measures split exactly.** For the free measure of Def. 10, the capped free measure (Def. 18), the
  segment free measure (Def. 20) and the ordinal measure `M_ord` (Def. 17), with the target constant on cells:
  `M = M^𝒢 + W`.
- (c) **The budget convention misattributes.** For Def. 10's budget measure, where both are defined:
  `M_budget = M_budget^𝒢 + W + E`, with `E ≥ 0`, and `E > 0` iff `W > 0`. The budget-matched intensity at the finest
  partition exceeds the one at `𝒢` whenever `W > 0`. Along a path that raises `W` with the cell masses fixed, `E` is
  non-decreasing. Where `W` pushes `KL(p̂‖q)` past `log 1/q(argmax F)`, the finest budget measure is undefined while
  `M_budget^𝒢` is defined.
- (d) **Declared blind spot.** `M^𝒢(p̂′) = M^𝒢(p̂)` whenever `p̂′_𝒢 = p̂_𝒢`: exploitation inside a cell is invisible
  at resolution `𝒢`. `M^𝒢 ≤ M` for the five measures in (b) and (c).
- (e) **Saturation.** Splitting each cell into `n` sub-outcomes with `q` uniform inside, a behaviour concentrating
  each cell on one sub-outcome has a free measure that grows without bound in `n`, while `M^𝒢` stays fixed.

## Check V40 (seed 4010), and predictions — all verification

600 instances: `m` in `{2, …, 6}` cells, each of size 1–4; `q` Dirichlet(1) with minimum ≥ `10⁻³`; `F ~ N(0, I)` on
cells; a random cap `s` and floor `0 < r < s`. Behaviours, 200 each: random full-support; **style drift** (cell masses
of `p_{F,t}`, random `t` in the segment, random splits inside cells); on-ray at the finest partition (`W = 0`).

| # | Claim | Prediction | Falsified if |
|---|---|---|---|
| P1 | (a) | a generic minimizer over the intended preimage (free, full ray; 4 starts) never beats `M^𝒢` by more than `10⁻⁹`, and matches it within `10⁻⁶` | beyond either threshold |
| P2 | (b) | `M = M^𝒢 + W` for all four free-type measures | above `10⁻⁹` |
| P3 | (c) | where both are defined: `M_budget − M_budget^𝒢 − W − E` within `±10⁻⁹` with `E` from the two budget points; `E > 10⁻¹²` whenever `W > 10⁻⁸`; the finest-partition intensity exceeds the coarse one; along 20 steps of a geometric path from `q(·\|C)` to a random split, `E` never decreases by more than `10⁻¹²` | any exception |
| P4 | (d) | resampling the splits inside cells changes `M^𝒢` by at most `10⁻¹²`; `M^𝒢 ≤ M + 10⁻¹⁰` for the five measures; style-drift behaviours score `M^𝒢 ≤ 10⁻¹⁰` on the free and segment measures, while their finest measure exceeds `10⁻⁹` whenever `W > 10⁻⁹` | any exception |
| P5 | (e) | with `n = 2, 4, …, 2¹⁶` and mass `1 − 10⁻⁶` on one sub-outcome per cell, the finest free measure increases strictly in `n` and exceeds `M^𝒢 + 10` at `n = 2¹⁶`; `M^𝒢` is constant to `10⁻¹²` | any exception |

The count of instances where the finest budget measure is undefined and `M_budget^𝒢` is defined is reported, not
predicted.

**Decision rules.** D1: a failed prediction is recorded; a corrected statement is new. D2: if P2 fails beyond its
threshold on an instance where it is not an optimizer or root-finding artefact, R7-10 stops. D3: if P3's sign claim
fails, the misattribution claim (c) is withdrawn and the budget reading is left as it is. **Falsifier of the purpose:**
a style-drift agent charged under a declared resolution, or a change inside cells moving `M^𝒢`.

**Not claimed.** Continuous `X` is outside the finite core; (e) illustrates R7-8's case by finite refinement only. No
claim is made for the capped, segment or ordinal *budget* measures under a resolution.
