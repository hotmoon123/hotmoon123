# 13 — Business Model, Go-to-Market & Growth

> Every number in this document is either **sourced**, **derived from a stated assumption**, or
> **labelled as an assumption**. There are no confident market-size figures invented for
> encouragement; where we lack data, the document says so and gives the cheapest way to get it.

---

## 13.1 How this business can make money (and what it costs)

| Stream | Mechanic | Typical rate | Starts | Risk / note |
| --- | --- | --- | --- | --- |
| **Service fee (take rate)** | % of each completed engagement, split-bearer configurable | 8–12% | MVP | H-001: the only model that must work |
| Client subscription (v1) | unlimited posts, priority support, team seats | GHS 150–400/mo | v1 | SMEs resist recurring fees early |
| Verified-talent subscription (v2) | assessment badge, priority ranking (non-deceptive), portfolio analytics | GHS 30–60/mo | v2 | Must not become "pay to be seen" |
| Featured job / urgent hiring (v2) | promoted listing, clearly labelled | GHS 50–150/post | v2 | Ranking integrity must stay clean |
| Assessment & certification fees | paid practical assessment with certificate | GHS 80–200 | v2 | Needs assessor capacity |
| Squad/agency managed delivery (v3) | platform runs the project with margin | 20–30% | v3 | Operational heavy; different business |
| Employer/agency API (v3) | integration for agencies | usage-based | v3 | Only after trust is proven |
| Grants / impact funding (non-dilutive) | youth employment, digital skills programmes | project-based | now | Slower, but non-dilutive and credible for the mission |

**Explicitly rejected revenue:** selling user data, pay-to-rank without disclosure, interest on
escrowed funds (regulated + corrosive to trust), fees charged to workers for simply applying,
charging for "guaranteed" job placement.

## 13.2 Unit economics (illustrative, with assumptions stated)

**Per completed engagement (MVP, posture A: provider split):**

| Line | Value | Basis |
| --- | --- | --- |
| Median job value | GHS 4,000 | assumption (must be measured from first 50 jobs) |
| Take rate | 10% | H-001 target |
| Gross revenue | GHS 400 | derived |
| Payment provider fee | ~1.95% of GHS 4,000 = GHS 78 | published rate (provider pricing; re-check at contract) |
| Payout fee | GHS 1–8 per transfer × 1–2 | published rate band |
| SMS/OTP/notifications | ~GHS 6 | assumption: 25 messages at ~GHS 0.25 (verify with gateway) |
| KYC verification | ~GHS 3–8 | vendor-dependent (verify quotes) |
| LLM usage (brief assistant + digest) | ~GHS 2 | token budget §8.6 |
| Infra | ~GHS 4 | capacity model §4.12 |
| Support & dispute cost | ~GHS 25 | assumption: 15 min at loaded cost, 5% dispute rate |
| **Contribution margin** | **~GHS 280** | ≈70% of gross revenue |

**Sensitivity that matters:** the model breaks if (a) take rate falls under ~6% due to leakage,
(b) dispute rate exceeds ~15%, or (c) average job value falls below ~GHS 1,200 (fixed costs dominate).
Those three numbers are monitored weekly, not annually.

**CAC assumptions (to be tested, H-010):** community/organic GHS 0–10 per verified talent; paid
social GHS 20–40; employer outreach is founder-led (time, not cash). Blended target < GHS 25 for
talent, < GHS 120 for clients.

**LTV sketch:** if a talent completes 2 jobs/month at GHS 400 revenue per job with 70% margin, and
retains 6 months, LTV ≈ GHS 3,360 vs CAC ≤ GHS 25 — the ratio looks excellent *and is therefore
the number most likely to be wrong*. It depends entirely on H-001 (they pay the fee) and H-002
(demand exists). Do not raise capital on it before those are tested.

## 13.3 Pricing design

| Decision | Choice | Why |
| --- | --- | --- |
| Who pays the fee | Client pays by default; talent fee optional and disclosed | Talent supply is more price-sensitive; clients compare to agency cost (15–30%), so 10% feels cheap |
| Fee visibility | Shown before funding, itemised, never hidden in the price | Hidden fees destroy trust faster than high fees |
| Minimum fee | GHS 20 per engagement | Sub-GHS-200 jobs are not economically viable |
| Escrow fee | none separately | Bundled in take rate; simplicity wins |
| Refund policy | full refund if work not started; pro-rata for partial milestones *(legal review required)* | Fair and defensible |
| Price changes | 60 days' notice, grandfathered for active engagements | Word-of-mouth market; surprises travel fast |

## 13.4 Go-to-market: the first 1,000 users

The realistic channel mix in Accra in 2026, in order of cost-effectiveness:

| # | Channel | Tactic | Metric | Cost |
| ---: | --- | --- | --- | --- |
| 1 | **Existing communities** | Dev communities, campus tech clubs, WhatsApp/Telegram groups, hackathon networks | verified talent/week | time |
| 2 | **Concierge matching** | founder personally matches first 20 jobs; every match is a sales call | paid jobs closed | time |
| 3 | **Campus partnerships** | universities, technical universities, bootcamps (ART-244) | cohorts onboarded | low |
| 4 | **Employer outreach** | SMEs, startups in incubators/hubs, NGOs with digital projects | jobs posted | time |
| 5 | **Content/SEO** | "how much does an app cost in Ghana", "hire a Flutter developer Ghana", rate guides | organic signups | low cash |
| 6 | **Referrals** | both sides rewarded after first *completed* job (not signup) | referred activation | ~GHS 20–40/job |
| 7 | **Community events** | monthly meetup + demo day where completed jobs are showcased | attendance → signups | GHS 1–3k/event |
| 8 | **Paid social** | Instagram/TikTok/X, skill-specific creative, retargeting | CAC | GHS 20–40/talent |
| 9 | **Partnerships** | coworking spaces, incubators, telco/ISP SME programmes | partner-sourced jobs | revenue share |

**Sequencing rule:** do not spend on paid acquisition until activation is proven — paying to fill a
leaky bucket is the most common way marketplaces die with money in the bank.

## 13.5 Liquidity strategy (the only real moat)

| Lever | Mechanism | Measure |
| --- | --- | --- |
| **Constrain scope** | launch in 2 skills + 1 city | fill rate by skill |
| **Seed supply deliberately** | hand-verify 100 specialists before opening demand | verified supply per demand unit |
| **Concierge first** | founder matches by hand, learns the real brief patterns | time-to-fill |
| **Time-box demand** | encourage clients to post jobs with a decision date | jobs with deadline |
| **Notify intelligently** | alert only qualified talent, in quiet hours, grouped | notification → proposal rate |
| **Guarantee SLAs** | "first proposals within 24h or we help you source" | SLA attainment |
| **Backfill with squads** | larger jobs staffed by a lead + juniors | squad deal share |

**Liquidity math to watch weekly:** `open jobs ÷ active verified talent` (target 0.3–0.6),
`proposals per job` (target 3–8), `fill rate 7d` (≥55%), `time to first proposal` (<24h). When the
ratio drifts above ~1.0, demand outruns supply and quality collapses; below ~0.15, talent leaves.

## 13.6 Growth loops

1. **Reputation loop:** completed job → rating → better matches → more jobs → more ratings.
2. **Referral loop:** client refers a founder (both get fee credit) → new demand → more work for supply.
3. **Content loop:** public rate guides and salary data → SEO traffic → signups (needs real data, so
   it starts month 4+).
4. **Community loop:** events → trust → first job → testimonial → next event.
5. **Squad loop:** solo specialist brings 1–2 juniors → supply grows without acquisition spend.

## 13.7 Retention design

| Stage | User state | Intervention | Metric |
| --- | --- | --- | --- |
| D0 | signed up, no profile | guided setup, 1 skill minimum | profile completion |
| D1–7 | no proposal sent | curated 3 jobs + template | first proposal |
| D1–30 | no completed job | concierge match, feedback call | first completion |
| D30–90 | one job done | "hire again" nudge, saved talent | repeat hire |
| 90+ | inactive | skill-gap content, community invite, re-engagement with real jobs only | reactivation |

**Anti-pattern refused:** guilt-trip notifications, fake "someone viewed your profile" messages, and
streak mechanics. They raise DAU and destroy the trust the product sells.

## 13.8 Financial plan shape (12 months, illustrative)

| Month | Verified talent | Clients | Jobs posted | Fill rate | GMV (GHS) | Revenue (GHS) | Burn (GHS) | Notes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 30 | 10 | 8 | 40% | 12,000 | 1,200 | 18,000 | concierge, no app |
| 2 | 60 | 20 | 18 | 45% | 32,000 | 3,200 | 20,000 | app beta |
| 3 | 100 | 35 | 30 | 50% | 60,000 | 6,000 | 24,000 | public launch |
| 4 | 150 | 55 | 45 | 52% | 100,000 | 10,000 | 26,000 | |
| 5 | 210 | 80 | 65 | 55% | 150,000 | 15,000 | 28,000 | |
| 6 | 280 | 110 | 90 | 55% | 210,000 | 21,000 | 30,000 | squad feature |
| 9 | 500 | 220 | 180 | 58% | 480,000 | 48,000 | 40,000 | second city prep |
| 12 | 800 | 380 | 300 | 60% | 900,000 | 90,000 | 55,000 | break-even trajectory |

**Assumptions behind it:** average job GHS 4,000 and rising with squad deals; 10% take rate; no
paid acquisition until month 4; team grows from 4 to 9. **This table is a planning instrument, not
a promise.** Re-forecast monthly against actuals; a forecast never revisited is a fairy tale with
columns.

## 13.9 Funding strategy

| Source | Fit | What it buys | Risk |
| --- | --- | --- | --- |
| Grants (youth employment, digital skills, innovation) | strong fit with the mission | runway + credibility, non-dilutive | slow, reporting burden |
| Angel / pre-seed (local + diaspora) | GHS 1–5M for 18 months | team + growth | dilution, pressure for premature scale |
| Strategic (telco, bank, PSP) | distribution + payments | reach | misaligned incentives, exclusivity traps |
| Revenue-based / debt | later, once GMV is predictable | working capital for escrow float | not before unit economics are proven |

**Capital discipline:** raise for a milestone, not for a mood. The milestone here is
**"600 completed paid engagements with <5% disputes and positive contribution margin"** — because
that is the first fact that makes the next round cheaper.

## 13.10 Partnerships that actually matter

| Partner type | Why | What we need from them | What they need |
| --- | --- | --- | --- |
| Payment provider (PSP) | rails, splits, settlement | compliance clarity, sandbox, rate clarity | volume, clean KYC |
| KYC/identity vendor | Ghana Card verification | accuracy, SLA, data-processing terms | volume |
| Universities / bootcamps | supply pipeline | cohorts, curriculum input | placement data |
| Incubators / hubs | demand | introductions to portfolio companies | talent access |
| Coworking spaces | community + events | space, members | programming |
| Employers / agencies | recurring demand | jobs, feedback | vetted talent fast |
| MoMo operators | payout reach + USSD promotion | API access, commercial terms | volume |

**Rule for every partnership:** written data-processing terms (S2), an exit clause, and a named owner
on both sides. Partnerships without DPAs are privacy incidents waiting for a date.

## 13.11 Competitive response

If a well-funded global marketplace enters Accra:

1. **Do not compete on breadth** — they will win on inventory. Compete on verification depth and
   local dispute resolution speed.
2. **Lock the supply relationship** through reputation portability, community, and payments trust.
3. **Make switching expensive by being genuinely better**, not by contract clauses.
4. **Keep the take rate honest**; a price war with a subsidised competitor is unwinnable, but a
   trust advantage is defensible.

## 13.12 The five numbers on the wall

If everything else is forgotten, these are the numbers that decide whether this works:

1. **Fill rate (7d)** — is the marketplace working?
2. **Repeat-hire rate (90d)** — is it a marketplace or a one-night stand?
3. **Dispute rate** — is the product's promise holding?
4. **Contribution margin per job** — is growth funded or fictional?
5. **Verified supply per demand unit** — is the loop sustainable?

Everything else — followers, downloads, waitlists — is a vanity metric that can be true while the
business is dying.
