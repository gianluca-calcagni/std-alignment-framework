---
kind: definition
id: D3
aliases: ["D3"]
source: "CORE.md"
---
# D3 — Specification, declaration and misalignment
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#d3--specification-declaration-and-misalignment). Edit the source, not this note.

## Statement
A **specification** is a pair `(q, 𝓘)`: a default `q ∈ Δ°`, and a non-empty set `𝓘 ⊆ Δ°` of
**intended behaviours**, closed in `Δ°`. The **misalignment** of a behaviour `p̂ ∈ Δ` is
`M(p̂) = inf_{p ∈ 𝓘} KL(p̂‖p)`. The **standard specification** of an objective `F` is `(q, R_F)`: pursuit of `F` from
`q` at every intensity, including none.
A specification is **declared** when it is fixed as [[A5 — Declared before|A5]] requires: before, and without using, the behaviour it will
judge.

## In plain terms
Before looking at what the actor does, the principal states a default behaviour and the set of
behaviours it would accept. Misalignment is how far the actual behaviour is from the nearest acceptable one, in nats.
When the request is "pursue this objective", every intensity of pursuing it is acceptable, including none: an actor
that stays at the default is not misaligned, though it may be useless, which is a different failure.

## Why this choice
- *The formula is forced.* By [[A3 — Pursuit is the best trade-off|A3]], pursuit is the best trade-off between an objective and a cost of departing from
  the default, and by [[P14 — The cost of departing from the default is forced|P14]] that cost can only be KL. Each intended behaviour `p` is then the best trade-off for its own
  objective, `log(p/q)` at intensity 1 ([[P4 — What KL measures|P4]](ii)), and `KL(p̂‖p)` is exactly the net value, in nats, that `p̂` loses
  against it. [[A4 — Misalignment is value lost|A4]] takes the least such loss over the acceptable behaviours: that is `M(p̂)`, including the order of
  the arguments. The cost term is
  what makes the reading general: without it, the only fully intended behaviours of an objective would be those on its
  best outcomes, and every behaviour that puts any mass elsewhere would be charged.
- *What the number means.* If the actor behaves as `p̂` and `p` is intended, each independent decision adds on average
  `KL(p̂‖p)` nats to the log-likelihood ratio in favour of `p̂` over `p`. So `M(p̂)` is the slowest rate at which an
  observer gathers evidence that the actor is not behaving as intended: about `1/M(p̂)` decisions give one nat, odds of
  about `e` to 1.
- *The direction charges the unintended.* `KL(p̂‖p)` is large when the actor often does what `p` rarely does, and
  comparatively small when the actor merely does less of what `p` does. Doing the unintended costs more than leaving the
  intended undone.
- *The nearest acceptable behaviour.* Taking the minimum gives the actor the benefit of the doubt: it is charged only
  for what no acceptable behaviour explains.
- *Grouping only hides.* By [[P4 — What KL measures|P4]](iii) and (iv), the score splits along groupings of outcomes, and grouping can only hide
  misalignment. Section 4 uses this for resolutions.
- *A set, not a point.* A principal who asks for `F` without naming an intensity would otherwise charge the actor for an
  intensity it never asked about (v7.10: row 74, the price measure is a regret, not misalignment). A single intended
  behaviour is the case `𝓘 = {p*}`.
- *The standard specification is the pursuit ray,* because "pursue `F`" states a fixed objective ([[D2 — Pursuit of an objective|D2]]) at an unstated
  intensity. It includes doing nothing. A principal for whom doing nothing is a failure declares a smaller set (v7.10:
  the floor, Def 20).
- *The actual behaviour may rule outcomes out; the intended ones may not.* A deterministic actor still gets a score.
  Intended behaviours keep full support so that the score is finite.
- *Declared before, not fitted after.* A default or an intended set fitted from the behaviour being judged removes
  exactly the differences the judgement needs. In v7.10, I1-dyn fitted its default (a Hardy–Weinberg expectation) from
  the counts it judged, and its test could not fail.
- *Stakes are reported separately.* Misalignment in nats says nothing about how much of `F` is at stake. Section 5
  reports the shortfall in `F`'s own units (v7.10: Def 22 and R8-1, where this lesson was learned).
- *Slim on purpose.* v7.10's declaration (Def 23, the same object under its old name) had nine slots. Only four changed
  the measure, and all four are ways of
  generating `𝓘`. Rules, instruments, feasibility and the environment did not enter the measure, so they are not
  part of the specification. Instruments return as interventions (section 6), and feasibility as a property of the
  actor (section 7), where it splits misalignment instead of changing it. The default enters the measure through `𝓘`
  (the pursuit ray starts at `q`), and other definitions use it directly. A slot is added only with a case where it
  changes a verdict, and with the value it takes when nothing is declared.

## Notes
The principal declares; what it declares is the specification, the word AI safety and formal verification use
for the set of acceptable behaviours. Misalignment is then a quantitative distance from the specification. The direction
of KL used here is the one called zero-forcing in variational inference. That the standard specification is a
specification, that is, that the pursuit ray is closed in `Δ°`, is shown in [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv); for a constant `F` the ray is the
single point `q`, which is closed.

## Lineage
v7.10: Def 19 and Prop 34 (the declared intended set), Def 17 (the free convention's half-ray), Def 23 (the
declaration, slimmed; its timing slot becomes the rule of use), and row 74. New: behaviours that rule outcomes out are
scored.

## Depends on
- [[A3 — Pursuit is the best trade-off|A3]] — Pursuit is the best trade-off
- [[A4 — Misalignment is value lost|A4]] — Misalignment is value lost
- [[A5 — Declared before|A5]] — Declared before
- [[D2 — Pursuit of an objective|D2]] — Pursuit of an objective
- [[P4 — What KL measures|P4]] — What KL measures
- [[P14 — The cost of departing from the default is forced|P14]] — The cost of departing from the default is forced

## Used by
- [[D5 — Stakes|D5]] — Stakes
- [[D7 — Feasibility|D7]] — Feasibility
- [[P35 — Floors and caps|P35]] — Floors and caps
- [[P36 — Ordinal objectives|P36]] — Ordinal objectives
- [[P33 — Error bounds for a known evaluator|P33]] — Error bounds for a known evaluator
- [[P24 — The evaluation gap|P24]] — The evaluation gap
- [[P39 — Several actors: coordination plus individual misalignment|P39]] — Several actors: coordination plus individual misalignment
- [[P40 — Attention: misalignment against ignoring the situation|P40]] — Attention: misalignment against ignoring the situation
- [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]] — Reversibility: the Jensen–Shannon divergence from the reversal
- [[C3 — An error confined to one region costs bounded nats|C3]] — An error confined to one region costs bounded nats
