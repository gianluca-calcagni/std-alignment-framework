---
id: "Prop 21"
type: "proposition"
title: "no overoptimization under an affine regression — for any actor that sees only the evaluator; tier 1, v6.3"
section: "Core 08 Capability what optimization pressure does"
order: 45
layer: "explanation"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Prop 20", "Def 13"]
mentions: ["B04"]
checks: ["V24"]
sources: []
aliases: ["Proposition 21", "Prop. 21"]
updated: "2026-09-26"
---
# Prop 21 — no overoptimization under an affine regression — for any actor that sees only the evaluator; tier 1, v6.3
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 08 Capability what optimization pressure does]]
<!-- /gen:header -->

## Statement

**Proposition 21 (no overoptimization under an affine regression — for any actor that sees only the
evaluator; tier 1, v6.3).** Suppose that under the reference the regression of target on evaluator is affine,
`E_q[F | F̂] = a + b·F̂`. Suppose also that the actor's weights depend on a behaviour only through its
evaluator value: `w = dp/dq = h(F̂)` for some function `h`. Then

```
E_pF − E_qF = b·(E_pF̂ − E_qF̂).
```

The target moves in fixed proportion to the proxy, so gold reward never turns down while the proxy rises.

Covered actors:
- the Gibbs actor, for any reference;
- threshold (top) selection;
- vanilla policy gradient started from a uniform reference;
- best-of-n with a uniform reference and no ties.

## Proof

*Proof.* By Prop. [[Prop 20|20]], `E_pF − E_qF = Cov_q(w, F) = Cov_q(w, E_q[F|F̂])`, since `w` is a function of `F̂`. That
equals `b·Cov_q(w, F̂) = b·(E_pF̂ − E_qF̂)`. ∎

## Notes and checks

*Note (R7-2: which base measure).* The hypothesis `w = dp/dq = h(F̂)` is stated relative to one base measure,
and the conclusion holds relative to the same one. An optimizer that reweights its own starting point `q_A` by
a function of `F̂` satisfies the proposition with `q := q_A`, and the regression taken under `q_A`. Relative to
the declared `q` its weights also carry `q_A/q`, so the hypothesis can fail there.

*Check.* [[V24]]: Gibbs, top selection, and arbitrary `F̂`-measurable actors, to `3·10⁻¹⁵`. An actor whose
weights use the residual violates it (median 0.55).

*Reading.* This generalizes [[B04|B4]] from the Gibbs path under Gaussian structure to every
evaluator-driven optimizer under any affine regression. **Overoptimization therefore requires either a
regression of target on evaluator that bends, or an optimizer whose weights use information beyond the
evaluator** — for example a non-uniform reference entering a gradient method. The independent review's T-D
(vanilla policy gradient, Gaussian joint, uniform reference: a constant gold-to-proxy ratio) is an instance.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 13]] — actor models; R7-1
- [[Prop 20]] — Goodhart as a covariance — any optimizer; tier 1

## Used by
- [[B04]] — Reward-model overoptimization — Gao, Schulman & Hilton (ICML 2023)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*

## Mentions
- [[B04]] — Reward-model overoptimization — Gao, Schulman & Hilton (ICML 2023)

## Mentioned in
- [[Prop 20]] — Goodhart as a covariance — any optimizer; tier 1

## Checks
- [[V24]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
