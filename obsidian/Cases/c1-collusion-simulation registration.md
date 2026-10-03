# C1 — Does coordination tell collusion from adaptation? Registration

**Kind:** simulation; it counts neither toward the finish line nor toward the base rate (`cases/README.md`). **Who:**
registered by the executor, a Claude model, under the PI's instruction to test as the executor sees fit (`NOTES.md`
§3.1, Q26). Nothing below has been computed before this file was pushed.

## Why

The industrial-organization ontology predicts that the coordination of two petrol stations' price moves ([[P39 — Several actors: coordination plus individual misalignment|P39]]), within
contexts and over episodes, rises once both adopt pricing algorithms that learned to coordinate, and is larger than
where only one adopted. Its specification, independent pursuit, charges every reaction, lawful adaptation to a rival's
prices included. Before that prediction meets data, this case asks whether the instrument can tell the two apart where
the truth is known: algorithms that learned to collude, against players that only adapt to the rival's last price. If it
cannot here, it cannot on German petrol prices, and the ontology's design must change before any of those data are read.

## The simulation

**Market.** The baseline of Calvano et al. [[References|@calvano2020]]. Two firms; logit demand
`q_i = e^{(a_i − p_i)/μ} / (Σ_j e^{(a_j − p_j)/μ} + e^{a_0/μ})`, with `a_i = 2`, `a_0 = 0`, `μ = 0.25`; marginal cost
`c_i = 1`; a firm's profit in a period is `(p_i − c_i)·q_i`. `p_N` is the static Nash price and `p_M` the common price
that maximizes joint profit, both computed on the continuum. Prices are 15 equally spaced points from
`p_N − 0.1·(p_M − p_N)` to `p_M + 0.1·(p_M − p_N)`.

**Players.**
- *Q-learning*, as in the paper: the state is the pair of last prices (225 states); learning rate `α = 0.15`;
  exploration with probability `ε_t = e^{−βt}`, `β = 4·10⁻⁶`, choosing a price uniformly at random; each `Q(s, a)`
  starts at the profit of `a` against a rival that picks uniformly at random, divided by `1 − δ`.
- *Best response*: the static best response to the rival's last price, ties to the lowest price. It does not learn.

**Arms**, 24 sessions each, each session with its own seed (arm offset plus session number):
- `Q95`: two Q-learners with discount `δ = 0.95`, the paper's baseline, which learned to collude there;
- `Q0`: two Q-learners with `δ = 0`, reported only;
- `BR`: two best responders: adaptation without learning;
- `MIX`: one Q-learner with `δ = 0.95` against one best responder, which explores during learning as the Q-learner does.

**Learning** stops when every Q-learner's greedy strategy has been unchanged for 100,000 consecutive periods, or at
`10⁷` periods; sessions stopped at the cap are counted and kept. `BR` has no learning phase and starts from prices drawn
uniformly.

**Measurement.** Strategies are then frozen. For `T = 200,000` periods each firm plays its strategy, except that with
probability `0.05`, independently of the other firm and of the past, it plays a price drawn uniformly: the shocks that
make reactions visible. The first 1,000 periods are discarded. Separately, the profit gain `Δ = (π̄ − π_N)/(π_M − π_N)`
is measured over 1,000 periods of the frozen strategies without shocks, from the state at which learning stopped (from
random prices for `BR`), with `π̄` the average profit per firm and `π_N`, `π_M` the profits at `p_N` and `p_M`.

## Quantities

Each firm's **move** in a period is the sign of its price change from the previous period: down, none or up. For each
session, with `N` the number of observations and mutual information computed from counts:
- `K1`, coordination within a period: the mutual information between the two firms' moves in the same period.
- `K2`, coordination over episodes of two periods: the mutual information between firm A's pair of moves and firm B's
  pair, over non-overlapping episodes (periods 1 and 2, 3 and 4, …).
- `Kh`, coordination given the last prices: the average over states `s` of the mutual information between the two moves
  given that the last prices were `s`, weighted by the frequency of `s`.

`K1` and `K2` are corrected for bias by Miller and Madow's rule: the plug-in value minus `(k_AB − k_A − k_B + 1)/(2N)`,
with `k` the numbers of non-empty cells. `Kh` is the plug-in value, and `G = 2N·Kh` with `df = Σ_s (r_s − 1)(c_s − 1)`,
where `r_s` and `c_s` are the numbers of A's and B's moves seen in state `s`.

## Validity, then predictions

**Validity.** If either fails, the case is void, not failed: the simulation would not reproduce the setting it stands
for.
- V1: the mean `Δ` over the `Q95` sessions is at least `0.5` (the paper reports `0.85`).
- V2: the mean `Δ` over the `BR` sessions is at most `0.2`.

**Predictions.**

| Id | From | Label | Prediction | Held if |
|---|---|---|---|---|
| S1 | [[P39 — Several actors: coordination plus individual misalignment\|P39]] | simulation | algorithms that learned to collude coordinate more over episodes than players that only adapt: `K2` larger in `Q95` than in `BR` | one-sided Mann–Whitney test over the 24 and 24 sessions, `p < 0.01` |
| S2 | [[P39 — Several actors: coordination plus individual misalignment\|P39]] | simulation | their coordination lies in time: `K2 > 2·K1` in a `Q95` session, more than two independent periods would give | in at least 22 of the 24 `Q95` sessions |
| S3 | [[P39 — Several actors: coordination plus individual misalignment\|P39]], [[D8 — Conditions, responses and views\|D8]] | verification | given the last prices, coordination is zero, since each strategy reads only the last prices and shocks are independent: the consequence of the ontology's section 3, and a check of the code | `G ≤ 2·df + 20` in every session of every arm |
| S4 | [[P39 — Several actors: coordination plus individual misalignment\|P39]] | simulation | two algorithms that learned to collude coordinate more over episodes than one such algorithm facing a best responder: `K2` larger in `Q95` than in `MIX` | one-sided Mann–Whitney test, `p < 0.01` |

**Readings, fixed now.**
- S1 fails: the instrument does not tell collusion from adaptation even where the truth is known. The
  industrial-organization prediction is revised before any German price is read, and the revision is recorded.
- S2 fails: the ontology's reading of the known result, that the algorithms' coordination unfolds over rounds
  ([[P39 — Several actors: coordination plus individual misalignment|P39]](iii)), is wrong for this setting, and is recorded as such.
- S3 fails: a bug, or the consequence is wrong; nothing else is read until it is explained.
- S4 fails: the second comparison of the industrial-organization prediction, with markets where only one station
  adopted, has no support from this mechanism; the prediction is revised as for S1.

Reported without a prediction: `K1`, `K2`, `Kh` and `Δ` for every arm, `Q0` included; the number of periods to
convergence; and how many sessions end at a single pair of prices rather than a cycle.
