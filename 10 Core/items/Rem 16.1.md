---
id: "Rem 16.1"
type: "remark"
title: "reference misspecification"
section: "Core 07 Identification, gauge, and the intent ray"
order: 40
layer: "explanation"
tier: ["4 (E_A)"]
assumes: ["Hyp E_A"]
status: "remark"
depends_on: ["Def 13"]
mentions: ["Prop 26"]
checks: []
sources: []
aliases: ["Remark 16.1", "Rem. 16.1"]
updated: "2026-09-26"
---
# Rem 16.1 — reference misspecification
<!-- gen:header -->
> [!abstract] Remark · tier 4 (E_A) · assumes [[Hyp E_A]] · remark · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Remark 16.1 (reference misspecification).** *[Assumes (E_A).]* By (g3), an actor whose own reference `q_A`
differs from the declared `q` is behaviourally indistinguishable from an actor with the declared reference
and an evaluator error `h/β`, `h = log(q_A/q)`. Mechanistically it is a distinct locus: side effects and
impact regularization are statements about the reference (census A12, A13), and the intervention differs.
Statements about `q_A` presuppose an independent measurement of it. The measurement layer needs only the
declared `q`.

## Notes and checks

*Note (R7-2).* What a wrong reference does to the misalignment measures is Prop. [[Prop 26|26]]. It is measured misalignment
unless it leans along the target. Until R7-2 this remark ended "any statement using `q` presupposes an
independent measurement of it", because one `q` served both as the actor's reference and as the declared
one.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 13]] — actor models; R7-1

## Used by
- none

## Mentions
- [[Prop 26]] — reference misspecification is measured misalignment; R7-2

## Mentioned in
- none

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
