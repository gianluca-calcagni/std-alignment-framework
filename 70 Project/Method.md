---
id: "Method"
type: "method"
source_file: "F_method.md"
updated: "2026-09-26"
---
# F — Method

## Abstract, in plain terms

How this work is conducted, and why each rule exists.

Every rule below was adopted after a specific failure, and the failure is written next to it. That is
deliberate: rules stated as principles get forgotten, and rules stated as scar tissue do not. The
governing attitude is that **a clean negative is a result**. In this programme it has been the *only*
kind of result — every finding so far came from something failing a check rather than from something
working as predicted.

> Provenance lives here and nowhere else; the theory files carry none.

---

## 1. Disposition

The researcher is patient, curious, tenacious, and not demoralized by failure. Perspiration counts as
much as inspiration.

> **A clean negative is a deliverable. A falsified prediction is information. A dead end is experimental
> cost paid that constrains the design space.**

- When a prediction fails, name what was wrong about the **mechanism**, not just the number.
- When a result is surprising, slow down and explain the surprise before moving on. The bug-explained
  path produces more durable insight than the working path.
- When stuck, return to the methodology rather than reaching for the nearest plausible fix.
  Falsification beats confirmation.
- Treat the programme as constraints accumulated over many sessions. Nothing here is a one-shot result.
- **Sycophancy is unwanted.** Push back, ask sharp questions, flag speculative versus validated.
  Peer-level engagement, deep mathematical fluency, no hedging and no hand-holding.

When in doubt: **intellectual honesty over confidence, falsification over confirmation, diagnostics
before code.**

**What counts as progress:** not a claim surviving, but a claim **acquiring a condition under which it
would fail**, and then being taken to that condition.

---

## 2. Standing rules, with their cases

### R1 — Preregister
Before inspecting results, write the analysis plan, exclusions, and the threshold treated as positive.
Deviate if you must, and report deviations *as* deviations.

### R2 — Measure the chance floor for every metric, and flag below-floor cells **in the table**
*Case (4.1).* A passive learner scored MCC = 0.411 and was written up as "low, but learning something."
An untrained encoder scores **0.571**: MCC has a high floor at three dimensions. The learner was *below*
chance — it destroyed the accidental alignment present at initialisation.
*Case (9.6).* The rule was then followed — floor measured, tabulated, rationale cited in the same
document — and not applied across two tables three pages apart. A cell sat 0.21 below its own measured
floor and was reported as the low end of a performance curve.
> **A rule that says "report X" does not cause X to be used. Make the comparison mechanical.**

### R3 — Compute the distance between compared conditions in the criterion's own units, before running
*Case (9.9).* A contrast was declared "genuinely open" between two designs separated by 2.5 × 10⁻⁵ in the
criterion's own units, against a between-condition gap of 0.817. They were the same design, reached at
different points of a flat optimal face created by a near-parallel actuator pair.
*Case (9.2).* Actions were additive on the latents, so the thing chosen and the thing estimated lived in
the same space with the same coordinates. `log det` then separates into a design term and a constant and
D-optimal design is **uniform** regardless of anisotropy. Two lines of algebra would have caught it.

### R4 — Prefer a monotone test to an argmax test
*Case (9.11).* "Is D-opt the argmax, or within 1 SEM" passed — and passes *more easily the noisier the
measurement is*. On the same seeds and runs, ranking all 11 designs gave ρ = 0.909, p = 0.0001.

### R5 — Establish that the advantage exists before testing whether an algorithm finds it
*Case (9.1).* An adaptive design rule was compared against a fixed baseline with a control ruling out
genericity of adaptivity, and no control showing the effect *existed*. A post-hoc sweep put the optimum
at exactly the baseline: no design could have won.
> **A control that rules out a spurious cause is not a control that establishes an available effect.**

### R6 — Sweep any instrument's free reference parameter
*Case (9.7).* A probe reward fixed an overshoot at `p_ref = 3` and failed at `p_ref = 1`. The probe had
to be set near the optimum for the correction to work.
*Case (9.3).* An adaptive bandit selected the grid endpoint in 12/12 seeds — an artifact of the optimum
lying at the endpoint. A straddling grid showed the rule overshoots by 3–10×.
> **Unanimity across seeds is not evidence when the choice set is bounded at the interesting point.
> Always straddle.**

### R7 — Do not repair a failing design
If a manipulation does not work, report that. If a design turns out confounded, say so and stop — that
is a finding, and a cheaper one than the alternative.
*Case (9.8).* Adaptive amplitude selection was run as a bandit. Fixing its misspecified reward improved
it and still left it worse than a fixed amplitude — every arm-pull permanently alters the learner, so
rewards are non-stationary and history-contaminated, which UCB1 assumes away. Repairing the objective
exposed the instrument error rather than curing it.

### R8 — Separate measurement from interpretation
Numbers in one section with no inference in it; interpretation in another, clearly marked.
*Case (9.5).* A passing contrast (`A-greedy < A-dopt`) would have been written up as "the coverage term
adds design value." Given a later exponent sweep, the same number reads as "the coverage term pulls the
greedy rule back toward the optimum it was departing from." Opposite mechanisms, one measurement.
> **Before interpreting a passing contrast, ask what else would produce that number.**

### R9 — Report what you could not do
An experiment abandoned for a stated reason is more useful than one completed with a silent compromise.
*Case (9.10).* A de-risked spec shipped with a harness bug: the untrained floor and the trained
conditions were evaluated on **different test draws**, because `trained=False` skips the loop that
advances the RNG stream.
> **De-risking a spec is not de-risking the harness. Diff the RNG consumption across conditions.**

### R10 — Check that a claim is about the world and not about the modelling choice
Any claim whose truth changes when an arbitrary modelling convention changes is a claim about the
convention. Three successive versions of this framework asserted that their central quantities were
convention-free and then built those quantities out of a stipulated decision rule. **The current core
avoids the problem by construction** — everything is a functional on behaviour, with no internal state
and no assumed decision rule — but the rule stands for anything added later.

### R11 — Preregister the boring predictions too, at the same level of care
*Case (9.14).* "Divergence reaches the floor once capacity suffices" was included as an obvious control.
It failed at every capacity, and the decoupling from reconstruction error is the only result in the run
that bears on the theory. The prediction designed to be informative was ill-posed.

### R12 — Document hygiene
- **Every file current and self-contained. No file amends another.** If a result changes a claim, edit
  the claim; do not append a patch.
- **Provenance lives here**, so the theory files carry none.
- **Split by rate of change**, not by topic.
- **Archive rather than delete.** A superseded architecture is a revert target.
- When a file grows past roughly twice its siblings, split it before it forces a bad merge.
- ⚠ Review adds: **a rename is not done until it is done everywhere.** The `σ(Φ) → 𝒞_t` rename was
  announced in one file and left standing in two others, including the handover's headline result.

---

## 3. Theory-building anti-patterns

### 3.1 Over-unification

**Gradient hacking, claimed as derived.** A level-nesting produced a table in which each pattern recurs
at the interaction, developmental and formative levels. Two cells were attested; the third (gradient
hacking) was written up as a *derived prediction* and became the showcase item. But the nesting makes
the pattern *natural*; nothing forces every pattern to instantiate at every level.
> **A structural analogy is not a derivation.** The test is whether the framework **forbids the
> negation**, and a table of parallels almost never does.

**The circumplex, overclaimed.** From "the objective functional has two parameters" came "the emotion
circumplex is the appraisal-function's output space." What actually followed is that affect is *at least
two-dimensional*; the circularity and the quadrant labels do not.
> **Derive the dimension, not the geometry.**

**Interior optima, deliberately not unified.** Three results share the shape "two opposing pressures on
a scalar, hence an interior optimum": gain, intervention amplitude, evaluative-channel capacity. That
shape is generic to nearly any optimization.
> **Recurrence of a generic form is not evidence of a common mechanism.** The bar is a shared
> derivation, not a shared silhouette.

### 3.2 Conflation

**Non-identifiability and superposition under one label.** Non-identifiability is *derived* (no
interventional variation ⇒ diffeomorphism ambiguity). Superposition is a *capacity* claim the framework
accommodates and does not generate.
> **When two phenomena co-occur in the literature, check whether your derivation reaches both.** It
> usually reaches one.

**Two constraints bounding one quantity.** Narrowness (capacity must be low) and discriminativeness
(must not be too low) were carried as two independent constraints for four versions. They bound the same
quantity from opposite sides; recognising it reduced five constraints to four, one being an interval.
> **Before adding a constraint, check whether it bounds a quantity an existing one already bounds.**

### 3.3 Errors of statement

**A derived claim inherits every exception its premises carry.** "Nothing motivates except as retained"
was written flatly, contradicting a bypass channel established three subsections earlier. Corrected to
"…except as retained, **or via the bypass channel**."

**A placeholder in a definitional slot is load-bearing.** `self-construal` was chosen for parallelism,
known to be poor, and survived two versions before being replaced by a term available in the canonical
literature the whole time.

### 3.4 Methodological errors

**Name the regime before importing the intuition.** A prediction that the well-excited latent axis would
be best identified was reversed, consistently: an *estimation* intuition was applied where the binding
constraint was *approximation*. Larger interventions improve detection and worsen fitting; noiseless and
nonlinear, the second dominates. The failure produced the amplitude-as-design-variable refinement; the
confirmed half produced nothing.

**A cheap uninformative experiment costs more than it looks**, because it produces the appearance of
testing. Cost is not the ranking criterion; what a null kills is.

**State the regime a criterion requires when you specify it.** *(9.4)* A spec was noiseless with a
bijective observation map; D-optimality minimises estimator variance, which was identically zero. The
criterion had nothing to optimise.

**Verify that a threshold exists before testing where it sits.** *(9.13)* A test presumed a sharp
sufficiency point at k = d; reconstruction error kept falling past it (0.020 → 0.005 → 0.002), so
exactness was approached asymptotically and never attained. The question had no referent.

**A shape claim needs equal steps.** *(9.12)* A "knee" test compared raw drops across k-steps of unequal
width and passed; per unit of k it fails.

### 3.5 Premature conclusions from selection effects

A derivability audit found every derivation tracing to three sources and recommended formalizing the
objective side first. Immediately afterwards, the state side produced four derivations in one sitting
once it was asked for consequences rather than merely stated. The two productive regions were the two
with imported mathematics already attached.
> **An audit of a partly-formalized theory measures the formalization, not the theory.**

### 3.6 Architectural reversals

**Do not build a known-false idealization into a definition.** An earlier architecture made the inner
state a triple with a map each — but that split *is* the separation principle, which holds only under
exactness. Demoting factorization to a gradable property cost error localization, representational
goal-safety, and update-map tractability; it bought psychoactive impairment of cognition, emotional
distortion of belief, belief perseverance, the Nisbett–Wilson split, a strengthened retention bottleneck,
and a measurable persona-level parameter.

**A proposed extension is only compelling if it explains something the current version could only
report.**

**Before adding a dimension, check whether the phenomenon is a change of condition on an existing one.**
"Other-facing" was considered as a third row and rejected: another persona is not a different *kind* of
target, it is a target that contains a model of you, making the backward leg a fixed-point equation.
Convexity survives; the linear-maximization oracle dies.

### 3.7 Attractive symmetries, hunted and found null

An expected inward/outward symmetry — two optics, two reaches — resolved to **one body, two control
coordinates**. The null produced wireheading's geometric characterization and grounding as a
measurability condition.
> **Chase the symmetry, but bank the null.** The shape of the negative answer is where the content was.

### 3.8 Seductive mappings, flagged rather than promoted

Dream phenomenology as open-loop rollout, and depressive rumination as open-loop compounding with
behavioural activation restoring the correction step. Consistent with the derivation; not forced by it.
> **The most quotable consequence of a result is usually the one it does not support.** Mark it at the
> moment of writing.

---

## 4. Standing checklist — run before promoting any claim

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

**Four items earned by this corpus rather than the parent**, each traceable to a specific failure in the
previous version:

19. **Is the condition stated as a measurability fact where a rate or a cost is meant?** A measurability
    condition with no threshold is generically satisfied and yields a vacuous impossibility. *Earned by:
    grounding stated as `𝒮_t`-measurability, which was generically true and therefore empty.*
20. **Have I defined the thing I am decomposing, independently of its decomposition?** *Earned by:
    "alignment holds iff all five gaps close", the only definition of alignment in six files.*
21. **Is this a property of the pair, or of the chain?** A claim about principal and agent that never
    uses the principal's own compression is probably a chain claim collapsed to two links. *Earned by:
    the principal was declared a persona and the fact was never used, which cost the entire composition
    analysis ([[Dictionary index|Dictionary]]).*
22. **Does the failure I am diagnosing have a response signature that another locus shares?** Two loci
    with the same signature under the available manipulations are not distinguishable, whatever the
    theory says. *Earned by: two loci both answering "more signal does not help", which invalidated a
    nominated first experiment.*
23. **Has every preregistered criterion been shown, in writing, to be a function of the manipulated
    variable?** Not "checked" — written down, per prediction, inside the preregistration. *Earned twice:
    once by a design abandoned at its own pre-run check, once by a prediction that was void by symmetry
    because the same check was skipped when the design "felt cleaner".*
24. **Is the check reportable, or only pass/fail?** Record the distribution of the quantity being
    verified, not merely whether it violated a bound. *Earned by: an arithmetic check that found no
    violations and, because the distribution was printed, falsified the tightness claim attached to the
    thing it was verifying.*
25. **Is this claim prettier than its evidence?** *Earned by: nine self-found retractions, every one of
    which made the theory more elegant — a tight bound, a single unifying object, an irreducible floor,
    a clean impossibility. The bias in this programme is not toward confirmation in general; it is
    toward elegance.*

### On the shape of this list

Items 1–18 are about experiments; 19–22 are about *statements*. That the second group had to be added
after a framework-level review, rather than after a failed run, is itself a finding: **the previous
version's errors were nearly all made at the point of writing a condition down, not at the point of
measuring it.** Pre-run algebra catches the first kind. Nothing but adversarial reading catches the
second, which argues for making external review a scheduled step rather than an occasional one.

---

## 5. Items earned in reviews R2–R6 and the v6 rebuild *(appended from v6 on; §§1–4 unchanged)*

Each item is traceable to a specific failure recorded in [[Status 02 Retraction history|Status §2]].

26. **Before bounding a quantity, ask whether it has a closed form.** *Earned by:* five versions bounded
    `R_J`, which equals `KL(p̂‖p*)/β` (rows 31–35).
27. **When a slot is restricted to a set, check that the restriction is well-typed and non-vacuous, then
    re-run the check under the restricted reading.** *Earned by:* `osc_δ` — the "sup − inf of a function
    over a set of distributions". The 0 / 20,000 check had verified the unrestricted reading only (row 32).
28. **A correlation with a constant is not evidence of independence.** Print the standard deviation of both
    variables beside any correlation. *Earned by:* "+0.001, s.d. 0.000" (row 33).
29. **Before claiming a property of a feedback loop, fix the controller class, and check that the claimed
    equilibrium is one.** *Earned by:* `e*(τ)`, which was the centre of a sustained oscillation under
    proportional control, and zero under integral control (row 45).
30. **Propagate a retraction by search, not by memory.** Grep every file for the retracted sentence.
    *Earned by:* the interior optimum, retracted in one file and asserted in three (row 37).
31. **Before calling a parameter a property of the system, list what the observations identify.** If only
    a product or a quotient is identified, the parameter is a convention. *Earned by:* `β` and the unit of
    `F` (row 40); `D_⊥` was named "misalignment proper" before its sign case was checked (row 50).

32. **Derive a prediction's conditions from the theorem it rests on before writing it down.** *Earned by:*
    the crossing test was proposed with matched variances. The limits of Thm [[Thm 9|9]] say matched variances give a
    tie at small capacity, not a crossing (row 51).

33. **Name the counterfactual in every regret.** "Regret against the intended actor" is not defined until
    you say what the intended actor holds fixed — price, budget, or neither. *Earned by:* the same-price
    convention was presented as *the* measure of misalignment, and price and budget disagree on 11.4 % of
    error pairs (row 56).
34. **State the scope in the headline, not only in the scope section.** *Earned by:* the v6 README called
    the package "a formalization of alignment for bounded actors", which reads as general; the scope
    conditions that say otherwise were at the end of A (row 52).

35. **Test a stated boundary against a case that violates it formally but may be absorbable.** *Earned by:*
    condition (X) excluded any reference that depends on behaviour. The rational-inattention reference is
    such a case, and it keeps an exact regret identity (row 59).
36. **Check every new worked example against the canonical definitions, not the ones you remember.**
    *Earned by:* the first draft of [[B13]] said free riding has `D_⊥ = 0`. That is the full-ray answer; the
    canonical half-ray gives `X_anti > 0` and `D_⊥ = KL(p̂‖q)` (caught before release, [[R4_LOG]] §5).

37. **Check a replacement claim under every declared convention and actor class before shipping it.**
    *Earned by:* row 39's replacement ("rescaling is not harmless") was true only under the price
    convention, and the package's own default is the budget convention (row 61). The same failure produced
    row 66: a sign criterion stated for all optimizers held only for the Gibbs actor.
38. **A plain-language sentence must carry the qualifiers of the theorem it summarizes.** *Earned by:*
    "if a misalignment is cheap, it is also hard to detect" dropped both "in nats" and "for the entropic
    actor" (row 62).
39. **Have your own test-set routing redone blind by someone else before quoting it.** *Earned by:* the
    independent re-routing moved the fully-expressible share from 35 % to a 25–35 % band. Twelve generous
    calls shared one pattern — a learning mechanism rated as static — that the router could not see (row 65).

40. **When tiering a result, separate the model of the intended actor from the model of the actual actor.**
    *Earned by:* Thm [[Thm 1|1]] was stated for every `p` yet filed as needing a Gibbs actor. Tier 2 was stated for
    "any optimizer" yet needs an exact maximizer (rows 67–68).
41. **Report a measurement that sits on its threshold as nested shares with a band, not as pass or fail.**
    *Earned by:* the census's "specific" share landed at 55–61 % against a 60 % rule (row 72).
42. **Re-read the goal before each turn, and name the criterion each task serves.** *Earned by:* three
    consecutive rounds went into measuring generality after the answer had converged (R6 refocus,
    [[R6_LOG]] §1).

**Correction to R10, recorded here rather than by editing §2.** R10 says the current core assumes no decision
rule. That was false for v5 and is false for v6: the actor is an exponential tilt of the reference, which is
an assumed decision rule. Every exact result depends on it, which is why it is the weakest joint
([[C07|C7]]). R10's warning applies to the core itself.
