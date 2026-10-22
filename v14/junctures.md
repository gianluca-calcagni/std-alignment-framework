# Junctures: where the framework's parts meet, and what each meeting inspires

> **Status: a brainstorm for the PI (Q77), the executor's; not reviewed, not decided, pending R24.** Nothing here is
> proved except what it cites. The imports from engineering and the social sciences named at the end are from memory and
> are to be read before any item cites them.

The PI observed that a record is where the specification meets the actor, and that such a meeting is fragile, as a
joint is in a structure: it can be tampered with, it invites gaming, and it can leave statistical artefacts over time.
This file lists every such meeting, a **juncture**, says how v14 treats it, and names the measure it inspires.

## The picture

Engineering analyses a hazard at the interactions between the parts of a control loop, not inside the parts (the method
of system-theoretic hazard analysis, STPA, is the clearest form). Read as a loop, the framework has these parts: the
**principal**, who declares; the **specification**; the **world**, which poses situations; the **actor**, which sees
through its **view** and acts through its **actions** on an **environment**; the **record**, made by a sensor, a grader
and a log; the **test**, which turns the record into evidence; the **report**, read by whoever decides; the
**shaper**, which changes the actor; other **actors** and other **principals**; and **time**. A juncture is an arrow
between two of them: something crosses it, and the crossing can fail.

For each juncture the analysis asks four questions, after the guide words of hazard studies (HAZOP): what crosses it,
and at which σ-algebra; what the **contract** is, declared before the record ([A5]); how the crossing can fail:
*missing*, *coarse*, *distorted*, *delayed*, *fed back*, *reused*; and what **measure** the failure inspires.

## The junctures

| # | Juncture | What crosses | How it fails | The measure it inspires | In v14 now |
|---|---|---|---|---|---|
| J1 | principal → specification | an intention, as requirements, the world's part `ℰ`, tolerances | misspecified; silent inside cells; inconsistent; fitted to the data; revised without a record | an inconsistent specification found before any record (Q74); latitude taken (RS7); each verdict's sensitivity to each declared limit, the budget's price (VK7); the declaration's date and hash | the inconsistency check decided (Q74); latitude taken proposed (RS7); the budget's price proved (VK7), other sensitivities not written; date and hash not written |
| J2 | specification ↔ record's **signature** | what a record must contain to be judged: outcomes, `ℰ`, the record's σ-algebra `ℛ`, horizon | a requirement finer than any record can see; fields that do not match | the share of each requirement a record at `ℛ` can decide, and its hidden part (RS4); a verification status per requirement | RS1–RS4; the signature not yet a declared object (`NOTES.md` §35.2, H67) |
| J3 | world → actor, the **view** | what the actor can tell apart | coarse; spoofed or injected inputs; shifted from what was declared | missing resolution (RS6); perplexity (H59); the view revealed from below (RS8) | proved or proposed |
| J4 | actor → world, **actions** and environment | what the actor can bring about | incapable; side effects on what nobody records; irreversible; actions that enlarge the actor's own feasible set | unavoidable misalignment; the worst case over the feasible set (`interface.md`; `NOTES.md` §33.5); growth of the feasible set along a course (`training.md`) | the first two |
| J5 | the boundary of `ℰ`, the world's part | which part of an outcome the world chooses | the actor shapes what it is asked (a conversation, a recommender shaping its users): **performativity** | a test of the declared exogeneity: whether the world's choices depend on the actor's earlier outputs; the divergence of the world's responses under the actor from those under a baseline | declared only (Q76) |
| J6 | outcome → record, the **sensor** | what happened, as noted | coarse (hidden misalignment); a grader's errors; a tampered sensor; selective logging; an edited log | the hidden interval (RS4); a grader's confusion matrix (H47); tampering against an honest channel ([P50]); the rate of missing records and its dependence on the outcome | the first and third; the rest open; an edited log is out of scope (`LIMITS.md`) |
| J7 | record → test, **evidence** | the record, into bets | peeking and optional stopping; many requirements at once; the same record reused for many decisions; bets chosen after looking | tests valid at every stopping time (VE3); evidence combined across requirements; a count of how often a record was used to choose; the registration's hash | the first and last; the others open |
| J8 | test → report → decision | verdicts and numbers | scales summed; certify read as more than an average or a sample of independent draws (Q76); a label read as more than its object; a number without its declaration | the report's validator; the labels' tests (L1, L2); every number naming its declaration (`README.md`) | in part |
| J9 | evaluation → actor, **observation fed back** | that the actor is being judged | behaviour that depends on being observed (evaluation gaming, sandbagging); adaptation after a certificate | the gap between honeypots and evaluations (H55); how well the actor's view tells evaluation from use ([P16], [P17]); misalignment by period after a verdict | proposed |
| J10 | verdict → shaper → actor, **feedback** | a signal that changes the actor | the feedback's own gaps (outer); a course that stops doing what it rewards (inner); overoptimization; misgeneralization | SH1's terms; the profile; misalignment by condition (`training.md`) | proposed, SH1 proved |
| J11 | actor ↔ actor | correlation between decisions | collusion; shared randomness; a common cause | dependence against a declared information structure ([P39]) | v13's; to migrate |
| J12 | principal ↔ principal | several specifications | conflict; gridlock without intensities | a joint inconsistency check; [P42]'s pooling | v13's; to migrate |
| J13 | reference → specification | a behaviour the specification compares with | known only by samples; changing; itself in breach | two-sample bets; an interval on the reference; the inconsistency check (Q74) | the inconsistency check decided (Q74); the rest open |
| J14 | **time**: record ↔ deployment, certificate ↔ actor's version | the claim that the record still describes the actor | drift; a certificate outliving its version or window | drift ([P54]); a certificate stating its version, window and expiry | in part |

## Couplings: a refinement here moves something there

The PI's example, the σ-algebras, is the clearest case of junctures acting on each other. The resolution results make
most of these exact.

| Refine | What it does | What it moves elsewhere |
|---|---|---|
| the record's σ-algebra, a better measurement | visible misalignment does not fall, hidden does not rise, their sum fixed (RS1) | a new channel to tamper with (J6); if the actor sees the record's new precision, it can move its misalignment into the cells still merged, *displacement*, so a refinement should be followed by misalignment cell by cell, before and after |
| the principal's σ-algebra, more care | misalignment does not fall when the finer specification's acceptable set lies inside the coarser one, `M` being an infimum over it; latitude taken does not rise (RS7) | more requirements, so more tests at once (J7) and more chances of an inconsistent specification (J1) |
| the actor's view or resolution, more capability | the missing-resolution factor does not rise (RS6); latitude available does not fall, perplexity does not rise (H59) | **the actor tells evaluation from use better** (J9), so honeypots weaken: capability and evaluability pull against each other. An excuse of incapacity also weakens, through elicitation (VF3) |
| the actor's actions, new tools | unavoidable misalignment does not rise; culpability reaches further | the worst case grows (J4); side effects reach variables nobody records |
| the world's part `ℰ`, declared wider | more of the outcome is charged to the world, less to the actor | if what the actor shapes is declared the world's, its influence on its own situations escapes judgement (J5) |
| the record's horizon, longer | smaller margins certifiable; drift visible | more peeking (handled by VE3) and a record reused more (J7) |

## Three rules the list suggests

1. **A contract at every juncture.** What crosses, at which σ-algebra, from whom, declared before the record. The
   framework already does this for the specification ([A5]); the list asks it of the signature (J2), the world's part
   (J5), the sensor (J6) and the certificate's window (J14).
2. **Every path from what judges the actor back to the actor is a channel.** A path to the record or the grader is a
   channel for tampering (J6); a path from the verdict to the actor's view or training is a channel for gaming (J9,
   J10). Each needs either a second, independent channel, the only thing that identifies tampering ([P51]), or a
   measure of how far the actor reaches into it.
3. **Monitoring does not stop.** A conviction keeps its level against any adaptive actor (VE3); a certificate does not,
   since the actor can change after it (J9, J14). Certificates expire with the version and window they name.

## Imports, to read before citing

Named from memory, each with what it would bring; none is read yet, so none is cited.
- System-theoretic process analysis (STPA, Leveson): hazards at interactions in a control structure; the frame above.
- Hazard and operability studies (HAZOP) and failure modes and effects analysis (FMEA): guide words and a table per
  juncture, with severity and detectability, the latter being the framework's evidence.
- Design by contract (Meyer): preconditions and postconditions at interfaces, the declarations of rule 1.
- Metrology's guide to the expression of uncertainty: a sensor's calibration and drift (J6, J14).
- Goodhart's law in its four variants, regressional, extremal, causal and adversarial (Manheim and Garrabrant), and
  Campbell's law: the failures of J6, J9 and J10 by mechanism.
- Performative prediction (Perdomo and coauthors): a predictor that shifts the distribution it predicts (J5).
- Adaptive data analysis and the reusable holdout (Dwork and coauthors): what reusing a record costs (J7).
- The Hawthorne effect and the Lucas critique: behaviour that changes because it is observed or because policy changed
  (J9).
