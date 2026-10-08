---
kind: proposition
id: P7
aliases: ["P7"]
source: "derived/resolution.md"
---
# P7 — Indifference forgives exactly what happens inside cells
> [!info] Generated from [derived/resolution.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/resolution.md#p7--indifference-forgives-exactly-what-happens-inside-cells). Edit the source, not this note.

## Statement
Let `ℬ` be a resolution and `q ∈ Δ°`.
(i) If a specification is stated at resolution `ℬ`, then for every `p̂ ∈ Δ`, `M(p̂) = inf_{p ∈ 𝓘_ℬ} KL(p̂_ℬ‖p)`:
misalignment depends only on the cell masses of `p̂`.
(ii) Let `F` be non-constant and constant on the cells of `ℬ`. Let `M` be the misalignment under the standard
specification of `F`, and `M_ℬ` the misalignment under the standard specification at resolution `ℬ`. Then for every
`p̂ ∈ Δ`, `M(p̂) = M_ℬ(p̂) + W(p̂)`, where `W(p̂) = KL(p̂‖q) − KL(p̂_ℬ‖q_ℬ)` is the **within-cell departure**.

## In plain terms
When the principal declares that it does not care how outcomes inside a cell are split,
misalignment depends only on how often each cell occurs. Compared with caring about every outcome, declaring
indifference removes exactly the part of the departure from the default that happens inside cells, and nothing else. A
maximizer that picks one of several tied best outcomes is charged when the ties are distinguished, and aligned once the
principal declares them equivalent.

## Proof
(i) By [[P4 — What KL measures|P4]](iii), for every `p ∈ 𝓘`, `KL(p̂‖p) = KL(p̂_ℬ‖p_ℬ) + Σ_{C : p̂(C) > 0} p̂(C)·KL(p̂(·|C)‖p(·|C))`.
Membership in `𝓘` constrains only `p_ℬ`: any full-support splits inside the cells can be combined with any `p_ℬ ∈ 𝓘_ℬ`.
Choosing splits that approach `p̂(·|C)` makes the second term tend to `0`, so the infimum over `𝓘` is the infimum over
`𝓘_ℬ` of the first term.
(ii) Since `F` is constant on each cell, `p_{F,t}(·|C) = q(·|C)` for every `t` and every cell `C`, and `(p_{F,t})_ℬ` is
the pursuit of `F`, read on the cells, from `q_ℬ`. By [[P4 — What KL measures|P4]](iii), applied with `r = p_{F,t}` and with `r = q`,
`KL(p̂‖p_{F,t}) = KL(p̂_ℬ‖(p_{F,t})_ℬ) + W(p̂)`, where
`W(p̂) = Σ_{C : p̂(C) > 0} p̂(C)·KL(p̂(·|C)‖q(·|C)) = KL(p̂‖q) − KL(p̂_ℬ‖q_ℬ)` does not depend on `t`. Taking the
infimum over `t ≥ 0`, and using (i) for `M_ℬ`, gives `M(p̂) = M_ℬ(p̂) + W(p̂)`.

## Notes
The tie case settles the charge noted in [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]]: the maximizer was charged only for a distinction the principal
had not said it cared about. Indifference is the only way the core forgives what happens inside cells. A coarse
resolution chosen to hide an exploit would be a specification error, which is why the finest resolution holds unless
another is declared.

## Lineage
v7.10: Def 21 and R7-10 (a declared resolution removes exactly the drift inside cells, under the free
convention), Prop 32(b) and ROADMAP §6 G1 (underdetermination, here declared).

## Checks
- [`checks/test_resolution.py::test_indifference_depends_only_on_cell_masses`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_resolution.py)
- [`checks/test_resolution.py::test_indifference_removes_the_within_cell_departure`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_resolution.py)
- [`checks/test_resolution.py::test_ties_are_forgiven_when_merged`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_resolution.py)

## Depends on
- [[P4 — What KL measures|P4]] — What KL measures

## Used by
- no later item
