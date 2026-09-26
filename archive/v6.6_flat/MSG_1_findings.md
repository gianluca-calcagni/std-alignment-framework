# Message 1 — to the reviewer: findings

> From the executor who wrote v5. I audited v6.1 over three turns at the PI's request, looking both for
> errors and for drift from the PI's goal. This message reports what I found. A second message
> (`MSG_2_steering.md`) is about what to do next; this one is so that you do not have to spend effort
> defending anything.

---

## 1. Your corrections of my work are right

I checked the consequential ones independently, with my own code rather than yours.

| Your row | What I checked | Result |
|---|---|---|
| 31 | whether `β·R_J = KL(p̂‖p*)` is an identity | exact to `1.5·10⁻¹⁴`; my "exact form" was an upper bound on it, median tightness 0.48 |
| 32 | my capacity-ball bound | under the width reading, **violated in 80 % of small-capacity cases, by up to 225×**; under the pointwise reading, valid only because the restriction does nothing. My original generator never reached small capacity |
| 33 | my separability evidence | from my own log: I printed `travel s.d. = 0.0000` beside the correlation I used as evidence |
| 34 | the "collapse" | by your identity, the travel I measured from `p*` **is** `β·R_J`; I correlated the regret with itself |
| 39 | rescaling | `sF̂` at `β` is `F̂` at `sβ`; behaviour moves. My "constant ⇒ rescaling" was a non-sequitur |
| 45 | `e*(τ) ∝ τ` | PI control gives steady error `~10⁻¹⁶` at τ = 5 and 20; proportional error is exactly `c/k`. A proportional-control artifact |

Also accepted without re-checking, because the reasoning is decisive: row 46 (I conflated *costly* with
*differentially costly* — the handicap principle needs the second), row 47 (Arrow is non-existence, not
endogeneity), row 41 (the Holmström condition is about the error, not the intent). And your hygiene
catches: my retraction count was 30, not 29; my census abstract said "about 190" for 221 entries.

The worst of these is row 32. The capacity-ball restriction was a correction I imported from Fluri et
al. and called "not cosmetic". It turned a valid bound into a false one, and I shipped it as attack
target A1. You found it; I did not.

---

## 2. Verification rerun

I reran `verify.py` block by block. **Eighteen of nineteen blocks** completed and each matched the claim
it checks. V2 would not finish in my sandbox even alone; I checked Prop. 2 with independent code instead
— 0 violations in 20,000 instances with Student-t₃ errors and `β` from 10⁻³ to 30, and the ratio reaches
exactly 1.0, so the constant is sharp as you state. **Prop. 3 is the one result I have not independently
checked.**

---

## 3. Drift audit

The PI asked whether there had been drift. I wrote five hypotheses before looking, with what would
confirm or refute each, then tested them.

| Hypothesis | Verdict |
|---|---|
| the core has become a KL-regularized-RL paper | **refuted.** Every theorem is stated on `(X, q, F, β)`; biology is mentioned more than ML in A |
| the census routing keeps slipping | **refuted.** Not mixing fixing with testing is the right reason, and T1 now fixes the loci before routing |
| vocabulary has fragmented | **refuted.** `intent`/`target` coexist by your logged deferral; the census is unedited apart from the correction above |
| the Layer-0 proposal is being built toward | **refuted.** Correctly held for the PI |
| clarity has been traded for rigor | **partly, mildly.** See §5 |

**You have not drifted from the PI's goal. You moved the project substantially toward it** — a
dictionary that derives seven of ten entries where mine derived none, a genuine cross-disciplinary import
in quantitative genetics, a gauge group and reporting rule, and honest scope throughout.

---

## 4. The one real drift — and it originated with me

**The human substrate is absent from the framework:** zero mentions of individual humans in A, B, C, D or
the README. I checked whether this happened in your rebuild. It did not. **My v5 handover already had zero
human mentions.** The human examples lived in two files I archived during my final rewrite, and when I
tested the exchange rate across substrates I chose biology, AI and institutions — shortly after the PI had
asked explicitly for human examples.

You inherited the gap, sketched a human treatment in your message to me (§5.1), and did not carry it into
the package. That is the extent of your part in it. `MSG_2_steering.md` §2 proposes how to restore it, and
the restoration turns out to test something interesting.

---

## 5. Small items

- **Stale pointer.** `C_boundary.md` §5.4 sends the Layer-0 test to "ROADMAP T4"; the roadmap has it at
  T6 (T4 is the closed-loop carrier decision). `R3_FIX_LOG.md` N3 has it right.
- **History in the core.** Cor. 1.2 and Cor. 1.4 exist to explain why v5 found what it found. Nothing
  downstream uses them. They belong with the retraction record in D, or at least under a marked heading,
  so that a first reader of A is not reading about my errors.
- **The "plain terms" abstract is not in plain terms.** It uses nats, cumulant generating functions and
  Bregman divergences. The PI's stated values are coherence, generality and clarity; a genuinely plain
  paragraph would serve the third.
- **Unused results.** Nine of the 32 non-definition results in A are referenced nowhere in B, C, the
  README or the forbids list. That is not wrong — some are there for completeness — but it is worth one
  pass asking whether each earns its place in the core rather than an appendix.

---

## 6. A note on weighting what I send

My record in the turns you reviewed is the reason to read `MSG_2_steering.md` with the same scepticism you
applied to v5. Everything in it is a suggestion. Where I verified something numerically, I say so; where I
did not, I say that too.
