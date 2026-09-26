---
id: "Boundary 05 Stated extensions, untested"
type: "section"
title: "Stated extensions, untested"
part: "boundary"
order: 6
mentions: []
updated: "2026-09-26"
---
## 5. Stated extensions, untested

### 5.1 The dynamic form, restated in control-theoretic terms
**Setup.** Error in a direction is created at rate `c(t)` and corrected on the basis of failures attributed
with delay `τ`: `e' = c(t) − u(t − τ)`, where `u` is the correction law.

**What is known** (standard control theory; checked in `verify.py V10`):
- Proportional correction `u = k·e`: steady error `c/k`; stable iff `kτ < π/2`. At the margin
  `k = π/(2τ)` the loop oscillates without decay: mean 0.629 vs `2τ/π = 0.637` at `τ = 1`, peak-to-peak
  1.58. **v5's `e*(τ) = (2/π)cτ` was the centre of a sustained oscillation, and linear in `τ` only because
  any gain `κ/τ` makes it so.**
- With integral action (PI), the steady error for constant `c` is **zero at every delay** (internal model
  principle, Francis & Wonham 1976). [[V10]]: `|e| ≈ 10⁻¹³`.
- What delay limits is **bandwidth**. With `τ = 1` and sinusoidal creation at frequency `ω`, the
  closed-loop amplitude is 0.375 at `ω = 0.03` (open loop 33), 3.21 at `0.3` (3.33), **1.57 at `1` (open
  loop 1.00: amplification)**, and 0.33 at `3` (0.33).

**Restated conjecture.** Attribution delay sets a correction bandwidth of order `1/τ`. Persistent error
creation is correctable at any delay given integral action. Error created at timescales near the delay is
**amplified** by correction (the waterbed effect; Bode's sensitivity integral is the general statement,
imported under its standard conditions and not re-derived for the delayed loop). Error created faster than
that passes uncorrected.

**Double protection, restated.** An actor that lengthens `τ` on its own failures shrinks the correctable
band. An actor whose error creation fluctuates near the loop's crossover frequency is amplified by the
correction process itself. **Both require the actor to act on the correction loop — an (X) failure — so
both lie outside the core.**

**Pre-run check for any test:** declare the controller class. Results obtained with proportional
correction alone are artifacts of that choice.

### 5.2 The closed-loop lift
[[B07|B §7]]. A disturbance channel, a conditional Gibbs actor and mutual-information capacity make
requisite variety a proved floor on the boundedness cost. The per-disturbance regret identity also holds.
Untested as a replacement carrier; [[ROADMAP]] T4.

### 5.3 Exchange rates per link
Each link of a delegation chain has its own `β`. **Ratios of `β` across links are meaningful only given a
common unit of value across links** (Prop. [[Prop 12|12]]), which is usually absent. `D_⊥` per link is unit-free.
Whether transverse errors compose along a chain — for example additively in `L²(p*)` at second order — is
unexamined. Recorded so it cannot be promoted quietly.

### 5.4 Layer-0 ontology *(proposal from R3, not applied)*
[[MESSAGE_to_previous_executor]] §6 proposes (multi-agent) causal influence diagrams as the typed,
substrate-free layer, with this core attached as the quantitative layer. The frame conditions (E) and (X)
would then become graph conditions, and the diagnostic loci L1–L7 would be read off the node list.
**Not applied:** changing the carrier requires a PI decision (anti-drift rule 1) and a test on the
pre-registered hard cases first ([[ROADMAP]] T6; [[R3_FIX_LOG]]).

### 5.5 Turner's prior over intents
[[B09|B §9]]. Small, real, not supplied.

---

