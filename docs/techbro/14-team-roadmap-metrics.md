# 14 — Team, Roadmap & Metrics

> This chapter converts 300 roles into **what 4 people actually do in week 1**, and converts ambition
> into a dated, testable sequence. The catalogue is the map; this is the route.

---

## 14.1 Team shapes by stage

| Stage | Headcount | Composition | Roles absorbed (from `01-role-catalog.md`) | What is deliberately *not* done |
| --- | ---: | --- | --- | --- |
| **Concierge** (m0–2) | 2–3 | Founder/CEO, full-stack engineer (or CTO), designer/PM hybrid | D001, D003, D061, D098, D099 | no ML, no squad features, no analytics stack |
| **MVP** (m2–5) | 4–6 | + backend engineer, + ops/support lead | + D100, D177, D172, D054 (part-time DPO) | no formal QA team (engineers own tests + SDET practices) |
| **Launch** (m5–9) | 7–9 | + QA/SDET, + growth, + trust & safety, + designer | + D121, D107, D178, D105 | no dedicated security (external pentest + D187 fractional) |
| **Scale** (m9–18) | 10–20 | + data engineer, + ML, + finance ops, + second squad | + D078, D084, D023, D193 | no microservices, no 24/7 rota |

**The "one person, many hats" rule:** at every stage, each person knows *which* catalogue roles they
hold and which artefacts they own. A hat that nobody claims is the artefact that will be missing at
the worst possible moment.

## 14.2 Seat plans

### Seat 1 — Founder / CEO (D001, D020, D005)
Owns: vision (ART-001), strategy (ART-009), funding (ART-012), partnerships, launch go/no-go.
Weekly time: 40% fundraising/partnerships, 30% concierge matching, 20% hiring, 10% product review.

### Seat 2 — CTO / founding engineer (D002, D061, D119)
Owns: architecture (ART-031/033), engineering standards (ART-051), delivery health.
Weekly: 60% hands-on code (money path, auth), 20% design/review, 20% hiring/mentoring.

### Seat 3 — Product / Design (D031, D105)
Owns: PRD (ART-016), screen inventory (ART-046), research cadence (ART-092), usability (ART-047).
Weekly: 40% discovery/interviews, 40% design/prototype, 20% analytics.

### Seat 4 — Backend / Platform (D099, D091)
Owns: API (ART-037), integrations (ART-065), deploy pipeline (ART-053), observability (ART-079).

### Seat 5 — Growth / Operations (D172, D229, D177)
Owns: support playbook (ART-062), acquisition experiments (ART-088), liquidity metrics (ART-089).

*(Seats 6+ as the stage table above.)*

## 14.3 RACI for the first 90 days

| Workstream | CEO | CTO | Product/Design | Backend | Growth/Ops |
| --- | --- | --- | --- | --- | --- |
| Concierge matching | **A/R** | I | C | I | R |
| Brief template | C | I | **A/R** | C | C |
| Escrow design + counsel | **A** | R | I | R | I |
| MVP build | I | **A** | C | R | I |
| KYC vendor selection | C | C | I | **A/R** | C |
| Store submissions | I | C | **A/R** | C | I |
| Support macros | I | I | C | C | **A/R** |
| DPC registration | **A** | I | I | I | C |
| Launch gate pack | **A** | R | R | R | R |

## 14.4 Hiring plan and sequencing

| Order | Role | When | Why now | Interview signal that matters |
| ---: | --- | --- | --- | --- |
| 1 | Founding full-stack engineer | now | nothing ships without code | has shipped and operated a payment flow |
| 2 | Product designer (contract → full) | m1 | brief/scoping UX is the wedge | can show a form that reduced support load |
| 3 | Ops/support lead | m3 | disputes and verification need a human owner | calm under angry users; process discipline |
| 4 | QA/SDET | m5 | money paths need dedicated verification | thinks in invariants, not checklists |
| 5 | Growth lead | m6 | liquidity needs a full-time owner | has grown a two-sided market locally |
| 6 | Trust & safety analyst | m7 | fraud arrives with volume | investigative patience + fairness |
| 7 | Data engineer | m9 | decisions need trustworthy data | has built a tested metrics layer |

**Hiring anti-patterns to avoid:** a "growth hacker" before retention exists; a data scientist before
labels exist; a security engineer before there is an attack surface worth staffing (use a fractional
expert + external pen test instead); a fifth engineer before the fourth is productive.

## 14.5 Twelve-month roadmap

| Quarter | Theme | Deliverables (mapped to artefacts) | Exit metric |
| --- | --- | --- | --- |
| **Q1** | Prove demand | Concierge 20 jobs (ART-008), brief template v1 (ART-016), escrow design + counsel memo (ART-041), MVP core (ART-037/046), DPC registration (ART-070) | ≥5 paid jobs, written licensing position |
| **Q2** | Launch safely | KYC-lite (ART-044), payouts (ART-041), MVP public in Accra (ART-081), support playbook (ART-062), security baseline (ART-066/067) | 100 verified talent, 30 jobs/month, dispute <10% |
| **Q3** | Build trust & liquidity | Ratings v1, disputes flow (ART-042), squads, assessments pilot (ART-098), referral (ART-088) | fill rate ≥55%, repeat hire ≥25% |
| **Q4** | Make it pay | Pricing experiments, employer accounts, second city prep, ranking v1 (ART-039), unit economics dashboard (ART-086) | contribution margin positive, GMV GHS 200k+/mo |

## 14.6 Two-week sprint template

| Day | Event | Output |
| --- | --- | --- |
| Mon (wk1) | Planning: pick from the top of the risk-ordered backlog | sprint goal, stories with AC |
| Tue–Thu | Build: TDD on domain rules, pairing on money paths | PRs ≤400 lines |
| Fri (wk1) | Mid-sprint check: demo-able increment? blockers? | adjusted scope |
| Mon–Wed (wk2) | Finish + verification (QA, authz, a11y) | evidence links |
| Thu (wk2) | Demo to real users (≥1 client, ≥1 talent) | feedback notes into ART-008 |
| Fri (wk2) | Retro (ART-094) + metrics review | 1–2 process changes, tracked |

**Sprint rule:** every sprint contains at least one **discovery** item and one **reliability** item.
A sprint of pure feature work is how marketplaces ship features nobody wanted and break the ones
they did.

## 14.7 Definition of Ready / Done

**Ready (ART-026):**
- [ ] User and job-to-be-done named
- [ ] Acceptance criteria in Given/When/Then
- [ ] Design link or explicit "no design needed"
- [ ] Test approach (unit/integration/e2e) named
- [ ] Analytics event named, if user-facing
- [ ] Dependencies resolved or flagged
- [ ] Sized (≤3 days; otherwise split)

**Done:**
- [ ] Merged to main with review
- [ ] Tests written and passing (TDD for domain rules)
- [ ] Acceptance criteria verified by someone who did not write it
- [ ] Analytics verified firing in staging
- [ ] Docs/runbook updated if operational behaviour changed
- [ ] Feature-flagged and rolled out per plan
- [ ] Accessibility checked for any new screen
- [ ] No new S1/S2 or unexplained S3 defects

## 14.8 Metrics: the full tree

```
North Star: Weekly completed paid engagements with a repeat or ≥4★ outcome
│
├── Demand
│   ├── Jobs posted / week
│   ├── Jobs filled within 7 days          ← fill rate
│   ├── Time to hire (median)
│   └── Repeat-hire rate (90d)
│
├── Supply
│   ├── Verified talent (cumulative)
│   ├── Active talent (proposed in 14d)
│   ├── Utilisation (paid days ÷ available days)
│   └── Supply per demand unit
│
├── Quality & trust
│   ├── Dispute rate
│   ├── Dispute resolution time
│   ├── On-time milestone rate
│   ├── Median rating / NPS both sides
│   └── Fraud loss ÷ GMV
│
├── Money
│   ├── GMV (settled)
│   ├── Take rate realised
│   ├── Contribution margin / job
│   ├── CAC / LTV (talent and client)
│   └── Payout success rate
│
└── System
    ├── Crash-free sessions / API p95
    ├── Funding success rate
    └── Support contacts per completed job
```

**Metric hygiene rules:** one definition per metric, stored in the analytics layer (ART-030), owned
by a named person, reviewed monthly. When two dashboards disagree, the metric is broken — stop and
fix it before using either number in a decision.

## 14.9 Operating cadence and decision rights

| Decision type | Who decides | Consultation | Recorded in |
| --- | --- | --- | --- |
| Vision/strategy pivot | CEO | board, CTO | ART-009 |
| Architecture | CTO | engineering | ADR |
| Pricing | CEO | finance + product | ART-011 |
| Product scope | Product | CEO, CTO | ART-027 |
| Hiring | CEO | team | hiring plan |
| Security exception | CTO + security owner | affected team | ART-014 |
| Launch go/no-go | CEO | all gate owners | ART-081 |

**Decision log rule:** every decision that costs more than a week or a month's budget gets a line:
date, decision, alternatives, who decided, and what would make us revisit it. Memory is a poor
auditor.

## 14.10 Growth and learning plan for the team

The team is building a skills marketplace; it should not be the least skilled-run platform in the
market.

| Role | 90-day goal | How |
| --- | --- | --- |
| Engineering | Every engineer can explain the ledger and restore a backup | internal workshop + drill |
| Product | Run 2 usability rounds solo | research playbook (ART-092) |
| Ops | Handle a dispute end-to-end within SLA | shadowing + rubric |
| Whole team | Security literacy (phishing, secrets, PII) | ART-291 training |

## 14.11 The honest scorecard (review monthly)

| Question | If "no", the fix is |
| --- | --- |
| Did we talk to ≥4 real users this month? | discovery cadence is broken |
| Did the North Star move in the right direction? | strategy or product |
| Are disputes under 5%? | scoping and quality |
| Is contribution margin per job positive? | pricing or cost |
| Is every gate for this month's releases evidenced? | process honesty |
| Did any S1/S2 recur? | postmortem follow-through failed |
| Is anyone on the team at risk of burnout? | staffing, scope, or expectations |
