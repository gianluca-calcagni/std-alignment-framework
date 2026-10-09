---
kind: definition
id: D5
aliases: ["D5"]
source: "CORE.md"
---
# D5 — Stakes
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#d5--stakes). Edit the source, not this note.

## Statement
Under the standard specification of a non-constant objective `F`, let `p̂ ∈ Δ` and let `A` be the set of
outcomes where `F` is largest. The **matched intensity** of `p̂` is `λ = inf{t ≥ 0 : KL(p_{F,t}‖q) ≥ KL(p̂‖q)}`, with
`λ = ∞` when the set is empty; the **matched pursuit** is `p_{F,λ}`, with `p_{F,∞} = q(·|A)`. The **shortfall** of `p̂`
is `S(p̂) = E_{p_{F,λ}}[F] − E_{p̂}[F]`, in the units of `F`.

## In plain terms
Stakes ask how much of the objective was actually lost. The actor is compared with the pursuit that
departs from the default by the same amount, and the shortfall is how much more of the objective that pursuit gets, in
the objective's own units.

## Why this choice
- *Misalignment is silent about stakes.* Misalignment does not change when the objective is rescaled
  (`derived/stakes.md`), so it cannot say how much of the objective is lost; a principal needs that in its own units. In
  v7.10 this was learned the hard way (R8-1).
- *Compare at the same departure.* The departure is what the actor spent, and the matched pursuit is the most of `F`
  that departure can buy (`derived/stakes.md`). Comparing with the nearest intended behaviour would say nothing: in the
  second case of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv) it reaches the same average of `F` by construction.
- *Not the best outcome.* Comparing with `max F` would charge every cautious actor for not being reckless, although the
  specification ([[D3 — Specification, declaration and misalignment|D3]]) counts departing from the default as a cost.
- *Defined by an infimum,* so that the definition needs no result: a derived result shows that the departure is matched
  exactly whenever `λ` is finite.

## Lineage
v7.10: Def 22 (the value shortfall `ΔV`), Thm 17(iii) (the same-budget counterfactual), and R8-1.

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits

## Used by
- [[P13 — What the start of a change gains|P13]] — What the start of a change gains
- [[P29 — The width is the exact worst case|P29]] — The width is the exact worst case
