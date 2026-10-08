---
kind: proposition
id: P12
aliases: ["P12"]
source: "derived/identifiability.md"
---
# P12 — What interventions reveal
> [!info] Generated from [derived/identifiability.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/identifiability.md#p12--what-interventions-reveal). Edit the source, not this note.

## Statement
(i) **Pass-through is identified from behaviour alone.** Let `p, p' ∈ Δ°` be the behaviour before and
after an intervention `u`. The actor passes it through if and only if `log(p'/p) ∈ span{u, 1}`, and then the
pass-through is the coefficient of `u`. If `log(p'/p)` is not in `span{u, 1}`, no pass-through explains the change.
(ii) **Changes certify distinctions.** Let `𝒜` be a resolution and `s ↦ p_s` a continuously differentiable path in `Δ°`,
over an interval containing `0`. Every behaviour on the path splits each cell of `𝒜` in the same proportions as `p_0` if
and only if every revealed objective `F_s` is constant on the cells of `𝒜`. So a revealed objective that separates two
outcomes of one cell shows that their ratio moved; revealed objectives that never separate them do not show that the
actor cannot tell them apart.

## In plain terms
Whether an actor simply follows an incentive can be read from its behaviour before and after,
without knowing what it wants: the change must be a multiple of the incentive, apart from a constant, and that multiple
is the pass-through. If the change has any other shape, something more than the incentive moved it: the incentive
changed what the actor pursues or where it starts from, or something else changed at the same time. Likewise, a change
that moves two outcomes apart proves that the actor treats them differently; changes that never do prove nothing.

## Proof
(i) If `p' = tilt(p, φ·u)`, then `log(p'/p) = φ·u − log E_p[e^{φu}]`, which is in `span{u, 1}`. Conversely,
if `log(p'/p) = φ·u + c`, then `p'` is proportional to `p·e^{φu}`, and normalization gives `p' = tilt(p, φ·u)`. Since
`u` is non-constant, `u` and `1` are linearly independent, so `φ` is determined.
(ii) If `p_s(·|A) = p_0(·|A)` for every cell `A` and every `s`, then for `x ∈ A`,
`log p_s(x) = log p_s(A) + log p_0(x|A)`, so `F_s(x) = ∂_s log p_s(A)` is the same for every `x ∈ A`. Conversely, if
every `F_s` is constant on each cell, then for `x` and `y` in one cell, `∂_s log(p_s(x)/p_s(y)) = F_s(x) − F_s(y) = 0`,
so every ratio inside a cell keeps its value at `s = 0`, and so does the split. For the last sentence: the constant path
`p_s = p_0` has `F_s = 0` for every actor, including one that tells every outcome apart.

## Notes
(i) has no power with two outcomes: then `span{u, 1}` is every function, so every change passes the
intervention through, and an intervention that changed what the actor pursues shows only as a negative or a surprising
pass-through. Telling the two apart needs at least three outcomes, or several interventions. With estimated behaviours
the distance of `log(p'/p)` from `span{u, 1}` is never exactly zero; testing it needs an estimation item, which the core
does not have yet. (ii) bounds an actor's resolution from one side only. Observed changes show which distinctions its
behaviour makes; identifying its resolution needs interventions varied enough to move every distinction it could make.
Together with [[P1 — Every behaviour is a tilt of any other|P1]], this is the ladder v7.10 proposed: a snapshot identifies an objective only given a declared default,
changes identify it up to a constant without one, and interventions identify how the actor responds.

## Lineage
v7.10: ROADMAP §6 I1 (the identifiability ladder: declare, measure, identify through interventions), B1
(identifying an actor's partition), and T7-2d. New: both statements.

## Checks
- [`checks/test_identifiability.py::test_pass_through_is_identified_from_behaviour_alone`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_identifiability.py)
- [`checks/test_identifiability.py::test_revealed_objectives_certify_distinctions`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_identifiability.py)

## Depends on
- nothing

## Used by
- no later item
