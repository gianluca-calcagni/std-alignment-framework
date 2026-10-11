# Overview: the framework for a mathematical reader

For a reader who knows probability and wants to judge the mathematics. It covers what the framework claims, the
premises, the results it rests on with their proofs, one case, what to check, and where the framework stops. The items
below are copied from `CORE.md` and `derived/`, which are the sources. `tools/overview.py` builds this file from them
and from `tools/overview_template.md`, and a test fails when the copy is stale.

## 1. The question

Alignment compares what an actor does with what a principal intended. The framework turns that comparison into a
number. A behaviour is a distribution over finitely many outcomes. Before looking, the principal declares a default
behaviour and a set of acceptable behaviours. Misalignment is the KL divergence from the actual behaviour to the nearest
acceptable one, in nats. The usual acceptable set is "pursue `F`": the default reweighted by `e^{t·F}`, at every
intensity `t ≥ 0`.

The framework does not assume KL or the order of its arguments: they follow from the premise that misalignment is a
rate of evidence (A4, section 2). Reweighting is the definition of pursuit, and its two reasons, the steepest climb and
the best trade-off, agree on it and on KL (section 3, and [P2] and [P14] in section 4). No result cites a premise in its
proof: a reader who rejects a premise keeps every result, and loses the meaning the premise gives it.

In familiar terms: the pursuits of `F` form the one-parameter exponential family with base `q`, statistic `F` and
natural parameter `t ≥ 0`. Misalignment is the KL divergence from the actual behaviour to that family, which maximum
likelihood minimizes; `2n` times it is the family's deviance on `n` counted draws. [P5] and [P6] are then the moment
equation and the Pythagorean identity of the family, and [P23] is Wilks's theorem for it. Nothing here is new
mathematics (`RECORD.md` §1); what the framework adds is the premises that single out this family, and what is built on
it.

It serves two purposes. The first is a common unit for reports of misalignment, so that two reports on the same actor
can be compared (`STANDARD.md`). The second is a set of diagnostics that split a measured misalignment into named parts:
what a named objective explains, the drift between training runs, and the tampering with a measurement. It is not a
theory of how an actor comes to behave as it does, nor of which objective is right.

{{counts}}

Each result has a proof and checks that run in CI. The checks are numerical, so they catch slips in a statement or in
code; they do not replace the proofs. No reader independent of the project has checked the proofs yet. That check is
what this overview asks for (`REQUESTS.md`, R1).

## 2. Foundations

The core is built by the method of reverse physics (`CORE.md` §0): it separates what it imports from probability theory
(M), the representation it assumes without loss of generality (B), and what it assumes about judging alignment (A), and
each of these says, in its Status, what kind of starting point it is. Every definition declares its interpretation: what
its object is in the world, how a record verifies it, and why that map is right. The premises say what alignment is
judged on (A1), what misalignment measures (A4), and when the standard of judgement is fixed (A5). This is v13
(`NOTES.md` §16, §17): in v12, A4 said that misalignment is value lost, and two more premises, A2 and A3, said what
pursuing is; they are now the reasons of D2, as no result used them.

{{item M1}}

{{item M2}}

{{item M3}}

{{item B1}}

{{item B2}}

{{item B3}}

{{item B4}}

{{item A1}}

{{item A4 why}}

{{item A5}}

## 3. Behaviour, pursuit and misalignment

Notation first. Pursuit is then defined as a reweighting of the default, and its reasons say why; section 4 proves
them. Misalignment is defined for any declared set of acceptable behaviours. The standard specification, "pursue `F`",
is the case with closed forms; the ordinal one, which accepts every behaviour that respects the order of `F`, is
reported beside it.

{{item D1}}

{{item D2 why}}

{{item D3}}

## 4. The results the rest stands on

Six results, in their reading order.
- [P1]: nothing is lost by writing behaviour as a reweighted default.
- [P2]: reweighting toward a fixed objective is the steepest climb in the Fisher metric, D2's first reason.
- [P4]: KL is exactly the value lost against a pursuit, a second reading of A4's evidence.
- [P14]: the steepest climb is the best trade-off, D2's second reason, for one cost of departing from the default, KL.
- [P5]: misalignment is attained, is zero exactly where it should be, and has closed forms for "pursue `F`".
- [P6]: the departure from the default splits into pursuit and misalignment, a split the standard asks every report for.
  [P53], in `derived/`, reads the split for every specification the core defines: misalignment is the departure beyond
  what the specification credits.

Each proof is complete given the items it cites and the facts it names as standard. Five of those facts are imported
(M3 lists every theorem the results import).
- Čencov's theorem enters through the first reason of D2, above. Its statement is read in the open text they cite, and
  its proof is Čencov's.
- Gibbs' and Pinsker's inequalities are read in an open text, which the Notes of [P4] and [P5] in `derived/` cite.
- Cauchy–Schwarz, and the uniqueness of solutions of an ODE with a locally Lipschitz field, are textbook facts.

{{item P1}}

{{item P2}}

{{item P4}}

{{item P14}}

{{item P5}}

{{item P6}}

## 5. What else is derived

Everything else follows from the core in this reading order (`derived/README.md`). A result may use only the core and
the results before it, which lint rule R5 enforces.

{{reading-order}}

## 6. One case, and the record

A case is a test registered before it is computed (`cases/README.md`). W1 is the one reported field by field to the
standard. It asked whether the coefficient that the literature fits to best-of-`n` curves is the initial slope that
[P13] computes from the initial policy. It is not. The registered prediction was refuted, and the analysis after the
verdict found where: the curve keeps the predicted slope at first, then bends, and the literature's form cannot bend.
Its registration, results and report are in `cases/w1-best-of-n-slope/`. Its report as data, `standard-report.json`, is
held to the standard by lint R16.

Every case so far, failures included:

{{cases}}

A case on simulated data runs in under a minute and shows the steps: `python3 examples/quickstart.py`. It fixes a
declaration, draws from a simulated assistant, estimates with the library `stdalign`, and writes a report that the
standard's validator accepts.

## 7. What to check

The proofs above, line by line. These are the places where a careful reader should push.
1. **From the steepest climb to the Fisher metric.** Čencov's theorem needs a Riemannian geometry, and invariance under
   splitting outcomes for outcome sets of every size at once. D2's first reason asks for both. A geometry that measures
   steepness by a norm that is not an inner product is not covered. A reader may reject either requirement, and [P2]
   then loses its reading as the steepest climb, though not its algebra.
2. **The price in the best trade-off.** [P14] forces KL because D2's second reason prices departure at exactly `1/t`.
   If the best trade-offs are only asked to lie somewhere on the pursuit ray, any increasing function of KL passes
   ([P14], Notes). Since v13 the measure does not rest on this: A4 fixes it.
3. **Evidence in A4.** Misalignment is the rate at which a record's counts become improbable under the accepted
   behaviour most favourable to them; that fixes the order of KL's arguments ([P55](i)). It assumes nothing of how the
   actor decides: independence is a convention of what is accepted, and what an actor's dependence and drift add is
   measured beside it ([P54]). Value lost is the same number ([P4](ii)), and the loss in the principal's own units is a
   different quantity, the stakes ([D5]). The conventions behind it are in the table of `CORE.md` §1: a reader may
   reject one, and each says whether a verdict would change.
4. **The edge cases of [P5](iv).** An actor that only ever picks the best outcomes is charged unless it splits its
   choices among tied outcomes as the default does.
5. **Which specification.** No premise says which specification a principal declares. The standard one charges
   best-of-`n` on `F` for its method as well as its goal ([P36], [P53]); the standard asks for the ordinal misalignment
   beside it, so that the charge is visible. A5 fixes the choice before the data; nothing fixes it across principals.
6. **The interpretations.** Each definition declares what its object is in the world and how a record verifies it. They
   carry the bridge from the results to judging an actor, and no check tests them: a reader may reject one, and the
   results stand while their reading falls.

The checks of these six results run in a few seconds, from the repository's root, after
`pip install -r requirements.txt`:

{{checks P1 P2 P4 P14 P5 P6}}

`python3 -m pytest` runs every check, the tests of the tools and of the library, and the quickstart.

Feedback is most useful in three forms:
- a step of a proof that fails;
- a premise that does not hold where the framework is meant to apply;
- a result that is already known under another name (`RELATED.md` lists what is known so far).

Open an issue, or a pull request under the terms of `CONTRIBUTING.md`.

## 8. Where it stops

- **Finite outcomes.** Outcomes that are not finite are drafted in `CORE-GENERAL.md`, and nothing there is claimed.
- **Behaviour only.** Two actors that behave alike in every condition are the same actor for the framework ([A1]).
- **Premises are choices.** Each premise is argued for in its "Why this choice" in `CORE.md`, not proved, and its
  Status says whether it is a principle or an assumption that may fail.
- **Imported theorems.** Every theorem a result imports is read in an open text or derived where it is used, and
  `REFERENCES.md` says which. Čencov's own proof is not in the open texts read here; an extension of it is.
- **Prediction.** On data not seen before, three predictions of the framework were tested and one held (W1 and W3,
  `RECORD.md` §2); W4's two diagnostic hypotheses, which are not the framework's predictions, were one refuted and one
  held (section 6). Those predictions test the optimum of KL-regularized training and a fitted curve, more than any
  premise of the framework's own (`NOTES.md` §15). The framework's worth as a predictive theory is not established. Its
  worth as a common unit and a set of diagnostics is what the next cases test.
- **Review.** No independent reader has checked the proofs.
