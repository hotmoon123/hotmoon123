# 01 — Role Catalogue: 300 SDLC Roles

> Generated from `tools/data/roles/*.yaml` by `tools/gen_blueprint.py`. Do not edit by hand:
> edit the data and regenerate, otherwise the document and the truth diverge.

**Roles:** 300 &nbsp;|&nbsp; **Families:** 19 &nbsp;|&nbsp; **Artefacts owned:** 114 &nbsp;|&nbsp; **Roles per artefact:** 2.6

Every role is a *job to be done*, not a headcount. In a 6-person startup one human holds
15–25 of these hats; the catalogue exists so that when a hat is dropped, somebody can name
the hat, the output and the artefact that went missing. Columns:

| Column | Meaning |
| --- | --- |
| **Owns** | the artefact(s) this role is accountable for (ART-###, see `artifacts/00-artifact-index.md`) |
| **Inputs → Outputs** | what must exist before the work, and what must exist after |
| **Core skill** | the specific competence, not a generic adjective |
| **Bloom** | cognitive ceiling of the role (revised Bloom, Anderson & Krathwohl 2001) |
| **AI leverage** | where a model accelerates the role, and the irreducible human judgement |
| **KPI** | how the role is measured (a role without a measure is a rumour) |

## 1.1 Family load

| # | Family | Roles | Share | Artefacts owned |
| ---: | --- | ---: | ---: | ---: |
| 1 | Security | 38 | 12.7% | 52 |
| 2 | Operations | 32 | 10.7% | 40 |
| 3 | Quality | 29 | 9.7% | 44 |
| 4 | Engineering | 27 | 9.0% | 37 |
| 5 | Business | 21 | 7.0% | 31 |
| 6 | Data | 16 | 5.3% | 23 |
| 7 | AI | 15 | 5.0% | 21 |
| 8 | Architecture | 14 | 4.7% | 23 |
| 9 | Finance | 14 | 4.7% | 17 |
| 10 | Growth | 13 | 4.3% | 14 |
| 11 | Research | 13 | 4.3% | 15 |
| 12 | People | 12 | 4.0% | 13 |
| 13 | Delivery | 11 | 3.7% | 17 |
| 14 | Content | 10 | 3.3% | 14 |
| 15 | Design | 10 | 3.3% | 15 |
| 16 | Governance | 8 | 2.7% | 10 |
| 17 | Leadership | 6 | 2.0% | 9 |
| 18 | Product | 6 | 2.0% | 12 |
| 19 | Legal | 5 | 1.7% | 5 |

## 1.2 Cognitive load (revised Bloom taxonomy)

The distribution is the design intent for an AI-augmented team: machines carry recall and
retrieval, humans are concentrated in analysis, evaluation and creation — the levels where
being wrong is expensive and accountability cannot be delegated to a model.

| Bloom level | Roles | Share | What AI changes |
| --- | ---: | ---: | --- |
| 1-Remember | 0 | 0.0% | AI retrieves and recalls; the human must move to verification |
| 2-Understand | 12 | 4.0% | AI explains and summarises; the human checks meaning against context |
| 3-Apply | 118 | 39.3% | AI drafts and executes; the human owns correctness, safety and edge cases |
| 4-Analyse | 79 | 26.3% | AI generates hypotheses and finds patterns; the human interrogates causal claims |
| 5-Evaluate | 62 | 20.7% | AI scores and compares; the human owns the judgement, the trade-off and the consequences |
| 6-Create | 29 | 9.7% | AI expands the option space; the human commits to the irreversible choice |

## 1.3 The catalogue

### Security — 38 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D054 | **Data Protection Officer** | ART-029, ART-071 | Data inventory, processing activities → PIA, privacy notice, DSAR process, DPC filings | Act 843, GDPR-equivalence, records of processing | 5-Evaluate | AI drafts PIA questionnaires and data maps; DPO makes the legal call | DSAR SLA, zero unregistered processing |
| D068 | **Security Architect** | ART-048, ART-066 | Threat landscape, data classes → Security architecture, control mapping, threat model | Defence in depth, IAM, cryptography | 6-Create | AI proposes STRIDE threats per boundary; architect validates exploitability | Control coverage, critical findings open |
| D096 | **Security Engineer** | ART-066 | Threat model, findings → Controls implemented, security tests in CI | AppSec engineering, secure defaults | 3-Apply | AI drafts secure-by-default configs; humans verify control intent | Critical findings open, controls automated |
| D097 | **Application Security Engineer** | ART-067 | Code, SAST/DAST results → Verified fixes, ASVS evidence | OWASP ASVS, code review, exploit reproduction | 4-Analyse | AI triages SAST noise and drafts exploit paths; humans reproduce | Mean time to remediate by severity |
| D145 | **AI Red Teamer (LLM)** | ART-050, ART-064 | Prompt library, model access → Jailbreak/prompt-injection findings, fixes | Adversarial prompting, tool-abuse paths | 5-Evaluate | AI generates attack corpora; humans judge real-world impact | Unsafe-output rate after fixes |
| D146 | **Access Control Tester** | ART-021, ART-067 | Permission matrix, API spec → BOLA/IDOR findings, matrix verification | Authz matrix testing, role confusion | 4-Analyse | AI enumerates role x endpoint combinations to test | Authz defects per release |
| D147 | **Pentester (Mobile)** | ART-069 | Builds, scope agreement → Mobile findings, PoC, retest evidence | MASVS/MASTG, Frida, static analysis | 5-Evaluate | AI assists with decompiled-code reading; humans exploit | Critical mobile findings open |
| D148 | **Pentester (Web/API)** | ART-069 | API spec, staging build → Web/API findings with CVSS | OWASP WSTG, API Top 10 | 5-Evaluate | AI accelerates recon and payload fuzzing in scope | Critical findings remediated |
| D149 | **Security Code Reviewer** | ART-067 | Diffs, threat model → Security review comments, blocking issues | Secure code patterns, data-flow review | 4-Analyse | AI pre-flags injection/SECRET/authz issues; humans verify | Security defects escaped |
| D150 | **CI/CD Security Engineer** | ART-053, ART-076 | Pipeline config, secrets → Hardened pipelines, OIDC auth, supply-chain gates | SLSA-style provenance, least-privilege CI | 3-Apply | AI audits workflow permissions and proposes least privilege | Pipeline privilege findings |
| D151 | **Application Security Manager** | ART-067, ART-075, ART-052 | Findings, risk appetite → AppSec roadmap, risk acceptances | Programme management, secure SDLC | 5-Evaluate | AI produces AppSec posture reports from tooling | Risk accepted with expiry |
| D152 | **Identity & Access Management Engineer** | ART-021, ART-044 | Auth design, role model → IAM implementation, token policy, MFA | OAuth2/OIDC, sessions, device binding | 3-Apply | AI reviews token lifetimes and scope creep | Account takeover incidents |
| D153 | **Fraud Analyst** | ART-072 | Transaction data, reports → Fraud rules, case decisions, loss reports | Pattern detection, investigative method | 4-Analyse | AI scores anomalies and drafts case summaries; analysts decide | Fraud loss rate, false-positive rate |
| D154 | **KYC/AML Analyst** | ART-044 | ID documents, watchlists → Verification decisions, escalation files | Identity verification, sanctions screening | 3-Apply | AI pre-screens documents; analysts handle exceptions | False-reject rate, review SLA |
| D155 | **Threat Intelligence Analyst** | ART-075 | External feeds, incident data → Threat briefings, IOC monitoring | OSINT, indicator management | 4-Analyse | AI summarises feeds and maps to our assets | Early warnings actioned |
| D156 | **Incident Responder (CSIRT)** | ART-073 | Alerts, reports → Contained incidents, forensics, postmortems | DFIR, containment, evidence handling | 5-Evaluate | AI drafts timelines from logs; humans verify chain of custody | Containment time, repeat incidents |
| D157 | **Security Operations Centre (SOC) Analyst** | ART-075 | SIEM alerts → Triage decisions, escalations | Alert triage, log analysis | 3-Apply | AI triages and enriches alerts; analysts approve closures | MTTD/MTTR, alert precision |
| D158 | **Detection Engineer** | ART-075, ART-079 | Threat model, incidents → Detection rules, test coverage | Detection-as-code, ATT&CK mapping | 3-Apply | AI proposes detections from postmortems; humans test false-positive rate | Detection coverage of modelled threats |
| D159 | **Vulnerability Manager** | ART-075 | Scanner output, asset inventory → Prioritised remediation plan | CVSS/EPSS interpretation, patch SLAs | 4-Analyse | AI deduplicates and ranks findings by exposure | Critical vulns outside SLA |
| D160 | **Supply Chain Security Analyst** | ART-076 | SBOM, dependency graph → Licence and provenance risk register | SBOM analysis, dependency policy | 4-Analyse | AI maps transitive dependencies to known CVEs | Unapproved dependencies in prod |
| D161 | **Cryptography Engineer** | ART-066 | Data classes, key lifecycle → Crypto design, key management, rotation | KMS, envelope encryption, TLS | 3-Apply | AI reviews misuse of primitives; humans own key custody | Key rotation compliance |
| D162 | **Forensics & Evidence Handler** | ART-073 | Incident artefacts → Evidence packs, chain-of-custody logs | Acquisition, hashing, legal admissibility | 3-Apply | AI indexes artefacts; humans verify integrity | Evidence accepted in proceedings |
| D163 | **Insider Risk Analyst** | ART-072 | Access logs, HR signals → Risk assessments, control changes | Behavioural baselining, least privilege | 4-Analyse | AI flags anomalous access patterns for human review | Insider incidents |
| D164 | **Physical Security & Office IT Lead** | ART-070 | Premises, device fleet → Device policy, access control, asset register | MDM, physical controls | 2-Understand | AI audits device compliance reports | Unmanaged devices |
| D165 | **Business Continuity Manager** | ART-074, ART-065 | BIA, dependency map → BCP, RTO/RPO, exercise reports | Business impact analysis, exercising | 5-Evaluate | AI drafts scenario playbooks from dependency maps | RTO met in exercises |
| D167 | **Trust & Safety Policy Manager** | ART-084 | Abuse reports, law, norms → Enforcement policy, appeal rules | Policy writing, proportionality | 5-Evaluate | AI drafts policy options and precedent comparisons | Appeal overturn rate |
| D169 | **Anti-Fraud Data Scientist** | ART-072 | Fraud cases, features → Detection models, threshold policy | Imbalanced learning, cost-sensitive evaluation | 4-Analyse | AI trains baseline detectors; humans set the cost trade-off | Loss avoided vs friction added |
| D170 | **Privacy Engineer** | ART-029, ART-085 | Data map, retention rules → De-identification, deletion pipelines, consent plumbing | PETs, k-anonymity, deletion integrity | 3-Apply | AI detects PII in logs and fixtures | PII found in logs, deletion proof coverage |
| D187 | **Security Programme Manager** | ART-048, ART-070 | Risk register, compliance needs → Security roadmap, control ownership | Programme management, ISO 27001 thinking | 5-Evaluate | AI maps controls to evidence and gaps | Control coverage, open critical risk |
| D188 | **Third-Party Risk Analyst** | ART-065, ART-076 | Vendor list, due-diligence packs → Vendor risk ratings, contract clauses | Due diligence, questionnaire design | 4-Analyse | AI summarises vendor security docs; humans verify claims | High-risk vendors without mitigation |
| D195 | **Fraud Rules Engine Owner** | ART-072 | Fraud losses, rule performance → Rule changes with expected impact | Rule design, backtesting | 4-Analyse | AI backtests rule changes against historical cases | Rule precision/recall |
| D201 | **Compliance Officer** | ART-070 | Regulations, internal policies → Compliance register, training, attestations | Regulatory mapping, evidence management | 4-Analyse | AI diffs regulator guidance against our controls | Open obligations past due |
| D202 | **Privacy Operations Analyst** | ART-071 | DSARs, consent records → DSAR responses, consent audits | Case handling, records of processing | 3-Apply | AI locates personal data across systems for DSAR scoping | DSAR SLA compliance |
| D203 | **Records & Retention Manager** | ART-085 | Data classes, legal holds → Retention schedule, deletion certificates | Records management, legal hold | 3-Apply | AI identifies over-retained data | Deletion coverage |
| D291 | **Security Awareness Trainer** | ART-070, ART-095 | Phishing results, policies → Training programme, simulation results | Security education, simulation design | 3-Apply | AI generates phishing simulations | Phishing failure rate |
| D292 | **Red Team Operator** | ART-069 | Scope, threat model → Adversary simulation findings | Offensive security | 5-Evaluate | AI assists with tooling and report drafting | Attack paths closed |
| D293 | **Bug Bounty Programme Manager** | ART-077 | Researcher reports → Triaged rewards, fixes | Programme operations, triage | 3-Apply | AI deduplicates reports | Validity rate, time to reward |
| D297 | **Privacy Champion (per team)** | ART-071 | Team changes → Privacy checklists applied | Privacy by design | 3-Apply | AI checks PRs for new PII fields | PII changes with PIA |

### Operations — 32 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D028 | **Procurement & Vendor Manager** | ART-065 | Vendor catalogue, SLAs → Vendor scorecards, contracts, cost review | Negotiation, vendor risk, SLA design | 4-Analyse | AI compares vendor terms and incident history | Cost savings, vendor incident rate |
| D168 | **Content Moderation Lead** | ART-084 | Reported content → Decisions, queue SLAs | Moderation standards, wellbeing practices | 3-Apply | AI pre-classifies reports; humans decide edge cases | Harmful content time-to-removal |
| D171 | **Operations Manager** | ART-084 | Service demand, SLAs → Ops plan, staffing, vendor coordination | Operations design, capacity planning | 3-Apply | AI forecasts ticket volume from seasonality | SLA attainment, cost per ticket |
| D172 | **Customer Support Lead** | ART-062 | Ticket themes, product changes → Playbooks, macros, escalation policy | Support operations, QA of replies | 4-Analyse | AI drafts macros from resolved tickets; lead approves tone | First-response time, CSAT |
| D173 | **Support Agent (Tier 1)** | ART-062, ART-054 | Tickets, help centre → Resolved tickets, article suggestions | Empathy, product knowledge | 2-Understand | AI suggests replies and links; agent verifies facts before sending | Resolution rate, reopen rate |
| D174 | **Support Agent (Tier 2 / Technical)** | ART-062 | Escalations, logs → Root-cause notes, bug tickets | Debugging with users, log reading | 4-Analyse | AI summarises logs and correlates incidents | Escalation resolution time |
| D175 | **Community Manager** | ART-090 | Community channels → Engagement calendar, moderation, feedback themes | Community building, moderation, facilitation | 3-Apply | AI drafts posts and clusters sentiment; humans host the room | Weekly active members, sentiment |
| D176 | **Events Coordinator** | ART-090 | Community calendar, budget → Event plans, host kits, attendance data | Logistics, budgeting, partnerships | 3-Apply | AI drafts run-of-show and checklists | Attendance, cost per attendee |
| D177 | **Marketplace Operations Analyst** | ART-089, ART-067 | Match data, fill rates → Liquidity interventions, supply campaigns | Marketplace metrics, cohort analysis | 4-Analyse | AI detects supply-demand imbalance per skill and city | Match-fill rate, time to fill |
| D178 | **Trust & Safety Analyst** | ART-084 | Reports, risk signals → Case decisions, pattern reports | Investigation, judgement under policy | 4-Analyse | AI clusters reports and drafts case files | Case SLA, repeat offenders |
| D179 | **Fraud Operations Specialist** | ART-072, ART-068 | Flagged transactions/accounts → Freezes, refunds, evidence files | Investigation, evidence discipline | 3-Apply | AI enriches cases with linked-account graphs | Loss prevented, wrongful freezes |
| D180 | **Dispute Resolution Officer** | ART-042, ART-087 | Disputes, evidence → Binding decisions, rationale, appeals handling | Evidence weighing, neutrality, writing | 5-Evaluate | AI summarises both sides and flags missing evidence; officer decides | Overturn rate on appeal, decision time |
| D181 | **Escrow & Payout Officer** | ART-041 | Milestones, approvals → Releases, holds, exception reports | Control discipline, reconciliation | 3-Apply | AI reconciles provider reports; humans approve exceptions | Payout accuracy, hold leakage |
| D182 | **Onboarding Specialist (Freelancer)** | ART-060, ART-069 | New signups → Verified, profile-complete workers | Guided setup, verification support | 3-Apply | AI personalises onboarding nudges by missing step | Activation rate, time to first proposal |
| D183 | **Onboarding Specialist (Client)** | ART-060 | New employer accounts → First job posted, first hire made | Consultative onboarding | 3-Apply | AI drafts the first job post from a short prompt | Time to first job post |
| D184 | **Workforce / Staffing Manager** | ART-089 | Forecast demand, skill gaps → Rota, capacity plan | Workforce planning | 3-Apply | AI forecasts demand by hour/day | Coverage vs demand |
| D185 | **Quality Assurance (Support) Analyst** | ART-062 | Ticket samples → QA scores, coaching notes | Rubric design, calibration | 4-Analyse | AI pre-scores a sample; humans calibrate | QA score trend |
| D196 | **Incident Communications Lead** | ART-073 | Incident status → Status page updates, user comms | Crisis comms, plain writing | 3-Apply | AI drafts updates from incident timeline; humans approve claims | Time to first external update |
| D199 | **Service Level Manager** | ART-062, ART-080 | SLAs, performance → SLA reports, credits, improvement plans | Contract SLAs, measurement | 4-Analyse | AI computes SLA attainment from tickets | SLA breaches |
| D200 | **Field Operations Coordinator** | ART-084 | On-site jobs, schedules → Scheduling, verification visits, incident logs | Logistics, field verification | 3-Apply | AI optimises route and schedule proposals | On-time completion |
| D204 | **Procurement Officer** | ART-065 | Purchase requests → POs, vendor onboarding | Procurement process, negotiation support | 2-Understand | AI compares quotes and flags anomalies | Procurement cycle time |
| D205 | **Business Continuity Tester** | ART-074 | BCP, scenarios → Exercise reports, corrective actions | Exercise design, after-action review | 4-Analyse | AI drafts scenario injects | Actions closed from exercises |
| D206 | **Facilities & Workplace Coordinator** | ART-070 | Team needs, budget → Workplace plan, asset register | Facilities management | 2-Understand | AI maintains asset inventory | Workplace cost per head |
| D209 | **Escalation Manager (Customer)** | ART-062 | Escalated cases → Resolution plans, root-cause feedback | De-escalation, cross-team mobilisation | 4-Analyse | AI compiles the full case history in one view | Escalation resolution time |
| D220 | **Technical Community Lead** | ART-090 | Developer/tech-bro community → Programmes, mentorship matching, meetups | Community programme design | 3-Apply | AI matches mentors to mentees by skill graph | Mentorship matches retained |
| D226 | **Green / Sustainability Analyst** | ART-049 | Energy, hardware lifecycle → Carbon estimates, reduction plan | Carbon accounting, efficiency | 4-Analyse | AI estimates emissions from cloud billing data | Carbon per active user |
| D239 | **Community Moderator** | ART-084 | Channel activity → Moderation actions, escalation | Community norms, de-escalation | 2-Understand | AI flags toxic content for human review | Response time to reports |
| D240 | **Marketplace Supply Manager** | ART-089 | Supply forecasts by skill → Supply campaigns, verification pipeline | Supply-side growth, verification ops | 4-Analyse | AI identifies supply gaps by skill x city | Verified supply per demand unit |
| D274 | **Developer Support Engineer** | ART-062, ART-065 | Integration tickets → Resolved integration issues | API debugging, empathy | 3-Apply | AI reproduces issues from logs; humans fix | Integration ticket resolution |
| D276 | **Skills Assessor (Practical Reviewer)** | ART-098 | Assessment submissions → Scored rubric, feedback | Domain expertise, rubric calibration | 5-Evaluate | AI pre-scores against rubric; humans adjudicate | Calibration agreement |
| D286 | **Marketplace Integrity Analyst** | ART-072, ART-084 | Fake profiles, review manipulation → Integrity rules, takedowns | Pattern detection, investigation | 4-Analyse | AI detects review rings and duplicate identities | Fake accounts removed pre-transaction |
| D289 | **Executive Assistant** | ART-093 | Executive calendar → Scheduling, minutes, follow-ups | Organisation, discretion | 2-Understand | AI drafts agendas and minutes | Follow-up completion |

### Quality — 29 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D107 | **QA Automation Engineer** | ART-055 | Test plan, API contracts → Automated suites, flake control | Playwright/Detox, contract tests, fixtures | 3-Apply | AI generates test cases from specs and screenshots; humans verify oracles | Automation coverage, flake rate |
| D117 | **Integration Test Engineer** | ART-055, ART-065 | Contracts, sandboxes → End-to-end integration suites | Contract testing, test doubles | 3-Apply | AI generates contract tests from OpenAPI | Integration escapes |
| D118 | **Performance Engineer** | ART-049, ART-104 | Traffic model, SLOs → Load test results, bottlenecks, tuning | Load modelling, profiling, capacity math | 4-Analyse | AI drafts load scripts and analyses bottlenecks; humans verify on prod-like data | p95 latency, cost per request |
| D121 | **QA Lead / Test Manager** | ART-054, ART-101 | Risk register, release scope → Test strategy, exit criteria, quality report | Risk-based testing, planning | 5-Evaluate | AI proposes risk-ranked test scope from change history | Escaped defects per release |
| D122 | **Manual Test Engineer** | ART-055 | Stories, builds → Exploratory session notes, bug reports | Exploratory testing, bug isolation | 3-Apply | AI drafts charters and clusters duplicate bugs | Bugs found per session |
| D123 | **Exploratory & Session-Based Tester** | ART-055 | Charters, heuristics → Risk-focused findings, coverage notes | Heuristic test strategy model | 4-Analyse | AI generates attack lists from past incidents | High-severity finds per hour |
| D124 | **Mobile Test Engineer** | ART-055, ART-059, ART-105 | Device matrix, OS versions → Device-lab results, store review notes | Device fragmentation, permission flows | 3-Apply | AI prioritises device matrix by market share data | Device-specific defects escaped |
| D125 | **API Test Engineer** | ART-055 | OpenAPI, auth model → Contract and negative tests | Schema validation, authz testing | 3-Apply | AI generates negative and boundary cases | API defect escapes |
| D126 | **Test Data Engineer** | ART-056 | Schema, privacy rules → Synthetic datasets, masks, refresh jobs | Data generation, masking, referential integrity | 3-Apply | AI generates realistic synthetic profiles (no real PII) | PII incidents in non-prod |
| D127 | **Test Environment Manager** | ART-057, ART-109 | Env demand, cost → Provisioned environments, booking policy | Infra-as-code for test, isolation | 2-Understand | AI reports env drift and idle cost | Env availability, cost |
| D128 | **Accessibility Tester** | ART-055, ART-102 | WCAG AA target, builds → A11y test report, assistive-tech evidence | Screen readers, keyboard-only testing | 4-Analyse | AI runs automated scans; humans do assistive-tech passes | AA conformance |
| D129 | **Usability Test Moderator** | ART-047 | Prototype, tasks → Session recordings, findings, severity | Moderation without leading | 3-Apply | AI transcribes and tags the recordings | Findings adopted per round |
| D130 | **Localisation QA Tester** | ART-061 | Localised builds, glossary → Linguistic and layout defect list | Native fluency, cultural checks | 3-Apply | AI flags length overflow and terminology drift; native speaker judges meaning | Localisation defects escaped |
| D131 | **Defect Manager / Triage Owner** | ART-054 | Bug reports, severity policy → Triaged backlog, release risk view | Severity vs priority, root-cause clustering | 4-Analyse | AI clusters duplicates and drafts severity suggestions | Triage turnaround, reopen rate |
| D132 | **Regression & Release Tester** | ART-054, ART-058 | Change set, risk areas → Regression results, sign-off | Impact analysis, smoke design | 3-Apply | AI selects the minimal regression set from change impact | Regression escapes |
| D133 | **ML / Model Test Engineer** | ART-063 | Model cards, eval sets → Behavioural test suites, slice analysis | Metamorphic testing, slice metrics | 4-Analyse | AI generates adversarial and metamorphic cases | Slice regressions caught pre-release |
| D134 | **Prompt & LLM Evaluator** | ART-064, ART-107 | Golden sets, prompt versions → Eval scores, regressions, cost deltas | Rubric design, LLM-as-judge calibration | 4-Analyse | AI scores outputs; humans calibrate the judge on a sample | Eval coverage, judge agreement |
| D135 | **Beta / Field Test Coordinator** | ART-059, ART-106 | Beta cohort, feedback → Crash triage, beta findings, release verdict | Cohort management, feedback synthesis | 3-Apply | AI groups beta feedback into themes and severity | Beta-blocking issues resolved |
| D136 | **Compliance Test Analyst** | ART-070, ART-110 | Regulatory requirements → Control test evidence | Control testing, evidence capture | 3-Apply | AI samples control evidence and drafts exception reports | Controls tested on schedule |
| D137 | **Payment & Reconciliation Tester** | ART-041 | Ledger design, provider sandbox → Money-path tests, reconciliation proofs | Double-entry verification, webhook replay | 4-Analyse | AI generates webhook edge cases (duplicate, out-of-order, partial) | Money defects escaped |
| D138 | **Chaos & Resilience Tester** | ART-074 | Dependency map, SLOs → Failure injection results, blast-radius map | Chaos experiments, game days | 5-Evaluate | AI proposes experiments ranked by blast radius | Recovery time under injected failure |
| D139 | **Test Automation Architect** | ART-055, ART-108 | Tech stack, flake history → Automation framework, CI integration policy | Framework design, determinism | 6-Create | AI refactors brittle selectors and proposes waits | Flake rate, suite runtime |
| D140 | **Property-Based & Fuzz Testing Engineer** | ART-055 | Invariants, parsers → Property suites, crash corpus | Hypothesis/Schemathesis style testing | 4-Analyse | AI derives invariants from the domain model | Crashes found pre-production |
| D141 | **SDET (Software Development Engineer in Test)** | ART-055 | Product code, test gaps → Testability improvements, harnesses | Production-quality test code | 3-Apply | AI pair-writes harness code; SDET owns determinism | Critical-path coverage |
| D142 | **UAT Coordinator** | ART-047, ART-103 | Business scenarios, real users → UAT sign-off, accepted defects | Scenario design, stakeholder handling | 3-Apply | AI drafts UAT scripts from process maps | UAT first-pass acceptance |
| D143 | **Contract Test Engineer** | ART-037, ART-038 | OpenAPI, event schemas → Consumer-driven contract tests | Pact-style contracts | 3-Apply | AI generates consumer expectations from mobile usage | Breaking-change incidents |
| D144 | **Observability Test Engineer** | ART-079 | Telemetry spec → Telemetry correctness tests | Trace assertions, metric validation | 3-Apply | AI checks dashboards for missing dimensions | Blind spots found |
| D198 | **Quality Management System (QMS) Owner** | ART-026, ART-094 | Process definitions, audits → Documented QMS, audit results | ISO 9001-style process control | 4-Analyse | AI audits documents for consistency | Non-conformities closed |
| D294 | **Localisation QA Lead (Native)** | ART-061 | Translations → Linguistic sign-off | Native fluency, cultural nuance | 4-Analyse | AI flags terminology inconsistency; human judges meaning | Native-speaker review pass |

### Engineering — 27 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D091 | **DevOps Engineer** | ART-057, ART-078 | Pipeline needs, environments → Automated build/deploy, environment parity | CI/CD, containers, IaC, secrets | 3-Apply | AI drafts pipeline YAML and IaC modules; humans review blast radius | Deploy lead time, failed deploy rate |
| D092 | **Site Reliability Engineer** | ART-080 | SLOs, incidents, capacity → Reliability improvements, error budget policy | SRE practice, load patterns, chaos testing | 5-Evaluate | AI correlates incidents and proposes guardrails; SRE approves | Availability vs SLO, MTTR |
| D093 | **Platform Engineer** | ART-078 | Team needs, golden paths → Internal platforms, self-service tooling | Developer experience, abstractions, autoscaling | 3-Apply | AI generates service scaffolds from templates | Time from repo to production |
| D094 | **Observability Engineer** | ART-079, ART-080 | Telemetry needs, incidents → Dashboards, alerts, trace propagation, log schema | OpenTelemetry, metrics design, alert tuning | 3-Apply | AI drafts dashboards and alert rules from SLOs; humans tune noise | Alert precision, MTTD |
| D095 | **Release Manager** | ART-058, ART-082, ART-114 | Change queue, readiness evidence → Release calendar, rollout plan, go/no-go | Change management, risk assessment | 3-Apply | AI assembles change logs and risk summaries | Change failure rate |
| D098 | **Mobile App Developer (React Native)** | ART-046 | Designs, API contracts → App screens, offline behaviour, tests | React Native, Expo, native bridges | 3-Apply | AI scaffolds components and tests; devs verify on real low-end devices | Crash-free sessions, frame drops |
| D099 | **Backend Developer (Python/Django/DRF)** | ART-037, ART-054, ART-044 | Specs, domain model → APIs, services, migrations, tests | Django, DRF, async tasks, SQL | 3-Apply | AI pair-programs and writes tests first; humans own data safety and design | Defect escape rate, test coverage of critical paths |
| D100 | **Payments Engineer** | ART-041 | Payment design, provider APIs → Ledger implementation, payouts, reconciliation jobs | Double-entry ledgers, idempotency, PSP webhooks | 3-Apply | AI drafts idempotency and reconciliation tests; humans run money-path chaos drills | Reconciliation breaks, failed payouts |
| D101 | **Full-Stack Developer** | ART-037, ART-046 | Stories, designs → End-to-end features | Front-end and back-end breadth | 3-Apply | AI scaffolds vertical slices; humans enforce boundary rules | Story throughput, rework |
| D102 | **Frontend Web Developer** | ART-046 | Designs, API contract → Admin console, marketing site | React/TypeScript, accessibility | 3-Apply | AI generates components from the design system | Lighthouse scores, a11y violations |
| D103 | **API Integration Engineer** | ART-065 | Partner docs, sandboxes → Adapters, webhook handlers, retries | Third-party APIs, resilience patterns | 3-Apply | AI writes adapter code and contract tests against sandbox | Integration success rate |
| D104 | **Database Administrator (Production)** | ART-035, ART-074 | Growth, query load → Backups, tuning, restore drills | PostgreSQL operations, PITR, migration safety | 3-Apply | AI reviews migration risk and drafts rollback steps | Restore success, migration incidents |
| D108 | **Build & Tooling Engineer** | ART-053 | Monorepo, dependency graph → Fast correct builds, caching, artifact policy | Build systems, caching, reproducibility | 3-Apply | AI identifies slow steps and proposes caching | CI duration, cache hit rate |
| D109 | **Embedded / Hardware Integrator** | ART-065 | Biometric devices, POS terminals → Device integration notes, field test results | Serial/USB, firmware versions, driver quirks | 2-Understand | AI summarises vendor SDK docs; humans test on hardware | Device failure rate in the field |
| D110 | **Networking & Connectivity Engineer** | ART-033 | Traffic, ISPs, mobile networks → Latency budget, offline sync design | DNS, TLS, CDN, retries under poor networks | 3-Apply | AI analyses latency distributions by network type | p95 latency on 3G, timeout rate |
| D111 | **Accessibility Engineer** | ART-045 | Design system, audit findings → Accessible components, screen-reader fixes | Semantics, focus management, RN a11y APIs | 3-Apply | AI scans for missing labels and contrast issues | Screen-reader task success |
| D113 | **Developer Experience (DevEx) Lead** | ART-052, ART-051 | Developer friction surveys → Golden paths, tooling roadmap | DX measurement, platform strategy | 5-Evaluate | AI clusters developer complaints into themes | Time to first deploy for a new dev |
| D114 | **Configuration & Environment Manager** | ART-057 | Env matrix, secrets policy → Config standards, drift reports | 12-factor config, secret rotation | 2-Understand | AI diffs config across environments | Config drift incidents |
| D115 | **Localisation Engineer** | ART-061 | String catalogues, layouts → i18n plumbing, RTL and plural handling | i18n frameworks, pseudo-localisation | 3-Apply | AI detects hardcoded strings and truncation risks | Untranslated strings in release |
| D116 | **Prototyping Engineer** | ART-047 | Concepts, feasibility questions → Throwaway prototypes, spike reports | Rapid prototyping, timeboxing | 6-Create | AI builds prototypes at speed; humans decide what to keep | Validated concepts per month |
| D120 | **Code Review / Standards Owner** | ART-051 | PRs, incidents → Review standards, lint rules, escape analysis | Review discipline, static analysis | 5-Evaluate | AI pre-reviews for style and known bug classes; humans judge design | Review turnaround, defect escapes |
| D166 | **Notification & Messaging Platform Engineer** | ART-043 | Channel requirements, cost limits → Delivery service, templates, quiet hours | Push/SMS/WhatsApp gateways, deliverability | 3-Apply | AI drafts templates and predicts cost per channel | Delivery rate, cost per notification |
| D218 | **Rollout / Canary Manager** | ART-082 | Release plan, SLOs → Rollout increments, halt decisions | Progressive delivery, guardrail metrics | 4-Analyse | AI watches guardrail metrics and recommends halt | Blast radius per bad release |
| D223 | **On-call & Incident Manager** | ART-083, ART-113 | Alerts, rota → Incident command, escalation, postmortem scheduling | Incident command, calm decision-making | 4-Analyse | AI captures timeline and drafts postmortem; humans correct | MTTA/MTTR, repeat incidents |
| D224 | **Capacity & Performance Planner** | ART-049 | Growth forecasts, benchmarks → Capacity plan, scale-out triggers | Queueing theory, load modelling | 4-Analyse | AI simulates growth scenarios against current topology | Headroom maintained, cost per request |
| D227 | **Disaster Recovery Engineer** | ART-074 | RTO/RPO, backups → Restore automation, drill evidence | Backup/restore, failover automation | 3-Apply | AI drafts restore scripts and verifies checksums | Last successful restore age |
| D228 | **Data Centre / Hosting Coordinator** | ART-078 | Provider options, compliance → Hosting decision, region rationale | Provider comparison, data residency | 4-Analyse | AI compares provider compliance docs | Residency compliance |

### Business — 21 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D004 | **Business Architect** | ART-002, ART-003, ART-112 | Strategy, market data, cost structure → Lean canvas, business model canvas, operating model | Business modelling, value chains, process design | 4-Analyse | AI runs scenario grids across price/take-rate assumptions | Model consistency, decision turnaround |
| D019 | **Government & Public Sector Liaison** | ART-013 | Policy direction, agency programmes → Partnership pipeline, advocacy positions | Stakeholder management, public affairs | 3-Apply | AI drafts briefing packs from public policy documents | Partnerships signed, policy alignment |
| D020 | **Fundraising & Grants Manager** | ART-012 | Milestones, cash need → Grant applications, investor pipeline, data room | Narrative, grant writing, diligence management | 5-Evaluate | AI assembles data-room answers from approved facts only | Capital raised, cost of capital, diligence pass rate |
| D029 | **Strategy Consultant (External Advisor)** | ART-009 | Board questions, market data → Options papers with trade-offs | Structured problem solving, synthesis | 5-Evaluate | AI produces hypothesis trees; advisor stress-tests them | Decisions unblocked |
| D033 | **Business Analyst** | ART-017, ART-028 | Stakeholder needs, processes → BRD, process models, traceability matrix | Elicitation, modelling (BPMN), gap analysis | 4-Analyse | AI extracts requirements from workshops; BA confirms intent with the source | Requirement defect rate found after build |
| D034 | **Systems Analyst** | ART-019, ART-021, ART-023 | Business requirements, current systems → Capability map, use cases, permission matrix | System decomposition, use-case modelling | 4-Analyse | AI cross-checks capability map against workflows for orphans | Coverage completeness |
| D035 | **Requirements Engineer** | ART-018 | Stakeholder input, constraints → SRS with verifiable requirements | Requirements quality (ISO 29148), ambiguity hunting | 4-Analyse | AI runs a requirement-quality lint (singular, verifiable, unambiguous); human adjudicates | Requirements passing quality lint first time |
| D036 | **Non-Functional Requirements Analyst** | ART-025 | Product scope, risk register → Quality attribute scenarios | ATAM-style scenarios, measurement design | 4-Analyse | AI proposes measurable thresholds from benchmarks; humans approve targets | NFRs with automated checks vs total |
| D048 | **Domain Expert (Labour Market & Skills)** | ART-020, ART-097 | Industry practice, employer expectations → Skill taxonomy, level descriptors, domain glossary | Trade knowledge, taxonomy design | 5-Evaluate | AI expands synonyms and maps to ESCO/O*NET-like structures; expert ratifies | Taxonomy coverage, employer agreement |
| D049 | **Business Rules Analyst** | ART-024 | Policies, edge cases → Decision tables, rule catalogue | Decision modelling (DMN), edge-case analysis | 4-Analyse | AI enumerates rule combinations and finds contradictions | Rule defects found in QA |
| D050 | **Process Analyst (BPMN)** | ART-007, ART-084 | Current workflows, exception logs → As-is/to-be process models, automation candidates | BPMN, process mining | 4-Analyse | AI mines event logs to reconstruct real process paths | Cycle-time reduction |
| D058 | **Partnerships Manager** | ART-065 | Institutional needs, API partners → MOUs, integration agreements, pilot plans | BD, negotiation, partner ops | 5-Evaluate | AI drafts partner briefs from public data | Partner-sourced jobs |
| D059 | **Customer Success Manager (B2B)** | ART-089 | Employer accounts, usage data → Account plans, QBRs, churn prevention | Account management, consultative selling | 5-Evaluate | AI flags at-risk accounts from usage deltas | Net revenue retention |
| D060 | **Business Development Representative** | ART-088 | Target segments, lead lists → Qualified meetings, pipeline | Outbound, qualification | 3-Apply | AI drafts personalised outreach; humans approve every send | Qualified meetings per month |
| D192 | **Revenue Operations Analyst** | ART-088, ART-073 | Pipeline data, pricing → Funnel analysis, comp plans | RevOps tools, forecasting | 4-Analyse | AI forecasts pipeline from historical conversion | Forecast accuracy |
| D221 | **Partnerships & Integrations PM** | ART-065 | Partner roadmap → Integration scope, launch dates | Partner project management | 3-Apply | AI tracks partner requirement deltas | Integrations shipped on date |
| D222 | **Account Manager (Employer)** | ART-089 | Account health, hiring needs → Renewals, upsell, hiring plans | Relationship management | 3-Apply | AI drafts account reviews from usage data | Renewal rate, hires per account |
| D235 | **Sales Operations Manager** | ART-088, ART-062 | Pipeline, quotas → Territory plan, quota model, CRM hygiene | Sales process design | 3-Apply | AI forecasts attainment and flags stalled deals | Quota attainment |
| D244 | **Partnerships (University/Bootcamp)** | ART-090 | Talent pipeline → MOU, cohorts, placement data | Academic partnerships | 3-Apply | AI maps curricula to in-demand skills | Placements per cohort |
| D248 | **Pricing & Monetisation Manager** | ART-011 | Willingness-to-pay, margins → Fee structure, packaging | Monetisation design, price testing | 5-Evaluate | AI models take-rate elasticities | Revenue per match |
| D264 | **Marketplace Economist** | ART-039, ART-089 | Match data, pricing → Market design changes, incentive analysis | Market design, two-sided theory | 5-Evaluate | AI simulates liquidity interventions | Match efficiency |

### Data — 16 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D040 | **Product Analytics Lead** | ART-030, ART-060 | Events, funnels, cohorts → Measurement plan, funnel analysis, insight memos | Product analytics, SQL, experiment analysis | 4-Analyse | AI writes exploratory queries; analyst validates definitions against the plan | Decisions informed, metric trust |
| D076 | **Data Architect** | ART-036 | Data requirements, retention rules → Data dictionary, lineage, ownership map | Modelling, lineage, data contracts | 6-Create | AI generates dictionaries from schema and flags PII columns | Data quality incidents |
| D077 | **Database Designer / DBA** | ART-035 | Query patterns, growth forecast → ERD, indexes, partitioning, backup policy | Normalisation, indexing, query plans | 6-Create | AI reviews slow-query plans and proposes indexes; DBA validates on staging | Query p95, backup restore success |
| D078 | **Data Engineer** | ART-063 | Source systems, analytics needs → Pipelines, warehouse models, event ingestion | ELT, orchestration, schema evolution | 3-Apply | AI writes transformation code; engineers add data-quality tests | Pipeline freshness, failed runs |
| D079 | **Analytics Engineer** | ART-030 | Warehouse tables, metric definitions → Dimensional models, tested metrics layer | SQL modelling, dbt patterns, metric governance | 3-Apply | AI drafts models and tests; humans lock metric semantics | Metric disputes per quarter |
| D080 | **Data Scientist** | ART-039 | Behaviour data, matching outcomes → Ranking features, experiments, model evaluation | Statistics, ML, causal analysis | 5-Evaluate | AI runs baseline models; scientist guards leakage and validity | Match-fill lift, model calibration |
| D189 | **Data Steward** | ART-036 | Data dictionary, quality issues → Ownership assignments, quality rules | Metadata management, quality dimensions | 3-Apply | AI profiles data and flags anomalies | Data quality score |
| D190 | **Data Quality Engineer** | ART-036, ART-079, ART-075 | Pipelines, contracts → Quality tests, freshness monitors | Great Expectations-style testing | 3-Apply | AI generates expectation suites from profiles | Bad data reaching users |
| D191 | **BI / Reporting Developer** | ART-086, ART-096, ART-077 | Metrics layer, stakeholder questions → Dashboards, scheduled reports | Semantic layers, visual design | 3-Apply | AI drafts dashboard layouts and queries | Report adoption, stale dashboards |
| D211 | **Data Governance Lead** | ART-036, ART-070 | Data map, policies → Governance charter, stewardship model | Policy design, metadata standards | 5-Evaluate | AI inventories data domains and owners | Data domains with named owners |
| D212 | **Master Data Manager** | ART-036 | Duplicate records, canonical lists → Golden records, dedupe rules | Entity resolution, match rules | 3-Apply | AI proposes merge candidates and confidence scores | Duplicate rate, merge errors |
| D213 | **Database Reliability Engineer** | ART-074, ART-077 | Growth, failure modes → Failover design, upgrade plans | PostgreSQL HA, PITR, capacity | 3-Apply | AI reviews failover runbooks for gaps | Database availability |
| D215 | **Recommendation Quality Analyst** | ART-039 | Match outcomes, feedback → Quality reviews, bias slices, tuning proposals | Evaluation design, slice analysis | 4-Analyse | AI produces slice-level quality reports | Fairness within tolerance |
| D216 | **Synthetic Data & Fixtures Engineer** | ART-056 | Schema, privacy policy → Generated datasets, masks | Data synthesis, referential integrity | 3-Apply | AI generates realistic but non-real profiles at scale | PII-free non-prod verified |
| D262 | **Statistician** | ART-088 | Experiment data, sampling problems → Valid inference, power calculations | Statistical inference, sampling | 5-Evaluate | AI runs analyses; statistician validates assumptions | False discovery rate |
| D266 | **Behavioural Data Analyst** | ART-060 | Event streams → Funnel and cohort insight | Behavioural analytics, SQL | 4-Analyse | AI segments users by behaviour patterns | Activation lift |

### AI — 15 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D081 | **ML Engineer** | ART-050, ART-063 | Model designs, serving constraints → Training pipelines, serving API, monitoring hooks | MLOps, feature stores, model serving | 3-Apply | AI writes training scaffolding; engineers own reproducibility | Model deploy frequency, drift detection latency |
| D082 | **MLOps Engineer** | ART-063, ART-079 | Model registry, traffic → CI/CD for models, drift alerts, rollback | Experiment tracking, model registry, monitoring | 3-Apply | AI generates pipeline configs; humans test rollback | Deployment lead time, rollback time |
| D083 | **Feature Store Engineer** | ART-063 | Feature requests, event data → Feature definitions, online/offline parity | Streaming/batch parity, point-in-time correctness | 3-Apply | AI detects train/serve skew in definitions | Feature parity failures |
| D084 | **Recommendation & Ranking Engineer** | ART-039 | Job/skill embeddings, feedback → Ranking service, evaluation harness | IR metrics (nDCG, MRR), hybrid retrieval | 5-Evaluate | AI proposes retrieval strategies and evaluates offline; humans check bias slices | nDCG, application rate per ranked job |
| D085 | **NLP / LLM Engineer** | ART-050, ART-064 | Job posts, CVs, chat transcripts → Extraction models, embeddings, prompt library | Transformers, embeddings, prompt engineering | 3-Apply | AI accelerates prompt iteration; engineer owns eval discipline | Extraction F1, hallucination rate on golden set |
| D086 | **Computer Vision Engineer (CV/KYC)** | ART-044 | ID document images, liveness video → OCR pipeline, document-tamper checks | OCR, document forensics, liveness | 3-Apply | AI augments synthetic tamper datasets for test coverage | KYC false-accept/false-reject rate |
| D087 | **Vector Search & Retrieval Engineer** | ART-039 | Document corpus, embeddings → Index design, hybrid search, freshness policy | ANN indexes, chunking, recall tuning | 3-Apply | AI tunes chunking and evaluates recall@k | Retrieval recall, index cost |
| D088 | **Conversational AI Designer** | ART-064 | User intents, policy constraints → Dialogue flows, guardrails, escalation rules | Intent design, safety policy, fallback UX | 6-Create | AI simulates adversarial users to test guardrails | Escalation accuracy, unsafe-response rate |
| D089 | **Prompt Engineer** | ART-064 | Task definitions, eval sets → Versioned prompts with scores and cost | Prompt patterns, evaluation, token budgeting | 3-Apply | AI drafts and A/B tests prompt variants against the golden set | Eval score, cost per task |
| D090 | **AI Ethics & Responsible AI Reviewer** | ART-050, ART-070 | Model cards, impact assessments → Bias review, fairness constraints, sign-off | Fairness metrics, harm analysis, governance | 5-Evaluate | AI measures outcome disparities across slices; reviewer interprets and decides | Disparity within tolerance, harms open |
| D214 | **Search Relevance Engineer** | ART-039 | Queries, click data → Search ranking, synonyms, typo tolerance | IR, query understanding | 4-Analyse | AI mines failed queries and proposes synonyms | Zero-result rate, click-through |
| D265 | **Algorithmic Pricing Engineer** | ART-039 | Market outcomes, cost data → Price recommendation engine | Contextual bandits, guardrails | 4-Analyse | AI tunes policies offline against logged data | Take rate vs. churn guardrail |
| D269 | **AI Governance Lead** | ART-050, ART-070 | AI inventory, risk appetite → AI register, policy, review gates | NIST AI RMF, model inventory | 5-Evaluate | AI drafts model cards and risk classifications for review | AI systems with review evidence |
| D270 | **Data Annotation & Labeling Manager** | ART-063 | Label specs, annotator pool → Labeled data, inter-annotator agreement | Label taxonomy, QA sampling | 3-Apply | AI pre-labels; humans verify and audit agreement | Label agreement, cost per label |
| D271 | **Vector/Embedding Ops Specialist** | ART-039, ART-063 | Corpus changes → Re-index plans, drift reports | Embedding lifecycle | 3-Apply | AI detects semantic drift in retrieval | Retrieval quality over time |

### Architecture — 14 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D061 | **Solution Architect** | ART-032, ART-033, ART-111 | Requirements, NFRs, constraints → Solution design, integration plan, ADRs | Design patterns, integration, trade-off analysis | 6-Create | AI generates candidate designs and failure-mode lists; architect decides | Design rework after build start |
| D062 | **Trust & Reputation Architect** | ART-040, ART-042 | Marketplace abuse data, dispute outcomes → Reputation model, dispute workflow design | Incentive design, game theory, fairness | 6-Create | AI simulates gaming strategies against the scoring model | Dispute rate, repeat-offender containment |
| D063 | **Enterprise Architect** | ART-019, ART-031 | Business capability map, portfolio → Target architecture, standards, roadmap alignment | Portfolio thinking, standards governance | 5-Evaluate | AI diffs current vs target architecture | Architecture conformance |
| D064 | **Integration Architect** | ART-038, ART-065 | System context, partner APIs → Integration patterns, event contracts, retry policy | Messaging, idempotency, schema evolution | 6-Create | AI drafts adapter code and contract tests | Integration incident rate |
| D065 | **Cloud Architect** | ART-033, ART-078 | Load model, budget, compliance → Cloud topology, region choice, IaC standards | Cloud networking, cost, resilience | 6-Create | AI cost-models topology options | Cost per 1k requests, availability |
| D066 | **Software Architect** | ART-031, ART-033 | Quality attributes, team topology → Module boundaries, ADRs, code standards | Modularity, coupling analysis, ADR writing | 6-Create | AI analyses dependency graphs for cycles and drift | Change failure rate, mean time to change |
| D067 | **Systems Architect** | ART-032 | Whole-system behaviour, interfaces → Context diagrams, interface contracts | Systems thinking, interface design | 6-Create | AI enumerates interfaces and data flows for review | Interface defect rate |
| D069 | **Network Architect** | ART-033 | Traffic patterns, trust zones → Network segmentation, egress policy, CDN plan | TCP/IP, DNS, TLS, zero-trust | 6-Create | AI drafts firewall rule sets for review; never auto-applies | Lateral movement paths, packet cost |
| D070 | **Domain-Driven Design Lead** | ART-034 | Domain expert input, use cases → Bounded contexts, aggregates, ubiquitous language | DDD, context mapping, event storming | 6-Create | AI clusters terms and proposes contexts; domain experts correct them | Cross-context coupling defects |
| D071 | **API Designer / API Product Manager** | ART-037 | Consumer needs, data model → OpenAPI spec, versioning policy, developer portal | REST/GraphQL design, contract-first | 6-Create | AI generates spec and example payloads; humans review error semantics | Integration time for a new partner |
| D072 | **GraphQL / BFF Architect** | ART-037 | Client needs, service catalogue → Schema design, resolver policy, caching | Schema federation, N+1 control | 6-Create | AI detects N+1 patterns and over-fetching | Mobile payload size, p95 latency |
| D073 | **Event-Driven Architect** | ART-038 | Domain events, consistency needs → Event catalogue, saga designs, outbox pattern | Eventual consistency, idempotency, replay | 6-Create | AI generates saga state machines and failure tests | Event processing lag, duplicate side effects |
| D074 | **Mobile Architect (React Native/Expo)** | ART-033, ART-046 | Screen inventory, device constraints → App architecture, offline strategy, release train | RN internals, native modules, OTA policy | 6-Create | AI scaffolds navigation and state patterns for review | Crash-free sessions, app size |
| D075 | **Backend Architect (Django)** | ART-033, ART-035 | Domain model, traffic model → Service layout, ORM and migration strategy | Django/DRF, caching, async task design | 6-Create | AI proposes app boundaries and migration plans; humans check data safety | p95 latency, migration incidents |

### Finance — 14 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D021 | **Financial Analyst** | ART-011 | Pricing, costs, volumes → Unit economics, cohort model, scenario analysis | Modelling, variance analysis, pricing | 4-Analyse | AI maintains model structure; analyst validates every assumption source | Forecast vs actual variance |
| D022 | **Management Accountant** | ART-011, ART-086 | Ledgers, payouts, fees → Monthly management accounts, cost allocation | Accounting standards, reconciliation | 3-Apply | AI reconciles line items and flags anomalies for review | Reconciliation accuracy, close speed |
| D023 | **Treasury Analyst** | ART-041 | Settlement flows, float, bank fees → Cash forecasting, settlement policy, FX exposure | Cash management, reconciliation, controls | 4-Analyse | AI forecasts settlement timing; analyst sets buffers | Float cost, failed payout rate |
| D024 | **Pricing Analyst** | ART-011 | Willingness-to-pay tests, competitor rates → Take-rate and fee recommendations | Price testing, elasticity, segmentation | 4-Analyse | AI simulates price ladders and margin outcomes | Take rate vs churn trade-off |
| D025 | **Tax Consultant (Ghana)** | ART-013 | Revenue flows, GRA rules → Tax treatment memo, withholding and VAT position | Ghana tax law, digital services tax, payroll | 4-Analyse | AI summarises public GRA guidance; a licensed practitioner certifies | Zero penalties, filings on time |
| D026 | **Internal Auditor** | ART-070 | Processes, ledger, access logs → Audit findings, control remediation plan | Controls testing, sampling | 5-Evaluate | AI samples transactions and drafts exceptions list | Control gap closure |
| D027 | **Investor Relations Manager** | ART-096 | Board packs, metrics → Monthly investor update, reporting pack | Financial narrative, stakeholder comms | 3-Apply | AI drafts the update from dashboards; numbers are locked by finance | Investor response rate, next-round conversion |
| D193 | **Payments Operations Analyst** | ART-041, ART-086 | Provider reports, disputes → Settlement reconciliation, fee analysis | Reconciliation, chargeback handling | 4-Analyse | AI matches settlements to ledger entries and flags breaks | Unreconciled items age |
| D194 | **Billing & Invoicing Specialist** | ART-041 | Contracts, usage → Invoices, dunning, credit notes | Billing logic, collections | 3-Apply | AI drafts dunning sequences | DSO, billing errors |
| D197 | **Vendor / Payroll Compliance Officer** | ART-070 | Worker payouts, tax rules → Withholding decisions, worker classification review | Ghana labour and tax rules | 4-Analyse | AI summarises rule applicability; humans decide cases | Compliance exceptions |
| D210 | **Refund & Chargeback Officer** | ART-042 | Refund requests, provider cases → Refund decisions, chargeback evidence | Provider rules, evidence packs | 3-Apply | AI assembles evidence packs from order logs | Chargeback win rate |
| D225 | **Cloud FinOps Analyst** | ART-086 | Billing exports, tagging → Cost allocation, savings plan | Cost modelling, tagging discipline | 4-Analyse | AI finds idle and oversized resources | Cost per active user |
| D261 | **Revenue Analyst** | ART-011, ART-086 | Fees, payouts, churn → Revenue forecasts, cohort revenue model | Cohort revenue modelling | 4-Analyse | AI projects revenue from cohort curves | Forecast variance |
| D287 | **Revenue Assurance Analyst** | ART-086 | Fees charged vs ledger → Leakage findings, corrections | Reconciliation, control testing | 4-Analyse | AI detects fee anomalies and missed take-rate | Revenue leakage % |

### Growth — 13 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D229 | **Performance Marketing Manager** | ART-088 | Channel data, CAC targets → Campaign plan, creative briefs, budget | Paid acquisition, attribution | 4-Analyse | AI drafts creative variants and predicts CAC ranges | CAC, ROAS |
| D230 | **SEO / ASO Specialist** | ART-088 | Search demand, store metadata → Keyword plan, listing copy, screenshots | Keyword research, store optimisation | 3-Apply | AI clusters keywords and drafts listing copy for review | Organic installs, keyword rank |
| D231 | **Social Media Manager** | ART-088 | Brand voice, community → Content calendar, engagement | Platform craft, crisis awareness | 3-Apply | AI drafts posts; humans approve all public claims | Engagement, follower-to-signup rate |
| D232 | **Content Marketing Lead** | ART-088 | Search demand, product truth → Editorial plan, published assets | Editorial judgement, distribution | 3-Apply | AI drafts long-form from verified briefs; editor owns accuracy | Organic signups per article |
| D233 | **Lifecycle & CRM Manager** | ART-060, ART-088 | Behaviour segments → Triggered journeys, frequency caps | CRM, segmentation, lifecycle design | 4-Analyse | AI builds segment rules and predicts churn | Retention by cohort |
| D234 | **Referral & Affiliate Manager** | ART-088 | Referral loops, fraud data → Programme design, payout rules | Incentive design, fraud control | 4-Analyse | AI detects referral rings | Referred activation, fraud rate |
| D236 | **PR & Communications Lead** | ART-091 | Milestones, media → Press kit, statements, crisis comms | Media relations, message discipline | 3-Apply | AI drafts statements; humans approve every word | Share of voice, sentiment |
| D241 | **Demand Generation Manager** | ART-088 | ICP, intent data → Campaigns, MQLs | Demand programmes, list building | 3-Apply | AI scores inbound leads against ICP | Qualified demand |
| D242 | **Community Programs Designer** | ART-090 | Member needs, ecosystem → Programmes (hackathons, cohorts) | Programme design, partnerships | 6-Create | AI drafts curricula and rubrics | Programme completion |
| D245 | **Employer Branding Lead** | ART-091 | Hiring data, culture → Employer profiles, success stories | Employer content, trust building | 3-Apply | AI drafts case studies from verified outcomes | Employer reply rate |
| D246 | **User Acquisition Analyst** | ART-088 | Attribution data → Channel ROI, experiment plan | Attribution modelling, incrementality | 4-Analyse | AI runs marketing mix comparisons | Incremental installs per cedi |
| D249 | **Experimentation Platform Manager** | ART-088 | Experiment demand → Flagging system, guardrails, analysis standards | Experimentation infrastructure | 4-Analyse | AI monitors sequential testing validity | Valid experiments, false-positive rate |
| D282 | **Brand Strategist** | ART-091 | Audience research, positioning → Naming, positioning, messaging house | Brand strategy, naming | 6-Create | AI generates naming and positioning options for screening | Aided awareness |

### Research — 13 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D006 | **Market Research Analyst** | ART-004 | Public statistics, survey data, competitor pricing → TAM/SAM/SOM model, demand evidence | Sizing, survey design, source triangulation | 4-Analyse | AI drafts the model skeleton; every input must carry a citation or be dropped | Forecast error, source coverage |
| D007 | **Competitive Intelligence Analyst** | ART-005 | Product teardowns, pricing pages, reviews → Landscape matrix, positioning gaps, feature parity map | Teardown, review mining, benchmarking | 4-Analyse | AI clusters app-store reviews at scale; analyst verifies quotes | Gap discovery rate, freshness of matrix |
| D008 | **Market Entry & Expansion Analyst** | ART-004 | City demographics, payment habits, connectivity → City-by-city entry scorecard, sequencing plan | Geo analysis, field interviews, logistics | 3-Apply | AI assembles city profiles from public data for human verification | Entry cost per city, time to liquidity |
| D009 | **UX Researcher** | ART-006 | Participant sessions, diary studies, support tickets → Personas, journey evidence, insight repository | Qualitative method, sampling, synthesis | 5-Evaluate | AI transcribes and clusters sessions; researcher checks every quote | Insight reuse, research-to-decision lag |
| D010 | **User Research Lead** | ART-008 | Research ops, product questions → JTBD statements, research plan, evidence log entries | Research strategy, moderation, bias control | 5-Evaluate | AI builds discussion guides and tag trees; humans run sessions | Interview velocity, hypothesis kill rate |
| D011 | **Ethnographic Field Researcher** | ART-008 | Field observation, community immersion → Contextual notes, workaround inventory | Observation, rapport, note discipline | 4-Analyse | AI structures field notes into themes; field truth stays human | Contextual insight adoption |
| D012 | **Survey Methodologist** | ART-008 | Research questions, sampling frame → Validated instruments, weighted results | Sampling, questionnaire design, weighting | 5-Evaluate | AI pre-tests item wording for ambiguity; methodologist owns validity | Response quality, confidence interval width |
| D013 | **Data Journalist (Ecosystem)** | ART-004 | Public labour and pay data → Ecosystem reports, pay transparency studies | Data storytelling, verification | 3-Apply | AI drafts narrative from verified tables | Publication accuracy, citations |
| D016 | **Behavioural Scientist** | ART-007 | Journeys, drop-off data → Behavioural interventions, experiment designs | Bias models, nudging, ethics review | 5-Evaluate | AI drafts intervention variants and expected effect sizes | Lift per intervention, harm avoided |
| D030 | **Experimentation & Evidence Lead** | ART-015, ART-088 | Hypotheses, metrics, traffic → Experiment designs, verdicts, evidence log | Causal inference, power analysis, guardrails | 5-Evaluate | AI computes power and drafts result memos; humans check for confounders | Experiment win rate, decisions changed by evidence |
| D250 | **Insights & Research Librarian** | ART-008, ART-092 | All research artefacts → Searchable evidence repository | Information architecture, taxonomies | 3-Apply | AI indexes and deduplicates insights | Insight reuse rate |
| D267 | **Customer Research Panel Manager** | ART-008 | Panel members → Recruited, incentivised participants | Panel operations, incentives | 2-Understand | AI schedules and segments panel members | Panel response rate |
| D272 | **Impact Measurement Lead** | ART-099 | Programme outcomes → Impact framework, evaluation reports | Theory of change, attribution | 5-Evaluate | AI drafts theory-of-change trees and survey instruments | Jobs filled, income uplift |

### People — 12 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D251 | **Talent Acquisition Partner** | ART-095 | Hiring plan, scorecards → Hired candidates, pipeline data | Structured interviewing, sourcing | 3-Apply | AI screens applications against the scorecard; humans interview | Time to hire, quality of hire |
| D252 | **People Operations Manager** | ART-095 | Headcount plan, policies → Policies, onboarding, HRIS accuracy | Employment law basics, ops | 3-Apply | AI drafts policy updates from legal changes; humans approve | eNPS, compliance |
| D253 | **Compensation & Benefits Analyst** | ART-095 | Market data, budget → Bands, equity guidelines | Benchmarking, pay equity | 4-Analyse | AI benchmarks roles against market surveys | Pay equity gaps |
| D254 | **Learning & Development Lead** | ART-095 | Skill gaps, role paths → L&D plan, completion data | ADDIE-style design, evaluation | 3-Apply | AI generates role-based learning paths | Skill uplift, completion |
| D255 | **HR Business Partner** | ART-095, ART-090 | Team performance, conflicts → Coaching, org design, ER cases | Coaching, conflict resolution | 4-Analyse | AI summarises 1:1 themes without identifying individuals | Attrition, engagement |
| D256 | **Diversity, Equity & Inclusion Lead** | ART-095 | Workforce data, hiring funnels → Inclusion interventions, pay reviews | Equity analysis, inclusive design | 5-Evaluate | AI measures funnel disparities; humans design remedies | Representation at each stage |
| D257 | **Internal Communications Manager** | ART-095 | Company news, change → Internal comms, town halls | Clear writing, change comms | 3-Apply | AI drafts internal updates | Read-through rate |
| D258 | **Workplace Experience Coordinator** | ART-095 | Team needs → Remote/hybrid norms, recognition | Employee experience design | 2-Understand | AI analyses pulse survey themes | eNPS |
| D259 | **Payroll & Compliance Officer** | ART-070 | Staff data, SSNIT/GRA rules → Payroll runs, statutory filings | Payroll, statutory compliance | 2-Understand | AI reconciles payroll changes | Payroll accuracy, filings on time |
| D260 | **Volunteer & Mentorship Coordinator** | ART-090 | Volunteer pool, needs → Rota, mentorship pairings | Volunteer management | 3-Apply | AI suggests matches from stated skills and availability | Volunteer retention, matches made |
| D275 | **Internal Enablement Trainer** | ART-095 | Role competencies → Training sessions, assessments | Instructional delivery | 3-Apply | AI generates quiz banks from the curriculum | Assessment pass rate |
| D290 | **Technical Recruiter (Engineering)** | ART-095 | Tech hiring plan → Engineering hires | Technical sourcing, calibration | 3-Apply | AI sources candidates by skill graph; humans assess | Engineering time to hire |

### Delivery — 11 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D037 | **Program Manager** | ART-093 | Multi-team plans, dependencies → Integrated plan, dependency resolution, status | Programme planning, risk escalation | 4-Analyse | AI rolls up status and flags slipping dependencies | Milestone hit rate |
| D038 | **Project Manager** | ART-027 | Scope, budget, timeline → Project plan, RAID log updates, change control | Planning, critical path, stakeholder comms | 3-Apply | AI maintains the plan and drafts change requests | On-time, on-scope delivery |
| D039 | **Scrum Master** | ART-094 | Team process, impediments → Facilitated ceremonies, removed blockers, retro actions | Agile facilitation, coaching, impediment removal | 5-Evaluate | AI prepares agenda and past-action follow-ups | Impediment cycle time, team health |
| D043 | **Agile Coach** | ART-026, ART-094 | Team behaviour, metrics → Coaching plan, maturity assessment | Systems coaching, facilitation | 5-Evaluate | AI summarises retro themes across sprints | Team maturity trend |
| D044 | **Release Train Engineer** | ART-053, ART-058, ART-094 | Release commitments, dependencies → Release calendar, go/no-go packs | Release coordination, dependency management | 3-Apply | AI assembles release readiness evidence from CI and trackers | Release predictability |
| D045 | **Technical Program Manager** | ART-053 | Architecture plan, cross-team dependencies → Technical milestones, risk burndown | Technical planning, dependency mapping | 4-Analyse | AI maps code ownership to milestone risk | Cross-team blockers resolved on time |
| D046 | **Delivery Manager** | ART-027, ART-058 | Pipeline health, capacity → Delivery forecasts, WIP control | Flow metrics, capacity planning | 4-Analyse | AI forecasts completion from cycle-time distributions | Forecast accuracy, WIP limit adherence |
| D047 | **Estimation & Sizing Analyst** | ART-027 | Backlog, historical data → Size estimates, confidence ranges | Reference class forecasting, decomposition | 4-Analyse | AI computes reference-class distributions from past tickets | Estimate error bands |
| D057 | **PMO Analyst** | ART-028, ART-081 | Project data, gate criteria → Portfolio dashboard, gate evidence | Reporting, governance, standards | 3-Apply | AI assembles gate packs from trackers | Gate evidence completeness |
| D217 | **Launch Manager** | ART-081, ART-058 | Readiness evidence, comms plan → Go/no-go decision pack, launch timeline | Cross-functional coordination, risk framing | 5-Evaluate | AI assembles the readiness pack and open-risk summary | Launch issues in first 14 days |
| D300 | **Continuous Improvement Lead** | ART-094 | Retro actions, incident trends → Improvement portfolio, verified gains | Lean/Six Sigma thinking | 5-Evaluate | AI mines incident and ticket data for waste patterns | Verified improvement value |

### Content — 10 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D051 | **Localisation & Translation Manager** | ART-061 | Source content, target languages → Localised strings, glossaries, QA sign-off | Translation management, cultural adaptation | 3-Apply | AI pre-translates with a glossary lock; a human native reviewer signs off | Localisation defect rate |
| D052 | **Technical Writer** | ART-037, ART-062 | Specs, code, support tickets → API docs, help centre articles, runbooks | Information architecture, plain language | 3-Apply | AI drafts docs from OpenAPI and code; writer verifies examples run | Doc search success rate |
| D053 | **UX Writer / Content Designer** | ART-061 | Screens, user mental models → Microcopy, error messages, empty states | Plain language, tone, local idiom | 3-Apply | AI A/B drafts microcopy; writer checks tone and local meaning | Form completion, support contacts per screen |
| D112 | **Documentation Engineer** | ART-037, ART-052 | Code, contracts, runbooks → Docs-as-code pipeline, generated references | Docs tooling, versioning | 3-Apply | AI drafts and links references; humans test snippets | Broken doc links, doc build success |
| D186 | **Knowledge Base Editor** | ART-062 | Tickets, product changes → Help articles, deflections | Information architecture, plain writing | 3-Apply | AI drafts articles from ticket threads; editor verifies accuracy | Self-service deflection rate |
| D219 | **Developer Relations / DevRel** | ART-037, ART-090 | API, developer needs → Guides, sample apps, community talks | Technical communication, demo building | 3-Apply | AI drafts tutorials; DevRel verifies code runs | API activation by third parties |
| D238 | **Motion & Video Producer** | ART-090 | Stories, product demos → Explainers, ad cuts, event recaps | Storyboarding, editing | 6-Create | AI drafts scripts and rough cuts | View-through rate |
| D243 | **Developer Educator** | ART-090, ART-098 | Skill gaps, curriculum → Courses, workshops, assessments | Instructional design | 6-Create | AI drafts lesson plans; human validates exercises | Learner outcome uplift |
| D285 | **Keyword & Taxonomy Curator** | ART-097 | Job titles, skill mentions → Canonical skill graph, aliases | Taxonomy maintenance, NLP oversight | 3-Apply | AI proposes alias merges; curator validates meaning | Search miss rate |
| D299 | **Documentation Localiser** | ART-061 | English docs → Localised help content | Translation, technical understanding | 3-Apply | AI pre-translates; humans review | Help content coverage by language |

### Design — 10 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D014 | **Service Designer** | ART-007 | Journeys, backstage operations, policies → Journey maps, service blueprints, failure-mode list | Blueprinting, systems thinking, facilitation | 6-Create | AI generates journey variants for critique | Drop-off reduction at mapped steps |
| D015 | **Design Thinking Facilitator** | ART-007, ART-047 | Team, problem space → Workshop outputs, opportunity backlog | Facilitation, ideation, convergence methods | 6-Create | AI produces divergent prompt sets; facilitator keeps divergent phase truly divergent | Ideas reaching prototype |
| D055 | **Accessibility Specialist** | ART-045, ART-047 | Designs, builds, user feedback → A11y audit, remediation tickets, conformance statement | WCAG 2.2 AA, assistive tech testing | 5-Evaluate | AI scans for code-level a11y issues; human tests with screen readers | WCAG AA conformance, complaint count |
| D105 | **Mobile UX/UI Designer** | ART-046 | Personas, journeys, platform guidelines → Screen designs, states, prototypes | iOS/Android patterns, low-end device constraints | 6-Create | AI generates layout variants for critique; designer owns hierarchy | Task success rate, first-pass design acceptance |
| D106 | **Design System Engineer** | ART-045 | Tokens, component specs → Component library, docs, versioning | Tokens, theming, a11y primitives | 3-Apply | AI generates variants and docs from tokens | Component reuse, a11y defects per component |
| D237 | **Brand Designer** | ART-091, ART-045 | Brand strategy → Identity system, templates | Visual identity, typography | 6-Create | AI explores concepts; designers choose and refine | Brand consistency defects |
| D263 | **Data Visualisation Designer** | ART-086, ART-096 | Metric definitions, audience → Clear charts, report layouts | Visual encoding, chart honesty | 3-Apply | AI generates chart drafts; designer fixes misleading encodings | Decision-maker comprehension |
| D283 | **UX Auditor** | ART-047, ART-055 | Live app, heuristics → Heuristic evaluation, prioritised fixes | Nielsen heuristics, WCAG | 5-Evaluate | AI runs screenshot-based heuristic passes; auditor verifies | Severity-weighted findings fixed |
| D284 | **Persona Custodian** | ART-006 | Research evidence → Current personas, anti-personas | Synthesis, ongoing validation | 4-Analyse | AI flags persona drift when new evidence contradicts | Persona freshness |
| D295 | **Accessibility Advocate / Community Liaison** | ART-047 | Disabled users' feedback → Accessibility roadmap input | Advocacy, co-design | 4-Analyse | AI summarises community feedback | Accessibility issues raised and fixed |

### Governance — 8 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D277 | **Certification Board Chair** | ART-098 | Assessment results, appeals → Certification decisions, standards updates | Governance, standard-setting | 5-Evaluate | AI produces decision packs; board decides | Appeal rate, employer acceptance |
| D278 | **Dispute Arbitration Panel Member** | ART-042 | Dispute files → Panel decisions | Neutral adjudication | 5-Evaluate | AI summarises evidence chronologically | Decision consistency |
| D279 | **Marketplace Policy Adjudicator** | ART-084 | Policy cases → Precedent-setting decisions | Policy reasoning, writing rationale | 5-Evaluate | AI retrieves relevant precedents | Consistency across cases |
| D280 | **Chairperson (Advisory Board)** | ART-093 | Board materials → Governance decisions, oversight | Governance, strategy oversight | 5-Evaluate | AI prepares board packs from approved metrics | Board effectiveness |
| D281 | **Non-Executive Director** | ART-070 | Board reporting → Challenge, oversight, approval | Independent judgement | 5-Evaluate | AI provides comparison benchmarks | Oversight quality |
| D288 | **ESG / Social Impact Reporting Officer** | ART-099, ART-096 | Impact data, funder asks → Impact reports, ESG disclosures | Impact reporting standards | 3-Apply | AI drafts reports from verified metrics | Reports accepted by funders |
| D296 | **Data Ethics Reviewer** | ART-029, ART-050 | Data uses, model designs → Ethics review decisions | Applied ethics, harm analysis | 5-Evaluate | AI drafts harm scenarios; reviewer decides | Reviews before launch |
| D298 | **Open Source Programme Office (OSPO) Lead** | ART-076 | Dependencies, contributions → Licence policy, contribution approvals | Licensing, community norms | 4-Analyse | AI audits licences and attribution | Licence violations |

### Leadership — 6 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D001 | **Founder & CEO** | ART-001, ART-009 | Market signals, capital, constraints → Vision, strategy brief, funding plan, hiring plan | Vision, fundraising, capital allocation, storytelling | 6-Create | AI drafts option sets and sensitivity tables; the human picks the bet | Survival, funding raised, NSM trend |
| D002 | **Co-founder & CTO** | ART-031, ART-051 | Strategy, product scope, risk appetite → Technical strategy, architecture guardrails, eng budget | Systems design, team building, build-vs-buy | 6-Create | AI accelerates spike prototypes and option research; CTO owns irreversible calls | Delivery predictability, platform reliability, eng cost per release |
| D005 | **Chief Operating Officer** | ART-081 | Strategy, unit economics → Operating cadence, hiring plan, launch gate decisions | Operations design, process control, cross-functional leadership | 5-Evaluate | AI maintains the operating dashboard and flags drift from plan | Cost per active user, SLA attainment, launch readiness |
| D042 | **Chief of Staff** | ART-093 | Leadership decisions, cross-team state → OKR tracking, decision log, follow-through | Coordination, writing, prioritisation | 5-Evaluate | AI maintains decision log and chases open items | Decisions closed within SLA |
| D056 | **Risk Manager** | ART-014 | All workstreams → RAID log, risk appetite statement, mitigation owners | Risk assessment, scenario planning | 5-Evaluate | AI monitors signals and suggests risk scores; managers decide | Risks with active mitigation |
| D119 | **Technical Lead / Engineering Manager** | ART-051, ART-052 | Team capacity, roadmap → Technical direction, staffing, delivery health | Leadership, code review, mentoring | 5-Evaluate | AI summarises code-review risk and review latency | Team retention, delivery health |

### Product — 6 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D003 | **Head of Product** | ART-010, ART-016 | Strategy, research, analytics → NSM tree, roadmap, product decisions | Product sense, prioritisation, metrics literacy | 5-Evaluate | AI synthesises interviews and drafts specs; human validates problem selection | Activation, match-fill, retention |
| D031 | **Product Manager** | ART-016, ART-027, ART-092, ART-100 | Research, metrics, business goals → PRD, roadmap, prioritised backlog | Discovery, prioritisation, stakeholder alignment | 5-Evaluate | AI drafts PRDs and acceptance criteria; PM owns the 'why' and the cut line | Outcome attainment per release |
| D032 | **Product Owner** | ART-022 | PRD, backlog, sprint goals → Refined stories, ordering, sprint acceptance | Backlog management, value ordering | 5-Evaluate | AI splits epics and drafts stories; PO rejects anything untestable | Story cycle time, rework rate |
| D041 | **Product Operations Manager** | ART-092, ART-026 | Process friction, tooling → Operating cadence, templates, DoR/DoD compliance | Process design, tooling, enablement | 4-Analyse | AI audits tickets against DoR/DoD and reports gaps | Process compliance, cycle-time reduction |
| D247 | **Growth Product Manager** | ART-060, ART-088 | Funnel data, experiments → Activation/retention experiments | Growth loops, experimentation | 5-Evaluate | AI ranks experiments by expected lift over effort | Experiment win rate |
| D268 | **AI Product Manager** | ART-050 | AI capabilities, user problems → AI feature specs, eval criteria, guardrails | AI literacy, eval design, risk framing | 5-Evaluate | AI prototypes features; PM defines acceptance thresholds | AI feature adoption, hallucination complaints |

### Legal — 5 roles

| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D017 | **Legal Counsel (Commercial & Labour)** | ART-070 | Contracts, product flows, employment law → T&Cs, contractor agreements, dispute liability position | Contract law, platform liability, IP | 5-Evaluate | AI drafts clause comparisons and flags risk; counsel signs off | Contract cycle time, disputes lost to unclear terms |
| D018 | **Regulatory Affairs Manager** | ART-013 | Acts, BoG/DPC/CSA guidance → Licensing map, filing calendar, regulator correspondence | Regulatory interpretation, filing management | 5-Evaluate | AI tracks published notices and diffs them; humans verify before acting | Filings on time, zero unlicensed activity |
| D207 | **Legal Operations Analyst** | ART-070 | Contracts, disputes → Contract database, obligation tracker | Contract lifecycle management | 3-Apply | AI extracts obligations and renewal dates from contracts | Missed obligations |
| D208 | **IP & Trademark Coordinator** | ART-091 | Brand assets, filings → Trademark register, infringement log | IP process, jurisdiction rules | 3-Apply | AI searches for conflicting marks in public registries; counsel advises | Filings on time |
| D273 | **Policy & Public Affairs Analyst** | ART-013 | Legislation, consultations → Position papers, consultation responses | Policy analysis, writing | 4-Analyse | AI summarises consultation documents | Consultations responded to |

## 1.4 Coverage proof

Three assertions are checked mechanically by the generator (build fails if violated):

1. every role owns at least one artefact — no job exists without a deliverable;
2. every artefact has exactly one accountable owner — no unowned work;
3. every artefact has a written definition of done — no "done" by assertion.

Artefacts with more than one owning role (accountable owner in *italics*):

| Artefact | Name | Accountable | Also involved |
| --- | --- | --- | --- |
| ART-004 | Market Sizing Model (TAM/SAM/SOM) | *D006 Market Research Analyst* | D008, D013 |
| ART-006 | Persona & Two-Sided Ecosystem Map | *D009 UX Researcher* | D284 |
| ART-007 | Customer Journey Map (AS-IS / TO-BE) | *D014 Service Designer* | D015, D016, D050 |
| ART-008 | Jobs-to-be-Done & Interview Synthesis | *D010 User Research Lead* | D011, D012, D250, D267 |
| ART-009 | Product Strategy Brief | *D001 Founder & CEO* | D029 |
| ART-011 | Financial Model & Unit Economics | *D021 Financial Analyst* | D022, D024, D248, D261 |
| ART-013 | Regulatory & Licensing Map | *D018 Regulatory Affairs Manager* | D019, D025, D273 |
| ART-016 | Product Requirements Document (PRD) | *D031 Product Manager* | D003 |
| ART-019 | Capability Map (L0/L1/L2) | *D034 Systems Analyst* | D063 |
| ART-021 | Role & Permission Matrix (RBAC/ABAC) | *D034 Systems Analyst* | D146, D152 |
| ART-026 | Definition of Ready / Done + AC Standard | *D043 Agile Coach* | D041, D198 |
| ART-027 | Release Roadmap & Scope (MoSCoW) | *D031 Product Manager* | D038, D046, D047 |
| ART-028 | Requirements Traceability Matrix | *D033 Business Analyst* | D057 |
| ART-029 | Data Requirements & Privacy Impact Assessment | *D054 Data Protection Officer* | D170, D296 |
| ART-030 | Analytics & Measurement Plan | *D040 Product Analytics Lead* | D079 |
| ART-031 | Architecture Decision Records (ADR index) | *D066 Software Architect* | D002, D063 |
| ART-032 | System Context Diagram (C4 L1) | *D067 Systems Architect* | D061 |
| ART-033 | Container & Deployment Diagram (C4 L2/L3) | *D066 Software Architect* | D061, D065, D069, D074, D075, D110 |
| ART-035 | Entity Relationship Diagram (ERD) | *D077 Database Designer / DBA* | D075, D104 |
| ART-036 | Data Dictionary | *D076 Data Architect* | D189, D190, D211, D212 |
| ART-037 | API Specification (OpenAPI 3.1) | *D071 API Designer / API Product Manager* | D052, D072, D099, D101, D112, D143, D219 |
| ART-038 | Event Catalogue & Async Contracts | *D073 Event-Driven Architect* | D064, D143 |
| ART-039 | Matching & Ranking System Design | *D084 Recommendation & Ranking Engineer* | D080, D087, D214, D215, D264, D265, D271 |
| ART-041 | Payments, Escrow & Payout Design | *D100 Payments Engineer* | D023, D137, D181, D193, D194 |
| ART-042 | Dispute & Resolution Workflow Design | *D062 Trust & Reputation Architect* | D180, D210, D278 |
| ART-044 | Identity, KYC & Verification Design | *D099 Backend Developer (Python/Django/DRF)* | D086, D152, D154 |
| ART-045 | Design System & UI Kit | *D106 Design System Engineer* | D055, D111, D237 |
| ART-046 | Screen Inventory & Navigation Map | *D105 Mobile UX/UI Designer* | D074, D098, D101, D102 |
| ART-047 | Interaction Prototype & Usability Test Plan | *D116 Prototyping Engineer* | D015, D055, D129, D142, D283, D295 |
| ART-048 | Threat Model (STRIDE + LINDDUN) | *D187 Security Programme Manager* | D068 |
| ART-049 | Capacity, Cost & Scalability Model | *D224 Capacity & Performance Planner* | D118, D226 |
| ART-050 | AI/ML System Design & Model Cards | *D081 ML Engineer* | D085, D090, D145, D268, D269, D296 |
| ART-051 | Engineering Standards & Conventions | *D120 Code Review / Standards Owner* | D002, D113, D119 |
| ART-052 | Repository Structure & Branching Model | *D151 Application Security Manager* | D112, D113, D119 |
| ART-053 | CI/CD Pipeline Specification | *D150 CI/CD Security Engineer* | D044, D045, D108 |
| ART-054 | Test Strategy & Master Test Plan | *D173 Support Agent (Tier 1)* | D099, D121, D131, D132 |
| ART-055 | Test Cases & Automation Matrix | *D141 SDET (Software Development Engineer in Test)* | D107, D117, D122, D123, D124, D125, D128, D139, D140, D283 |
| ART-056 | Synthetic Data & Test Fixtures Policy | *D216 Synthetic Data & Fixtures Engineer* | D126 |
| ART-057 | Environment Matrix & Secrets Management | *D091 DevOps Engineer* | D114, D127 |
| ART-058 | Release Notes & Changelog Standard | *D217 Launch Manager* | D044, D046, D095, D132 |
| ART-059 | Mobile Store Readiness Checklist | *D135 Beta / Field Test Coordinator* | D124 |
| ART-060 | Onboarding & Activation Funnel Spec | *D040 Product Analytics Lead* | D182, D183, D233, D247, D266 |
| ART-061 | Content & Localisation Style Guide | *D053 UX Writer / Content Designer* | D051, D115, D130, D294, D299 |
| ART-062 | Support Playbook & Macros | *D235 Sales Operations Manager* | D052, D172, D173, D174, D185, D186, D199, D209, D274 |
| ART-063 | Model Training & Evaluation Pack | *D133 ML / Model Test Engineer* | D078, D081, D082, D083, D270, D271 |
| ART-064 | Prompt & Agent Library | *D089 Prompt Engineer* | D085, D088, D134, D145 |
| ART-065 | Integration & Webhook Catalogue | *D165 Business Continuity Manager* | D028, D058, D064, D103, D109, D117, D188, D204, D221, D274 |
| ART-066 | Security Architecture Review | *D096 Security Engineer* | D068, D161 |
| ART-067 | ASVS Verification Report | *D177 Marketplace Operations Analyst* | D097, D146, D149, D151 |
| ART-069 | Penetration Test Report & Remediation Log | *D182 Onboarding Specialist (Freelancer)* | D147, D148, D292 |
| ART-070 | Compliance Register & Evidence Pack | *D201 Compliance Officer* | D017, D026, D090, D136, D164, D187, D197, D206, D207, D211, D259, D269, D281, D291 |
| ART-071 | Privacy Notice, Consent & DSAR Runbook | *D202 Privacy Operations Analyst* | D054, D297 |
| ART-072 | Fraud & Abuse Playbook | *D195 Fraud Rules Engine Owner* | D153, D163, D169, D179, D286 |
| ART-073 | Incident Response Plan & Runbooks | *D192 Revenue Operations Analyst* | D156, D162, D196 |
| ART-074 | DR/BCP Plan & Restore Evidence | *D227 Disaster Recovery Engineer* | D104, D138, D165, D205, D213 |
| ART-075 | Vulnerability Management Policy | *D190 Data Quality Engineer* | D151, D155, D157, D158, D159 |
| ART-076 | Supply Chain Security Pack (SBOM) | *D188 Third-Party Risk Analyst* | D150, D160, D298 |
| ART-077 | Vulnerability Disclosure Policy | *D191 BI / Reporting Developer* | D213, D293 |
| ART-078 | Infrastructure as Code Specification | *D091 DevOps Engineer* | D065, D093, D228 |
| ART-079 | Observability & Alerting Design | *D094 Observability Engineer* | D082, D144, D158, D190 |
| ART-080 | SLO/SLI & Error Budget Policy | *D094 Observability Engineer* | D092, D199 |
| ART-081 | Launch Readiness Checklist (Go/No-Go) | *D217 Launch Manager* | D005, D057 |
| ART-082 | Release & Rollback Runbook | *D218 Rollout / Canary Manager* | D095 |
| ART-084 | Trust & Safety Operations Manual | *D239 Community Moderator* | D050, D167, D168, D171, D178, D200, D279, D286 |
| ART-085 | Data Retention & Deletion Schedule | *D203 Records & Retention Manager* | D170 |
| ART-086 | Cost & Unit-Economics Dashboard | *D225 Cloud FinOps Analyst* | D022, D191, D193, D261, D263, D287 |
| ART-088 | Growth Experiment Backlog | *D249 Experimentation Platform Manager* | D030, D060, D192, D229, D230, D231, D232, D233, D234, D235, D241, D246, D247, D262 |
| ART-089 | Marketplace Liquidity Playbook | *D240 Marketplace Supply Manager* | D059, D177, D184, D222, D264 |
| ART-090 | Community & Events Playbook | *D255 HR Business Partner* | D175, D176, D219, D220, D238, D242, D243, D244, D260 |
| ART-091 | Brand, Naming & Positioning Kit | *D282 Brand Strategist* | D208, D236, D237, D245 |
| ART-092 | Continuous Discovery Cadence | *D031 Product Manager* | D041, D250 |
| ART-093 | Quarterly OKR & Roadmap Review | *D042 Chief of Staff* | D037, D280, D289 |
| ART-094 | Retrospective & Process Improvement Kit | *D044 Release Train Engineer* | D039, D043, D198, D300 |
| ART-095 | Training & Enablement Curriculum | *D275 Internal Enablement Trainer* | D251, D252, D253, D254, D255, D256, D257, D258, D290, D291 |
| ART-096 | Investor/Donor Reporting Pack | *D288 ESG / Social Impact Reporting Officer* | D027, D191, D263 |
| ART-097 | Skills Taxonomy & Level Framework | *D048 Domain Expert (Labour Market & Skills)* | D285 |
| ART-098 | Assessment & Certification Design | *D277 Certification Board Chair* | D243, D276 |
| ART-099 | Impact Measurement Framework | *D272 Impact Measurement Lead* | D288 |
