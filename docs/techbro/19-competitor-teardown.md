# 19 — Competitor Teardown & Prior-Art Review

> Purpose: learn from what already exists so you do not pay to rediscover it. Every factual claim
> here is sourced in `99-sources-and-assumptions.md` (S51–S57) and was checked on **2026-11-06**.
> Fee and pricing claims are the most volatile thing in this document — re-verify before quoting
> them to an investor or writing them into a contract.

---

## 19.1 The map: five different businesses people call "freelance platforms"

The single most useful insight in this chapter: **these platforms are not competitors with each
other, they are five different business models.** Your app is closer to two of them than to the
other three, and choosing the wrong reference model is how you end up building the wrong product.

| Model | Who it serves | How it earns | Example | Your overlap |
| --- | --- | --- | --- | --- |
| **1. Open global marketplace** | anyone ↔ anyone | take rate from both sides | Upwork, Fiverr, Freelancer | **high** — same mechanics, different segment |
| **2. Curated premium network** | vetted senior ↔ enterprise | markup hidden in the rate | Toptal, Braintrust | medium — the trust model you want, the segment you don't |
| **3. Managed talent outsourcing** | vetted engineer ↔ enterprise team | margin on a monthly contract | Andela, Tecla, Gebeya | low — long contracts, not task delegation |
| **4. Regional micro-marketplaces** | local talent ↔ local clients | mixed/undisclosed | CediJob, TERAWORK, Findworka | **high** — same market, weaker product |
| **5. Peer collaboration tools** | engineer ↔ engineer | subscription | GitHub, Linear, Slack | low — they are your *competition for attention*, not your revenue |

**The gap you described** — "I have more work than I can do, find me someone competent who can
deliver it, and hold the money safely" — sits between model 1 (too open, price-anchored to $5/hr)
and model 3 (too slow, 12-month contracts). That gap is real. It is also narrow, and this chapter
shows exactly how narrow.

---

## 19.2 Upwork — the reference implementation of everything you must get right

**Model:** open marketplace, escrow-backed milestones, hourly protection, proposals with paid
"Connects". Fees: freelancer service fee reported in the **0–15% range with most contracts around
10%** in 2026, plus a client marketplace fee of roughly **5%** and a one-time contract initiation fee
(S51; sources disagree on whether 10% is now flat, so treat the exact number as needing
confirmation).

| Strengths (copy these) | Weaknesses (this is your opening) |
| --- | --- |
| Escrow as a default, not an option — money is the trust mechanism | Fees on *both* sides plus paid proposals: the worker pays to apply and still pays on earning |
| Job Success Score + top-rated badges create portable reputation | Reputation is coarse; a "Top Rated" badge says nothing about whether someone can do a Flutter migration |
| Time-zone and skill filters at scale; mature dispute process | Global price competition anchors Ghanaian talent to $2–$10/hr (S57) — the exact trap you must avoid |
| Contract types (fixed, hourly with protection) match real work | Hourly "protection" still leaves scope disputes; brief quality is the user's problem, not the platform's |
| Huge demand liquidity | Discovery is a lottery; small clients get 50 low-quality proposals |

**What to steal:** milestone escrow as the default, portfolio-grade reputation, structured contract
types. **What to beat:** *scoping*. Upwork hands you a blank box and 40 proposals. You can hand the
client a structured brief that a professional would accept — that is the wedge.

---

## 19.3 Fiverr — the productised-gig model, and why it fails for real engineering

**Model:** sellers publish fixed-scope "gigs"; buyers buy. Fees: **20% flat seller commission**,
buyer pays **5.5%** plus a small-order fee, earnings clear in **14 days** (7 for higher tiers) (S54).

| Strengths | Weaknesses |
| --- | --- |
| Zero friction to start; the seller does the scoping in advance | 20% + buyer fees means the platform takes ~24–29% of the transaction (S54) — unsustainable for skilled work |
| Productised packages make price comparison easy | Engineering work is not a productised gig; a "fix my app" task is discovery, not a SKU |
| Strong for creative/commodity deliverables | Ranked placement + gig SEO rewards marketing skill over engineering skill |
| Great UX for browsing | No real collaboration surface (no repo, no milestone review, no technical acceptance criteria) |

**What to steal:** the *package* idea — but apply it to **task archetypes** ("review my architecture",
"unblock a deadlock", "security pass on a payment flow"), pre-scoped with acceptance criteria.
**What to avoid:** 20% take rates and gig-style ranking. Skilled workers will not tolerate it.

---

## 19.4 Toptal — the trust model you actually want, at a price your market cannot pay

**Model:** accept ~**3%** of applicants through a multi-stage screen (live interview + test project);
freelancers pay **0%**; the client pays a **markup reported at 30–50%** on top of a $60–$200+/hr rate,
plus a monthly subscription and deposit (S52).

| Strengths | Weaknesses |
| --- | --- |
| Screening creates genuine quality signal — clients trust the badge | The model does not scale down: a GHS 4,000 job cannot absorb a 30–50% markup |
| Talent pays nothing, so supply quality is not price-gated | Opaque pricing; the worker cannot see their own margin |
| Human matchers beat algorithms for high-stakes hires | Enterprise-only demand; no SMEs, no local market |
| Long-term relationship orientation | Acceptance at 3% means ~97% of your target users would be rejected — wrong posture for a community product |

**What to steal:** the *idea* that verification is the product. **What to reject:** the 3%
gate and the hidden markup. Your version: tiered verification (ID → assessed → peer-endorsed) with
visible levels, so a junior can enter, and a client can see exactly what is verified and what is not.

---

## 19.5 Braintrust — the fee structure that should worry you most

**Model:** **0% to talent**, **flat 10% to clients**, community/token governance (S53).

This is the most directly threatening benchmark in this document, for one reason: **if a credible
platform charges talent nothing, your 10% talent-side fee has no defence.** It also shows the
sustainable shape of the business: charge the side that has budget (clients), and make the supply
side feel ownership.

**What to steal:** client-side fees. **What to reject:** token governance — it adds regulatory and
reputational complexity you cannot afford, and it does not help a worker in Accra get paid this week.
**The strategic lesson:** *who pays* is a product decision, and charging the worker is the easiest
way to lose the worker.

---

## 19.6 Andela — proof that African tech talent is a real export business, and why that is a warning

**Model:** founded Lagos 2014; vets engineers (acceptance reported near **0.5%**), places them into
client teams on long contracts (commonly **12-month minimums**) at roughly
**$6,000–$14,000 per developer per month**; talent are contractors, majority enterprise demand in
North America and Western Europe (S55).

| Strengths | Weaknesses (your opening) |
| --- | --- |
| Proves global demand for African engineers at premium rates | **No short-term freelance tier** — if you need 6 hours of help on Saturday, Andela is not an option |
| Vetting rigour + managed payments/compliance | Enterprise sales cycle; an SME cannot buy |
| Handles the hard parts: cross-border payroll, contracts | Talent is placed *outward*, so the local market gains little |
| Strong brand, capital, and a decade of operating data | Price point excludes the Ghanaian SME and the solo founder entirely |

**The strategic warning:** Andela demonstrates that the most valuable flow is **talent going out to
global clients**, not local talent serving local clients. That is where the money is. It is *not*
where your stated mission is. You must decide consciously which one you are building, because the
product, pricing and payout rails differ.

---

## 19.7 Regional players — the actual competitive set in Accra

Ghana-focused and pan-African platforms exist and are already listing Accra developers: CediJob
(Ghana-first freelance marketplace, accelerator-backed), Gebeya, TERAWORK, Findworka, Solangigs, plus
global platforms (Truelancer, Twine) with Accra listings (S57).

| Their pattern | What it tells you |
| --- | --- |
| Thin verification ("basic verification process" for at least one Ghanaian platform) | Trust is the unclaimed ground — verification depth is a genuine differentiator |
| Mobile money + bank transfer as first-class rails | Table stakes in Ghana; not a differentiator, but a hard requirement |
| Price anchoring at $2–$10/hr in public listings | The market is already anchored low; if you compete on price, you lose to people who can afford to lose |
| Small supply pools, weak matching | Liquidity is local and thin — which means a *narrow* launch can win a whole category |
| Little evidence of escrow or structured disputes | **This is the gap.** Nobody local owns "the money is safe and disputes get resolved in days" |

**Honest caveat:** these platforms were assessed from public listings and directories, not from
internal data. Their revenue, user numbers and retention are unknown, and this pack does not pretend
to know them. Before launch, sign up as a user on the top three and document the real onboarding,
fees and dispute experience — a half-day of mystery shopping is worth more than this table.

---

## 19.8 Feature-by-feature comparison

Legend: ● strong · ◐ partial · ○ absent/weak · — not applicable. *Judgements are based on public
product information; verify by using each product.*

| Capability | Upwork | Fiverr | Toptal | Braintrust | Andela | GH regional | **Your target** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Structured brief / scoping help | ◐ | ○ | ◐ (human) | ◐ | ◐ | ○ | **●** |
| Skill verification depth | ◐ (tests) | ○ | ● | ◐ | ● | ○ | **●** tiered |
| Escrow / milestone protection | ● | ● | ● | ● | ● | ◐ | **●** |
| Local mobile-money payouts | ◐ | ○ | ○ | ○ | ◐ | ● | **●** |
| Dispute resolution speed (published) | ◐ | ◐ | ◐ | ◐ | ○ | ○ | **●** SLA |
| Ghana-specific compliance (DPC, GHS, local KYC) | ○ | ○ | ○ | ○ | ○ | ◐ | **●** |
| Task-level (hours) delegation | ◐ | ● | ○ | ◐ | ○ | ◐ | **●** |
| Team/squad assembly | ◐ | ○ | ◐ | ◐ | ● | ○ | ● (v1) |
| Peer-to-peer escalation ("I'm stuck") | ○ | ○ | ○ | ○ | ○ | ○ | **●** |
| Transparent fees | ● | ◐ | ○ | ● | ○ | ◐ | **●** |
| AI-assisted scoping | ◐ | ◐ | ○ | ○ | ◐ | ○ | **●** |

**Read the last column, not the others.** There is exactly one column with no ○ or ◐ in the first
six rows, and it is the one you can own: *structured scoping + tiered verification + local rails +
published dispute SLAs*. That is a coherent product, and it fits a small team.

---

## 19.9 The six things every one of them gets wrong (your openings)

1. **Scoping is dumped on the user.** All of them let a client write "need an app" and then blame the
   dispute on the client. Fix the brief and you fix half the disputes before they exist.
2. **Verification is either absent or binary.** A badge or nothing. Nobody publishes *what* was
   verified and *how well* — which is exactly what a client paying GHS 4,000 needs to know.
3. **Price is anchored to the global bottom.** Public Accra listings at $2–$10/hr (S57) mean the
   local market has already learned to undervalue itself. A platform that visibly pays more, faster,
   and safely can re-anchor it.
4. **Disputes are black boxes.** Deadlines and criteria are rarely published. Publishing an SLA
   ("first response 24h, decision 5 business days") is a marketing asset, not just an ops policy.
5. **The worker pays to apply.** Connects/proposal credits monetise the side with the least money.
   Charge the side with a budget.
6. **Nothing is designed for intermittent power, 3G, or data cost.** Every one of them assumes a
   Silicon-Valley network. A product that works well on a 2GB Android on 3G is a differentiator
   nobody in this list is optimising for.

---

## 19.10 What this means for your strategy (the hard parts)

| Question the teardown forces | Evidence | Honest answer |
| --- | --- | --- |
| Can you win on price? | Fiverr takes ~24–29% of a transaction and still wins on volume (S54); global supply is infinite | **No.** Compete on trust, speed and local rails, never on price |
| Can you win on breadth? | Upwork/Andela inventory is enormous | **No.** One city, two skills, one promise |
| Is local competition real? | Multiple Ghana/Africa platforms already list Accra talent (S57) | **Yes**, but weakly on trust and disputes — that is the seam |
| Is there more money abroad? | Andela's enterprise demand is North America/Western Europe (S55) | **Yes** — so decide explicitly: local mission, or export business, or both in sequence (local first to build the verified supply graph, then export) |
| Can you charge the worker? | Braintrust charges talent 0% (S53) | **Prefer client-side fees.** If you must charge talent, keep it far below 10% and justify it with escrow + dispute protection |
| Can you hold funds yourself? | Act 987 requires a BoG licence for payment services (S5); Stripe Connect is not directly available to a Ghanaian entity (S56) | **No.** Provider-side split with delayed settlement, own ledger, licensed partner later |

---

## 19.11 The strategic fork this teardown exposes

You cannot serve two masters with one pricing model. Choose one primary thesis now, and write it
into ART-009:

| Thesis | Who pays | Product centre of gravity | Ceiling | Main risk |
| --- | --- | --- | --- | --- |
| **A. Local trust marketplace** | Ghanaian clients (SMEs, founders, agencies) | escrow + verification + dispute speed | medium revenue, deep local moat | the local market may not pay enough |
| **B. Export talent network** | Foreign clients paying in USD/EUR | vetting + payroll + compliance | high revenue, competes with Andela/Toptal | you become a staffing agency, not a community |
| **C. Peer collaboration + delegation network** | workers themselves (subscription) or a mix | matching between peers, escalation, squads | low revenue, high engagement | does not monetise well enough to survive |

**The recommendation from the evidence:** start with **A** to build the verified supply graph and
the trust mechanics cheaply, then add **B** on top once verification is credible — because the
export market pays 10–50× more per hour, and the verified-supply graph is the only asset that makes
you more than a middleman when you get there. Do not start with C; it is the most fun and the least
fundable.

---

## 19.12 What to copy, what to refuse

| Copy | Why | Refuse | Why |
| --- | --- | --- | --- |
| Escrow-first money flow (Upwork) | it is the trust mechanism | fee on both sides at 10%+ | Braintrust at 0% makes it indefensible (S53) |
| Verification as the core product (Toptal) | quality signal is what clients buy | a 3% gate | it starves your supply and contradicts a community mission |
| Task archetypes/packages (Fiverr) | lowers scoping friction | 20% commission, 14-day clearing | skilled workers will not tolerate it (S54) |
| Client-side fee model (Braintrust) | aligns with who has budget | token governance | regulatory + reputational complexity |
| Local mobile-money rails (regional players) | table stakes in Ghana | weak verification | it is the unclaimed differentiator |
| Long-term relationship orientation (Andela) | repeat hire is the real retention | 12-month minimums | kills the small-job wedge (S55) |

---

## 19.13 The one-sentence conclusion

Every incumbent has picked a position on the trade-off between **open + cheap + fast** and
**closed + trusted + expensive**. The open niche between them is **"trusted enough to be safe, open
enough to be fast, and local enough to be paid in cedis by Friday."** That is defensible, it is
buildable by four people, and — critically — it is small enough that the incumbents will not bother
to defend it until you have already won the supply.
