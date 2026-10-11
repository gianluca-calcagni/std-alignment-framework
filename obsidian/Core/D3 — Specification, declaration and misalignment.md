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
**intended behaviours**, closed in `Δ°`. The **misalignment** of a behaviour `p̂ ∈ Δ` is `M(p̂) = inf_{p ∈ 𝓘} KL(p̂‖p)`.
A **family of targets** is a closed set `𝓚` of objectives that contains the constants and `a·G + b·G'` whenever it
contains `G` and `G'`, for all numbers `a, b ≥ 0`; its specification is `(q, 𝓘_𝓚)`, with `𝓘_𝓚 = {tilt(q, G) : G ∈ 𝓚}`,
the pursuits of its targets from `q`. For an objective `F`, the **standard specification** is that of the family
`{t·F + c : t ≥ 0, c real}`, so that `𝓘_𝓚 = R_F`: pursuit of `F` from `q` at every intensity, including none; the
**ordinal specification** is that of the family of non-decreasing functions of `F`, so that
`𝓘_𝓚 = C_F = {p ∈ Δ° : p/q is a non-decreasing function of F}`. A specification is **declared** when it is fixed as [[A5 — Declared before|A5]]
requires: before, and without using, the behaviour it will judge.

## In plain terms
Before looking at what the actor does, the principal states a default behaviour and the set of
behaviours it would accept. Misalignment is how far the actual behaviour is from the nearest acceptable one, in nats:
how fast a record of it builds a case that it is not acceptable. For the request "pursue this objective", two sets are
natural. For an actor that pursues, weighing outcomes by how much better they are, every intensity of pursuing the
objective is acceptable, including none. For an actor that only ranks outcomes, or whose method is unknown, every
behaviour that favours better outcomes at least as much as worse ones, relative to the default, is acceptable. Under
either, an actor that stays at the default is not misaligned, though it may be useless, which is a different failure.

## Interpretation
*Declared.* A specification is the principal's standard, written down and dated before the record it
judges is read ([[A5 — Declared before|A5]]): a default, and the ensembles the principal accepts. A family of targets is the set of aims the
principal accepts being pursued: each at every strength, and every positive mix of them; "pursue `F`" is the smallest
family that holds `F`, and "favour what `F` ranks higher" the family of its order. Misalignment is the rate, in nats per
decision, at which a record's counts become improbable under every accepted behaviour ([[A4 — Misalignment is evidence|A4]]): about `1/M` decisions make
them `e` times less probable. *Verified.* "Misaligned", `M > 0`, is verifiable in the statistical sense, by a test whose
rate of false accusation is bounded at every size of record and whose power tends to one, with no model of how the actor
decides beyond what acceptance asks: an intended actor decides independently, and one that does not may be accused for
that alone (Notes). "Aligned within `ε`", `M < ε`, is verifiable in the same sense for an actor that decides
independently. "Exactly aligned", `M = 0`, can only be refuted: an actor can be shown to be misaligned, or aligned
within a stated margin, never exactly aligned, unless the specification accepts every behaviour. *Justified.* Counts are
what a record supplies ([[A4 — Misalignment is evidence|A4]]); fixing the standard first is what makes the judgement a test ([[A5 — Declared before|A5]]); and the statements
above are verifiable or refutable because of their shape, open or closed in the behaviours, as the statistical form of
reverse physics requires (Notes).

## Why this choice
- *The formula is [[A4 — Misalignment is evidence|A4]] made exact.* If the actor behaves as `p̂` and `p` is intended, each independent decision adds on
  average `KL(p̂‖p)` nats to the log-likelihood ratio in favour of `p̂` over `p`; the least such rate over the intended
  behaviours is `M(p̂)`, including the order of the arguments. Each intended behaviour is also the best trade-off for
  its own objective at a KL price ([[P4 — What KL measures|P4]](ii)), so `M(p̂)` is as well the least net value lost, in nats; for a pursuit
  that is both the steepest climb and the best trade-off ([[D2 — Pursuit of an objective|D2]]), that price is the only one ([[P14 — The cost of departing from the default is forced|P14]]).
- *What the number means.* About `1/M(p̂)` decisions give one nat of evidence that the actor is not behaving as
  intended, odds of about `e` to 1.
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
  intensity, for an actor that weighs outcomes by their values ([[D2 — Pursuit of an objective|D2]], its reasons). It includes doing nothing; a
  principal for whom doing nothing is a failure declares a smaller set (v7.10: the floor, Def 20). The cost of departing
  is what makes it a set of compromises: without it, the only fully intended behaviours would be those on the best
  outcomes of `F`.
- *A family of targets, not one.* A principal often knows its target only up to a family: its order, a span of
  candidate rewards, the objectives of several principals whose weights are not agreed. Declaring the family keeps one
  definition for all of them; the single objective is the smallest family. The family holds the constants, since they
  change no aim ([[B3 — An objective up to scale and constant|B3]]), and positive mixes of its targets, since a principal who accepts each of two targets with
  weights it has not fixed accepts their weighted pursuit; a family that is not convex is the union of the
  specifications of its convex parts, and its misalignment is the least of theirs.
- *Misalignment is excess departure.* Every family credits the actor with what it achieves on the family's targets, and
  `M(p̂)` is the departure spent beyond the cheapest behaviour that does at least as well on every target (Notes). The
  standard specification credits the average of `F`, only when the actor does better than the default; the ordinal one
  credits reaching every threshold of `F` at least as often. What is charged is departure that buys nothing the family
  credits, whether from a wrong goal or from a way of acting that cannot reach the cheapest behaviour.
- *The ordinal specification, for actors that rank.* An actor that picks by rank, such as best-of-`n`, behaves alike
  for every increasing transformation of `F`, and keeps the default's proportions within each level set of `F`. Its
  specification is the order of `F`, which accepts every pursuit of an increasing transformation of `F` and every
  best-of-`n` by `F` (Notes). Under it, misalignment charges only what contradicts the order; the standard
  specification charges, besides, the shape of the reweighting.
- *Both, side by side.* The declaration names the specification that judges. No premise chooses it for the principal: a
  rule that tied the choice to how the actor is declared to act would move a judgement about the actor into the
  standard. A report under the standard specification gives the ordinal misalignment beside it, so that the part charged
  for the shape of the reweighting is visible (Notes; `STANDARD.md`).
- *The actual behaviour may rule outcomes out; the intended ones may not.* A deterministic actor still gets a score.
  Intended behaviours keep full support so that the score is finite.
- *Declared before, not fitted after.* A default or an intended set fitted from the behaviour being judged removes
  exactly the differences the judgement needs. In v7.10, I1-dyn fitted its default (a Hardy–Weinberg expectation) from
  the counts it judged, and its test could not fail.
- *Stakes are reported separately.* Misalignment in nats says nothing about how much of `F` is at stake. Section 5
  reports the shortfall in `F`'s own units (v7.10: Def 22 and R8-1, where this lesson was learned).
- *Slim on purpose.* v7.10's declaration (Def 23, the same object under its old name) had nine slots. Only four changed
  the measure, and all four are ways of generating `𝓘`. Rules, instruments, feasibility and the environment did not
  enter the measure, so they are not part of the specification. Instruments return as interventions (section 6), and
  feasibility as a property of the actor (section 7), where it splits misalignment instead of changing it. The default
  enters the measure through `𝓘` (the pursuit ray starts at `q`), and other definitions use it directly. A slot is added
  only with a case where it changes a verdict, and with the value it takes when nothing is declared.

## Notes
The principal declares; what it declares is the specification, the word AI safety and formal verification use
for the set of acceptable behaviours. Misalignment is then a quantitative distance from the specification. The direction
of KL used here is the one called zero-forcing in variational inference. That the standard specification is a
specification, that is, that the pursuit ray is closed in `Δ°`, is shown in [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv); for a constant `F` the ray is the
single point `q`, which is closed. That the ordinal specification is one, that it contains every best-of-`n` by `F`, and
that its misalignment and the shape's add up to at most the standard one are [[P36 — Ordinal objectives|P36]](i) and (iv). That the nearest
intended behaviour of a pursuer has the least departure among those with the actor's average of `F` is [[P6 — The departure from the default splits into pursuit and misalignment|P6]](ii), and
that, for every family of targets, the specification is closed, its nearest intended behaviour unique, and misalignment
the departure beyond the cheapest behaviour that does at least as well on every target, is [[P53 — Misalignment is the departure beyond what the family of targets credits|P53]]. The test that makes
"misaligned" verifiable at every size, and the interval that makes "aligned within `ε`" verifiable, are [[P55 — What a record of counts certifies, at every size|P55]]; its level
holds for intended behaviours deciding independently, and for independent decisions that drift, but an actor whose
decisions depend on each other may be accused for its dependence alone ([[P55 — What a record of counts certifies, at every size|P55]], Notes); that the statements so verifiable
are the open sets of behaviours, and the refutable ones the closed sets, is Genin and Kelly's theorem [[References|@genin2017]], the
statistical form of the verifiable and refutable statements of reverse physics [[References|@carcassi2021]] ([[P55 — What a record of counts certifies, at every size|P55]], Notes). In
statistics, the standard specification is a one-parameter exponential family and the ordinal one a cone of monotone
likelihood ratios, and misalignment is the divergence from the actual behaviour to either.

## Lineage
v7.10: Def 19 and Prop 34 (the declared intended set), Def 17 (the free convention's half-ray), Def 23 (the
declaration, slimmed; its timing slot becomes the rule of use), row 74, and the target sets of R7-7, cardinal or
ordinal by the principal's declaration. New: behaviours that rule outcomes out are scored. v13: the ordinal
specification moved here from [[P36 — Ordinal objectives|P36]]; misalignment read first as evidence ([[A4 — Misalignment is evidence|A4]]); the draft's rule of a matched
specification (its A6) replaced by the paired report (Q52); families of targets, of which the standard and the ordinal
specification are cases, at the PI's question whether a family is more general than one target (Q53).

## Depends on
- [[B3 — An objective up to scale and constant|B3]] — An objective up to scale and constant
- [[A4 — Misalignment is evidence|A4]] — Misalignment is evidence
- [[A5 — Declared before|A5]] — Declared before
- [[D2 — Pursuit of an objective|D2]] — Pursuit of an objective
- [[P4 — What KL measures|P4]] — What KL measures
- [[P14 — The cost of departing from the default is forced|P14]] — The cost of departing from the default is forced

## Used by
- [[D5 — Stakes|D5]] — Stakes
- [[D7 — Feasibility|D7]] — Feasibility
- [[P35 — Floors and caps|P35]] — Floors and caps
- [[P36 — Ordinal objectives|P36]] — Ordinal objectives
- [[P53 — Misalignment is the departure beyond what the family of targets credits|P53]] — Misalignment is the departure beyond what the family of targets credits
- [[P33 — Error bounds for a known evaluator|P33]] — Error bounds for a known evaluator
- [[P24 — The evaluation gap|P24]] — The evaluation gap
- [[P39 — Several actors: coordination plus individual misalignment|P39]] — Several actors: coordination plus individual misalignment
- [[P40 — Attention: misalignment against ignoring the situation|P40]] — Attention: misalignment against ignoring the situation
- [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]] — Reversibility: the Jensen–Shannon divergence from the reversal
- [[P45 — Drift: what runs share, and what they do not|P45]] — Drift: what runs share, and what they do not
- [[P50 — Tampering: a change of the measurement, not of the world|P50]] — Tampering: a change of the measurement, not of the world
- [[C3 — An error confined to one region costs bounded nats|C3]] — An error confined to one region costs bounded nats
