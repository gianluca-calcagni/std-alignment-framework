---
kind: lemma
id: L1
aliases: ["L1"]
source: "derived/evaluator.md"
---
# L1 — Separable bounds are loose when two quantities change rank
> [!info] Generated from [derived/evaluator.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/evaluator.md#l1--separable-bounds-are-loose-when-two-quantities-change-rank). Edit the source, not this note.

## Statement
Let `Q(E, δ) > 0` for `E` in a pair `{E₁, E₂}` and `δ` in a set `D`, let
`ρ(δ) = Q(E₁, δ)/Q(E₂, δ)`, and `K = sup_D ρ / inf_D ρ`. If `B(E, δ) = a(E)·b(δ)` satisfies `Q ≤ B ≤ L·Q` on
`{E₁, E₂} × D`, then `L ≥ √K`; and some separable `B` attains `L = √K`.

## In plain terms
A bound that multiplies a property of the error by a function of the budget cannot follow two errors
whose ratio changes with the budget: if the ratio moves by a factor `K`, the bound is off by at least `√K` somewhere.

## Proof
For every `δ`, `κ = a(E₁)/a(E₂) = B(E₁, δ)/B(E₂, δ)` lies in `[ρ(δ)/L, L·ρ(δ)]`, so
`sup_D ρ/L ≤ κ ≤ L·inf_D ρ`, which gives `L² ≥ K`. For the second part, take `a(E₂) = 1`,
`a(E₁) = κ = (sup_D ρ · inf_D ρ)^{1/2}` and `b(δ) = Q(E₂, δ)·(ρ(δ)/κ)^{1/2}`: then `B/Q` is `(ρ/κ)^{1/2}` on `E₂` and
`(κ/ρ)^{1/2}` on `E₁`, both between `K^{−1/4}` and `K^{1/4}`; rescaling `b` by `K^{1/4}` gives `Q ≤ B ≤ √K·Q`.

## Lineage
v7.10: Lemma 8. New: that `√K` is attained.

## Checks
- [`checks/test_evaluator.py::test_no_separable_bound_on_the_worst_case`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_evaluator.py)

## Depends on
- nothing

## Used by
- [[P30 — No separable bound on the worst case|P30]] — No separable bound on the worst case
