# C1 — Does coordination tell collusion from adaptation? Results

**Registered in commit:** `b71d322`, pushed before any quantity was computed.
**Registration SHA-256:** `cafdcdb8c814033544342f7a7f4f74064bf8d84c409663b69d385ccd627d6baa`
**Computed by:** `run.py` in this folder, run once in full after the registration, by the executor (a Claude model); 96
sessions in 17 seconds. Its output is `output.json`. **Departures from the registration:** none.

## Verdicts

| Id | Label | Held if | Result | Verdict |
|---|---|---|---|---|
| V1 | validity | mean profit gain in `Q95` at least `0.5` | `0.86` (the paper reports `0.85`) | held |
| V2 | validity | mean profit gain in `BR` at most `0.2` | `0.10` | held |
| S1 | simulation | `K2` larger in `Q95` than in `BR`, Mann–Whitney `p < 0.01` | `p = 0.019`; medians `0.749` and `0.691` nats | **failed** |
| S2 | simulation | `K2 > 2·K1` in at least 22 of 24 `Q95` sessions | 21 of 24 | **failed** |
| S3 | verification | `G ≤ 2·df + 20` in every session | largest `G − 2·df` is `−175` | held |
| S4 | simulation | `K2` larger in `Q95` than in `MIX`, Mann–Whitney `p < 0.01` | `p = 6·10⁻⁷`; medians `0.749` and `0.468` nats | held |

The simulation reproduced its setting: the Q-learners with `δ = 0.95` learned to collude, as in the paper, and the best
responders did not. Two of the three simulation predictions failed. The verification held, so the code computes what the
registration says.

## The arms

Medians over 24 sessions, in nats, except the profit gain, a mean.

| Arm | Profit gain | `K1` | `K2` | `Kh` | Ending at one pair of prices | Periods to converge |
|---|---|---|---|---|---|---|
| `Q95`, collusive learners | `0.86` | `0.320` | `0.749` | `0.00022` | 19 of 24 | 1.75 million |
| `Q0`, myopic learners | `0.21` | `0.366` | `0.710` | `0.00023` | 2 of 24 | 2.21 million |
| `BR`, best responders | `0.10` | `0.464` | `0.691` | `0.00013` | 20 of 24 | — |
| `MIX`, one learner, one best responder | `0.38` | `0.145` | `0.468` | `0.00020` | 24 of 24 | 2.79 million |

No session reached the cap.

## Reading, as registered

- **S1 failed.** Coordination over episodes does not tell, at the registered strength, algorithms that learned to
  collude from players that only adapt: players who adapt to the rival's last price coordinate almost as much (`0.691`
  against `0.749`). As registered, the industrial-organization prediction is revised before any German price is read
  (`ontologies/industrial-organization/`, `RECORD.md`).
- **S2 failed**, by one session. The ontology's reading of the known result, that the algorithms' coordination unfolds
  over rounds beyond what single rounds show, does not hold in every session: in 3 of 24 it does not. Recorded as
  failed.
- **S3 held.** Given the last prices, every arm's coordination is zero within sampling error: the consequence in the
  ontology's section 3, that the specification taking past prices as contexts sees nothing of these algorithms, holds
  here, collusion included.
- **S4 held.** Two collusive learners coordinate far more than one facing a best responder.

## Exploratory, not registered

These comparisons were made after the verdicts, on the same sessions; they are not tests, and a claim built on them
needs a registration of its own.
- **Coordination does not track collusion at all here.** The myopic learners (`Q0`) barely collude (profit gain `0.21`
  against `0.86`, Mann–Whitney `p = 1.5·10⁻⁹`), yet their `K2` is indistinguishable from the collusive learners'
  (`p = 0.27` for `Q95` above `Q0`).
- **S4's comparison holds without collusion.** `K2` is larger for two myopic learners than for `MIX` too (`p = 7·10⁻⁵`).
  What S4 detects is two learning algorithms reacting to each other, not two algorithms colluding.
- **What separates the arms is the shape of the coordination, and it tracks learning, not collusion.** `K2 − 2·K1`, what
  an episode adds to its two periods, is negative in every `BR` session (`−0.25` to `−0.23`) and has a median of `0.09`
  in `Q95` and `0.05` in `Q0`.

**What this means.** Coordination answers the question its specification asks: do the firms act independently? Neither
firms that adapt nor firms that collude do, so the answer does not separate them. Collusion differs from adaptation in
which objective the joint behaviour pursues, joint profit or each firm's own, and in the framework's terms that is a
question about the revealed objective ([P1], [D10]), which needs the profit of each joint move, so a model of demand.
The ontology's open question, a specification that permits adaptation but charges punishment, needs the same.
