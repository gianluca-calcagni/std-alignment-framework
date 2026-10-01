# Ontologies — the core, read in five disciplines

An ontology says what each object of the core is in one discipline: what an outcome is, who the principal is, what the
default is, and so on. It is a dictionary, not a theorem. It proves nothing, and the core's results reach a discipline
only through it. A wrong ontology gives correct mathematics about the wrong things, so every entry says how well it fits.

Each ontology then reframes one known result of its discipline in the core's terms. It says what the core adds to that
result, separating three kinds of claims: consequences, predictions that data could refute, and readings that only
redescribe. It ends with the limits of the mapping and the open questions.

An ontology is not evidence for the core. Evidence comes from worked cases: a prediction, pre-registered, tested on
data that did not suggest it.

## The five ontologies

| File | Discipline | Principal → actor | Known result |
|---|---|---|---|
| `machine-learning.md` | machine learning: fine-tuning against a learned reward | a developer → a fine-tuned policy | reward-model overoptimization [@gao2023] |
| `biology.md` | evolutionary biology: selection between the sexes | an analyst's question → a population under selection | sexually antagonistic fitness [@chippindale2001], [@prasad2007] |
| `humans.md` | behavioural economics: choices under defaults and incentives | an employer or an institution → people choosing | default effects [@madrian2001]; a fine that raised lateness [@gneezy2000] |
| `institutions.md` | health policy: public reports on performance | a regulator → hospitals and surgeons | cardiac surgery report cards [@dranove2003] |
| `job-delegation.md` | organizations: delegating work | a manager → an employee | rewarding A while hoping for B [@kerr1975]; multitask incentives [@holmstrom1991] |

## The slots

Every ontology fills every slot, once, in a table with the columns Slot, Core, In this discipline, Observed as, and Fit.
The Core column names the item below.

| Slot | Core | Type | What the entry must say |
|---|---|---|---|
| **outcomes** | [D1] | a finite set | what one outcome is, and how a continuum is cut into finitely many |
| **contexts** | [D4] | a resolution whose cell masses the actor does not choose | the part of an outcome that is fixed before the actor acts, or "none" |
| **behaviour** | [D1] | a distribution on the outcomes | whose behaviour, counted over what (people, occasions, generations), and how it is measured |
| **default** | [D2] | a full-support distribution on the outcomes | what happens with no pursuit, and how it is measured apart from the behaviour it will judge |
| **objective** | [D2] | a function on the outcomes, up to a constant | what the principal wants pursued, in whose units |
| **intensity** | [D2] | a number, at least 0 | what makes pursuit stronger or weaker; only the product of intensity and objective is identified ([P1]) |
| **specification** | [D3] | a default and a closed set of intended behaviours | who declares it, when, and where it is written down |
| **principal's resolution** | [D4] | a partition, the finest unless declared | the distinctions the principal declares it does not care about |
| **actor's resolution** | [D4] | a partition | the distinctions the actor cannot make |
| **change** | [P2] | a differentiable path of behaviours | what moves behaviour over time, and what its revealed objective is |
| **intervention** | [D6] | a known non-constant function on the outcomes | what a principal or an experimenter adds to what the actor faces |
| **stakes** | [D5] | the units of the objective | what a shortfall is counted in |

**Contexts.** Often part of an outcome is fixed before the actor acts: the prompt a model answers, the patient who
arrives, the request a manager sends. The actor chooses only what happens within each context. Contexts are then a
third position for a resolution, beside the two of [D4], and the core has no item for this position yet. Until it has
one, the ontologies apply every item context by context: within one context the actor chooses everything, and every item
applies as stated. Across contexts, the intended set "pursue `F` in every context, at any intensity in each" is a
specification by [D3]. When the actual behaviour has the default's context masses, its misalignment is the average of
the misalignments within the contexts, weighted by the context masses, by the chain rule [P4](iii). Whether "pursue `F`"
should instead require one intensity in every context is a design question for the core, recorded in `NOTES.md`.
[P13](i) holds for any path, and the first limit of [P13](ii) for any path as in [P11], so both apply across contexts as
stated; the second limit compares with a pursuit that moves the context masses, which the actor cannot do.

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
  suggested it is not a test; tests are pre-registered (see the rules in the top-level `README.md`).
- **Reading** with [items]: redescribes a known result in the core's terms. It explains nothing by itself and is no
  evidence for the core. It earns its place by making a consequence or a prediction possible.

## The format of an ontology

A title `# Ontology — <discipline>`, a short introduction, then these sections, in this order: `## 1. Slots`,
`## 2. Known result`, `## 3. What the core says`, `## 4. Limits`, `## 5. Open questions`. The known result cites its
source, listed in `REFERENCES.md`. Lint rule R10 checks the sections, that every slot appears once and names
its item, the fit words, the claim kinds and their items, the *Refuted if* of every prediction, that every item named
exists, and that every source cited is listed.
