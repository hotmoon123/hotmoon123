# 17 — Governance, Decision Records & Risk

> Governance in a small company is not a board pack; it is **the habit of writing down what you
> decided, why, and what would change your mind.** Everything here exists to make future-you able to
> audit present-you without relying on memory.

---

## 17.1 Decision-making framework

| Decision class | Reversibility | Who decides | Process | Record |
| --- | --- | --- | --- | --- |
| **Type 1** — one-way door (licensing posture, ledger design, naming, data residency) | Low | CEO + CTO, with specialist input | written options paper, 48h comment window | ADR + board note |
| **Type 2** — two-way door (UI copy, ranking weights, vendor for SMS) | High | Individual owner | decide fast, instrument, revisit | ticket + changelog |
| **Type 3** — experimental (pricing variant, feature hypothesis) | High | Product owner | hypothesis + metric + kill date | ART-088 |

**Rule:** spend deliberation in proportion to reversibility, not to how loudly someone feels about
it. Most arguments in startups are Type 3 decisions treated as Type 1.

## 17.2 ADR template (ART-031)

```markdown
# ADR-NNN: <title>
Status: proposed | accepted | superseded by ADR-XXX | rejected
Date: YYYY-MM-DD
Owners: <role ids>
Context: what forces are at play (constraints, regulations, user needs, costs)
Options considered: A / B / C — with the honest trade-off of each
Decision: what we will do
Consequences: what becomes easier, what becomes harder, what we are now committed to
Revisit if: the specific signal that should reopen this decision
```

**A rejected option must be written down.** The cheapest institutional memory is the reason you
*didn't* do the obvious thing.

## 17.3 Decision log (seed)

| ID | Decision | Date | Owner | Class | Status | Revisit if |
| --- | --- | --- | --- | --- | --- | --- |
| ADR-001 | Django 5.2 LTS + DRF (S40) | 2026-11-06 | D002 | 1 | accepted | team language changes, or API latency becomes unacceptable |
| ADR-002 | PostgreSQL 17 as system of record (S42) | 2026-11-06 | D002 | 1 | accepted | write throughput exceeds a single primary at 10× growth |
| ADR-003 | Expo React Native for cross-platform | 2026-11-06 | D002 | 1 | accepted | camera/liveness or heavy media becomes core |
| ADR-004 | Modular monolith + transactional outbox | 2026-11-06 | D061 | 1 | accepted | a context needs independent scaling or a separate team |
| ADR-005 | Celery + Redis for async work (S43) | 2026-11-06 | D091 | 2 | accepted | managed queue offers materially better reliability |
| ADR-006 | Data residency: regional hosting with documented transfer basis | 2026-11-06 | D054 | 1 | **proposed** | DPC guidance changes, or cost of Ghana-region hosting drops |
| ADR-007 | Provider-split money posture at launch; own ledger always | 2026-11-06 | D018 | 1 | accepted | volume justifies a licensed escrow partner, or counsel advises otherwise |
| ADR-008 | Rule-based matching before learned ranking | 2026-11-06 | D084 | 1 | accepted | ≥2,000 completed engagements with stable taxonomy |
| ADR-009 | Server-rendered admin console | 2026-11-06 | D099 | 2 | accepted | admin workflows need rich interactivity |
| ADR-010 | Money as integer minor units + ISO currency | 2026-11-06 | D100 | 1 | accepted | multi-currency with FX requires a treasury design |
| ADR-011 | No paid placement in ranking, year one | 2026-11-06 | D003 | 1 | accepted | never, without explicit disclosure design |
| ADR-012 | AI never decides payouts or disputes autonomously | 2026-11-06 | D269 | 1 | accepted | never |
| ADR-013 | Ghana-only launch; second country after unit economics | 2026-11-06 | D001 | 1 | accepted | positive contribution margin for 2 consecutive quarters |
| ADR-014 | Phone-first auth (no passwords) | 2026-11-06 | D152 | 2 | accepted | significant account-takeover signal from SIM swap |

## 17.4 Risk register (top 15, scored)

Score = likelihood (1–5) × impact (1–5). Anything ≥ 12 has a mitigation owner and a date.

| ID | Risk | L | I | Score | Mitigation | Owner | Review |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| R-01 | Payment licensing perimeter breached by our escrow mechanism | 3 | 5 | **15** | written counsel opinion; provider posture A; ledger switchable to posture B (ART-041) | D018 | monthly |
| R-02 | Market does not pay fees; leakage to WhatsApp | 4 | 5 | **20** | charge from job #1 in concierge phase; measure leakage monthly; value adds (escrow, dispute) that off-platform cannot match | D001 | weekly |
| R-03 | Fraud (fake profiles, payout redirection) destroys trust | 3 | 5 | **15** | KYC gate before payout; destination cooling; fraud playbook; anomaly detection (ART-072) | D179 | weekly |
| R-04 | Dispute volume outruns the ops team | 3 | 4 | 12 | scope-first product design; self-resolution layer; SLA dashboards; brief-defect analysis | D180 | weekly |
| R-05 | Data breach of identity documents | 2 | 5 | 10 | separated encryption keys; access tickets + audit; minimisation; pen test | D187 | monthly |
| R-06 | Liquidity never reached (supply or demand thin) | 3 | 5 | **15** | narrow wedge (2 skills, 1 city); concierge matching; supply-first seeding | D240 | weekly |
| R-07 | Key-person dependency (2–4 people) | 3 | 4 | 12 | documented runbooks; pair on money path; no single-owner modules | D119 | monthly |
| R-08 | SMS/KYC/LLM vendor outage or price shock | 3 | 3 | 9 | two vendors per critical channel; cost ceilings; graceful degradation | D028 | quarterly |
| R-09 | App store rejection (payments/UGC rules) | 2 | 4 | 8 | pre-submission review against S18/S19; dispute flow + reporting built in | D059 | per release |
| R-10 | Burnout of a small team during launch | 3 | 4 | 12 | rota honesty; scope cut lines; launch is gated not dated | D005 | monthly |
| R-11 | Ranking bias erodes supply | 3 | 3 | 9 | slice metrics; constrained exposure; new-talent boosts | D090 | monthly |
| R-12 | Legal claim from a worker misclassification | 2 | 4 | 8 | contractor terms reviewed by counsel; no control signals that imply employment | D017 | pre-launch |
| R-13 | Currency/inflation erodes unit economics | 3 | 3 | 9 | price reviews quarterly; GHS-only revenue; cost ceilings | D021 | quarterly |
| R-14 | Global competitor enters with subsidised pricing | 2 | 4 | 8 | trust depth, local dispute speed, community; do not price-war | D001 | quarterly |
| R-15 | AI feature produces harmful advice and goes viral | 2 | 4 | 8 | labelling, guardrails, human-in-loop, kill switch, red-team | D269 | monthly |

## 17.5 Governance bodies (right-sized)

| Body | Members | Cadence | Decisions | Quorum |
| --- | --- | --- | --- | --- |
| Operating review | CEO, CTO, Product, Ops | weekly | execution, unblocking | 3 |
| Risk & security review | CTO, DPO (fractional), Ops | monthly | risk acceptances, control gaps | 3 |
| Product council | CEO, Product, CTO, 1 user-research voice | fortnightly | scope, prioritisation | 3 |
| Advisory board | CEO, 2 external advisors | quarterly | strategy, introductions | informal |
| Dispute appeal panel | Ops lead + one uninvolved senior | as needed | final dispute appeals | 2 |

## 17.6 Policies that must exist before launch

| Policy | Minimum content | Owner | Evidence |
| --- | --- | --- | --- |
| Privacy notice | what, why, who, how long, rights, contact, transfer basis | D054 | published URL + version |
| Terms of service | fees, escrow mechanism, obligations, liability, dispute process, termination | D017 | published URL + version |
| Acceptable use / community policy | prohibited work, harassment, off-platform payment solicitation | D167 | published |
| Refund & cancellation policy | pre-start refunds, partial milestones, dispute outcomes | D017 | published |
| Contractor agreement | independent contractor status, IP assignment, payment terms | D017 | signed at onboarding |
| Security policy (internal) | access, devices, incident reporting, secrets | D187 | ART-070 |
| Data retention & deletion policy | per data class, legal holds | D203 | ART-085 |
| Vulnerability disclosure policy | contact, safe harbour, SLA | D191 | ART-077 |
| Complaint handling | channels, SLA, escalation | D172 | ART-062 |

**None of these may be copied from a template without reading every clause.** A policy that
contradicts the product is worse than no policy, because it is enforceable against us.

## 17.7 Accountability and ethics

| Commitment | Practical meaning | Owner |
| --- | --- | --- |
| Fair treatment of workers | no fee for applying; transparent payouts; disputes decided on evidence; appeal path | D167 |
| No dark patterns | no fake urgency, no hidden fees, no roach-motel cancellation | D105 |
| Data minimisation | collect only what a flow needs; delete on schedule | D054 |
| Algorithmic transparency | match reasons shown; ranking changes documented | D090 |
| Accessible by default | WCAG 2.2 AA on critical journeys | D128 |
| Honest marketing | no claimed certifications; no invented statistics | D282 |
| Incident honesty | tell users what happened, promptly, in plain language | D005 |

## 17.8 Board/investor reporting (monthly, 1 page)

1. North Star and the three inputs.
2. Liquidity: fill rate, supply/demand ratio, time to first proposal.
3. Trust: dispute rate, resolution time, fraud losses.
4. Money: GMV, revenue, contribution margin per job, burn, runway.
5. Risks changed this month (only changes).
6. The single ask (intro, hire, decision).

**One page is a discipline, not a constraint.** If it does not fit, the business has more problems
than the board can solve in a meeting.

## 17.9 Audit trail requirements

| Event | Retained | Contains | Immutable |
| --- | --- | --- | --- |
| Ledger entries | 7 years (S27) | amounts, wallets, txn, reference | yes (DB rule) |
| Payout records | 7 years | destination last-4, provider ref, status | yes |
| Verification decisions | 7 years | actor, evidence hash, outcome | yes |
| Admin actions | 7 years | actor, before/after, IP hash | yes (hash-chained) |
| Dispute decisions | 7 years | rationale, evidence refs, reviewer | yes |
| Consent records | life of account + 2 years | notice version, timestamp, scope | yes |
| Access to sensitive documents | 2 years | who, when, ticket ref | yes |

## 17.10 The governance test

A decision record is adequate if a competent stranger could read it in two years and answer:
**what did we decide, what did we give up, and what should make us revisit it?** If not, it is a
note, not governance.
