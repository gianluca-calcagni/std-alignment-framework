# References

Bibliography of every source cited in the package (v6.1) and in `MESSAGE_to_previous_executor.md`. A BibTeX
version of Parts A and B is in `references.bib`.

In v6.1, the Part B prior-art sources are cited at their point of use in `A_core.md` and
`B_dictionary.md`. Chernoff (1952) is used in `A_core.md` Prop. 18. Price, Robertson, Lande and Falconer &
Mackay are used in `B_dictionary.md` §11.

**Status codes**

| Code | Meaning |
|---|---|
| **V** | bibliographic details checked against a search result in this session |
| **K** | from memory, high confidence |
| **U** | from memory; some detail (pages, article number, exact author list or year) should be checked before publication |
| **C** | cited in `E_census.md` exactly as given there; carried from v5 and not checked |

"Where" gives the file and section in which the source is used. `MSG` is `MESSAGE_to_previous_executor.md`.

---

## Part A — Sources cited in the v6 package files

### A.1 Mathematics used in the core

| Reference | Where | Status |
|---|---|---|
| Donsker, M. D. & Varadhan, S. R. S. (1975). Asymptotic evaluation of certain Markov process expectations for large time, I. *Communications on Pure and Applied Mathematics* 28(1), 1–47. | A Props 6, 7, 10; B §2 | K |
| Dupuis, P. & Ellis, R. S. (1997). *A Weak Convergence Approach to the Theory of Large Deviations*. Wiley. — standard reference for the Gibbs variational principle | A Def. 2, Thm 1 | K |
| Csiszár, I. (1975). I-divergence geometry of probability distributions and minimization problems. *Annals of Probability* 3(1), 146–158. | A Thm 13 | K |
| Amari, S. & Nagaoka, H. (2000). *Methods of Information Geometry*. AMS / Oxford University Press. — Pythagorean relations for exponential families | A Thm 13; MSG | K |
| Hoeffding, W. (1963). Probability inequalities for sums of bounded random variables. *Journal of the American Statistical Association* 58(301), 13–30. | A Prop. 7 | K |
| Popoviciu, T. (1935). Sur les équations algébriques ayant toutes leurs racines réelles. *Mathematica (Cluj)* 9, 129–145. — the variance bound `Var ≤ osc²/4` | A Prop. 2 | U |
| Pinsker, M. S. (1964). *Information and Information Stability of Random Variables and Processes*. Holden-Day (transl. of the 1960 Russian edition). | A Remark 7.1 | K |
| Cover, T. M. & Thomas, J. A. (2006). *Elements of Information Theory*, 2nd ed. Wiley. — Fano's inequality, the grouping identity, Stein's lemma | B7; MSG | K |
| Bobkov, S. G. & Götze, F. (1999). Exponential integrability and transportation cost related to logarithmic Sobolev inequalities. *Journal of Functional Analysis* 163(1), 1–28. — transportation form of the sub-Gaussian bound | A Prop. 7 (background) | K |
| Rockafellar, R. T. (1970). *Convex Analysis*. Princeton University Press. — Fenchel–Young, Legendre transform | A Cor. 1.3; C14 | K |
| Bregman, L. M. (1967). The relaxation method of finding the common point of convex sets and its application to the solution of problems in convex programming. *USSR Computational Mathematics and Mathematical Physics* 7(3), 200–217. | A Thm 13 (`D_∥` as a Bregman divergence); MSG | K |
| Blahut, R. E. (1972). Computation of channel capacity and rate-distortion functions. *IEEE Transactions on Information Theory* 18(4), 460–473. | NOTES H2; B7 | K |
| Arimoto, S. (1972). An algorithm for computing the capacity of arbitrary discrete memoryless channels. *IEEE Transactions on Information Theory* 18(1), 14–20. | NOTES H2; B7 | K |

### A.2 Bounded rationality, information-theoretic decision making

| Reference | Where | Status |
|---|---|---|
| Ortega, P. A. & Braun, D. A. (2013). Thermodynamics as a theory of decision-making with information-processing costs. *Proceedings of the Royal Society A* 469, 20120683. | A Def. 2 (the actor), lineage from v5 | V |
| Tishby, N. & Polani, D. (2011). Information theory of decisions and actions. In Cutsuridis et al. (eds.), *Perception-Action Cycle*, pp. 601–636. Springer. | B7 | K |
| Genewein, T., Leibfried, F., Grau-Moya, J. & Braun, D. A. (2015). Bounded rationality, abstraction, and hierarchical decision-making: an information-theoretic optimality principle. *Frontiers in Robotics and AI* 2, 27. | B7 | K |
| Sims, C. A. (2003). Implications of rational inattention. *Journal of Monetary Economics* 50(3), 665–690. | B7 | K |
| Stratonovich, R. L. (1965). On value of information. *Izvestiya of USSR Academy of Sciences, Technical Cybernetics* 5 (in Russian). | B7 | U |
| Stratonovich, R. L. (2020). *Theory of Information and its Value* (R. V. Belavkin, P. M. Pardalos & J. C. Principe, eds.). Springer. | B7 | K |
| Train, K. E. (2009). *Discrete Choice Methods with Simulation*, 2nd ed. Cambridge University Press. — scale normalization in logit models | A §9; C10 | K |

### A.3 Reward misspecification, Goodhart, overoptimization

| Reference | Where | Status |
|---|---|---|
| Fluri, L., Lang, L., Abate, A., Forré, P., Krueger, D. & Skalse, J. (2025). The perils of optimizing learned reward functions: low training error does not guarantee low regret. *Proceedings of ICML 2025*, PMLR 267, 17306–17377. arXiv:2406.15753. | B §2; D §2 row 44 | V |
| Kwa, T., Thomas, D. & Garriga-Alonso, A. (2024). Catastrophic Goodhart: regularizing RLHF with KL divergence does not mitigate heavy-tailed reward misspecification. *NeurIPS 2024*. arXiv:2407.14503. | A Prop. 11; B §2; C4 | V |
| Laidlaw, C., Singhal, S. & Dragan, A. (2025). Correlated proxies: a new definition and improved mitigation for reward hacking. *ICLR 2025*. arXiv:2403.03185. | B §§2, 5 | V |
| Gao, L., Schulman, J. & Hilton, J. (2023). Scaling laws for reward model overoptimization. *Proceedings of ICML 2023*, PMLR 202, 10835–10866. arXiv:2210.10760. | B §4; C7, C9 | V |
| Manheim, D. & Garrabrant, S. (2018). Categorizing variants of Goodhart's law. arXiv:1803.04585. | B §3 | K |
| Karwowski, J., Hayman, O., Bai, X., Kiendlhofer, K., Griffin, C. & Skalse, J. (2024). Goodhart's law in reinforcement learning. *ICLR 2024*. arXiv:2310.09144. | B §3 | U |
| Beirami, A., Agarwal, A., Berant, J., D'Amour, A., Eisenstein, J., Nagpal, C. & Suresh, A. T. (2024). Theoretical guarantees on the best-of-n alignment policy. arXiv:2401.01879. — the BoN KL expression is an upper bound | B §4; MSG | U (bound itself: V) |
| Munos, R. & Szepesvári, C. (2008). Finite-time bounds for fitted value iteration. *Journal of Machine Learning Research* 9, 815–857. — concentrability coefficients | A Prop. 10(d); B §2 | K |

### A.4 Economics: contracts, signalling, social choice

| Reference | Where | Status |
|---|---|---|
| Holmström, B. (1979). Moral hazard and observability. *Bell Journal of Economics* 10(1), 74–91. | B §6 | K |
| Holmström, B. & Milgrom, P. (1991). Multitask principal–agent analyses: incentive contracts, asset ownership, and job design. *Journal of Law, Economics, and Organization* 7 (special issue), 24–52. | B §5 | K |
| Spence, M. (1973). Job market signaling. *Quarterly Journal of Economics* 87(3), 355–374. — single-crossing | B §8 | K |
| Zahavi, A. (1975). Mate selection — a selection for a handicap. *Journal of Theoretical Biology* 53(1), 205–214. | B §8 | K |
| Grafen, A. (1990). Biological signals as handicaps. *Journal of Theoretical Biology* 144(4), 517–546. | B §8 | K |
| Penn, D. J. & Számadó, S. (2020). The handicap principle: how an erroneous hypothesis became a scientific principle. *Biological Reviews* 95(1), 267–290. doi:10.1111/brv.12563. | B §8; D row 46 | V |
| Számadó, S., Zachar, I., Czégel, D. & Penn, D. J. (2023). Honesty in signalling games is maintained by trade-offs rather than costs. *BMC Biology* 21. | B §8 | V (article number not checked) |
| Arrow, K. J. (1951). *Social Choice and Individual Values*. Wiley. | C §§2.1, 3 | K |
| Gibbard, A. (1973). Manipulation of voting schemes: a general result. *Econometrica* 41(4), 587–601. | C §§2.1, 3 | K |
| Satterthwaite, M. A. (1975). Strategy-proofness and Arrow's conditions. *Journal of Economic Theory* 10(2), 187–217. | C §§2.1, 3 | K |

### A.5 Cybernetics and control

| Reference | Where | Status |
|---|---|---|
| Ashby, W. R. (1956). *An Introduction to Cybernetics*. Chapman & Hall. | B7 | K |
| Conant, R. C. (1969). The information transfer required in regulatory processes. *IEEE Transactions on Systems Science and Cybernetics* 5(4), 334–338. | B7 | U |
| Conant, R. C. & Ashby, W. R. (1970). Every good regulator of a system must be a model of that system. *International Journal of Systems Science* 1(2), 89–97. | B7 | K |
| Touchette, H. & Lloyd, S. (2000). Information-theoretic limits of control. *Physical Review Letters* 84(6), 1156–1159. | B7 lineage; MSG | K |
| Touchette, H. & Lloyd, S. (2004). Information-theoretic approach to the study of control systems. *Physica A* 331(1–2), 140–172. | MSG | U |
| Francis, B. A. & Wonham, W. M. (1976). The internal model principle of control theory. *Automatica* 12(5), 457–465. | C §5.1 | K |
| Bode, H. W. (1945). *Network Analysis and Feedback Amplifier Design*. Van Nostrand. | C §5.1 | K |
| Freudenberg, J. S. & Looze, D. P. (1985). Right half plane poles and zeros and design tradeoffs in feedback systems. *IEEE Transactions on Automatic Control* 30(6), 555–565. — for checking Bode's integral on the delayed loop | MSG | K |

### A.6 Population genetics and evolution

| Reference | Where | Status |
|---|---|---|
| Iwasa, Y. (1988). Free fitness that always increases in evolution. *Journal of Theoretical Biology* 135(3), 265–281. | A §9 | U |
| Sella, G. & Hirsh, A. E. (2005). The application of statistical physics to evolutionary biology. *PNAS* 102(27), 9541–9546. | A §9 | K |
| Manhart, M., Haldane, A. & Morozov, A. V. (2012). A universal scaling law determines time reversibility and steady state of substitutions under selection. *Theoretical Population Biology* 82(1), 66–76. — author list corrected in v6.1 (v6 had "Manhart & Morozov") | A §9 | U |
| Barton, N. H. & Coe, J. B. (2009). On the application of statistical physics to evolutionary biology. *Journal of Theoretical Biology* 259(2), 317–324. — cited in v5, dropped in v6 | v5 A §4.2 | U |
| Wright, S. (1931). Evolution in Mendelian populations. *Genetics* 16(2), 97–159. — cited in v5 | v5 A §4.2 | K |
| Sung, W., Ackerman, M. S., Miller, S. F., Doak, T. G. & Lynch, M. (2012). Drift-barrier hypothesis and mutation-rate evolution. *PNAS* 109(45), 18488–18492. | D row 49; NOTES H5 | U |

### A.7 Power-seeking

| Reference | Where | Status |
|---|---|---|
| Turner, A. M., Smith, L., Shah, R., Critch, A. & Tadepalli, P. (2021). Optimal policies tend to seek power. *NeurIPS 2021*. | B §9 | K |

---

## Part B — Sources introduced in review R3 (`MESSAGE_to_previous_executor.md`)

### B.1 Prior art for the v6 core

| Reference | Relation to v6 | Status |
|---|---|---|
| Korbak, T., Elsahar, H., Kruszewski, G. & Dymetman, M. (2022). On reinforcement learning and distribution matching for fine-tuning language models with no catastrophic forgetting. *NeurIPS 2022*. | KL-regularized reward maximization ≡ reverse-KL minimization toward the Gibbs policy (Thm 1) | U (cited as "Korbak et al. 2022a, Thm 1" by a later paper: V) |
| Korbak, T., Perez, E. & Buckley, C. L. (2022). RL with KL penalties is better viewed as Bayesian inference. *Findings of EMNLP 2022*. | same identity, Bayesian reading | K |
| Zhao, H., Ye, C., Gu, Q. & Zhang, T. (2024). Sharp analysis for KL-regularized contextual bandits and RLHF. arXiv:2411.04625. | uses the closed form in suboptimality analysis | V (arXiv id); author list U |
| Mroueh, Y. (2024). Information theoretic guarantees for policy alignment in large language models. arXiv:2406.05883. Published as Mroueh, Y. & Nitsure, A. (2025), *Transactions on Machine Learning Research*. | √KL transportation bound under sub-Gaussian tails, Rényi refinements, BoN via order statistics (Prop. 7, Prop. 10) | V |
| Huang, A., Zhan, W., Xie, T., Lee, J. D., Sun, W., Krishnamurthy, A. & Foster, D. J. (2025). Correcting the mythos of KL-regularization: direct alignment without overoptimization via chi-squared preference optimization. *ICLR 2025*. arXiv:2407.13399. | KL too weak; χ² regularization; single-policy concentrability (Props 10–11) | V |
| El-Mhamdi, E.-M. & Hoang, L.-N. (2024). On Goodhart's law, with an application to value alignment. arXiv:2410.09638. | weak vs strong Goodhart determined by tails of the discrepancy (A §10 item 6; B §§3–4) | V |
| *Authors not checked* (2025). The strong, weak and benign Goodhart's law: an independence-free and paradigm-agnostic formalisation. arXiv:2505.23445. | extends El-Mhamdi & Hoang | V (title and id only) |
| Skalse, J., Farnik, L., Motwani, S. R., Jenner, E., Gleave, A. & Abate, A. (2024). STARC: a general framework for quantifying differences between reward functions. *ICLR 2024*. arXiv:2309.15257. | reward distance modulo potential shaping and positive rescaling, with upper and lower worst-case regret bounds (Thm 13) | V |
| Wang, J. & Huang, J. (2026). Reward hacking as equilibrium under finite evaluation. arXiv:2603.28063. | Holmström–Milgrom multitask instantiated for AI alignment (B §5) | V |
| Gottwald, S. & Braun, D. A. (2019). Systems of bounded rational agents with information-theoretic constraints. *Neural Computation* 31(2), 440–476. arXiv:1809.05897. | cross-substrate free-energy framework for economic, artificial and biological systems | V |

### B.2 Suggested imports for a general framework

| Reference | Proposed role | Status |
|---|---|---|
| Koller, D. & Milch, B. (2003). Multi-agent influence diagrams for representing and solving games. *Games and Economic Behavior* 45(1), 181–221. | Layer-0 ontology (multi-agent) | K |
| Everitt, T., Carey, R., Langlois, E. D., Ortega, P. A. & Legg, S. (2021). Agent incentives: a causal perspective. *AAAI 2021*. | Layer-0 ontology; incentives read from graph structure | K |
| Everitt, T., Hutter, M., Kumar, R. & Krakovna, V. (2021). Reward tampering problems and solutions in reinforcement learning: a causal influence diagram perspective. *Synthese* 198 (Suppl. 27), 6435–6467. | frame endogeneity (X) as graph structure | U |
| Hammond, L., Fox, J., Everitt, T., Carey, R., Abate, A. & Wooldridge, M. (2023). Reasoning about causality in games. *Artificial Intelligence* 320, 103919. | causal games; multi-agent layer | U |
| Price, G. R. (1970). Selection and covariance. *Nature* 227, 520–521. | Prop. 14(ii) is the Price selection term; multi-level decomposition | K |
| Robertson, A. (1966). A mathematical model of the culling process in dairy cattle. *Animal Production* 8, 95–108. — the "secondary theorem of natural selection" | Prop. 14(ii) | U |
| Lande, R. (1979). Quantitative genetic analysis of multivariate evolution, applied to brain:body size allometry. *Evolution* 33(1), 402–416. | correlated response to selection (B4 in biology) | K |
| Lande, R. & Arnold, S. J. (1983). The measurement of selection on correlated characters. *Evolution* 37(6), 1210–1226. | selection gradients; unit channel for trait-level objectives | K |
| Falconer, D. S. & Mackay, T. F. C. (1996). *Introduction to Quantitative Genetics*, 4th ed. Longman. | correlated response: selection on a proxy trait | K |
| Chernoff, H. (1952). A measure of asymptotic efficiency for tests of a hypothesis based on the sum of observations. *Annals of Mathematical Statistics* 23(4), 493–507. | detection exponents — `A_core.md` Prop. 18 (v6.1) | K |
| Ben-Tal, A., den Hertog, D., De Waegenaere, A., Melenberg, B. & Rennen, G. (2013). Robust solutions of optimization problems affected by uncertain probabilities. *Management Science* 59(2), 341–357. | φ-divergence DRO: the width as a robust objective — cited at `A_core.md` Prop. 6 (v6.1) | K |
| Namkoong, H. & Duchi, J. C. (2017). Variance-based regularization with convex objectives. *NeurIPS 2017*. | χ²-DRO ≈ variance regularization — cited at `A_core.md` Prop. 6 (v6.1) | K |
| Hubinger, E., van Merwijk, C., Mikulik, V., Skalse, J. & Garrabrant, S. (2019). Risks from learned optimization in advanced machine learning systems. arXiv:1906.01820. | inner/outer alignment as a two-link chain | K |
| Hadfield-Menell, D., Dragan, A., Abbeel, P. & Russell, S. (2016). Cooperative inverse reinforcement learning. *NeurIPS 2016*. | uncertainty over the intent | K |
| Armstrong, S. & Mindermann, S. (2018). Occam's razor is insufficient to infer the preferences of irrational agents. *NeurIPS 2018*. | beliefs vs values non-identifiability | K |
| Abel, D., Dabney, W., Harutyunyan, A., Ho, M. K., Littman, M. L., Precup, D. & Singh, S. (2021). On the expressivity of Markov reward. *NeurIPS 2021*. | intents not expressible as linear functionals | K |
| Bewley, T. F. (2002). Knightian decision theory. Part I. *Decisions in Economics and Finance* 25(2), 79–110. | intent sets / incomplete preferences | K |
| Thaler, R. H. & Shefrin, H. M. (1981). An economic theory of self-control. *Journal of Political Economy* 89(2), 392–406. | planner–doer: a within-person chain | K |
| Fudenberg, D. & Levine, D. K. (2006). A dual-self model of impulse control. *American Economic Review* 96(5), 1449–1476. | within-person chain | K |
| Laibson, D. (1997). Golden eggs and hyperbolic discounting. *Quarterly Journal of Economics* 112(2), 443–477. | time inconsistency (dynamic layer) | K |

### B.3 Sources introduced in review R4 (v6.2)

| Reference | Where | Status |
|---|---|---|
| Matějka, F. & McKay, A. (2015). Rational inattention to discrete choices: a new foundation for the multinomial logit model. *American Economic Review* 105(1), 272–298. | B7(e), B §12 | K |
| Caplin, A., Dean, M. & Leahy, J. (2019). Rational inattention, optimal consideration sets, and stochastic choice. *Review of Economic Studies* 86(3), 1061–1094. | B7(e) caveat | U |
| McFadden, D. (1974). Conditional logit analysis of qualitative choice behavior. In P. Zarembka (ed.), *Frontiers in Econometrics*, pp. 105–142. Academic Press. | B §12 | K |
| Madrian, B. C. & Shea, D. F. (2001). The power of suggestion: inertia in 401(k) participation and savings behavior. *Quarterly Journal of Economics* 116(4), 1149–1187. | B §12 | K |
| Johnson, E. J. & Goldstein, D. (2003). Do defaults save lives? *Science* 302(5649), 1338–1339. | B §12 | K |
| McKenzie, C. R. M., Liersch, M. J. & Finkelstein, S. R. (2006). Recommendations implicit in policy defaults. *Psychological Science* 17(5), 414–420. | B §12 | U |
| O'Donoghue, T. & Rabin, M. (1999). Doing it now or later. *American Economic Review* 89(1), 103–124. | B §12 | K |
| Blume, L. E. (1993). The statistical mechanics of strategic interaction. *Games and Economic Behavior* 5(3), 387–424. | B §13 | K |
| Monderer, D. & Shapley, L. S. (1996). Potential games. *Games and Economic Behavior* 14(1), 124–143. | B §13 | K |
| Rosenthal, R. W. (1973). A class of games possessing pure-strategy Nash equilibria. *International Journal of Game Theory* 2(1), 65–67. | B §13 | K |
| Koutsoupias, E. & Papadimitriou, C. (1999). Worst-case equilibria. *Proceedings of STACS 1999*, LNCS 1563, pp. 404–413. | B §13 | K |
| McKelvey, R. D. & Palfrey, T. R. (1995). Quantal response equilibria for normal form games. *Games and Economic Behavior* 10(1), 6–38. | B §13 | K |

Also used in v6.2, already listed above: Sims (2003); Laibson (1997); Thaler & Shefrin (1981); Fudenberg &
Levine (2006).

---

## Part C — Sources as cited in `E_census.md` (status C)

The census gives short attributions only. They are reproduced exactly, with the census items that use
them. None were checked in v5, v6 or R3. Before the census is used as a test set in a publication, every
row in C.1 needs a full reference. Every row in C.2 needs either a citable source or an explicit
"practitioner observation" label.

### C.1 Named sources

| Source as cited | Census items |
|---|---|
| *Toxoplasma*, *Ophiocordyceps* | J13 |
| Abdelnabi & Salem 2025 | D9 |
| Abel et al. 2021 | A10, L1 |
| Ainslie | H2, H23 |
| Akerlof 1970 | I3 |
| Alchian & Demsetz | I20 |
| Amodei et al. 2016 | A2, A6, A12, A15, C7, F1 |
| Aristotle | H1 |
| Armstrong & Mindermann 2018 | L13 |
| Armstrong et al. 2016 | G6 |
| Arrow | I2 |
| Arrow 1951 | I16, L8 |
| Baek et al. 2026 | D10 |
| Bai et al. 2022 | E13 |
| Belyaev | J14 |
| Betley et al. 2025 | B10 |
| Bikhchandani et al. | I24 |
| Bolukbasi et al. | F5 |
| Bostrom | G7 |
| Bostrom 2012 | D1 |
| Bowling et al. 2023 | A11, L2 |
| Brickman & Campbell | H6 |
| Burns et al. 2023 | F7 |
| Burt & Trivers 2006 | K1, K3 |
| Buss | K13 |
| Calvano et al. 2020 | G3 |
| Campbell 1979 | I5 |
| Carroll et al. | G4 |
| Chapman et al. | J10 |
| Christiano et al. 2021 | F2 |
| Condorcet | I17 |
| CoT-faithfulness line | D17 |
| D'Amour et al. 2020 | C4 |
| Davidson | H1 |
| Davies | J6 |
| Dawkins | K14 |
| de Blanc | C5 |
| Elster 1983 | H17 |
| Endler | J9 |
| Everitt et al. | A3, L5 |
| Farquhar, Carey & Everitt | L6 |
| Fisher | J20 |
| Fronsdal et al. 2026 | F11 |
| Gao, Schulman & Hilton 2022 | E1 |
| Geirhos et al. 2020 | C3 |
| Gibbard 1973 | I18, L9 |
| Gilbert & Wilson | H7 |
| Gneezy & Rustichini 2000 | I29 |
| Goodhart 1975 | I4 |
| Greenblatt et al. 2024 | B4 |
| Hadfield-Menell et al. 2017 | D4, L15 |
| Haig 2000 | K6 |
| Hamilton | J17, K14 |
| Hamilton's rule | J17 |
| Hardin 1968 | I14 |
| Holmström | I2 |
| Holmström & Milgrom 1991 | I7 |
| Hubinger et al. 2019 | B1, B2, B3 |
| Irving et al. 2018 | F8 |
| Janis 1972 | I23 |
| Jensen & Meckling 1976 | I1 |
| Johansson et al. 2005 | H9 |
| Kirk et al. 2026 | D13 |
| Koch et al. | B9 |
| Krakovna et al. | A13 |
| Krakovna et al. 2020 | A1, A16 |
| Krueger et al. | C8, G4 |
| Kulveit et al. 2025 | G8 |
| Kunda 1990 | H13 |
| Laibson | H2 |
| Laidlaw et al. | A8 |
| Laine et al. 2024 | D7, D8 |
| Langosco et al. | B9 |
| Langosco et al. 2022 | C1, C2 |
| Lanham et al. 2023 | D18 |
| Leike et al. 2018 | F9 |
| Lichtenstein & Slovic | H11 |
| Lipsky 1980 | I28 |
| MacDiarmid et al. 2025 | B12, D14 |
| Manheim & Garrabrant 2018 | I6, L10 |
| Marks et al. 2025 | F3 |
| McClintock | K4 |
| McKenzie et al. 2023 | C10 |
| Medawar | J19 |
| Meinke et al. 2024 | B5, D11, D12 |
| Merton | I10 |
| Merton 1940 | I8 |
| Monin & Miller | H24 |
| Muller 2018 | I12 |
| Needham et al. 2025 | D7 |
| Ng & Russell | L12 |
| Ng, Harada & Russell 1999 | A9 |
| Nisbett & Wilson 1977 | H8 |
| O'Donoghue & Rabin | H22 |
| Olson 1965 | I15 |
| Omohundro 2008 | D1 |
| Ord | G7 |
| Orseau & Armstrong 2016 | D5 |
| Paul 2014 | H16 |
| Perez et al. 2022 | E2 |
| Power 1997 | I27 |
| Rice 1953 | L14 |
| Richens & Everitt 2024 | L7 |
| Ring & Orseau 2011 | A4, A5 |
| Ryan | J9 |
| Schelling | H23 |
| Seligman | H21 |
| Shah et al. 2022 | C1 |
| Sharma et al. 2023 | E2, E5 |
| Skalse et al. | L12 |
| Skalse et al. 2022 | A7, L3 |
| Slovic 1995 | H10 |
| Soares et al. 2015 | D3 |
| Stigler 1971 | I9 |
| Strotz 1955 | H3, L11 |
| Taylor et al. 2025 | B11 |
| Tice et al. 2026 | D16 |
| Tinbergen | J1 |
| Trivers | H14 |
| Trivers 1974 | J11 |
| Tullock | I19 |
| Turner et al. 2021 | D2, L4 |
| Turpin et al. 2023 | D18 |
| Tversky & Kahneman | H12 |
| van der Weij et al. | D6 |
| Werren | K9 |
| Werren et al. 1988 | K2 |
| Williams | J19 |

### C.2 Items attributed to a literature, a practice or a descriptor rather than a citable work

| Attribution as given | Census items |
|---|---|
| 2025 auditing games | D6, F12 |
| 2025 literature | B6, E15 |
| 2025 monitoring literature | D15 |
| 2025 red-team work | F10 |
| 2026 empirical work | E12 |
| 2026 mitigation work | E17 |
| 2026 RLHF taxonomies | E9, E10, E11 |
| ageing biology | K11 |
| anecdotal but canonical | I13 |
| applied | H25 |
| applied evolution | J16 |
| behavioural ecology | J7, J8, J12 |
| by analogy, widely used | I21 |
| clinical | H4 |
| common-agency literature | I30 |
| conflict/speciation reviews | K15 |
| contested, replication issues | H20 |
| corporate governance | I22 |
| CoT literature | F4 |
| cuckoo literature | J6 |
| cytogenetics | K5 |
| deployment reality | G10 |
| documented incidents | A19 |
| education literature | I11 |
| ELK literature | C11 |
| evolutionary medicine | J2 |
| fox experiment | J14 |
| habit literature | H19 |
| immunology | K12 |
| inner-alignment literature | B8 |
| livestock genetics | J15 |
| MIRI | C6 |
| MIRI line | C5 |
| mismatch literature | J3, J4 |
| MONA line of work | A18 |
| multi-agent RL | G1, G2 |
| multicellularity literature | K10 |
| organelle genetics | K8 |
| organisational theory | I25 |
| pharmacology | H5, J5 |
| philosophical literature | H15 |
| pipeline folklore | A14 |
| plant genetics | K7 |
| policy | I26 |
| PPO/KL practice | E8 |
| practice | E14, E16 |
| psychology | H18 |
| recent, 2026 | A17 |
| reciprocity literature | J18 |
| reward-hacking benchmarks, 2026 | A20 |
| RLHF folklore, measured | E7 |
| speculative, alignment forum | B7 |
| systemic-risk literature | G9 |
| this and related work | E6 |
| widely documented | F6, G5 |
| widely measured | E3, E4 |
| widely observed | C9 |
