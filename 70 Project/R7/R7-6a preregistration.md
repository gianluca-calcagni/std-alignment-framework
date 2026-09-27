---
id: "R7-6a preregistration"
type: "report"
updated: "2026-09-27"
---
# R7-6a — pre-registration: intensity caps and distributional targets (written before any R7-6a computation)

**Seen before.** The go/no-go probe ([[R7-6 go-no-go]], `r76_probe.py`) computed, on 300 instances, the linear and
path free measures for collapsed, over-diffuse and random behaviours, and checked the path of `−KL(·‖p_T)` against a
generic optimizer (to `1.1·10⁻⁵`). Checks repeating those are marked **(R)**. Nothing below has been computed.

## Definitions under test (measurement layer)

**Def. 18 (intensity cap).** For a cardinal target `[F]₊`, a declared **cap** is a point `p^max = p_{F,s}` of the
half-ray, `s ∈ (0, ∞]` (`s = ∞`: no cap). Being a point, it needs no unit. The **capped intent segment** is
`𝓡⁺_F(p^max) = {p_{F,t} : 0 ≤ t ≤ s}`. With `k = KL(p̂‖q)` and `k_s = KL(p^max‖q)`:
- `M_free^cap = inf over the segment of KL(p̂‖p)`;
- `M_budget^cap = KL(p̂‖p_{F,λ})` with `λ` the budget match if `k ≤ k_s`, and `KL(p̂‖p^max)` if `k > k_s`: past the cap,
  the intended behaviour is the cap itself.

A **distributional target** `p_T` (full support) is the cap `p^max = p_T` on `F = log(p_T/q)` (`s = 1` in that unit).
The contract's M5 becomes: "`p̂ = p_{G,t}` for some `G ∈ 𝒯`, at an intensity within the declared cap, implies `M = 0`".

## Claimed results (Prop. 33)

- (a) `M_free^cap = M(min(t̂⁺, s))`, with `M(t) = KL(p̂‖p_{F,t})` and `t̂⁺` as in Thm 13.
- (b) If `t̂ > s`: `M_free^cap = D_⊥ + KL(p_{F,t̂}‖p^max)` — transverse error plus an **overshoot** term.
- (c) Both capped measures satisfy M1–M4, the capped M5, M6 and M8; `M_free^cap ≤ M_budget^cap`; with `s = ∞` they are
  Def. 10's measures (M7), and `M_budget^cap` keeps Def. 10's saturation rule.
- (d) For `U(p) = −KL(p‖p_T)`: `argmax_p [U(p) − KL(p‖q)/t] = p_{F, t/(1+t)}`, `F = log(p_T/q)`; so the regularized path of
  `U` is the capped segment with `p^max = p_T`.

## Check V36 (seeded), and predictions

600 instances: `n` uniform on `{3, …, 12}`, `q` and `p_T` Dirichlet(1) with minimum ≥ `10⁻³`, `F = log(p_T/q)` (cap `s = 1`),
plus 300 with a random `F ~ N(0, I)` and `s ~ U(0.2, 5)`. Behaviours: random Dirichlet; on-segment `p_{F,t}`, `t ≤ s`;
overshoot `p_{F,t}`, `t ∈ (s, 4s]`; off-ray reweightings of overshoots.

| # | Claim | Prediction | Falsified if |
|---|---|---|---|
| P1 | (a) | the closed form equals a 400-point grid plus bounded minimization over `[0, s]` | a difference above `10⁻⁹` |
| P2 | (b) | the decomposition holds whenever `t̂ > s` | above `10⁻¹⁰` |
| P3 | (c), M1, capped M5 | on-segment behaviours score `≤ 10⁻¹⁰` on both capped measures; overshoots and off-ray behaviours score `> 10⁻⁹` | any exception |
| P4 | (c), M3 | both capped measures unchanged under `F ↦ aF + c`, `s ↦ s/a` | above `10⁻⁹` |
| P5 | (c), order and M7 | `M_free^cap ≤ M_budget^cap + 10⁻¹⁰`; with `s = ∞`, both equal Def. 10's measures | any violation; above `10⁻¹⁰` |
| P6 | (d) | the closed-form path matches a generic optimizer | above `10⁻⁴` (optimizer-limited; the probe saw `1.1·10⁻⁵`) |
| P7 (R) | the defect | collapsed agents `p_{F,t}`, `t ∈ (1, 10]`, on distributional targets: uncapped `M_free ≤ 10⁻¹⁰`; capped `M_free^cap = KL(p̂‖p_T)` to `10⁻¹⁰` and `> 10⁻⁹` | any exception |

**Decision rules.** D1: a failed proof-backed prediction (P1–P5, P7's equality) means the statement is wrong, not the
check; it is recorded, and a corrected statement is a new result. D2: if lint or M7 fails, restore Def. 11 and stop.
**Falsifier of the step's purpose:** if an on-segment (under-pursuing) agent is charged, or a collapsed agent is not,
the cap does not capture "intensity as the principal's declaration".
