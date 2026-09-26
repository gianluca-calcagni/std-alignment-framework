---
id: "Def 13"
type: "definition"
title: "actor models; R7-1"
section: "Core 01 Setting"
order: 4
layer: "explanation"
tier: []
assumes: []
status: "definition"
depends_on: []
mentions: ["Def 11", "Def 14", "Def 15", "Def 16", "Prop 12", "Prop 23", "Prop 26", "Prop 27"]
checks: []
sources: []
aliases: ["Definition 13", "Def. 13"]
updated: "2026-09-26"
---
# Def 13 — actor models; R7-1
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 01 Setting]]
<!-- /gen:header -->

## Statement

**Definition 13 (the explanation layer: evaluators and actor models; R7-1–R7-3).**

| Symbol | Object |
|---|---|
| `F̂ = F + E` | an **evaluator**: an objective an actor model is run on. `E` is its **error** |
| `Λ(t) = log E_{p*} e^{t(E − E_{p*}E)}` | the centred cumulant generating function (CGF) of the error under `p*` |
| `Λ_q(t)` | the same under `q` |
| `q_A` | the actor's own full-support reference |

An **actor model** is a map `A` from an objective `G` (with the actor's own reference `q_A` and a resource `r`)
to a behaviour `A(G; q_A, r) ∈ Δ(X)`. It *explains*
behaviour, and is not part of what misalignment means. The **entropic model** is
`A(G; q_A, β) = p^{q_A}_{G,β}`, with the price `β` as its resource.

**Hypothesis (E_A).** The actual behaviour is the entropic model run on the evaluator from the actor's own
full-support reference: `p̂ = p^{q_A}_{F̂,β}`.

**Hypothesis (E).** The special case `q_A = q`: `p̂ = p_{F̂,β}`.

A result that needs an actor model says so in brackets, *[Assumes (E).]* or *[Assumes (E_A).]*.

## Notes and checks

*Note.* Other named models:
- the capacity model — Def. [[Def 15|15]], hypothesis (C);
- argmax selectors over a random candidate set, e.g. best-of-n — Prop. [[Prop 23|23]].

No misalignment measure assumes an actor model (Def. [[Def 11|11]], M4). Comparisons that do are in Def. [[Def 14|14]].

*Note (R7-4).* An evaluator can be split into the agent's own objective `G` and an external reward `R`,
weighted per context by a derived shadow price: `F̂_c = G + κ_c R` (Def. [[Def 16|16]], Prop. [[Prop 27|27]]).

*Note (R7-2).* The declared reference `q` belongs to the specification of intent. The actor's reference `q_A`
belongs to the explanation, and behaviour does not identify it separately from the evaluator (Prop. [[Prop 12|12]]).
The two coincide in v6.6, where one `q` played both roles. Every result stated under (E) transfers to (E_A)
with the error replaced by `E + h/β`, where `h = log(q_A/q)` (Prop. [[Prop 26|26]]).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- none

## Used by
- [[B03]] — Goodhart variants — Manheim & Garrabrant (2018)
- [[B04]] — Reward-model overoptimization — Gao, Schulman & Hilton (ICML 2023)
- [[B05]] — When does optimizing a proxy help at all? — Laidlaw et al.; Holmström & Milgrom (1991)
- [[B11]] — Quantitative genetics — selection on a proxy trait *(new in v6.1)*
- [[B12]] — Human choice — logit, defaults, rational inattention, present bias *(new in v6.2)*
- [[B13]] — Potential games — collective behaviour is a tilt (Blume 1993) *(new in v6.2)*
- [[C05]] — Decomposition, gauge and conventions (Thm 13, Prop. 16, Thm 17, Def. 8)
- [[C06]] — What optimization pressure does (Prop. 14)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[C09]] — The overoptimization slope *(untested prediction)*
- [[Cor 1.3]] — CGF and integral forms
- [[Cor 13.1]]
- [[Cor 13.3]] — rescaling is purely axial
- [[Cor 17.1]] — the capacity actor's regret is the budget convention
- [[Def 7]] — reporting rule
- [[Def 14]] — mechanism-relative comparison; explanation layer; R7-1
- [[Def 15]] — the capacity model; R7-3
- [[Def 16]] — external reward, contingency and coupling; R7-4
- [[Prop 3]] — only the upper tail matters
- [[Prop 6]] — the width, computed
- [[Prop 7]] — a bound with realized travel from the reference
- [[Prop 10]] — conjugate pairings
- [[Prop 11]] — the order is structural, not a matter of tightness
- [[Prop 12]] — what behaviour identifies
- [[Prop 14]]
- [[Prop 16]] — gauge group and identified quantities
- [[Prop 20]] — Goodhart as a covariance — any optimizer; tier 1
- [[Prop 21]] — no overoptimization under an affine regression — for any actor that sees only the evaluator; tier 1, v6.3
- [[Prop 22]] — the first-order effect of any smooth optimizer; tier 1, v6.3
- [[Prop 23]] — argmax selectors on a common candidate set — tier 2′, v6.4
- [[Prop 25]] — mechanism-relative comparisons against the contract; tier 1 given the attribution
- [[Prop 26]] — reference misspecification is measured misalignment; R7-2
- [[Prop 27]] — instrumental tracking — the weight on external reward is a shadow price; R7-4
- [[Prop 28]] — incentive masking; R7-4
- [[Prop 30]] — the fake-alignment gap; R7-4
- [[Rem 13.5]] — whether rescaling is harmful depends on the declared convention; v6.3
- [[Rem 16.1]] — reference misspecification
- [[Thm 5]] — the width is the exact worst case

## Mentions
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 14]] — mechanism-relative comparison; explanation layer; R7-1
- [[Def 15]] — the capacity model; R7-3
- [[Def 16]] — external reward, contingency and coupling; R7-4
- [[Prop 12]] — what behaviour identifies
- [[Prop 23]] — argmax selectors on a common candidate set — tier 2′, v6.4
- [[Prop 26]] — reference misspecification is measured misalignment; R7-2
- [[Prop 27]] — instrumental tracking — the weight on external reward is a shadow price; R7-4

## Mentioned in
- [[Def 1]] — objects
- [[Def 12]] — alignment instance; formal
- [[Overview 0]] — alignment instance — static, single-target module; not a definition — the formal definition is Definition 12

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
