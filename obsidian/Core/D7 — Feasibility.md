---
kind: definition
id: D7
aliases: ["D7"]
source: "CORE.md"
---
# D7 — Feasibility
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#d7--feasibility). Edit the source, not this note.

## Statement
The actor's **feasible set** is a non-empty closed set `𝓕 ⊆ Δ`: the behaviours it can produce. It is
**linear** if it is the set of behaviours whose averages of given functions take given values,
`𝓕 = {p ∈ Δ : E_p[f_i] = a_i for i = 1, …, m}`, for functions `f_i : X → ℝ` and numbers `a_i`. When nothing is known
about what the actor can do, `𝓕 = Δ`.

## In plain terms
The feasible set is what the actor can do. It is linear when the actor's limits take the form "these
averages cannot change": how often each situation arises, how the actor splits outcomes it cannot tell apart, how the
environment responds to what the actor does.

## Why this choice
- *It separates "cannot" from "will not".* Misalignment ([[D3 — Specification, declaration and misalignment|D3]]) judges what the actor did; the feasible set says what it
  could have done. Without it, an actor is charged alike for what it chose and for what no behaviour in its reach could
  avoid.
- *Linear limits are the natural class.* Three limits met in practice are linear: situations whose frequencies the actor
  does not choose (fixed masses of groups of outcomes), outcomes the actor cannot tell apart ([[D4 — Resolution|D4]]: fixed ratios inside
  cells), and acting in an environment whose responses are fixed (fixed transition probabilities). For linear limits the
  split of misalignment into an avoidable and an unavoidable part is exact, and it is at once Csiszár's Pythagorean
  theorem and an exact accounting of net value (`derived/feasibility.md`). Convex limits give only an inequality, and
  limits of capacity, such as a parametric family, give none.
- *Closed,* so that a best feasible behaviour exists.
- *Everything, when nothing is known.* Then no misalignment is excused as unavoidable, as the finest resolution is the
  default in [[D4 — Resolution|D4]]. Excusing requires a stated limit.

## Notes
In reinforcement learning the feasible set of a policy acting in a fixed environment is the set of trajectory
distributions it can induce; in economics, a budget or technology set; in biology, the genotypes and frequencies that
inheritance allows. In control theory the question "which behaviours can the actor reach" is controllability.

## Lineage
v7.10: Def 23's feasibility slot, dropped in v8 because it did not change the measure; it returns because
it splits the measure. v7.10: B1 and ROADMAP §6 G2 (retention). New: the definition, and linearity as the class for
which the split is exact.

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[D4 — Resolution|D4]] — Resolution

## Used by
- [[D8 — Conditions, responses and views|D8]] — Conditions, responses and views
- [[D9 — Observation and identification|D9]] — Observation and identification
- [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]] — Misalignment splits into what the actor could avoid and what it could not
- [[P27 — The best use of a departure budget|P27]] — The best use of a departure budget
