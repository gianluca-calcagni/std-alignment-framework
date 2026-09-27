---
id: "R8-1 results"
type: "report"
updated: "2026-09-27"
---
# R8-1 — results: value shortfall, the free default, the floor as a standard (v7.9)

Implements the PI-accepted recommendations of [[R8 foundations review]]: A1 (stakes), A5 (default convention), A6
(budget set). Pre-registered twice: [[R8-1 preregistration]] (sha256 `6be8af57…`, `1c6e97d`) and, after run 1
stopped on D2, [[R8-1 preregistration run 2]] (sha256 `705fbfc0…`, `894161d`). Check [[V41]].

## Run 1: stopped on D2

| # | Prediction | Result |
|---|---|---|
| P1 | `ΔV ≥ 0`; `= 0` on the ray; `> 10⁻⁹` off it | **fails**: off-ray minimum `8.26·10⁻¹⁰`, on a nearly on-ray instance (`M_budget = 2.3·10⁻⁹`, `λ = 2.8`) |
| P2–P4 | scaling; value-neutral free point; floor as a standard | hold |

**Diagnosis.** Across run 1, `ΔV/M_budget = 1/λ`. The bound `10⁻⁹` had no scale: `ΔV` is as small as `M_budget/λ`,
and that can be anything. **The identity is not new.** It is Thm [[Thm 17|17]](iii), in the core since v6, and Cor.
[[Cor 17.1|17.1]] uses it. I did not read Thm 17 before registering (a repeat of [[NOTES_claude]] §1: read what a test
depends on first).

## Run 2

| # | Prediction | Result | Verdict |
|---|---|---|---|
| P1′ | `\|ΔV − M_budget/λ\| ≤ 10⁻⁹·max(1, ΔV)` for `λ > 10⁻³` below saturation; `ΔV ≥ −10⁻¹²`; `ΔV > 0` where `M_budget > 10⁻¹²` | `5.2·10⁻¹⁴` over 1,744 points; min `−4·10⁻¹⁴`; no exception | holds |
| P2 | `ΔV(aF + c) = a·ΔV(F)` | `5.4·10⁻¹³` | holds |
| P3 | `E_{p_{t̂}}F = E_{p̂}F` when `t̂ ≥ 0` | `3.8·10⁻¹⁵` | holds |
| P4 | `t ≥ r` iff `E_{p_t}F ≥ v_min` | 0 disagreements | holds |

Both SIMD paths: identical verdicts.

## What changed in the core

- **Def. [[Def 22|22]]:** the value shortfall `ΔV`, a report in `F`'s units (not a measure: it fails M3 by design). Its
  notes read it across ML, humans, institutions and biology.
- **Prop. [[Prop 37|37]]:** `M_budget = λ·ΔV`; units; the free point is value-neutral; a floor is a minimum standard. No new
  mathematics: it collects Thm 17(iii), Thm 13 and Lemma 5.1 into the form the core uses.
- **Def. [[Def 8|8]]:** the default convention is **free**; budget is declared ("compare at equal effort"). Every
  diagnosis reports `ΔV`. Notes on stakes (A1) and the rejected harm-weighted divergence. Prop. 24, Rem. 13.5 and Cor.
  17.1 updated to match; no verdict of theirs changes (rescaling costs 0 under free as under budget).
- **Def. [[Def 19|19]]:** the budget set depends on `p̂` (A6); KL is the divergence because the principal is entropic,
  not because of detection (A2).

## Semantics across disciplines (the PI's condition)

The reading is sound where three things are declared: `q`, `F` and the declarer of `F`. Then `ΔV` means "value the
principal cares about, forgone against pure pursuit with the same departure from the reference" in every substrate
(Def. 22's table).
- **Biology is exact, not an analogy.** With constant fitness, replicator dynamics are the intent ray and Fisher's
  fundamental theorem is Prop. 37(d)'s monotonicity. The "principal" is the modeller's choice of `F`, and misalignment
  means departure from pure selection.
- **ML:** `KL(p̂‖q)` is the quantity RLHF already budgets, and `ΔV` is gold reward forgone at that KL.
- **Humans and institutions:** the criterion must be declared and its declarer named. T7 showed that the default can
  move the evaluator, so `q` cannot be fitted from choices.

**Where the reading breaks:** frequency-dependent fitness and endogenous contexts (no fixed `F` or `ρ`); risk attitudes
(`ΔV` is an expectation); estimation (population quantities, A3, deferred).

## Not changed

- No numerical verdict elsewhere in the vault depended on the default. T7's budget/free splits reported both.
- The estimation protocol (A3) remains the prerequisite for further empirical work.
