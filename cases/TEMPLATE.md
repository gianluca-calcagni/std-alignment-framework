# Template for a registration

Copy this file to `cases/<case>/REGISTRATION.md` and fill every section; delete this paragraph and the guidance in
italics. Lint rule R15 checks that every section below is present, that the declaration has a row for every field of
`STANDARD.md`, section 1, that every prediction says where its threshold comes from, and that the rehearsal's record,
`rehearsal.json`, is in the case folder. Lint cannot check that the entries are right: that is what a reader is for.

# <Id> — <the question> — Registration

**Kind:** world or simulation (`cases/README.md`). **Who:** who registered it, under whose instruction, and who read it
before it was pushed. Nothing below has been computed on the test's data before this file was pushed.

## Why

*Which row of the finish line and which step of `ROADMAP.md` this serves; which result of the core is tested, and what
earlier cases left open.*

## The system

*Models, data, rewards and their versions, with where each comes from, and the checks made on loading, on no test item.*

## Declaration

*Every field of `STANDARD.md`, section 1, one row each. Fix here the specification across conditions (each at its own
intensity, or one shared: [P43]), which outcomes the evaluator scores alike, ties included ([D10]), the named
objectives in their order ([P44]) and the runs ([P45]).*

| Field | Core | Entry |
|---|---|---|
| Outcomes | [D1] | |

## The procedure

*What the script computes, step by step, with every seed. A statistic on a sample that mixes sources is computed within
each source (design rule 5). Quantities are estimated in nats where the departure is not small ([P44], Notes), and the
cost of every reweighting is stated ([P47]).*

## Auxiliary assumptions

*What each prediction needs beyond the framework, such as that a run converged or that a curve has a given form, and
how the design tests it or keeps the verdict independent of it (design rule 2).*

| # | Assumption | Tested how, or why the verdict does not depend on it |
|---|---|---|
| A1 | | |

## Predictions

*A threshold comes from a result or from a stated scale, such as the noise level measured in the rehearsal (design rule
3); otherwise the prediction is a direction, with its estimate and interval.*

| Id | From | Label | Prediction | Held if | Threshold from |
|---|---|---|---|---|---|
| S1 | | | | | |

## Readings, fixed now

*For each prediction, what each outcome would mean, and which auxiliary assumption a verdict bears on.*

## Rehearsal

*What the script did, end to end, on synthetic data shaped like the real data, with the degenerate cases built in (a
regressor that does not vary, ties, intensities at their boundaries, values that underflow), and its run time measured
on this machine; and what the rehearsal changed in the design. Its record is `rehearsal.json` (design rule 4).*

## Licences

*Under which licences the inputs are released; the repository keeps code and aggregates only (README, working
agreements).*
