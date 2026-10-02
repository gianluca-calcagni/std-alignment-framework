# RECORD — what the framework claims about the world, and what it has taken back

Lint rule R13 checks this file. It names only existing items. Its ledger has exactly one row for every prediction of
the ontologies, with the prediction's label and a state that starts with one of: untested, held, refuted, untestable.
Nothing here is deleted. A refuted prediction keeps its row and its result, and a retraction keeps its line
(README, working agreements).

## 1. The honest position

**Nothing in the core is new mathematics.** Its proofs use the Gibbs variational principle, convex duality
(Donsker–Varadhan), the Pythagorean identities of KL projections, data processing, Taylor expansion, Chernoff's and
Wilks's theorems, isotonic regression and total positivity. What it adds is one vocabulary, five premises and eleven
definitions, in which results from several fields are derived, checked, and reported through one standard.

**Where to look for prior art first.** v7.10 searched for these and did not find them stated elsewhere:
- the width as the exact worst case, with no separable bound ([P29], [P30]);
- the split of the departure behind [P6] and [P9];
- the pairing of budgets with statistics of the error ([P31]);
- the floor of [P32];
- detection bounded by misalignment ([P22](iii)).

The core's own results have not been searched for: [P15], [P16], [P17], [P25], [P26], [P36], and the leading form of
[P37](i). Novelty is not a goal; this list says where a reader should look first.

**What it is not yet.** The core is a checked calculus. It has made six predictions about the world and tested none of
them on data not seen before (section 2). The finish line is in the README.

## 2. Predictions

### 2.1 The ontologies' predictions

Every prediction is empirical: it can be wrong about the world, not only through a bug. A verification prediction,
which can fail only through a bug or a badly scaled threshold, does not count toward the base rate (section 2.2).

| Ontology | From | Label | State | Where |
|---|---|---|---|---|
| machine-learning | [P13] | empirical | untested. The published paper does not report what it needs (v7.10, T3); it needs samples of the initial policy (`NOTES.md` §3.2, D3) | `ontologies/machine-learning/`, sections 3 and 4 |
| machine-learning | [P20] | empirical | untested | `ontologies/machine-learning/`, section 3 |
| humans | [P12], [D6] | empirical | refuted in its two-default form (v7.10, T7-2d); against enrolment on request it held loosely, in three of four companies (T7-2, T7-2b). Those data are seen | `ontologies/humans/`, section 3 |
| institutions | [P12], [D6] | empirical | untested: the data are not public (`NOTES.md` §3.2, D5) | `ontologies/institutions/`, section 3 |
| job-delegation | [P12], [D6] | empirical | untested | `ontologies/job-delegation/`, section 3 |
| biology | [P13], [D1] | empirical | untested: neither paper reports the genome-level data | `ontologies/biology/`, section 3 |

The humans prediction was tested before its ontology was written, and the ontology first presented it as untested
(section 3, row 4). Three of the six predictions share its form: an actor that only adds a known nudge keeps the
ratios among the other options. The refutation concerns a new default option, which [D6] models as a bonus only
approximately; the institutions and job-delegation predictions concern explicit incentives.

### 2.2 The base rate

**The archive.** v7.10 registered every empirical test before reading the data:
- T7, case 1 (evaluator length bias): 1 of 7 predictions held, plus 1 that could not fail. The one that held came after
  two failed designs.
- T7, case 2 (retirement defaults): 4 of 8 held, and 1 could not be evaluated.
- T3: not testable from published data.
- I1-dyn: could not fail, since its reference was fitted from the counts it judged.
- I1-dyn2: not rejected, at power 0.51.

Every verification prediction held. So the archive's empirical base rate is 5 of 15 in T7, the only study with several
predictions.

**This core.** None of its six empirical predictions has been tested on data not seen before.

## 3. Retractions

The core's own log, from the restart on. v7.10's 78 rows stay in the archive, tagged `v7.10`, and are cited as
`v7.10: row N`. "Found by" says who: per the working agreements, a person, or a model family.

| # | Retracted | Replaced by | Found by |
|---|---|---|---|
| 1 | v7.10's Prop 3, "only the error's upper tail matters", imported as [P33](iii) | for misalignment an underrating also costs nats, a bounded number of them ([C3]); (iii) now says only that the bound needs no range | the compatibility review of the import (`IMPORT.md` §7), by the executor, a Claude session |
| 2 | [P29](ii) and [P34](ii): "the largest loss" | the supremum: the worst case is approached as `c → 1`, never reached | the same review |
| 3 | [P37](i): the Chernoff information vanishes "like" the divergence; its Notes: strong incentives make evaluations weak evidence "exactly to the extent" they point at the objective | at least as fast ([P22](ii)); the Notes now say what (ii) and (iii) give | the same review |
| 4 | `ontologies/humans/`: the pass-through prediction for a new default, presented as untested, with a request for data | tested in v7.10 before the ontology was written, and refuted in its two-default form; section 2.1 | the analysis of the archive before the merge, by the executor, a Claude session |
| 5 | `IMPORT.md` §5: T3 "in core" in the machine-learning ontology's Limits; the census "could" be re-routed against the core | the Limits did not mention T3, and now do; the PI froze the census in v6.4 | the same analysis |
| 6 | `ontologies/biology/`: v7.10's I1-dyn "found no power" | I1-dyn could not fail; I1-dyn2 did not reject one objective, at power 0.51 | the same analysis |
