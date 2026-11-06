# 12 — Runbooks, Operations & Launch

> A runbook is written for the person who is half-awake at 02:00 and has never seen this system
> before. If it needs tribal knowledge, it is not a runbook — it is a wish.

---

## 12.1 On-call model (pre-seed reality)

| Aspect | Decision | Rationale |
| --- | --- | --- |
| Rota | 1 engineer/week, secondary as backup; founder is final escalation | A 4-person team cannot run a formal 24/7 follow-the-sun rota |
| Hours | 07:00–23:00 GMT active; outside hours, S1 auto-pages | Honest about what a small team can sustain |
| Escalation | Pager → secondary (15 min) → founder (30 min) | |
| Handover | Written at end of week: open incidents, ongoing risks, pending deploys | Prevents "nobody knows" |
| Compensation | Time off in lieu, documented | Burnout is a reliability risk |
| Postmortem | Within 5 business days for S1/S2, blameless | S23/S26 |

## 12.2 Severity & first 10 minutes

| Sev | Trigger | First 10 minutes | Comms |
| --- | --- | --- | --- |
| S1 | money loss, data breach, full outage | declare incident, open bridge, check status page, stop the bleeding (§12.3) | status page + founder + affected users within 60 min |
| S2 | one critical function down | assign owner, check recent deploys, rollback if suspect | status page |
| S3 | degraded, single user | create ticket, handle in business hours | direct to user |
| S4 | cosmetic | backlog | none |

**The first question is never "what broke?" It is "is money moving wrongly right now?"** If yes,
freeze the money subsystem before debugging anything else.

## 12.3 Kill switches (built in advance, tested monthly)

| Switch | Effect | Who can flip | Where |
| --- | --- | --- | --- |
| `payments.funding.enabled` | blocks new escrow funding | on-call + finance | feature flag console |
| `payments.release.enabled` | blocks milestone release | on-call + founder | feature flag console |
| `payouts.enabled` | blocks all outbound payouts | on-call + finance | wallet admin (4-eyes) |
| `matching.v2.enabled` | falls back to v1 weighted score | on-call | feature flag |
| `ai.brief_assistant.enabled` | falls back to manual form | on-call | feature flag |
| `signup.enabled` | pauses new registrations | on-call | feature flag |
| `readonly_mode` | serves cached reads; writes rejected with clear message | on-call + founder | infra switch |

**Requirement:** each switch is exercised in staging every month, and its effect is documented in
the user-facing message so support can explain it.

## 12.4 Runbook index (ART-073/082/083)

| ID | Runbook | Trigger | Owner |
| --- | --- | --- | --- |
| RB-01 | **Escrow funding failing** | funding error rate > 5% for 10 min | D100 |
| RB-02 | **Double release detected** | ledger invariant alert | D100 + D023 |
| RB-03 | **Payout provider outage** | provider status + our error rate | D193 |
| RB-04 | **Webhook signature failures spike** | > 1% verify failures | D103 |
| RB-05 | **Database failover** | primary unreachable | D213 |
| RB-06 | **Redis/Celery backlog** | queue depth > 50k or lag > 10 min | D091 |
| RB-07 | **OTP delivery failure** | verify success < 60% | D166 |
| RB-08 | **Data breach suspicion** | abnormal export/access alert | D156 |
| RB-09 | **Fraud ring detected** | T&S signal threshold | D179 |
| RB-10 | **Dispute SLA breach risk** | > 20% of open disputes near deadline | D180 |
| RB-11 | **Mobile crash spike** | crash-free < 98% on one build | D098 |
| RB-12 | **Rollback a bad release** | guardrail breach | D218 |
| RB-13 | **Restore from backup** | data loss event | D227 |
| RB-14 | **Account takeover wave** | auth anomaly | D152 |
| RB-15 | **KYC vendor outage** | verification backlog | D154 |

### RB-02 in full (because it is the scariest)

```
TRIGGER: nightly reconciliation reports Σ escrow_liability ≠ funded − released − refunded
         OR any wallet balance ≠ ledger sum

1. DECLARE S1. Page on-call, founder, finance owner. Open incident channel.
2. FREEZE: flip payments.release.enabled and payouts.enabled OFF.
   → Users see: "Payouts are paused for a scheduled check. Your balance is safe."
3. ASSESS (≤30 min):
   a. Run reconciliation queries (§5.4) and capture output verbatim into the incident doc.
   b. Identify affected milestones/payouts by reference id.
   c. If a payout already left the platform: note provider reference, do NOT attempt a reverse transfer
      without finance sign-off.
4. CONTAIN:
   a. Disable the specific code path via flag if identifiable.
   b. If data corruption: stop writes to the affected tables (readonly_mode).
5. CORRECT (never delete):
   a. Write compensating ledger entries with a new txn and a memo referencing the incident id.
   b. Two-person approval (finance + engineering) recorded in audit_log.
   c. Re-run reconciliation until zero rows.
6. COMMUNICATE: affected users within 24h with what happened, what we did, what they get.
7. UNFREEZE only when reconciliation is clean AND a regression test reproduces the original bug.
8. POSTMORTEM within 5 business days; systemic fix tracked to closure.
```

## 12.5 Release process

| Stage | What happens | Gate | Rollback trigger |
| --- | --- | --- | --- |
| 1. Build | CI builds immutable image, runs unit/integration/SAST/SCA | all green | — |
| 2. Staging deploy | migrations dry-run, E2E, authz matrix, perf smoke | gates in §11.7 | auto |
| 3. Internal release | 1% users (staff devices) via store internal track / EAS channel | no S1/S2 in 24h | manual |
| 4. Canary 5% | guardrails: error rate, crash-free, payout failures, p95 | within thresholds 48h | automatic halt |
| 5. 25% → 100% | staggered | monitored | manual |
| 6. Post-release | changelog, support briefing, metrics review at D+3, D+14 | — | — |

**Database migrations run before code and must be backward compatible with the previous release**
(expand/contract), because during a canary both versions run simultaneously.

## 12.6 Support operations

| Tier | Scope | Target first response | Escalates to |
| --- | --- | --- | --- |
| Tier 1 | account, how-to, OTP, refunds FAQ | 2h (business), 12h (off-hours) | Tier 2 |
| Tier 2 | payments stuck, verification, dispute intake | 4h | engineering / T&S |
| Tier 3 | engineering investigation | 1 business day | incident process |

**Top intents** (designed macros in ART-062): "where is my money", "verification rejected",
"client not responding", "milestone accepted by mistake", "payout failed", "how do fees work",
"someone asked me to pay off-platform", "my account was accessed".

Every intent has a macro, a decision tree, and an analytics event so we can see which flows generate
contacts. **Support contact rate per completed job is a product metric, not a support metric.**

## 12.7 Observability

| Signal class | What | Alert threshold | Runbook |
| --- | --- | --- | --- |
| RED (services) | rate, errors, duration per endpoint | error rate > 2% 5 min | RB-05 |
| Money invariants | reconciliation jobs | any nonzero | RB-02 |
| Queue health | depth, age, failures | lag > 10 min | RB-06 |
| Auth | OTP success rate, refresh failures | < 60% / > 5% | RB-07/RB-14 |
| Mobile | crash-free sessions, ANR rate, cold start | < 98% / > 0.5% / > 4s | RB-11 |
| Business guardrails | funding success, payout failures, dispute SLA | per SLO | RB-01/03/10 |
| Cost | SMS per hour, KYC calls, LLM tokens per hour | 3× daily median | cost review |

**SLOs** (ART-080): availability 99.5% monthly (API), p95 latency < 400 ms, funding success ≥ 97%,
payout settlement within 1 business day ≥ 95%, dispute first response within 24h ≥ 95%.

Error budget policy: if a service burns > 50% of its monthly budget in a week, feature work on that
service pauses until reliability work restores it. Written down so it survives pressure.

## 12.8 Launch plan (12 weeks to first paid job)

| Week | Focus | Exit criteria |
| ---: | --- | --- |
| 1–2 | Concierge phase: 20 real jobs matched by hand, no app needed | 5 paid jobs closed → proceed |
| 3–4 | Brief template + escrow flow design; lawyer opinion on licensing posture (ART-041) | written counsel position |
| 5–6 | MVP build: auth, profile, brief, proposal, escrow funding, milestone release | internal demo pass |
| 7 | Verification (KYC-lite) + payouts to MoMo in sandbox then live with tiny amounts | 10 test payouts successful |
| 8 | Security review, authz matrix, threat model update; DPC registration filed | G5 pass |
| 9 | Beta with 30 talent / 10 clients on real jobs | dispute rate ≤ 10%, crash-free ≥ 99% |
| 10 | Store submissions (internal → closed testing), support playbook, runbooks | store approval |
| 11 | Canary 5% (Accra only), monitor guardrails | no S1/S2 |
| 12 | Public launch Accra; press + community; measure daily | G6 pass, launch review scheduled |

**Launch is gated, not dated.** If an artefact in G6 is missing, the date moves. This is stated now,
while nobody is under pressure, because at week 12 everyone will want to ship.

## 12.9 Go / No-Go checklist (ART-081)

| # | Item | Evidence | Owner | Status |
| ---: | --- | --- | --- | --- |
| 1 | DPC registration submitted/approved | certificate or application receipt | D054 | ☐ |
| 2 | Payment licensing position documented by counsel | legal memo | D018 | ☐ |
| 3 | Terms, privacy notice, refund policy live and versioned | URLs + version | D017 | ☐ |
| 4 | Escrow flow tested end-to-end with real small amounts | test log | D100 | ☐ |
| 5 | Ledger reconciliation clean for 7 consecutive days | dashboards | D023 | ☐ |
| 6 | Payout success ≥ 95% on both MoMo and bank | report | D193 | ☐ |
| 7 | Critical journeys E2E green | CI link | D139 | ☐ |
| 8 | Authz matrix 100% | report | D146 | ☐ |
| 9 | No open S1/S2 defects | tracker filter | D131 | ☐ |
| 10 | Pen-test criticals closed or accepted in writing | ART-069 | D187 | ☐ |
| 11 | Backups restored successfully in last 30 days | ART-074 | D227 | ☐ |
| 12 | Rollback rehearsed on production-like env | ART-082 | D218 | ☐ |
| 13 | Support macros + rota ready | ART-062 | D172 | ☐ |
| 14 | Store listings approved, data-safety forms consistent with code | store console | D059 | ☐ |
| 15 | On-call rota, escalation, kill switches tested | ART-083 | D223 | ☐ |
| 16 | Analytics events verified; NSM computable | dashboard | D040 | ☐ |
| 17 | Fraud playbook + first-line detection live | ART-072 | D179 | ☐ |
| 18 | Insurance/liability position reviewed (if applicable) | memo | D017 | ☐ |

## 12.10 Post-launch operating rhythm

| Cadence | Activity | Output |
| --- | --- | --- |
| Daily | money reconciliation, incident review, support queue health | green/red report |
| Weekly | liquidity review (fill rate by skill/city), funnel, cost per job | ART-089 update |
| Weekly | dispute sample review (5 cases) for fairness | notes + product fixes |
| Monthly | unit economics, cohort retention, AI cost | ART-086, G7 inputs |
| Monthly | access review, vulnerability SLA review | ART-075 |
| Quarterly | threat model refresh, DR drill, OKR reset | ART-048, ART-074, ART-093 |

## 12.11 What "operationally excellent" looks like here

- No one asks "is the money right?" on a call; there is a dashboard and it is green.
- A new engineer can deploy on day one by following the runbook.
- Every alert that fires has a runbook, and every runbook has been used at least once in a drill.
- The team can describe the top three risks without looking them up.
- Postmortem action items close within their due dates, or they get re-scoped in public.

If those five things are true, the process is working. If they are not, more documentation will not
help — smaller systems and fewer moving parts will.
