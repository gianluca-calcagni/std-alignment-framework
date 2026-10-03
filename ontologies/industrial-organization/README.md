# Ontology — industrial organization: pricing algorithms and competition

Competition law asks firms to set their conduct on the market independently. The competition authority is the principal;
the firms of a local market, taken together, are the actor, since the core reads a group as one actor on joint outcomes
([P39]). What the authority polices is not how each firm pursues its profit, but whether the firms coordinate: in the
core's terms, the coordination of their joint behaviour under the specification of independent pursuit. Pricing
algorithms make the question numerical. German petrol stations must report every price change to the regulator as it
happens, and the record is public. Two known results are reframed: algorithms that learn to sustain high prices in
simulations, and margins that rose in German duopolies once both stations had adopted algorithms.

## 1. Slots

| Slot | Core | In this discipline | Observed as | Fit |
|---|---|---|---|---|
| **outcomes** | [D1] | for one local duopoly, the pair of the two stations' price moves in an hour, each cut into down, none or up; an episode of several hours is one outcome on the pairs of sequences | the reported price changes of each station | approximate: prices and time are cut into classes |
| **contexts** | [D8] | the hour of the day, the day of the week, and the change of the wholesale price: fixed before the stations act, and shared by both | the time stamps; published wholesale and crude oil prices | approximate: a common cost shock makes the two stations move together without coordinating, so it must be a context |
| **behaviour** | [D1] | the frequencies of the joint moves, per market and period, before and after adoption | the reported price changes | exact as frequencies |
| **sample** | [D11] | one episode of one market | the reported price changes | approximate: successive days of one market depend on each other, and markets share regional shocks, so error bars are computed by market |
| **default** | [D2] | the joint behaviour of the same market before any station adopted an algorithm, or in comparable markets where neither did | the price changes of the earlier period, or of the comparison markets | assumed: the comparison must be declared before the outcomes are read |
| **objective** | [D2] | each station's profit, its margin times its volume, which competition law means each to pursue on its own | margins over the wholesale price; volumes are not reported | assumed: volumes and costs other than the wholesale price are not observed |
| **evaluator** | [D10] | the objective an algorithm is set to pursue; the vendors' algorithms are not public, so it is known only as revealed by behaviour ([P1]) | the stations' price changes | assumed: revealed, not declared |
| **intensity** | [D2] | how strongly a station's prices respond to what it pursues: the settings of its algorithm, its staff's attention | not apart from the objective | approximate |
| **specification** | [D3] | independent pursuit ([P39]): each station pursues its own profit, independently of the other, from the default of the earlier period, given the contexts of this table and no others. Competition law's requirement that each firm determine its conduct on the market independently, read as a specification, in its stricter form: the one that papers and the public record can test (section 4) | the law, and the authority's decisions | assumed: stricter than the law, which lets a firm adapt to its rivals' observed conduct |
| **principal's resolution** | [D4] | the finest: the authority sees every reported price change of every station | the reports to the regulator | exact |
| **actor's resolution** | [D4] | each station, or its algorithm, sees the other's posted prices, which are public, and the wholesale price | the public posting of prices | approximate: what an algorithm uses is not disclosed |
| **change** | [P2] | the path of the joint behaviour after adoption, including a learning period | the prices month by month | approximate: monthly steps |
| **intervention** | [D6] | the adoption of an algorithm by one station or by both, an event that changes what the actor does; a change of the wholesale price, which adds a known cost to every outcome | structural breaks in a station's own pricing, dated as in the Data paragraph | approximate: adoption is inferred, not observed, and is not a known function of the outcomes |
| **stakes** | [D5] | cents per litre of margin, and what consumers pay | prices and wholesale prices | exact, given the objective |

## 2. Known result

Calvano, Calzolari, Denicolò and Pastorello let reinforcement-learning algorithms set prices against each other in
simulated markets [@calvano2020]. The algorithms learned to charge prices above the competitive level and to sustain
them by punishing a deviation with a temporary price war, without communicating and without being designed to collude.

Assad, Clark, Ershov and Xu studied the adoption of algorithmic pricing by German petrol stations around 2017
[@assad2024]. In local duopolies, margins rose by 28% when both stations had adopted, and not when only one had; in
local monopolies, adoption changed nothing. Margins began to rise about a year after both stations had adopted, which
the authors read as the algorithms learning to soften competition.

**Data.** Every German petrol station reports every price change to the Markttransparenzstelle für Kraftstoffe of the
Bundeskartellamt. Tankerkönig distributes the record of all price changes since June 2014, for about 15,000 stations,
under a Creative Commons licence: by secondary sources, CC BY-NC-SA 4.0 for the archive, so for non-commercial use, and
CC BY 4.0 for the live feed; the primary pages could not be reached from here. Assad et al. built their markets from
these data, for 2016 to 2018, and dated adoption by structural breaks in four markers of a station's pricing: the number
of its daily price changes, the speed of its response to its rivals' changes, its response to crude oil prices, and its
response to local weather; a station adopted when two markers broke within four weeks [@assad2024]. Their replication
package is listed on Harvard Dataverse; whether it holds the adoption dates has not been checked. Their results have
been read here only in summary, and the price data have not been read. Whether the code of Calvano et al. is public has
not been checked.

## 3. What the core says

- **Consequence** of [P39], [D8]: under independent pursuit, with the contexts held fixed, the misalignment of a
  duopoly's joint behaviour is the coordination of the two stations' moves plus each station's own misalignment,
  averaged over contexts. Competition law polices the first term only: how far each station departs from pursuing its
  own profit is its own affair. A common cost shock moves both stations together, so it must be a context, or it is
  counted as coordination.
- **Consequence** of [P39]: coordination depends on what counts as one outcome. A station that matches its rival's price
  an hour later shows no coordination in a table of moves within the hour, and shows it in episodes that contain the
  response. The episode length is declared before the data are read (README, rule (d)).
- **Consequence** of [P39], [D8]: under the specification that takes the rival's past prices as contexts, the simulated
  algorithms of the known result show no coordination at all. In the paper's baseline, each sets its price from the last
  round's prices alone, exploring independently of the other, so given those prices their moves are independent,
  punishments included. Their coordination lies between a deviation and its punishment, in time, and only a
  specification that does not take past prices as contexts can see it, and only when deviations occur (section 4). Case
  C1 found it so in every session (`cases/c1-collusion-simulation/`, S3).
- **Prediction** (empirical) from [P39], [D6]: in German local duopolies, the coordination of the two stations' joint
  price moves, within contexts and over episodes of a declared length, is larger where both stations have adopted
  pricing algorithms than where only one has, over the same calendar periods. Adoption is dated without the speed of
  response to the rival, the one marker that measures a dependence between the two stations. *Refuted if* it is not,
  beyond its sampling error computed by market. In simulation the comparison holds for learning algorithms whether or
  not they collude (`cases/c1-collusion-simulation/`), so a held prediction says that both stations' algorithms react to
  each other, not that they collude. Revised before any data were read: the comparison with the period before adoption
  was dropped, because in the same case players who only adapt coordinated almost as much as algorithms that collude.
  The data are public for non-commercial use and unread; the known result is seen in summary only.
- **Reading** with [P39]: the simulated algorithms of the known result sustain high prices by punishments that unfold
  over rounds, the case of [P39](iii): coordination that a single round's table does not show. Case C1 found it in 21 of
  24 simulated markets, against 22 predicted (S2, failed).

## 4. Limits

- Coordination is not collusion. Competing stations react to each other too, and a reaction creates dependence between
  moves: independent pursuit charges every reaction. Competition law is generally read as letting a firm adapt to its
  rivals' observed conduct, so this specification is stricter than the law. It is declared because it is the one that
  can be tested: taking the rival's past prices as contexts would permit that adaptation, but it would need a declared
  model of what each station observes, and it is blind by construction to the known result's algorithms (section 3). So
  a positive coordination says that the stations do not act independently, not that they agreed, colluded or broke the
  law; the prediction compares before with after, where lawful adaptation is present on both sides.
- Coordination does not detect collusion. In simulation, learning algorithms that barely collude coordinate as much as
  algorithms that do, and players who only adapt almost as much (case C1). Collusion differs in the objective the joint
  behaviour pursues, the two firms' joint profit rather than each one's own, and reading that objective ([P1], [D10])
  needs the profit of each joint move: a model of demand, which the public record does not give.
- A collusive steady state shows no coordination. Two stations that hold a high price and never deviate have a joint
  behaviour that is a point mass, and a point mass is independent. Coordination shows only in how the stations respond
  to shocks and to each other's moves; the record has many, in the wholesale price and in the daily cycle of prices, but
  a market that never moves says nothing.
- Contexts must include every common shock. One left out, such as a regional event, is counted as coordination.
- Moves cut into three classes, and hours, see less than the record holds: grouping only hides ([P4](iv)), so the
  coordination measured is a lower bound on that of finer records.
- Adoption is inferred from the stations' pricing, not observed, and its timing is uncertain. One of Assad et al.'s
  markers, the speed of response to the rival, is itself a dependence between the stations: adoption dated with it would
  make a rise in coordination partly true by construction, so the prediction dates adoption without it, and its dates
  are not those of the known result.
- Volumes and costs other than the wholesale price are unobserved, so each station's own misalignment, unlike the
  coordination, is not measured.

## 5. Open questions

- Which episode length makes coordination visible without needing more data than the record has: an hour, a day, a week?
- Is there a specification between the two of sections 3 and 4, one that permits adaptation to a rival's prices but
  charges a reaction that punishes a price cut, and can it be declared without a model of the firms' profits? Case C1
  suggests not without a model of demand: what separates collusion from adaptation is which profit the moves pursue.
- In simulations like those of Calvano et al., rerun with their exploration, does the coordination of the algorithms
  show mostly over rounds rather than within a round, as two tit-for-tat players' does (`general/derived-spaces.md`)?
- German retail prices change several times a day. Are their paths irreversible in the sense of [P41], and did adoption
  change how irreversible they are?
