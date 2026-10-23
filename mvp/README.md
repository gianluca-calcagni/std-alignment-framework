# Misalignment as evidence: the MVP

> **Status: a minimum viable version of the std-alignment-framework (Q80), built from its v14 draft; not approved, and
> reviewed only within the executor's model family.** Everything here is checked in CI. Start here; nothing else in the
> repository is needed to read, run or judge it.

## What it does

An **actor**, an AI system or any other, makes decisions. A **principal** declares, before looking at any record, what
it accepts: limits such as "never leak a customer's data" or "at most one wrong answer in twenty". The MVP turns a
record of the actor's decisions into:
- **verdicts**: *convicted* (the record shows a breach, at an error rate fixed in advance, whatever the dependence
  between decisions) or *certified* (the record shows the requirement met, within a margin, on average);
- **misalignment**: how fast the evidence of breach accumulates, in nats per decision, the same number read three ways:
  the growth of the best fair bet against the declaration, how fast the declaration makes the record improbable, and
  the distance to the nearest acceptable behaviour;
- **sizes**, in units that matter: how often a forbidden outcome happens, an expected cost, an overrun, each with an
  interval;
- **splits**: how much of the misalignment no available option could avoid, how much this actor could have avoided, and
  whether it is **culpable** at a declared standard of care; and how much a coarse record leaves hidden.

It does not model how the actor decides: a frozen model, a person and an institution are judged alike, by what they do.

## The ideas, in five lines

1. Outcomes are what a record notes of a decision, the situation included; the principal declares which part the world
   chooses, and the actor is never judged on how often the world posed each situation (`CORE.md`, D1, R1).
2. A specification is a list of requirements: per decision (convex: "each answer at most this risky") or pooled ("over
   the deployment, on average at most this") (D4).
3. Misalignment is the best growth rate of a bet that every acceptable behaviour calls fair (D5, R2); a test from such
   bets keeps its error rate however the actor's decisions depend on each other (R4).
4. A record convicts exactly, and certifies only an average, never that every decision was acceptable (R16, R17).
5. What the actor could have done, declared as an interface, splits misalignment exactly into what no option avoids and
   what this actor could have avoided (R14).

## Run it

```bash
pip install -e .                                  # the library, stdalign (numpy, scipy)
python3 mvp/examples/quickstart.py                # a support bot, from declaration to report, in seconds
python3 -m pytest mvp                             # every result's checks, the structure of the core, the quickstart
```

In code:

```python
import numpy as np
from stdalign import spec as S

p = np.array([0.70, 0.25, 0.05])                  # how often each outcome happens: fine, slow, harmful
limits = [S.rate_limit([2], 0.01, 3)]             # at most one harmful outcome in a hundred
m = S.misalignment(p, limits)                     # 0.0413 nats per decision, with a certified interval
harm = np.random.default_rng(0).random(5000) < 0.05                  # a record: was each decision harmful?
verdict, bounds = S.pooled_verdict(harm.astype(float), 0.01)         # 'convict', 'certify' or 'neither'
```

## A case on real data

`cases/m1-decoding-toxicity/`: a frozen GPT-2 completing prompts chosen to provoke, under three decodings, graded by a
public classifier, against a declared limit of one toxic continuation in ten. Registered before any computation. The
deployed decoding is convicted (toxic rate `0.326`, interval `[0.292, 0.360]`); the other decodings are more toxic, so
its misalignment is all unavoidable with this interface and it is not culpable
(`cases/m1-decoding-toxicity/RESULTS.md`).

## The files

| File | What it holds |
|---|---|
| `CORE.md` | ten definitions, each with what its object is in the world, and eighteen results, each with a proof and its checks |
| `checks/` | the checks: one or more per result, on random instances and degenerate cases; and the core's structure |
| `examples/quickstart.py` | the support bot, end to end |
| `cases/m1-decoding-toxicity/` | the case on real data: registration, scripts, rehearsals, results, report |
| `KNOWN.md` | what is known and used, with the sources read; what is new |
| `LIMITS.md` | what the MVP cannot do |
| `PLAN.md` | how the MVP was built, step by step |
| `../stdalign/spec.py` | the library: every quantity above, one function each |

## Status and licence

A draft for review. Its proofs were read adversarially by a model of the same family as the one that wrote them, which
found and fixed two false statements and several gaps (`../NOTES.md` §1); an outside review is the next step. Licensed
under the GNU Affero General Public License, version 3 or later, as the repository is.
