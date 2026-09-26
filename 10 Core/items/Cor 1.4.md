---
id: "Cor 1.4"
type: "corollary"
title: "historical note: why v5 found \"tight to about 2×\""
section: "Core 02 The identity"
order: 10
layer: "explanation"
tier: ["4 (E)"]
assumes: ["Hyp E"]
status: "historical"
depends_on: ["Def 3"]
mentions: []
checks: ["V01"]
sources: []
aliases: ["Corollary 1.4", "Cor. 1.4"]
updated: "2026-09-26"
---
# Cor 1.4 — historical note: why v5 found "tight to about 2×"
<!-- gen:header -->
> [!abstract] Corollary · tier 4 (E) · assumes [[Hyp E]] · historical · in [[Core 02 The identity]]
<!-- /gen:header -->

## Statement

**Corollary 1.4 (historical note: why v5 found "tight to about 2×").** *[Assumes (E).]* 

```
R_J / (E_{p̂}E − E_{p*}E) = ∫₀^β t·V(t) dt / (β·∫₀^β V(t) dt)  ∈ (0, 1),
```

the `V`-weighted mean of `t/β` on `[0, β]`. It tends to `1/2` as `E → 0` (then `V` is nearly constant), and
exceeds `1/2` iff `∫₀^β (t − β/2)·V(t) dt > 0`, i.e. iff the error's variance is larger, on average, on the
second half of the tilt path.

## Notes and checks

*Check.* [[V01|V1]]: p5/p50/p95 = 0.185 / **0.482** / 0.682, range [0.034, 0.937]. The v5 median 0.48 was this
symmetry, not a tightness property.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 3]] — regrets

## Used by
- [[C01]] — The regret identity (`A_core.md` Thm 1, Cors 1.1–1.4)

## Mentions
- none

## Mentioned in
- none

## Checks
- [[V01]]

## Sources
- none

## Retractions touching this note
- [[R031]]
<!-- /gen:links -->
