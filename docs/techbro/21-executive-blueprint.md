# 21 — Executive Blueprint: The Complete System on Twelve Pages

> This is the pack compressed. Everything here is expanded — with sources, diagrams, DDL, runbooks
> and tests — in chapters 1–20. Read this first, then go to the chapter that you need to act on.
>
> **Working name:** TechBro · **Market:** Accra, Ghana · **Form:** cross-platform mobile marketplace
> **Stack:** React Native + Expo / Django + DRF / PostgreSQL / Redis + Celery

---

## 21.1 The one-paragraph system

A mobile marketplace where a tech professional who is over capacity delegates scoped work to a
verified peer, and someone who needs work done finds that person without gambling on a stranger.
The product is not a job board: it is **structured scoping + tiered verification + held money +
published dispute deadlines**. The promise to both sides is the same sentence — *"the work gets done,
and the money is handled safely"* — and every architectural decision in this pack exists to make that
sentence true.

---

## 21.2 The three jobs behind the idea (do not conflate them)

| # | Job to be done | Who | What they do today | What it costs them |
| ---: | --- | --- | --- | --- |
| **J1** | "I have more work than capacity — hand it to someone I can trust" | freelancers, agencies, senior devs | WhatsApp groups, referrals | turned-down revenue, quality risk |
| **J2** | "I need a specific skill for a defined outcome, fast" | founders, SMEs, NGOs | ask 6 groups and hope | weeks lost, scams, overpaying |
| **J3** | "I want real paid work to build a track record" | juniors, students, switchers | unpaid "collabs" | exploitation, no evidence |

**The wedge is J1 + a slice of J2.** Both sides are already inside the community, and trust transfers
fastest there. J3 is your supply pipeline, not your product (§3.5).

---

## 21.3 Architecture in one diagram

```
┌──────────────── iOS + Android (Expo React Native) ────────────────┐
│ 42 screens · offline queue · secure storage · 3G-first            │
└───────────────────────────┬───────────────────────────────────────┘
                            │ HTTPS/TLS 1.2+ · JWT (rotating) · cursor pagination
┌───────────────────────────▼───────────────────────────────────────┐
│              API — Django 5.2 LTS + DRF (modular monolith)         │
│  Identity │ Talent │ Demand │ Matching │ Contracts │ Money │       │
│  Reputation │ Disputes │ Comms │ Moderation   ← bounded contexts   │
└───────┬───────────────────────────────┬───────────────────────────┘
        │ transactional outbox          │
┌───────▼─────────────┐        ┌────────▼──────────────────────────┐
│ Celery workers      │        │ PostgreSQL 17 (system of record)  │
│ outbox · notify ·   │◄──────►│ ledger (append-only) · audit      │
│ reconcile · index   │        │ uuid v7 · integer pesewas         │
└───────┬─────────────┘        └────────┬──────────────────────────┘
        │                               │
┌───────▼─────────────┐        ┌────────▼──────────────────────────┐
│ Redis (cache/queue) │        │ Object storage (private, signed)  │
└─────────────────────┘        └───────────────────────────────────┘
        │
┌───────▼───────────────────────────────────────────────────────────┐
│ EXTERNAL: payment provider (splits/delayed settlement) · MoMo +   │
│ bank payouts · SMS/OTP · push · KYC/ID · LLM APIs · observability │
└───────────────────────────────────────────────────────────────────┘
```

**Why a monolith:** four people cannot operate microservices. Boundaries are enforced in code and
review so extraction is possible later, not required now (§4.9 ADR-004, §20.2).

---

## 21.4 The money model (the only part that must be right first time)

```
UNFUNDED ──fund──▶ FUNDED ──▶ IN_PROGRESS ──submit──▶ SUBMITTED
                                    │                    │
                              client accepts       dispute opened
                                    │                    │
                                    ▼                    ▼
                                 RELEASED ──▶ SETTLED   FROZEN ──▶ decision ──▶ SPLIT/REFUND
```

**Double-entry ledger, append-only, integer pesewas.** Seven account types, eight tested invariants,
reconciliation queries that must return zero rows (§5.4).

**The four invariants that matter:**
1. Σ debits = Σ credits per transaction.
2. escrow liability = funded − released − refunded, always.
3. No ledger row is ever updated or deleted (DB rule, not convention).
4. A payout never exceeds the wallet balance (row-locked check).

**Licensing (Act 987 — S5):** holding client money can require a Bank of Ghana licence. Three
postures, in order (§4.5):

| Posture | Mechanism | Use when |
| --- | --- | --- |
| **A. Provider split + delayed settlement** | provider holds the talent share; you trigger release | launch |
| **B. Licensed escrow partner** | a licensed institution holds funds, tripartite agreement | volume justifies it |
| **C. Own licence** | BoG authorisation | scale |

**Critical honesty:** Paystack states it does **not** offer true escrow, release is one-directional,
and refunds on settled splits come from your own balance (S11). So: never call it escrow in the
T&Cs; fund refunds from a bounded reserve; keep the ledger so the posture can change without a data
migration. And note **Stripe Connect is not available to a Ghanaian entity** (S56) — a plan built on
it is built on sand (§20.3.1).

---

## 21.5 The 300 roles, mechanically

The role catalogue is not prose — it is data, validated at build time.

```
19 families · 300 roles · 110 artefacts · 3.0 artefacts per role
Each role: id · title · family · artefact(s) owned · inputs→outputs
           · core skill · Bloom ceiling · AI leverage · KPI
```

| Family | Roles | Family | Roles |
| --- | ---: | --- | ---: |
| Security | 38 | Growth | 13 |
| Operations | 32 | Research | 13 |
| Quality | 29 | People | 12 |
| Engineering | 27 | Delivery | 11 |
| Business | 21 | Content | 10 |
| Data | 16 | Design | 10 |
| AI | 15 | Governance | 8 |
| Architecture | 14 | Leadership | 6 |
| Finance | 14 | Product | 6 |
| | | Legal | 5 |

**Bloom distribution is the design intent:** roles cluster at *Apply/Analyse/Evaluate/Create* — the
levels where being wrong is expensive — because AI absorbs recall and retrieval. Machines draft;
humans own judgement and consequences (§1.2).

**Three mechanically enforced rules:**
1. every role owns at least one artefact;
2. every artefact has exactly one accountable owner;
3. every artefact has a written definition of done.

Break any of them and `tools/gen_blueprint.py` fails the build.

---

## 21.6 The SDLC operating model: 8 cells, 7 gates

| Cell | Question | Artefacts |
| --- | --- | ---: |
| Discover | is it true? | 15 |
| Define | what exactly, for whom? | 12 |
| Architect | how does it hold up? | 12 |
| Build | make it real, reversibly | 8 |
| Assure | how do we know it works? | 14 |
| Secure | who attacks it, and what stops them? | 12 |
| Deploy | how does it reach users, and come back? | 14 |
| Sustain | is it still working and affordable? | 23 |

| Gate | Between | Fails if |
| --- | --- | --- |
| **G0 Problem** | Discover → Define | the pain is inferred, not observed |
| **G1 Scope** | Define → Architect | NFRs are adjectives; roles undefined |
| **G2 Design** | Architect → Build | money/trust paths undesigned |
| **G3 Ready** | Build entry | no acceptance criteria or test approach |
| **G4 Verification** | Assure → Secure | critical paths untested |
| **G5 Security** | Secure → Deploy | open critical/high without written acceptance |
| **G6 Launch** | Deploy → Sustain | rollback unproven; compliance evidence missing |
| **G7 Review** | Sustain → Discover | no metric movement, no honest cost accounting |

**Tailoring:** a 6-person team cannot produce 110 artefacts. §2.10 names the ~27 that are mandatory
pre-seed and puts every skipped one on the risk register with a date. Skipping is a decision; silence
is an omission.

---

## 21.7 The MVP (10 capabilities, ~10–12 weeks)

| # | Capability | Acceptance bar |
| ---: | --- | --- |
| M1 | Phone + OTP auth, profile, skill tags | signup <90s on 3G |
| M2 | Structured brief (outcome, deliverables, budget, deadline) | ≥80% pass validation unaided |
| M3 | Rule-based matching with explanations | median 5 qualified, each explains why |
| M4 | Proposal + milestone scope agreement | milestones sum exactly to total |
| M5 | Escrow-style funding → release | every transition idempotent, ledger-backed |
| M6 | Chat + files + milestone submit/accept | survives offline, ordering stable |
| M7 | Two-sided ratings | 14-day editable, then immutable |
| M8 | Admin console: verification, disputes, ledger | resolve a dispute with no DB access |
| M9 | Push + SMS fallback for money events | delivered or visibly escalated |
| M10 | KYC-lite (Ghana Card + selfie) before payout | decision <24h |

**Explicitly deferred:** video calls, time tracking, equity-for-work, worker advances (regulated),
multi-currency, global supply.

---

## 21.8 Trust engineering (matching, reputation, disputes)

**Matching:** hard filters first (skill ∧ level ∧ availability ∧ city ∧ rate), then a transparent
7-signal weighted score with a version and a plain-language explanation. Learned ranking only after
**2,000 completed engagements** — because before that you have no labels, and a model trained on
nothing is a random number generator with a dashboard (§7.4).

**Reputation:** Bayesian-smoothed five-star average + trust band + *which inputs produced it*. Inputs
weighted: client ratings 40%, completion 20%, on-time 15%, responsiveness 10%, dispute outcomes 10%,
verification 5%. Decays, so one bad month does not ruin a career and an old five-star cannot coast.
Anti-gaming is designed in, not bolted on (§7.5).

**Disputes, three layers so most never reach a human:**

| Layer | Mechanism | Handles |
| --- | --- | --- |
| L0 | prevention: structured brief + acceptance criteria + milestones | ~60% |
| L1 | self-resolution: "request changes" with checklist, 72h | ~30% |
| L2/L3 | mediation → adjudication, written rationale, one appeal | ~10% |

Dispute freezes escrow. Evidence is append-only and visible to **both** sides. Decisions are made
against the written acceptance criteria — and if the criteria were vague, that is logged as a *brief
defect*, because it is a product bug, not a customer problem. Published SLA: first response 24h,
decision 5 business days, appeal 5 business days.

---

## 21.9 AI: twelve use cases, three refusals

**Ships:** brief assistant (parse plain language → structured brief), skill extraction, proposal
summarisation, semantic search, fraud-signal clustering, dispute evidence digest, support RAG,
assessment question generation, internal copilots.

**Refused, permanently:**
- AI deciding who gets paid;
- AI deciding disputes autonomously;
- AI silently hiding candidates from search.

**Why the refusals matter:** two of the three cause irreversible harm to someone's income. No model
card repairs a wrongly denied wage.

**Discipline:** every AI feature has a golden set, a cost ceiling (≤2% of the platform fee on that
action), a version record, and a named human accountable when it is wrong. The flagship brief
assistant must **never invent scope** — unknown fields return `null` plus a question, and budget
ranges come from your own historical data or are absent (§8.2).

---

## 21.10 Security & compliance (Ghana-first)

| Layer | Baseline |
| --- | --- |
| Web/API | OWASP ASVS 5.0.0 Level 2 (S20), API Top 10 — BOLA is threat #1 (S34) |
| Mobile | OWASP MASVS 2.1.0, profile L2 + P (S21) |
| Threat model | STRIDE per trust boundary (S14) + LINDDUN for privacy (S15) |
| Severity | CVSS v4.0 (S22); critical 24h, high 7d, medium 30d |
| Audit | append-only, hash-chained, 4-eyes on money adjustments |

**Ghana register (verified 2026-11-06):**

| Area | Instrument | Obligation |
| --- | --- | --- |
| Data protection | Act 843 (S2) | **register with the DPC before processing**; renew 2-yearly |
| Cross-border | Act 843 transfer rules (S3) | adequacy / safeguards / BCR basis |
| Payments | Act 987 (S5) | no payment service without BoG licence |
| E-levy | Repeal Act 2025 (S6) | abolished 2 Apr 2025 — do not price it in |
| Records | Act 915 s.27(3) (S27) | keep transaction records ≥6 years |
| Identity | NIA Ghana Card (S36) | accepted KYC document |
| Stores | Apple 3.1.3(d)/(e) (S18), Google Play (S19) | real-world services ≠ in-app purchase |

**Non-negotiables:** no PII in logs; identity documents encrypted with a separate key and
ticket-based access; DSAR path in-app; no claimed certifications you do not hold.

---

## 21.11 Testing & operations

**Risk-ordered testing** — money first, then authorization, then disputes, then bad-network mobile,
then matching quality. Property-based ledger invariants (8 of them), chaos drills on webhook replay,
a role×endpoint authz matrix that must be 100% green.

**Quality gates:** unit+integration green; ≥90% coverage *plus ≥60% mutation score* on money/auth/
disputes; critical E2E zero-flake; p95 within SLO; zero open critical/high; rollback rehearsed.

**Kill switches built in advance:** funding, release, payouts, matching-v2, AI assistant, signup,
read-only mode. Each exercised monthly.

**The one that matters most — RB-02, ledger drift:**
```
alert → declare S1 → freeze release+payouts → reconcile (≤30 min)
     → contain → CORRECT WITH COMPENSATING ENTRIES (never delete)
     → two-person approval → communicate → unfreeze only when reconciliation
       is clean AND a regression test reproduces the bug → postmortem ≤5 days
```

---

## 21.12 Business model & the competitor reality

**Revenue:** 8–12% client-side take rate (preferred), subscriptions in v1, assessments/featured in
v2. **Not** worker-side 10% — because Braintrust charges talent 0% (S53) and Fiverr already takes
20% from sellers plus fees from buyers (S54), so a worker fee has no defensible story.

**Unit economics (illustrative, all assumptions labelled):** GHS 4,000 median job → GHS 400 gross →
~GHS 120 costs (PSP ~1.95%, payout, SMS, KYC, LLM, infra, support) → **~70% contribution margin**.
The model breaks if take rate <6% (leakage), disputes >15%, or job value <GHS 1,200.

**Competitor summary (full teardown in §19):**

| Platform | Model | Fee | What they get right | What they get wrong (your opening) |
| --- | --- | --- | --- | --- |
| **Upwork** | open global marketplace | ~10% freelancer (0–15% reported) + ~5% client (S51) | escrow default, portable reputation | scoping dumped on users; price anchored to $2–10/hr in Accra listings |
| **Fiverr** | productised gigs | 20% seller + 5.5% buyer (S54) | frictionless, pre-scoped | ~24–29% total take; engineering is not a SKU |
| **Toptal** | curated elite network | 0% talent, 30–50% client markup (S52) | verification *is* the product | 3% acceptance starves a community; no SMEs |
| **Braintrust** | user-owned network | **0% talent, 10% client** (S53) | right side to charge | token governance adds risk with no local benefit |
| **Andela** | managed outsourcing | built into $6k–14k/month/dev (S55) | proves African talent demand | 12-month minimums; no Saturday-afternoon help |
| **GH regional** | local marketplaces | mixed | mobile money, local presence | thin verification, no real escrow/disputes |

**The strategic fork:** local trust marketplace (local moat, lower revenue) vs export talent network
(higher revenue, becomes a staffing agency) vs peer collaboration (high engagement, poor
monetisation). Recommendation: **build A to earn the verified-supply graph, then add B on top**
(§19.11).

---

## 21.13 Team, roadmap, metrics

| Stage | People | Adds | Exit metric |
| --- | ---: | --- | --- |
| Concierge (m0–2) | 2–3 | — | ≥5 paid jobs closed manually |
| MVP (m2–5) | 4–6 | backend, ops/support | 100 verified talent, 30 jobs/mo |
| Launch (m5–9) | 7–9 | QA, growth, T&S | fill rate ≥55%, dispute <10% |
| Scale (m9–18) | 10–20 | data, ML, finance ops | contribution margin positive |

**North Star:** weekly completed paid engagements with a repeat or ≥4★ outcome.
**The five numbers on the wall:** fill rate (7d) · repeat-hire rate (90d) · dispute rate ·
contribution margin per job · verified supply per demand unit.

**Capacity honesty:** a 4-person team has ~7 engineer-days of feature work per week, not 20
(§15.6). Plan accordingly or be "late" for knowable reasons.

---

## 21.14 Build / buy / reorder (short version)

| Build (it is the moat) | Buy (commodity or regulated) | Reorder (delete the problem) |
| --- | --- | --- |
| ledger + reconciliation | payment rails & settlement | instant payouts → next business day |
| brief assistant + evals | KYC/identity | video interviews → written assessments |
| matching v0/v1 | SMS/OTP/push/email | multi-currency → GHS only |
| reputation & disputes | LLM APIs, hosting, search | time tracking → outcome milestones |
| admin console (protection) | observability, flags | real-time collaboration → async review |

**Build expensively only one thing: the trust layer.** Everything else should be boring or bought
(§15.8).

---

## 21.15 What is decided, what is not

**Decided (with ADRs in §17.3):** Django+DRF, PostgreSQL, Expo/RN, modular monolith + outbox,
Celery+Redis, provider-split money posture with own ledger, rule-based matching first, server-rendered
admin, integer-pesewas money, no paid placement year one, AI never decides payouts/disputes,
Ghana-only launch, phone-first auth.

**Not decided — only you can answer (12 questions in §18.2):**
who your first 50 customers are · profit vs impact · how you get paid · whether money moves at
launch · who verifies skill · launch geography · which skills first · team technical depth · runway ·
existing community · your kill criteria · your 12-month success number.

**Every one of those changes specific chapters — the impact map is in §18.3.**

---

## 21.16 Next 14 days (risk-ordered)

| Day | Action | Output |
| ---: | --- | --- |
| 1–2 | one-page vision + written kill criteria | ART-001, ART-009 |
| 2–4 | 6 customer conversations (3 supply, 3 demand) | raw notes, ≥3 quotes each |
| 3 | send the payments question to counsel | appointment booked |
| 5 | price test: "would you pay 10% for escrow + disputes?" verbatim answers | evidence log |
| 6–7 | brief template on paper; run 3 real briefs manually | brief v1 + observed friction |
| 8–10 | concierge: hand-match 3 real jobs, take a fee | first revenue, dispute patterns |
| 9 | file DPC registration | receipt (long clock — S2) |
| 11 | choose payment posture with counsel; open sandbox | written posture note |
| 12–13 | draft the 12 MVP screens; test with 3 users | screen inventory v1 |
| 14 | **decide: build, or re-test the wedge** | written decision |

**Success bar day 14:** ≥2 paid jobs completed manually **and** 1 written legal position on
payments. If not, more discovery — not more code.

---

## 21.17 The five sentences that decide whether this works

1. The product is **structured scoping and safe money**, not a job board — and that is why someone
   will pay 10% instead of using WhatsApp.
2. The **ledger and the licensing posture** are the only things that must be perfect on day one;
   everything else can iterate.
3. **Charge the client**, never the worker, because the market has already been taught that workers
   should not pay (Braintrust 0%, and Fiverr's 20% is why its sellers leave).
4. **Verification is the moat** — tiered, visible, and honest about what is and is not checked.
5. **The wedge is one city and two skills.** Breadth is how the incumbents win; depth is the only
   game available to four people.

---

## 21.18 Where to go next

| If you want… | Go to |
| --- | --- |
| the full role catalogue | §01 (300 roles, 19 families) |
| competitor detail with sources | **§19** |
| the critique of the two pasted blueprints | **§20** |
| the questions to answer | **§18.2** |
| the money design | §4.5, §5.4, §6.4 |
| the security/compliance register | §9.6 |
| the launch gate checklist | §12.9 |
| every source | §99 |
| the 110 deliverables with definitions of done | `artifacts/00-artifact-index.md` |
