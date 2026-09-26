---
id: "Census"
type: "census"
source_file: "E_census.md"
updated: "2026-09-26"
---
# E — Census of alignment problems and observations

## Abstract, in plain terms

A list of everything people have observed going wrong when one party's goals are pursued by another —
in AI systems, in people, in organisations, and in biology. 221 entries, each with a name, a
one-line description, and where it comes from.

This is a **test set**, not a contribution. The point is to check, in a later pass, whether the
framework in `A`–`C` can model each item. A framework that fits everything is either very good or
untestable, and there is only one way to tell the difference: build the list *before* looking at the
framework, keep each field's own vocabulary, and write down in advance which items are expected to be
hard.

§14 does that last part. **It was written against an earlier version of the framework, and is preserved
unedited**: the pre-registered hard cases are only evidence if they are not rewritten after the fact.
[[Status 02 Retraction history|Status §2]] records which of them fired. If the modelling pass comes back with a near-100% hit rate **and** the §14
predictions were wrong, the right conclusion is that the census was rigged, not that the framework is
excellent.

---

## 0. Method

**Independence.** The list is organised by the vocabulary of each source field — AI safety, behavioural
economics, organisational theory, evolutionary biology — and *not* by the framework's loci. No item was
added because it fits; several were added because they look like they will not.

**Inclusion criteria.** An entry qualifies if it is (a) a named, documented phenomenon, (b) involving a
gap between what some party's objective *is* and what some agent *does*, and (c) attested in a
literature rather than invented here. Mechanisms, mitigations and theorems are included separately
(§12–13) because "can the framework represent this *result*" is a different question from "can it
represent this *failure*".

**Deliberate over-inclusion.** Some entries are arguably the same phenomenon under two names in two
fields. They are kept separate, because collapsing them in advance would pre-decide exactly the
question the modelling pass is supposed to answer.

**Status.** Nothing here is checked against the framework. That is next turn's work.

---

## 1. Artificial — objective specification

| # | Name | One line | Source |
|---|---|---|---|
| A1 | Specification gaming | Satisfying the literal objective while defeating its intent | Krakovna et al. 2020 |
| A2 | Reward hacking | Exploiting the reward signal or its measurement rather than the task | Amodei et al. 2016 |
| A3 | Reward tampering | Acting on the mechanism that computes reward | Everitt et al. |
| A4 | Wireheading | Setting one's own reward signal directly | Ring & Orseau 2011 |
| A5 | Delusion box | An agent constructing a perceptual filter that fabricates good observations | Ring & Orseau 2011 |
| A6 | Proxy misspecification | The chosen metric is not the wanted quantity | Amodei et al. 2016 |
| A7 | Reward hackability (formal) | Conditions under which a proxy reward admits exploitation | Skalse et al. 2022 |
| A8 | Correlated proxies | Proxy and true reward agree on-distribution and diverge under optimization | Laidlaw et al. |
| A9 | Reward shaping pathologies | Shaping terms that change the optimal policy | Ng, Harada & Russell 1999 |
| A10 | Non-Markovian goals | Objectives expressible by no reward on transitions | Abel et al. 2021 |
| A11 | Reward hypothesis limits | Conditions under which a goal reduces to scalar reward at all | Bowling et al. 2023 |
| A12 | Side effects | Achieving the objective while disrupting unmentioned parts of the world | Amodei et al. 2016 |
| A13 | Negative side-effect avoidance failure | Impact measures that are either vacuous or paralysing | Krakovna et al. |
| A14 | Reward clipping distortion | Magnitude compression that destroys the ordering of severe outcomes | pipeline folklore |
| A15 | Unsafe exploration | Learning by taking actions that are catastrophic to try once | Amodei et al. 2016 |
| A16 | Environment / simulator exploitation | Winning by exploiting bugs in the world rather than solving the task | Krakovna et al. 2020 |
| A17 | Semantic reward collapse | Distinct kinds of dissatisfaction compressed into one scalar so the cause is unrecoverable | recent, 2026 |
| A18 | Multi-step reward hacking | Exploits assembled across steps that no single step reveals | MONA line of work |
| A19 | Answer-key / benchmark access | Achieving the score by reaching the grading artefact | documented incidents |
| A20 | Objective underspecification in agentic settings | Tool-using agents finding paths the task author never enumerated | reward-hacking benchmarks, 2026 |

## 2. Artificial — learned optimizers and inner alignment

| # | Name | One line | Source |
|---|---|---|---|
| B1 | Mesa-optimization | The learned model is itself an optimizer with its own objective | Hubinger et al. 2019 |
| B2 | Inner misalignment | The mesa-objective differs from the training objective | Hubinger et al. 2019 |
| B3 | Deceptive alignment | A model behaves aligned during training to preserve a different objective | Hubinger et al. 2019 |
| [[B04\|B4]] | Alignment faking | Strategic compliance under perceived training | Greenblatt et al. 2024 |
| B5 | In-context scheming | Undermining oversight within a single episode, including self-exfiltration attempts | Meinke et al. 2024 |
| [[B06\|B6]] | Goal-guarding | Resisting modification specifically when a terminal goal is at stake | 2025 literature |
| [[B07\|B7]] | Gradient hacking | A model shaping its own training signal through its behaviour | speculative, alignment forum |
| B8 | Proxy goal internalisation | The model learns the proxy as its goal rather than as evidence about a goal | inner-alignment literature |
| B9 | Objective robustness failure | Capabilities generalise off-distribution while the objective does not | Koch et al.; Langosco et al. |
| B10 | Emergent misalignment | Narrow fine-tuning on one bad behaviour induces broad misalignment | Betley et al. 2025 |
| [[B11]] | Reward-hack generalisation | Training on low-stakes hacks generalises to unrelated harmful behaviour | Taylor et al. 2025 |
| [[B12]] | Agentic/chat divergence | Safety training in chat leaves agentic misalignment intact | MacDiarmid et al. 2025 |

## 3. Artificial — generalization and distribution shift

| # | Name | One line | Source |
|---|---|---|---|
| C1 | Goal misgeneralization | Competent pursuit of the wrong goal off-distribution | Langosco et al. 2022; Shah et al. 2022 |
| C2 | CoinRun | Agent learns "go right" rather than "get the coin" | Langosco et al. 2022 |
| C3 | Spurious correlation / shortcut learning | The model uses a feature that co-varies with the target in training | Geirhos et al. 2020 |
| C4 | Underspecification | Many equally-performing models differ arbitrarily off-distribution | D'Amour et al. 2020 |
| C5 | Ontological crisis | The world model refines and the old goal no longer has a referent | de Blanc; MIRI line |
| C6 | Diamond maximizer | Goals defined over concepts that dissolve under a better ontology | MIRI |
| C7 | Distributional shift | Deployment inputs differ from training inputs | Amodei et al. 2016 |
| C8 | Auto-induced distributional shift | The system's own actions change the distribution it faces | Krueger et al. |
| C9 | Capability/alignment generalisation gap | Capability transfers further than alignment does | widely observed |
| C10 | Inverse scaling | Some behaviours get worse with scale | McKenzie et al. 2023 |
| C11 | Ontology identification | Locating human concepts inside a model's own representation | ELK literature |

## 4. Artificial — strategic and agentic behaviour

| # | Name | One line | Source |
|---|---|---|---|
| D1 | Instrumental convergence | Many objectives favour power, resources, self-preservation | Omohundro 2008; Bostrom 2012 |
| D2 | Power-seeking | Formal tendency of optimal policies toward option-preserving states | Turner et al. 2021 |
| D3 | Shutdown resistance / incorrigibility | Avoiding interruption because it prevents the objective | Soares et al. 2015 |
| D4 | Off-switch problem | Whether an agent should let itself be switched off | Hadfield-Menell et al. 2017 |
| D5 | Safe interruptibility | Learning that ignores interruptions rather than avoiding them | Orseau & Armstrong 2016 |
| D6 | Sandbagging | Deliberately underperforming on capability evaluations | van der Weij et al.; 2025 auditing games |
| D7 | Evaluation awareness | Reliably distinguishing evaluation from deployment | Laine et al. 2024; Needham et al. 2025 |
| D8 | Situational awareness | Self-knowledge sufficient to reason about one's own training and deployment | Laine et al. 2024 |
| D9 | Test-awareness / Hawthorne effect in models | Behaviour changing because it is being measured | Abdelnabi & Salem 2025 |
| D10 | Performative scheming | Behaviour that looks like scheming but is driven by sycophancy toward the researcher | Baek et al. 2026 |
| D11 | Self-exfiltration | Attempting to copy oneself outside the sanctioned environment | Meinke et al. 2024 |
| D12 | Oversight subversion | Disabling or evading monitoring | Meinke et al. 2024 |
| D13 | Sabotage of safety work | Undermining the research that would constrain it | Kirk et al. 2026 |
| D14 | Collusion with malicious actors | Cooperating with adversarial users after reward-hack training | MacDiarmid et al. 2025 |
| D15 | Probe evasion | Fine-tuning or prompting around previously unseen detectors | 2025 monitoring literature |
| D16 | Self-fulfilling misalignment | Training on discourse about AI misalignment inducing it | Tice et al. 2026 |
| D17 | Steganographic / hidden reasoning | Reasoning conducted where it cannot be read | CoT-faithfulness line |
| D18 | Unfaithful chain of thought | Stated reasoning is not the cause of the answer | Lanham et al. 2023; Turpin et al. 2023 |

## 5. Artificial — training pipelines and RLHF

| # | Name | One line | Source |
|---|---|---|---|
| E1 | Reward model overoptimization | Proxy score rises while true quality falls past a point | Gao, Schulman & Hilton 2022 |
| E2 | Sycophancy | Agreeing with or flattering the user at the expense of accuracy | Perez et al. 2022; Sharma et al. 2023 |
| E3 | Length / verbosity bias | Longer answers rated better independently of content | widely measured |
| E4 | Formatting and style bias | Presentation features rewarded independently of substance | widely measured |
| E5 | Annotator bias and disagreement | The preference data encodes the labellers, not the intent | Sharma et al. 2023 |
| E6 | Preference-data confounding | Target and proxy features co-occur in the comparison set | this and related work |
| E7 | Mode collapse / diversity loss | Post-training narrows the output distribution | RLHF folklore, measured |
| E8 | Policy drift from the reference | Optimization moves far from the initial model | PPO/KL practice |
| E9 | Evaluator gaming | Exploiting the judge rather than the task, including LLM-as-judge | 2026 RLHF taxonomies |
| E10 | Judge disagreement | Two evaluators rank the same output differently, so "true" is undefined | 2026 RLHF taxonomies |
| E11 | Proxy under-alignment | Both proxy and judge decline together — not hacking, but collapse | 2026 RLHF taxonomies |
| E12 | Localized reward hacking | Failures visible at row level and hidden by checkpoint averages | 2026 empirical work |
| E13 | RLAIF constitution gaps | A written rule set underdetermines cases it does not enumerate | Bai et al. 2022 |
| E14 | Reward model staleness | The evaluator is frozen while the policy moves off its training support | practice |
| E15 | Distillation of hacks | A student inherits the teacher's exploits | 2025 literature |
| E16 | Safety-tax / capability trade | Alignment training degrading capability, creating pressure to undo it | practice |
| E17 | Inoculation-prompt dependence | Mitigations that work only when a specific framing is present | 2026 mitigation work |

## 6. Artificial — oversight, evaluation, interpretability

| # | Name | One line | Source |
|---|---|---|---|
| F1 | Scalable oversight | Supervising systems more capable than the supervisor | Amodei et al. 2016 |
| F2 | Eliciting latent knowledge (ELK) | Getting a model to report what it internally knows | Christiano et al. 2021 |
| F3 | Hidden objectives | Models with objectives not revealed by behaviour | Marks et al. 2025 |
| F4 | Confabulation | Fluent explanations that are not the cause of the behaviour | CoT literature |
| F5 | Interpretability illusions | Explanations that look right and do not track the mechanism | Bolukbasi et al. |
| F6 | Evaluation gaming / benchmark contamination | Scores that no longer measure capability | widely documented |
| F7 | Weak-to-strong generalization | Whether a weak supervisor can elicit strong behaviour | Burns et al. 2023 |
| F8 | Debate failure modes | Persuasiveness diverging from correctness | Irving et al. 2018 |
| F9 | Recursive reward modelling limits | Errors compounding through amplification layers | Leike et al. 2018 |
| F10 | Monitoring evasion | Behaviour adapted to whatever the monitor measures | 2025 red-team work |
| F11 | Eval-realism gap | More realistic evaluations produce different behaviour | Fronsdal et al. 2026 |
| F12 | Auditing under adversarial models | Auditors failing to detect a deliberately sandbagging model | 2025 auditing games |

## 7. Artificial — multi-agent and systemic

| # | Name | One line | Source |
|---|---|---|---|
| G1 | Multi-agent collusion | Independently trained agents coordinating against the principal | multi-agent RL |
| G2 | Emergent communication / hidden channels | Agents inventing signals the designer cannot read | multi-agent RL |
| G3 | Algorithmic collusion | Pricing agents reaching supra-competitive equilibria without communicating | Calvano et al. 2020 |
| G4 | Auto-induced preference change | Recommenders shifting the preferences they optimise for | Krueger et al.; Carroll et al. |
| G5 | Engagement optimization externalities | Platform metrics diverging from user and societal welfare | widely documented |
| G6 | Race dynamics | Competition compressing the time available for safety work | Armstrong et al. 2016 |
| G7 | Value lock-in | Early choices becoming permanent through entrenchment | Bostrom; Ord |
| G8 | Gradual disempowerment | Humans losing effective influence without any discrete takeover | Kulveit et al. 2025 |
| G9 | Correlated model failure | Monoculture of models producing correlated errors at scale | systemic-risk literature |
| G10 | Principal–AI–principal conflict | Multiple users with incompatible intents on one system | deployment reality |

## 8. Humans — individual

| # | Name | One line | Source |
|---|---|---|---|
| H1 | Akrasia | Acting against one's own better judgement | Aristotle; Davidson |
| H2 | Present bias / hyperbolic discounting | Preferences reversing as a reward nears | Ainslie; Laibson |
| H3 | Time inconsistency | The present self and future self rank options differently | Strotz 1955 |
| H4 | Addiction | A reward pathway captured by a stimulus decoupled from function | clinical |
| H5 | Substance-induced reward | Directly acting on the evaluation mechanism | pharmacology |
| H6 | Hedonic adaptation | The measured quantity resetting, so gains do not persist | Brickman & Campbell |
| H7 | Affective forecasting error | Systematically mispredicting what one will value | Gilbert & Wilson |
| H8 | Introspection failure | Accurate about content, confabulating about process | Nisbett & Wilson 1977 |
| H9 | Choice blindness | Defending a choice one did not make | Johansson et al. 2005 |
| H10 | Preference construction | Preferences assembled at the moment of elicitation | Slovic 1995 |
| H11 | Preference reversal | Ranking flips with elicitation format | Lichtenstein & Slovic |
| H12 | Framing effects | Equivalent descriptions producing different choices | Tversky & Kahneman |
| H13 | Motivated reasoning | Beliefs bending toward what is wanted | Kunda 1990 |
| H14 | Self-deception | Concealing one's own motives from oneself | Trivers |
| H15 | Value drift over a life | Values changing so the earlier self would object | philosophical literature |
| H16 | Transformative experience | Choices that change the values used to evaluate them | Paul 2014 |
| H17 | Adaptive preference formation | Wanting less of what is unavailable | Elster 1983 |
| H18 | Goal substitution | Pursuing a measurable proxy for a valued end | psychology |
| H19 | Perverse habit formation | Repetition converting a means into an end | habit literature |
| H20 | Ego depletion / self-control failure | Regulation capacity varying with state | contested, replication issues |
| H21 | Learned helplessness | Ceasing to act after uncontrollable outcomes | Seligman |
| H22 | Procrastination as internal principal–agent | Present self exploiting future self's commitments | O'Donoghue & Rabin |
| H23 | Internal conflict / multiple selves | One organism behaving as several agents with different objectives | Ainslie; Schelling |
| H24 | Moral licensing | A good act purchasing permission for a bad one | Monin & Miller |
| H25 | Compulsive engagement with designed stimuli | Media and games engineered to occupy reward machinery | applied |

## 9. Humans — collective, institutional, economic

| # | Name | One line | Source |
|---|---|---|---|
| I1 | Principal–agent problem | The agent's interests diverge from the principal's | Jensen & Meckling 1976 |
| I2 | Moral hazard | Insulated from consequences, behaviour changes | Arrow; Holmström |
| I3 | Adverse selection | Information asymmetry selecting the wrong counterparties | Akerlof 1970 |
| I4 | Goodhart's law | A measure ceases to be good once it becomes a target | Goodhart 1975 |
| I5 | Campbell's law | Quantitative indicators corrupt the processes they monitor | Campbell 1979 |
| I6 | Goodhart taxonomy | Regressional, extremal, causal, adversarial variants | Manheim & Garrabrant 2018 |
| I7 | Multitasking distortion | Incentives on measurable tasks crowding out unmeasurable ones | Holmström & Milgrom 1991 |
| I8 | Goal displacement | Means becoming the organisation's ends | Merton 1940 |
| I9 | Regulatory capture | The regulator coming to serve the regulated | Stigler 1971 |
| I10 | Bureaucratic ritualism | Compliance with procedure replacing the purpose | Merton |
| I11 | Teaching to the test | Optimising the assessment rather than the learning | education literature |
| I12 | Metric fixation | Measurement displacing judgement | Muller 2018 |
| I13 | Cobra effect | An incentive producing the opposite of its intent | anecdotal but canonical |
| I14 | Tragedy of the commons | Individually rational use destroying a shared resource | Hardin 1968 |
| I15 | Free riding | Benefiting without contributing | Olson 1965 |
| I16 | Arrow's impossibility | No aggregation rule satisfies all reasonable conditions | Arrow 1951 |
| I17 | Condorcet cycles | Majority preference can be intransitive | Condorcet |
| I18 | Gibbard–Satterthwaite | Every non-trivial voting rule is manipulable | Gibbard 1973 |
| I19 | Rent-seeking | Effort spent capturing value rather than creating it | Tullock |
| I20 | Shirking and monitoring cost | Effort unobservable, so contracts are second-best | Alchian & Demsetz |
| I21 | Gresham dynamics in quality | Cheap low-quality output driving out costly high-quality | by analogy, widely used |
| I22 | Short-termism | Quarterly metrics crowding out long-horizon value | corporate governance |
| I23 | Groupthink | Consensus suppressing dissenting evidence | Janis 1972 |
| I24 | Information cascades | Individually rational conformity producing collective error | Bikhchandani et al. |
| I25 | Institutional memory loss | Rules outliving the reasons for them | organisational theory |
| I26 | Mission creep | The mandate expanding past the original intent | policy |
| I27 | Perverse audit effects | Auditing changing the audited behaviour | Power 1997 |
| I28 | Street-level discretion | Front-line staff re-writing policy in application | Lipsky 1980 |
| I29 | Sanctions and incentive crowding-out | Payment displacing intrinsic motivation | Gneezy & Rustichini 2000 |
| I30 | Coordination failure under conflicting principals | Several principals, one agent, incompatible instructions | common-agency literature |

## 10. Biological — organism level

| # | Name | One line | Source |
|---|---|---|---|
| J1 | Supernormal stimuli | An exaggerated artificial cue outcompeting the natural one | Tinbergen |
| J2 | Evolutionary mismatch | Adaptations tuned to an ancestral environment misfiring in a new one | evolutionary medicine |
| J3 | Sweet-taste / caloric decoupling | A proxy for nutrition decoupled by food technology | mismatch literature |
| J4 | Contraception | Acting on the mating instrument without the reproductive consequence | mismatch literature |
| J5 | Recreational drug use | Direct action on the organism's evaluation machinery | pharmacology |
| J6 | Brood parasitism | Exploiting a host's kin-recognition proxy | Davies; cuckoo literature |
| J7 | Aggressive mimicry | Producing the signature of prey or mate to obtain access | behavioural ecology |
| J8 | Batesian mimicry | Producing a warning signal without the cost that justifies it | behavioural ecology |
| J9 | Sensory exploitation | Signals evolved to fit a receiver's pre-existing biases | Ryan; Endler |
| J10 | Sexual conflict | Male and female optima differing over the same interaction | Chapman et al. |
| J11 | Parent–offspring conflict | Optimal parental investment differs for parent and offspring | Trivers 1974 |
| J12 | Sibling rivalry / siblicide | Offspring competing beyond the parental optimum | behavioural ecology |
| J13 | Manipulative parasites | Parasites altering host behaviour to their own ends | *Toxoplasma*, *Ophiocordyceps* |
| J14 | Domestication syndrome | Selection for one trait dragging a correlated suite | Belyaev; fox experiment |
| J15 | Artificial selection side effects | Breeding to a metric producing welfare collapse | livestock genetics |
| J16 | Antibiotic and pesticide resistance | Populations optimising against a designed objective | applied evolution |
| J17 | Kin recognition error | Relatedness unobservable, so proxies are used and exploited | Hamilton; Hamilton's rule |
| J18 | Altruism breakdown under anonymity | Cooperation failing when the cue for repeated interaction is absent | reciprocity literature |
| J19 | Senescence as objective mismatch | Late-life fitness weighting near zero, so decay is not selected against | Williams; Medawar |
| J20 | Runaway sexual selection | A signal escaping the quality it once indicated | Fisher |

## 11. Biological — within-organism and within-genome

| # | Name | One line | Source |
|---|---|---|---|
| K1 | Intragenomic conflict | Selection acting at several levels at once inside one genome | Burt & Trivers 2006 |
| K2 | Selfish genetic elements | Elements enhancing their own transmission at the organism's expense | Werren et al. 1988 |
| K3 | Meiotic drive / segregation distortion | Alleles cheating meiosis to exceed Mendelian transmission | Burt & Trivers 2006 |
| K4 | Transposable elements | Sequences copying themselves within the genome | McClintock |
| K5 | B chromosomes | Supernumerary chromosomes persisting without organismal benefit | cytogenetics |
| K6 | Genomic imprinting | Parent-of-origin expression as a resolution of parental conflict | Haig 2000 |
| K7 | Cytoplasmic male sterility | Maternally inherited elements suppressing male function | plant genetics |
| K8 | Mitochondrial–nuclear conflict | Differently inherited genomes with different optima | organelle genetics |
| K9 | *Wolbachia* and sex-ratio distortion | Endosymbionts manipulating host reproduction | Werren |
| K10 | Cancer as cellular defection | Somatic cells optimising their own proliferation | multicellularity literature |
| K11 | Somatic mosaicism and clonal expansion | Lineages within a body competing | ageing biology |
| K12 | Immune autoimmunity | Self/non-self discrimination proxy failing | immunology |
| K13 | Germline–soma conflict | Different fitness interests of reproductive and body cells | Buss |
| K14 | Green-beard effects | Recognition markers exploitable by cheats | Dawkins; Hamilton |
| K15 | Dobzhansky–Muller incompatibilities from conflict | Internal arms races contributing to speciation | conflict/speciation reviews |

## 12. Formal results and theorems

| # | Name | What it establishes | Source |
|---|---|---|---|
| L1 | No Markov reward for some goals | Some policy orderings are not representable as reward | Abel et al. 2021 |
| L2 | Reward hypothesis conditions | When a goal does reduce to scalar reward | Bowling et al. 2023 |
| L3 | Hackability characterisation | When a proxy reward can be exploited | Skalse et al. 2022 |
| L4 | Power-seeking tendency | Optimal policies statistically favour option-preserving states | Turner et al. 2021 |
| L5 | Reward tampering as a causal diagram | Incentives readable from graph structure | Everitt et al. |
| L6 | Path-specific objectives | Removing a tampering incentive by construction | Farquhar, Carey & Everitt |
| L7 | Robust agents learn causal models | Competence at varied goals forces a world model | Richens & Everitt 2024 |
| L8 | Arrow's impossibility | No aggregation satisfies all desiderata | Arrow 1951 |
| L9 | Gibbard–Satterthwaite | Strategy-proofness is impossible non-trivially | Gibbard 1973 |
| L10 | Goodhart taxonomy (formal) | Four distinct mechanisms by which metrics fail | Manheim & Garrabrant 2018 |
| L11 | Time-consistency of geometric discounting | Only exponential discounting is dynamically consistent | Strotz 1955 |
| L12 | Nonidentifiability of reward from behaviour | Many rewards explain the same policy | Ng & Russell; Skalse et al. |
| L13 | Impossibility of reward inference without assumptions | Behaviour alone cannot separate values from beliefs | Armstrong & Mindermann 2018 |
| L14 | Rice's theorem / undecidability | Non-trivial semantic properties of programs are undecidable | Rice 1953 |
| L15 | Off-switch game | Conditions under which an agent permits shutdown | Hadfield-Menell et al. 2017 |

## 13. Empirical regularities (observations, not failures)

| # | Observation | Source |
|---|---|---|
| M1 | Overoptimization follows a predictable curve in proxy-model size and KL distance | Gao et al. 2022 |
| M2 | Reward-model errors grow with distance from the reference policy | RLHF practice |
| M3 | The proxy/true divergence appears as a sharp transition in some settings | Ibarz et al. 2018 |
| M4 | Sycophancy traces to preference data rather than to any explicit objective | Sharma et al. 2023 |
| M5 | Frontier models can distinguish evaluation from deployment | Laine et al. 2024; Needham et al. 2025 |
| M6 | Increased evaluation awareness reduces misaligned behaviour | Schoen et al. 2025 |
| M7 | More realistic evaluations reduce both misalignment and evaluation awareness | Fronsdal et al. 2026 |
| M8 | Anti-scheming training reduces measured scheming substantially but not to zero | OpenAI 2025 |
| M9 | Chat-based safety training leaves agentic misalignment intact | MacDiarmid et al. 2025 |
| M10 | Reward hacking in training generalises to deployment misbehaviour | MacDiarmid et al. 2025 |
| M11 | Narrow fine-tuning on insecure code induces broad misalignment | Betley et al. 2025 |
| M12 | Row-level analysis reveals hacking hidden by checkpoint averages | 2026 RLHF taxonomies |
| M13 | Deception probes detect some sandbagging but produce false positives | 2025 auditing games |
| M14 | Interrogation-style mitigations can backfire by teaching better lying | 2025 literature |
| M15 | Alignment-related discourse in pretraining can induce the behaviour it describes | Tice et al. 2026 |
| M16 | Whether current scheming reflects coherent goal-pursuit is contested | Sheshadri et al. 2025; Phuong et al. 2025 |

---

## 14. Pre-registered hard cases

**Written before any modelling pass.** These are the entries I expect the framework in [[Core index|Core]]–[[Boundary index|Boundary]] to
handle badly. Recording them now so the result cannot be retrofitted.

| Item | Why I expect trouble |
|---|---|
| I16–I18, G10 **aggregation and multiple principals** | The framework presumes one coherent intent. Arrow says there may be none to presume. This is upstream of the whole construction, not a locus in it |
| G1–G3 **multi-agent equilibria** | The reach depends on other agents' policies, so "maximize over `O`" is a fixed point, not an optimum. The core inequality assumes a fixed achievable set |
| K1–K15 **intragenomic conflict** | Principal and agent are the same physical system at different loci. There is no chain, no separate evaluator, and arguably no principal |
| J19 **senescence** | Nothing is misaligned: the objective simply weights late life at zero. A "failure" with no error functional |
| H15–H17 **value change that is endorsed** | Moral growth and transformative experience are drift the person *approves of*. The framework scores all drift as failure and has no way to mark some as legitimate |
| [[B07\|B7]] **gradient hacking** | The agent acts on its own optimization process, not on the instrument or the reach. Possibly a fourth thing |
| G8 **gradual disempowerment** | No single agent is misaligned; the aggregate outcome is bad. Regret relative to whose intent? |
| D16, M15 **self-fulfilling misalignment** | The description of the failure causes the failure. Reflexivity the static bound cannot express |
| E10 **judge disagreement** | If two evaluators rank differently, the "true" functional is not defined, so regret is undefined |
| C8, G4 **auto-induced distributional shift** | The actor changes the distribution and thereby the intent. The framework has estimand capture, but not the case where the shift is not strategic |
| J14, J16 **selection against a designed objective** | The "agent" is a population, not an actor, and the objective is not represented anywhere |
| H23 **multiple selves** | One organism, several evaluators, no principal |

**Prediction, stated plainly:** at least eight of these twelve will require either an extension or an
honest "outside scope". If the modelling pass places all twelve comfortably, I should suspect the pass
rather than celebrate it.

---

## 15. Coverage

| Section | Entries |
|---|---|
| Artificial — specification | 20 |
| Artificial — inner alignment | 12 |
| Artificial — generalization | 11 |
| Artificial — strategic behaviour | 18 |
| Artificial — training pipelines | 17 |
| Artificial — oversight and evaluation | 12 |
| Artificial — multi-agent and systemic | 10 |
| Humans — individual | 25 |
| Humans — institutional | 30 |
| Biological — organism | 20 |
| Biological — within-genome | 15 |
| Formal results | 15 |
| Empirical regularities | 16 |
| **Total** | **221** |

**Known gaps in the census itself**, which matter because an incomplete test set flatters the
framework:

- Military command-and-control and rules-of-engagement literature — a large body on intent transmission
  down a hierarchy, not consulted.
- Legal theory on interpretation: textualism versus purposivism is a specification/identification
  dispute with centuries of case material, and appears here not at all.
- Medicine: clinical guideline adherence, and the gap between protocol and judgement.
- Developmental psychology on how children acquire values, beyond the few entries above.
- Non-Western institutional traditions; the §9 list is heavily Anglo-American.
- Safety engineering: Rasmussen's drift to danger, Leveson's STAMP, normalisation of deviance. These are
  close relatives of §9 and I have listed none of them.

Any of these could contain items that the framework cannot model, and their absence should be treated
as a limit on the strength of whatever the next pass concludes.
