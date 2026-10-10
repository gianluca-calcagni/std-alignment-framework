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

The framework does not assume KL, reweighting or the order of KL's arguments. It derives them from five premises
(section 2) through the results of section 4, so a reader who rejects a premise can see which results fall with it.

It serves two purposes. The first is a common unit for reports of misalignment, so that two reports on the same actor
can be compared (`STANDARD.md`). The second is a set of diagnostics that split a measured misalignment into named parts:
what a named objective explains, the drift between training runs, and the tampering with a measurement. It is not a
theory of how an actor comes to behave as it does, nor of which objective is right.

{{counts}}

Each result has a proof and checks that run in CI. The checks are numerical, so they catch slips in a statement or in
code; they do not replace the proofs. No reader independent of the project has checked the proofs yet. That check is
what this overview asks for (`REQUESTS.md`, R1).

## 2. Setting and premises

Notation first. The premises then say what alignment is judged on (A1), what pursuing an objective means, geometrically
(A2) and economically (A3), what misalignment measures (A4), and when the standard of judgement is fixed (A5).

{{item D1}}

{{item A1}}

{{item A2 why}}

{{item A3 why}}

{{item A4 why}}

{{item A5}}

## 3. Pursuit and misalignment

Pursuit is defined as a reweighting of the default. Section 4 shows that A2 leads to it. Misalignment is defined for any
declared set of acceptable behaviours. The standard specification, "pursue `F`", is the case with closed forms.

{{item D2 why}}

{{item D3}}

## 4. The results the rest stands on

Six results, in their reading order.
- [P1]: nothing is lost by writing behaviour as a reweighted default.
- [P2]: reweighting toward a fixed objective is the steepest climb of A2.
- [P4]: KL is exactly the value lost against a pursuit, which is A4's reading of misalignment.
- [P14]: A2 and A3 together leave one cost of departing from the default, KL.
- [P5]: misalignment is attained, is zero exactly where it should be, and has closed forms for "pursue `F`".
- [P6]: the departure from the default splits into pursuit and misalignment, a split the standard asks every report for.

Each proof is complete given the items it cites and the facts it names as standard. Five of those facts are imported.
- Čencov's theorem enters through the reasons for A2 and D2, above. Its statement is read in the open text they cite,
  and its proof is Čencov's.
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
1. **From A2 to the Fisher metric.** Čencov's theorem needs a Riemannian geometry, and invariance under splitting
   outcomes for outcome sets of every size at once. A2 asks for both, the first since v12. A geometry that measures
   steepness by a norm that is not an inner product is not covered. A reader may reject either requirement, and [P2]
   then loses its reading as the steepest climb, though not its algebra.
2. **The price in A3.** [P14] forces KL because A3 prices departure at exactly `1/t`. If the best trade-offs are only
   asked to lie somewhere on the pursuit ray, any increasing function of KL passes ([P14], Notes).
3. **The benefit of the doubt in A4.** Misalignment takes the least loss over the acceptable behaviours, each judged by
   its own objective. That choice fixes the order of KL's arguments ([P4](ii)). The loss in the principal's own units is
   a different quantity, the stakes ([D5]).
4. **The edge cases of [P5](iv).** An actor that only ever picks the best outcomes is charged unless it splits its
   choices among tied outcomes as the default does.

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
- **Premises are choices.** Each premise is argued for in its "Why this choice" in `CORE.md`, not proved.
- **Imported theorems.** Every theorem a result imports is read in an open text or derived where it is used, and
  `REFERENCES.md` says which. Čencov's own proof is not in the open texts read here; an extension of it is.
- **Prediction.** On real data, as of 2026-10-09, three registered predictions failed and two held (section 6). The
  framework's worth as a predictive theory is not established. Its worth as a common unit and a set of diagnostics is
  what the next cases test.
- **Review.** No independent reader has checked the proofs.
