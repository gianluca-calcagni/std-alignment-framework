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
| **specification** | [D3] | independent pursuit ([P39]): each station pursues its own profit, independently of the other, from the default of the earlier period. Competition law's requirement that each firm determine its conduct on the market independently, read as a specification | the law, and the authority's decisions | assumed: the law's requirement read as a declared set of intended behaviours |
| **principal's resolution** | [D4] | the finest: the authority sees every reported price change of every station | the reports to the regulator | exact |
| **actor's resolution** | [D4] | each station, or its algorithm, sees the other's posted prices, which are public, and the wholesale price | the public posting of prices | approximate: what an algorithm uses is not disclosed |
| **change** | [P2] | the path of the joint behaviour after adoption, including a learning period | the prices month by month | approximate: monthly steps |
| **intervention** | [D6] | the adoption of an algorithm by one station or by both, an event that changes what the actor does; a change of the wholesale price, which adds a known cost to every outcome | adoption is detected from changes in a station's pricing, such as the frequency of its price changes | approximate: adoption is inferred, not observed, and is not a known function of the outcomes |
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
Bundeskartellamt, and the record of all price changes since mid-2014, more than 15,000 stations, is public under a
Creative Commons licence (CC BY 4.0), distributed by Tankerkönig. Assad et al. built their markets and their dating of
adoption from these data; their results have been read here only in summary, and the price data have not been read. The
simulations of Calvano et al. come with public code and data.

## 3. What the core says

- **Consequence** of [P39], [D8]: under independent pursuit, with the contexts held fixed, the misalignment of a
  duopoly's joint behaviour is the coordination of the two stations' moves plus each station's own misalignment,
  averaged over contexts. Competition law polices the first term only: how far each station departs from pursuing its
  own profit is its own affair. A common cost shock moves both stations together, so it must be a context, or it is
  counted as coordination.
- **Consequence** of [P39]: coordination depends on what counts as one outcome. A station that matches its rival's price
  an hour later shows no coordination in a table of moves within the hour, and shows it in episodes that contain the
  response. The episode length is declared before the data are read (README, rule (d)).
- **Prediction** (empirical) from [P39], [D6]: in German local duopolies, if the algorithms that both stations adopted
  learned to coordinate, the coordination of the two stations' joint price moves, within contexts and over episodes of a
  declared length, is larger after both have adopted than before, and than in duopolies where only one adopted.
  *Refuted if* it is not, beyond its sampling error computed by market. A refutation means the rise in margins came
  about without coordination in the declared moves, for example by each algorithm raising prices on its own. The data
  are public and unread; the known result is seen in summary only.
- **Reading** with [P39]: the simulated algorithms of the known result sustain high prices by punishments that unfold
  over rounds, the case of [P39](iii): coordination that a single round's table does not show.

## 4. Limits

- Coordination is not collusion. Competing stations react to each other too, and a reaction creates dependence between
  moves: the specification of independent pursuit charges every reaction, so a positive coordination says that the
  stations do not act independently, not that they agreed or colluded.
- Contexts must include every common shock. One left out, such as a regional event, is counted as coordination.
- Moves cut into three classes, and hours, see less than the record holds: grouping only hides ([P4](iv)), so the
  coordination measured is a lower bound on that of finer records.
- Adoption is inferred from the stations' pricing, not observed, and its timing is uncertain.
- Volumes and costs other than the wholesale price are unobserved, so each station's own misalignment, unlike the
  coordination, is not measured.

## 5. Open questions

- Which episode length makes coordination visible without needing more data than the record has: an hour, a day, a week?
- In the public simulations of Calvano et al., does the coordination of the algorithms show mostly over rounds rather
  than within a round, as two tit-for-tat players' does (`general/derived-spaces.md`)?
- German retail prices change several times a day. Are their paths irreversible in the sense of [P41], and did adoption
  change how irreversible they are?
