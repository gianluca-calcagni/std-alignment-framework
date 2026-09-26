---
id: "Prop 29"
type: "proposition"
title: "the outer process sees only rewarded behaviour; R7-4"
section: "Core 09b External reward and fake alignment"
order: 58
layer: "explanation"
tier: ["1", "4 (E_R)"]
assumes: ["Hyp E_R"]
status: "proved"
depends_on: ["Prop 28", "Def 16"]
mentions: []
checks: ["V34"]
sources: []
aliases: ["Proposition 29", "Prop. 29"]
updated: "2026-09-26"
---
# Prop 29 — the outer process sees only rewarded behaviour; R7-4
<!-- gen:header -->
> [!abstract] Proposition · tier 1 / 4 (E_R) · assumes [[Hyp E_R]] · proved · in [[Core 09b External reward and fake alignment]]
<!-- /gen:header -->

## Statement

**Proposition 29 (the outer process sees only rewarded behaviour; R7-4).**

(a) *(No assumption on the actual actor.)* Under the persistence coupling, an agent's persistence
probability per episode is `S = E_c s_c(p̂_c) = 1 − ν·E_c m_c (max R(c,·) − E_{p̂_c}R(c,·))`. It depends on the
agent's behaviour only in contexts with `m_c > 0`. Two agents with equal `m`-weighted expected reward persist
equally, and an outer process that retains agents in proportion to `S` leaves their population ratio
unchanged: **selection equivalence**.

(b) *[Assumes (E_R).]* For two types as in Prop. 28, with a common weight `κ` in a contingent context `c`,
`|E_{p_1^κ}R − E_{p_2^κ}R| = O(e^{−βκ·gap_R})`. The rate is exactly `β·gap_R` when
`Σ_{x: d(x)=gap_R} (a_1(x) − a_2(x)) ≠ 0`. The outer process's power to tell the types apart in `c` therefore
vanishes as the incentive grows.

## Proof

*Proof.* (a) `S` is linear in the `E_{p̂_c}R` with coefficients `ν·ρ(c)·m_c`, which vanish where `m_c = 0`. If
`π'(θ) ∝ π(θ)S(θ)`, then `π'(θ_1)/π'(θ_2) = [π(θ_1)/π(θ_2)]·[S(θ_1)/S(θ_2)]`.
(b) `E_{p_1}R − E_{p_2}R = Σ_{x≠x_R}(p_1(x) − p_2(x))(R(x) − R(x_R))`. With the expansion in Prop. 28's proof, the
leading term is `−gap_R·Σ_{d(x)=gap_R}(a_1(x) − a_2(x))·e^{−βκ·gap_R}`. ∎

## Notes and checks

*Check.* [[V34]], over 300 instances in the same window as Prop. [[Prop 28|28]]: the log-slope divided by `−β·gap_R` lies in
`[0.958, 1.125]`, and 298 of 300 are within 10 %. The two outside are pre-asymptotic interference between
the runner-up and the next term.

*Reading.* **Reward can only select on what reward sees** (a). Among what it sees, a stronger incentive makes
different own objectives look the same (b). So selection on `R` cannot remove a type whose own objective
departs from the target only where `m_c = 0`, and it loses its grip on the rest as incentives grow. That is
the structural reason no external reward guarantees alignment. The two escape routes are contexts that are
contingent but that the agent does not recognize as such (`m_c` believed small), and moderate incentives
(Prop. [[Prop 28|28]], the P5 measurement).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 16]] — external reward, contingency and coupling; R7-4
- [[Prop 28]] — incentive masking; R7-4

## Used by
- none

## Mentions
- none

## Mentioned in
- [[Prop 30]] — the fake-alignment gap; R7-4

## Checks
- [[V34]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
