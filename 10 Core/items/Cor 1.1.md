---
id: "Cor 1.1"
type: "corollary"
title: ""
section: "Core 02 The identity"
order: 7
layer: "explanation"
tier: ["4 (E)"]
assumes: ["Hyp E"]
status: "proved"
depends_on: ["Thm 1", "Def 3"]
mentions: []
checks: []
sources: []
aliases: ["Corollary 1.1", "Cor. 1.1"]
updated: "2026-09-26"
---
# Cor 1.1
<!-- gen:header -->
> [!abstract] Corollary · tier 4 (E) · assumes [[Hyp E]] · proved · in [[Core 02 The identity]]
<!-- /gen:header -->

## Statement

**Corollary 1.1.** *[Assumes (E).]* `R_J = 0` iff `E` is constant on `X`.

## Proof

*Proof.* By Thm 1, `R_J = 0` iff `p̂ = p*`. Under (E), `p̂ ∝ p*·e^{βE}` and `p*` has full support, so `p̂ = p*` iff
`βE` is constant. ∎

## Notes and checks

*Note (R7-3).* Part (a) of v6.6–v7.1 — for any actual behaviour, `R_J ≥ 0` with equality iff `p̂ = p*` —
now closes Thm [[Thm 1|1]], in the measurement layer. What remains here needs the evaluator.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 3]] — regrets
- [[Thm 1]] — regret is a divergence

## Used by
- [[C01]] — The regret identity (`A_core.md` Thm 1, Cors 1.1–1.4)

## Mentions
- none

## Mentioned in
- [[Def 3]] — regrets

## Checks
- none

## Sources
- none

## Retractions touching this note
- [[R076]]
<!-- /gen:links -->
