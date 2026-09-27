---
id: "R7-9 preregistration"
type: "report"
updated: "2026-09-27"
---
# R7-9 — pre-registration: the core as a declared intended set (written before any R7-9 computation)

**Rule 13.** Runs under the structural exception (the PI, after v7.5). No verdict changes by design. The falsifiable
claim is structural: the projection's good properties come from log-convexity of the declared set.
**Rule 11.** Every prediction below is *verification* (it checks a proof); none is empirical.

## Definitions under test (measurement layer)

**Def. 19 (declared intended set).** A **declaration** fixes a set `𝓘 ⊆ Δ°`, closed in `Δ°`, of intended behaviours;
the misalignment of a full-support `p̂` is `M_𝓘(p̂) = inf_{p ∈ 𝓘} KL(p̂‖p)`, undefined when `𝓘` is empty. `𝓘` is
**log-convex** if for all `p₀, p₁ ∈ 𝓘` and `λ ∈ [0,1]` the geometric mixture `p_λ ∝ p₀^{1−λ} p₁^λ` is in `𝓘`.

## Claimed results (Prop. 34)

- (a) **Reduction.** Def. 10's free and budget measures, Def. 17's target-set measures and Def. 18's capped measures
  are `M_𝓘` for the intended sets they define.
- (b) **The contract as conditions on `𝓘`.** M1 holds iff `𝓘` is closed in `Δ°` (the infimum is then attained); M2, M4
  and M6 hold for every `𝓘`; M3 holds iff `𝓘` depends on the target only through the declared set; M5 holds iff `𝓘`
  contains the declared pursuit family; M8 holds per context.
- (c) **Log-convex sets.** If `𝓘` is log-convex and closed in `Δ°`, the minimizer `p°` is unique and, for every `p ∈ 𝓘`,
  `KL(p̂‖p) ≥ M_𝓘(p̂) + KL(p°‖p)`, with equality when `𝓘` contains the geometric line through `p°` and `p` beyond
  `p°`. Proof: along the geometric mixture, `KL(p̂‖p_λ) = (1−λ)KL(p̂‖p₀) + λKL(p̂‖p₁) + log Σ p₀^{1−λ}p₁^λ`, a convex
  function of `λ` (Csiszár–Matúš 2003 for the literature).
- (d) **Instances.** The intent half-ray, the capped segment and the ordinal cone are log-convex; Thm 13(a),
  Prop. 32(c) and Prop. 33(b) are cases of (c). The budget intended sets are not log-convex in general.

## Check V37 (seeded), and predictions — all verification

Instances: `n` uniform on `{3, …, 10}`, `q` Dirichlet(1) with minimum ≥ `10⁻³`, random full-support `p̂`.
**Generic log-convex hulls:** `𝓘 = {p ∝ exp(Σ_k w_k ℓ_k) : w in the simplex}` for `K ∈ {2, 3, 5}` random log-densities
`ℓ_k`; `M_𝓘` computed by convex minimization over `w`.

| # | Claim | Prediction | Falsified if |
|---|---|---|---|
| P1 | (c), uniqueness | on 400 generic hulls, the minimizer from 5 random starts agrees | any pair of end points more than `10⁻⁶` apart (optimizer-bound) |
| P2 | (c), Pythagoras | for 20 random members `p` of each hull, `KL(p̂‖p) − M_𝓘 − KL(p°‖p) ≥ −10⁻⁸` | any violation |
| P3 | (a), (d) | the generic hull code on the two-point hull `{q, p_{F,s}}` reproduces `M_free^cap` (Prop. 33(a)); on the conic hull of the level steps `1{F ≥ v_j}` (non-negative weights, free constant) it reproduces `M_ord` (Prop. 32(b)) | a difference above `10⁻⁸` |
| P4 | (d), the budget set | on 200 instances of the cardinal budget sphere intersected with a two-point hull `{q, p_{G,s}}` of an unrelated `G`, reported without prediction: how often 5 starts disagree | — (exploratory) |

**Decision rules.** D1: a failed proof check means the statement is wrong; recorded; a corrected statement is new.
D2: if the reduction (a) fails for any existing measure, R7-9 stops and Def. 11 stays as it is.
**Falsifier of the structural claim:** a load-bearing decomposition of the core that is not an instance of (c).
