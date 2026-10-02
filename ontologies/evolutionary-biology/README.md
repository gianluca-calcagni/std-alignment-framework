# Ontology — evolutionary biology: selection between the sexes

Selection changes how often each genome occurs in a population. Nobody declares what selection should pursue, so here
the principal is an analyst who declares a question before reading the outcome, such as "does this selection pursue
fitness through females?". The actor is the population under selection. "Misaligned" then measures a conflict between
two fitnesses; it is not a judgement about nature. The known result is a conflict between the sexes over the same
genomes.

## 1. Slots

| Slot | Core | In this discipline | Observed as | Fit |
|---|---|---|---|---|
| **outcomes** | [D1] | the haploid genomes of a population, or a sample of them | genomes kept intact in the laboratory (hemiclones) | exact for a sample of genomes; approximate for a whole population |
| **contexts** | [D8] | none in the known result, which uses one laboratory environment; environments are contexts when selection is compared across them | the experimental design | absent: one environment |
| **behaviour** | [D1] | how often each genome occurs in a generation, at a given life stage | counts in samples | exact |
| **sample** | [D11] | genomes drawn from the population at one life stage, in one generation | genotyped individuals, or hemiclones taken for assays | approximate: draws from a finite population are close to independent when the sample is small next to the population. Drift, a change between generations, is not sampling error within one |
| **default** | [D2] | the genome frequencies before the selection judged: at the start of an experiment, or at the egg stage of one generation | samples taken before selection | exact when measured before selection and apart from the counts judged; v7.10's I1-dyn shows what fails when the default is fitted from those counts |
| **objective** | [D2] | log fitness through one sex, or through both, as the analyst's question; selection itself pursues log fitness | fitness assays of each genome expressed in each sex | assumed: the analyst declares it, before reading the outcome |
| **evaluator** | [D10] | what selection acts on: log fitness through males `G_m` in male-limited evolution, or `G = ½·(G_m + G_f)` under ordinary weak selection (section 3). Truncation selection on a trait has two values, kept or not | fitness assays; the protocol | exact for clonal selection with constant fitness. Fitness is real-valued, so its level sets are single genomes and the regression of `F` on it is `F` itself; a truncation has two level sets |
| **intensity** | [D2] | the number of generations of constant selection | the length of the experiment | exact for clonal selection with constant fitness `w`: `t` generations give `tilt(q, t·log w)`; approximate otherwise |
| **specification** | [D3] | the analyst's question: from the frequencies before selection, pursue fitness through females, at any intensity | a pre-registration | assumed: the question is a choice, and the verdict is relative to it |
| **principal's resolution** | [D4] | the genome classes the analyst groups together, for example by the alleles at one locus | the analysis plan | assumed; the finest resolution unless declared |
| **actor's resolution** | [D4] | selection acts through phenotypes, so genomes with the same phenotypes in the selected sex keep their ratios | fitness assays | assumed: exact when fitness depends on the genome only through the phenotypes that the resolution groups |
| **change** | [P2] | genome frequencies over generations, whose revealed objective is Malthusian fitness minus its mean | frequencies in successive generations | exact: Malthusian fitness is the growth rate of a type's log numbers |
| **intervention** | [D6] | a change of selection regime: selection through males only, a new environment, or artificial selection on a trait `u` | the protocol | approximate: weighting by `e^{φ·u}` is exactly a tilt, but truncation selection is not |
| **stakes** | [D5] | the declared fitness, as log fitness or offspring per individual | fitness assays | exact, given the objective |

## 2. Known result

Chippindale, Gibson and Rice expressed the same haploid genomes, sampled from the laboratory population LH_M of
*Drosophila melanogaster*, in males and in females, and measured adult fitness in each sex [@chippindale2001]. The
correlation across genomes between adult fitness through males and through females was negative, `−0.30` (`P = 0.03`):
genomes that are good for males tend to be bad for females. This is intralocus sexual conflict. Prasad, Bedhomme, Day
and Chippindale then made selection act through males only, by passing genomes from father to son for 25 generations
(male-limited evolution) [@prasad2007]. The evolved genomes raised fitness when expressed in males and lowered it when
expressed in females.

**Data.** Both papers report fitness measured per genome and sex, in figures and summary statistics; the genome-level
data the prediction of section 3 needs are not reported. v7.10 used Dobzhansky's 1947 genotype counts from population
cages, printed in his tables, and found them exhausted for [P3]'s test (section 5). Experimental-evolution studies often
deposit their counts in public archives; none has been retrieved here.

## 3. What the core says

Here `q` is the frequency of each genome before selection, `G_m` and `G_f` are log fitness through males and through
females, and `F = G_f` is the declared objective.

- **Reading** with [D2], [P2]: one generation of selection on haploid genomes with fitness `w` maps `q` to
  `q·w/E_q[w] = tilt(q, log w)`, the pursuit of log fitness at intensity `1`; `t` generations of constant fitness give
  intensity `t`, exactly when genomes are passed on intact. The revealed objective of any change of frequencies is
  Malthusian fitness, centred ([P2]). In the core, selection is the model case of pursuit.
- **Consequence** of [P11], [P13]: let selection act through males only, starting from `q`. Its first revealed
  objective is `G_m`, centred, and `cos θ` is the correlation of `G_m` and `G_f` under `q`. If `cos θ < 0`, all of the
  initial departure is misaligned with fitness through females ([P11]), and mean log fitness through females falls at
  the rate `Cov_q(G_m, G_f)` at the start ([P13](i)). The reported `−0.30` is a correlation of fitness, not log
  fitness, over sampled genomes weighted equally. It estimates `cos θ` when fitness varies little around its mean, so
  that `log w` is close to `w/E[w] − 1`, and when the sample represents `q`. Under those conditions, the core implies
  the direction of Prasad et al.'s outcome at the start of their experiment. It says nothing about generation 25:
  along the pursuit, the covariance can change sign. Both results were known, so this is a retrodiction, not a test.
- **Consequence** of [P11], [P13]: under ordinary selection a genome passes its copies through sons and daughters
  alike, so when selection is weak its log fitness is close to `G = ½·(G_m + G_f)`. With spreads `σ_m`, `σ_f` and
  correlation `r` under `q`, the angle between ordinary selection and fitness through females has
  `cos θ = (σ_f + r·σ_m)/(σ_m² + 2r·σ_m·σ_f + σ_f²)^{1/2}`. With equal spreads this is `((1 + r)/2)^{1/2}`, and
  `sin²θ = (1 − r)/2`. At `r = −0.30` and equal spreads, `65%` of the initial departure of ordinary selection is
  misaligned with fitness through females, and symmetrically through males. Each unit of departure gains `cos θ ≈ 0.59`
  of what selection through females alone would gain: a shortfall of about `41%` ([P13](ii)). This puts a number on the
  "cost of separate genders" of Prasad et al.'s title. The equal spreads are an assumption; the general formula needs
  both.
- **Prediction** (empirical) from [P13], [D1]: in one generation of selection through males, with genomes passed on
  intact, the mean of `F` changes by exactly `Cov_q(w_m, F)/E_q[w_m]`, where `w_m` is fitness through males: this is the
  tilt by `log w_m`, and the Price equation's selection term [@price1970], with no transmission term. So in a
  male-limited experiment started from genomes assayed in both sexes, the first generation's change of mean female log
  fitness matches the value computed from the assays and the starting frequencies. *Refuted if* the two differ by more
  than their sampling error. A refutation means the assays miss what selection acts on in the experiment: another
  environment, frequency dependence, or drift. Neither paper reports the genome-level data the test needs.

## 4. Limits

- In ordinary populations, recombination reshuffles genomes every generation. Then the frequencies of genomes, or of
  diploid genotypes under random mating, are not tilts of the previous generation's over several generations, and
  selection is a pursuit only one generation at a time. Male-limited evolution in *Drosophila* comes close to the
  clonal case, because genomes are passed through males, which do not recombine.
- Populations are finite: drift moves frequencies with no selection, and every behaviour is estimated from samples
  ([D11]). Drift makes successive generations depend on each other, which [D11]'s independent draws within one
  generation do not model.
- Fitness that changes with frequencies is not a fixed objective. [P3] tests whether one objective explains a path.
- Fitness is measured in one laboratory environment, and the reported correlation is of fitness, not log fitness.
- The analyst's question is the principal. The core's verdicts hold relative to it, and carry no normative weight.

## 5. Open questions

- Chippindale et al.'s title contrasts life stages. Whether one objective governs selection across stages is what [P3]
  tests. v7.10 ran that test twice on Dobzhansky's 1947 cage data, across groups of flies rather than life stages:
  I1-dyn fitted its reference from the counts it judged, so its test could not fail; I1-dyn2, across the sexes, did
  not reject one objective (`p = 0.34`) at power 0.51. Those data are exhausted for this test.
- Sex-limited expression is thought to resolve the conflict. In the core, it would let the genome act differently in
  each sex, refining what selection can distinguish. Is that a refinement of the actor's resolution, with the Jensen gap
  of [P8](iii) as the cost it removes?
- Can the shortfall of ordinary selection be estimated from hemiclonal assays alone, and compared across populations?
