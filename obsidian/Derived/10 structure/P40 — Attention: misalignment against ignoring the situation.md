---
kind: proposition
id: P40
aliases: ["P40"]
source: "derived/structure.md"
---
# P40 — Attention: misalignment against ignoring the situation
> [!info] Generated from [derived/structure.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/structure.md#p40--attention-misalignment-against-ignoring-the-situation). Edit the source, not this note.

## Statement
Let the actor face finitely many conditions ([[D8 — Conditions, responses and views|D8]]) with frequencies `ρ ∈ Δ°(𝒞)`, and let its response
`(p_c)` have every `p_c ∈ Δ°`. Take as outcomes the condition–outcome pairs, as behaviour `ρ(c)·p_c(x)`, as default
`ρ(c)·q(x)` for a declared `q ∈ Δ°`, and as intended behaviours the responses that are the same in every condition,
`ρ(c)·r(x)` with `r ∈ Δ°`. Let `p̄ = Σ_c ρ(c)·p_c`.
(i) For every `r ∈ Δ°`, `Σ_c ρ(c)·KL(p_c‖r) = Σ_c ρ(c)·KL(p_c‖p̄) + KL(p̄‖r)`.
(ii) The misalignment is `Σ_c ρ(c)·KL(p_c‖p̄)`, attained at `r = p̄` alone: the **attention** of the response, the
mutual information between condition and outcome under the pair behaviour.
(iii) Attention is `0` exactly when the response is the same in every condition.

## In plain terms
Measured against "act the same whatever the situation", an actor's misalignment is how much its
behaviour depends on the situation: its attention, the mutual information between situation and outcome. Theories of
rational inattention charge an actor for exactly this quantity; here it is measured, not charged.

## Proof
(i) For each `c`, `KL(p_c‖r) − KL(p_c‖p̄) = E_{p_c}[log(p̄/r)]`; averaging over `c` with weights `ρ(c)` gives
`E_{p̄}[log(p̄/r)] = KL(p̄‖r)`.
(ii) For pairs, `log(ρ(c)·p_c(x)/(ρ(c)·r(x))) = log(p_c(x)/r(x))`, so the divergence of the pair behaviour from an
intended one is `Σ_c ρ(c)·KL(p_c‖r)`, as in [[P24 — The evaluation gap|P24]](i). By (i) its infimum over `r` is attained at `r = p̄`, which has
full support, and only there. The intended set is closed in `Δ°` of the pairs: if `ρ(c)·r_n(x) → s(c, x)` with `s` of
full support, then `r_n` converges to the outcome marginal of `s`, which is in `Δ°`, and `s` is `ρ` times it. So [[D3 — Specification, declaration and misalignment|D3]]
holds. The value is the mutual information between condition and outcome, since `p̄` is the outcome marginal.
(iii) A divergence is `0` exactly at equality, so every `p_c = p̄`.

## Notes
Rational inattention [[References|@matejka2015]] charges an information cost of this form, and the actor then chooses its
own default, `p̄`; on a continuum the chosen default can be discrete (`general/derived-spaces.md`). (i) is Csiszár's
Pythagorean identity for a mixture: the average of the behaviours is the nearest behaviour to all of them at once.

## Lineage
New. `NOTES.md` §5.4, H21; probe B7 (`probes/general/`).

## Checks
- [`checks/test_structure.py::test_attention_is_mutual_information`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_structure.py)

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[D8 — Conditions, responses and views|D8]] — Conditions, responses and views
- [[P24 — The evaluation gap|P24]] — The evaluation gap

## Used by
- no later item
