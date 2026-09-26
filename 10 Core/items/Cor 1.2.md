---
id: "Cor 1.2"
type: "corollary"
title: "the optimality gap is a symmetric divergence"
section: "Core 02 The identity"
order: 8
layer: "explanation"
tier: ["4 (E)"]
assumes: ["Hyp E"]
status: "proved"
depends_on: []
mentions: []
checks: []
sources: []
aliases: ["Corollary 1.2", "Cor. 1.2"]
updated: "2026-09-26"
---
# Cor 1.2 — the optimality gap is a symmetric divergence
<!-- gen:header -->
> [!abstract] Corollary · tier 4 (E) · assumes [[Hyp E]] · proved · in [[Core 02 The identity]]
<!-- /gen:header -->

## Statement

**Corollary 1.2 (the optimality gap is a symmetric divergence).** *[Assumes (E).]* The v5 "exact form" satisfies

```
E_{p̂}[E] − E_{p*}[E] = (1/β)·[ KL(p̂‖p*) + KL(p*‖p̂) ].
```

## Proof

*Proof.* `log(p̂/p*) = βE − log E_{p*}e^{βE}`. Take expectations under `p̂` and `p*` and subtract. ∎

## Notes and checks

So the v5 inequality `R_J ≤ E_{p̂}E − E_{p*}E` is the statement `KL ≤ KL + KL_reverse`, and its slack is
exactly `(1/β)·KL(p*‖p̂)`.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- none

## Used by
- [[C01]] — The regret identity (`A_core.md` Thm 1, Cors 1.1–1.4)
- [[Prop 7]] — a bound with realized travel from the reference

## Mentions
- none

## Mentioned in
- none

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
