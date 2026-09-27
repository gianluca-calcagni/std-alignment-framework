---
id: "Sources index"
type: "index"
part: "sources"
updated: "2026-09-26"
---
# References

Bibliography of every source cited in the package and in [[MESSAGE_to_previous_executor]].

**The bibliography file is `references.bib`** (v7.3.2). It holds one BibTeX entry for each source note in Parts A and B:
102 entries for 101 notes, because [[src Mroueh 2024]] has both its arXiv version and its TMLR version. Each
source note names its entries in the frontmatter field `bibkey`. `lint` enforces a one-to-one match, no repeated
fields, and a `note={check …}` on every status-U entry. `sync` keeps the entries in the order of the sections
below. Part C (the census attributions) is not in the file: those are short attributions with no checked
details, and each needs a full reference before it can be cited.

In v6.1, the Part B prior-art sources are cited at their point of use in [[Core index|Core]] and
[[Dictionary index|Dictionary]]. Chernoff (1952) is used in [[Core index|Core]] Prop. [[Prop 18|18]]. Price, Robertson, Lande and Falconer &
Mackay are used in [[B11|B §11]].

**Status codes**

| Code | Meaning |
|---|---|
| **V** | bibliographic details checked against a search result in this session |
| **K** | from memory, high confidence |
| **U** | from memory; some detail (pages, article number, exact author list or year) should be checked before publication |
| **C** | cited in [[Census]] exactly as given there; carried from v5 and not checked |

"Where" gives the file and section in which the source is used. `MSG` is [[MESSAGE_to_previous_executor]].

---

## Part A — Sources cited in the v6 package files

### A.1 Mathematics used in the core

<!-- srctable:| Reference | Where | Status | -->
<!-- src:src Donsker 1975 -->
<!-- src:src Dupuis 1997 -->
<!-- src:src Csiszár 1975 -->
<!-- src:src Amari 2000 -->
<!-- src:src Hoeffding 1963 -->
<!-- src:src Popoviciu 1935 -->
<!-- src:src Pinsker 1964 -->
<!-- src:src Cover 2006 -->
<!-- src:src Bobkov 1999 -->
<!-- src:src Rockafellar 1970 -->
<!-- src:src Bregman 1967 -->
<!-- src:src Blahut 1972 -->
<!-- src:src Arimoto 1972 -->
<!-- gen:srclist -->
- [[src Donsker 1975]] — A Props 6, 7, 10; B §2 · status K
- [[src Dupuis 1997]] — A Def. 2, Thm 1 · status K
- [[src Csiszár 1975]] — A Thm 13 · status K
- [[src Amari 2000]] — A Thm 13; MSG · status K
- [[src Hoeffding 1963]] — A Prop. 7 · status K
- [[src Popoviciu 1935]] — A Prop. 2 · status U
- [[src Pinsker 1964]] — A Remark 7.1 · status K
- [[src Cover 2006]] — B7; MSG · status K
- [[src Bobkov 1999]] — A Prop. 7 (background) · status K
- [[src Rockafellar 1970]] — A Cor. 1.3; C14 · status K
- [[src Bregman 1967]] — A Thm 13 (`D_∥` as a Bregman divergence); MSG · status K
- [[src Blahut 1972]] — NOTES H2; B7 · status K
- [[src Arimoto 1972]] — NOTES H2; B7 · status K
<!-- /gen:srclist -->

### A.2 Bounded rationality, information-theoretic decision making

<!-- srctable:| Reference | Where | Status | -->
<!-- src:src Ortega 2013 -->
<!-- src:src Tishby 2011 -->
<!-- src:src Genewein 2015 -->
<!-- src:src Sims 2003 -->
<!-- src:src Stratonovich 1965 -->
<!-- src:src Stratonovich 2020 -->
<!-- src:src Train 2009 -->
<!-- gen:srclist -->
- [[src Ortega 2013]] — A Def. 2 (the actor), lineage from v5 · status V
- [[src Tishby 2011]] — B7 · status K
- [[src Genewein 2015]] — B7 · status K
- [[src Sims 2003]] — B7 · status K
- [[src Stratonovich 1965]] — B7 · status U
- [[src Stratonovich 2020]] — B7 · status K
- [[src Train 2009]] — A §9; C10 · status K
<!-- /gen:srclist -->

### A.3 Reward misspecification, Goodhart, overoptimization

<!-- srctable:| Reference | Where | Status | -->
<!-- src:src Fluri 2025 -->
<!-- src:src Kwa 2024 -->
<!-- src:src Laidlaw 2025 -->
<!-- src:src Gao 2023 -->
<!-- src:src Manheim 2018 -->
<!-- src:src Karwowski 2024 -->
<!-- src:src Beirami 2024 -->
<!-- src:src Munos 2008 -->
<!-- gen:srclist -->
- [[src Fluri 2025]] — B §2; D §2 row 44 · status V
- [[src Kwa 2024]] — A Prop. 11; B §2; C4; [[R7-5 go-no-go]] · status V
- [[src Laidlaw 2025]] — B §§2, 5 · status V
- [[src Gao 2023]] — B §4; C7, C9; [[T3 results]] · status V
- [[src Manheim 2018]] — B §3 · status K
- [[src Karwowski 2024]] — B §3 · status U
- [[src Beirami 2024]] — B §4; MSG; [[R7-5 go-no-go]] · status U (bound itself: V)
- [[src Munos 2008]] — A Prop. 10(d); B §2 · status K
<!-- /gen:srclist -->

### A.4 Economics: contracts, signalling, social choice

<!-- srctable:| Reference | Where | Status | -->
<!-- src:src Holmström 1979 -->
<!-- src:src Holmström 1991 -->
<!-- src:src Spence 1973 -->
<!-- src:src Zahavi 1975 -->
<!-- src:src Grafen 1990 -->
<!-- src:src Penn 2020 -->
<!-- src:src Számadó 2023 -->
<!-- src:src Arrow 1951 -->
<!-- src:src Gibbard 1973 -->
<!-- src:src Satterthwaite 1975 -->
<!-- gen:srclist -->
- [[src Holmström 1979]] — B §6 · status K
- [[src Holmström 1991]] — B §5 · status K
- [[src Spence 1973]] — B §8 · status K
- [[src Zahavi 1975]] — B §8 · status K
- [[src Grafen 1990]] — B §8 · status K
- [[src Penn 2020]] — B §8; D row 46 · status V
- [[src Számadó 2023]] — B §8 · status V (article number not checked)
- [[src Arrow 1951]] — C §§2.1, 3 · status K
- [[src Gibbard 1973]] — C §§2.1, 3 · status K
- [[src Satterthwaite 1975]] — C §§2.1, 3 · status K
<!-- /gen:srclist -->

### A.5 Cybernetics and control

<!-- srctable:| Reference | Where | Status | -->
<!-- src:src Ashby 1956 -->
<!-- src:src Conant 1969 -->
<!-- src:src Conant 1970 -->
<!-- src:src Touchette 2000 -->
<!-- src:src Touchette 2004 -->
<!-- src:src Francis 1976 -->
<!-- src:src Bode 1945 -->
<!-- src:src Freudenberg 1985 -->
<!-- gen:srclist -->
- [[src Ashby 1956]] — B7 · status K
- [[src Conant 1969]] — B7 · status U
- [[src Conant 1970]] — B7 · status K
- [[src Touchette 2000]] — B7 lineage; MSG · status K
- [[src Touchette 2004]] — MSG · status U
- [[src Francis 1976]] — C §5.1 · status K
- [[src Bode 1945]] — C §5.1 · status K
- [[src Freudenberg 1985]] — MSG · status K
<!-- /gen:srclist -->

### A.6 Population genetics and evolution

<!-- srctable:| Reference | Where | Status | -->
<!-- src:src Iwasa 1988 -->
<!-- src:src Sella 2005 -->
<!-- src:src Manhart 2012 -->
<!-- src:src Barton 2009 -->
<!-- src:src Wright 1931 -->
<!-- src:src Sung 2012 -->
<!-- gen:srclist -->
- [[src Iwasa 1988]] — A §9 · status U
- [[src Sella 2005]] — A §9 · status K
- [[src Manhart 2012]] — A §9 · status U
- [[src Barton 2009]] — v5 A §4.2 · status U
- [[src Wright 1931]] — v5 A §4.2 · status K
- [[src Sung 2012]] — D row 49; NOTES H5 · status U
<!-- /gen:srclist -->

### A.7 Power-seeking

<!-- srctable:| Reference | Where | Status | -->
<!-- src:src Turner 2021 -->
<!-- gen:srclist -->
- [[src Turner 2021]] — B §9 · status K
<!-- /gen:srclist -->

---

## Part B — Sources introduced in review R3 ([[MESSAGE_to_previous_executor]])

### B.1 Prior art for the v6 core

<!-- srctable:| Reference | Relation to v6 | Status | -->
<!-- src:src Korbak 2022 -->
<!-- src:src Korbak 2022 (2) -->
<!-- src:src Zhao 2024 -->
<!-- src:src Mroueh 2024 -->
<!-- src:src Huang 2025 -->
<!-- src:src El-Mhamdi 2024 -->
<!-- src:src Authors not checked 2025 -->
<!-- src:src Skalse 2024 -->
<!-- src:src Wang 2026 -->
<!-- src:src Gottwald 2019 -->
<!-- gen:srclist -->
- [[src Korbak 2022]] — KL-regularized reward maximization ≡ reverse-KL minimization toward the Gibbs policy (Thm 1) · status U (cited as "Korbak et al. 2022a, Thm 1" by a later paper: V)
- [[src Korbak 2022 (2)]] — same identity, Bayesian reading · status K
- [[src Zhao 2024]] — uses the closed form in suboptimality analysis · status V (arXiv id); author list U
- [[src Mroueh 2024]] — √KL transportation bound under sub-Gaussian tails, Rényi refinements, BoN via order statistics (Prop. 7, Prop. 10) · status V
- [[src Huang 2025]] — KL too weak; χ² regularization; single-policy concentrability (Props 10–11); [[R7-5 go-no-go]] · status V
- [[src El-Mhamdi 2024]] — weak vs strong Goodhart determined by tails of the discrepancy (A §10 item 6; B §§3–4) · status V
- [[src Authors not checked 2025]] — extends El-Mhamdi & Hoang · status V (title and id only)
- [[src Skalse 2024]] — reward distance modulo potential shaping and positive rescaling, with upper and lower worst-case regret bounds (Thm 13) · status V
- [[src Wang 2026]] — Holmström–Milgrom multitask instantiated for AI alignment (B §5) · status V
- [[src Gottwald 2019]] — cross-substrate free-energy framework for economic, artificial and biological systems · status V
<!-- /gen:srclist -->

### B.2 Suggested imports for a general framework

<!-- srctable:| Reference | Proposed role | Status | -->
<!-- src:src Koller 2003 -->
<!-- src:src Everitt 2021 -->
<!-- src:src Everitt 2021 (2) -->
<!-- src:src Hammond 2023 -->
<!-- src:src Price 1970 -->
<!-- src:src Robertson 1966 -->
<!-- src:src Lande 1979 -->
<!-- src:src Lande 1983 -->
<!-- src:src Falconer 1996 -->
<!-- src:src Chernoff 1952 -->
<!-- src:src Ben-Tal 2013 -->
<!-- src:src Namkoong 2017 -->
<!-- src:src Hubinger 2019 -->
<!-- src:src Hadfield-Menell 2016 -->
<!-- src:src Armstrong 2018 -->
<!-- src:src Abel 2021 -->
<!-- src:src Bewley 2002 -->
<!-- src:src Thaler 1981 -->
<!-- src:src Fudenberg 2006 -->
<!-- src:src Laibson 1997 -->
<!-- gen:srclist -->
- [[src Koller 2003]] — Layer-0 ontology (multi-agent) · status K
- [[src Everitt 2021]] — Layer-0 ontology; incentives read from graph structure · status K
- [[src Everitt 2021 (2)]] — frame endogeneity (X) as graph structure · status U
- [[src Hammond 2023]] — causal games; multi-agent layer · status U
- [[src Price 1970]] — Prop. 14(ii) is the Price selection term; multi-level decomposition · status K
- [[src Robertson 1966]] — Prop. 14(ii) · status U
- [[src Lande 1979]] — correlated response to selection (B4 in biology) · status K
- [[src Lande 1983]] — selection gradients; unit channel for trait-level objectives · status K
- [[src Falconer 1996]] — correlated response: selection on a proxy trait · status K
- [[src Chernoff 1952]] — detection exponents — `A_core.md` Prop. 18 (v6.1) · status K
- [[src Ben-Tal 2013]] — φ-divergence DRO: the width as a robust objective — cited at `A_core.md` Prop. 6 (v6.1) · status K
- [[src Namkoong 2017]] — χ²-DRO ≈ variance regularization — cited at `A_core.md` Prop. 6 (v6.1) · status K
- [[src Hubinger 2019]] — inner/outer alignment as a two-link chain · status K
- [[src Hadfield-Menell 2016]] — uncertainty over the intent · status K
- [[src Armstrong 2018]] — beliefs vs values non-identifiability · status K
- [[src Abel 2021]] — intents not expressible as linear functionals · status K
- [[src Bewley 2002]] — intent sets / incomplete preferences · status K
- [[src Thaler 1981]] — planner–doer: a within-person chain · status K
- [[src Fudenberg 2006]] — within-person chain · status K
- [[src Laibson 1997]] — time inconsistency (dynamic layer) · status K
<!-- /gen:srclist -->

### B.3 Sources introduced in review R4 (v6.2)

<!-- srctable:| Reference | Where | Status | -->
<!-- src:src Matějka 2015 -->
<!-- src:src Caplin 2019 -->
<!-- src:src McFadden 1974 -->
<!-- src:src Madrian 2001 -->
<!-- src:src Johnson 2003 -->
<!-- src:src McKenzie 2006 -->
<!-- src:src O'Donoghue 1999 -->
<!-- src:src Blume 1993 -->
<!-- src:src Monderer 1996 -->
<!-- src:src Rosenthal 1973 -->
<!-- src:src Koutsoupias 1999 -->
<!-- src:src McKelvey 1995 -->
<!-- gen:srclist -->
- [[src Matějka 2015]] — B7(e), B §12 · status K
- [[src Caplin 2019]] — B7(e) caveat · status U
- [[src McFadden 1974]] — B §12 · status K
- [[src Madrian 2001]] — B §12 · status K
- [[src Johnson 2003]] — B §12 · status K
- [[src McKenzie 2006]] — B §12 · status U
- [[src O'Donoghue 1999]] — B §12 · status K
- [[src Blume 1993]] — B §13 · status K
- [[src Monderer 1996]] — B §13 · status K
- [[src Rosenthal 1973]] — B §13 · status K
- [[src Koutsoupias 1999]] — B §13 · status K
- [[src McKelvey 1995]] — B §13 · status K
<!-- /gen:srclist -->

Also used in v6.2, already listed above: Sims (2003); Laibson (1997); Thaler & Shefrin (1981); Fudenberg &
Levine (2006).

### B.4 Sources introduced in the R7-5 go/no-go (v7.3.1)

<!-- srctable:| Reference | Where | Status | -->
<!-- src:src Na 2026 -->
<!-- src:src Wang 2024 -->
<!-- src:src Taylor 2016 -->
<!-- src:src Verdun 2025 -->
<!-- src:src Barlow 1972 -->
<!-- src:src Robertson 1988 -->
<!-- gen:srclist -->
- [[src Na 2026]] — [[R7-5 go-no-go]] case 2: Wasserstein as the trained actor's regularizer; KL's semantic blindness · status V
- [[src Wang 2024]] — [[R7-5 go-no-go]] case 2: f-divergence DPO; diversity versus alignment · status V
- [[src Taylor 2016]] — [[R7-5 go-no-go]] case 3: quantilizers · status K
- [[src Verdun 2025]] — [[R7-5 go-no-go]] case 3: best-of-n does not traverse the reward–KL frontier; soft best-of-n converges to the tilt · status U
- [[src Barlow 1972]] — [[R7-5 go-no-go]] case 3: isotonic regression solves the ordinal projection · status U
- [[src Robertson 1988]] — [[R7-5 go-no-go]] case 3: order-restricted inference · status K
<!-- /gen:srclist -->

Also cited there, already listed above: Kwa et al. (2024); Huang et al. (2025); Beirami et al. (2024).

---

