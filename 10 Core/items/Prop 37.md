---
id: "Prop 37"
type: "proposition"
title: "the value shortfall; R8-1"
section: "Core 07 Identification, gauge, and the intent ray"
order: 42.84
layer: "measurement"
tier: []
assumes: []
status: "proved"
depends_on: ["Def 22", "Thm 13", "Def 20", "Thm 17", "Lemma 5.1", "Def 10"]
mentions: ["R8-1 preregistration run 2", "R8-1 results"]
checks: ["V41"]
sources: []
aliases: ["Proposition 37", "Prop. 37"]
updated: "2026-09-27"
---
# Prop 37 — the value shortfall; R8-1

## Statement

**Proposition 37 (the value shortfall; R8-1; tier 1).** Let `F` be non-constant, `p̂` full-support, and `ΔV` as in
Def. [[Def 22|22]].

(a) **Nats are priced value.** Below saturation with `λ > 0`, `ΔV = M_budget/λ`. Hence `ΔV ≥ 0`, with `ΔV = 0` iff
`p̂ = p_{F,λ}`. At saturation `ΔV = max F − E_{p̂}F > 0`.

(b) **Units.** Under `F ↦ aF + c` with `a > 0`, `ΔV ↦ a·ΔV`, while `M_budget` is unchanged.

(c) **The free point is value-neutral.** If the moment point `t̂` of Thm [[Thm 13|13]] is `≥ 0`, then
`E_{p_{F,t̂}}F = E_{p̂}F`.

(d) **A floor is a minimum standard.** For `r, t ≥ 0`: `t ≥ r` iff `E_{p_{F,t}}F ≥ v_min`, with
`v_min = E_{p_{F,r}}F`. So a floor at intensity `r` (Def. [[Def 20|20]]) declares a minimum expected value `v_min` in `F`'s
units.

## Proof

*Proof.* (a) The identity is Thm [[Thm 17|17]](iii). `M_budget = KL(p̂‖p_{F,λ}) ≥ 0`, with equality iff `p̂ = p_{F,λ}`. At
saturation `p̂` is full-support, so it puts mass off `argmax F`, which is a proper subset for non-constant `F`.

(b) `p_{aF+c,t} = p_{F,at}`, so the budget-matched intended behaviour is the same distribution, with intensity `λ/a`.
Both expectations scale by `a` and shift by `c`; the shift cancels. `M_budget` is Thm [[Thm 17|17]](iv).

(c) Thm [[Thm 13|13]]: `t̂` solves the moment condition `E_{p_{F,t̂}}F = E_{p̂}F`.

(d) `dE_{p_{F,t}}F/dt = Var_{p_{F,t}}F > 0` for non-constant `F` (Lemma [[Lemma 5.1|5.1]]), so `t ↦ E_{p_{F,t}}F` is strictly
increasing. ∎

## Notes and checks

*Reading.* (a) says that `M_budget` and `ΔV` are the same comparison in two units: nats, and `F`'s units, related by the
intended exchange rate. (b) is why `ΔV` is a report and not a measure. (c) is why the value shortfall is taken at equal
effort and not at the free point. (d) turns a floor into the form a principal states it: "at least `v_min`".

*Nothing here is new mathematics.* (a) is Thm [[Thm 17|17]](iii), (c) is Thm [[Thm 13|13]]'s moment condition, and (d) is the
monotonicity of Lemma [[Lemma 5.1|5.1]]. The step names the report and fixes how the core uses it. Pre-registration run 1
missed Thm 17(iii) and set a bound without a scale; its P1 failed as registered ([[R8-1 results]]).

*Check.* [[V41]] (600 instances, 1,744 points for the identity; pre-registered, [[R8-1 preregistration run 2]]):
- (a): `|ΔV − M_budget/λ| ≤ 5.2·10⁻¹⁴·max(1, ΔV)`; `ΔV ≥ −4·10⁻¹⁴`; never `ΔV ≤ 0` while `M_budget > 10⁻¹²`.
- (b): relative difference `≤ 5.4·10⁻¹³`.
- (c): `≤ 3.8·10⁻¹⁵`.
- (d): no disagreement.
