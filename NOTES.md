# NOTES — the executor's working notes

Not part of the core, and not checked by lint. Blunt on purpose. A hunch is not a claim: nothing moves into `CORE.md`
without a proof and a check. Names, and correspondences with the literature, with their confidence levels, live in
`TERMS.md`.

## 1. Failure modes

The full table, with its evidence, is on `main`: `70 Project/NOTES_claude.md` §1. More from building this core:

| Failure mode | Evidence | Countermeasure |
|---|---|---|
| **A check that omits the constraint it tests** | the ray-minimizer check never required `t* ≥ 0`; a mutant that pursued `−F` passed | mutation-test every new check before recording it: break the mathematics on purpose and watch it fail |
| **A tolerance without its scale, again** | the ray-closedness check compared a tight bound with no rounding margin (1.79134602e-43 against itself) | every comparison gets the relative margin of `EXACT`, including the "obvious" ones |
| **A justification leaning on a later result** | D3 cited P5 while P5 came after it; lint rule R5 caught it | keep R5; write the "why" from what is above |
| **A check helper that misclassifies at the edge of float64** | at intensity 40, the coarse actor's mass off the best outcome (about `1e-34`) vanished from its mean of `F`; the helper took the "all mass on the best outcomes" case and returned `+∞` | keep check instances where float64 represents every mass; test limits by their own formula |
| **A familiar formula that hides a typing error** | "the KL-regularized optimum is `tilt(π_ref, r/β)`" is true prompt by prompt, and false on prompt–response pairs: the pursuit ray of [D2] would also reweight the prompts, which no policy can do. Found only when the ontologies had to say what an outcome is | typed slots in every ontology, including **contexts**; a formula from the literature enters only with its outcome space stated |

**One that worked.** "Misalignment of a coarse actor grows with effort" was the natural claim from main's B1 ("rises with
budget"). A 400-instance probe before writing it found 123 non-monotone cases, so [P8] claims only the small-effort law
and exhibits a counterexample. The rule "a shape claim needs a random sample before it is said" (main, §1) paid off.

## 2. Is the core a compelling standard yet?

Not yet: a credible foundation. The PI has the full assessment. Progress against the gaps listed after the second
review:

| Gap | State |
|---|---|
| everything is relative to a declared specification; no sensitivity result | **closed by [P10]**: an error in the default moves misalignment by at most its spread, and an error in the objective by at most the revealed intensity times its spread |
| no resolution: cannot say "I don't care about these details" | **closed by section 4**: [P7] forgives exactly the within-cell departure; [P8] gives the coarse actor's unavoidable misalignment and its small-effort law |
| no stakes report | **closed by [P9]**: the shortfall at matched intensity splits into misalignment, under-pursuit and anti-pursuit; misalignment is scale-free, stakes are not |
| identifiability: what can be read from behaviour, and what cannot | **closed in part by section 6**: [P11] the misaligned share at the start of any change; [P12] pass-through is identified from behaviour alone, and revealed objectives certify an actor's distinctions but cannot prove their absence |
| no estimation layer | open: the deviance identity of [P5] is the way in; [P12](i) needs it to be tested on data |
| known mathematics, organization not yet shown across disciplines | **addressed by `ontologies/`**: five disciplines, each with typed slots, one known result, and claims labelled as consequences, predictions or readings (lint rule R10). Next: worked cases, which need data |
| what one change of behaviour gains, not only what it misaligns | **closed by [P13]**: the average moves at the covariance rate (the Price equation), and at the start each unit of departure gains `cos θ` of the objective's spread |
| outcomes that are partly fixed before the actor acts (contexts) | **open, found by the ontologies**: see the design question below |

**Deferred from identifiability.** The "dynamic rank" (the dimension of the span of the revealed objectives along a
path, modulo constants) generalizes [P3] beyond rank one. It adds no verdict the core needs yet: [P3] already says when a
single objective explains a path. It stays on `main` until an ontology needs it; none did.

## 3. Design question for the PI: contexts

**What was found.** In four of the five ontologies, part of an outcome is fixed before the actor acts: the prompt a
model answers, the patient who arrives, the request a manager sends, a person's circumstances. The actor chooses only
what happens within each context. The core's pursuit ray reweights whole outcomes, contexts included, which the actor
cannot do. So within one context every item applies as stated, but "pursue `F`" across contexts is not yet defined by
the core.

**What the ontologies do meanwhile.** They apply every item context by context. Across contexts they use the
specification "pursue `F` in every context, at any intensity in each", which is a specification by [D3]; when the
actual behaviour has the default's context masses, its misalignment is the average of the per-context misalignments,
by [P4](iii). [P13](i), and the first limit of [P13](ii), hold across contexts as stated.

**Options.**
- **A (recommended): one shared intensity.** A definition: a resolution of *contexts* is one whose cell masses every
  behaviour of the actor shares with the default; the standard specification in contexts is pursuit of `F` within every
  context at one shared intensity. Then a proposition, to be proved and checked: (i) it is the unique maximizer of net
  value among behaviours with the default's context masses (the per-context form of [P4](i)); (ii) its misalignment is
  the average of the per-context misalignments plus an inconsistency term, never negative, which is zero when one
  intensity is nearest in every context. Why one intensity: "pursue `F`" names one objective on all outcomes, and
  pursuing it at different intensities in different contexts is pursuing a different objective, `t(C)·F`, which [P1](ii)
  tells apart from `F`. KL-regularized fine-tuning, with one `β` for all prompts, is exactly this specification. The
  report-card prediction (`ontologies/institutions.md`) needs it; the delegation ontology asks for it.
- **B: free intensity per context.** Keep what the ontologies do now. It needs no new item, but it forgives an actor
  that pursues hard in some contexts and not at all in others.

Either way the change is an addition (one definition, one proposition, a new section), not a refactoring: no existing
item changes.

**Order next.** The PI's decision on contexts. Then worked cases, one per discipline, on data the PI supplies, each
pre-registered: the first candidates are the predictions in the ontologies that need only published or easily
collected data (the pass-through ratios after automatic enrolment; the best-of-`n` slope from initial-policy samples).
