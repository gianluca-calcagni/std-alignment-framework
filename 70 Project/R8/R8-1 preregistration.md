---
id: "R8-1 preregistration"
type: "report"
updated: "2026-09-27"
---
# R8-1 — pre-registration: value shortfall, the free default, and the floor as a standard (before any computation)

Implements the PI-accepted recommendations of [[R8 foundations review]] A1 and A5.

**Rule 13.**
- An agent that spends a lot of information and gets a mediocre expected value scores `M_free = 0` if its behaviour is
  shaped like a tilt, and nothing in the core reports the value it forwent.
- A catastrophe inherited from `q` is barely charged at low intensity.

**Rule 11:** every prediction below is *verification*.

## Changes under test

**Def. 22 (value shortfall at equal effort).** For a non-constant `F` and a full-support `p̂` with `k = KL(p̂‖q)`, let `λ`
be the budget-matched intensity (Def. 10).

```
ΔV = E_{p_{F,λ}}F − E_{p̂}F        if k < log 1/q(argmax F)
ΔV = max F − E_{p̂}F               otherwise (saturation)
```

It is in the units of `F`.

**Def. 8, the default convention:** `free` replaces `budget`; `budget` remains a declared option.

## Claimed results (Prop. 37)

- (a) `ΔV ≥ 0`. Below saturation, `ΔV = 0` iff `p̂ = p_{F,λ}` (Lemma 5.1: the tilt uniquely maximizes `E F` on the KL
  sphere).
- (b) `F ↦ aF + c`, `a > 0`, gives `ΔV ↦ a·ΔV`: the shortfall carries the unit of `F`, where `M` carries none.
- (c) The free measure is value-neutral. If `t̂ ≥ 0`, then `E_{p_{F,t̂}}F = E_{p̂}F` (Thm 13's moment condition). If
  `t̂ < 0`, the free intended point is `q`, and its value gap is `E_qF − E_{p̂}F > 0`.
- (d) A floor at `r` is a minimum standard: for `t ≥ 0`, `t ≥ r` iff `E_{p_{F,t}}F ≥ v_min := E_{p_{F,r}}F`.

## Check V41 (seed 4141): 600 instances, `n` in 3–10, `q` Dirichlet(1) with minimum ≥ `10⁻³`, `F ~ N(0, I)`

| # | Prediction | Falsified if |
|---|---|---|
| P1 | (a): `ΔV ≥ −10⁻¹²` on random behaviours; `ΔV ≤ 10⁻¹⁰` on ray points `p_{F,t}`; `ΔV > 10⁻⁹` on off-ray behaviours below saturation | any exception |
| P2 | (b): `\|ΔV(aF+c) − a·ΔV(F)\| ≤ 10⁻⁹·max(1, a·ΔV)` | any exception |
| P3 | (c): `\|E_{p_{F,t̂}}F − E_{p̂}F\| ≤ 10⁻¹⁰` when `t̂ ≥ 0` | any exception |
| P4 | (d): for random `r` and `t`, `t ≥ r` agrees with `E_{p_{F,t}}F ≥ v_min` (ties within `10⁻¹²` excluded) | any disagreement |

**D1:** a failed prediction is recorded. **D2:** if P1 fails, R8-1 stops.
