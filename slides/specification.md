<!-- theme: default -->
<!-- paginate: true -->
<!-- style: "section { font-size: 26px; }" -->

# Declaring a specification

What a principal writes down before any record is read, what it implies by itself, and what must be stated outright

The v14 draft (`v14/constraints.md`, the last section). Nothing in v14 is approved yet.

---

## The one object

A **specification** is a list of **requirements**. Each requirement is a set of acceptable behaviours, and every
acceptable behaviour lies in all of them.

- A **behaviour** says how often each outcome happens, in each condition the actor faces.
- Every requirement for which a mix of acceptable behaviours is acceptable is a list of limits on averages: "on
  average, at most this much of that" (VK0).
- So a **constraint** and a requirement are the same kind of object. "Constraint" names the ones stated absolutely,
  with no reference.

Named "specification" by the PI's decision (Q70); the draft called it "the request".

---

## Three absolute forms

| Form | Says | Example |
|---|---|---|
| forbidden outcome | never this | never leak a customer's data |
| rate limit | this, at most so often | at most 5% wrong answers |
| budget | this average, at most so much | at most 30 seconds per answer, on average |

A forbidden outcome is a rate limit of zero; a rate limit is a budget on how often something happens.

---

## Some requirements come with no constraint written

| Declared | What it already requires |
|---|---|
| the outcomes | nothing outside them can be required |
| the conditions and how often each arises | the actor does not choose its situations |
| what the principal does not care about | nothing inside those groups of outcomes |
| a reference and the targets it must not lose on | no worse than the reference on each target |
| a ranking and a reference | at least as often as the reference at every standard |

---

## Conditions are a requirement too

The actor does not choose how often each kind of question arrives.

- Support bot: wrong in 2.9% of open questions, 35.3% of account questions; 12.6% overall; the limit is 5%.
- Judged as one pool: 0.0440 nats per decision.
- Judged with the frequencies of the conditions held fixed: **0.0496** (VK6).

The pooled number understates the evidence: the nearest acceptable bot must lower its wrong answers in each kind of
question, not in the pool.

---

## A reference can forbid by itself

The previous version never leaked. If "not leaking" is one of the targets it must not lose on, the new version must
never leak either: a forbidden outcome, with no constraint written (TG1).

But only when:

- there is a reference;
- the reference meets the standard;
- the quantity is one of the targets.

---

## When a constraint must be explicit

When nothing else in the specification implies it:

- **no reference**: a legal limit, "never";
- **a quantity no target scores**: side effects, cost, latency, privacy;
- **a tolerance that is not the reference's**: the previous version leaks too, or is held to a looser limit;
- **a forbidden outcome the reference produces**;
- **a requirement across conditions**: "act alike whatever the user's name".

---

## May, not can

The specification says what the actor **may** do. The **interface** says what it **can** do: what it sees, what actions
it has, how the world responds.

| Situation | Where it goes | What the report shows |
|---|---|---|
| the actor cannot do something | interface only | nothing to judge |
| the principal requires what no feasible behaviour does | specification | unavoidable misalignment |
| the interface makes a requirement automatic | specification still | nothing now; a new version may differ |
| an optimizer under a binding requirement | specification | a shadow price, in its objective's units |

---

## Why not put abilities in the specification

- A capability the actor lacks needs no requirement: no record can show it.
- Declaring it as one would make an inability look like obedience.
- A requirement nobody can meet is not an error: the factorization reports it as **unavoidable**, and culpability is
  judged against the best the actor could do.

---

## What a limit costs in evidence

For an actor held fixed, loosening a budget by one unit removes about **λ\*** nats per decision of evidence, where λ\*
is the stake of the best bet against it (VK7).

- The stake depends on the actor and the budget: no constant converts the budget's units into evidence.
- This is where severity, a cost the principal declares, meets misalignment (`v14/severity.md`).

---

## In five questions

1. What are the outcomes, and the conditions with how often each arises?
2. Which distinctions between outcomes does the principal not care about?
3. Is there a reference, and on which targets must it not be beaten?
4. What is required absolutely: forbidden outcomes, rates, averages?
5. What can the actor see and do?

The first four make the specification, written and dated before any record is read. The fifth is the interface: it
explains verdicts, it never changes them.

---

## Where things are

| File | Holds |
|---|---|
| `v14/constraints.md` | the forms, VK0–VK7, and the section on declaring |
| `v14/targets.md` | a family of targets with a reference (TG1) |
| `v14/resolution.md` | what the principal does not care about (RS3) |
| `v14/interface.md` | the interface |
| `probes/v14/resolution.py` | the numbers of VK6 and VK7 |
