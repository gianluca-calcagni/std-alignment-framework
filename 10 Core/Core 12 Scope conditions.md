---
id: "Core 12 Scope conditions"
type: "section"
part: "core"
order: 15
updated: "2026-09-26"
---
## 12. Scope conditions

- **Finite `X`**, except Prop. [[Prop 11|11]] and [[Dictionary index|Dictionary]] Prop. [[B04|B4]]. The proofs extend to general spaces under exponential integrability of
  `F`, `F̂`, and `E` in a neighbourhood of `[0, β]`.
- **Actor.** See the assumption tiers at the top of this file. Tier-1 results hold for any actual actor.
  Tier 2 holds for exact maximizers, tier 2′ for argmax selectors compared at equal budget. **The gauge is actor-specific.** For the entropic actor, behaviour identifies the evaluator up
  to positive affine maps and a reference shift (Prop. [[Prop 16|16]]). For best-of-n it identifies only the evaluator's
  ordering: any strictly increasing transform leaves behaviour unchanged ([[V26]]). Identification statements
  must name the actor class. The independent review's tests of which tier-4 predictions transfer to other
  optimizers are summarized in [[C07|C7]]. The exponential form enters in two ways. Thms [[Thm 1|1]], [[Thm 13|13]] and [[Thm 17|17]] and the cap
  in Prop. [[Prop 18|18]] use it for the **intended** actor only, so they hold for any actual actor (tier 1). Props [[Prop 2|2]]–[[Prop 4|4]],
  Prop. [[Prop 14|14]](ii)–(iii) and Cors [[Cor 1.1|1.1]]–[[Cor 1.5|1.5]] use it for the actual actor too, under (E). Prop. [[Prop 15|15]] extends the
  identity to an intended actor that exactly maximizes a concave target minus a convex regularizer. Best-of-n,
  quantilizers and gradient-trained policies that do not reach the regularized optimum are covered as actual
  actors by the tier-1 results, and best-of-n compared at equal `n` by Prop. [[Prop 23|23]] (tier 2′). The tier-2 and
  tier-4 results do not cover them. Theorem [[Thm 5|5]](i) needs only that the actor maximizes its objective over a set
  containing the intended actor.
- **Other agents.** Only exact potential games under log-linear learning ([[B13|B §13]]). General
  games, collusion and arms races are the largest missing layer ([[T1_census_routing]]).
- **Target.** A single target, linear except in Prop. [[Prop 15|15]]. Sets of targets (aggregation, disagreement,
  multiple selves) are not formalized ([[R3_FIX_LOG]]). The target is **cardinal**: the budget and free measures
  charge the shape of a pursuit as well as its direction, so best-of-n or a quantilizer run on the true target
  scores as misaligned ([[R7-5 go-no-go]]). The ordinal target is [[ROADMAP]] R7-7.
- **Observation.** i.i.d. behavioural samples, optionally with exogenous contexts (§9). No data layer for
  the evaluator; no adaptive or strategic observation.
- **Static, with one exception.** The explanation layer's hypothesis (E_R) carries one stationary dynamic
  element, the continuation value (Prop. [[Prop 27|27]](b)). Otherwise there are no dynamics, and contexts (§9) are the
  only structure beyond one-shot behaviour. `X` may be a set of trajectories. KL between trajectory distributions with shared dynamics
  equals the expected sum of per-step action-distribution KLs (chain rule); divergences between occupancy
  measures are different objects.
- **Exogenous frame and existing intent.** `q`, `β`, `F` fixed and not functions of `p`; a single `F`
  exists. See [[Boundary 03 The boundary as two conditions|Boundary §3]].
