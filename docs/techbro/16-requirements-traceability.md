# 16 — Requirements Traceability

> Requirement → design → build → test → evidence. If a chain breaks anywhere, the requirement is
> either not built, not verified, or not wanted. This matrix is **generated and checked in CI**
> (ART-028); the version below is the seed that the generator fills.

---

## 16.1 Traceability model

```
Business goal (ART-017)
   └─▶ Capability (ART-019)
         └─▶ Requirement REQ-### in the SRS (ART-018)
               ├─▶ Design: ADR / OpenAPI / ERD
               ├─▶ Build: PR(s) / migration
               ├─▶ Test: TC-### (ART-055)
               └─▶ Evidence: gate artefact (ART-067/068/069/101/104)
```

**Rules:**
1. Every REQ has exactly one owner role and at least one test.
2. Every test names the REQ it verifies (tag or filename convention).
3. A REQ with no test cannot pass G4; a test with no REQ is deleted or linked.
4. Changes to a REQ create a version note; silently edited requirements are how scope creep hides.

## 16.2 Requirement conventions

| Prefix | Class | Example ID | Verified by |
| --- | --- | --- | --- |
| `REQ-F-` | functional | REQ-F-042 | unit/integration/e2e |
| `REQ-N-` | non-functional | REQ-N-007 | load test / audit / drill |
| `REQ-S-` | security | REQ-S-011 | ASVS/MASVS test, pen test |
| `REQ-P-` | privacy | REQ-P-003 | DSAR drill, data map audit |
| `REQ-C-` | compliance | REQ-C-002 | control test, legal review |

Each requirement statement follows: **"The system shall <behaviour> when <condition>, measured as
<threshold>."** If a statement cannot take a threshold, it is a goal, not a requirement.

## 16.3 Functional requirements (MVP seed)

| ID | Requirement | Owner | Design ref | Tests | Evidence |
| --- | --- | --- | --- | --- | --- |
| REQ-F-001 | A user shall register with a phone number and verify via OTP within 90 s (p95) on a 3G connection. | D098 | §6.3 Auth | TC-AUTH-001..008 | ART-101 |
| REQ-F-002 | The system shall bind each session to a device and revoke sessions on phone change. | D152 | §9.2 | TC-AUTH-020..025 | ART-067 |
| REQ-F-003 | A talent profile shall require ≥1 skill with a declared level before appearing in matching. | D099 | §5.3 | TC-PROF-001..004 | ART-055 |
| REQ-F-004 | A job post shall not publish without outcome, ≥1 deliverable with acceptance criteria, budget range, and deadline. | D031 | §3.6 M2 | TC-JOB-001..010 | ART-103 |
| REQ-F-005 | The system shall return ranked eligible candidates for a published job within 800 ms (p95). | D084 | §7.2/7.3 | TC-MATCH-001..012 | ART-104 |
| REQ-F-006 | Every match shown shall include ≥2 human-readable match reasons. | D105 | §7.3 | TC-MATCH-020 | ART-055 |
| REQ-F-007 | Accepting a proposal shall create an engagement and ≥1 milestone whose amounts sum to the engagement total. | D100 | §5.3 | TC-CON-001..009 | ART-137 |
| REQ-F-008 | A milestone shall not be released before its escrow funding is confirmed by a verified provider webhook. | D100 | §6.4.1 | TC-MONEY-001..015 | ART-137 |
| REQ-F-009 | Releasing a milestone shall write balanced double-entry ledger rows in the same transaction as the state change. | D100 | §5.4 | TC-MONEY-020..040 | ART-137 |
| REQ-F-010 | Duplicate provider webhooks shall not create duplicate financial effects (idempotency). | D100 | §6.5 | TC-MONEY-041..055 | ART-137 |
| REQ-F-011 | A payout shall not be initiated if the amount exceeds the wallet balance at that moment. | D193 | §6.4.3 | TC-PAY-001..012 | ART-137 |
| REQ-F-012 | Changing a payout destination shall require re-verification and notify the previous number. | D152 | §9.2 | TC-PAY-020..026 | ART-067 |
| REQ-F-013 | A dispute shall freeze the associated escrow until a decision or appeal window closes. | D180 | §7.6 | TC-DIS-001..014 | ART-103 |
| REQ-F-014 | Reviews shall be editable for 14 days then immutable, and only from funded engagements. | D099 | §5.5 | TC-REV-001..008 | ART-055 |
| REQ-F-015 | Chat messages shall be delivered exactly once per recipient in stable order, surviving reconnect. | D098 | §6.7 | TC-CHAT-001..020 | ART-105 |
| REQ-F-016 | Admin money adjustments shall require two distinct staff actors and write an audit entry in the same transaction. | D187 | §5.5 | TC-ADM-001..010 | ART-067 |
| REQ-F-017 | Account deletion shall remove personal data except records retained for financial compliance, and inform the user of the exception. | D054 | §9.5 | TC-PRI-001..009 | ART-110 |
| REQ-F-018 | The brief assistant shall never publish a job without explicit user confirmation. | D268 | §8.2 | TC-AI-001..015 | ART-107 |
| REQ-F-019 | Any AI-generated text shown as advice shall be labelled as such and be editable. | D268 | §8.2 | TC-AI-020..028 | ART-107 |
| REQ-F-020 | Support users shall be able to resolve a dispute end-to-end without database access. | D180 | §12.6 | TC-SUP-001..012 | ART-103 |

*(The full set — target ~120 for MVP — lives in the generated matrix; the 20 above are the load-bearing
ones that gate G4/G5.)*

## 16.4 Non-functional requirements (measurable, testable)

| ID | Requirement | Measure | Verification | Evidence |
| --- | --- | --- | --- | --- |
| REQ-N-001 | API p95 latency < 400 ms at 2× forecast peak | load test | ART-104 |
| REQ-N-002 | Mobile cold start < 3 s on a 2 GB RAM Android device | 20 runs | ART-105 |
| REQ-N-003 | Crash-free sessions ≥ 99.5% | crash reporting | ART-101 |
| REQ-N-004 | App must remain usable for read flows with no network, showing cached data ≤15 min old | offline test | ART-055 |
| REQ-N-005 | Backups restored within RTO 4 h, RPO 15 min | quarterly drill | ART-074 |
| REQ-N-006 | API availability ≥ 99.5% monthly | SLO | ART-080 |
| REQ-N-007 | Push/notification delivery ≥ 95% for money events, with SMS fallback | delivery report | ART-043 |
| REQ-N-008 | The app shall function on Android 3G with 400 kbps bandwidth for all critical flows | throttled tests | ART-105 |
| REQ-N-009 | WCAG 2.2 AA conformance on all critical journeys | audit | ART-102 |
| REQ-N-010 | Initial JS bundle ≤ 8 MB; app install ≤ 60 MB | build report | ART-104 |

## 16.5 Security requirements

| ID | Requirement | Standard | Verification |
| --- | --- | --- | --- |
| REQ-S-001 | Every API request shall be authenticated except explicitly public endpoints, and denied by default. | ASVS v5.0.0 V6/V8 (S20) | authz matrix (ART-146) |
| REQ-S-002 | Object-level authorization shall be enforced on every read/write of user-scoped resources. | API Top 10 BOLA (S34) | ART-146 |
| REQ-S-003 | Tokens shall be stored in platform secure storage, never in plain files or logs. | MASVS-STORAGE (S21) | ART-068 |
| REQ-S-004 | All traffic shall use TLS 1.2+ with certificate pinning and a documented rotation path. | MASVS-NETWORK (S21) | ART-068 |
| REQ-S-005 | Inbound webhooks shall be signature-verified and replay-protected before any state change. | ASVS V2/V4 | ART-055, pen test |
| REQ-S-006 | Privileged admin actions shall require MFA and be fully audited (hash-chained). | ASVS V8/V16 | ART-067 |
| REQ-S-007 | Secrets shall not exist in source, CI logs, or mobile bundles. | OWASP | secret scan (ART-076) |
| REQ-S-008 | Vulnerability remediation SLAs: critical 24 h, high 7 d, medium 30 d. | S24 | ART-075 |
| REQ-S-009 | Input shall be validated schema-first at the API boundary; output encoded; no dynamic SQL. | ASVS V1/V2 | SAST/DAST (ART-097) |
| REQ-S-010 | Rate limits shall protect OTP, funding, payouts and reports from automation. | OAT (S28) | ART-087 |

## 16.6 Privacy and compliance requirements

| ID | Requirement | Source | Verification |
| --- | --- | --- | --- |
| REQ-P-001 | Register as a data controller with the DPC before processing personal data. | Act 843 s.27(1) (S2) | ART-070 evidence |
| REQ-P-002 | Collect only the personal data needed for the stated purpose; each field justified in the inventory. | S2 | ART-029 review |
| REQ-P-003 | Provide an in-app path to request access, correction, and deletion, with an SLA. | S2 | DSAR drill (ART-071) |
| REQ-P-004 | Record consent with timestamp and notice version; allow withdrawal as easily as giving. | S2 | consent audit |
| REQ-P-005 | Apply the retention schedule per data class, with proof of deletion. | S2 + S27 | ART-085 |
| REQ-P-006 | Document the cross-border transfer basis for every processor's region. | S3 | ADR-006 |
| REQ-C-001 | Do not operate a payment service without a licence; use a compliant provider posture. | Act 987 (S5) | legal memo (ART-070) |
| REQ-C-002 | Use external payment (not in-app purchase) for real-world services; declare data collection accurately in stores. | S18, S19 | ART-059 |
| REQ-C-003 | Keep transaction records for at least six years. | Act 915 s.27(3) (S27) | ART-085 |
| REQ-C-004 | State fees, escrow mechanism, and refund rules in plain language before purchase. | Consumer protection (counsel) | T&Cs review |

## 16.7 Coverage status board (generated)

| Class | Requirements defined | With tests | With evidence | Gaps |
| --- | ---: | ---: | ---: | --- |
| Functional | 120 (target) | — | — | generated |
| Non-functional | 10 | — | — | generated |
| Security | 10 | — | — | generated |
| Privacy/compliance | 10 | — | — | generated |

**DoD for this artefact:** the generator reads test tags and evidence links from the repo and fails
the build if any REQ above has no test. A traceability matrix maintained by hand is a work of
fiction with good formatting.
