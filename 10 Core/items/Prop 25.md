---
id: "Prop 25"
type: "proposition"
title: "mechanism-relative comparisons against the contract; tier 1 given the attribution"
section: "Core 09 Observation what an overseer can detect"
order: 54
layer: "explanation"
tier: []
assumes: []
status: "proved"
depends_on: ["Prop 12", "Prop 23", "Def 13", "Def 14"]
mentions: ["Def 8", "Prop 24"]
checks: ["V31", "V32"]
sources: []
aliases: ["Proposition 25", "Prop. 25"]
updated: "2026-09-26"
---
# Prop 25 — mechanism-relative comparisons against the contract; tier 1 given the attribution
<!-- gen:header -->
> [!abstract] Proposition · proved · in [[Core 09 Observation what an overseer can detect]]
<!-- /gen:header -->

## Statement

**Proposition 25 (mechanism-relative comparisons against the contract; tier 1 given the attribution).**
- (a) `M_own` satisfies M1, M2, M6 (whenever `A(F;q,r)` has full support) and M8. It also satisfies the
  mechanism analogue of M5: `M_own = 0` when `p̂ = A(F; q, r)`, i.e. the mechanism pursues the target itself.
- (b) `M_own` satisfies M3 when the model is equivariant under positive affine maps of its objective, with the
  resource transformed accordingly. Argmax selectors are invariant outright.
- (c) **`M_own` violates M4.** It depends on the attributed `(A, r)`, which behaviour does not identify. Under
  the entropic model, `p̂ = p_{F̂,β} = p_{sF̂, β/s}` (Prop. [[Prop 12|12]]), and the two attributions give intended behaviours
  `p_{F,β}` and `p_{F,β/s}`, hence different `M_own`.
- (d) **`R_own` violates M1 and M2.**
  - M1: a selector whose evaluator only reorders behaviours of equal target value has `R_own = 0` with
    `p̂ ≠ A(F; q, r)`.
  - M2: vanilla policy gradient run for the same number of steps on `F̂ = 2F` gains target faster, so
    `R_own < 0`.
  - For argmax selectors on a common candidate set, `0 ≤ R_own` (Prop. [[Prop 23|23]]), so M2 holds there, but M1 still
    fails.
- (e) Detection against the mechanism-relative counterfactual is capped by `M_own`: the Chernoff exponent
  satisfies `C(p̂, A(F; q, r)) ≤ M_own`.

## Proof

*Proof.* (a), (e): properties of `KL`, and the Chernoff bound `C(P,Q) ≤ KL(P‖Q)`. M8: apply per context.
(b): substitution. (c): Prop. [[Prop 12|12]](i) with `s ≠ 1`, and `p_{F,β} ≠ p_{F,β/s}` for non-constant `F`. (d): the
constructions are checked in [[V31]]. ∎

## Notes and checks

*Note (R7-2).* The attribution in (c) includes the actor's reference `q_A` (Def. [[Def 14|14]]). By Prop. [[Prop 12|12]](ii), a
second attribution `(q_A', F̂ − h/β)` gives the same behaviour, but a different intended behaviour
`A(F; q_A', β)` whenever `h` is not constant, and generically a different `M_own`: in [[V32]] it differed in
300 of 300 instances, by a median of 0.26 nats. So `M_own` fails M4
on the reference as well as on the scale.

*Check.* [[V31]]:
- the two attributions of one behaviour give `M_own` = 0.231 and 0.294 nats;
- `R_own = 0` exactly, with a behaviour at KL 0.210 nats from the intended one;
- `R_own < 0` for the policy-gradient pair, in 200 of 200 instances;
- `M_own = 0` for best-of-n on the target at the actor's `n`;
- best-of-n's `M_own` is unchanged under positive affine maps of the target;
- 0 violations of the detection cap in 1,000 instances.

*Reading.* "Did this mechanism, with its resources, do what it would have done on the target?" is a
legitimate **engineering** question, and `M_own` answers it with a detection guarantee. It is not the
**misalignment** question, because its answer depends on how the behaviour is explained. Misalignment stays
the behavioural budget or free measure (Def. [[Def 8|8]], Prop. [[Prop 24|24]]). The price measure is the mechanism-relative
measure for the entropic model with the price as its resource. That is the structural reason it both needs a
unit and fails M5.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 13]] — actor models; R7-1
- [[Def 14]] — mechanism-relative comparison; explanation layer; R7-1
- [[Prop 12]] — what behaviour identifies
- [[Prop 23]] — argmax selectors on a common candidate set — tier 2′, v6.4

## Used by
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*

## Mentions
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Prop 24]] — the v6.4 measures against the contract; tier 1

## Mentioned in
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Def 11]] — the misalignment contract; R7-0
- [[Prop 18]] — harm bounds detectability

## Checks
- [[V31]]
- [[V32]]

## Sources
- none

## Retractions touching this note
- [[R075]]
<!-- /gen:links -->
