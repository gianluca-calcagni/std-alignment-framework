# General results — the disciplines on a continuum

The ontologies (`ontologies/`) are written for the finite core, and lint fixes their sections, so their reading on a
continuum lives here. Each discipline shows one phenomenon of the general case. These are readings, not predictions; the
predictions are in the ontologies, on finite records.

| Discipline | What is continuous | Phenomenon | What must be declared |
|---|---|---|---|
| machine learning | the reward model's score; actions in continuous control. Responses are texts, countably many: no σ-algebras beyond partitions, only tails | one-dimensional evaluators; tails | a proper default; a nearness for deterministic policies |
| evolutionary biology | trait values; fitness | noise: a phenotype is never pinned | nothing beyond the core |
| behavioural economics | amounts chosen, with piles at exact values | atoms, which a tilt cannot create | a record's resolution |
| medical sciences | time in the department; a patient's severity | resolutions of statistics that merge outcomes; conditions met once | a record's resolution; the risk model's statistic |
| experimental economics | the shares of a population of players; time, in continuous-time sessions | irreversibility: learning that goes round in circles | a record's resolution in time and in shares |
| industrial organization | prices; time | coordination in time | the length of an episode, the record's resolution in time |

**Machine learning.** Responses are sequences of tokens: countably many outcomes, so every resolution is a partition, as
in the core, and what changes is the tails. A reward model's score is unbounded in principle. If its error has a heavy
upper tail under the base policy, the evaluator is not pursuable (GD2), and regularizing fine-tuning by KL cannot
contain it; Kwa et al. measured the tails of reward models and found them light, so this is a possibility the framework
can test, not a finding [@kwa2024]. The score is one number per response, so its distribution under the base policy,
recorded by an empirical distribution function with its bands (GD11), carries best-of-`n`: its divergence exactly, and
its gold curve from the regression of the gold score on the proxy score (`transfer.md`). The ontology's prediction from
[P20] could then be stated for best-of-`n`. In continuous control, actions are vectors: a deterministic policy pins
values, and needs a declared nearness to score `0` at its target, and noise or a resolution to be graded near it (GD3,
GD7). Maximum-entropy methods need a proper default (GD2).

**Evolutionary biology.** Trait values and fitness components are continuous. Selection with log-fitness `F` for `t`
generations, for types passed on intact, is pursuit at intensity `t` ([D2], Notes), and stabilizing selection,
`F(x) = −(x − θ)²`, on a normal default is `transfer.md`'s on-target example. A population never pins a phenotype,
because phenotypes include environmental variation that the genotype does not control: biology supplies the precision of
GD7 as a fact, and the singular case does not arise. Selection gradients are regressions of relative fitness on traits
[@lande1983]; with normal traits, the plane spanned by two objectives (`NOTES.md` §5.4, H6) has closed forms. In the
ontology's known result, fitness through males is the evaluator and fitness through females the target. With fitness
measured as a continuous quantity, the regression is the average fitness through females at each value of fitness
through males: informative because one number summarizes a genotype of many loci, and so merges genotypes.

**Behavioural economics.** A default produces a pile of people at one exact choice. Where choices are amounts, such as
savings in money or taxable income near a kink in a tax schedule, a pile is an atom: an exact value chosen with positive
probability. A tilt keeps the events of probability zero (GD6), so a pile at a value that had probability zero before is
not the pass-through of any incentive, whatever its form; economists measure such piles as bunching [@kleven2016]. Where
choices are whole percentages, as contribution rates usually are, outcomes are finite and the core applies as it stands.
The continuous reading is consistent with the refutation of the two-default prediction (`RECORD.md` §2.1): a default is
not a bonus added to what people pursue, but a change in which choices are made exactly. A pass-through test then
applies to the shape of the distribution away from the piles.

**Medical sciences.** Time in the department is continuous; the four-hour target, pass or breach, has two cells on a
continuum too. "Departments only add the target to what they pursue" now says that the ratio of the distribution of
waiting times after the target to the distribution before is a function of the target's statistic: one value below four
hours and one above. So the shape of the waiting-time distribution inside each of the two intervals is unchanged. Mason
et al.'s three intervals [@mason2012] and national counts by minute are two records of it, kept at two resolutions, and
the departure inside the passing cell measured on either is a lower bound that rises with the resolution. A pile of
departures in the last minutes before four hours is close to an atom, and its size in nats depends on the record's
resolution, which is why that resolution is declared before the test (GA5). Since no pursuit of the target makes a pile
(`derived-spaces.md`), a pile is evidence of something the target does not explain; and from records at 20, 10, 5 and 1
minutes, the growth of the misalignment estimates how many patients were timed to the threshold (`vocabulary.md`,
"fudging"). For the report cards, a patient's severity is a continuum, and the risk model reads a few recorded
variables: a statistic that merges patients whom clinicians tell apart. The card judges at the resolution of that
statistic, and the clinicians act at a finer one, inside cells of probability zero: a difference of resolution between
principal and actor that needs σ-algebras. And each patient arrives once (GD9): the response to one patient is never
observed, only how treatment goes with severity across patients.

**Experimental economics.** In a population game played in continuous time, the state is the share of the population
playing each strategy, a point of a simplex, and the record is a trajectory. Cason, Friedman and Hopkins ran
Rock–Paper–Scissors population games of this kind and found cycles in the population mix [@cason2014]. On the finite
record that the ontology uses, transitions between coarse states, the departure from reversibility is [P41]'s
Jensen–Shannon divergence; on the continuum, it is an entropy production rate per unit of time, and for learning by
logit responses it is the game's harmonic circulation, times the intensity, squared, times the conductance of the
learning rule (`derived-spaces.md`).

**Industrial organization.** Prices are continuous in principle and recorded to the cent; time is continuous, and German
stations report each price change to the regulator as it happens. Coordination between two stations is [P39]'s on a
finite episode. On a continuum of time it becomes a rate: the mutual information per unit of time between the two price
paths, which can be positive while every snapshot of the two prices shows none (T3). Assad et al. found margins rising
in duopolies only when both stations had adopted pricing algorithms, and only about a year later [@assad2024]: the
reading here is that what the algorithms learned shows in the paths, not in any one snapshot.
