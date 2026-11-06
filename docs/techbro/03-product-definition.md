# 03 — Product Definition: The Two-Sided Tech Talent Marketplace

> Working name: **TechBro** (see ART-091 for naming; `TechBro` is a placeholder with known
> risks — §3.10 — not a decision). Everything here is a *hypothesis with a test attached*, which
> is what a product brief is before users exist.

---

## 3.1 The one-paragraph product

A cross-platform mobile marketplace where vetted tech talent in Ghana finds paid work, and people
who need work done — founders, SMEs, agencies, and other tech workers who are over capacity —
find someone competent to do it. The product is not a job board. Its core promise is
**"you will get the work done, and the money will be handled safely"**: structured job briefs,
skill-level matching, milestone-based escrow, delivery verification, and a dispute path that
resolves inside days, not months. The community layer ("tech bros") is the retention engine:
learning, squads, and reputation that compounds.

**What it is not:** a CV database (LinkedIn), a full-time recruitment agency, a generic freelance
marketplace optimised for the lowest global price (Upwork/Fiverr), or a bootcamp.

## 3.2 The problem, stated precisely

Three distinct jobs-to-be-done sit behind the user's original idea. They are different products
wearing one coat, and conflating them is the most likely way to fail:

| # | JTBD | Who says it | Current workaround | Cost of the workaround |
| --- | --- | --- | --- | --- |
| J1 | *When I have more work than capacity, I want to hand a well-scoped task to someone I can trust, so I keep my client and my reputation.* | Freelancers, small agencies, senior devs | WhatsApp groups, referrals, personal network | Turned-down revenue; quality risk with strangers |
| J2 | *When I need a specific skill (mobile, data, security) for a defined outcome, I want to find and verify someone quickly, so the project does not stall.* | Founders, SMEs, NGOs, non-tech companies | Ask in 6 WhatsApp/Telegram groups and hope | Weeks lost; overpaying for generalists; scams |
| J3 | *When I am starting or growing in tech, I want real paid work and feedback, so I can build a verifiable track record.* | Students, self-taught devs, junior talent, career-switchers | Free "collabs", unpaid trials, cold DMs | Exploitation; no evidence of ability; no income |

**The wedge** (§3.5) is J1 + a slice of J2, because both sides of that transaction are already
inside the community and the trust transfer is highest. J3 is the supply pipeline, not the product.

## 3.3 Users and actors

**Supply side (talent)**

| Actor | Description | Primary need | Success signal |
| --- | --- | --- | --- |
| **Solo specialist** | Freelancer with one strong skill (Flutter, Django, data, design, security) | Steady paid work without hustling in DMs | ≥1 paid engagement/month; repeat client |
| **Squad lead** | Senior dev who assembles 2–5 people for bigger jobs | Access to bigger contracts without an agency | Squad deal completion |
| **Junior / emerging** | 0–2 years, portfolio thin | First paid work + mentorship | First completed paid job, rating ≥4 |
| **Agency overflow** | Small studio with pipeline spikes | Reliable subcontractors | Repeat subcontracts |

**Demand side (work)**

| Actor | Description | Primary need | Success signal |
| --- | --- | --- | --- |
| **Founder / startup** | Needs a thing built in weeks | Speed + trust, not the cheapest | Job posted → hired in <72h |
| **SME / non-tech business** | Needs a website, app, integration, audit | Plain-language scoping help | Repeat hire within 90 days |
| **NGO / donor project** | Needs delivery with accountability | Procurement-friendly evidence | Milestone sign-off |
| **Agency** | Needs overflow capacity | Vetted subs fast | Time-to-fill <48h |

**Platform-side actors** (these are users too, and they are the ones who break trust): reviewers/
assessors (D276), dispute officers (D180), trust & safety analysts (D178), support agents (D173).

## 3.4 The core loop

```
  Client posts structured brief
        │
        ├─▶ Platform parses to: skills[], level, budget range, deadline, deliverables
        │
        ▼
  Matching (rules first, ranking later)  ──▶ Talent sees ranked, explainable matches
        │
        ▼
  Proposal + scope agreement (milestones, acceptance criteria)
        │
        ▼
  Escrow funded  ──▶ Work happens (chat, files, milestone submissions)
        │
        ▼
  Client accepts (or auto-accept timer)  ──▶ Milestone released to wallet
        │
        ├─▶ Ratings both ways  ──▶ Reputation compounds  ──▶ Better matches (loop closes)
        └─▶ Dispute?  ──▶ Evidence → decision → split release → appeal window
```

**The loop that matters for retention is not "get hired". It is "get hired *again*."**
Repeat-hire rate is the metric that separates a marketplace from a job board. It is the North Star
candidate in §3.7.

## 3.5 The wedge strategy (why start here)

The classic marketplace mistake is launching both sides broadly in a city and waiting for liquidity.
The alternative: **start where trust already exists and the transaction is small enough to rehearse.**

| Phase | Wedge | Supply | Demand | Why it works | Kill/continue signal |
| --- | --- | --- | --- | --- | --- |
| P0 (weeks 1–8) | Concierge: founder matches 20 jobs by hand, no algorithm | 30 hand-verified specialists from the community | 20 real paid jobs | Proves willingness to pay and reveals the real brief format | <5 paid jobs closed → the demand is not there |
| P1 (weeks 8–20) | Skill-specific: mobile + backend implementation work only | 100 verified in 2 skills | Founders/SMEs with funded projects | Narrow scope = quality control; high willingness to pay | Dispute rate >10% → scoping product is wrong |
| P2 (months 5–9) | Add squads for larger jobs | Squad leads + juniors | Agencies, NGOs | Higher contract value; uses junior supply | Squad NPS <30 → coordination failure |
| P3 (month 9+) | Adjacent skills (data, security, design), 2nd city | Expand taxonomy | Expand | Only after repeat-hire rate >30% | Liquidity dilution |

**Refusal list (what we will not build in year one):** global talent supply (price race to the
bottom), full-time recruitment (different product, different law), training business (different
economics), crypto payments, an "AI replaces the freelancer" tool (kills supply trust).

## 3.6 Scope: MVP → v1 → v2

### MVP (must ship to learn, ~10–12 weeks)

| # | Capability | Acceptance (testable) |
| --- | --- | --- |
| M1 | Phone-number + OTP auth, profile, skill tagging | A new user completes signup in <90s on a 3G connection |
| M2 | Structured job brief (guided form: outcome, deliverables, skills, budget, deadline) | ≥80% of briefs pass validation without support contact |
| M3 | Search & rule-based matching (skill ∧ level ∧ availability ∧ location) | Median 5 qualified candidates shown; every result explains *why* it matched |
| M4 | Proposal + milestone scope agreement | Both parties e-sign scope; milestones sum exactly to total |
| M5 | Escrow-style funded milestone → release | Funds move only through ledger transitions; every transition idempotent |
| M6 | In-app chat + file sharing + milestone submission/acceptance | Message delivery <2s on 4G, retried offline; files virus-scanned |
| M7 | Two-sided ratings after completion | Rating editable for 14 days, then immutable; abuse-reportable |
| M8 | Admin console: verification queue, dispute queue, ledger view | Ops can resolve a dispute end-to-end without DB access |
| M9 | Notifications: push + SMS fallback for critical events | Critical events delivered or visibly escalated |
| M10 | KYC-lite: Ghana Card + selfie for payout eligibility | Verification decision in <24h (manual review acceptable) |

### v1 (trust & liquidity, months 4–9)

Skill assessments (ART-098), squad formation, saved talent lists, recurring engagements, invoice
PDFs, payout to MoMo + bank with reconciliation, dispute arbitration panel, employer accounts with
multiple seats, referral programme with anti-fraud, analytics for talent (profile views → proposals
→ hires).

### v2 (scale, months 9–18)

Ranking with learned relevance, price guidance, milestone auto-release timers, escrow with licensed
partner if volumes justify, multi-city, web app for employers, API for agencies, mobile-money
collection for clients, Ghana-wide expansion, second country only after unit economics are proven.

**Explicitly deferred:** video calls (integrate, do not build), time tracking (wrong model for
outcome-based work), equity-for-work, loans/advances to workers (regulated, dangerous).

## 3.7 Success metrics

**North Star (candidate):** *weekly completed paid engagements with a repeat or positive-rating
outcome.* It combines volume, quality and retention in one number and cannot be gamed by vanity
signups. Alternative considered and rejected: GMV (gamed by price inflation, ignores trust).

| Layer | Metric | Definition | Target (first 6 months) | Why it is here |
| --- | --- | --- | --- | --- |
| Acquisition | Verified signups/week | completed KYC-lite | 150/wk by month 6 | Funnel top; hypothesis H-010 |
| Activation | Time to first proposal | median hours, talent | <24h | Predicts retention better than profile completion |
| **Marketplace** | **Match-fill rate** | jobs filled ÷ jobs posted (7d) | ≥55% | The liquidity truth (H-002) |
| Marketplace | Time to hire | post → contract signed | <72h | The promise to clients |
| Delivery | On-time milestone rate | accepted on/before deadline | ≥80% | Operational quality |
| Trust | Dispute rate | disputes ÷ completed jobs | <5% | Scoping and matching quality |
| Trust | Repeat-hire rate (90d) | clients hiring again | ≥30% | The moat |
| Quality | Median rating / NPS | after completion | ≥4.5 / ≥40 | Demand-side confidence |
| Money | GMV and take rate | settled volume; fee % | GMV GHS 250k/mo by M6; take 8–12% | Viability |
| Cost | CAC per verified talent / client | blended | <GHS 25 / <GHS 120 | H-010 |
| Reliability | Crash-free sessions / p95 API | mobile / backend | ≥99.5% / <400ms | Table stakes |
| Safety | Fraud loss rate | losses ÷ GMV | <0.3% | Existential for trust |

All targets are **hypotheses**, not commitments; they are set so that being wrong is informative.
Every metric in this table has an owner in `01-role-catalog.md` and a definition in the analytics
plan (ART-030). A metric without a definition is a future argument.

## 3.8 Positioning

> *For founders and teams in Ghana who need real technical work done, **TechBro** is the trusted
> talent marketplace that turns "I know a guy" into a verified, escrowed, on-time delivery — because
> every worker is skill-verified, every payment is held until you accept the work, and disputes
> resolve in days.*

Against alternatives: LinkedIn (network, not delivery), Upwork/Fiverr (global price competition,
payment friction, no local verification), agencies (expensive, slow, opaque), WhatsApp referrals
(no protection), bootcamps (training, not delivery).

## 3.9 The riskiest assumptions (and the cheapest test for each)

Cross-referenced with `99-sources-and-assumptions.md`:

| ID | Assumption | Cheapest test | Cost | Time |
| --- | --- | --- | --- | --- |
| H-001 | Users will pay a 10% fee instead of going off-platform | Concierge phase: charge it from job #1; measure leakage | ~0 | 4 weeks |
| H-002 | Supply utilisation ≥55% per skill | Manual matching, instrument fill rate | ~0 | 6 weeks |
| H-003 | Clients fund escrow before work starts | A/B message framing on 40 job posts | ~0 | 3 weeks |
| H-006 | KYC completion before first paid match is tolerable | Hard gate on 50 talent, measure drop-off | Low | 3 weeks |
| H-010 | CAC ≤ GHS 25 for verified talent | 3 paid channels, 2 weeks each | ~GHS 3k | 6 weeks |

**Sequencing rule:** test H-001 and H-002 before writing any matching algorithm. A perfect ranker
on a market that will not pay is a beautifully engineered zero.

## 3.10 Naming and brand caveat

"TechBro" is used as the working name because it is the user's language and it carries the
community's tone. Two honest risks: (a) **inclusivity** — "bro" reads male-coded, which narrows
the supply side in a market where women are under-represented; (b) **trademark/domain
availability** is unknown and must be screened (ART-091, owner D282) before any spend on identity.
Alternatives to test with users: *Kasa* (speak/talk), *Nkwa* (life), *Sika Works*, *Forge*,
*Handoff*, *TalentBridge*. Do not settle the name before the trademark search.

## 3.11 Product principles (the tie-breakers)

1. **Trust is a feature with a UI.** Every screen either builds it or spends it.
2. **Money is sacred.** No feature ships if it can strand funds, double-pay, or hide a balance.
3. **Scoping beats matching.** Most disputes are specification failures, not skill failures.
4. **The phone is the office.** Assume 3G, 2GB RAM, intermittent power, data anxiety.
5. **Explain the match.** A ranking nobody can explain will not be trusted, and cannot be debugged.
6. **Both sides are users.** A marketplace that only listens to the payer loses the supply and dies.
7. **Cheap to try, expensive to abuse.** Friction goes on bad actors, never on first-time good ones.
8. **Ship the smallest reversible thing.** Reversibility is the real velocity.

## 3.12 What would make us kill this

Written now, while it is cheap to be honest (ART-009 requirement):

- Fewer than 5 paid jobs closed in the 8-week concierge phase despite 100 real conversations.
- Off-platform leakage >60% after three fee/pricing experiments.
- Match-fill below 30% for six consecutive weeks with supply ≥100 verified workers.
- Fraud losses >2% of GMV with controls in place.
- A legal position that requires a Bank of Ghana licence we cannot obtain, with no compliant
  third-party structure available (ART-041, ART-070).
