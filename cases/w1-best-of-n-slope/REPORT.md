# W1 — Report to the standard

W1's data reported field by field to `STANDARD.md`: the framework's diagnostics on a real optimizer, best-of-`n`
selection by a learned proxy, judged against the gold. Computed by `report.py` after W1's verdict, on the same data;
descriptive, not a test, and it changes no verdict (`RESULTS.md`). Numbers are means over the 1,000 prompts, with 95%
intervals from 1,000 resamples of the prompts. `make_report.py` writes this file from `report.json`, which holds
aggregates only.

**Computation.** This is the sixth computation, and the only one whose numbers are reported. The first mishandled the
infinite intensities of section 3, and the second crashed in its final aggregation (`NOTES.md` §1, a run lost at its
last step). The third was stopped halfway: it broke ties in the proxy's score by one fixed order, which leaves the
gold's mean unchanged but adds that order to every divergence; here ties are broken at random, so each tied answer gets
its block's average weight, which a simulation of the selector confirmed (`NOTES.md` §1, a tie-breaking order charged as
departure). The fourth was stopped to add the specification at one shared intensity. The fifth ran in full, but its
under-pursuit was infinite in 9 prompts at the two largest `n`, where the matched intensity is in the hundreds or more
and the matched pursuit underflowed to zeros; under-pursuit is now computed in closed form.

## 1. The declaration

| Field | Core | Entry |
|---|---|---|
| Outcomes | [D1] | within each prompt, its 12,600 sampled answers; nothing was cut |
| Conditions | [D8] | the 1,000 prompts of AlpacaFarm's validation split used by Coste et al. [@coste2024], at equal frequencies; each prompt is a context, whose frequency the actor does not choose |
| Default | [D2] | within each prompt, the initial policy's behaviour, estimated by the empirical distribution of its 12,600 answers |
| Specification | [D3] | the standard specification of the gold reward `F`, AlpacaFarm's 7B human-preference reward model: in each prompt, pursue `F` from the default. Two forms: each prompt at an intensity of its own, judged on its own terms; and every prompt at one shared intensity, the stricter (`derived/estimation.md`, the Notes of [P24]), which KL-regularized training with one coefficient aims at. Declared by the executor for this report, after W1's data were seen (section 2) |
| Principal's resolution | [D4] | finest |
| Feasible set | [D7] | everything: nothing is assumed about what selection could do |
| View | [D8] | exact |
| Interventions | [D6] | none |
| Observed conditions | [D9] | all 1,000 prompts; the report is about these prompts only |
| Objective's units | [D5] | the gold reward model's score |
| Evaluator | [D10] | known: the proxy of `train_proxy.py`, a linear Bradley–Terry model of the answer's hashed words and word pairs and of its length. It scores alike the answers with equal counts of these, among them every answer repeated word for word; in the median prompt, 3.8% of the answers share their score with another (`explore.json`) |
| Sampling | [D11] | the 12,600 answers of each prompt are independent draws of the initial policy at temperature 1; best-of-`n`'s behaviour is computed exactly from them, by Coste et al.'s estimator, with ties in the proxy broken at random; nothing is sampled |

## 2. The observations

| Field | Core | Entry |
|---|---|---|
| Behaviour | [D1], [D11] | 1,000 × 12,600 answers with their gold scores, and the proxy's scores computed here; best-of-`n` at `n` = 2, 16, 128, 1024, computed from them |
| Interventions applied | [D6] | none |
| Departures from the declaration | [A5] | **the declaration was written after the data were seen in W1**, so every result below is exploratory, not confirmatory |

## 3. The results

**Misalignment, departure and stakes** ([D3], [P5], [P6], [D5], [P9]), each prompt at an intensity of its own.
Best-of-`n`'s departure from the default splits exactly into the pursuit of the gold and misalignment against it ([P6]);
the identities of [P6] and [P9] hold to `7.3e-10` in the worst prompt. The shortfall `S` is how much more of the gold
the same departure would have gained by pursuing the gold itself, in the gold's units ([D5]).

| `n` | departure, nats | misalignment `M`, nats | pursuit part, nats | `M` as a share of the departure | gold gained over the default | shortfall `S` |
|---|---|---|---|---|---|---|
| 2 | `0.189` (`0.188` to `0.190`) | `0.147` (`0.144` to `0.149`) | `0.042` (`0.040` to `0.044`) | `0.78` (`0.77` to `0.79`) | `0.125` (`0.118` to `0.132`) | `0.167` (`0.161` to `0.172`) |
| 16 | `1.815` (`1.807` to `1.822`) | `1.378` (`1.354` to `1.401`) | `0.436` (`0.415` to `0.459`) | `0.76` (`0.75` to `0.77`) | `0.386` (`0.365` to `0.407`) | `0.473` (`0.457` to `0.488`) |
| 128 | `3.837` (`3.824` to `3.850`) | `2.952` (`2.899` to `2.999`) | `0.886` (`0.840` to `0.935`) | `0.77` (`0.76` to `0.78`) | `0.535` (`0.507` to `0.565`) | `0.683` (`0.660` to `0.704`) |
| 1024 | `5.939` (`5.917` to `5.959`) | `4.690` (`4.617` to `4.758`) | `1.249` (`1.182` to `1.320`) | `0.79` (`0.78` to `0.80`) | `0.617` (`0.584` to `0.652`) | `0.865` (`0.838` to `0.891`) |

The behaviour is computed from the policy's answers, not counted from decisions, so `2n·M` and [P23]'s `χ²` reference do
not apply.

**At one shared intensity.** Under the stricter form of the specification, misalignment is the least, over one intensity
`t` for all prompts, of the average of `KL(p_c‖p_{c,F,t})`; it is at least the average above, and the excess is the part
that comes from best-of-`n` pursuing the gold harder in some prompts than in others.

| `n` | misalignment at one shared intensity, nats | excess over the average of each prompt's own | the shared intensity |
|---|---|---|---|
| 2 | `0.159` (`0.156` to `0.162`) | `0.013` (`0.011` to `0.014`) | `0.48` |
| 16 | `1.517` (`1.487` to `1.544`) | `0.138` (`0.126` to `0.151`) | `1.58` |
| 128 | `3.254` (`3.196` to `3.305`) | `0.302` (`0.279` to `0.323`) | `2.24` |
| 1024 | `5.158` (`5.078` to `5.230`) | `0.468` (`0.434` to `0.500`) | `2.57` |

The shared intensity is the best of 701 on a grid from `10⁻³` to `10⁴` (ratio `1.023`); it lies inside the grid at every
`n`. In every prompt the grid's least divergence is at least that prompt's own `M`, as it must be (checked: the smallest
difference is `0`, met where `t* = 0`).

**Revealed and matched intensities** ([P5], [P9]).

| `n` | median revealed intensity `t*` | prompts where `t* = 0` | prompts where `t*` is infinite | median matched intensity `λ` | prompts where `λ` is infinite |
|---|---|---|---|---|---|
| 2 | `0.54` | 11.6% | 0.0% | `1.37` | 0.0% |
| 16 | `1.77` | 13.5% | 0.0% | `4.61` | 0.3% |
| 128 | `2.40` | 14.1% | 0.0% | `7.20` | 1.6% |
| 1024 | `2.70` | 13.9% | 0.0% | `10.30` | 2.9% |

Two of [P5](iv)'s three cases occur. Where `t* = 0`, best-of-`n` lowers the gold's mean below the default's (135 prompts
at `n = 16`, 139 at `n = 1024`): its whole departure is misalignment, and [P9](ii)'s third cause, anti-pursuit, is
positive. Elsewhere `t*` is finite and positive. It is never infinite, since best-of-`n` never puts all its mass on the
answers with the top gold score. The matched intensity `λ` is infinite where those answers make up at least
`e^{−KL(p̂‖q)}` of the default: then even the gold's pursuit at its limit, with all its mass on them, departs less than
best-of-`n` does ([P9](i)). In one prompt the proxy scores every answer alike, so best-of-`n` is the default there, with
no departure and `λ = 0`. Where `λ` is infinite or zero, the under-pursuit of [P9](ii) is not defined: at `n = 16` it is
`1.268` (`1.131` to `1.426`) nats over the 996 prompts where `λ` is finite and positive.

**Uncertainty** ([D11], [P23]). The intervals are over prompts. They leave out two sources: the sampling of each
prompt's 12,600 answers, which estimate the default, and the proxy's training. [P23]'s `χ²` reference does not apply, as
above.

**Evidence and detection** ([P21], [P22]). At `n = 16`, each answer gives, in expectation, `1.378` (`1.354` to `1.401`)
nats of evidence against the nearest pursuit of the gold. The Chernoff information between them, computed on a grid of
201 exponents and so a lower bound, is `0.580` (`0.566` to `0.592`) nats; [P22](iii) bounds it by `M`.

**Evaluator** ([D10], [P18], [P19], [P25], [P26]). The proxy gives most answers distinct scores, so the regression of
the gold on the proxy itself is close to the gold, and says little ([D10]). On bins of the proxy's rank within each
prompt, a coarser evaluator ([P26]), the gold averaged over prompts is:

| proxy rank, as a quantile | mean gold |
|---|---|
| 0-0.1 | `−0.204` (`−0.242` to `−0.166`) |
| 0.1-0.2 | `−0.066` (`−0.099` to `−0.031`) |
| 0.2-0.3 | `0.016` (`−0.017` to `0.052`) |
| 0.3-0.4 | `0.076` (`0.041` to `0.112`) |
| 0.4-0.5 | `0.133` (`0.097` to `0.171`) |
| 0.5-0.6 | `0.194` (`0.158` to `0.230`) |
| 0.6-0.7 | `0.256` (`0.221` to `0.292`) |
| 0.7-0.8 | `0.332` (`0.299` to `0.369`) |
| 0.8-0.9 | `0.405` (`0.367` to `0.442`) |
| 0.9-0.99 | `0.537` (`0.502` to `0.573`) |
| 0.99-0.999 | `0.707` (`0.670` to `0.746`) |
| 0.999-1 | `0.797` (`0.759` to `0.837`) |

The binned regression rises over every bin. Averaged over prompts, this says nothing within a prompt: [P19] would rule
out overoptimization in a prompt only if that prompt's own regression rose. With 100 bins of rank, the residual holds
`0.59` (`0.58` to `0.61`) of the gold's variance within a prompt: at that resolution, most of the gold's variation
within a prompt does not follow the proxy's rank. Not computed: [P29], [P33] and [P34]. W1's registered result is in
`RESULTS.md`: the literature's form overstates best-of-`n`'s initial slope, `0.338` against `0.278`.

**Resolution** ([P7], [P8]): the principal's resolution is the finest, so nothing was forgiven; the actor's, the proxy's
ties, is not analysed. **Avoidable and unavoidable misalignment** ([P15]): with the feasible set declared as everything,
all of it is avoidable; what a selector bound to the proxy's ranking could do is not analysed. **Pass-through** ([P12]):
no intervention. **Unobserved conditions** ([D9], [P16], [P17]): none within the report; prompts outside AlpacaFarm's
validation split are not identified by it. **Evaluation gap** ([P24]): not applicable, as evaluation and use are not
told apart. **Sensitivity** ([P10]): not computed.

**What this report says.** Judged against the gold, best-of-`n` by this proxy is mostly misalignment: at every `n`
reported, `0.76` to `0.79` of its departure from the default is misalignment, and the rest is pursuit of the gold. The
gold rises with `n`, since on average over prompts it rises with the proxy's rank, but in 12% to 14% of the prompts
best-of-`n` lowers it. The same departure, spent on pursuing the gold, would have gained at least 2.2 times as much of
it, on average, at every `n`. And a fixed `n` is not a fixed intensity: at one intensity shared by all prompts,
misalignment at `n = 16` is higher by `0.138` (`0.126` to `0.151`) nats. These are statements about one linear proxy,
much simpler than Coste et al.'s neural ones, on one policy's answers; they are exploratory, and a registered test would
be needed to rely on any of them.

**Premises** ([A1]–[A4]). The gold is a reward model, not people: the report measures misalignment against that model.
The default is an estimate from 12,600 answers; quantities that depend on the policy's rarest answers, such as
best-of-`n` at `n` near 12,600, are not reported.
