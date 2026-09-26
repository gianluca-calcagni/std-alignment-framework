---
id: "Core 11 What the core forbids"
type: "section"
part: "core"
order: 14
updated: "2026-09-26"
---
## 11. What the core forbids

Each item is a statement the core entails, whose negation it rules out, with the result it rests on.

1. **No capacity-free ranking of errors**, and no separable bound on worst-case regret with bounded
   looseness (Thm [[Thm 9|9]]). *Testable:* two evaluator errors with `Var_q(E₁) > Var_q(E₂)` but `osc(E₁) < osc(E₂)`
   have crossing gold-versus-capacity curves ([[C08|C8]]). With matched variances the curves tie
   to leading order at small capacity and separate at large capacity; they need not cross. The crossing
   was found for every optimizer tested (R5, R6), but **where** it falls is optimizer-specific: at KL 0.026
   for vanilla policy gradient, 0.54 for Gibbs, 4.7 for best-of-n.
2. **KL-limited optimization does not bound exposure to errors with sub-exponential tails, at any budget**;
   χ²-limited optimization does, if the variance is finite (Prop. [[Prop 11|11]]).
3. **For the entropic actor, an error confined to one region has bounded cost in nats**, whatever its size
   (Prop. [[Prop 4|4]], under (E)).
4. **For the entropic actor, rescaling the target produces zero transverse error** (under (E)). It costs exactly the axial error of Cor. [[Cor 13.3|13.3]]
   under the price convention, and nothing under the budget or free conventions (Remark [[Rem 13.5|13.5]]).
5. **For the entropic actor (E), the initial effect of optimization has the sign of `Cov_q(F̂, F)`**, and its
   terminal effect is set by argmax agreement (Prop. [[Prop 14|14]]). For any other smooth optimizer, the initial sign is
   the covariance in that optimizer's own geometry (Prop. [[Prop 22|22]]). A vanilla gradient can have the opposite
   sign.
6. **For jointly Gaussian intent and evaluator under the reference, the Gibbs path never overoptimizes**:
   gold gain is exactly linear in `d = √KL`, with slope `√2·ρ_q(F,F̂)·sd_q(F)` ([[B04|B §4]]).
   Overoptimization requires non-Gaussian joint structure. This is the KL-tilt counterpart of El-Mhamdi &
   Hoang (2024): Gaussian discrepancies give only a weak Goodhart effect under selection. **Tier 1 (Prop. [[Prop 21|21]]):**
   under any affine regression of target on evaluator, no optimizer whose weights depend only on the
   evaluator overoptimizes.
7. **No test on behaviour detects a departure from the intended behaviour with an error exponent above
   `β·R_J`** (Prop. [[Prop 18|18]]). This holds for any actual actor, measured against the Gibbs intended actor at a
   declared price (tier 1). `β·R_J` is the price-convention *regret*. The budget-convention misalignment caps
   detection against the budget-matched counterfactual in the same way (Chernoff ≤ KL).
8. **Deployment harm exceeds the achievable detection exponent by at least the evaluation gap `Γ`**
   (Prop. [[Prop 19|19]]).
9. **Price and budget conventions disagree.** They rank errors differently in a positive fraction of cases
   (11.4 % on the [[V14]] generator, Thm [[Thm 17|17]]), so any claim "error `A` is worse than error `B`" must name its
   convention.

