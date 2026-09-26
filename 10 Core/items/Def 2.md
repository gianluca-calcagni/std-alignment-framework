---
id: "Def 2"
type: "definition"
title: "the bounded actor"
section: "Core 01 Setting"
order: 3
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: []
mentions: ["Thm 1"]
checks: []
sources: ["src Dupuis 1997", "src Ortega 2013"]
aliases: ["Definition 2", "Def. 2"]
updated: "2026-09-26"
---
# Def 2 — the bounded actor
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 01 Setting]]
<!-- /gen:header -->

## Statement

**Definition 2 (the bounded actor).** For `β < ∞`,

```
J_G(p) = E_p[G] − (1/β)·KL(p ‖ q)
```

and for `β = ∞`, `J_G(p) = E_p[G]`.

## Notes and checks

*Note.* By Thm [[Thm 1|1]] (the Gibbs variational principle), for `β < ∞` the unique maximizer of `J_G` over `Δ(X)` is
`p_{G,β}`, with `max J_G = (1/β)·log E_q e^{βG}`.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- none

## Used by
- [[B07]] — Ashby (requisite variety); Conant & Ashby (good regulator)
- [[B09]] — Turner et al. — power as attainable utility
- [[B12]] — Human choice — logit, defaults, rational inattention, present bias *(new in v6.2)*
- [[Cor 17.1]] — the capacity actor's regret is the budget convention
- [[Def 3]] — regrets
- [[Def 5]] — capacity actor
- [[Def 15]] — the capacity model; R7-3
- [[Lemma 5.1]] — form of the capacity actor
- [[Thm 1]] — regret is a divergence
- [[Thm 5]] — the width is the exact worst case

## Mentions
- [[Thm 1]] — regret is a divergence

## Mentioned in
- none

## Checks
- none

## Sources
- [[src Dupuis 1997]]
- [[src Ortega 2013]]

## Retractions touching this note
- none
<!-- /gen:links -->
