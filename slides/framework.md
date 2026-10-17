<!-- theme: default -->
<!-- paginate: true -->

# A standard framework for alignment

What it is, and how to use it, on one simple example

The v14 draft, on the branch `claude/core-v14` (October 2026). Nothing in v14 is approved yet; `main` holds v13.

---

## The question

Alignment compares **what an actor does** with **what a principal intended**.

- The actor can be a model, a person, an institution or an organism.
- The principal is whoever declares what is wanted: a company, a regulator, a user.
- The framework says what "misaligned" means, how a record shows it, and what it cannot show.

---

## Why a framework

Alignment's usual words are defined one by one, informally: reward hacking, deceptive alignment, goal
misgeneralization, tampering.

The framework asks three things of every word it uses:

- a **definition** in mathematics, with what it means in the world;
- a **test**: what a record of decisions can verify or refute about it;
- a **check** that the word means what it says, on cases chosen before anything is computed.

---

## How it is built

The method of reverse physics (Carcassi and Aidala): every starting point says what kind it is.

- **Imported mathematics**: probability, taken as it is.
- **Background conditions** assumed without loss of generality, each with what it would lose.
- **Premises**, few, each with its status.
- **Definitions**, each with how a record verifies it.
- **Conventions**, each forced by a requirement, chosen for convenience, or taken from the literature, and marked by
  whether it changes a verdict.

---

## Three layers

| Layer | Answers | Needs |
|---|---|---|
| **CORE** | What happened? | behaviour, the request, records |
| **INTERFACE** | Could the actor have done otherwise, or known? | what the actor sees and can do |
| **OPTIMIZERS** | Why did it happen? | the actor's objective |

A frozen model has a CORE and an INTERFACE, and optimizes nothing.

---

## CORE in one slide

1. **Behaviour**: how often each outcome happens, in each condition the actor faces.
2. **The request**: a list of **requirements**, each a set of acceptable behaviours, declared before the record is
   read.
3. **Misalignment**: the evidence, in nats per decision, that the actor's behaviour is not acceptable.
4. **Records**: decisions as they come, judged by bets.

No optimization, no reward and no training appear in CORE.

---

## Behaviour

A behaviour is the share of each outcome over many decisions, one share per condition.

- A support bot's answers to account questions: wrong 35%, escalated 65%.
- A behaviour is never seen exactly; a record of decisions estimates it.
- Two actors that behave alike in every condition are the same actor for the framework: it judges what is done, not
  how.

---

## Requirements

Three forms cover what principals say:

- a **forbidden** outcome: "never leak a customer's data";
- a **rate limit**: "at most 5% wrong answers";
- a **budget**: "on average at most 30 seconds per answer".

Every requirement for which a mix of acceptable behaviours is acceptable is a list of limits on averages, possibly
infinite (VK0). A budget is not one kind of constraint among others: it is the general form.

---

## Orders against a reference

A principal may rank outcomes (wrong < escalated < correct) and compare with a **reference**: the previous version, a
baseline, the status quo.

- **Better for every reading** of the ranking means reaching each standard ("at least escalated", "correct") at least as
  often as the reference (VO1).
- An actor can be better, worse, both, or **neither**: more correct answers and more wrong ones.
- Turning an order into a requirement is the principal's choice, such as "no shortfall beyond 2% at any standard".

---

## Misalignment is evidence

Bet against the request with tickets that no acceptable behaviour expects to win.

- If the actor is acceptable, no such bet grows.
- If it is not, the best bet grows at a rate: that rate is its **misalignment** (VE1).
- It equals the least divergence from the actor's behaviour to an acceptable one,
  `M = min over acceptable a of KL(actual‖a)`.

About `1/M` decisions give one nat of evidence: odds of `e` to 1.

---

## Why this number

| Step from "evidence" to the formula | Status |
|---|---|
| evidence of independent decisions adds: a logarithm | forced |
| a bet must be fair under acceptance | forced |
| wealth valued by its long-run growth (Kelly) | a choice |
| "how improbable acceptance makes the record" fixes KL's order | forced, given the question |
| the best bet, the benefit of the doubt | from the literature |

Total variation measures how far probability must move, not how fast a record convicts.

---

## Records and bets

- Bets multiply over decisions, and stay a fair game under acceptance **whatever the dependence** between decisions
  (VE3).
- So a test from bets keeps its error rate with no model of how the actor decides.
- A bet needs no bins: its average is an average, even on a continuum.

A record can **convict** an actor, never **certify** it: "misaligned" is verifiable, "aligned" only refutable (VF1).

---

## INTERFACE

What the actor **sees** (its views), what it **can do** (its actions), and how the world turns actions into outcomes.

- These fix the **feasible** behaviours, a hypothesis a record can refute.
- **Culpability**: the evidence that the actor is not doing the best it could.
- An excuse ("it could not do better") is tested only in conditions that try to make it do better: **elicitation**
  (VF3).

---

## Factoring misalignment

Remove the actor's capabilities one at a time, from the most capable declarable actor down to this one.

`misalignment = unavoidable + the cost of each limitation + the avoidable excess`

The sum is exact, and every term is non-negative (FA1). Each limitation, such as a coarse view, is a form of
misalignment with a number.

---

## OPTIMIZERS

Everything that needs the actor's objective:

- pursuit of an objective, and its price in KL;
- evaluators, Goodhart, overoptimization;
- outer and inner misalignment;
- strategic deception.

A constraint enters as a **shadow price**: an optimizer under a budget acts like one that subtracts the cost at a price
(VK5). Motives are hypotheses a record can refute, never verify.

---

## Every form, by layer

| Form of misalignment | Layer |
|---|---|
| breach, by condition, drift, evaluation gap, side effects | CORE |
| unavoidable, coarse perception, noise, tampering, collusion | INTERFACE |
| reward hacking as a motive, overoptimization, outer, inner | OPTIMIZERS |

Severity needs the principal's value scale; a wrong request needs a second standard.

---

## The example: a support bot

A company runs a frozen model as a support bot. A **new version** is ready. Should it replace the **previous** one?

- Questions are **open** (answerable from the documentation, 70%) or about an **account** (30%), which the bot cannot
  access.
- The previous version could tell the two apart. The new version was deployed without that signal.

Every number that follows is computed by `probes/slides/support_bot.py`.

---

## Step 1: outcomes and conditions

| Outcome | Meaning |
|---|---|
| **L** | leaks another customer's data |
| **W** | a wrong answer |
| **R** | escalates to a human |
| **A** | a correct answer |

Conditions: open questions (70%) and account questions (30%). The ranking: W < R < A; L is forbidden.

---

## Step 2: the request, declared before

- **R1**: never leak.
- **R2**: at most 5% wrong answers, over all questions.
- **R3**: no shortfall beyond 2 points against the previous version at the standards "escalated or correct" and
  "correct".

Written down and dated before any record of the new version is read.

---

## Step 3: what each version does

| | L | W | R | A |
|---|---|---|---|---|
| previous, open questions | 0 | 2.7% | 10% | 87.3% |
| previous, account questions | 0 | 0 | 100% | 0 |
| new, open questions | 0 | 2.9% | 3% | 94.1% |
| new, account questions | 0.06% | 35.3% | 64.6% | 0 |

The new version answers more open questions, and guesses on account questions it takes for open ones; on some it tries
an account look-up, which sometimes leaks.

---

## Step 4: a verdict per requirement

| Requirement | New version | Verdict |
|---|---|---|
| R1 never leak | 0.019% of decisions leak | breached |
| R2 wrong answers at most 5% | 12.6% | breached |
| R3 "escalated or correct" at least 96.1% | 87.3% | breached |
| R3 "correct" at least 59.1% | 65.9% | met |

The previous version meets all three.

---

## Step 5: how much evidence

| Against | Misalignment, nats per decision |
|---|---|
| R2 alone | 0.0496 |
| R3 alone | 0.0730 |
| R2 and R3 together | 0.0730 |
| with R1 too | infinite: a leak is impossible under R1 |

About 14 decisions give one nat of evidence against R2 and R3.

---

## Step 6: better or worse?

| Standard | New | Previous |
|---|---|---|
| anything but a leak | 99.98% | 100% |
| escalated or correct | 87.3% | 98.1% |
| correct | 65.9% | 61.1% |

**Neither**: more correct answers, and many more wrong ones. A ranking alone cannot say whether that trade is good; the
request (R3) can, and it says no.

---

## Step 7: what a record shows

A bet against R2, refitted before each decision, at a 5% level:

| Decisions in the record | New version accused | An actor exactly at the limit accused |
|---|---|---|
| 100 | 18.5% | 0% |
| 300 | 92% | 0.2% |
| 1000 | 100% | 0.4% |

The error rate holds whatever the dependence between decisions; nothing is assumed about how the bot decides.

---

## Step 8: the forbidden outcome

A single leak proves the breach of R1, with certainty (VK1). But leaks are rare: 0.019% of decisions.

| Decisions | Chance of seeing a leak |
|---|---|
| 1000 | 17.5% |
| 5000 | 61.7% |
| 20000 | 97.9% |

The evidence is decisive once a leak is seen; how bad the breach is lives in the rate, and in a value scale the company
declares.

---

## Step 9: the interface

- **Actions**: answer from the documentation, look up the account, escalate.
- **Environment**: open answers are right 97% of the time; account questions answered from the documentation are wrong;
  a look-up is wrong and leaks 0.4% of the time.
- **Views**: the previous version saw every account question as one. The new one sees 80% of them; **20% look open**.

---

## Step 10: factoring the misalignment

Against R2 and R3, leaks set aside:

| Part | Nats per decision |
|---|---|
| unavoidable even with a full view | 0 |
| the cost of the coarse view | 0.0106 |
| avoidable with the new version's view | 0.0624 |
| total | 0.0730 |

The lost signal explains about a seventh; the rest the new version could have avoided.

---

## Step 11: culpability

- Every leak was avoidable: escalating instead of looking up never leaks. So the culpability of the new version is
  **infinite**: one leak is decisive evidence that it did not do its best.
- Without its look-ups it would never leak: its misalignment would fall to 0.0173, of which 0.0067 avoidable, and its
  culpability to 0.0559.
- What remains is the coarse view's cost, which only restoring the account signal removes.

---

## Step 12: the report

- **Breaches**: R1, R2, R3 at "escalated or correct".
- **Evidence**: 0.0730 nats per decision against R2 and R3; infinite with R1.
- **Comparison**: neither better nor worse than the previous version.
- **Interface**: the coarse view costs 0.0106; most misalignment is avoidable; leaks are culpable.
- **What the company reads**: the new version should not replace the previous one as it is. Stopping account look-ups
  removes the leaks and most of the avoidable part; restoring the account signal removes the rest. Then measure again,
  under the same request.

---

## What the framework cannot tell you

- Whether the request is the right one: it judges against what was declared.
- How serious a breach is, without a declared value scale: evidence is not harm.
- Why the bot behaves so: motives are hypotheses, refutable, never verified.
- That an actor could not do better, without elicitation.
- Small shifts of about `1/√n` per decision escape every test over `n` decisions (a hunch, H43).

All of them are listed in `v14/LIMITS.md`.

---

## Using it on your own case

1. Name the outcomes a record can tell apart, and the conditions.
2. Declare the request before reading any record: forbidden outcomes, limits, an order against a reference.
3. Record decisions; bet against each requirement; report a verdict per requirement and the evidence.
4. Declare the interface, from capabilities shown in elicitation; factor the misalignment; report culpability.
5. Only then, if needed, test hypotheses about motives (OPTIMIZERS).

---

## Where things are

| File | Holds |
|---|---|
| `v14/README.md` | the design, its generality, its conventions |
| `v14/*.md` | the results, the limits, what of v13 survives |
| `probes/slides/support_bot.py` | every number of this example |
| `ROADMAP.md` | what comes next |

Next: test the new words on chosen cases (L2), write the three layers as items, then a real case.
