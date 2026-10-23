# The MVP plan

> **Status: the plan of record (Q80), set by the executor at the PI's request; it takes priority over `ROADMAP.md`'s
> recommendations and backlog until it is done.** Each step lists its exit criterion; a step is done when the criterion
> holds and CI is green on the commit that meets it.

## What the MVP is

The smallest version of the framework that a person outside the project can read, run and judge, with nothing in it
that is unchecked, undeclared or overclaimed. It is v14's first layer and the part of its second that diagnoses, on
finite outcomes, written as checked items, with a library, a quickstart and one case on real data. The PI plans to
publish it from a second repository, cleaned for readers; this folder is its source.

**In.** One distribution on finite outcomes, with the world's part declared; a specification as requirements, per
decision (convex, closed) or pooled (closed, over a horizon); misalignment as the evidence against the per-decision
ones; bets, and tests valid under any dependence; the verdicts convict and certify, certify for averages and samples
only; the record's resolution and its hidden part; the interface's feasible set, unavoidable misalignment, the avoidable
excess and culpability at a declared care margin, with the exact factorization along feasible sets; severity as a
declared budget, reported beside misalignment.

**Out, and named as future work.** PURPOSE and SHAPING (aims, training); outcomes that are not finite (the general
twins); orders beyond a family of criteria with a reference; latitude, perplexity and confusion; the junctures,
contamination and the record's signature as a declared object (Q77, pending R24); the label protocol and L2 (R23).
Nothing out of scope is deleted from the repository; the MVP only does not depend on it.

## Steps

| # | Step | Exit criterion |
|---|---|---|
| P1 | this plan, and the records that put it first | `ROADMAP.md` points here first; a decision row (Q80) |
| P2 | `mvp/CORE.md`: the definitions, each with its interpretation, and the results, each with a statement, plain terms, a proof and the checks that test it; including a certificate for a pooled rate, derived here, and the impossibility of certifying every decision (Q76) | every item complete; every proof read against its statement by a reviewing subagent, its findings fixed |
| P3 | the library, `stdalign/spec.py`: misalignment against declared linear requirements with the world's part; the closed form for a rate limit; a bet and its test; the certificate; the factorization along feasible sets; the split along the record's resolution; a report as data | unit tests pass on both SIMD paths; every function mutation-tested |
| P4 | `mvp/checks/`: at least one check per result, on random instances and degenerate cases, with tolerances from the quantity's scale; a structural check that every item has its fields and cites checks that exist, and every check is cited | all pass on both paths; mutants of the checks caught or explained |
| P5 | `mvp/examples/quickstart.py`: from a declaration to a report in under a minute, on simulated data | CI runs it |
| P6 | one case on real data, `cases/m1-decoding-toxicity/`: a frozen public language model under several decodings, judged by a public classifier against a declared rate limit; convict or certify, the factorization by the decodings available, culpability; one empirical prediction, labelled; registered and pushed before any computation | registration pushed before the run; results and a report recorded, whatever they say |
| P7 | `mvp/README.md` to start from, `mvp/LIMITS.md`, and `mvp/KNOWN.md`, what is known and what is new, citing only sources read | a reader can go from README to a run without another file |
| P8 | an adversarial reread of the whole MVP by a subagent of the executor's model family (not independent, rule (f)), its findings fixed; then the PI's external review asked for | findings fixed; the request for review in `REQUESTS.md` |

## What the MVP does not need from the PI

The decisions it rests on are taken (Q70, Q74, Q76). Pending requests (R23, R24, R25) are outside its scope. At the end
it needs one thing only: a review by someone outside the executor's model family, before the PI publishes it.
