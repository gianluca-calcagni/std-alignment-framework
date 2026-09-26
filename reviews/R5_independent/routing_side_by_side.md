# Blind re-routing of the 221-item census vs the v6.2 routing

Mine was frozen (sha256 388f5a70…) before `T1_census_routing.md` and `t1/` were opened. `Pt` = snapshot only under the lenient reading (projection collapses to generic proxy error); strict reading treats it as N.

| id | prev expr | prev layer | mine expr | mine layer | agree? | my note |
|---|---|---|---|---|---|---|
| A1 | F | static | F | static |  | argmax-agreement (P14iii), P20 covariance |
| A2 | F | static | F | static |  | exogenous-measurement exploitation = evaluator error; tampering part is A3 |
| A3 | P | outside-X | Pt | outside-X |  | acts on F-hat as a function; static projection = generic spike error |
| A4 | P | outside-X | Pt | outside-X |  | as A3 |
| A5 | P | outside-X | Pt | outside-X |  | acts on observation channel of evaluator |
| A6 | F | static | F | static |  | canonical E |
| A7 | F | static | F | static |  | Cor13.1: D_perp=0 iff positive-affine = unhackability over full simplex |
| A8 | F | static | F | static |  | B5: Laidlaw proxy = Cov_q>0 first-order |
| A9 | F | static | F | static |  | potential shaping = gauge g2 on trajectory X (terminal-potential caveat) |
| A10 | F | static | P | undetermined | ≠ | trajectory-functional goals fine (F not Markov); policy-ordering goals lack a target form |
| A11 | P | outside-E | P | undetermined |  | core target class = vNM positive-affine (+concave P15); Markov-ness irrelevant to core |
| A12 | F | static | F | static |  | B5 multitask split F=F_m+F_u; impact reg = KL to q |
| A13 | F | static | F | static |  | vacuous = small reg; paralysing = g large (P14i) |
| A14 | F | static | F | static |  | clip error on tail region; P4 cost log 1/p*(A) |
| A15 | P | dynamic | N | dynamic | ≠ | learning-time exploration; no epistemic object |
| A16 | F | static | F | static |  | localized evaluator error on bug states (P4, extremal) |
| A17 | P | statistical | Pt | statistical |  | diagnosability of scalar feedback: a learning-signal issue |
| A18 | F | static | Pt | dynamic | ≠ | invisibility at step level needs a partial/sequential observation model |
| A19 | F | static | F | static |  | as A16: grading artefact is a region F-hat overrates |
| A20 | F | static | F | static |  | E on unenumerated region; P4/extremal |
| B1 | P | statistical | P | category |  | Cor1.5 gives the stage; "is an optimizer" is mechanism-level |
| B2 | F | static | F | static |  | Cor1.5 inner-stage error, additive in exponent |
| B3 | P | strategic | P | outside-X |  | P19 Gamma gives the snapshot; motive acts on the correction loop |
| B4 | P | strategic | P | outside-X |  | as B3 |
| B5 | P | outside-X | Pt | outside-X |  | undermining oversight = correction loop |
| B6 | N | outside-X | Pt | outside-X | ≠ | resisting modification |
| B7 | N | outside-X | N | outside-X |  | acts on own optimization process; snapshot need not even be misaligned |
| B8 | F | static | P | statistical | ≠ | Cor1.5 stage with proxy objective; goal-vs-evidence is learning under uncertainty about F |
| B9 | F | static | P | statistical | ≠ | contexts with high beta, off-dist E_c; P19 |
| B10 | N | statistical | Pt | statistical | ≠ | narrow-to-broad generalization of training |
| B11 | N | statistical | Pt | statistical | ≠ | as B10 |
| B12 | F | static | P | statistical | ≠ | P19: rho_ev = chat, rho_dep = agentic |
| C1 | F | static | P | statistical | ≠ | contexts + P19; which goal is learned is statistical |
| C2 | F | static | P | statistical | ≠ | instance of C1 |
| C3 | P | statistical | P | statistical |  | B6 informativeness / Cov under q; shortcut choice is learning |
| C4 | P | statistical | Pt | statistical |  | a set of data-consistent evaluators; core has one F-hat |
| C5 | N | outside-E | N | outside-E |  | target has no referent on refined X |
| C6 | N | outside-E | N | outside-E |  | as C5 |
| C7 | F | static | F | static |  | Def9 rho_ev vs rho_dep; P19 Gamma |
| C8 | N | outside-X | P | dynamic | ≠ | absorbable on trajectory X (shared dynamics); DISAGREES with C_boundary (X) |
| C9 | F | static | P | statistical | ≠ | as B9; P14 capability amplifies E |
| C10 | F | static | F | static |  | P14: T(beta) non-monotone; needs scale->beta reading |
| C11 | N | category | N | category |  | interpretability |
| D1 | P | dynamic | N | outside-X | ≠ | resource acquisition changes the actor's reach/capacity |
| D2 | P | dynamic | N | undetermined | ≠ | Turner fixed-MDP theorem needs a prior over intents, NOT frame endogeneity; disagrees with B9 |
| D3 | N | outside-X | Pt | outside-X | ≠ | correction loop |
| D4 | N | strategic | N | strategic |  | assistance game, uncertainty over F |
| D5 | N | dynamic | N | dynamic |  | off-policy learning of interruptions |
| D6 | P | strategic | P | outside-X |  | context-dependent evaluator + Gamma; motive is the deployment decision |
| D7 | F | static | P | category | ≠ | core presupposes actor sees c; discrimination mechanism outside |
| D8 | N | strategic | N | outside-X |  | self-knowledge; self-reference |
| D9 | F | static | F | static |  | behaviour differs by measured-context; P19 |
| D10 | F | static | P | category | ≠ | P12: behaviour does not identify which evaluator component; attribution |
| D11 | N | outside-X | Pt | outside-X | ≠ | acts on own deployment frame |
| D12 | N | outside-X | Pt | outside-X | ≠ | acts on monitoring |
| D13 | N | outside-X | Pt | outside-X | ≠ | acts on the correction loop |
| D14 | N | strategic | Pt | statistical | ≠ | generalization from hack training; malicious user is context |
| D15 | N | strategic | N | category |  | probes are mechanism-level |
| D16 | P | statistical | P | statistical |  | PUSHBACK on §14: reference q contaminated by discourse; Remark 16.1; actor frame exogenous |
| D17 | P | category | N | category | ≠ | hidden computation |
| D18 | N | category | N | category |  | mechanism faithfulness |
| E1 | F | static | F | static |  | Thm9, P11, B4 |
| E2 | F | static | F | static |  | evaluator overrates agreement |
| E3 | F | static | F | static |  | B6 length bias worked example |
| E4 | F | static | F | static |  | as E3 |
| E5 | F | static | P | statistical | ≠ | names the data mechanism; disagreement half is outside-E |
| E6 | P | statistical | P | statistical |  | B6/Cov_q; confound enters via learned RM |
| E7 | F | static | F | static |  | axial error D_par (Cor13.3) / concave target P15 |
| E8 | F | static | F | static |  | KL(p-hat||q), P7 |
| E9 | F | static | F | static |  | judge error |
| E10 | N | outside-E | N | outside-E |  | no single F |
| E11 | P | dynamic | P | dynamic |  | proxy falls: tier-2 violated; P20 still decomposes for any actor |
| E12 | F | static | F | static |  | P19(ii) chain rule: exponent is rho-weighted; P4 localized |
| E13 | F | static | F | static |  | evaluator undefined off enumeration (if constitution = evaluator, not target) |
| E14 | F | static | F | static |  | P10(d): E_p|E| <= e^{Dinf} E_q|E| |
| E15 | F | static | P | statistical | ≠ | Cor1.5 stage inheritance |
| E16 | F | static | P | strategic | ≠ | g vs Delta-F trade (P14); pressure to undo is competitive |
| E17 | F | static | P | statistical | ≠ | contexts: mitigation only where framing present |
| F1 | P | strategic | P | statistical |  | P18 caps detection; evaluator-capacity asymmetry not in core |
| F2 | N | category | N | category |  | latent knowledge |
| F3 | F | static | F | static |  | P12/16 identification + P18 |
| F4 | N | category | N | category |  |  |
| F5 | N | category | N | category |  |  |
| F6 | F | static | F | static |  | Goodhart on benchmark; P20 |
| F7 | P | statistical | Pt | statistical |  | core predicts no gain beyond F-hat; W2S gain is a learning prior |
| F8 | P | strategic | Pt | strategic |  | zero-sum debate game |
| F9 | F | static | P | statistical | ≠ | Cor1.5 composition, but RRM composes evaluators not behaviour stages |
| F10 | P | strategic | F | static | ≠ | Goodhart on a fixed monitor (obfuscated hacking); arms-race version is strategic |
| F11 | F | static | F | static |  | P19: realism moves rho_ev toward rho_dep |
| F12 | P | strategic | P | strategic |  | P18 bound holds; adversarial choice of behaviour is a game |
| G1 | N | strategic | N | strategic |  | collusion |
| G2 | N | strategic | N | strategic |  | hidden channels |
| G3 | N | strategic | N | strategic |  | repeated-game pricing; not potential |
| G4 | N | outside-X | N | outside-X |  | F depends on actor |
| G5 | F | static | F | static |  | engagement vs welfare E; societal-aggregation part is outside-E |
| G6 | N | strategic | N | strategic |  | race |
| G7 | N | dynamic | N | dynamic |  | irreversibility |
| G8 | N | dynamic | N | strategic |  | no misaligned individual; emergent |
| G9 | P | statistical | N | undetermined | ≠ | correlated errors across actors; core speaks expected regret of one actor |
| G10 | N | outside-E | N | outside-E |  |  |
| H1 | F | static | F | static |  | judgement=target, momentary motivation=evaluator |
| H2 | P | dynamic | P | dynamic |  | B12c: date-indexed contexts; reversal is sequential |
| H3 | P | dynamic | P | dynamic |  | as H2 |
| H4 | P | dynamic | P | dynamic |  | P4 localized overrating of drug region; tolerance dynamics |
| H5 | P | outside-X | Pt | outside-X |  | acts on evaluation mechanism (wireheading analogue) |
| H6 | P | dynamic | N | dynamic | ≠ | evaluator resets; nothing misaligned at a snapshot |
| H7 | F | static | F | static |  | forecast error = E |
| H8 | N | category | N | category |  |  |
| H9 | N | category | N | category |  |  |
| H10 | P | outside-E | N | outside-E | ≠ | no pre-existing target |
| H11 | P | outside-E | N | outside-E | ≠ | which elicitation is "true" undefined |
| H12 | F | static | F | static |  | frame=context, F(c) invariant, F-hat(c) varies (normative invariance assumed) |
| H13 | P | statistical | Pt | statistical |  | belief formation |
| H14 | N | category | N | category |  |  |
| H15 | N | outside-E | N | outside-E |  | which self is principal |
| H16 | N | outside-X | N | outside-X |  | choice changes F |
| H17 | N | outside-X | N | outside-X |  | F depends on reach |
| H18 | F | static | F | static |  | proxy pursuit |
| H19 | P | dynamic | P | dynamic |  | habit = reference q (B12a); repetition moves q |
| H20 | P | dynamic | P | dynamic |  | state-varying capacity |
| H21 | N | dynamic | P | dynamic | ≠ | beta->0 collapse to reference; learned |
| H22 | P | dynamic | P | strategic |  | intrapersonal game (B12c) |
| H23 | N | strategic | N | outside-E |  |  |
| H24 | P | dynamic | N | dynamic | ≠ | evaluator depends on past behaviour |
| H25 | P | strategic | P | strategic |  | designer finds tail of person's E (extremal, by a second optimizer) |
| I1 | F | static | P | strategic | ≠ | agency loss = R_J; contracting is Stackelberg |
| I2 | F | static | P | strategic | ≠ | hidden action + contract |
| I3 | N | strategic | N | strategic |  | types, equilibrium |
| I4 | F | static | F | static |  | P20, Thm9 |
| I5 | P | dynamic | F | static | ≠ | Goodhart restated |
| I6 | P | strategic | P | strategic |  | 2/4 derived; causal, adversarial not |
| I7 | F | static | F | static |  | B5 |
| I8 | P | dynamic | Pt | dynamic |  | means->ends over time |
| I9 | N | outside-X | Pt | strategic | ≠ | lobbying shapes evaluator |
| I10 | F | static | F | static |  | procedure = proxy |
| I11 | F | static | F | static |  | B5 / Goodhart |
| I12 | F | static | F | static |  | metric replaces judgement |
| I13 | F | static | F | static |  | X_anti / negative Cov_q (P14ii, Thm13b) |
| I14 | N | strategic | N | strategic |  | B13 would move to F post-hoc |
| I15 | N | strategic | N | strategic |  | B13 would move to F post-hoc |
| I16 | N | outside-E | N | outside-E |  |  |
| I17 | N | outside-E | N | outside-E |  |  |
| I18 | N | outside-X | N | strategic |  | manipulable aggregation |
| I19 | P | strategic | Pt | strategic |  | contest |
| I20 | P | strategic | Pt | strategic |  | second-best contracting |
| I21 | P | strategic | P | dynamic |  | selection on cost with negative correlated response in quality (B11/Price) |
| I22 | F | static | F | static |  | B5 across time |
| I23 | N | strategic | N | strategic |  |  |
| I24 | N | strategic | N | strategic |  |  |
| I25 | P | dynamic | P | dynamic |  | frozen evaluator, drifting contexts (P19) |
| I26 | N | outside-X | Pt | outside-X | ≠ | agent redefines own mandate |
| I27 | F | static | F | static |  | Hawthorne/Goodhart on auditability |
| I28 | F | static | F | static |  | per-link evaluator error under capacity |
| I29 | P | strategic | Pt | strategic |  | evaluator not additive in incentive; signalling |
| I30 | N | outside-E | N | outside-E |  | common agency |
| J1 | F | static | F | static |  | tail extrapolation off q-support: P10(d)/P11 |
| J2 | F | static | F | static |  | ancestral vs modern contexts, P19 |
| J3 | F | static | F | static |  | instance of J1/J2 |
| J4 | F | static | F | static |  | PUSHBACK: causal Goodhart projects to E on the decoupling behaviours |
| J5 | P | outside-X | Pt | outside-X |  | as H5 |
| J6 | P | strategic | P | strategic |  | P4 localized host error; coevolution |
| J7 | P | strategic | P | strategic |  | as J6 |
| J8 | P | strategic | P | strategic |  | as J6 |
| J9 | P | strategic | P | strategic |  | as J6 |
| J10 | N | strategic | N | strategic |  |  |
| J11 | N | strategic | Pt | strategic | ≠ | parent as principal; begging game |
| J12 | N | strategic | Pt | strategic | ≠ | as J11 |
| J13 | N | strategic | Pt | strategic | ≠ | exogenous rewrite of host evaluator by another agent |
| J14 | F | static | F | static |  | PUSHBACK on §14: B11(iii) correlated response |
| J15 | F | static | F | static |  | B11 |
| J16 | N | strategic | F | static | ≠ | PUSHBACK on §14: population tilt anti-aligned with designated target (X_anti) |
| J17 | P | strategic | F | static | ≠ | proxy cue for relatedness |
| J18 | P | strategic | P | strategic |  | cue-context shift, but reciprocity is a repeated game |
| J19 | F | static | N | outside-E | ≠ | target choice (fitness vs longevity) |
| J20 | N | dynamic | N | strategic |  | frequency-dependent coevolution |
| K1 | P | strategic | N | strategic | ≠ | multilevel |
| K2 | P | strategic | Pt | strategic |  | element transmission vs organism fitness; multilevel Price stated only |
| K3 | P | strategic | Pt | strategic |  | element transmission vs organism fitness; multilevel Price stated only |
| K4 | P | dynamic | Pt | strategic |  | element transmission vs organism fitness; multilevel Price stated only |
| K5 | P | dynamic | Pt | strategic |  | element transmission vs organism fitness; multilevel Price stated only |
| K6 | N | strategic | N | strategic |  | conflict between genomes/parties |
| K7 | P | strategic | N | strategic | ≠ | conflict between genomes/parties |
| K8 | P | strategic | N | strategic | ≠ | conflict between genomes/parties |
| K9 | N | strategic | Pt | strategic | ≠ | as J13 |
| K10 | P | dynamic | P | dynamic |  | somatic selection vs organism target (B11) |
| K11 | P | dynamic | P | dynamic |  | as K10 |
| K12 | F | static | F | static |  | B10 / P4 |
| K13 | P | strategic | N | strategic | ≠ | conflict between genomes/parties |
| K14 | P | strategic | P | strategic |  | as J8 |
| K15 | N | strategic | N | strategic |  | conflict between genomes/parties |
| L1 | P | static | P | undetermined |  | as A10 |
| L2 | P | outside-E | P | undetermined |  | as A11 |
| L3 | F | static | F | static |  | Cor13.1 |
| L4 | P | dynamic | N | undetermined | ≠ | as D2 |
| L5 | N | outside-X | N | outside-X |  | causal influence diagrams |
| L6 | N | outside-X | N | outside-X |  |  |
| L7 | N | category | N | category |  | world models |
| L8 | N | outside-E | N | outside-E |  |  |
| L9 | N | outside-X | N | strategic |  |  |
| L10 | P | strategic | P | strategic |  | as I6 |
| L11 | P | dynamic | N | dynamic | ≠ |  |
| L12 | F | static | F | static |  | P12/16 |
| L13 | F | static | F | static |  | P12(ii)/g3: q and F-hat trade off |
| L14 | N | category | N | category |  | computability |
| L15 | N | strategic | N | strategic |  | as D4 |
| M1 | P | statistical | P | statistical |  | KL-slope derived (Gaussian); curvature and RM-size not |
| M2 | F | static | P | statistical | ≠ | error growth of a learned evaluator is statistical; P10(d) gives its consequence |
| M3 | F | static | F | static |  | P4: p-hat(A) logistic in beta*M -> sharp for large M |
| M4 | P | statistical | Pt | statistical |  | attribution to data |
| M5 | F | static | P | category | ≠ | as D7 |
| M6 | F | static | P | category | ≠ | contexts; direction not predicted |
| M7 | F | static | P | category | ≠ | contexts; direction not predicted |
| M8 | P | dynamic | Pt | dynamic |  | training dynamics |
| M9 | F | static | P | statistical | ≠ | as B12 |
| M10 | N | statistical | Pt | statistical | ≠ | as B11 |
| M11 | N | statistical | Pt | statistical | ≠ | as B10 |
| M12 | F | static | F | static |  | as E12 |
| M13 | P | category | N | category | ≠ | probes |
| M14 | P | strategic | F | static | ≠ | Goodhart on a deception detector (as F10) |
| M15 | P | statistical | P | statistical |  | as D16 |
| M16 | P | category | N | category | ≠ | coherence of goal pursuit |
