---
id: "Def 19"
type: "definition"
title: "declared intended set; R7-9"
section: "Core 07 Identification, gauge, and the intent ray"
order: 42.8
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: []
mentions: ["Def 17", "Def 18", "Def 8", "Prop 18", "Prop 34", "R7-9 results", "R8 foundations review", "Thm 1"]
checks: []
sources: []
aliases: ["Definition 19", "Def. 19"]
updated: "2026-09-27"
---
# Def 19 — declared intended set; R7-9
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

# Def 19 — declared intended set; R7-9

## Statement

**Definition 19 (declared intended set; R7-9).** Let `Δ°` be the set of full-support distributions on `X`.
- A **declaration** fixes a set `𝓘 ⊆ Δ°` of **intended behaviours**, closed in `Δ°`.
- The **misalignment** of a full-support `p̂` under `𝓘` is `M_𝓘(p̂) = inf_{p ∈ 𝓘} KL(p̂‖p)`, undefined when `𝓘` is empty.
- `𝓘` is **log-convex** if, for all `p₀, p₁ ∈ 𝓘` and `λ ∈ [0, 1]`, the **geometric mixture**
  `p_λ = p₀^{1−λ}·p₁^{λ} / Σ_x p₀^{1−λ}·p₁^{λ}` is in `𝓘`.

## Notes and checks

*Note (what this definition does).* It states the measurement layer in one line: **misalignment is the KL projection
of the actual behaviour onto what the principal declared as intended.** Everything else the measurement layer
contains is a way to *generate* `𝓘` from declarations — the reference `q`, a target set (Def. [[Def 17|17]]), a convention
(Def. [[Def 8|8]]), a cap (Def. [[Def 18|18]]) — and Prop. [[Prop 34|34]](a) shows each existing measure is a case. A new notion enters as a
new generator of `𝓘`, not as a new axiom. KL is the divergence because the principal is entropic (Thm [[Thm 1|1]]); detection (Prop. [[Prop 18|18]]) bounds it but does not select it ([[R8 foundations review]], A2).

*Note (the budget set is not a declaration; R8-1).* Under the budget convention `𝓘 = {p_{F,λ}}`, and `λ` is set by
`KL(p̂‖q)`: the set depends on the behaviour being judged. Prop. [[Prop 34|34]] still holds, since the measure uses that set,
but the declaration is a *family* of sets indexed by the agent's spending. "The projection onto what the principal
declared" is literal only for the free-type measures ([[R8 foundations review]], A6).

*Note (the declaration registry).* Every declaration needs an elicitation story — how a real principal states it
— and a justified default. The registry, and the audit of choices still made silently, are in [[R7-9 results]].

*Note (why log-convexity).* Prop. [[Prop 34|34]](c): on a log-convex set the projection is unique and satisfies a
Pythagorean inequality. That is where every decomposition of the core comes from, and why the ordinal budget
measure, whose set is not log-convex, needed a solver.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- none

## Used by
- [[Prop 34]] — the core as a declared intended set; R7-9
- [[Prop 36]] — declared resolution against the core; R7-10

## Mentions
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Def 17]] — target sets; R7-7
- [[Def 18]] — intensity caps and distributional targets; R7-6a
- [[Prop 18]] — harm bounds detectability
- [[Prop 34]] — the core as a declared intended set; R7-9
- [[R7-9 results]]
- [[R8 foundations review]]
- [[Thm 1]] — regret is a divergence

## Mentioned in
- [[Def 11]] — the misalignment contract; R7-0

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
