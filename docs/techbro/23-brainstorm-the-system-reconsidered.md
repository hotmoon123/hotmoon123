# 23 — The Brainstorm: The System, Reconsidered

> **Status:** brainstorm, not specification. Everything here is either a correction to `01`–`22`, a new
> finding, or an open question. Nothing here is code, and nothing here is agreed until you say so.
>
> **Reading labels used throughout** (adopted from `22` §22.2):
> `[F]` verified fact with a source · `[S]` source claim, not independently verified ·
> `[I]` my interpretation · `[A]` assumption · `[D]` decision · `[?]` unknown, needs evidence.
>
> **Sources:** new claims registered as **S58–S62** in `tools/data/sources.yaml` and rendered in
> `99-sources-and-assumptions.md`. S58 (VAT Act 1151) is verified; S59–S62 are marked
> `verified: false` because they rest on vendor help pages or founder-reported figures.
>
> **The rule this document obeys:** when a statement cannot be supported, it is marked `[?]` or `[A]`
> rather than written as fact. Where the pack is wrong, it says so in §23.1.

---

## 23.1 First: three things I got wrong

You asked for a brainstorm that mines the files. Before mining them, three corrections — because two
of them change the design, and one of them is a legal fact that landed two months ago.

### Correction 1 — Ghana's VAT changed on 1 January 2026, and the pack says nothing about it

The Value Added Tax Act, 2025 (**Act 1151**) took effect **1 January 2026**. It replaces the old
regime with a **unified 20%** charge — VAT 15% + NHIL 2.5% + GETFund 2.5% on the same taxable value —
**abolishes the COVID-19 Health Recovery Levy**, raises the registration threshold for goods from
GHS 200,000 to **GHS 750,000**, and makes NHIL and GETFund **creditable as input tax** for the first
time. `[F]` **S58** (GRA public notice, reported Dec 2025–Feb 2026)

**Why this is not a footnote:** I searched the entire pack. `Act 1151` and `VAT` appear **nowhere**
in chapters `02`–`22`. My GHS 25 / GHS 120 CAC targets, my 8–12% take rate, my unit economics in §13
and §21 were all computed on a pre-2026 tax assumption. That is a real error and it is mine.

**The forced structural consequence** `[I]`, built on `[F]` Act 1151, Act 987 and S11:

| If TechBro acts as | Tax & legal position | Cash-flow capability |
| --- | --- | --- |
| **Agent** (facilitates, provider invoices client) | Commission is TechBro's service supply → VAT on the **commission only** (10% of GHS 10,000 = GHS 1,000 → GHS 200 VAT) | **Cannot hold client funds** — that is deposit-taking, Act 987, BoG licence |
| **Principal** (buys the work, resells it) | TechBro invoices the **whole job** → VAT on **GHS 10,000 = GHS 2,000** | Can hold funds, can guarantee, can absorb disputes — but carries the liability |

**You cannot have both.** Agent status keeps you 10× lighter on VAT and keeps you out of BoG
licensing; principal status buys you the escrow-like guarantee that makes trust possible. This is the
single biggest architectural fork in the business and it was not in the pack.

My recommendation `[D → needs your decision]`: **agent at launch, principal only for a narrow class of
"guaranteed" jobs later** (deploy/sustain retainers, §23.7), once volume justifies the licence
conversation. Do not use the word "escrow" in any T&Cs under either posture.

### Correction 2 — I designed the wrong product

Your own words, from the prompt: *"if i have a job and i can't do it or i need help i can go on the app
and find someone who can."*

That is **not** Upwork. It is **Codementor**. And Codementor was in none of the 57 sources and none of
the 12 competitors in `19`.

| | What it actually sells | Unit of transaction | Optimised for |
| --- | --- | --- | --- |
| Upwork, Fiverr, Toptal, Braintrust, Andela | a **durable contract** | weeks to months | deliberate purchasing |
| **Codementor** | an **interruption handled** | **15 minutes**, then per-minute | urgency |

Codementor facts: **$8–15 per 15 min** for newer mentors, **$15–30** for experienced; **15-minute
minimum**, per-minute after; platform fee **10–20%**; sessions by screen-share/video/text; most mentors
respond in **10–30 minutes**; site claims **12,000+** developers. `[S]` S59 (Codementor help centre via
MentorCruise/sefism; the 10–20% fee figure is from a 2015 Mashable piece — `[?]` current rate)

**This changes what the app is.** For 21 chapters I have been designing a hiring marketplace. Your
sentence describes an **emergency room**: someone is blocked, they need the specific person who
unblocks them, now, and they will pay by the minute.

Those two products have almost nothing in common operationally:

| | Hiring marketplace | Unblocking network |
| --- | --- | --- |
| Core question | *who should I hire?* | *who can fix this in the next hour?* |
| Supply side motivation | earn money | earn money **and** status, and find bigger clients |
| Matching signal | portfolio, reviews | **specific problem fingerprint** (stack + error + version) |
| Latency requirement | days | **minutes** |
| Session artefact | deliverable | **the fix, plus a written explanation** |
| Repeat behaviour | hire again | **ask the same person again** |

**My read `[I]`:** you are building the unblocking network and calling it a job marketplace. If that
is right, half of `10-ux-ui-design-system.md` is aimed at the wrong user. If it is wrong, say so and
§23.1 becomes a footnote instead of a re-architecture.

### Correction 3 — the competitive set was incomplete, and one entrant invalidates a strategy

Five competitors were missing from `19`, and they matter more than Upwork does, because they are
**operating in your market right now**:

| Entrant | What is verified | Why it matters to you |
| --- | --- | --- |
| **Codementor** | $8–30/15 min, 10–20% fee, 12k+ devs, global/USD `[S]` | The closest analogue to your actual idea, and it is **already 13 years old** |
| **Growwr** (Lagos, 2024) | AI crawler + behavioural interview + matching; **$1.5M paid out**, 3,000 businesses, 19,000 applicants → **1,100 vetted**, 13 countries incl. **Ghana (first customer)**; 8-person team `[S]` S60, founder claims | **Direct competitor with AI vetting, already in Ghana, already funded, already at 1,100 vetted supply** |
| **TERAWORK** (Lagos, 2018) | escrow + task management + review; 15,000 freelancers, 6,000+ transactions; has **iOS and Android apps** `[S]` S61 | Proof the full-stack marketplace is already built in West Africa — and proof it took 7 years |
| **Hamzry** (Nigeria, 2025) | naira-native, 1,800 freelancers at launch `[S]` S62 | Naira-native pricing is a real wedge you have not used |
| **CediJob** (Accra) | Ghana-first, Betaraise accelerator, pre-seed targeting $100k+ `[S]` S57 | Local incumbent; current operating status `[?]` |

**And one fact that kills a strategy I proposed:** Braintrust charges **0% to talent** `[F]` (S53).
You cannot win providers by charging them less than zero. Any pitch built on "lower fees for
developers" is dead on arrival. `[I]`

---

## 23.2 The reframe: you have two products and have been designing one

```
                 ┌──────────────────────────────────────────┐
                 │  THE BLOCK                              │
                 │  "I cannot finish this. I am stuck."    │
                 └───────────────┬──────────────────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌────────────────────┐          ┌────────────────────┐
      │  A. UNBLOCK        │          │  B. HAND OFF       │
      │  minutes           │          │  days–weeks        │
      │  "help me do it"   │          │  "you do it"       │
      │  screen-share      │          │  brief + milestones│
      │  Codementor's game │          │  Upwork's game     │
      └────────────────────┘          └────────────────────┘
```

Both start at the same place — **the block** — and that is the strategic asset. Almost every
marketplace starts with a *browse*, which needs liquidity on day one. A product that starts with
**"describe what is blocking you"** needs only *one* available human, and that is a business you can
run with 20 people instead of 20,000.

`[I]` **This is the strongest idea in the whole brainstorm:** the intake form is the product. Upwork
starts with search and needs a market. Codementor starts with a problem and needs one person.

### The "block" as the atomic unit

| Field | Why it is required |
| --- | --- |
| What are you trying to do | outcome, not symptom |
| What happened instead | the actual error, screenshot or log |
| Stack + versions | filters 80% of candidates instantly |
| What you already tried | prevents paying for advice you have |
| Deadline / urgency | sets price ceiling and matching window |
| Budget band | GHS 100 / 500 / 2,000 / open |
| Can you share your screen / repo | determines whether it is A or B |

Six fields, one screen, no account required to submit. `[D]`

---

## 23.3 The competitor teardown, extended — twelve dimensions, nine products

`19` covered five. This adds the four that were missing and reads all nine on the same axes.

| | **Upwork** | **Fiverr** | **Toptal** | **Braintrust** | **Codementor** | **Andela** | **Growwr** | **TERAWORK** | **CediJob** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Model** | open bidding | productised gigs | curated elite | open + vetted | **on-demand minutes** | staff augmentation | AI-vetted freelance | escrow marketplace | local marketplace |
| **Who pays** | both | both | client (markup) | client | client | client | client | client | client |
| **Take rate** | 0–15% talent `[S]`, ~5% client | 20% seller + 5.5% buyer | 30–50% markup | 0% talent / 10% client | 10–20% `[S]` | embedded | `[?]` | `[?]` | `[?]` |
| **Unit** | contract | gig | engagement | contract | **15 min** | 12-mo seat | project | task | task |
| **Time to first value** | days | hours | **2–8 weeks** | days | **10–30 min** | weeks | days | hours | hours |
| **Trust mechanism** | reviews + JSS | reviews + levels | **<3% acceptance** | vetting | rating + response time | **0.5% acceptance** | AI interview | escrow | `[?]` "basic" |
| **Dispute** | arbitration | resolution centre | account mgmt | `[?]` | **1-hour refund window** | account mgmt | `[?]` | escrow hold | `[?]` |
| **Supply source** | global | global | global elite | US-centric | global | Africa→enterprise | Africa | Nigeria | Ghana |
| **Cash control** | milestone | holds 14d | invoices | invoices | card auth | invoices | `[?]` | **escrow** | `[?]` |
| **Mobile** | strong | strong | weak | web | desktop-first | none | `[?]` | **has apps** | `[?]` |
| **Local fit (Accra)** | poor (USD, no MoMo) | poor | impossible | poor | poor (USD) | none (12-mo) | **partial** | **partial** | **high** |
| **Direction of failure** | disintermediation | quality ceiling | price ceiling | liquidity | **anonymity** | scope | scale | depth | funding |

### The three weaknesses that are actually openings

**Opening 1 — Codementor cannot verify context.** It matches on *stack*, not on *your* system. A mentor
who has never seen your codebase, your framework version, or your deployment is guessing alongside
you. And it is anonymous: you cannot know if they will be there tomorrow, or whether their "senior"
badge is real. `[I]` from `[S]`

**Opening 2 — TERAWORK proves the full stack, and proves it is slow.** They built escrow, tasks,
reviews and native apps — and after seven years have **6,000 transactions** `[S]` S61. That is roughly two
a day. **Building the full marketplace is not the bottleneck; liquidity is.** Anyone who tells you the
product is the moat is wrong.

**Opening 3 — Growwr proves the AI-vetting thesis, and shows the cost.** 19,000 applicants → 1,100
vetted = **5.8%**. With an 8-person team `[S]` S60. That is the real cost of a trust layer, and it is why
`[I]` **you should not build AI vetting first** — you should borrow trust (client's own network, other
people's references, visible artefacts) until you can afford to manufacture it.

### And the thing all nine get wrong

**None of them can answer "who in this city can unblock my Django 5.2 deployment at 9pm tonight, is
reachable on WhatsApp, and takes MoMo."** That sentence is not a feature gap. It is a different
product category, and it is the only gap where a two-person team in Accra has an advantage over a
$2B company. `[I]`

---

## 23.4 Eight failure laws of marketplace apps

These are not opinions about your app. They are the recurring causes of death across the nine above,
stated as laws so they can be tested.

**Law 1 — Liquidity dies on the short side.**
In an unblock network the short side is **verified seniors willing to be interrupted.** They are the
busiest and best-paid people in the market. `[I]` Cash alone loses to their hourly rate. What they will
accept instead: **status** (public proof they are the person who solved X), **pipeline** (a 30-minute
rescue that becomes a GHS 40,000 contract), and **reciprocity** (they get to ask too).

> **Design consequence:** the provider's reward must include *exposure to larger work*, not just fees.
> A "this session led to a contract" counter is worth more than a 1% fee cut.

**Law 2 — One dispute costs more than ten commissions.**
At a 10% take on a GHS 2,000 job the platform earns **GHS 200**. A single refund plus two hours of
support costs **GHS 1,500+** — **7.5 jobs of margin.** `[I]` arithmetic.

> **Design consequence:** dispute prevention is the business model, not a support function. Every
> screen that prevents a mismatch is worth more than every screen that resolves one.

**Law 3 — Disintermediation is the default, not the exception.**
WhatsApp makes it one tap. The moment two people have each other's numbers, the platform must *keep
earning* its fee monthly. Upwork fights this with Connects and escrow; Fiverr fights it by owning the
buyer.

> **Design consequence:** never let the intro be the product. The product must be the **record**
> (proof of work, verified outcome), the **money** (only route to a protected payment), and the
> **repeat** (the person you used last time, one tap away). `[D]`

**Law 4 — An empty room is permanent.**
50 providers and 3 clients reads as "dead" and never recovers. `[I]` from every failed marketplace.

> **Design consequence:** launch with **one cell, one city, one problem class**, and make it look full.

**Law 5 — Ratings inflate until they carry no information.**
Upwork/Fiverr both compress toward 4.8–5.0. A score everybody has does not discriminate. `[I]`

> **Design consequence:** do not ship ratings. Ship **binary, specific, retrievable evidence**:
> "solved a Django migration error in 22 minutes, verified by the requester" beats 4.9 stars.

**Law 6 — The generalist marketplace is a 20-year, billion-dollar business.**
Upwork is general and wins because of two decades and enormous capital. Growwr, 8 people, is
**Africa-focused and AI-vetted**, not general. `[S]` + `[I]`

> **Design consequence:** "all SDLC roles" is the **coverage ambition** (correct, `01` does it with 300
> rows). It must not be the **launch surface**. Launch shows ~12 roles. `[D]`

**Law 7 — Cross-platform mobile doubles cost before it halves friction.**
Every marketplace above is **web-first for supply** because professionals onboard on desktop, and
mobile-first for demand because buyers browse on phones.

> **Design consequence:** your "cross-platform mobile app" is right for the *buyer*. It is probably
> wrong for the *first 50 providers*. `[D → challenge]` Ship buyer-mobile + provider-web + the same
> backend. The React Native app is not the risk; building two polished surfaces with a 4-person team
> is.

**Law 8 — You cannot undercut zero.**
Braintrust is 0% to talent `[F]`. Any "we charge developers less" positioning is already beaten.

> **Design consequence:** charge the **client** — confirmed again in `19` — and never make fee
> comparison the pitch. Make **unblocking speed** the pitch.

---

## 23.5 The seven shapes of work (replacing "the job")

You asked for all jobs, works, tasks, titles, inputs, outputs. `01` gives 300 roles and 110 artefacts.
What it does **not** give is the **commercial shape** — and shape is what determines whether a
marketplace transaction can exist at all. There are only seven shapes:

| # | Shape | Duration | Buyer | Verifiable by | Example | Marketplace fit |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | **Unblock** | 15 min–4 h | the blocked dev | "it works now" | deployment failing, auth bug | **excellent** |
| 2 | **Fix** | 1–5 days | business owner | defect closed | "checkout is broken" | **excellent** |
| 3 | **Build** | 2 weeks–6 months | founder / company | acceptance criteria | "build me the MVP" | good, high value, high risk |
| 4 | **Review** | 1–3 days | founder / CTO | written findings | code audit, security review | **excellent** |
| 5 | **Maintain** | monthly | business owner | uptime, tickets | retainer | **excellent, recurring** |
| 6 | **Advise** | 1 h | founder | their own judgement | architecture call | good, low value per unit |
| 7 | **Staff** | 3–12 months | company / agency | performance | embedded engineer | **terrible at launch** |

**The insight `[I]`:** shapes 1, 2, 4, 5 are all shippable by a small team, all verifiable by a
non-technical buyer, and all currently served badly. Shape 3 is where the money is but where trust
fails. Shape 7 is Andela's business and needs a sales team you do not have.

**And note what this does to the 300 roles:** they are not 300 products. They are 300 *labels on seven
shapes*. A "Kubernetes SRE" and an "Accessibility Auditor" sell shape 1 sometimes, shape 4 mostly, and
shape 5 always. That is the entire mapping problem, and it is solvable in one table. `[D]`

---

## 23.6 The SDLC map — where deals actually form

You asked for all SDLC stages. Here is every cell scored on the three things that decide whether a
two-sided transaction can exist: **is money already being spent**, **is the output verifiable**, and
**is the buyer non-technical**.

| Cell | Deals form? | Output verifiable? | Buyer non-technical? | Recurs? | Verdict |
| --- | --- | --- | --- | --- | --- |
| `discover` | rarely — internal | no | no | no | ✗ |
| `define` | sometimes (BA, spec) | yes | sometimes | no | ○ |
| `architect` | yes | hard (opinion) | no | no | ○ |
| `build` | **yes — largest** | yes | **yes** | no | ✓✓ |
| `assure` | yes (QA, pen-test) | **yes** | sometimes | no | ✓ |
| `secure` | yes (audit, remediation) | yes | sometimes | no | ✓ |
| `deploy` | yes | **yes** | **yes** | yes | ✓✓ |
| `sustain` | **yes — constant** | **yes** | **yes** | **yes** | ✓✓✓ |

**The wedge `[I]`, recommended for your consideration:**

> **Sustain + Deploy. "Your thing is broken or your thing won't go live."**
>
> Because it is the only cell where all four conditions hold at once: the buyer is a **non-technical
> business owner**, the pain is **urgent**, the fix is **objectively verifiable**, and it **recurs
> every month**. It is also the work local dev shops hate — 9pm hotfixes, domain/DNS pain, expired
> certificates, "the server is down" — which means **supply is available and affordable.**

This is a real strategic change from the pack, which framed the wedge as export-first (`thesis A local
trust, then B export`, §19.11). Sustain is a **better entry wedge** because it produces the thing
export needs: a record of verified repairs on real businesses.

And it is testable in ten days with no app at all.

---

## 23.7 The evidence gate: how you prove "senior" without interviews

Every one of these platforms struggles with the same lie: people claim seniority and cannot prove it.
Growwr's answer is an AI behavioural interview — 19,000 → 1,100, and an 8-person team. `[S]`

**The pack already contains the answer and I did not notice it.** `01-role-catalog.md` defines **110
artefacts** with owners and definitions of done. That is not a documentation exercise — **it is a
verification instrument.**

> **Gate:** you may not claim a capability until you have produced its artefact, or can show someone
> else's you contributed to.

| Claim | Proof accepted | Not accepted |
| --- | --- | --- |
| "I do backend" | a repo, an ERD, a migration file, a deployed endpoint | a CV line, a bootcamp certificate |
| "I do security" | a redacted report with findings and remediation | "I know OWASP" |
| "I do design" | 3 screens with states, plus the token file | a dribbble shot |
| "I am senior" | someone else's attestation + 5 closed jobs | years of experience |

`[I]` This is cheap, unfakeable, and it makes `01` load-bearing instead of decorative. It is also the
one thing Codementor structurally cannot do, because it is global and anonymous.

**The redefinition worth arguing about:** seniority is not years, it is **"has resolved this class of
block before, and someone says so."** `[D]`

---

## 23.8 The two currencies: trust and attention

Marketplaces distribute one currency (money). This product distributes three, and mismanaging the
other two is why competitors feel transactional.

**Attention** — the scarce resource is a senior's *interruptibility*. It must be budgeted like money:
a senior sets "I accept 2 interruptions a week, ≥GHS 150, evenings only". That is a **calendar of
availability**, not an "online" dot. `[D]` Codementor's "response in 10–30 min" `[S]` S59 is the right
metric implemented the wrong way — it is an average, not a promise.

**Trust** — must be *portable* and *specific*, not a star. Three trust objects, in order of value:

1. **Attestation** — a named human vouches for a capability. Highest signal, hardest to fake.
2. **Verified outcome** — "this session ended with the build passing, confirmed by the requester."
3. **Composite reputation** — only after ~20 verified outcomes, and never as a single number.

`[D]` Launch with 1 and 2 only. Law 5 says a rating with no history behind it is noise.

**Status** — deliberately ninth. Badges are the cheapest thing to fake and the fastest to inflate.

---

## 23.9 Money: the four flows that must be decided before any screen

| Flow | Question | Options | My recommendation |
| --- | --- | --- | --- |
| **Capture** | who receives the client's money? | Paystack/Flutterwave/Hubtel split · direct MoMo to provider · platform account | **Paystack split** (S11): 1.95% local, GHS 1 payout, T+1 |
| **Timing** | when does it move? | on acceptance · on completion · on dispute close | **on requester confirmation**, auto-confirm after 72h |
| **Tax** | who bears the 20%? | absorb · pass to client · pass to provider | **pass to client explicitly**, shown as a line item |
| **Fee** | who pays TechBro? | client · provider · both | **client only** (Braintrust already beats 0% for talent) |

### The number that actually decides the business

Take a GHS 2,000 sustain job at a 10% client fee, agent posture:

```
Client pays            2,000.00
  TechBro fee (10%)      200.00
  VAT on fee (20%)        40.00   ← Act 1151, on the commission only
  Client total         2,040.00
Provider receives       2,000.00
  Paystack (1.95%)        39.00
  Payout                   1.00
  Provider net         1,960.00
TechBro gross             200.00
  less VAT                -40.00
  less Paystack           -40.00
  less support ~0.5h     -50.00   ← GHS 100/h fully loaded
TechBro net              70.00   ← 3.5% of GMV, not 10%
```

`[I]` arithmetic on `[F]` rates. **Every take-rate number in §13 and §21 was gross. Net is roughly a
third of gross.** At GHS 70 net per job, covering GHS 25 CAC and a 4-person team means roughly **285
jobs a month just to break even on support.** That is the real number the plan has to survive, and it
is why shape 5 (maintain, recurring) matters more than shape 3.

**I would not want you to discover this in month nine.** `[D]` Re-base §13 unit economics on net, not
gross.

---

## 23.10 Screens: 42 was wrong, 28 is still too many, the answer is 9

`10-ux-ui-design-system.md` specifies 42 screens. Concierge phase needs no app at all.

| Phase | What exists | Screens |
| --- | --- | --- |
| **0 — Concierge** (weeks 1–4) | a form, a WhatsApp thread, a payment link, a receipt | **0** |
| **1 — Unblock** (weeks 5–12) | block intake · matched provider · session · pay · confirm · proof | **9** |
| **2 — Sustain** (month 3–6) | + retainer, availability calendar, ticket list | **+8** |
| **3 — Hand off** (month 6+) | + brief composer, milestones, dispute | **+11** |

**The nine for phase 1** `[D]`: `Block (describe)` · `Block (review)` · `Match (who can)` ·
`Provider profile` · `Session (chat/screen)` · `Pay` · `Confirm outcome` · `Proof (the record)` ·
`Your history`.

Everything else — settings, notifications, onboarding tour, ratings, portfolio, search, filters,
categories, saved items — is **phase 3 or never**. `[D]`

**And one design constraint the keywords file makes non-negotiable:** 390px first, 44px targets, one
filled button per screen, skeleton not spinner, errors name the cause and give one move. On a low-end
Android over 3G in Accra, that is not taste — it is whether the app works. `[F]` from `keywords.pdf`

---

## 23.11 Offline-first is not a feature, it is a correctness requirement

I found one genuinely important thing buried in `prompter.md` (§23, line 102,351 of the concatenation):
the phrase *"this is where your offline-first requirement becomes important"* — in a document about a
different app. It is the right question for this one.

`[I]` The failure mode is not "no internet". It is:

1. A session is logged on a flaky connection and the transcript is half-lost → **the proof of work,
   which is the product, does not exist**.
2. A provider marks a job complete and the write is lost → payment never releases → **trust collapses
   on the first bad network**, which in Accra is Tuesday.
3. A requester confirms and the double-tap sends twice → **the invariant breaks.**

**Design consequences** `[D]`: local-first writes with an outbox, client-generated idempotency keys on
every money action, transcripts stored locally and synced, and a visible "unverified sync" state
rather than a silent failure. This is the single most under-designed area in the pack.

---

## 23.12 AI: five uses that pay, and the one you must refuse

You asked for AI efficiency. Concretely, ranked by value per unit of risk:

| # | Use | Why it pays | Risk | Gate |
| ---: | --- | --- | --- | --- |
| 1 | **Block → structured brief** | turns a panicked paragraph into stack/version/symptom/tried; the highest-value transformation in the product | misreads and mis-routes | human confirms before match |
| 2 | **Match routing** | SQL/rule-based first (already decided in `07`) | none at v0 | must be explainable |
| 3 | **Session → written record** | turns a fix into the proof artefact + reusable knowledge | hallucinated steps | provider approves before publish |
| 4 | **Scam & off-platform detection** | protects the 10% | false positives ban good users | human review queue |
| 5 | **Price band suggestion** | reduces the #1 negotiation failure | anchoring bias | show a range, never a single price |

**The refusal** `[D]`: **do not let AI decide who gets paid, who is trusted, or who is banned.** Those
are the three decisions where an unexplainable error ends the company. `07` already forbids learned
ranking before 2,000 completions — extend that rule to every trust decision, permanently.

Growwr's AI behavioural interview `[S]` S60 is the cautionary tale: 19,000 → 1,100 is a 94.2% rejection
rate that a model produced and a human has to defend. At your size you cannot afford to defend it.

---

## 23.13 What to cut (the kill list, extended)

Additions to `03` §3.12's kill criteria:

| Cut | Why | When it can return |
| --- | --- | --- |
| 300 roles visible | Law 6 | never as a list; only as a search result |
| star ratings | Law 5 | after 20 verified outcomes per provider |
| video calls | bandwidth cost, not value | phase 3 |
| portfolios / dribbble feeds | browse-first, contradicts the intake thesis | never |
| AI vetting | 5.8% pass rate needs a team you do not have | after 500 verified outcomes |
| multi-currency | adds VAT and FX to every invoice | after first export client |
| enterprise / teams | needs sales | month 12+ |
| staff augmentation (shape 7) | Andela's game | year 2, maybe never |
| provider mobile app | Law 7 | after 50 providers ask |
| general "find a freelancer" search | the thing every competitor already does | — |

---

## 23.14 The 90-day test, rewritten for the new wedge

| Days | What | Success gate |
| --- | --- | --- |
| 1–10 | **20 interviews** with business owners whose site/app is broken or not live | ≥10 describe the same pain unprompted |
| 11–20 | **Run 5 sustain jobs by hand.** WhatsApp, MoMo, you personally. No app. | 5 paid; ≥3 finished; ≥1 repeat |
| 21–30 | **Write the block-intake form.** Nine fields. It is the product | 80% of submissions need no follow-up question |
| 31–50 | **Recruit 12 providers** with artefacts, not interviews (§23.7) | 12 verified; 6 accept a job |
| 51–70 | **One cell, one city.** Sustain only. Instrument every step | median time-to-unblock < 4 h |
| 71–90 | **Decide:** does the record produce a second job? | ≥30% repeat within 30 days |

**Kill it if** — after 5 paid jobs, fewer than 2 requesters return, or median time-to-unblock exceeds
24 hours, or you cannot get 6 of 12 verified providers to accept work. `[D]`

---

## 23.15 New risks this brainstorm adds

| ID | Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- | --- |
| R-30 | VAT reclassification (agent → principal) forces a re-price | med | **high** | written opinion before launch; agent posture |
| R-31 | Growwr or TERAWORK enters Accra sustain with existing supply | med | high | speed, local payment, WhatsApp-native |
| R-32 | Verified seniors will not accept interruptions | **high** | high | status + pipeline reward (§23.4 L1) |
| R-33 | Offline write loss destroys proof-of-work | med | **high** | outbox + idempotency (§23.11) |
| R-34 | Net take rate ~3.5% makes the model unviable | **high** | **high** | re-base unit economics on net (§23.9) |
| R-35 | Anchoring to $2–10/h Accra rates suppresses price | high | med | never compete on price; price the *block* |
| R-36 | Dispute at 7.5 jobs of margin | med | high | prevention-first design (Law 2) |

---

## 23.16 What I could not verify — the honest list

| Claim used | Status | Why it matters |
| --- | --- | --- |
| Codementor's current take rate | `[?]` 10–20% is from 2015 | if it is now 20%+, your pricing ceiling changes |
| CediJob is still operating | `[?]` no 2026 evidence found | your closest local competitor may be dormant |
| Growwr's $1.5M / 3,000 businesses | `[S]` founder claim, no audit | do not treat as market size |
| TERAWORK's Ghana volume | `[?]` | 6,000 transactions is all-time, all-country |
| VAT treatment of a marketplace commission | `[?]` needs a Ghanaian tax practitioner | §23.9 could be wrong by a factor |
| Whether Act 1151's threshold applies to *services* at GHS 750,000 | `[?]` reports state "goods" | changes when you must register |
| ISO/IEC/IEEE 29148 edition cited by `prompter.md` | `[?]` not checked this session | do not quote an edition number |

**Stopping here rather than filling these in.** Every one of them is answerable by a human in Accra
this week, and none of them is answerable by me without inventing.

---

## 23.18 Correction 4 — the "300 roles" claim does not cover the roles you named

I audited `01-role-catalog.md` against the role list in your own prompt. This is the result and it is
not good.

### What is true

The generator validates **structure**: 300 ids D001–D300, no duplicates, no gaps, every role has an
output, every artefact has an owner. That is what `ok: 300 roles` means. **It has never validated
coverage** — whether the catalogue contains the roles you actually asked for.

### What is false

Of the **57 distinct roles you named by hand**, the catalogue covers **39** and **misses 18**:

| Missing role | Why it matters here |
| --- | --- |
| **System Analyst** | a core SDLC function you named twice |
| **System Designer** | you named it — and it is the discipline this whole project is |
| **Software Developer / Engineer** (generic) | only the specialisations exist; the generic title does not |
| **Information Security Engineer** | distinct from Security Engineer, and you named it |
| **Cybersecurity Engineer** | you named it; only `Security Engineer` exists |
| **System Administrator** | the person who actually runs small-business servers — a **sustain-wedge** buyer and seller |
| **Electrical/Electronics Engineer** | you named it |
| **Computer Architect** | you named it |
| **Systems Engineer** | you named it (only `Systems Analyst` exists) |
| **System Thinker** | you named it as a discipline |
| **Mathematician** | you named it |
| **Psychologist** | you named it |
| **Physician** | you named it |
| **Reverse Engineer** | you named it |
| **Change Manager** | ITIL core role — central to the sustain wedge |
| **Problem Manager** | ITIL core role — the role that owns recurring breakage |
| **Business Manager** | only `Business Architect` exists |
| **Business Administrator** | only `Business Architect` exists |

The honest position: **39/57 named roles covered = 68%**, and the pack's headline "300 roles" is a
*structural* achievement, not a *coverage* one. I wrote it as coverage. That was an overclaim, and it
is the same class of error I criticised in `22` §22.5 — **size presented as completeness.**

### Why this is not cosmetic

`Physician`, `Mathematician` and `Psychologist` are in your prompt because you want the **reasoning
disciplines**, not the medical profession. That is legitimate — but it means they are **lenses**, not
**marketplace roles**, and they belong in a different table. Mixing lenses into a job catalogue is what
made the gap invisible: a list that mixes jobs, disciplines and lenses **cannot be audited for
coverage**, because there is no definition of what "complete" means.

### The fix, in two parts

**Part 1 — separate three kinds of row.** The catalogue conflates them:

| Kind | Definition | Approx. today | Belongs in |
| --- | --- | ---: | --- |
| **Marketplace role** | someone who can be hired on the app | ~250 | `01` catalogue |
| **Discipline / lens** | a way of thinking applied to the work | ~35 | a new `disciplines` table |
| **Internal operator** | someone TechBro itself employs | ~15 | `14` team plan |

**Part 2 — register the gaps.** 18 named roles are now logged as **coverage gaps** instead of being
silently absent. Closing them is either a 20-minute data edit (`D301`–`D318`) or an explicit decision
that a role is a lens, not a job. **I have not added them yet** — that is a decision about what the
product sells, and `23.6` says the launch surface is 12 roles, not 318.

### The methodological lesson, which is the real output

> **A generator that says "ok" is validating the shape of the data, not the truth of the claim.**

`gen_blueprint.py` will report `ok: 300 roles` for a catalogue of 300 roles even if all 300 are wrong.
Structural validation and coverage validation are different instruments, and I only ever built the
first. Any future completeness claim must be tested against **your own words**, not against the file's
self-consistency.

---

## 23.18 Correction 5 — the one law I quoted and then broke in the same document

`THE_SEVEN_LAYERS.md` ends with **ten laws** and one of them indicts this pack:

> **Law 7 — "The business rules belong in exactly one place — the domain. Everywhere else is a caller,
> not a decider."**

`23` §23.11 said the same thing in different words: *"offline-first is a correctness requirement."*
`23` §23.9 said the money rules are a four-way decision. And then the pack distributed those rules
across **three UI clients** — React Native, a web app, a marketing site — with no single place that owns
them. That is the exact failure the law names, and I wrote it down and then ignored it.

### The architectural consequence, stated once

```
                 ┌─────────────────────────────────────────┐
                 │  DOMAIN  (Django)                       │
                 │  money · state · permissions · pricing  │
                 │  the ONLY decider                       │
                 └───────────────┬─────────────────────────┘
                                 │ typed contract (OpenAPI)
        ┌────────────────────────┼────────────────────────┐
        ▼                        ▼                        ▼
  React Native            Web client                Admin console
  (buyer)                 (provider onboarding)     (you, at 30 jobs)
  offline-capable,        no local rules,           no local rules,
  but never a decider     never a decider           never a decider
```

**Three rules, non-negotiable** `[D]`:

1. **No client computes a price, a fee, a payout, a tax amount, or a state transition.** It displays
   what the server said, or it says "unknown".
2. **Every money action carries a client-generated idempotency key** and is safe to retry by
   construction — because on a 3G connection in Accra, retry is not an edge case.
3. **Offline queue holds intent, never decisions.** A queued action says "the user wants X". The server
   decides whether X is still legal when the queue drains — a state re-check on arrival, not a replay.

`[I]` Point 3 is the one that is usually missed. Replaying an offline queue *optimistically* (applying
the stored decision on reconnect) is how a provider marks a job complete twice, gets paid once, and
opens a dispute the platform loses. Offline-first means **the user's intent survives the network**, not
that the client's decision survives it.

### And the second correction this batch forces

`THE_COMPLETE_STACK.md` §9 contains the SDLC role table — and it lists **23 roles**, including one
printed **twice** (Engineering Manager / Tech Lead). That duplication is a small thing. The real
question it forces is the one `23.18` dodged:

> **Why does `23` §23.6 recommend launching on roughly 12 roles when `01` catalogues 300?**

Because a catalogue, a launch surface, and a hiring market are three different graphs:

| Graph | What it is | Size | Changes |
| --- | --- | ---: | --- |
| **Coverage catalogue** | every role the system can *describe* | 300 | rarely |
| **Launch surface** | roles that appear in the app *today* | **12** | per cell, per city |
| **Liquidity graph** | roles where you have ≥3 available providers | **starts at 1** | hourly |

**The 12 launch roles, named** `[D]` — chosen because they are the ones the sustain wedge
(`23` §23.6) actually transacts, and because you can recruit them in Accra this month:

`D099 Backend Developer` · `D098 Mobile App Developer` · `D102 Frontend Web Developer` ·
`D104 Database Administrator (Production)` · `D091 DevOps Engineer` · `D110 Networking & Connectivity Engineer` ·
`D096 Security Engineer` · `D107 QA Automation Engineer` · `D223 On-call & Incident Manager` ·
`D052 Technical Writer` · `D105 Mobile UX/UI Designer` · `D114 Configuration & Environment Manager`

Every other role stays **searchable but unstaffed** — visible, honest about availability, and a
waiting list rather than a promise. That is the difference between a catalogue and a lie.

---

## 23.19 The whole brainstorm in eleven lines

1. You described an **unblocking network**, not a hiring marketplace — and Codementor, not Upwork, is
   the comparable. `[I]`
2. Ghana's **VAT changed to 20% on 1 Jan 2026**; the pack never accounted for it. `[F]`
3. Agent vs principal is a **forced choice**: cheap tax or held money, never both. `[I]`
4. **Growwr already runs AI-vetted African freelance in Ghana** with 1,100 vetted people. `[S]`
5. **You cannot undercut Braintrust's 0% talent fee.** Charge the client, sell speed. `[F]`
6. **Sustain/deploy is the wedge** nobody owns and the only cell that is urgent, verifiable,
   non-technical and recurring. `[I]`
7. There are **seven commercial shapes**, not 300 products. Map the 300 roles onto them. `[D]`
8. The **110 artefacts in `01` are the verification instrument** — proof, not paperwork. `[I]`
9. **Nine screens**, not 42; **zero** for the first month. `[D]`
10. Net take is **~3.5%, not 10%** — re-base the economics before building anything. `[I]`
10b. **The "300 roles" claim misses 18 of the 57 roles you named by hand** — structural validation is
    not coverage validation, and I presented one as the other. `[F]` §23.18
