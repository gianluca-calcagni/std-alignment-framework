# A — Anti-Patterns *(carried over)*

> **Inherited from the parent programme unchanged.** Every entry was earned from a specific failure
> in that work; none is hypothetical. The §10 checklist is the most transferable artifact either
> corpus produced and should be run before promoting any claim in this thread.
>
> Parent: `../persona-state-framework/`. The narrative below refers to that programme's experiments;
> it is retained because the lessons stick better with the cases attached.

### Navigating this file

Sections **1–8** are drawn from theory-building in the parent programme; several cases concern
machinery this subframework dropped (emotion theory, representation architecture). The *lessons*
transfer; the *cases* may not.

Sections **9–10** are the experimental and methodological core and transfer in full. **§10 is the
checklist.** If reading once, read §10 and §9.

---

## 1. Over-unification

### 1.1 Gradient hacking, claimed as derived

**What happened.** The `Para(Optic)` level-nesting produced a table in which each pattern recurs
at the interaction, developmental and formative levels. Two cells were attested (self-deception,
epistemic wireheading); the third was gradient hacking. It was written up as a *derived
prediction* and became the showcase item.

**Why it was wrong.** The nesting makes the pattern *natural*. Nothing forces every pattern to
instantiate at every level. The framework would happily represent a world where the formative
level has no evaluator-corruption analogue.

**Lesson.** *A structural analogy is not a derivation.* The test is whether the framework
**forbids the negation**, and a table of parallels almost never does.

### 1.2 The circumplex, overclaimed

**What happened.** From "the objective functional has two parameters" I wrote "the emotion
circumplex is the appraisal-function's output space."

**What actually followed.** Affect is **at least two-dimensional**. The circularity — orthogonality
of valence and gain, a disc rather than a square — does not follow, nor do the quadrant labels.

**Lesson.** *Derive the dimension, not the geometry.* When an import has more structure than the
derivation, take only the part you earned.

### 1.3 Interior optima, and the temptation to unify them

Three independent results have the same shape: gain (exploitation vs exploration), intervention
amplitude (detection vs fitting), and evaluative-channel capacity (discriminativeness vs
narrowness). Each is "two opposing pressures on a scalar, hence an interior optimum."

**This was not unified, deliberately.** That shape is generic — nearly any optimization has it.
Three instances of a generic form is not a pattern, and asserting otherwise would have repeated
§1.1 exactly.

**Lesson.** *Recurrence of a generic form is not evidence of a common mechanism.* The bar is a
shared derivation, not a shared silhouette.

---

## 2. Conflation

### 2.1 Non-identifiability and superposition under one label

**What happened.** "Pretraining predicts polysemanticity and superposition" was written as one
claim.

**The split.** Non-identifiability is **derived** (no interventional variation ⇒ diffeomorphism
ambiguity). Superposition is a **capacity** claim — more features than dimensions — which is a
separate argument the framework accommodates and does not generate.

**Lesson.** *When two phenomena co-occur in the literature, check whether your derivation reaches
both.* It usually reaches one.

### 2.2 Constraints (N) and (D), held apart for four versions

Narrowness said the evaluative channel's capacity must be low; discriminativeness said it must not
be too low. These were listed as two of five independent constraints.

**They bound the same quantity from opposite sides.** Recognising this reduced the constraint set
to four, with one being an interval.

**Lesson.** *Before adding a constraint, check whether it bounds a quantity an existing one
already bounds.*

---

## 3. Errors of statement

### 3.1 The retention bottleneck, stated without its exception

**What happened.** "Nothing motivates except as retained" was written flatly — and it contradicted
a section three subsections earlier establishing the bypass channel as a route to valuation that
does *not* pass through the retained state.

**Corrected.** "…except as retained, **or via the bypass channel**," with the bottleneck's force
depending explicitly on the channel's narrowness.

**Lesson.** *A derived claim inherits every exception its premises carry.* Re-read the premises
when writing the conclusion, not only when writing the premises.

### 3.2 Placeholder names that stick

`self-construal` was chosen for parallelism, known to be poor, and survived two versions before
being replaced by `monitoring` — which was available in the canonical literature the whole time.

**Lesson.** *A placeholder in a definitional slot is a load-bearing placeholder.* Search the
literature for the term before, not after, the structure stabilises.

---

## 4. Methodological errors

### 4.1 Reporting a number without a floor

**What happened.** The passive learner in E18 scored MCC = 0.411 and was written up as "low, but
learning something."

**The control.** An untrained encoder scores **0.571**. MCC has a high floor at three dimensions.
The passive learner is *below chance* — it does not merely fail to identify, it destroys the
accidental alignment present at initialisation.

**Lesson.** *No absolute number is interpretable without its chance floor.* Now a standing
commitment in the experiment register.

### 4.2 Transplanting an intuition across regimes

**What happened.** I predicted that the well-excited latent axis would be best identified, on
signal-to-noise grounds. The observed ordering was the reverse, consistently.

**Diagnosis.** An *estimation* intuition applied where the binding constraint was *approximation*.
Larger interventions improve detection and worsen fitting; in a noiseless, nonlinear setting the
second dominates.

**Why it was worth it.** The failure produced the amplitude-as-design-variable refinement, which
nothing else had produced. The confirmed half of the experiment produced nothing new.

**Lesson.** *Name the regime before importing the intuition.* And: the failed half of an
experiment is where the content is.

### 4.3 Cheap experiments that cannot inform

Three register entries — SAE feature clustering, nonparametric growth rates, comparative
metamemory — are inexpensive and nearly uninformative. Feature clustering fails in a way the
framework also predicts; growth rates are satisfied by almost any sublinear curve; comparative
metamemory runs into disputes the framework cannot adjudicate.

**Lesson.** *A cheap uninformative experiment costs more than it looks*, because it produces the
appearance of testing. Cost is not the ranking criterion; what a null kills is.

---

## 5. Premature conclusions from selection effects

**What happened.** The derivability audit found that every derivation traced to the reach's
geometry, the bounded-rationality currency, or a channel constraint — and that the state-side
apparatus produced only *located* results. Recommendation issued: formalize the objective side
first.

**What followed immediately.** Filter stability — state-side — produced four derivations in one
sitting (offline consolidation, replay, forgetting, model collapse), once it was asked for
consequences rather than merely stated.

**Diagnosis.** The two productive regions were the two with imported mathematics already attached.
The audit measured *where formalization had reached*, not where content lived.

**Lesson.** *An audit of a partly-formalized theory measures the formalization, not the theory.*
Recommendation downgraded from finding to preference.

---

## 6. Architectural reversals

### 6.1 The v0.5 → v0.6 inversion

**What was wrong.** v0.5 made the inner state a triple — construal, disposition, intention — with
a map each. But the construal/intention split *is* the separation principle, which holds only
under exactness. So the architecture built into its definitions something its own imported
theorems say is generically false.

**The fix.** Unfactored persona-state primitive; factorization demoted to a gradable property.

**What it cost.** Error *localization* (classification survived); representational goal-safety;
tractability of the update map.

**What it bought.** Psychoactive impairment of cognition, emotional distortion of belief, belief
perseverance, the Nisbett–Wilson split, a strengthened retention bottleneck, and a measurable
persona-level parameter — all previously anomalies or stipulations.

**Lesson.** *Do not build a known-false idealization into a definition.* Make it a hypothesis the
framework can state, and it usually earns its keep as a variable.

### 6.2 The quartet, which was almost an epicycle

The request was for a 2×2. The honest answer would have been "no" if the fourth cell had been an
addition. It was not: it is a reading of the `Para(Optic)` structure already imported, with
valuation placed as the *objective* rather than a fourth interface — which explains why it has no
direction of fit rather than merely noting it.

**Lesson.** *A proposed extension is only compelling if it explains something the current version
could only report.*

### 6.3 The third row, correctly refused

"Other-facing" was considered as a third row alongside self and world, and rejected. Another
persona is not a different *kind* of target; it is a target that **contains a model of you**,
making the environment-facing backward leg a fixed-point equation. Convexity survives; the
linear-maximization oracle dies.

**Lesson.** *Before adding a dimension, check whether the phenomenon is a change of condition on
an existing one.*

---

## 7. Attractive symmetries, hunted and found null

**The self-optic's own convex body.** The expectation was a pleasing inward/outward symmetry: two
optics, two reaches. The answer is **one body, two control coordinates**.

The null produced more than the symmetry would have: wireheading's geometric characterization,
grounding as a measurability condition — the cleanest result in the corpus — and the placement of
inward exploration in the metamemory literature.

**Lesson.** *Chase the symmetry, but bank the null.* The shape of the negative answer is where the
content was.

---

## 8. Seductive mappings, flagged rather than promoted

Two mappings are consistent with the offline-consolidation derivation and are **not** forced:
dream phenomenology as open-loop rollout, and depressive rumination as open-loop compounding with
behavioural activation restoring the correction step.

They are recorded in the growth file as speculative and excluded from the derivation ledger. The
framework forces an offline phase with replay; it does not force that phase to be *experienced*,
and it bears on no clinical question.

**Lesson.** *The most quotable consequence of a result is usually the one it does not support.*
Mark it at the moment of writing, not later.

---

## 9. Experimental design and measurement failures

### 9.1 No achievable-advantage control

X2 compared an adaptive design rule against a fixed baseline and specified a κ = 1 control to show
the effect was not generic to adaptivity. It did **not** specify a control showing the effect
*existed*. A post-hoc sweep over fixed designs put the optimum at exactly the baseline — so no
design, adaptive or otherwise, could have won.

**Lesson.** *A control that rules out a spurious cause is not a control that establishes an
available effect.* Sweep the design space before testing whether an algorithm searches it.

### 9.2 Design space equal to parameter space

The deeper failure. X2's actions were additive on the latents, so the thing chosen and the thing
estimated lived in the same space, with the same coordinates. In that case `log det` separates into
a design term and a constant, and D-optimal design is **uniform** regardless of how anisotropic the
problem is. The experiment could not have found what it was looking for.

**Lesson.** *Check whether the optimum of your criterion is analytically trivial for your setup
before running it.* Two lines of algebra would have caught this.

### 9.3 Unanimity as an artifact of the choice set

An adaptive amplitude bandit selected the grid endpoint in 12/12 seeds, which reads as decisive
confirmation. It was an artifact: the optimum lay at the endpoint. A straddling grid showed the
rule overshoots by 3–10×.

**Lesson.** *Unanimity across seeds is not evidence of correctness when the choice set is bounded
at the interesting point.* Always straddle.

### 9.4 A specification whose regime made the criterion undefined

X2 as written was noiseless, and the observation map was a bijection. D-optimality minimises
estimator variance; with no noise that variance is identically zero. The specified criterion had
nothing to optimise. The executor caught this during calibration, before any contrast was
inspected.

**Lesson.** *State the regime a criterion requires when you specify it.* Ours required estimation
noise and did not say so.

### 9.5 The same measurement, two mechanisms

The executor's P4 (`A-greedy < A-dopt`) passed and would have been written up as "the coverage term
adds design value." Given the exponent sweep showing isotropy is optimal, the same number reads as
"the coverage term pulls the greedy rule back toward the optimum it was departing from." Opposite
mechanisms, one measurement, and only the post-hoc control discriminates.

**Lesson.** *Before interpreting a passing contrast, ask what else would produce that number.*

---

### 9.6 The floor rule failing at write-up rather than measurement

The chance-floor rule was followed — the floor was measured, tabulated, and its rationale cited in
the same document — and then not applied across two tables three pages apart. A treatment cell sat
0.21 below its own measured floor and was reported as the low end of a performance curve.

**Lesson.** *A rule that says "report X" does not cause X to be used.* Make the comparison
mechanical: flag below-floor cells in the table itself.

### 9.7 An instrument that works only near the answer

A probe reward fixed the overshoot at `p_ref = 3` and failed at `p_ref = 1` — the probe had to be
set near the optimum for the correction to work. Same shape as a bandit choosing a grid endpoint
unanimously because the optimum sat at that endpoint.

**Lesson.** *Sweep any instrument's free reference parameter.* If the result survives only at the
value nearest the truth, the instrument is reading the truth rather than finding it.

### 9.8 The wrong instrument class, hidden behind a wrong objective

Adaptive amplitude selection was run as a bandit. Fixing its misspecified reward improved it and
still left it worse than a fixed amplitude — because every arm-pull permanently alters the learner,
so rewards are non-stationary and history-contaminated. UCB1 assumes neither. Repairing the
objective exposed the instrument error rather than curing it.

**Lesson.** *Check that the problem has the structure your algorithm assumes before blaming the
objective.*

### 9.9 A comparison declared "genuinely open" that was algebraically vacuous

The reviewer specified X2b's central contrast as D-opt vs an empirical rival and wrote *"whether
D-optimality or something else is the argmax is genuinely open."* The two designs were separated by
2.5 × 10⁻⁵ in the criterion's own units against a between-condition gap of 0.817. They were the same
design, reached at different points of a flat optimal face created by a near-parallel actuator pair.

**Lesson.** *Before claiming a comparison is open, compute the distance between its arms in the units
the hypothesis is about.* Two lines of algebra. Now hard rule 2c.

### 9.10 A harness bug shipped with a de-risked spec

The same reviewer who imposed rule 7 shipped precondition code in which the untrained floor and the
trained conditions were evaluated on **different test draws**, because `trained=False` skips the loop
that advances the RNG stream. The executor localised the resulting divergence to "upstream of
everything the experiment manipulates" without being able to see the code.

**Lesson.** *De-risking a spec is not de-risking the harness.* Diff the RNG consumption across
conditions.

### 9.11 Argmax tests waste power and reward imprecision

"Is D-opt the argmax, or within 1 SEM" passed — and passes *more easily the noisier the measurement
is*. On the same seeds and the same runs, ranking all 11 designs by the criterion gave ρ = 0.909,
p = 0.0001.

**Lesson.** *A test whose pass condition is helped by imprecision should not carry an experiment.*
Now hard rule 2d.

### 9.12 A shape test across unequal steps

X9's P3 asked whether the drop in reward-dependence was a *knee at sufficiency*. It compared **raw**
drops across k-steps of **unequal width** — one unit for `1→2`, two for `4→6` — and passed. Per unit
of k it fails.

**Lesson.** *A shape claim needs equal steps, or a per-unit normalisation stated in the
preregistration.*

### 9.13 A threshold test with no threshold

The same P3 presumed a sharp sufficiency point at k = d. Reconstruction error kept falling well past
it (0.020 → 0.005 → 0.002), so exactness was approached asymptotically and never attained. There was
no threshold for the knee to sit at, and the question had no referent.

**Lesson.** *Verify that a threshold exists before testing where it is.* Three of this programme's
four specified experiments could not answer their own question, and all three failures were
checkable in advance.

### 9.14 The sanity check was the experiment

X9's P2 — "divergence reaches the floor once capacity suffices" — was included as an obvious control.
It failed at every capacity, and the decoupling from reconstruction error is the only result in the
run that bears on the theory. The prediction designed to be informative (P3) was ill-posed.

**Lesson.** *Preregister the boring predictions too, and at the same level of care.*

---

## 10. Standing checklist

Before promoting any claim:

1. Does the framework **forbid the negation**? If not, it is not derived.
2. Have I derived the **dimension** and then assumed the **geometry**?
3. Does this claim inherit an **exception** from its premises?
4. Is this a **new quantity**, or a second bound on an existing one?
5. Is there a **chance floor** for this number?
6. Which **regime** does the imported intuition come from?
7. What does a **null** kill? If nothing, do not run it.
8. Am I measuring the **theory** or the **formalization**?
9. Is the recurrence a **shared derivation** or a shared silhouette?
10. Is the most quotable consequence one the result actually supports?
11. Is the optimum of my criterion **analytically trivial** for this setup?
12. Have I shown the advantage **exists** before testing whether an algorithm finds it?
13. Does my choice set **straddle** the interesting point?
14. How far apart are my conditions **in the criterion's own units**?
15. Is this an **argmax** test where a **monotone** one would use the same data better?
16. Do all conditions consume the **same RNG stream**?
17. Does my **shape** claim compare **equal steps**?
18. Have I verified the **threshold exists** before testing where it sits?

---

*Archived through v0.7. The theory files carry no provenance; it is all here.*
