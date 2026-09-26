---
id: "Prop 15"
type: "proposition"
title: "the identity for any convex regularizer and any target that keeps the objective concave"
section: "Core 02 The identity"
order: 11
layer: "measurement"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Thm 1"]
mentions: ["Cor 1.3", "Cor 1.5", "Prop 14", "Prop 18", "Prop 19", "Prop 2", "Prop 3", "Prop 4", "R078", "Thm 13", "Thm 17"]
checks: ["V12", "V29"]
sources: []
aliases: ["Proposition 15", "Prop. 15"]
updated: "2026-09-26"
---
# Prop 15 — the identity for any convex regularizer and any target that keeps the objective concave
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 02 The identity]]
<!-- /gen:header -->

## Statement

**Proposition 15 (the identity for any convex regularizer and any target that keeps the objective concave).**
Let `φ` and `U` be functions on `Δ(X)` such that `Ψ = φ/β − U` is convex. For instance, `φ` convex and `U`
concave — but `U` need not be concave (v6.4; [[V29]]). Let `J(p) = U(p) − φ(p)/β`, let `p*` maximize `J` over
`Δ(X)`, and let `Ψ` be differentiable at `p*`. Then for every `p`:

```
J(p*) − J(p) = B_Ψ(p, p*) − ⟨∇J(p*), p − p*⟩  ≥  B_Ψ(p, p*),
```

where `B_Ψ(p, p*) = Ψ(p) − Ψ(p*) − ⟨∇Ψ(p*), p − p*⟩` is the Bregman divergence. Equality holds when `p*` is
in the relative interior of `Δ(X)`. In particular, **any** actual behaviour `p̂` — whether or not it optimizes
anything — has regret at least `B_Ψ(p̂, p*)`, with equality when `p*` is interior.

| Case | `B_Ψ(p, p*)` |
|---|---|
| `U(p) = E_pF`, `φ = KL(·‖q)` | `KL(p‖p*)/β` — Theorem [[Thm 1\|1]] |
| `U(p) = E_pF`, `φ = χ²(·‖q)` | `Σ_x (p − p*)²/(β q)`; the optimum may lie on the boundary |
| `U(p) = E_pF − κ(E_pG)²`, `φ = KL(·‖q)` | `KL(p‖p*)/β + κ(E_pG − E_{p*}G)²` — a concave target that cannot be written as `E_p` of any function |

## Proof

*Proof.* `J = −Ψ`, so `J(p*) − J(p) = Ψ(p) − Ψ(p*) = B_Ψ(p,p*) + ⟨∇Ψ(p*), p − p*⟩`, and
`∇Ψ = −∇J`. At a maximum of a concave function over a convex set, `⟨∇J(p*), p − p*⟩ ≤ 0` for all `p`. If `p*` is
in the relative interior, first-order optimality makes `∇J(p*)` a constant vector, and `Σ_x (p − p*)(x) = 0`,
so the term vanishes. ∎

## Notes and checks

*Check.* [[V29]] checks a non-concave `U` with convex `Ψ`, to `2·10⁻¹⁵`. [[V12]]:
- χ²: equality to `4.5·10⁻¹³` on 961 interior optima, and `≥` with no violation on 3,039 boundary optima;
- concave target: to `6.7·10⁻¹⁵`.

*Tier (R7-3).* Only the **intended** behaviour must be an exact regularized optimum; the actual behaviour is
arbitrary. So this is tier 1 in the actual actor, like Thm [[Thm 1|1]]. *(Filed as the whole of "tier 3" until R7-3;
[[R078|row 78]].)* The v6.6–v7.1 statement ended "the actual actor `p̂ = argmax [Û − φ/β]` has regret at
least …", which read as a hypothesis on `p̂`. It was only an example.

*Scope.* Props [[Prop 18|18]] and [[Prop 19|19]], and Thms [[Thm 13|13]] and [[Thm 17|17]], use the exponential form of the **intended**
entropic actor. Props [[Prop 2|2]]–[[Prop 4|4]], [[Prop 14|14]](ii)–(iii), and Cors [[Cor 1.3|1.3]] and [[Cor 1.5|1.5]] use it for the actual actor
too, under (E). For Props [[Prop 18|18]]–[[Prop 19|19]], the Chernoff bound `C ≤ KL(p̂‖p*)` survives, but `KL(p̂‖p*)` is no longer
the regret. Prop. 15 is what survives for other regularizers. The Pythagorean identity needs the intent ray to be an exponential family
and does not extend.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Thm 1]] — regret is a divergence

## Used by
- [[C01]] — The regret identity (`A_core.md` Thm 1, Cors 1.1–1.4)

## Mentions
- [[Cor 1.3]] — CGF and integral forms
- [[Cor 1.5]] — stacked stages compose additively
- [[Prop 2]] — sharp error-only bound
- [[Prop 3]] — only the upper tail matters
- [[Prop 4]] — an error confined to one region saturates
- [[Prop 14]]
- [[Prop 18]] — harm bounds detectability
- [[Prop 19]] — the evaluation gap
- [[R078]]
- [[Thm 13]] — intent-ray decomposition
- [[Thm 17]] — every regret notion is a point on one convex curve

## Mentioned in
- [[Thm 1]] — regret is a divergence

## Checks
- [[V12]]
- [[V29]]

## Sources
- none

## Retractions touching this note
- [[R078]]
<!-- /gen:links -->
