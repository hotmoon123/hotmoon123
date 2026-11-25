# Law and governance

The rules the business must obey, and the rules it imposes on itself. Researched
**2026-11-06**.

Marked **FACT** (sourced), **INFERENCE** (my reasoning), **DECIDED**, **PROPOSED**.

> **Not legal advice.** Every claim below carries its source. Ghanaian law changes;
> confirm with a lawyer or the regulator before relying on any of it. What this
> document does is tell you which questions to ask and which ones are already
> answered.

---

## The two findings, first

### 1. SoftFire is almost certainly an unregistered data controller — and 2026 is an enforcement year

**FACT.** The Data Protection Act, 2012 (**Act 843**) requires **every data
controller to register with the Data Protection Commission before processing
personal data** (s.27(1)). Registration is valid **two years** and must be renewed
(s.50). An unregistered controller **must not process personal data at all**
(s.53). Processing without registration is a criminal offence: a fine of up to
**250 penalty units or up to two years' imprisonment, or both** (s.56).

**FACT.** The DPC has declared **2026 an enforcement year**. Its Executive
Director, Arnold Kavaarpuo, said there will be **"no exemptions"** — the law
mandates registration regardless of size. Spot checks and inspections began
**5 October 2026**. The Communications Minister announced a directive requiring
the DPC to impose fines on unregistered controllers. The Commission has moved
*"from awareness creation to enforcement."*

**FACT — there is a size threshold, and it is not in the Act.** One 2026 source
states registration is mandatory for any entity processing **more than 200
records**, with sole traders under 200 exempt. **This conflicts with the Act's own
text**, which sets no threshold, and with the DPC's public position that there are
no exemptions. **Treat the 200-record figure as unconfirmed and do not rely on it.**

**Does SoftFire process personal data? — INFERENCE, and the answer is yes.**
- A buyer messages the WhatsApp number. That is a name, a phone number and
  whatever they say about their business.
- The site's own brief flow opens WhatsApp with text pre-filled.
- Every site SoftFire builds with a contact form **collects personal data on the
  client's behalf.**

**And that second point creates a second, separate obligation — FACT.** Act 843
**s.30(2) requires a written contract with every data processor**, and s.30(4)
requires the controller to ensure a processor outside Ghana complies with Ghanaian
law.

**So when SoftFire builds a site with a contact form:**
- the **client** is the data controller for that form;
- **SoftFire** is the processor;
- and there must be a **written processor agreement**, not a handshake.

**DECIDED — the actions, in order:**

| # | Action | Cost | When |
|---|---|---|---|
| 1 | Register as a data controller at `app.dataprotection.org.gh` | **GHS 500–5,000/yr** depending on size (reported) | **before the next enquiry** |
| 2 | Renew every two years; notify changes within **14 days** (s.55) | — | calendar it |
| 3 | Add a **privacy line** to the site: what is collected and why | GH₵0 | with the next deploy |
| 4 | Add a **processor clause** to every contract | GH₵0 | before the first paid job |
| 5 | Keep an **incident log** — breaches must be notified to the DPC and the people affected **as soon as reasonably practicable** (s.31) | GH₵0 | from day one |
| 6 | Appoint a data supervisor if the DPC requires one at registration | — | at registration |

**INFERENCE — this is the single highest-priority legal action in the business.**
It is cheap, it is quick, the regulator has publicly announced it is coming, and
the penalty is criminal. Nothing else in this document matters as much as item 1.

### 2. In Ghana, the client owns the copyright by default — and almost no studio tells them

**FACT.** The Copyright Act, 2005 (**Act 690**), s.7: *in the absence of a contract
to the contrary, the economic right in a work **vests in the person who
commissioned it***. Ghana's default is the **opposite** of the US and UK default,
where the contractor keeps the copyright unless there is a written assignment.

**FACT.** Moral rights stay with the author — the right to be identified and to
resist distortion — unless waived.

**INFERENCE — this is the best legal fact in the whole brand.** A Ghanaian client
who commissions a website **already owns it by law**, unless the studio's contract
takes it away. Many contracts do, using template "work made for hire" language
imported from the US where it means something different.

**So the sentence on the page is true, checkable, and nobody else says it:**

> **In Ghana the work you commission is yours by law — unless the contract takes it
> away. Mine does not take it away.**

**But there is a carve-out that must be written honestly — INFERENCE.** SoftFire
builds from a reusable system: the layout, type scale, components and checks that
produced this very page. If everything vests in the client, SoftFire gives away its
base and cannot build the next site. The contract must therefore say:

| What | Whose |
|---|---|
| the pages, words, images, structure and content made **for this client** | **the client's** |
| SoftFire's pre-existing components, and the right to reuse the approach | **SoftFire's**, with the client granted a **perpetual, irrevocable licence** to use what is on their site |
| the client's own logo, photos and text | the client's, always |
| third-party fonts and libraries | under their own licences — Inter and JetBrains Mono are SIL OFL, so this is fine, and it is worth saying so |

**DECIDED:** the assignment clause is written out in plain language in the scope,
not buried. The carve-out is stated in the same breath as the gift, because a gift
with a hidden condition is not a gift.

---

## 1. The laws that actually apply

Not a list of every Ghanaian statute. The ones that touch this business.

| Law | What it requires of SoftFire | Status |
|---|---|---|
| **Data Protection Act, 2012 (Act 843)** | register as a controller; written processor contracts; notify breaches; honour access and correction requests | **UNMET — see above** |
| **Copyright Act, 2005 (Act 690)** | default ownership vests in the client; assignment must be **in writing and signed** (s.9(4)); moral rights stay with the author | write the clause |
| **Income Tax Act, 2015 (Act 896)** as amended by **Act 1178 (2026)** | pay personal income tax; file by 30 April | see `OPERATIONS.md` §8 |
| **Revenue Administration Act, 2016 (Act 915)** | keep records; file electronically; penalties and interest | see `OPERATIONS.md` §8 |
| **Trade Marks Act, 2004 (Act 664)** | register the name if it is to be defended | see `BRAND.md` §4 |
| **Companies Act, 2019 (Act 992)** | business name registration; annual renewal | GH₵130 + GH₵70/yr |
| **Electronic Transactions Act, 2008 (Act 772)** | electronic records and signatures are legally valid | **this is why a WhatsApp "yes" is arguably binding — so get the signature anyway** |
| **Cybersecurity Act, 2020 (Act 1038)** | relevant once handling others' systems at scale | not yet triggered |
| **Contracts Act, 1960 (Act 25)** | the general law of contract — offer, acceptance, consideration | applies to every quote |

**INFERENCE — the shortest honest summary.** SoftFire's legal exposure is not
intellectual property, it is **paperwork**: one registration, one clause, one
processor agreement, one privacy line. All four are cheap and none are done.

---

## 2. What a contract must contain

A one-person studio does not need a lawyer for every job. It needs one good
agreement, reused, with the variables filled in.

**DECIDED — nine clauses, and the reason each exists:**

| # | Clause | Why it is there |
|---|---|---|
| 1 | **Parties and date** | who is bound; the business name is not a legal person — **Caleb is** |
| 2 | **Scope** — pages, sections, exclusions, one revision round | the whole fixed-price promise rests on this |
| 3 | **Price and payment** — 50/40/10, and what stops work | a promise is not a payment |
| 4 | **Dates and dependencies** — the launch date moves if content is late | protects the date you gave |
| 5 | **Ownership** — the s.7 assignment, the carve-out, the licence | see §"finding 2" |
| 6 | **Warranty** — 30 days, bugs only, bug defined | `MAINTENANCE.md` §4 |
| 7 | **Data** — the processor clause required by Act 843 s.30(2) | the legal obligation |
| 8 | **Liability** — capped at the fees paid | standard, and honest |
| 9 | **Termination** — either party, written notice, payment for work done, files released | the exit cost is a zip file |

**INFERENCE — clause 9 is a feature, not a formality.** Every competitor's exit
cost is a migration. Yours is a zip file. Say so.

### 2.1 The three sentences that prevent most disputes

1. *"A bug is something that does not work as the scope said. A change is something
   that works and you want different. I will tell you which one it is before I
   touch it."*
2. *"If your content arrives late, the launch date moves by the same number of
   days. I will tell you the new date in writing."*
3. *"Nothing recurs until you say yes in writing. I will not invoice you without
   asking first."*

---

## 3. Governance: how one person governs a business

Governance sounds like a board. For a sole trader it means something narrower and
more useful: **the rules that stop the person who does the work from quietly
overriding the person who set the standard.**

The risk is not fraud. It is **drift** — the scope creeping, the warranty stretching,
"just this once" becoming the norm, and the business slowly becoming the thing it
said it would not be.

### 3.1 The constitution — six clauses

This is the whole of SoftFire's internal law. It fits on a card.

1. **No price without a written scope, and no scope without exclusions.**
2. **No work before the deposit clears.**
3. **The client owns their accounts, their domain and their content. Always.**
4. **Nothing recurring starts without an explicit yes, in writing.**
5. **No claim that has not been measured or sourced — including in my own records.**
6. **If a rule above costs me the job, the rule wins.**

**INFERENCE — clause 6 is the only one that needs courage.** The other five are
procedures. The sixth is the one that gets tested on a Thursday afternoon when a
church with a real budget wants a GH₵1,500 portal.

### 3.2 Decision rights

| Decision | Sole authority | Checked by | Reversible? |
|---|---|---|---|
| price | Caleb | the ladder in `PRICING.md` | slowly — the ladder is published |
| take the job | Caleb | the ten-question screen (§3.4) | no — once accepted, it is accepted |
| scope | Caleb + client signature | the exclusions list | only by a new written number |
| a claim on the page | the verifier | `verify-claims.py` | yes |
| client's accounts | the client | the handover sheet | n/a — never Caleb's to decide |
| tax position | Caleb | an accountant | yes, before filing |

**INFERENCE — the only genuine check on a one-person business is a written
document that predates the temptation.** That is what the verifier is. It is not
there to catch typos; it is there so that a decision made calmly in November
cannot be quietly undone in a hurried March.

### 3.3 The review cycle — governance as a calendar

| Cycle | Question asked | Output |
|---|---|---|
| **Weekly, Friday** | are the books closed and is anything owed? | a reconciled week |
| **Monthly** | did the plan notes go out; did the tax move; is anything overdue? | a closed month |
| **Quarterly** | which rule did I break, and was it the rule's fault? | one rule changed, or one kept |
| **Annually** | is the business still the one in this document? | a written diff |

**INFERENCE — the quarterly question is deliberately uncomfortable.** *"Which rule
did I break"* assumes a rule was broken. If the answer is always "none", the
question is not being asked honestly.

### 3.4 The ten-question screen, before accepting any job

Every "yes" here costs money later. Answer all ten before quoting.

1. Can they state what "done" means in one sentence?
2. Is the buyer the person who signs?
3. Is the budget at or above the published price?
4. Is the content available, or is someone writing it?
5. Is there one decision-maker, or a committee?
6. Does this need a database, a login or payments? *(if yes, it is not this offer)*
7. Can I meet the date with 30 hours?
8. Will the deposit clear before I start?
9. Are they willing to own the accounts?
10. **Would I be comfortable if this client published the entire email thread?**

**INFERENCE — question 10 is the one that matters.** It is the fastest honest
screen for a client who will be a problem, and it works because you already know
the answer before you finish asking.

### 3.5 Conflicts of interest

A one-person business has three, and they are all about the same person.

| Conflict | The temptation | The rule |
|---|---|---|
| **Sell the bigger offer** | quote the portal when the site would do | quote the smallest offer that solves the stated problem, and say so |
| **Stretch the warranty** | a "free" fix to keep the peace | name it as a bug or a change, every time, even when it is free |
| **Take the discounted job** | a lower price to win the first client | **never discount.** A published price that moves once has moved forever. Add scope, not a discount |

**DECIDED — no discount, ever, in any form.** Not a stated one, not a dated one,
not one for a church. There is no version of a lower price that leaves the position
intact, because the position *is* the price.

**What to do instead, when a job is worth winning:** add scope at the same price.
The first three clients get a **written case study published with their permission**
included in the GH₵1,500 — not a GH₵500 reduction. It costs two hours instead of
five hundred cedis, and it produces a better case study because the client consents
to it from the start.

**INFERENCE — why the "stated discount" I proposed earlier was wrong.** It is
honest about the *motive* and still corrupts the *signal*. A buyer reads a published
price as a fact. The moment one buyer is told it is negotiable, the fact becomes an
opening offer, and every conversation after that is a negotiation — with a client
who has been told, by the discount, that negotiation works.

### 3.6 Records as governance

**INFERENCE — a business is governed by what it can prove.** Four records, all
free, and all of them are governance rather than admin:

| Record | Proves |
|---|---|
| the signed scope per job | what was promised |
| the payment log | what was paid, and when |
| the monthly check note | what was done for the retainer |
| the incident log | what broke, and what was done |

**FACT-adjacent:** Act 843 requires breach notification (s.31), so the incident log
is not merely good practice — it is the evidence that the duty was met.

### 3.7 What happens if Caleb cannot work

Nobody plans for this, and it is the cheapest thing in the document.

| Document | Where | Why |
|---|---|---|
| **one handover sheet per live client** | the job folder | host, registrar, what to do if the site breaks |
| **the account list** | a sealed note with one trusted person | which accounts exist, not the passwords |
| **a named stand-in** | agreed in advance | someone who could answer a client for a week |
| **the documents in this repo** | this repository | the business's memory is not in one head |

**INFERENCE:** three of those four cost nothing and take an hour. The third is the
one people avoid, because it requires admitting the business is one person.

---

## 4. Professional boundaries: the ones that are law, not preference

| Boundary | Legal or chosen | Consequence |
|---|---|---|
| Never hold a client's card details | **legal** — and `verify-claims.py` proves none exist in the code | fines, and personal liability |
| Never claim a result that was not measured | chosen | the verifier fails the build |
| Never take a client's account into your own name | chosen, and it is why the promise is credible | you cannot lose what you never held |
| Never process personal data without registration | **legal** (Act 843) | criminal |
| Never reuse a client's images elsewhere without permission | **legal** (Act 690) | infringement |
| Never tell a client a date you cannot hold | chosen | the only kind of reputation that compounds |

---

## 5. What changes this document

| Trigger | What must be revisited |
|---|---|
| **first employee or contractor** | SSNIT registration, PAYE, employment contracts — none of this is written yet, deliberately |
| **a portal or any login** | Act 843 becomes materially harder; backups become data; the retainer must rise |
| **turnover above GH₵200,000** | VAT registration |
| **a client who requires a registered company** | Companies Act route, GH₵585 + 1% |
| **selling the product, not the project** | terms of service, a refund policy, support levels |
| **a trademark filing** | Act 664 — see `BRAND.md` |

**INFERENCE — the last row is why governance matters now rather than later.** Every
trigger above is easier to meet from a business that already has a constitution, a
contract, a record system and a verifier. The point of writing them down while
there is one person and no clients is that they cost almost nothing today and are
nearly impossible to retrofit under pressure.

---

## 6. What I could not verify

| Unknown | Why it matters | Who answers |
|---|---|---|
| **Whether the 200-record threshold is real** | it would change whether registration is required now | **the DPC**, at registration |
| The actual DPC fee for a sole trader | reported range GHS 500–5,000 is too wide to budget | the DPC portal |
| Whether a "certified data supervisor" is required | one source says the DPC requires it though the Act does not | the DPC |
| Whether SoftFire counts as processing data through WhatsApp | likely yes; the threshold question is unresolved | the DPC |
| Whether a trading name can sign an enforceable contract | Act 25 is general; a sole trader contracts personally | a lawyer, before the first big job |
| The consumer-protection duties on a B2B service | not researched | a lawyer |
| Whether the Electronic Transactions Act makes a WhatsApp "yes" binding | probably, which is why the signature matters | a lawyer |

---

## 7. Sources

- **Data protection:** Data Protection Act, 2012 (Act 843) ss.27, 30, 31, 50, 53,
  55, 56 — full text at dataprotection.org.gh; DPC enforcement statements (GhanaWeb,
  Jan 2026; DPC/GNA, Oct 2026); 2026 compliance guides (recordinglaw.com,
  stackweaver.cloud, phoot.io, Lexology); fee and record-threshold reporting from
  jbklutse.com (May 2026) — **marked unconfirmed**.
- **Copyright:** Copyright Act, 2005 (Act 690) ss.7, 9(4), 9, 12 — text and
  commentary from Mondaq (May 2025), omaplex (Oct 2025), Afro-IP on the
  commissioner-owns default, and codelicenses.com on contractor ownership
  (Oct 2026).
- **Everything else:** this repository — `OPERATIONS.md`, `PRICING.md`,
  `MAINTENANCE.md`, `SECURITY-HOSTING.md`.
