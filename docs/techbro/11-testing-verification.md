# 11 — Testing & Verification

> Testing exists to answer one question: **what will break in production, and would we know before a
> user tells us?** Coverage percentages are a weak proxy; *risk coverage* and *escape rate* are the
> real measures.

---

## 11.1 Principles

1. **Test the risk, not the file tree.** A 100%-covered login screen is worth less than a
   property-tested ledger.
2. **Test what you can't undo first.** Money, identity, and deletions get the most expensive testing.
3. **Fast feedback wins.** Unit < 1 min, integration < 10 min, e2e < 30 min. Beyond that, developers
   stop running tests and the suite rots.
4. **Every escaped defect produces a test.** Non-negotiable; the regression suite *is* the memory of
   past failures.
5. **Flaky tests are worse than missing tests** — they teach the team to ignore red (S44).
6. **Test data is not production data.** Synthetic only, always (ART-056).

## 11.2 Test pyramid for this product

| Layer | Share | Count target (MVP) | Runtime | Tooling |
| --- | ---: | ---: | --- | --- |
| Unit (domain rules, money math, validators) | 60% | ~800 | < 60 s | pytest, jest |
| Integration (API + DB + outbox, contracts) | 25% | ~250 | < 8 min | pytest + testcontainers, Pact-style |
| End-to-end (critical journeys only) | 10% | ~25 | < 20 min | Detox (mobile), Playwright (web/admin) |
| Exploratory / manual | 5% | per release | — | session-based charters |

**Critical journeys that must have E2E coverage** (no exceptions): signup+verification happy path;
post job → proposal → accept; fund → submit → accept → payout; dispute open → evidence → decision;
payout destination change; account deletion request.

## 11.3 Risk-based test matrix

| Risk | Likelihood | Impact | Coverage strategy | Owner |
| --- | --- | --- | --- | --- |
| Double payment / duplicate release | Low | Catastrophic | property tests on ledger; idempotency replay tests; webhook duplicate storms | D137 |
| Unauthorized data access (BOLA) | Medium | Severe | role×endpoint matrix; authz fuzzing; tenant confusion cases | D146 |
| Wrong payout destination | Low | Severe | change-with-cooling tests; last-4 confirmation; notification to prior number | D137 |
| Milestone sum mismatch | Medium | High | DB constraint + API validation + reconciliation job tests | D125 |
| Dispute decision inconsistency | Medium | High (trust) | decision scenario library; inter-rater agreement on 30 past cases | D142 |
| Offline message loss | High | Medium | network throttling suites; queue replay; ordering tests | D124 |
| OTP SMS pumping | Medium | Medium (cost) | rate-limit tests per IP/phone/device; anomaly detection | D087 |
| Search returns zero for common skills | Medium | Medium | taxonomy regression set of 200 queries | D214 |
| AI brief assistant hallucination | Medium | High | golden set + human review + schema validation | D134 |
| Accessibility break on money screens | Medium | Medium | screen-reader E2E; automated token checks | D128 |

## 11.4 Money path testing (the part most teams get wrong)

**Property-based invariants** (Hypothesis / fast-check), run against a model of the ledger:

| # | Invariant | Example failure it catches |
| ---: | --- | --- |
| P1 | Σ debits = Σ credits per transaction | a release written with only one side |
| P2 | wallet balance = Σ credits − Σ debits | cache drift |
| P3 | escrow liability = funded − released − refunded | double release after webhook retry |
| P4 | any (txn, idempotency_key) applied twice has the same effect as once | duplicate webhook |
| P5 | a milestone cannot be released twice | race between accept and auto-accept |
| P6 | refunds + releases ≤ funded amount | split dispute math error |
| P7 | no negative wallet balance except the platform's designated fee-floating account | refund after settlement |
| P8 | payout amount ≤ wallet balance at initiation | concurrent payout requests |

**Chaos drills for money** (run on staging, monthly):
1. Send the same `charge.success` webhook 5 times, out of order.
2. Kill the worker mid-payout; verify recovery produces exactly one transfer.
3. Force provider timeout on the transfer call; verify retry uses the same idempotency key.
4. Replay a refund after settlement; verify the platform absorbs and records the shortfall.

## 11.5 Security testing (see also §9)

| Type | Frequency | Scope | Output |
| --- | --- | --- | --- |
| SAST | every PR | all code | findings triaged < 24h |
| SCA / SBOM | every build | dependencies | block on critical |
| DAST | weekly | staging API | tracked findings |
| Authz matrix | every release | all endpoints × roles | zero unexplained allows |
| Secrets scan | every push | repo + images | zero |
| Mobile static/dynamic | per release candidate | MASVS L2+P | ART-068 report |
| External pen test | pre-launch + annual | app, API, admin | ART-069 |
| AI red team | per prompt/model change | LLM features | ART-145 findings |

## 11.6 Test data strategy

| Environment | Data source | Rule |
| --- | --- | --- |
| local / CI | generated fixtures (deterministic seeds) | no real data, ever |
| staging | synthetic at production shape (100k users, 1M events) | refresh weekly; PII-free verified by scan |
| production-like perf | synthetic + masked subset **only with DPO written approval** | never in a lower-trust environment |

Synthetic data must preserve *statistical shape* (skill distribution, price ranges, dispute rate) or
the tests will pass on data that looks nothing like Accra in 2026.

## 11.7 Quality gates (release criteria)

| Gate | Criterion | Blocking? |
| --- | --- | --- |
| Unit + integration green | 100% pass | yes |
| Coverage (critical modules: money, auth, disputes) | ≥90% line, ≥80% branch **plus** mutation score ≥60% | yes |
| Coverage (everything else) | ≥70% line | yes (with documented exceptions) |
| E2E critical journeys | 100% pass, zero flakes in last 5 runs | yes |
| Performance smoke | p95 within SLO on staging | yes |
| Authz matrix | 100% pass | yes |
| No critical/high security findings open | 0 | yes |
| Accessibility checks on money screens | pass | yes |
| Known defects | no S1/S2 open; S3 with workaround documented | yes |
| Rollback rehearsed | evidence linked | yes |
| Analytics events firing | verified in staging | no (warn) |

## 11.8 Defect management

| Severity | Definition | Fix SLA | Example |
| --- | --- | --- | --- |
| **S1 Blocker** | money loss/duplication, data breach, total outage, data corruption | immediate hotfix | double release |
| **S2 Critical** | core journey broken for many users, no workaround | 24–48h | cannot fund escrow on MTN |
| **S3 Major** | journey degraded, workaround exists | 7 days | chat ordering wrong after reconnect |
| **S4 Minor** | cosmetic, copy, small UX | next cycle | misaligned amount column |

Rules: severity is set by **impact**, priority by **business**; only the triage owner (D131) changes
severity; every S1/S2 gets a postmortem line even if it was caught pre-Launch. Reopened defects
count double in the quality dashboard — they are a signal about the fix, not the bug.

## 11.9 Test environment matrix

| Dimension | Values tested | Why |
| --- | --- | --- |
| Android | 2 lowest-share-but-common versions in GH + latest | fragmentation |
| iOS | latest two majors | |
| Devices | 1 low-RAM (2GB), 1 mid, 1 flagship per platform | real performance |
| Networks | Wi-Fi, 4G, throttled 3G (400 kbps, 300 ms RTT), offline transitions | the actual market |
| Locale | en-GH; long-text pseudo-locale | layout safety |
| Accessibility | TalkBack, VoiceOver, 200% text, high contrast | conformance |
| Power | app killed by OS mid-flow | resumability |

## 11.10 Verification of non-functional requirements

| NFR | How verified | Evidence artefact |
| --- | --- | --- |
| p95 API latency < 400 ms | load test at 2× forecast peak | ART-104 |
| Cold start < 3 s on 2GB device | device measurement, 20 runs | ART-105 |
| Crash-free sessions ≥ 99.5% | crash reporting over beta + production | ART-101 |
| Offline message durability | airplane-mode E2E suite | ART-055 |
| Backup restore RTO < 4h | quarterly restore drill | ART-074 |
| WCAG 2.2 AA | audit + screen-reader evidence | ART-102 |
| Accessibility of money flows | scripted assistive-tech tests | ART-102 |
| AI brief schema validity 100% | golden set regression | ART-107 |

## 11.11 The test suite as documentation

Each critical rule in `06-api-contract.md` and `07-matching-reputation.md` names the test that
proves it. That linkage is generated into ART-055 so that "we tested it" always has a click target.
A rule without a test is a hope; a test without a rule is clutter.

## 11.12 What we deliberately do not test (and why)

| Not tested | Why | Risk accepted by |
| --- | --- | --- |
| Exhaustive device matrix (300 devices) | cost >> value; use market-share top 12 | D124 |
| Third-party provider behaviour under failure beyond documented codes | not our system | D100 |
| LLM output exact wording | non-deterministic by design; test properties, not strings | D134 |
| Visual pixel diffing of every screen | flaky, low signal at MVP; use snapshot for components only | D139 |
| Load test beyond 2× forecast | premature; revisit at 10k MAU | D118 |

Each accepted risk is recorded in ART-014 with an owner and a review date — that is what makes it a
decision rather than an oversight.
