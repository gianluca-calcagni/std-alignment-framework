---
id: "Thm 1"
type: "theorem"
title: "regret is a divergence"
section: "Core 02 The identity"
order: 6
layer: "measurement"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Def 2", "Def 3"]
mentions: ["Prop 15"]
checks: ["V01", "V27"]
sources: ["src Dupuis 1997", "src Korbak 2022"]
aliases: ["Theorem 1", "Thm. 1"]
updated: "2026-09-26"
---
# Thm 1 — regret is a divergence
<!-- gen:header -->
> [!abstract] Theorem · tier 1 · proved · in [[Core 02 The identity]]
<!-- /gen:header -->

## Statement

**Theorem 1 (regret is a divergence).** For `β < ∞` and every distribution `p` on `X`,

```
J_F(p*) − J_F(p) = (1/β)·KL(p ‖ p*).
```

In particular **`β·R_J = KL(p̂ ‖ p*)`**, so `R_J ≥ 0`, with equality iff `p̂ = p*`.

## Proof

*Proof.* `log p* = log q + βF − log Z`, `Z = E_q e^{βF}`. Hence
`KL(p‖p*) = KL(p‖q) − β·E_p F + log Z = β·[(1/β)log Z − J_F(p)] = β·[J_F(p*) − J_F(p)]`. ∎

## Notes and checks

*Check.* [[V01|V1]]: max `|β·R_J − KL(p̂‖p*)| = 4.8·10⁻¹⁴` over 20,000 random instances.

**The actual actor is arbitrary.** Only `p*` is the Gibbs actor. So `β·R_J = KL(p̂‖p*)` holds for best-of-n,
for a policy-gradient iterate, or for any behaviour whatever, with `R_J` read as the free-energy regret at the
declared price. *([[V27]]: 4,222 non-tilt actors, to `2·10⁻¹⁴`; R6 checked 18,003 KL-penalized policy-gradient
iterates, to `3·10⁻¹⁴`.)*

*Prior art.* This is the Gibbs variational principle. For KL-regularized reward maximization it is the
known equivalence with reverse-KL minimization toward the Gibbs policy (Korbak et al., NeurIPS 2022;
Korbak, Perez & Buckley, Findings of EMNLP 2022), used routinely in RLHF theory (e.g. Zhao et al. 2024).
Applying it to the misspecified actor is immediate. Prop. [[Prop 15|15]] shows it is the entropic case of a Bregman
identity.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 2]] — the bounded actor
- [[Def 3]] — regrets

## Used by
- [[B01]] — Anchor
- [[B07]] — Ashby (requisite variety); Conant & Ashby (good regulator)
- [[C01]] — The regret identity (`A_core.md` Thm 1, Cors 1.1–1.4)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[C14]] — Does the arrangement have content? *(successor to v5 A9; answered in R3)*
- [[Cor 1.1]]
- [[Cor 1.5]] — stacked stages compose additively
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave
- [[Prop 18]] — harm bounds detectability
- [[Prop 19]] — the evaluation gap
- [[Prop 27]] — instrumental tracking — the weight on external reward is a shadow price; R7-4
- [[Thm 13]] — intent-ray decomposition
- [[Thm 17]] — every regret notion is a point on one convex curve

## Mentions
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave

## Mentioned in
- [[Def 2]] — the bounded actor
- [[Prop 24]] — the v6.4 measures against the contract; tier 1

## Checks
- [[V01]]
- [[V27]]

## Sources
- [[src Dupuis 1997]]
- [[src Korbak 2022]]

## Retractions touching this note
- [[R035]]
- [[R068]]
- [[R077]]
<!-- /gen:links -->
