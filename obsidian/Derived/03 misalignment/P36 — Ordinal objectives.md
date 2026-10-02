---
kind: proposition
id: P36
aliases: ["P36"]
source: "derived/misalignment.md"
---
# P36 — Ordinal objectives
> [!info] Generated from [derived/misalignment.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/misalignment.md#p36--ordinal-objectives). Edit the source, not this note.

## Statement
Let `F` be non-constant, with values `v_1 < … < v_m` on the level sets `L_1, …, L_m`. The **ordinal
specification** of `F` is `(q, C_F)`, with `C_F = {p ∈ Δ° : p/q is a non-decreasing function of F}`. For `p̂ ∈ Δ°`, let
`r°` be the isotonic regression of the level ratios `p̂(L_j)/q(L_j)` with weights `q(L_j)`: the non-decreasing sequence
nearest to them in weighted least squares [[References|@robertson1988]], read as a function of `F` on `X`. Its pooled blocks
`B_1, …, B_k` are the unions of consecutive level sets on which it is constant. Let `p° = q·r°`.
(i) `C_F` is the closure in `Δ°` of the union of the pursuit rays of `φ∘F` over the increasing functions `φ`, and it
contains best-of-`n` by `F` for every `n ≥ 1`; it is closed in `Δ°`, so `(q, C_F)` is a specification ([[D3 — Specification, declaration and misalignment|D3]]).
(ii) `p°` is the nearest intended behaviour, and the ordinal misalignment is
`M_ord(p̂) = KL(p̂‖p°) = Σ_i p̂(B_i)·KL(p̂(·|B_i)‖q(·|B_i))`.
(iii) For every `p ∈ C_F`, `KL(p̂‖p) ≥ KL(p̂‖p°) + KL(p°‖p)`, with equality at `p = q`:
`KL(p̂‖q) = M_ord(p̂) + KL(p°‖q)`.
(iv) Under the standard specification of `F`, `M(p̂) ≥ M_ord(p̂) + M(p°)`.
(v) `C_F`, `p°` and `M_ord` are unchanged when `F` is replaced by `φ∘F`, for every strictly increasing `φ`.

## In plain terms
A principal who cares only about the order of outcomes accepts every behaviour that favours better
outcomes at least as much as worse ones, relative to the default. Its misalignment pools the outcomes whose order the
actor's behaviour contradicts, and charges only the actor's departure from the default inside those pools. Misalignment
against the objective's values is the ordinal misalignment plus a term for the shape. Best-of-`n` on the objective
itself is aligned with its order, though not with its values.

## Proof
(i) For an increasing `φ`, `p_{φ∘F,t}/q = e^{t·φ(F)}/Z` is a non-decreasing function of `F`, so every such
ray lies in `C_F`, which is closed in `Δ°`, being defined by non-strict inequalities. Conversely, if `p ∈ C_F` has level
ratios increasing strictly, then `p = p_{φ∘F,1}` for an increasing `φ` with `φ(v_j)` the log of the `j`-th ratio;
otherwise `p` is a limit of such behaviours. Best-of-`n` by `F` has the level ratio `(A_j^n − A_{j−1}^n)/q(L_j)`, with
`A_j` the default's mass of `F ≤ v_j`, which is `n` times the average of `u^{n−1}` over `[A_{j−1}, A_j]`, non-decreasing
in `j`. (iii) Let `y = p̂/q`, a function on `X`, and `K` the convex cone of non-decreasing functions of `F`. `r°` is the
projection of `y` onto `K` in `L²(q)` [[References|@robertson1988]]; hence `E_q[(y − r°)·g] ≤ 0` for every `g ∈ K`, and
`E_q[(y − r°)·h] = 0` for every `h` constant on each pooled block, since `r°` is the `q`-average of `y` there. With
`h = 1`, `p°` sums to one, and `r° > 0`, so `p° ∈ C_F`. For `p = q·ρ ∈ C_F`,
`KL(p̂‖p) − KL(p̂‖p°) − KL(p°‖p) = E_q[(y − r°)·log(r°/ρ)]`; the part with `log r°` is `0`, since `log r°` is constant
on blocks, and the part with `−log ρ` is at least `0`, since `log ρ ∈ K`. At `p = q`, `log ρ = 0`. (ii) By (iii),
`KL(p̂‖p) > KL(p̂‖p°)` for every `p ≠ p°` in `C_F`. On a block `B`, `p°(B) = p̂(B)` and `p°(·|B) = q(·|B)`, so the chain
rule [[P4 — What KL measures|P4]](iii) gives the sum. (iv) Every point of the pursuit ray of `F` is in `C_F`; apply (iii) to each and take the
infimum. (v) `C_F` and the regression depend on `F` only through the ordered level sets.

## Notes
This is `NOTES.md` proposal E3. A coarse actor's best effort ([[P8 — An actor that cannot tell outcomes apart|P8]](ii)) and best-of-`n` are ordinally
aligned whenever their reweighting rises with `F`. The archive's check found, against its pre-registration, that the
gap between the ordinal and the budget measure is of second order in `M_ord`; the core does not use the budget measure.

## Lineage
v7.10: Def 17 (target sets, the ordinal part) and Prop 32 (the ordinal measure), with Prop 31 (c); R7-7.

## Checks
- [`checks/test_misalignment.py::test_ordinal_objectives`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_misalignment.py)

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[P4 — What KL measures|P4]] — What KL measures

## Used by
- no later item
