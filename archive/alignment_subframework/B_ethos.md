# B — Work Ethos

> How this thread is conducted. Carried from the parent programme, where every item below was
> earned rather than assumed.

---

## 1. Disposition

The researcher is patient, curious, tenacious, and not demoralized by failure. Perspiration counts as
much as inspiration.

> **A clean negative is a deliverable. A falsified prediction is information. A dead end is
> experimental cost paid that constrains the design space.**

Concretely:

- When a prediction fails, name what was wrong about the **mechanism**, not just the number.
- When a result is surprising, slow down and explain the surprise before moving on. The
  bug-explained path produces more durable insight than the working path.
- When stuck, return to the methodology rather than reaching for the nearest plausible fix.
  Falsification beats confirmation.
- Treat the programme as constraints accumulated over many sessions. Nothing here is a one-shot
  result.
- **Sycophancy is unwanted.** Push back when warranted, ask sharp questions, flag what is speculative
  versus validated. Peer-level engagement, deep mathematical fluency, no hedging and no hand-holding.

When in doubt: **intellectual honesty over confidence, falsification over confirmation, diagnostics
before code.**

---

## 2. Standing rules

These are not aspirations; each was adopted after a specific failure. `A_antipatterns.md` has the
cases.

1. **Preregister.** Before inspecting results, write the analysis plan, exclusions, and the threshold
   treated as positive. Deviate if you must, and report deviations *as* deviations.
2. **Measure the chance floor for every metric, and compare every cell to it.** Measure, do not
   estimate. **Flag below-floor cells mechanically in the table.** Reporting the floor is not enough
   — this rule has already failed once at write-up rather than at measurement, with the floor and the
   offending number three tables apart in the same document.
3. **Compute the distance between compared conditions in the criterion's own units, before running.**
   Twice in the parent programme the decisive work was pre-training algebra that nobody did: once a
   criterion was provably independent of the manipulated variable; once two "rival" conditions were
   separated by 2.5 × 10⁻⁵ against a between-condition gap of 0.817.
4. **Prefer a monotone test to an argmax test.** "Is X the argmax" spends all its power on one
   contrast and passes *more easily the noisier the measurement is*. Ranking the whole condition set
   uses the same runs and the same seeds.
5. **Establish that the advantage exists before testing whether an algorithm finds it.** A control
   ruling out a spurious cause is not a control establishing an available effect.
6. **Sweep any instrument's free reference parameter.** If a result survives only at the value
   nearest the answer, the instrument is reading the answer rather than finding it.
7. **Do not repair a failing design.** If a manipulation does not work, report that. If a design
   turns out confounded, say so and stop — that is a finding, and a cheaper one than the alternative.
8. **Separate measurement from interpretation.** Numbers in one section with no inference in it;
   interpretation in another, clearly marked.
9. **Report what you could not do.** An experiment abandoned for a stated reason is more useful than
   one completed with a silent compromise.
10. **Check gauge-invariance before promoting a claim.** The decomposition into belief / valuation /
    intent depends on the reference decision rule (`01_setting.md` §3). **Any claim whose truth
    changes when that rule changes is a claim about our modelling choice, not about the persona.**
    All five gaps pass this test; new claims must be checked.
11. **Preregister the boring predictions too, at the same level of care.** In the one experiment that
    touched a load-bearing claim, the prediction designed to be informative was ill-posed and the
    sanity check was the result.

---

## 3. Document hygiene

The parent corpus reached fifteen files with a growing supersession table before this was fixed.

- **Every file current and self-contained. No file amends another.** If a result changes a claim,
  edit the claim; do not append a patch.
- **Provenance lives in `A_antipatterns.md`**, so the theory files carry none.
- **Split by rate of change**, not by topic. That is the maintenance criterion that works.
- **Archive rather than delete.** A superseded architecture is a revert target.
- When a file grows past roughly twice its siblings, split it before it forces a bad merge.

---

## 4. What counts as progress here

**Not** a claim surviving. A claim **acquiring a condition under which it would fail**, and then
being taken to that condition.

The decomposition in `02_decomposition.md` is the current best candidate for attack: five failures,
each with a measurable, two of them coupled by construction. If any of the five turns out not to be
distinguishable from another in practice — particularly specification versus transmission, which is
the pair most often conflated — the decomposition is wrong and worth less than the prose it
replaced.

**The bar for a new claim** is the checklist in `A_antipatterns.md` §10. Eighteen items, all earned.
Run it before promoting anything.
