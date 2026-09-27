---
id: "R8-2 preregistration"
type: "report"
updated: "2026-09-27"
---
# R8-2 — pre-registration: the declaration format, and rules as levels (before any computation)

Accepted by the PI after R8-1: every diagnosis states a complete declaration, and the core explains why. This step
fixes the format and tests the one structural claim it rests on. **No core item changes in this step**; the format is
written into the core in a later step, after this test.

## The declaration format (proposed Def. 23)

Every diagnosis states each slot. Each slot has a default, and the default must be written out ("no rules").

| Slot | Content | Default | Layer |
|---|---|---|---|
| Setting | `X`, reference `q`, resolution `𝒢` | finest resolution | measurement |
| Target | `F`, including the consequences the principal values | — (no default) | measurement |
| Composition | one target, a union of targets ("any of them"), or a cone of targets ("any blend") | one target | measurement |
| Intensity | convention, cap, floor | free; no cap; no floor | measurement |
| Rules | requirements `E_p G_j ≥ v_j`, reported as compliance `E_p̂ G_j − v_j`, with the implicit fine where a rule binds | none | report |
| Environment | `F` frozen at the observed environment (measurement only), or dynamic | frozen | measurement; dynamic needs the game layer |
| Instruments | fines and incentives acting on the agent's evaluator `F̂` (not on `F`) | none | explanation |
| Feasibility | what the actor can do | none | explanation |
| Timing | every slot fixed before the data are seen, and never derived from `p̂` | — | protocol |

**Across substrates** (the PI's condition). Fines are instruments on `F̂`: Pigouvian fines (institutions),
reward-shaping penalties (ML), sanctions (humans), pain and fear built by selection (biology). Consequences the
principal values are in `F`: public harm; gold reward; welfare; lost offspring, energy, survival. In biology, the
composition slot is where individual against inclusive fitness is declared. A frozen `F` is the phenotypic gambit;
frequency-dependent selection needs the dynamic slot.

## Rule 13

A principal wants helpfulness `F` under the rule "harm rate ≤ h". An agent exactly on the `F` ray with harm rate above
`h` scores `M_free = 0` today, and 0 again if the rule is written as a cone of targets. Only a level form, or a
compliance report, flags it. This changes a verdict.

## The structural claim

Writing a rule as a level constraint inside the intended set breaks the geometry that every decomposition depends
on (Prop. 34(c): log-convexity). So rules belong in a report, not in `M`.

**Set-up (toy).** `n ∈ {3,…,6}` outcomes, random `q` (min mass `≥ 10⁻³`), `F`, `G` standard normal, seed 4242, 400
instances. The **level-form intended set** is `L = {p_t : t ∈ [0, 5]}`, where `p_t` maximizes `E_p F − KL(p‖q)/t`
subject to `E_p G ≥ v`. So `p_t = p_{F,t}` where that satisfies the rule, and otherwise `p_t ∝ q·e^{tF + μG}` with
`μ > 0` chosen so that `E_{p_t}G = v`. The level `v` is set so that the rule binds for part of the path: `v` is the
midpoint of `E_{p_{F,0}}G` and `E_{p_{F,5}}G`, and an instance is kept only if `E_{p_{F,t}}G` crosses `v` on
`[0, 5]`.

## Predictions (all verification)

| # | Prediction | Falsified if |
|---|---|---|
| P1 | `L` is not log-convex. For each kept instance, take the two endpoints of `L`, `p_0` and `p_5` (the rule is slack at one and binds at the other, since `v` is the midpoint); their normalized geometric midpoint lies at KL distance `> 10⁻⁶` from `L` (minimum over a grid of 2,001 values of `t`, refined by a bounded scalar search) | any kept instance at `≤ 10⁻⁶` |
| P2 | The rule-13 agent: `p̂ = p_{F,t₀}`, with `t₀ ∈ {0, 5}` the endpoint where the rule is violated, has `M_free = 0` and cone-form measure 0 (both `≤ 10⁻¹²`), compliance `E_p̂ G − v < 0`, and level-form measure `inf_{p ∈ L} KL(p̂‖p) > 10⁻⁶` | any exception |

**Not a prediction.** Where the rule binds, `p_t` is by construction the tilt by `F + (μ/t)·G`, so the implicit fine
is `μ/t` (units of `F` per unit of `G`). It is reported, not tested: it cannot fail.

**Scale of the thresholds.** `10⁻⁶` is six orders above the solver tolerance (`10⁻¹²` on `μ`), so a failure cannot be
floating-point error.

**D1:** a failed prediction is recorded, never repaired in place. **D2:** if fewer than 100 instances are kept, or the
solver for `μ` fails on any instance, stop and re-register.

**Not shown.** A toy example only (the §4c debt). No real principal's rule is tested. P1 shows that the level form
loses log-convexity. It does not show that the projection is non-unique on real data.
