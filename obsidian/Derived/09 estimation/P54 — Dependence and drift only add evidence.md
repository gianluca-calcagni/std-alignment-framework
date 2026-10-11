---
kind: proposition
id: P54
aliases: ["P54"]
source: "derived/estimation.md"
---
# P54 — Dependence and drift only add evidence
> [!info] Generated from [derived/estimation.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/estimation.md#p54--dependence-and-drift-only-add-evidence). Edit the source, not this note.

## Statement
Let a record of `n ≥ 1` decisions ([[D11 — Record, sample and evidence|D11]]) have joint behaviour `P`, a distribution on the sequences of
`n` outcomes, with marginals `p̂_1, …, p̂_n` on `X`. Let `p̄ = (1/n)·Σ_i p̂_i` be its average behaviour,
`δ = (1/n)·Σ_i KL(p̂_i‖p̄)` its drift, and `κ = (1/n)·KL(P‖p̂_1 ⊗ … ⊗ p̂_n)` its **dependence**, per decision.
(i) For every `p ∈ Δ°`, `(1/n)·KL(P‖p^{⊗n}) = KL(p̄‖p) + δ + κ`, where `p^{⊗n}` is `n` independent decisions from `p`.
(ii) Under a specification `(q, 𝓘)`, the least expected evidence per decision that the record gives for its joint
behaviour against an intended behaviour deciding independently, `inf_{p∈𝓘} (1/n)·KL(P‖p^{⊗n})`, is `M(p̄) + δ + κ`,
attained by a nearest intended behaviour for `p̄` when `p̄ ∈ Δ°` ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](i)). `δ = 0` exactly when the decisions are
identically distributed, and `κ = 0` exactly when they are independent.
(iii) The record's empirical behaviour has expectation `p̄`, whatever the dependence and the drift.

## In plain terms
When an actor's decisions depend on one another, or change over the record, the record holds more
evidence against every intended behaviour than the misalignment of its average behaviour, and exactly two terms more:
how much the decisions drift, and how much they depend on one another. Misalignment computed from the counts judges the
actor's average behaviour, which the counts estimate without bias, though they settle on it only when the dependence
between decisions fades over the record; and it is the whole evidence exactly when the decisions are independent and
alike. So independence of the actor is not needed for the measure; what it adds, when it fails, is reported beside it.

## Proof
(i) `P` gives positive probability only to sequences whose outcomes each have positive probability under
their marginal, so `log(P(x)/p^{⊗n}(x)) = log(P(x)/Π_i p̂_i(x_i)) + Σ_i log(p̂_i(x_i)/p(x_i))` wherever `P(x) > 0`. The
average under `P` of the first term is `n·κ`, and that of the `i`-th term of the sum depends only on the marginal
`p̂_i`, so it is `KL(p̂_i‖p)`. Then
`(1/n)·Σ_i KL(p̂_i‖p) = (1/n)·Σ_i Σ_x p̂_i(x)·(log(p̂_i(x)/p̄(x)) + log(p̄(x)/p(x))) = δ + KL(p̄‖p)`. (ii) `δ` and `κ`
do not depend on `p`, so the infimum over `𝓘` is `M(p̄) + δ + κ`, attained where `KL(p̄‖p)` is least, which some `p ∈ 𝓘`
is when `p̄ ∈ Δ°` ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](i)). By Gibbs' inequality, `δ = 0` exactly when every `p̂_i` equals `p̄`, and `κ = 0` exactly
when `P` is the product of its marginals.
(iii) The expected share of an outcome `x` is `(1/n)·Σ_i P(x_i = x) = p̄(x)`.

## Notes
(i) is the chain rule for a product reference ([[References|@polyanskiy2025]], Theorem 2.16(c), (2.27)) followed by the
split of [[P45 — Drift: what runs share, and what they do not|P45]](i) over the decisions, read in time rather than across runs; `κ` is the coordination of [[P39 — Several actors: coordination plus individual misalignment|P39]] with the
decisions as the actors, and it is often called the total correlation or the multi-information. For a sample ([[D11 — Record, sample and evidence|D11]]),
`δ = κ = 0` and (ii) is [[P21 — The expected evidence is misalignment|P21]](ii). What the record's counts certify is [[P55 — What a record of counts certifies, at every size|P55]]: its test keeps its level for independent
decisions that drift, but not for decisions that depend on each other, whose counts may stay far from `p̄` ([[P55 — What a record of counts certifies, at every size|P55]],
Notes). Estimating `κ` needs the order of the decisions, not only their counts, and many episodes per dependent block; a
case that suspects dependence between episodes reports it as a diagnostic, beside the misalignment of the counts.

## Lineage
New in v13 (`NOTES.md` §18): the independence of the actor's decisions, a phenomenological assumption of
[[A4 — Misalignment is evidence|A4]] until then, replaced by this account of what dependence and drift add (Q53).

## Checks
- [`checks/test_estimation.py::test_dependence_and_drift_only_add`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_estimation.py)

## Depends on
- [[D11 — Record, sample and evidence|D11]] — Record, sample and evidence
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits

## Used by
- no later item
