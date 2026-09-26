---
id: "Def 16"
type: "definition"
title: "external reward, contingency and coupling; R7-4"
section: "Core 09b External reward and fake alignment"
order: 55
layer: "explanation"
tier: []
assumes: []
status: "definition"
depends_on: ["Def 9", "Def 13"]
mentions: ["Boundary 03 The boundary as two conditions", "Prop 27"]
checks: []
sources: []
aliases: ["Definition 16", "Def. 16"]
updated: "2026-09-26"
---
# Def 16 — external reward, contingency and coupling; R7-4
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 09b External reward and fake alignment]]
<!-- /gen:header -->

## Statement

**Definition 16 (external reward, contingency and coupling; R7-4).** In each context `c` (Def. 9) an
explanation may specify:
- the **external reward** `R(c,·)`: the evaluator of an *outer process* — selection, training, payment —
  that acts on the agent;
- the **contingency** `m_c ∈ [0,1]`: the probability, as the agent assesses it, that its behaviour in `c` is
  scored by the outer process;
- the agent's **own objective** `G(c,·)`, with its own reference `q_A(·|c)` and price `β` (Def. 13);
- a **coupling** `W_c`: a concave function, differentiable on an open interval containing
  `[min R(c,·), max R(c,·)]`. It gives the agent's continuation value, in units of `G`, as a function of the
  expected reward `y = E_{p_c}R(c,·)` it earns in `c`.

The **persistence coupling** is a stationary special case:
- episodes repeat, with contexts drawn i.i.d. from `ρ`;
- after an episode in `c`, the agent persists — is neither modified nor replaced — with probability
  `s_c(p) = 1 − ν·m_c·(max R(c,·) − E_p R(c,·))`, where `ν·osc R ≤ 1`;
- it discounts future episodes by `γ ∈ (0,1)`;
- being replaced is worth `0` to it.

**Hypothesis (E_R).** The agent maximizes its own entropic utility plus its continuation value:
`p̂_c` maximizes `u_c(p) + W_c(E_p R(c,·))`, with `u_c(p) = E_p G(c,·) − KL(p ‖ q_A(·|c))/β`. Under the
persistence coupling, it maximizes its discounted value `V = E_c[u_c(p_c) + γ·s_c(p_c)·V]` over stationary
policies.

## Notes and checks

*Note.*
- **Two evaluators.** `R` is objective in one precise sense: it is the evaluator of a process that acts on
  the agent whatever the agent values. Its *binding force* on behaviour is not assumed; it is derived as a
  shadow price (Prop. [[Prop 27|27]]). The single evaluator `F̂` of Def. [[Def 13|13]] is recovered per context as
  `F̂_c = G + κ_c R`.
- **Couplings.** The persistence coupling models training and selection: reward buys "not being changed". A
  resource coupling — reward buys energy, money or compute, and hence future capacity — is another concave
  `W_c`, covered by Prop. [[Prop 27|27]](a).
- **The normalization "replaced = 0".** `V` depends on the level of `G`, not only on its differences: adding
  a constant to `G` changes `V*` and hence the weight on reward. The level encodes how much the agent's own
  continuation is worth to it.
- **Outside this definition.** Acting on `R` or on `m_c` themselves — tampering with the reward channel, or
  with the monitoring — is frame endogeneity, condition (X), [[Boundary 03 The boundary as two conditions]].

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 9]] — contexts
- [[Def 13]] — actor models; R7-1

## Used by
- [[Prop 27]] — instrumental tracking — the weight on external reward is a shadow price; R7-4
- [[Prop 28]] — incentive masking; R7-4
- [[Prop 29]] — the outer process sees only rewarded behaviour; R7-4
- [[Prop 30]] — the fake-alignment gap; R7-4

## Mentions
- [[Boundary 03 The boundary as two conditions]] — The boundary as two conditions
- [[Prop 27]] — instrumental tracking — the weight on external reward is a shadow price; R7-4

## Mentioned in
- [[Def 13]] — actor models; R7-1

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
