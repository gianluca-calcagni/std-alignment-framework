# C — Boundary and attack surface

> **Status: v7.3 (R7-4).** Complying where rewarded and reverting where not is inside the explanation layer;
> acting on the reward channel or the monitoring stays outside, by (X) (§3). **v7.2 (R7-3):** tier 3 of C7 is
> empty, since the Bregman identity is tier 1 (row 78). **v7.1 (R7-2):** §3 separates the declared
> reference, which cannot depend on the actor, from the actor's own, whose drift is dynamic.
> **v6.4.** R6 (the third independent review) corrected the tiers of C7, measured where C8's crossing falls for each optimizer, and restated C15's falsifier.
> **v6.3:** R5 (an independent review) tested C7 and C8, corrected C15's plain reading, and refined
> §3 (auto-induced shift; power-seeking). v6.2 and earlier: the v5 attack surface (A1–A11) was attacked in review R2; most targets fell or were
> restated. Review R3 answered C14, weakened C7 (Prop. 15), restated C5 (half-ray), and added C15. Review R4
> turned C7 into a tier map, refined condition (X) (rational inattention), and routed the census
> (T1_census_routing).
> Status §2 records each outcome.

## Abstract, in plain terms

This file is for someone whose job is to break the framework. It lists what the framework claims, what
would falsify each claim, and the cheapest way to try; then what it admits it cannot do.

Two notes before starting. First, v6's core is a set of identities and sharp bounds, each a consequence of
standard mathematics, so attacking the algebra is low-yield; it is checked by hand and by `verify.py`. The
live joints are where the mathematics meets the world: **the actor model (C7)**, **whether the arrangement
has content (C14, answered in R3: predominantly an index)**, **three untested predictions (C8, C9, C11)**, and **the untested application of the detection bound (C15)**. Second, v5's weakest joint (A9) was
broken: the product normal form is forceable. v6 abandons it rather than defending it.

---

## 1. The attack surface

### C1 — The regret identity (Core Thm 1, Cors 1.1–1.4)
**Asserts.** `β·R_J = KL(p̂‖p*)`; the v5 optimality gap is `(1/β)×` the Jeffreys divergence; CGF and
integral forms; the ratio of the two is a weighted mean of `t/β`.
**Breaks if.** Algebra error.
**Cheapest route.** By hand — three lines.
**Status.** Proved; V1 agreement to 10⁻¹³. Extended in v6.1:
- Prop. 15 — any convex regularizer and concave target; regret is a Bregman divergence (V12);
- Cor. 1.5 — stacked stages add in the exponent (V15).

Both are proved. Theorem 1 itself is known (Korbak et al. 2022).

### C2 — The width is the exact worst case (Thm 5, Lemma 5.1, Prop. 6)
**Asserts.** Under a KL capacity `δ`, `R^C ≤ w_δ(E)` for every actor, with equality in the supremum over
intents for the pure capacity maximizer. The width has a Donsker–Varadhan formula and known small- and
large-`δ` asymptotes.
**Breaks if.** The KKT argument in Lemma 5.1 fails, or the attaining construction in Thm 5(ii) does.
**Status.** Proved; V4 (0 / 3,000 violations; attainment `c = 0.999` exactly).

### C3 — Non-separability (Lemma 8, Thm 9)
**Asserts.** No bound of the form `a(E)·b(δ)` on worst-case capacity-constrained regret has bounded
looseness.
**Where it is weak.** The theorem is about the **worst case over intents**. A principal who knows `F` cares
about `R^C` for that `F`. For fixed `F` there is only a measured example (ratio span ×103, V5), not a
theorem.
**Cheapest route.** Prove or refute a fixed-intent version: for fixed non-constant `F`, is
`sup_δ ρ / inf_δ ρ` unbounded over pairs of errors?

### C4 — The divergence order is structural (Props 10, 11)
**Asserts.** KL-limited exposure is infinite for errors with `log 1/q(E>m) = o(m)`, at every budget;
χ²-limited exposure is finite when the variance is.
**Where it is weak.** Practical relevance. Kwa et al. measured open reward models and found tails
consistent with **light**-tailed error. If real evaluator errors are light-tailed, the structural
difference is real but idle.
**Cheapest route.** A tail estimate on an evaluator used in a setting of interest.

### C5 — Decomposition, gauge and conventions (Thm 13, Prop. 16, Thm 17, Def. 8)
**Asserts.**
- On the half-ray, `β·R_J = D_⊥ + D_∥ + X_anti` exactly.
- The gauge-invariant quantities are exactly those listed in Prop. 16.
- All regret notions are points on the convex curve `M(t)`.
- The price and budget conventions disagree on rankings (11.4 % on V14's generator).

**Where it is weak.** Interpretation, not algebra.
- v6 used the full ray, on which `F̂ = −F` had `D_⊥ = 0` (row 50). v6.1 uses the half-ray (row 54). With it,
  anti-alignment is transverse plus `X_anti`.
- The recommended default convention (budget) is a choice. It is justified by being both a regret and
  gauge-invariant, not by any theorem.

**Breaks if.** A use case where the budget convention misleads and the price convention does not. Or a
quantity useful for diagnosis that is neither gauge-invariant nor reportable with a natural gauge fixing.

### C6 — What optimization pressure does (Prop. 14)
**Asserts.** For the entropic actor, the initial sign of the effect of optimization is `−Cov_q(F̂,F)`. For
any smooth optimizer, it is the covariance in that optimizer's geometry (Prop. 22). The terminal value is set
by argmax agreement, and the raw alignment regret has no sign.
**Status.** Proved; V8. The measured frequencies are generator-dependent and marked so.

### C7 — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*

**Asserts.** Each result holds for the actual-actor class of its tier (Core, "Assumption tiers"). The
intended actor is fixed separately by the comparison convention (Def. 8).

| Tier | Holds for, as the actual actor | Results |
|---|---|---|
| 1 | every actor | Thm 1, Thm 13, Thm 17 (i)–(iii), Prop. 18's cap, Prop. 19 (all against a Gibbs intended actor); Props 6, 10, 11, 20, 21, 22; Lemma 8; B7(a)–(e) (for (e), against the rational-inattention optimum); B11(i) |
| 2 | exact maximizers over a set containing the intended actor | Thm 5(i)–(ii); Thm 9; the regret bound of Prop. 7 |
| 2′ | argmax selectors over a common random candidate set (equal budget) | Prop. 23 |
| 3 | exact regularized optima (with `φ/β − U` convex) | none since R7-3: the Bregman identity is tier 1 (row 78) |
| 4 | exponential tilts: (E) from the declared reference, (E_A) from the actor's own | the E-based bounds (Props 2–4), Prop. 14, the Gibbs-specific corollaries — (E); the gauge (Props 12, 16) and Prop. 26 — (E_A). Every (E) result transfers to (E_A) with error `E + log(q_A/q)/β` |
| 4″ | log-linear learning in potential games | B13 |

**What the independent reviews measured** (R5, R6; `reviews/`):

| Claim | Best-of-n | Vanilla policy gradient | KL-penalized PG | Natural PG | Meaning |
|---|---|---|---|---|---|
| C8 crossing exists | holds | holds | holds | holds | universal; **its location is not** (C8) |
| Tier 2 (Thm 5(i)) | **fails at matched KL** (4.3 %); holds at equal `n` (Prop. 23) | **fails** (25.5 %, early-stopped) | — | — | tier 2 needs exact maximizers |
| Sign criterion (Prop. 14(ii)) | fails (rank covariance; 2.45 % random) | fails (`q²`-weighted; 4 % random) | as VPG | holds | a covariance in the optimizer's geometry (Prop. 22) |
| Thm 1 identity | holds (tier 1) | holds | holds, along 18,003 iterates | holds | tier 1 |
| No overoptimization under affine regression | holds | holds (uniform `q`) | — | — | Prop. 21 |
| Rescaling harmless (own or budget convention) | holds (monotone-invariant) | holds at matched KL | — | — | Remark 13.5 |

**KL-penalized policy gradient behaves like vanilla policy gradient** over the range where the crossing
happens. Its early phase overshoots into near-determinism: at the V5 scale, a runner-up probability of
`1.9·10⁻¹⁰` against `0.19` at the optimum. It relaxes toward the Gibbs optimum only on very long timescales
(R6, P9 diagnosis). That cuts against reading RLHF-trained policies as Gibbs actors, which is a tier-4
assumption.

**Where it is still weak.** The tier-4 results describe the entropic actor exactly and do not transfer. The
tier-1 identities transfer, but their counterfactual (a Gibbs intended actor) may not be the natural one for a
given optimizer. For engineering comparisons, use the mechanism-relative comparison (Def. 14), knowing that it
depends on the attributed mechanism (Prop. 25).

**Open.** Whether the ordering of crossing locations follows one index of the optimizer — how strongly its
update favours already-probable behaviour (ROADMAP T8).

### C8 — Crossing curves *(tested in R5 on best-of-n and vanilla policy gradient: holds)*
**Asserts.** Two evaluator errors, one dense and one concentrated on a rare region, with
`Var_q(E_dense) > Var_q(E_rare)` but `osc(E_dense) < osc(E_rare)`, yield gold-regret curves that **cross** as
capacity grows: the dense error is worse at small capacity, the concentrated one at large capacity. For
the worst case over intents the crossing is forced by the two limits of Thm 9. (Review R2 proposed
*matched* variances; that version predicts a tie at small capacity, not a crossing — row 51.)
**Falsifier.** No crossing for a best-of-n actor, or for a policy trained with a KL penalty, over a
capacity range spanning both asymptotes of Prop. 6.
**Result (R5, R6).** The crossing exists, with exactly one sign change, for every optimizer tested: Gibbs,
natural policy gradient, best-of-n, vanilla policy gradient, and KL-penalized policy gradient. **Its location
is optimizer-specific**, spanning roughly 180-fold:

| Optimizer | d\* (KL) |
|---|---|
| vanilla policy gradient | 0.026 |
| KL-penalized policy gradient | 0.026 |
| Gibbs | 0.54 |
| natural policy gradient | 0.54 |
| best-of-n | 4.7 |

Statements of the form "at this capacity, error type X dominates" do not transfer between optimizers.
Whether one index of an optimizer predicts the **order** of d\* is open (ROADMAP T8).
**Note.** For the Gibbs actor this is the V5 example and cannot fail. The test is only informative for
other actors (C7).

### C9 — The overoptimization slope *(untested prediction)*
**Asserts.** The leading coefficient of gold reward in `d = √KL` is `α ≈ √2·ρ_q(F,F̂)·sd_q(F)` for Gibbs
paths, and approached by best-of-n as `n` grows (B §4).
**Falsifier.** Published or replicated `α_bon` off by more than a factor 1.5 from `√2·ρ·sd` when `ρ` (the
proxy–gold correlation under the initial policy) is measured.
**Cheapest route.** Check whether Gao et al. report the initial proxy–gold correlation; otherwise replicate
with small open models.

### C10 — Identification (Props 12 and 16, Core §10)
**Asserts.** Value-unit statements need an external unit channel; institutions lack one, so the
institutional `β` is a normalization.
**Breaks if.** An institutional setting identifies the selection intensity without a scale normalization.
**Cheapest route.** Laboratory games with monetary payoffs estimate quantal-response precision in money
units. That is a unit channel, but only if the principal's intent is denominated in money. Find a case
where it is.

### C11 — The dynamic form, restated *(untested; §5.1)*

### C12 — The closed-loop lift *(proved pieces, untested as a carrier; B §7)*

### C13 — The boundary is two conditions *(§3)*
**Breaks if.** An outside item fails neither existence nor exogeneity, and is not a category difference.

### C14 — Does the arrangement have content? *(successor to v5 A9; answered in R3)*
**R3 answer.** The prior-art search (MESSAGE_to_previous_executor §2) found most individual results
stated elsewhere:
- Korbak et al. — Thm 1;
- Mroueh; Mroueh & Nitsure — Prop. 7 and the √KL law;
- Huang et al.; Kwa et al. — Props 10–11;
- El-Mhamdi & Hoang — the Gaussian / tail regime;
- STARC — unit-free comparison;
- Wang & Huang — multitask.

**Verdict: predominantly an index.** The following were not found stated elsewhere:
- the width as the exact worst case with the non-separability theorem;
- the intent-ray decomposition;
- the conjugate-pairing organization of regularizer choice;
- the closed-loop Conant–Fano floor;
- the one-curve view of counterfactual conventions (Thm 17);
- the regret–detection bound in the form of Prop. 18.

Absence from roughly ten queries is not novelty. For the PI's goal — a standard into which results import —
an index whose entries are derived inside one calculus is the desired outcome, not a failure.

The original statement of C14 follows.

**Forceability, now a theorem.** For any convex capacity functional `φ` on distributions with conjugate
`φ*(G) = sup_p [E_pG − φ(p)]`, Fenchel–Young gives, for every `t > 0`,
`E_pE − E_qE ≤ [φ(p) + φ*(tE) − t·E_qE]/t`. Optimizing over `t` yields a "capacity × error" normal form
whenever `φ` is a power of a norm of `p − q` (then the infimum is `‖p − q‖·‖E‖_*`). **A normal form exists for every convex capacity; its shape carries no
information.** v5's product form is abandoned.
**What v6 claims instead.** Content lives in the forbidden statements (Core §11) and in the nine
derivations of Dictionary (six in v6). The claim is that alignment phenomena from several literatures
(regressional and extremal Goodhart, catastrophic Goodhart, correlated proxies, error–regret mismatch,
overoptimization slopes, rescaling) are readings of one object: the tilt of the error by the actor, read at
different capacities and against different divergences.
**Breaks if.** That unification already exists in the same generality (then v6 is an index, which is
survivable), or a forbidden statement does not follow from the tilt structure.
**Cheapest route.** A literature search for work treating these phenomena jointly via Donsker–Varadhan /
Hölder duality.

### C15 — Detection and the evaluation gap (Props 18, 19) *(proved; tier 1 in the actual actor since v6.4; application untested)*
**Asserts.**
- For any actual actor, no test on behavioural samples has an asymptotic error exponent above `β·R_J`,
  measured against the Gibbs intended actor at a declared price.
- Deployment harm exceeds the achievable detection exponent by at least `Γ`.
**Where it is weak.** The bound is for the most favourable overseer — both hypotheses known, i.i.d.
samples, exogenous contexts. Realistic overseers face composite hypotheses and adaptively chosen contexts.
The proposition says nothing about how an actor comes to condition on undersampled contexts.
**Breaks if.** It does not break by finite-sample success: at small `n` the empirical rate can exceed
`β·R_J` even for the entropic actor (F2). *(v6.3's falsifier was stated for "few samples",
which cannot falsify an asymptotic claim; R6, row 70.)* The claim is a theorem about exponents,
so it breaks only by an error in the proof. What can fail empirically is its **relevance**. A realistic
overseer's sample complexity may be dominated by composite-hypothesis and adaptive-context effects that the
bound ignores, and then the bound is true but uninformative.
**Cheapest route.** A toy bandit with a KL-regularized misaligned policy. Measure the number of samples a
likelihood-ratio test needs, against `log(1/ε)/C(p̂,p*)`, across `β`.

---

## 2. What is outside

### 2.1 Aggregation and social choice
The core needs a single functional `F`. For a group principal it must be constructed. Arrow's theorem says
no rule meets unrestricted domain, Pareto, IIA and non-dictatorship together — **even with sincere
reports**. Gibbard–Satterthwaite adds that non-dictatorial rules are manipulable, which makes `F` depend on
strategic reporting. **These are two different failures:** Arrow is a failure of *existence*;
Gibbard–Satterthwaite is a failure of *exogeneity*. See §3.

### 2.2 Self-reference and embedded agency
`R_J` needs `q`, `F` and `β` fixed at the moment of comparison. An actor whose choice moves its own
reference or capacity has no fixed intended counterpart. This includes power-seeking as read in
B §9, and the attribution-delay manipulation of §5.1.

### 2.3 Interpretability
A category difference. The core is behavioural. It can say which quantities are identified from
behaviour — `D_⊥` and `sign(t̂)` given `q` (Core Cor. 13.2) — and nothing about mechanisms.
Interpretability results enter as inputs, e.g. shortening attribution delay (§5.1) or supplying an
independent reference measurement (Prop. 12).

---

## 3. The boundary as two conditions

> **(E) Existence.** A single functional `F` on behaviours exists.
> **(X) Exogeneity.** `F`, `β`, the evaluator and the correction loop are not functions of the actor's
> behaviour at the moment of evaluation. Neither is `q`, **unless** `q` is optimized jointly with the policy
> as part of the capacity (rational inattention). That case keeps an exact regret identity
> (B7(e)) and is inside. *(Refined in v6.2; row 59.)*

| Outside item | Condition that fails |
|---|---|
| Arrow (sincere aggregation) | (E) |
| judge disagreement (census E10) | (E) |
| Gibbard–Satterthwaite (strategic reporting) | (X): `F` depends on reports |
| multi-agent / equilibrium | (X): `F` and the reach depend on others |
| frequency-dependent selection | (X) |
| self-reference; **acquiring capacity or resources** beyond the fixed environment; manipulation of `τ` | (X): the capacity, the correction loop, or `q` *other than by joint optimization*, depends on the actor |
| *not outside:* power-seeking in Turner's sense, within a fixed environment | inside on trajectory space; it needs a prior over intents, not frame endogeneity (R5; B §9; D row 64) |
| sophisticated present bias (intrapersonal game) | (X): later selves' behaviour responds to earlier selves' — the equilibrium fork (B §12(c)) |
| auto-induced **preference** change (census G4) | (X): the target depends on the actor |
| *not outside:* auto-induced **distributional** shift with a fixed target (census C8) | inside. On trajectory space with shared dynamics, the shifted state distribution is part of the actor's own trajectory law (R5; D row 63) |
| interpretability | neither: category difference |

v5 claimed three of four outside items were "one condition". **Arrow breaks that**: it is non-existence
under sincere reporting, not endogeneity. Two conditions, then, and both are needed.

**Not outside (v6.2):** a rational-inattention actor, whose reference is its own optimized action marginal.
Endogeneity of the reference through optimization of the information cost is absorbed by the calculus
(B7(e)). Endogeneity through tampering, manipulation, or the actor changing the target is not.

*Note (R7-4).* An agent that complies where it is rewarded and reverts where it is not is **inside** the
explanation layer: one stationary dynamic element, the continuation value, derives it (Prop. 27). So do its
consequences — masking, selection blindness, and the fake-alignment gap (Props 28–30). Two things stay
outside, by (X):
- acting on the reward channel `R`, or on the monitoring `m_c`: tampering, or disabling oversight;
- an agent that *learns* `m_c` from its own history — the dynamic layer.

The frozen census routing (v6.3) is not affected.

*Note (R7-2).* Since R7-2 there are two references. The **declared** reference `q` is part of the intent, so it
cannot depend on the actor. The actor's **own** reference `q_A` can drift with its behaviour (habit
formation, census H19). At a snapshot such drift is absorbed into an effective evaluator error
`log(q_A/q)/β` (Prop. 26(a)). Across time it is a dynamic-layer phenomenon. It violates (X) only when the
actor changes the reference *other than* through its behaviour's own statistics, e.g. by rewriting the
default. The frozen census routing (v6.3) is not affected: it was recorded against v6.3's single `q`.

---

## 4. The equilibrium fork

**Still open — and now measured.** The census routing puts strategic interaction as the largest missing
layer: 51 items need it, 23 of them inexpressible without it (T1_census_routing). One piece is already
inside the carrier: exact potential games under log-linear learning are a joint tilt (B §13). The cost of deferring the rest is concrete in three places:

- the handicap/signalling import needs equilibrium **and** type-dependent references (B §8);
- adversarial Goodhart needs it (B §3);
- (X)-failures by other agents need it.

The recommendation to keep the single-principal scope stands for the reason v5 gave: test the one-import
version first. v6 is more tested than v5, but its untested predictions (C8, C9) are cheaper than the fork.

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
  principle, Francis & Wonham 1976). V10: `|e| ≈ 10⁻¹³`.
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
B §7. A disturbance channel, a conditional Gibbs actor and mutual-information capacity make
requisite variety a proved floor on the boundedness cost. The per-disturbance regret identity also holds.
Untested as a replacement carrier; ROADMAP T4.

### 5.3 Exchange rates per link
Each link of a delegation chain has its own `β`. **Ratios of `β` across links are meaningful only given a
common unit of value across links** (Prop. 12), which is usually absent. `D_⊥` per link is unit-free.
Whether transverse errors compose along a chain — for example additively in `L²(p*)` at second order — is
unexamined. Recorded so it cannot be promoted quietly.

### 5.4 Layer-0 ontology *(proposal from R3, not applied)*
MESSAGE_to_previous_executor §6 proposes (multi-agent) causal influence diagrams as the typed,
substrate-free layer, with this core attached as the quantitative layer. The frame conditions (E) and (X)
would then become graph conditions, and the diagnostic loci L1–L7 would be read off the node list.
**Not applied:** changing the carrier requires a PI decision (anti-drift rule 1) and a test on the
pre-registered hard cases first (ROADMAP T6; R3_FIX_LOG).

### 5.5 Turner's prior over intents
B §9. Small, real, not supplied.

---

## 6. What a good attack looks like

**Most damaging, in order.**

0. **The generality claim.** The census has been routed by two raters (T1_census_routing), who disagree
   on about 100 items. An adjudication of those items, or a showing that many census items fit neither the
   core nor a stated outside condition, would settle or refute the generality claim more directly than
   anything below.
1. **C7.** Show that the qualitative predictions fail for non-Gibbs actors. This would confine the core to
   an idealized actor that nobody deploys.
2. **C14.** The index verdict is already conceded. What remains damaging: showing that one of the residual
   organizing statements listed in C14 is also stated elsewhere, or that a forbidden statement does not
   follow from the tilt structure (a real defect).
3. **C15.** Show that detection from few behavioural samples succeeds where `β·R_J` is small. That would
   mean the entropic actor is the wrong model of that system.
4. **C4.** Show that the structural difference between divergence orders is idle for the evaluators that
   matter.
5. **C9.** Falsify the slope prediction against published coefficients.

**Less damaging than it looks.** Showing that an individual result is known. Every result in Core is
standard mathematics, and says so.

**Not worth your time.** The looseness of Props 2 and 7 — reported, with distributions. The scope —
§§2–4 say what is outside and why.
