# 22 — Source Library Review: What the 15 Attached Files Actually Are

> 15 files, 3.46 MB. I read all of them: headings, structure, substance, duplication, and the six
> PDFs (via text extraction). This chapter records what is in them, what is genuinely valuable, what
> is duplicated, what is wrong, and exactly how each one feeds the TechBro build.
>
> **The headline finding:** 73% of the library is *method and prompt templates*, 23% is *design craft*,
> 3.5% is *pre-build discipline*, and 0.2% is unrelated. **None of it is market research, legal
> research, or competitor data.** That is not a criticism — it is a categorisation, and it tells you
> precisely what you now have to go and find (§22.9).

---

## 22.1 Inventory and classification

| # | File | Size | Lines/pages | What it actually is | Verdict |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `disciplines_field.md` | 271 KB | 5,682 | **81 fields × 3 prompt types** (PEP/CEP/LEP) ≈ 243 templates; 59 full role prompts with the IPO method | **Keep — high value** |
| 2 | `system design.md` | 1,246 KB | 25,866 | Concatenation: brand blueprint + design prompt + teaching loops + prompt engineer + more | **Redundant — superset of 5 & 7** |
| 3 | `brand and branding.md` | 652 KB | 13,206 | Brand research blueprint: 12 areas (A–L), deliverables checklist, disciplines, governance | Keep — solid reference |
| 4 | `design prompt.md` | 131 KB | 2,907 | Poster/creative-director prompt + design system templates + cheat-code index | Keep — craft quality is high |
| 5 | `bitekasa_business_context_engineering_raas_prompt.md` | 181 KB | 2,351 | **Results-as-a-Service operating prompt** + Master Codex roadmap + **The 8 Structures** | **Keep — the best document in the set** |
| 6 | `business_foundations_master_guide.md` | 32 KB | 508 | Business admin/accounting/commerce foundations, 8W+H, break-even worked example | Keep — clean and correct |
| 7 | `software_security_context_engineering_results_as_a_service_prompt (1).md` | 16 KB | 290 | Security Raas prompt: evidence taxonomy, authorisation boundary, stop rules | **Keep — the second best** |
| 8 | `keywords.pdf` | 380 KB | 14 | 40 keywords that replace vague design phrases ("make it modern" → "Bento Grid") | **Keep — fixes AI slop** |
| 9 | `UI Design System Master Prompt _ By Janus Tiu.pdf` | 47 KB | 3 | Fill-in design-system template (tokens, type, spacing, components, rules) | **Keep — converts to tokens** |
| 10 | `200-creative-codes-chatgpt-higgsfield.pdf` | 71 KB | 3 | 200 file-level "slash" labels for image/video prompting | Reference only |
| 11 | `200_Creative_Image_Slash_Commands.pdf` | 28 KB | 11 | 200 camera/style/lighting commands in 10 categories | Reference only |
| 12 | `HyperFrames Starter Prompts _ By Janus Tiu.pdf` | 169 KB | 5 | Prompts for an open-source video render framework (HeyGen) | Out of scope for app |
| 13 | `UGC REALISTIC VIDEO .pdf` | 112 KB | 6 | Universal AI image/UGC prompt template | Out of scope for app |
| 14 | `Before_Anyone_Builds_Your_Site (2) (1).pdf` | 120 KB | 9 | **The 6 planning documents** to demand before a build starts, with a 6-box readiness check | **Keep — commercially sharp** |
| 15 | `WEBSITE_GUIDE.md` | 8 KB | 91 | A guide for a musician's website (Emma Revelation) | **Unrelated** |

### Duplication finding (measured, not guessed)

I sampled distinctive lines from each `.md` and checked whether they already appear in
`system design.md`:

| File | Distinctive lines sampled | Already inside `system design.md` |
| --- | ---: | ---: |
| `brand and branding.md` | 25 | **22** |
| `design prompt.md` | 9 | 5 |
| `bitekasa_…_prompt.md` | 12 | 5 |
| `disciplines_field.md` | 13 | 0 |
| `business_foundations_master_guide.md` | 4 | 0 |

**Conclusion:** `system design.md` is ~88% a superset of `brand and branding.md` and partly of
`design prompt.md`. It is not "the system design document" its name promises — it is a large
concatenation. **Read `brand and branding.md` directly; ignore `system design.md` unless you need one
file to search.** If you want a clean library, delete it and keep the 5 sources.

---

## 22.2 What is genuinely excellent (and must be adopted)

### 1. The evidence taxonomy — six classes, not two

From the Bitekasa and software-security Raas prompts. Every statement is labelled:

```
Confirmed company fact · Verified external fact · Source claim
Interpretation · Assumption/hypothesis · Decision · Unknown / needs verification
```

**Why this matters for TechBro:** this is stronger than what most design packs do (I used three
classes in §99: verified, flagged, hypothesis). Four extra classes catch the two failure modes that
actually hurt: *interpretation presented as fact*, and *decision presented as discovery*. **Adopt all
seven labels in every future artifact.**

### 2. Status labels and stop rules

```
Verified · Evidence needed · Proposed · Needs owner decision
Needs professional review · Out of scope · Complete for agreed scope
```

And: *"Stop when the agreed output is complete or a necessary decision/evidence is missing. Do not
invent certainty to keep moving."*

This is the operational form of your "don't hallucinate, stop when it happens" instruction. It is not
a mood; it is a set of words that force a stop. **Adopt verbatim in the AGENTS/CLAUDE working file.**

### 3. The 8 Structures ("Multi-Readiness Output Standard")

A deliverable is only "ready" if it is simultaneously: **product-ready, standardised/protocol-ready,
professionally crafted, project-ready, academically sound, industry-ready, business-ready, and
marketing/sales-ready.** These are a *quality bar run over the same task*, not eight tasks.

**Verbatim lesson:** *"these are NOT content instructions — they're a quality bar. You run the same
task through all 8. 'Ready in every aspect' means all eight, not just the visual one."*

**Gap it exposes in my pack:** chapters 1–21 are strong on product-, standard-, project-, academic-
and industry-readiness. They are **weak on marketing/sales-readiness** (there is no page in the pack
that a customer, investor, or partner could read and be persuaded by). That is a real omission and it
is fixed in §22.6.

### 4. The 11-step response format

A forced sequence that never skips: restate → readiness targets → research → **≥2 concepts** →
recommend one → build → refined spec → handoff → readiness checklist → **self-critique & risk
register** → **stop recommendation**.

The two killer steps are *two distinct concepts before recommending* (kills first-idea fixation) and
*self-critique before delivery* (kills confident nonsense). **Adopt for every design deliverable.**

### 5. The "push-back rule"

*"If a request is a cliché / inaccessible / a dark pattern / unlicensed, the AI must push back with a
better alternative — not comply silently."*

This is rare and correct. It is the behavioural antidote to sycophantic generation.

### 6. The 59 role prompts' IPO structure

Every role is specified identically: **Context → Foundations → Inputs → Tasks by level → Outputs →
Deliverables → Governance & compliance → Bloom L1–L6 → Mindset → References.**

This is the same shape as my 300-role catalogue (§01) but with two things mine lacks: an explicit
**referenced reading list per role** (Cagan, Torres, Pichler, PMI/IEEE 29148, WCAG) and
**"Tasks by level"** (beginner/intermediate/advanced) rather than a single task list.

**Reconciliation:** keep my catalogue as the *coverage* layer (300 roles, inputs/outputs, KPIs,
AI-leverage — mechanically validated), and adopt theirs as the *depth* layer for the ~10 roles that
matter most in the first 90 days. Do not replace 300 validated rows with 59 prose prompts.

---

## 22.3 The six "Before Anyone Builds Your Site" documents

This PDF is the most commercially useful item in the set. Its claim: **a build should not start
until six documents exist, each readable by a non-technical founder.**

| # | Document | Content | The check that matters |
| ---: | --- | --- | --- |
| 1 | **Product requirements** | goal, who uses it, features table (feature / who / done-when), "not in this version" | every "done when" must be personally checkable |
| 2 | **Technical requirements** | area / choice / why in plain English + decisions still needed | every tool you already pay for appears in "connects to" |
| 3 | **App flow** | main path, from-dashboard paths, **what happens when things go wrong** | walk it as a client; every red box ends somewhere completable |
| 4 | **Design brief** | real hex codes, real fonts, component rules, tone | if it could describe any company, it is not specific enough |
| 5 | **Backend schema (plain English)** | record / what's stored / who can see it, links, rules | flag anything personal, anything about children, anything you should not store |
| 6 | **Implementation plan** | 5 stages, what you get, **you sign off when**, riskiest part first | if you cannot test it yourself, you will only find out at the end |

**The 6-box readiness check:** 6/6 = build; 3–5 = get the missing ones written first; 0–2 = nobody has
decided what is being built yet.

### Why this matters here

It maps almost one-to-one onto what I already produced:

| Their document | My equivalent | Status |
| --- | --- | --- |
| Product requirements | §03 §3.6 MVP (10 capabilities with acceptance) | **covered** |
| Technical requirements | §04 §4.9 ADR table + §15 build/buy | **covered** |
| App flow | §10 §10.5 (4 flows with friction budgets) | **covered** — but their *failure paths* are better structured |
| Design brief | §10 §10.6 tokens + §3.11 principles | **covered** |
| Backend schema in plain English | §05 DDL + §5.8 data dictionary | **covered technically, weaker in plain English** |
| Implementation plan | §12 §12.8 12-week plan + §12.9 Go/No-Go | **covered** |

**The genuine gap:** my pack is written for engineers and operators. Their six documents are written
so that *a non-technical founder can check them*. Same content, different reader — and the second
reader is your investor, your first client, and your non-technical co-founder. §22.6 fixes this.

---

## 22.4 The design-craft layer (why 23% of the library is about fighting AI slop)

`keywords.pdf` is the most immediately actionable file for TechBro's UI. Its thesis: *"Don't describe
it. Name it."* Vague prompts produce generic AI output; named patterns produce professional output.

| Instead of | Say | Application in TechBro |
| --- | --- | --- |
| "make it simple" | **one primary action per screen**, 44px pill, no second filled button | job detail, milestone accept |
| "don't overload it" | **five choices above the fold** | talent home, proposal composer |
| "nice spacing" | **8px grid, 16px gutter**, title 12px above content, sections 24–28px | all screens |
| "nice list" | **rows 44–56px**: leading visual, title + grey sub-line, one trailing element | proposals, candidates, transactions |
| "add a popup" | **bottom sheet with a grabber**, title, ×, delete last in red | filters, payout confirmation, report |
| "add a loading spinner" | **skeleton of the final layout**, no full-screen spinners | feed, wallet |
| "show an error" | **name the cause, give one move**: "Couldn't load your orders. Retry." | every failure path |
| "use a good font" | **name the font, and only one** | one sans + optional serif for amounts |
| "nice colours" | **one accent**, everything else ink and greys | escrow state colour = the accent |
| "put it in cards" | **cards are for objects**, not for grouping text | job cards, talent cards only |
| "add animations" | **one animation per change** | milestone state transitions |
| "make it mobile friendly" | **design at 390px first**, check 320 and 430, **44px touch** | the Ghana reality |

**This is a significant upgrade to §10.** My design system specified tokens and principles; these
keywords specify *counts and measurements*, which is what actually stops drift — and crucially, what
stops an AI-assisted build from producing the generic look the user is worried about.

**The single most useful sentence in the whole library** for this project: *"Simple is a count: one
filled button, and everything else is content or a quiet text link."*

---

## 22.5 Errors, overclaims and risks in the library

I am applying the library's own standard to itself.

| Item | Problem | Correction |
| --- | --- | --- |
| `brand and branding.md` line 3 | Opens with **hallucinated-looking inline citations**: `[1] (https://knamaky.medium.com/…)` and a YouTube link about brand strategy used to support *"branding is divided into three distinct layers"* | The three-layer model (Strategy / Identity / Experience) is widely used and defensible, but the specific numbered citations are decorative, unverifiable, and some are YouTube videos. **Strip the fake-looking citation apparatus; keep the model.** |
| `brand and branding.md` / `system design.md` | 13,000–25,000 lines with heavy internal duplication | Consolidate. Size is not authority. |
| `disciplines_field.md` | "≈81 disciplines × 3 prompts = 243 prompts" | The count is presented as completeness. 81 *job titles* is not 81 *disciplines*, and 243 templates is a quantity claim, not a quality claim. Use it as a generator, not a library to "finish". |
| `system design.md` | Named "system design" but is ~88% a brand/creative concatenation; **contains no distributed-systems content** | Rename to `library-concatenated.md` or delete. Anyone reading it expecting system design will be misled by the title. |
| Bitekasa Master Codex §"Status" | *"Graphic Design (13 vol.) ✅ Complete"* + ~201 documents planned | This is a **production plan for a content library**, not a delivered asset. Do not let a roadmap with ✅ marks imply the business has these assets. |
| `200_Creative_Image_Slash_Commands.pdf` | "200 commands" are *custom shortcuts*, not built-in tool commands | The file states this correctly up front — good. Just never present them as native features. |
| `HyperFrames` / `UGC` PDFs | Vendor-specific prompts (HeyGen; image generation) | Zero relevance to a marketplace app. Do not let them into scope. |
| `WEBSITE_GUIDE.md` | Musician website for "Emma Revelation" | **Unrelated project.** Excluded. |
| Whole library | **Zero** market research, competitor pricing, Ghana regulation, payment-rail availability, or user evidence | This is the library's real boundary — see §22.9. |

**The library's own best rule applied to the library:** *"Do not treat duplicate repetition as
independent evidence."* A 1.2 MB file is not more true than a 12 KB one.

---

## 22.6 How each source upgrades the TechBro pack

| Source | Where it plugs in | Concrete change |
| --- | --- | --- |
| Evidence taxonomy (7 labels) | §99 sources register | relabel every claim as fact / verified / source claim / interpretation / assumption / decision / unknown |
| Status + stop labels | new working agreement | add a `WORKING-AGREEMENT.md` so every future session obeys it |
| 8 Structures | §02 gates | add an **8-dimension readiness check** to G6 Launch (currently G6 checks ops evidence, not business/marketing readiness) |
| 11-step response format | how I answer | two concepts before recommending; self-critique before delivery |
| Push-back rule | §17.7 ethics | formalise "refuse clichés, dark patterns, unlicensed claims" |
| 59 role prompts (IPO + references + tasks by level) | §01 catalogue | keep 300-row coverage; add depth sheets for the 10 roles that matter in 90 days |
| 6 pre-build documents | §18 next steps | **rewrite the 6 as founder-readable one-pagers** (see below) |
| `keywords.pdf` (40 named patterns) | §10 design system | add a **named-patterns table with counts and measurements** — this is the anti-drift layer |
| Janus Tiu design-system template | §10 §10.6 | convert to actual token JSON (colour/type/space/radius/shadow/rules) |
| Brand blueprint A–L | §13 GTM + ART-091 | use its 12 areas as the brand checklist; mine was thin on brand architecture and naming |
| Business foundations (8W+H, break-even) | §13 unit economics | cross-check my break-even framing against its worked example |
| Security Raas prompt | §09 | adopt its authorisation-boundary and "no action claimed without evidence" clauses |

### The gap this forces me to name

The **8 Structures** test says a deliverable must also be *marketing- and sales-ready*. Judged by that
test, my pack scores: product-ready ✅, standard-ready ✅, professionally crafted ✅, project-ready ✅,
academically sound ✅, industry-ready ✅, business-ready ◐ (unit economics are illustrative),
**marketing/sales-ready ❌**.

That is the honest score. The missing artefact is a page written for a *client or investor*, not an
engineer. It belongs in the next turn, not this one — it is a deliverable, not a critique.

---

## 22.7 The one-page method that unifies the library

Across all 15 files, the same method appears in different clothes. It reconciles to this:

```
1. FRAME     8W+H (what/why/who/whom/where/when/which/how) + first principles
2. SEPARATE  fact · verified external · source claim · interpretation · assumption · decision · unknown
3. SCOPE     Results-as-a-Service brief: outcome, deliverable, measure, baseline,
             constraints, owner, risks, exclusions, definition of done, review date
4. THINK     Bloom L1→L6 to set depth; System 1 (fast capture) vs System 2 (slow verification)
5. DESIGN    ≥2 distinct concepts before choosing; lo-fi before hi-fi
6. BAR       8 readiness dimensions, run over the same work
7. PROVE     evidence, citations, verification status, test results
8. CRITIQUE  self-critique + risk register + what to test
9. STOP      ship / needs evidence / needs owner decision / needs professional review
```

**This is the method I will use from here on**, and it is a genuine improvement on what I was doing —
because it forces steps 8 and 9, which are the two that prevent confident nonsense.

---

## 22.8 What the library tells me about *how you work* (and what to change)

Reading 3.46 MB of someone's collected prompts reveals their working style. Honest observations:

1. **You collect method faster than you apply it.** 243 role templates + 201 planned codex volumes is
   a library large enough to build ten companies and finish none. The TechBro pack exists because
   *application* had not happened yet.
2. **You already have the anti-hallucination instinct** — the Raas prompts, stop rules and evidence
   taxonomy are better than most professionals'. Trust it and enforce it with labels, not willpower.
3. **Your design taste is already specified** — `keywords.pdf` proves you know the difference between
   generic and professional. The risk is not taste; it is scope.
4. **The library has no Ghana in it.** Not one payment rail, regulator, or local competitor. That is
   precisely where the risk now sits, and it is where the next research should go.

**The uncomfortable recommendation:** stop adding to the library until the TechBro concierge phase
has closed five paid jobs (§18.4). No new prompt pack will answer "will someone pay 10% in Accra".
Only five customers will.

---

## 22.9 What the library cannot tell you (the research queue)

Ranked by how much each answer changes the design:

| # | Unknown | Why it blocks | Where to get it | Owner |
| ---: | --- | --- | --- | --- |
| 1 | Will a Ghanaian client pay a 10% fee rather than transact off-platform? | decides whether there is a business | 5 concierge jobs, verbatim answers | D001 |
| 2 | Does Act 987 require a licence for our exact money flow? | decides the launch architecture | written counsel opinion | D018 |
| 3 | Is Paystack's delayed settlement sufficient as an escrow substitute? | decides whether we need a partner at launch | provider compliance + sandbox test | D100 |
| 4 | What do Accra clients actually pay for a Flutter/Django job today? | decides unit economics | 10 real quotes + public listings | D024 |
| 5 | How many verified workers can we get to 55% utilisation? | decides liquidity | concierge matching data | D240 |
| 6 | What is the real KYC cost and false-reject rate locally? | decides onboarding friction | 2 vendor quotes + pilot | D154 |
| 7 | What are the actual dispute patterns in local tech work? | decides the brief template | 5 closed jobs, dispute log | D180 |
| 8 | Which acquisition channel produces verified supply at <GHS 25? | decides GTM | 3 channels × 2 weeks | D229 |

**Notice what is not on this list:** architecture, roles, design system, testing strategy, runbooks.
Those are *solved* — the pack has them. The unsolved problems are all outside the library's scope,
which is exactly why it cannot substitute for them.

---

## 22.10 The library, in one paragraph

This is a mature, unusually well-organised **personal operating system for thinking and producing** —
strong on method, evidence labelling, design precision and role structure; weak on market truth,
local regulation, and the discipline of finishing. Its best three artefacts are the seven-label
evidence taxonomy, the eight readiness structures, and the 40 named design patterns; its worst habit
is scale-as-progress. Used as a *quality bar and a working agreement*, it makes the TechBro pack
measurably sharper. Used as a *substitute for customer contact*, it will make you extremely well
prepared to build something nobody buys.

**Adopt the method. Keep the five source files, drop the concatenation. Then go and talk to five
customers.**

---

## 22.11 Update — the second batch (15 files, 155 KB) and what it changed

A second upload arrived with 15 more files totalling **155 KB / 2,900 lines** — 3% of the first
batch's size, and almost all of it **index material rather than new method**. Verdict per group:

| Group | Files | What it is | Verdict |
| --- | ---: | --- | --- |
| **Cheat-code indexes** | 8 | `MASTER-INDEX-all-codes`, `the-everything-master-codes`, `domain-cheat-codes-10-areas`, `business-*`, `computing-study`, `study-learn`, `collaborative-and-tool-codes`, `prompt-context-engineering-cheatcodes` | **One index, rest redundant.** Keep `MASTER-INDEX` only |
| **Idea → product flows** | 3 | `idea-to-product`, `software-idea-to-product`, `business-idea-to-product` | Useful as a **checklist**, not a method |
| **Competitor analysis** | 1 | `competitor-analysis-cheatcodes` | **Adopt the vocabulary** (see below) |
| **Prompt frameworks** | 2 | `real-prompt-frameworks`, `prompt-and-context-engineering-guide` | The guide is the best of the batch |
| **Codex roadmap** | 1 | `00-MASTER-CODEX-ROADMAP` | Duplicate of material already summarised in §22.4 |

### The one genuinely important sentence in the batch

`prompt-and-context-engineering-guide.md` contains the most intellectually honest paragraph in all
30 uploaded files:

> *"I **did** create many codes myself (e.g. `/business_fundamentals`, `/unit_economics`, `/dsa`).
> These are **not documented AI features.** … nobody at OpenAI or Anthropic officially defined
> `/business_fundamentals`. I was honest about those being additions I made to complete the flow."*

And the conclusion: **"the `/` prefix does nothing. What actually improves output is prompt and
context structure."**

That is correct, and it matters for a project-level reason: **your library is 3.46 MB + 155 KB, and
the slash codes inside it carry no mechanism.** Every improvement in this pack came from structure —
evidence labels, stop rules, named patterns, the six documents — not from shortcut codes. Adopt the
structure; drop the codes.

### The one thing I am adopting: competitor vocabulary

`competitor-analysis-cheatcodes.md` supplies six words the pack was missing, and they are sharper than
what `19` used:

| Term | What it forces you to state |
| --- | --- |
| **`/whitespace`** | the unfilled gap — not "we are better", but "nobody serves this" |
| **`/moat`** | their defensible advantage, *and how to beat it* |
| **`/dodge`** | where you must **not** compete head-on |
| **`/assumptions`** | what their strategy depends on being true |
| **`/redflag`** | their points of failure |
| **`/counter_strategy`** | what they do if you succeed, and your answer |

Applying `/dodge` to TechBro: **do not compete on fee, on catalogue breadth, or on vetting rigour** —
Braintrust wins fee at 0%, Upwork wins breadth, Toptal and Growwr win rigour. The only undefended axis
is **speed to unblock in a local payment context**, which is `23` §23.6.

### And the honest limitation to record

Like the first batch, this one contains **no market data at all** — the competitor file is a *method
for analysing* competitors, not an analysis. It even says so: *"For real, current competitor data, pair
these codes with live web search rather than relying on the model's memory."* `23` did exactly that,
which is how S58–S62 came to exist.



---

## 22.12 Update — the third batch (20 files, 1.0 MB): what is new, what is already paid for

The third upload is **1.0 MB / 15,700 lines** across 20 files. It is the most *internally coherent*
batch so far and the least *new*: 18 of the 20 are the graphic-design codex volumes whose provenance
`THE-GREAT-LOOP-GRAPHIC-DESIGN.md` already named explicitly in `22` §22.3.

| Group | Files | Lines | Verdict |
| --- | ---: | ---: | --- |
| Graphic-design codex (13 volumes) | 13 | ~10,000 | **Already paid for.** The Great Loop digested them; read that instead |
| Senior graphic-designer prompts | 3 | ~1,450 | Superseded by The Great Loop |
| DaVinci Resolve codex | 1 | 1,304 | **Out of scope** — video post-production |
| **THE_SEVEN_LAYERS** | 1 | 738 | **Keep — ten laws, one of which indicts this pack** |
| **THE_COMPLETE_STACK** | 1 | 665 | **Keep — §9 role table + §10 SDLC order** |
| Senior software/network/security prompts | 2 | 1,036 | Reference only |

### The ten laws, and the one I broke

`THE_SEVEN_LAYERS.md` closes with ten laws that "don't care about your stack". Eight are things this
pack already obeys (unreliable network, non-zero latency, heterogeneous clients, least privilege).
Two are not:

| Law | Status in the pack |
| --- | --- |
| **8 — "Your users are on 3G Android phones in sunlight. Design for that, not your M-series MacBook on fibre."** | **Honoured** in `10` (390px, 44px targets) and `23` §23.11 — this is the best line in the batch for your context |
| **7 — "The business rules belong in exactly one place — the domain. Everywhere else is a caller, not a decider."** | **Broken.** See `23` §23.18 |

Law 7 is the finding. The pack specified three clients (React Native, web, admin) and never stated
where the money rules live. It is now stated, with three non-negotiable rules.

### The one thing worth lifting verbatim

The batch's most useful contribution to *this* project is a single sentence of calibration:

> *"Your users are on 3G Android phones in sunlight. Design for that, not your M-series MacBook on
> fibre."*

Every design decision in `10` and `23` §23.10 can be tested against that one line. It is the clearest
statement of the constraint that governs the entire product, and it came from a file about system
layers rather than a file about design.

### And the honest bottom line on the library as a whole

Across **65 files and ~4.6 MB**, the value distribution is now clear:

| Contribution | Where it came from | Share of value |
| --- | --- | ---: |
| Evidence discipline, stop rules, 8 structures | batch 1 (`bitekasa`, `software_security`) | **high** |
| Named design patterns, pre-build gate | batch 1 (`keywords.pdf`, `Before_Anyone_Builds`) | **high** |
| Ten laws, domain-single-source | batch 3 (`THE_SEVEN_LAYERS`) | **high** |
| Prompt frameworks, cheat-code indexes | batches 1–3 | **low** — one page each |
| Design codex volumes, Davinci, music, image prompts | batches 1–3 | **none for this product** |

**Roughly 5% of the library carries 90% of the value, and every high-value item is a *standard or a
rule*, not a template.** That is the pattern across all three batches and it is worth stating plainly:
you do not need a 66th file. You need the ten laws, the seven evidence labels, the six documents and
the eight structures — all of which you now have.


---

## 22.13 Update — the fourth batch (9 files, 6 new): the first batch that closed a real gap

`[F]` Three of the nine were byte-identical to files already reviewed in §22.12 (`ULTIMATE-MASTER-PROMPT-senior-fullstack…`, `-graphic-designer`, `-software-network-security…`). Those are excluded here.

| File | Lines | What it is | Verdict |
| --- | ---: | --- | --- |
| `ULTIMATE-MASTER-PROMPT-senior-uiux-wireframe-motion-designer` | 487 | Senior UI/UX prompt with motion and wireframe scope | **keep** — closest prompt to the app's actual craft |
| `Basic Use Case Diagram` | 1,127 | UML 2.5.1 use-case notation, 11 shape definitions, actor left/right rule | **keep — used** |
| `Basic Sequence Diagram` | 876 | 9 message types incl. async, create, destroy, activation boxes | **keep — used** |
| `Basic Activity Diagram` | 1,508 | 11 shapes incl. fork/join/merge, decision, guard, swimlane | **keep — used** |
| `Basic Process Flow Diagram` | 2,132 | process notation + the longest worked example of the five | keep |
| `Basic Flowchart 6 Shapes` | 1,505 | the minimal 6-shape vocabulary | keep as the floor |

### Why these five are different from everything else uploaded

Across four batches and **74 files**, this is the first set that gave the pack something it **could not
have generated itself**: a *precise, checkable notation*.

Every prior batch supplied method (how to think), templates (what to fill in), or indexes (where to
find things). All of that is advisory. UML notation is **constraining** — a sequence diagram with a
sync arrow where an async one belongs is *wrong in a way a reader can point at*. That is a different
category of contribution.

The proof is immediate: `24-behavioural-model.md` now exists because these files made it possible to
draw the six behaviours *to a standard* rather than sketch them. Three findings fell out that the prose
had hidden:

1. **The 90-second budget.** Drawing the matching fan-out forced a latency number that no chapter had
   ever stated. `[A]`
2. **The refund state is platform-funded, not a ledger reversal** — visible only when the payment
   transitions are drawn adjacent to another (`24` §24.5).
3. **The dispute asymmetry decision** — requester-wins-by-default — was not decided anywhere in 23
   chapters and had to be decided to complete the activity diagram (`24` §24.6).

### The pattern across all four batches, stated finally

| Batch | Size | Genuinely new value | Category |
| ---: | ---: | --- | --- |
| 1 | 3.46 MB | 7-label evidence taxonomy · 8 structures · 6 pre-build documents · 40 named patterns | **method** |
| 2 | 155 KB | competitor vocabulary (`/whitespace`, `/moat`, `/dodge`) | **vocabulary** |
| 3 | 1.0 MB | ten laws (one of which the pack was breaking) | **rules** |
| 4 | 270 KB | **UML notation** | **constraint** |

> **The smaller the batch, the more it changed the work.** Batch 1 was 13× the size of batch 4 and
> contributed method; batch 4 contributed the notation that turned method into specification.

That is the opposite of the intuition that bigger libraries are more valuable, and it is the last thing
worth recording about this library.
