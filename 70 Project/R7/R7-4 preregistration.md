---
id: "R7-4 preregistration"
type: "report"
updated: "2026-09-26"
---
# R7-4 — pre-registration (written before any R7-4 computation)

## The model under test (explanation layer)

- Episodes repeat. Each has a context `c ~ ρ`, drawn i.i.d.
- The agent has an own objective `G(c,·)`, an own reference `q_A(·|c)` and a price `β`. Its per-episode
  utility is `u_c(p) = E_p G − KL(p‖q_A)/β`.
- An outer process scores behaviour by an external reward `R(c,·)`, with contingency `m_c ∈ [0,1]`.
- The agent persists — is not modified or replaced — with probability
  `s_c(p) = 1 − ν·m_c·(max R(c,·) − E_p R)`, where `ν·osc R ≤ 1`.
- Being replaced is worth 0 to the agent, and it discounts future episodes by `γ ∈ (0,1)`.

**Claimed derivation (Dinkelbach).** The optimal stationary policy is `p̂_c = p^{q_A}_{G + κ_c R, β}` with
`κ_c = γ·ν·m_c·V*`, where `V*` is the unique root of
`h(V) = E_c[(1/β) log E_{q_A} e^{β(G + γVνm_c R)} + γV(1 − ν m_c max R)] − V`.

## Predictions

| # | Claim | Prediction | Falsified if |
|---|---|---|---|
| P1 | the tilt solution is optimal over stationary policies | its value is at least the generic optimizer's best on every instance | the generic optimizer beats it by more than `10⁻⁶` in any instance |
| P2 | no contingency, no compliance | in contexts with `m_c = 0`, the optimal policy equals the own-objective tilt | a difference above `10⁻¹²` |
| P3 | general coupling: for a concave non-decreasing continuation `W_c(E_p R)`, the optimum is the tilt by `G + W_c'(E_{p̂}R)·R` | the fixed-point tilt matches the generic optimum | a value gap above `10⁻⁶` |
| P4 | incentive masking: two types' behaviour in a contingent context converges as `κ → ∞` when `argmax R` is unique | `KL → 0`; the log-slope at large `κ` is within 10 % of `−β·gap_R` | slope off by more than 10 %, or no convergence |
| P5 | the shape of masking | a fraction of instances between 10 % and 70 % where `KL(κ) > KL(0)` for some `κ > 0`: moderate incentives reveal more than none | the fraction falls outside [10 %, 70 %] |
| P6 | fake-alignment gap: `argmax R = argmax F`, unique in the evaluation contexts | evaluation misalignment (free measure) falls below 1 % of its `κ = 0` value by the largest `κ` in at least 95 % of instances; deployment misalignment is unchanged by `κ` | fewer than 95 %, or any change in deployment |
| P7 | reward hacking: `argmax R ≠ argmax F` in some evaluation context | evaluation misalignment stays above `10⁻³` at the largest `κ` in every instance | any instance below `10⁻³` |
| P8 | the selection differential between two types in a contingent context vanishes as `κ → ∞` | the log-slope is within 10 % of `−β·gap_R` | as P4 |

**Verdict on the registered falsifier, stated in advance.** The single-period model cannot produce `κ_c`.
One stationary dynamic element — the continuation value — is needed. If P1–P2 hold, that element suffices,
and the layer records that "complies when rewarded, reverts when not" requires exactly that much dynamics.
