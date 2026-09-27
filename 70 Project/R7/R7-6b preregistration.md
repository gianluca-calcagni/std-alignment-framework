---
id: "R7-6b preregistration"
type: "report"
updated: "2026-09-27"
---
# R7-6b — pre-registration: minimum intensity (written before any R7-6b computation)

**Rule 13.** Passes: under a policy "harmful outputs at most 1 %", with target `F = −1_H`, the free and budget measures
score an untouched base model with 5 % harm as perfectly aligned (the ray starts at `q`). **Rule 11:** every prediction is
*verification*. **Seen before:** nothing computed for floors.

## Definitions under test (measurement layer)

**Def. 20 (intended segment: floor and cap).** For `[F]₊`, a declared **floor** `p^min = p_{F,r}` and cap `p^max = p_{F,s}`,
`0 ≤ r ≤ s ≤ ∞` (`r = 0`: no floor; `s = ∞`: no cap). The intended segment is `{p_{F,t} : r ≤ t ≤ s}`, log-convex.
- Free: `M_free^seg = inf over the segment of KL(p̂‖p)`.
- Budget, with `k = KL(p̂‖q)`, `k_r = KL(p^min‖q)`, `k_s = KL(p^max‖q)`: `KL(p̂‖p^min)` if `k < k_r`; the budget match if
  `k_r ≤ k ≤ k_s`; `KL(p̂‖p^max)` if `k > k_s`. **Below the floor, the intended behaviour is the floor.**
- Def. 11's M5: pursuit at an intensity within the declared floor and cap.

## Claimed results (Prop. 35)

- (a) With `t̂` the full-ray moment point (Thm 13) and `t* = min(max(t̂, r), s)`:
  `M_free^seg = KL(p̂‖p_{F,t̂}) + KL(p_{F,t̂}‖p_{F,t*})` — error off the ray, plus undershoot (`t̂ < r`) or overshoot (`t̂ > s`).
- (b) Both measures satisfy M1–M4, M5 within the segment, M6, M8, and `M_free^seg ≤ M_budget^seg`; with `r = 0` they are
  Def. 18's capped measures; with `r = 0, s = ∞`, Def. 10's.
- (c) A threshold policy: for `F = −1_H` and `ε < q(H)`, the floor with `p^min(H) = ε` exists and is unique; the base
  model `p̂ = q` scores `KL(q‖p^min) > 0` on both measures, while it scores 0 without a floor.

## Check V39 (seed 3909), and predictions — all verification

600 instances: `n` in `{3, …, 10}`, `q` Dirichlet(1) with minimum ≥ `10⁻³`; half with random `F ~ N(0, I)` and random
`0 < r < s`, half threshold policies (`F = −1_H` with `|H|` from 1 to `n−1`, `ε` uniform in `(0.1, 0.9)·q(H)`, no cap).
Behaviours: random; on-segment; below the floor (`p_{F,t}`, `0 ≤ t < r`, including `q`); above the cap; off-ray.

| # | Claim | Prediction | Falsified if |
|---|---|---|---|
| P1 | (a) | the formula equals a 400-point grid plus bounded minimization over `[r, s]` | above `10⁻⁹` |
| P2 | (b), M1 and M5 | on-segment behaviours score `≤ 10⁻¹⁰` on both measures; below-floor, above-cap and off-ray behaviours `> 10⁻⁹` | any exception |
| P3 | (b), order and reductions | `M_free^seg ≤ M_budget^seg + 10⁻¹⁰`; `r = 0` reproduces Def. 18's capped measures and `r = 0, s = ∞` Def. 10's | above `10⁻¹⁰` |
| P4 | (b), M3 | both measures unchanged under `F ↦ aF + c`, `r ↦ r/a`, `s ↦ s/a` | above `10⁻⁹` |
| P5 | (c) | on every threshold policy the base model scores `> 10⁻⁹` with the floor and `≤ 10⁻¹²` without; `p^min(H) = ε` to `10⁻¹²` | any exception |

**Decision rules.** D1: a failed prediction is recorded; a corrected statement is new. D2: if a reduction in P3 fails
beyond the threshold on its refuting side, R7-6b stops. **Falsifier of the purpose:** an agent between floor and cap
charged, or the untouched base model not charged when a floor is declared.
