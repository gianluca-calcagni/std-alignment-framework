---
id: "Prop 14"
type: "proposition"
title: ""
section: "Core 08 Capability what optimization pressure does"
order: 43
layer: "explanation"
tier: ["4 (E)", "—"]
assumes: ["Hyp E"]
status: "proved"
depends_on: ["Lemma 5.1", "Def 13", "Def 3"]
mentions: []
checks: ["V08", "V33"]
sources: ["src Price 1970", "src Robertson 1966"]
aliases: ["Proposition 14", "Prop. 14"]
updated: "2026-09-26"
---
# Prop 14
<!-- gen:header -->
> [!abstract] Proposition · tier 4 (E) / — · assumes [[Hyp E]] · proved · in [[Core 08 Capability what optimization pressure does]]
<!-- /gen:header -->

## Statement

**Proposition 14.** Let `F` be non-constant.
(i) `g` is strictly decreasing in `β`, with `g'(β) = −Var_{p*}(F)`: Lemma 5.1 with `G = F`. *(A statement about the
intended behaviour only, in the measurement layer; since R7-3 it is proved there.)*
(ii) *[Assumes (E), in (ii)–(iii).]* `T'(0) = −Cov_q(F̂, F)` and `ΔF'(0) = −Cov_q(E, F)`. So `ΔF(β) = −β·Cov_q(E,F) + O(β²)`, which has
either sign.
(iii) `lim_{β→∞} T(β) = max F − E_{q(·|argmax F̂)}[F]`, which is 0 iff `argmax F̂ ⊆ argmax F`.

## Proof

*Proof.* `d/dβ E_{p_{G,β}}[F] = Cov_{p_{G,β}}(G, F)`; evaluate at `G = F`, and at `β = 0`, where
`p_{G,0} = q`. (iii) `p_{F̂,β} → q(·|argmax F̂)`. ∎

## Notes and checks

*Check.* [[V08|V8]], for (ii)–(iii): `T'(0)` to `4·10⁻⁵` (finite difference), the limit to `4·10⁻⁶`. Part (i) is
Lemma [[Lemma 5.1|5.1]] and is checked by [[V33]]. *(Until R7-3 this note read "V8: derivative to `4·10⁻⁵`", which
suggested that (i) was covered. It was not.)*

> **Neither "capacity is good" nor "capacity is dangerous" holds in general.** Whether more optimization
> helps at first is the sign of the covariance between evaluator and intent under the reference. Whether it
> helps in the end is whether the evaluator's top behaviours are among the intent's.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 3]] — regrets
- [[Def 13]] — actor models; R7-1
- [[Lemma 5.1]] — form of the capacity actor

## Used by
- [[B03]] — Goodhart variants — Manheim & Garrabrant (2018)
- [[B05]] — When does optimizing a proxy help at all? — Laidlaw et al.; Holmström & Milgrom (1991)
- [[B07]] — Ashby (requisite variety); Conant & Ashby (good regulator)
- [[B11]] — Quantitative genetics — selection on a proxy trait *(new in v6.1)*
- [[C06]] — What optimization pressure does (Prop. 14)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[Prop 22]] — the first-order effect of any smooth optimizer; tier 1, v6.3

## Mentions
- none

## Mentioned in
- [[Lemma 5.1]] — form of the capacity actor
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave
- [[Prop 20]] — Goodhart as a covariance — any optimizer; tier 1

## Checks
- [[V08]]
- [[V33]]

## Sources
- [[src Price 1970]]
- [[src Robertson 1966]]

## Retractions touching this note
- [[R038]]
- [[R076]]
<!-- /gen:links -->
