# Ontologies — the core, read in six disciplines

An ontology says what each object of the core is in one discipline: what an outcome is, who the principal is, what the
default is, and so on. It is a dictionary, not a theorem. It proves nothing, and the core's results reach a discipline
only through it. A wrong ontology gives correct mathematics about the wrong things, so every entry says how well it
fits.

Each ontology then reframes one known result of its discipline in the core's terms. It says what the core adds to that
result, separating three kinds of claims: consequences, predictions that data could refute, and readings that only
redescribe. It ends with the limits of the mapping and the open questions.

An ontology is not evidence for the core. Evidence comes from worked cases: a prediction, pre-registered, tested on
data that did not suggest it.

## Which disciplines

A discipline gets an ontology only if it meets all four conditions. The second is the point: without numbers, nothing
in the discipline can be diagnosed or interpreted in the core's terms.
1. **A principal and an actor.** One party's purpose, or a question declared in advance, and another party's behaviour
   judged against it: the core's scope (`CORE.md` §0). The other party may be a group, taken as one actor on joint
   outcomes ([P39]).
2. **Behaviour reported in numbers.** Its papers report counts or shares over finitely many outcomes, ideally before
   and after a change, so that a default and a behaviour can be read off.
3. **Data that can be read.** Such data are public, or can be supplied, and the ontology records which have already
   been seen (README, rule (e)). Each ontology says so in its **Data** paragraph.
4. **Inside the scope.** Not a choice of which objective is right. Several actors only as one actor on joint outcomes,
   with a declared specification of their joint behaviour ([P39]); several principals only with declared weights
   ([P42]).

| File | Discipline | Principal → actor | Known result | Numbers |
|---|---|---|---|---|
| `machine-learning/` | machine learning: fine-tuning against a learned reward | a developer → a fine-tuned policy | reward-model overoptimization [@gao2023] | scores and log-probabilities per response; public benchmarks |
| `evolutionary-biology/` | evolutionary biology: selection between the sexes | an analyst's question → a population under selection | sexually antagonistic fitness [@chippindale2001], [@prasad2007] | genotype counts and fitness assays |
| `behavioural-economics/` | behavioural economics: choices under defaults and incentives | an employer or an institution → people choosing | default effects [@madrian2001]; a fine that raised lateness [@gneezy2000] | distributions of choices before and after a change |
| `medical-sciences/` | medical sciences: performance measures in health care | a ministry or a regulator → hospitals and clinicians | the four-hour target [@mason2012]; cardiac surgery report cards [@dranove2003] | attendances by time in the department; patients by treatment and severity |
| `industrial-organization/` | industrial organization: pricing algorithms and competition | a competition authority → the firms of a local market, as one actor | algorithmic pricing in German petrol duopolies [@assad2024]; algorithms that learn to sustain high prices [@calvano2020] | every price change of every station; public, for non-commercial use |
| `experimental-economics/` | experimental economics: learning in games | an experimenter → a group of subjects, as one actor | cycles in Rock–Paper–Scissors played in continuous time [@cason2014]; log-linear learning [@blume1993] | each subject's strategy, moment by moment |

No discipline is added while the framework is frozen, until a prediction has been tested on data not seen before
(`NOTES.md` §3.1, Q26).

**Considered and not adopted** (`NOTES.md` §3.1, Q22, Q24).

| Discipline | Numbers | Why not |
|---|---|---|
| job delegation (dropped) | none in its known result, an essay and a model; its running example was invented | fails condition 2. Its consequences hold wherever a bonus is paid on an indicator, and behavioural economics carries incentives with data |
| ethics and philosophy | few; surveys of moral choices are numerical, but record what people say should be pursued | fails condition 4: which objective is right is outside the core. Such surveys could inform a declared specification; they do not judge an actor |
| normative sciences | norms are not data; compliance with them is, and is behavioural economics | fails condition 4 for the norms; compliance belongs to behavioural economics |
| game theory (became experimental economics) | its models report no behaviour; its experiments do | its models fail condition 2. Its experiments failed condition 4 until a group could be read as one actor on joint outcomes ([P39]); they are now `experimental-economics/` |
| network science | large datasets | fails condition 1: structure among many agents, with no principal whose purpose judges it. Many agents are now one actor on joint outcomes ([P39]), so condition 4 no longer excludes it |
| complexity theory | mostly models and simulations | fails conditions 1 and 2 |

The institutions ontology became the medical-sciences one: its known result was already health care, and the four-hour
target added a measure whose data are partly public. When [P39]–[P42] brought groups, and several principals with
declared weights, into the scope, condition 4 was revised (Q24). Game theory's experiments then met all four
conditions, and industrial organization joined for its public record of prices, where competition law's requirement
of independent conduct gives a specification, in the stricter form that can be tested (Q25).

## The slots

Every ontology fills every slot, once, in a table with the columns Slot, Core, In this discipline, Observed as, and Fit.
The Core column names the item below.

| Slot | Core | Type | What the entry must say |
|---|---|---|---|
| **outcomes** | [D1] | a finite set | what one outcome is, and how a continuum is cut into finitely many |
| **contexts** | [D8] | conditions whose frequencies the actor does not choose | the part of an outcome that is fixed before the actor acts, or "none" |
| **behaviour** | [D1] | a distribution on the outcomes | whose behaviour, counted over what (people, occasions, generations), and how it is measured |
| **sample** | [D11] | independent draws from a behaviour | what one draw is, how many there are in each condition, and why independence is a fair model |
| **default** | [D2] | a full-support distribution on the outcomes | what happens with no pursuit, and how it is measured apart from the behaviour it will judge |
| **objective** | [D2] | a function on the outcomes, up to a constant | what the principal wants pursued, in whose units |
| **evaluator** | [D10] | a function on the outcomes, known or revealed | what the actor is rewarded or selected on, if that is known, and its level sets: which outcomes it scores alike |
| **intensity** | [D2] | a number, at least 0 | what makes pursuit stronger or weaker; only the product of intensity and objective is identified ([P1]) |
| **specification** | [D3] | a default and a closed set of intended behaviours | who declares it, when, and where it is written down |
| **principal's resolution** | [D4] | a partition, the finest unless declared | the distinctions the principal declares it does not care about |
| **actor's resolution** | [D4] | a partition | the distinctions the actor cannot make |
| **change** | [P2] | a differentiable path of behaviours | what moves behaviour over time, and what its revealed objective is |
| **intervention** | [D6] | a known non-constant function on the outcomes | what a principal or an experimenter adds to what the actor faces |
| **stakes** | [D5] | the units of the objective | what a shortfall is counted in |

**Contexts.** Often part of an outcome is fixed before the actor acts: the prompt a model answers, the patient who
arrives, a person's circumstances. These are conditions ([D8]) whose frequencies the actor does not choose. On
condition–outcome pairs, the behaviours with those frequencies form a linear feasible set ([D7]). Within one context
every item applies as stated. Across contexts, [P15] splits misalignment under the standard specification exactly: the
best feasible behaviour pursues the objective within each context at one shared intensity, and the unavoidable part is
how much the unconstrained pursuit would have reweighted the contexts. [P13](i) holds for any path, and the first limit
of [P13](ii) for any path as in [P11], so both apply across contexts as stated.

**Evaluator.** The regression of the objective on the evaluator ([D10]) says more than the objective itself only when
the evaluator scores several outcomes alike: a test passed or failed, a grade, an indicator, a fine. A real-valued
evaluator, such as a reward model's score or a genome's fitness, gives distinct outcomes distinct values, so each level
set is one outcome, the regression is the objective, and the residual is zero. Then the regression on bins of its
values governs the pursuit, up to a margin that grows with the intensity and the width of the bins ([P26]). Every
entry says which case holds.

**Sample.** Every behaviour in an ontology is known through samples ([D11]). [P23] needs each outcome counted many
times, and independent draws. With very many outcomes, counts are grouped into the cells of a resolution, and grouping
only hides misalignment ([P4](iv)), so what is estimated is a lower bound on misalignment. Draws that depend on each
other, such as one person's successive decisions, make the error bars of [P23] too narrow.

**Fit.** The last column says how well the discipline's object has the slot's type. It starts with one of four words.
- **exact**: the object has the type, by definition or by a cited result.
- **approximate**: it has the type under an approximation the entry names.
- **assumed**: the entry is a modelling choice, and says who makes it. A verdict of the core is only as good as these
  choices.
- **absent**: the discipline has nothing in this slot. The entry says why, and the core's fallback applies: the finest
  resolution, no contexts, or no intervention observed.

## Claims

The section "What the core says" holds the claims, one per bullet. Each starts with its kind and the items it uses.
- **Consequence** of [items]: follows from the items and the slot entries, with no data. It fails only if a slot entry
  is wrong.
- **Prediction** from [items]: says what data would show, and when it is *Refuted if*. Testing it on the data that
  suggested it is not a test; tests are pre-registered and run as cases (`cases/`, and the rules in the top-level
  `README.md`).
- **Reading** with [items]: redescribes a known result in the core's terms. It explains nothing by itself and is no
  evidence for the core. It earns its place by making a consequence or a prediction possible.

## The format of an ontology

Each ontology lives in its own folder, `ontologies/<name>/README.md`, so that its worked cases and data can join it
later. It has a title `# Ontology — <discipline>`, a short introduction, then these sections, in this order:
`## 1. Slots`, `## 2. Known result`, `## 3. What the core says`, `## 4. Limits`, `## 5. Open questions`. The known
result cites its source, listed in `REFERENCES.md`, and a paragraph that starts `**Data.**` says what numbers the
discipline offers for the slots, where they are, whether they are public, and which have already been seen. Lint rule
R10 checks the sections, the Data paragraph, that every slot appears once and names its item, the fit words, the claim
kinds and their items, the label and the *Refuted if* of every prediction, that every item named exists, and that every
source cited is listed.
