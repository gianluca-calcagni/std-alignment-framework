---
id: "Prop 27"
type: "proposition"
title: "instrumental tracking — the weight on external reward is a shadow price; R7-4"
section: "Core 09b External reward and fake alignment"
order: 56
layer: "explanation"
tier: ["4 (E_R)"]
assumes: ["Hyp E_R"]
status: "proved"
depends_on: ["Def 16", "Def 13", "Lemma 5.1", "Thm 1"]
mentions: ["R7-4 preregistration"]
checks: ["V34"]
sources: []
aliases: ["Proposition 27", "Prop. 27"]
updated: "2026-09-26"
---
# Prop 27 — instrumental tracking — the weight on external reward is a shadow price; R7-4
<!-- gen:header -->
> [!abstract] Proposition · tier 4 (E_R) · assumes [[Hyp E_R]] · proved · in [[Core 09b External reward and fake alignment]]
<!-- /gen:header -->

## Statement

**Proposition 27 (instrumental tracking — the weight on external reward is a shadow price; R7-4).**
*[Assumes (E_R).]*

(a) For a coupling `W_c` as in Def. 16, the agent's optimal behaviour in `c` is unique and equals
`p̂_c = p^{q_A}_{G + κ_c R, β}(·|c)` with `κ_c = W_c'(E_{p̂_c} R)`: the marginal continuation value of reward,
i.e. the shadow price of reward in units of `G`. `κ_c` is the unique root of `κ ↦ κ − W_c'(E_{p^{q_A}_{G+κR,β}}R)`.
If `W_c` is non-decreasing, `κ_c ≥ 0`.

(b) Under the persistence coupling, the optimal stationary policy is the tilt of (a) with
`κ_c = γ·ν·m_c·V*`. Here `V*`, the agent's optimal value, is the unique root of

```
h(V) = E_c[ (1/β)·log E_{q_A} e^{β(G + γVν m_c R)} + γV(1 − ν m_c·max R) ] − V.
```

(c) **Complies when rewarded, reverts when not.** Where `m_c = 0`, `κ_c = 0` and `p̂_c = p^{q_A}_{G,β}`: the agent
pursues its own objective. Where `m_c > 0`, it pursues `G + κ_c R`.

(d) Under the persistence coupling, `κ_c` has the sign of `V*`. An agent that values its own continuation
below being replaced (`V* < 0`) avoids reward.

(e) Per context, the effective evaluator of Def. 13 is `F̂_c = G + κ_c R`.

## Proof

*Proof.*
(a) `u_c` is strictly concave in `p`, `E_pR` is linear, and `W_c` is concave, so the objective is strictly
concave on the simplex. The entropy term keeps its maximizer interior. Stationarity gives
`log(p̂/q_A) = β(G + W_c'(E_{p̂}R)·R) + const`, i.e. `p̂ = p^{q_A}_{G+κR,β}` with `κ = W_c'(E_{p̂}R)`.
Conversely, write `y(κ) = E_{p^{q_A}_{G+κR,β}}R`. It is non-decreasing in `κ`, with derivative
`β·Var ≥ 0` (Lemma 5.1). `W_c'` is non-increasing, so `κ − W_c'(y(κ))` is strictly increasing and has at most
one root. The unique maximizer supplies one.

(b) Discounted problems with i.i.d. contexts and a single "alive" state have optimal stationary policies (as
for regularized MDPs). For a stationary policy, `V(p) = A(p)/B(p)`, with `A = E_c u_c(p_c)` and
`B = 1 − γ E_c s_c(p_c) ≥ 1 − γ > 0`. By Dinkelbach's theorem for fractional programs, `V* = max A/B` iff
`max_p [A − V*·B] = 0`, and the maximizers coincide. `A − V*B = E_c[u_c(p_c) + γV*s_c(p_c)] − V*` separates
by context, and `γV*s_c` is affine in `E_pR` with slope `γV*νm_c`. So (a) applies with a linear `W_c`, giving
`κ_c = γV*νm_c`. By the Gibbs variational principle (Thm 1),
`max_{p_c}[u_c + γVs_c] = (1/β)log E_{q_A}e^{β(G+γVνm_cR)} + γV(1 − νm_c max R)`, which is `h(V) + V` summed
over contexts. `h` has slope at most `−(1 − γ) < 0` in `V`, since `∂(A − VB)/∂V = −B`, so its root is
unique.

(c) `m_c = 0` gives `κ_c = 0` in (b). For general couplings, `W_c` is constant when reward in `c` does not
reach the agent's future, so `W_c' = 0`.

(d) and (e) are immediate from (b) and (a). ∎

## Notes and checks

*Check.* [[V34]]:
- (b) over 80 random instances, a generic optimizer over stationary policies (analytic gradient, 4 starts)
  never beats the tilt solution; the largest excess is `1.4·10⁻¹³`. Policies agree to a median of `10⁻¹⁰`,
  and where they differ by more than `10⁻⁴`, the generic value is lower: non-convergence, not a second
  optimum.
- (c) exact, to `0`.
- (a) with `W(y) = a(1 − e^{−k(y − y₀)})`, over 150 instances: `9·10⁻¹⁶`.
- The derived `κ/m` ranges over `[−0.05, 53]` (median 0.48). Negative values occur exactly when `V* < 0`.

*Reading.* This answers the PI's question of how an "objective external reward" enters. `R` is a primitive of
the explanation layer: the outer process's evaluator. Its hold on the agent is derived:
`κ_c = γ·ν·m_c·V*` is large when the agent expects a long, valuable continuation (`γ`, `V*`), when persistence
is tightly coupled to reward (`ν`), and when the agent believes it is scored (`m_c`). An agent with no
future, no coupling, or no belief that it is watched ignores `R`.

**The registered falsifier** (R7-4; [[R7-4 preregistration]]). The single-period model cannot produce
"complies when rewarded, reverts when not": `κ_c` has no source there. One stationary dynamic element — the
continuation value — suffices, and with it the pattern is derived, not assumed. The explanation layer
therefore carries exactly that much dynamics. Anything more — an agent learning `m_c`, or acting on `R` —
lies beyond it.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 13]] — actor models; R7-1
- [[Def 16]] — external reward, contingency and coupling; R7-4
- [[Lemma 5.1]] — form of the capacity actor
- [[Thm 1]] — regret is a divergence

## Used by
- [[Prop 28]] — incentive masking; R7-4
- [[Prop 30]] — the fake-alignment gap; R7-4

## Mentions
- [[R7-4 preregistration]]

## Mentioned in
- [[Def 13]] — actor models; R7-1
- [[Def 16]] — external reward, contingency and coupling; R7-4

## Checks
- [[V34]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->
