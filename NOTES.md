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
| known mathematics, organization not yet shown across disciplines | open: five ontologies (`ontologies/`), then one worked case each |

**Deferred from identifiability.** The "dynamic rank" (the dimension of the span of the revealed objectives along a
path, modulo constants) generalizes [P3] beyond rank one. It adds no verdict the core needs yet: [P3] already says when a
single objective explains a path. It stays on `main` until an ontology needs it.

**Order next.** Ontologies in their own folder: machine learning, biology, humans, institutions, and job delegation from
a manager to an employee. Each fills the same typed slots with items of the core, reframes one known result, and states
what the core predicts and where it stops. Then one worked case per discipline, on data the PI supplies.
