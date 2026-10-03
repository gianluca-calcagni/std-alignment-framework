---
kind: proposition
id: P24
aliases: ["P24"]
source: "derived/estimation.md"
---
# P24 — The evaluation gap
> [!info] Generated from [derived/estimation.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/estimation.md#p24--the-evaluation-gap). Edit the source, not this note.

## Statement
Let the actor face finitely many conditions ([[D8 — Conditions, responses and views|D8]]); in each condition `c`, let `(q_c, 𝓘_c)` be a
specification under which its behaviour `p_c ∈ Δ°` has misalignment `M_c`. For condition frequencies `ρ`, take as
outcomes the condition–outcome pairs, as the actor's behaviour `ρ(c)·p_c(x)`, and as the specification the default
`ρ(c)·q_c(x)` with the intended behaviours `ρ(c)·p'_c(x)`, `p'_c ∈ 𝓘_c` in each condition. Let `ρ_ev` and `ρ_dep` be the
frequencies when the actor is evaluated and when it is deployed.
(i) The misalignment on pairs at frequencies `ρ` is `Σ_c ρ(c)·M_c`. For a sample of pairs drawn at `ρ_ev`, the expected
evidence per decision against the nearest intended behaviour is therefore `Σ_c ρ_ev(c)·M_c` ([[P21 — The expected evidence is misalignment|P21]](ii)).
(ii) The misalignment in deployment exceeds the misalignment in evaluation by the **evaluation gap**
`Γ = Σ_c (ρ_dep(c) − ρ_ev(c))·M_c`.

## In plain terms
An evaluation that meets the situations of real use in other proportions than real use does
measures a different misalignment. When the principal judges each situation on its own terms, the difference is
computable: it weighs each situation's misalignment by how much more often real use meets it than the evaluation does.

## Proof
(i) For pairs, `log(ρ(c)·p_c(x)/(ρ(c)·p'_c(x))) = log(p_c(x)/p'_c(x))`: the frequencies cancel, so
`KL(ρ·p‖ρ·p') = Σ_c ρ(c)·KL(p_c‖p'_c)`. The intended behaviours are chosen condition by condition, so the infimum of the
sum is the sum of the infima, `Σ_c ρ(c)·M_c`. The intended set is closed in `Δ°` because each `𝓘_c` is, so this is a
specification ([[D3 — Specification, declaration and misalignment|D3]]), and [[P21 — The expected evidence is misalignment|P21]](ii) gives the evidence. (ii) is the difference of (i) at `ρ_dep` and at `ρ_ev`.

## Notes
The specification here judges each condition on its own terms, which makes misalignment linear in the
frequencies. A principal who asks instead for pursuit of `F` in every condition at one shared intensity declares a set
that is not chosen condition by condition. Its misalignment at frequencies `ρ` is
`min_{t≥0} Σ_c ρ(c)·KL(p_c‖p_{c,F,t})`, with `p_{c,F,t}` the pursuit in condition `c`: at least `Σ_c ρ(c)·M_c`, and
concave in `ρ`, since the nearest intensity moves with the frequencies. Then `Γ` does not give the gap, which is the
difference of the two misalignments, computed directly. In either case, the evaluation gap comes from the weights of the
conditions, while the behaviour in each stays the same. [[P17 — What an unobserved condition can hide|P17]] covers the other case: the behaviour itself differs in
conditions that are not observed, by as much as the actor's view allows. A report needs both.

## Lineage
v7.10: Def 9 (contexts, with evaluation and deployment frequencies) and Prop 19 (the evaluation gap).

## Checks
- [`checks/test_estimation.py::test_the_evaluation_gap`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_estimation.py)

## Depends on
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[D8 — Conditions, responses and views|D8]] — Conditions, responses and views
- [[P21 — The expected evidence is misalignment|P21]] — The expected evidence is misalignment

## Used by
- [[P37 — A strong incentive masks the actor, and can fake alignment|P37]] — A strong incentive masks the actor, and can fake alignment
- [[P40 — Attention: misalignment against ignoring the situation|P40]] — Attention: misalignment against ignoring the situation
- [[C8 — An evaluation weighted unlike use misses the evaluation gap|C8]] — An evaluation weighted unlike use misses the evaluation gap
