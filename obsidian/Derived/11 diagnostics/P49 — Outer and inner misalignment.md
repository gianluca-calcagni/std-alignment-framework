---
kind: proposition
id: P49
aliases: ["P49"]
source: "derived/diagnostics.md"
---
# P49 — Outer and inner misalignment
> [!info] Generated from [derived/diagnostics.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/diagnostics.md#p49--outer-and-inner-misalignment). Edit the source, not this note.

## Statement
Let a principal's target `F` and a trainer's evaluator `F̂` be non-constant functions on `X`, judged from
one default `q`; write `M_P` for misalignment under the standard specification of `F`, and `M_T` under that of `F̂`,
whose intended behaviours are the optima of training on `F̂` with a KL penalty ([[P4 — What KL measures|P4]]).
(i) **Outer misalignment.** At intensity `t ≥ 0`, the **outer misalignment** is `O(t) = M_P(p_{F̂,t})`, the principal's
misalignment of the trainer's own optimum. If `F̂ = a·F + c` with `a > 0`, then `O(t) = 0` for every `t`; otherwise
`O(t) > 0` for every `t > 0`. As `t → 0`, `O(t)/KL(p_{F̂,t}‖q) → sin²θ` if `cos θ ≥ 0`, and `→ 1` otherwise, with `θ`
the angle of [[P11 — The misaligned share at the start of a change|P11]] between `F̂` and `F`.
(ii) **Inner misalignment and the split.** The **inner misalignment** of a behaviour `p̂ ∈ Δ°` is `M_T(p̂)`. Let `p̃` be
the tilt of `q` by a combination of `F` and `F̂` with `p̂`'s averages of both ([[P48 — Misalignment when the target is uncertain|P48]]). Then `M_P(p̂) = U + M_P(p̃)` and
`M_T(p̂) = U + M_T(p̃)`, with the same **strict inner misalignment** `U = KL(p̂‖p̃)`: the least misalignment that any
principal whose target combines `F` and `F̂` finds in `p̂` ([[P48 — Misalignment when the target is uncertain|P48]]).
(iii) **The two limits.** A perfect optimizer of the training objective, `p̂ = p_{F̂,t}`, has `U = 0` and `M_T(p̂) = 0`,
and its misalignment is all outer: `M_P(p̂) = O(t)`. An evaluator that is the target up to a positive scale and a
constant, `F̂ = a·F + c` with `a > 0`, has `O = 0` and `M_T = M_P`: all misalignment is inner.

## In plain terms
Training on an evaluator in place of the target fails in two ways. Outer misalignment is a fault of
the specification: even a perfect optimizer of the training objective is that far from what the principal wants, and it
is zero only when the evaluator is the target rescaled. Inner misalignment is a fault of the optimizer: how far the
trained actor is from anything the training objective could produce. The principal's and the trainer's misalignments
share one part exactly, the change that pursues neither the target nor the evaluator; the rest is how the actor's
pursuit, within what target and evaluator can describe, leans away from each.

## Proof
(i) If `F̂ = a·F + c` with `a > 0`, then `p_{F̂,t} = p_{F,at}` by [[P1 — Every behaviour is a tilt of any other|P1]](ii), which is on the principal's ray.
Otherwise, if `O(t) = 0` for some `t > 0`, the full-support `p_{F̂,t}` is in the closure of `F`'s ray, hence on it
([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](ii)), so `tilt(q, t·F̂) = tilt(q, s·F)` for some `s ≥ 0`, and `t·F̂ − s·F` is constant by [[P1 — Every behaviour is a tilt of any other|P1]](ii); `s > 0`
because `F̂` is not constant, a contradiction. The limit is [[P11 — The misaligned share at the start of a change|P11]] for the path `t ↦ p_{F̂,t}`, whose revealed objective
at `t = 0` is `F̂`.
(ii) `p̂` and `p̃` have the same averages of `F` and of `F̂`, so `p̃` is the named pursuit of [[P44 — What named objectives explain|P44]] both for the
principal's specification with `F̂` named and for the trainer's with `F` named ([[P48 — Misalignment when the target is uncertain|P48]](iii)). [[P44 — What named objectives explain|P44]](ii) gives both
identities, with the same first term `KL(p̂‖p̃)`, and [[P48 — Misalignment when the target is uncertain|P48]](i) gives its reading as the least misalignment over the
principals whose target lies in the span of `F` and `F̂`.
(iii) `p_{F̂,t}` is on the trainer's ray, so `M_T(p̂) = 0`, and it is a tilt of `q` by a combination of `F` and `F̂`, so
`U = 0` by [[P44 — What named objectives explain|P44]](ii); `M_P(p̂) = O(t)` by definition. If `F̂ = a·F + c` with `a > 0`, the two rays are the same set by
[[P1 — Every behaviour is a tilt of any other|P1]](ii), so the two specifications, and their misalignments, are the same ([[P9 — What is at stake|P9]](iii)), and `O = 0` by (i).

## Notes
Outer misalignment needs the principal's target: case W1 had one, a gold reward model, and W3 and W4 had
none, so they measured inner misalignment only (`NOTES.md` §7). The growth of `O(t)` with intensity is Goodhart's law in
this framework: how the principal's objective moves along the evaluator's ray is governed by the regression of `F` on
`F̂` ([[P18 — Through the evaluator, only the regression counts|P18]]–[[P20 — Where overoptimization starts, and how it ends|P20]], [[P25 — The target's curve turns no more often than the regression|P25]]). Inner misalignment splits further by the diagnostics above: what named objectives explain
([[P44 — What named objectives explain|P44]]), what recurs across runs and what is drift ([[P45 — Drift: what runs share, and what they do not|P45]]), what differs between evaluation and use ([[P46 — What runs share between conditions, and what they do not|P46]]), and what
the actor's limits make unavoidable ([[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]). When the principal's target is uncertain, both outer misalignment and the
split become intervals over the declared family ([[P48 — Misalignment when the target is uncertain|P48]]). The split assumes one default for principal and trainer; with
two defaults, the change of default adds a term of its own.

## Lineage
v7.10: Cor 1.5 and A16 (stacked stages, with an outer–inner cross term at second order), and H12 (the chain
rule of KL may give the archive's five gaps back as additive terms); the outer and inner alignment of Hubinger et al.
(2019), as a two-link chain (`RELATED.md`). New: the exact split, and outer misalignment as a function of intensity.

## Checks
- [`checks/test_diagnostics.py::test_outer_and_inner_misalignment`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_diagnostics.py)

## Depends on
- [[P1 — Every behaviour is a tilt of any other|P1]] — Every behaviour is a tilt of any other
- [[P4 — What KL measures|P4]] — What KL measures
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits
- [[P9 — What is at stake|P9]] — What is at stake
- [[P11 — The misaligned share at the start of a change|P11]] — The misaligned share at the start of a change
- [[P44 — What named objectives explain|P44]] — What named objectives explain
- [[P48 — Misalignment when the target is uncertain|P48]] — Misalignment when the target is uncertain

## Used by
- no later item
