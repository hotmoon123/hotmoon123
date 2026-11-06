# 00 — Artefact Index: 110 Deliverables That Define the System

> Generated from `tools/data/artifacts.yaml`. The eight cells are the SDLC itself
> (see `02-sdlc-framework.md`). An artefact is real only when it satisfies its definition of done.

| Cell | Artefacts |
| --- | ---: |
| discover | 15 |
| define | 16 |
| architect | 19 |
| build | 9 |
| assure | 13 |
| secure | 12 |
| deploy | 14 |
| sustain | 12 |
| **total** | **110** |

## Discover — 15 artefacts

| ID | Artefact | Accountable owner | Standard / source | Definition of done |
| --- | --- | --- | --- | --- |
| ART-001 | **Vision & Mission Canvas** | D001 Founder & CEO | internal convention | One page; names the user, the pain, the promise, and the 12-month bet; founder signs it. |
| ART-002 | **Lean Canvas** | D004 Business Architect | S1 | All 9 blocks filled; every 'unfair advantage' claim has evidence or is labelled a hypothesis. |
| ART-003 | **Business Model Canvas** | D004 Business Architect | S1 | Two canvases: MVP model and 24-month model; unit economics consistent with ART-011. |
| ART-004 | **Market Sizing Model (TAM/SAM/SOM)** | D006 Market Research Analyst | internal convention | Bottom-up build from public counts; every input has a source and a date; formula visible. |
| ART-005 | **Competitive Landscape Matrix** | D007 Competitive Intelligence Analyst | internal convention | >=8 comparables (GH + Africa + global); columns are buyer-verifiable facts, not vibes. |
| ART-006 | **Persona & Two-Sided Ecosystem Map** | D009 UX Researcher | internal convention | >=3 personas per side; each persona tied to >=3 verbatim research quotes. |
| ART-007 | **Customer Journey Map (AS-IS / TO-BE)** | D014 Service Designer | internal convention | Every step has emotion, failure mode, and the product countermeasure. |
| ART-008 | **Jobs-to-be-Done & Interview Synthesis** | D010 User Research Lead | internal convention | >=12 interviews documented; JTBD statements in 'when/ I want to/ so I can' form; raw notes retained. |
| ART-009 | **Product Strategy Brief** | D001 Founder & CEO | internal convention | States the wedge, the moat hypothesis, what we refuse to build, and the kill criteria. |
| ART-010 | **North Star Metric & KPI Tree** | D003 Head of Product | internal convention | One NSM, 3 input metrics, formula and data source for each; reviewed monthly. |
| ART-011 | **Financial Model & Unit Economics** | D021 Financial Analyst | internal convention | Take-rate scenarios, CAC/LTV, contribution margin per match; assumptions tab is editable. |
| ART-012 | **Funding & Grants Plan** | D020 Fundraising & Grants Manager | internal convention | 18-month cash need, sources (grant/equity/revenue), and the milestone each tranche buys. |
| ART-013 | **Regulatory & Licensing Map** | D018 Regulatory Affairs Manager | S2, S5, S6 | Each obligation mapped: who, what filing, deadline, owner, evidence location. |
| ART-014 | **RAID Log (Risks/Assumptions/Issues/Deps)** | D056 Risk Manager | internal convention | Each entry has owner, probability, impact, mitigation, and review date. |
| ART-015 | **Assumptions & Evidence Log** | D030 Experimentation & Evidence Lead | internal convention | Every load-bearing assumption has a test, a result, and a verdict (supported/rejected). |

## Define — 16 artefacts

| ID | Artefact | Accountable owner | Standard / source | Definition of done |
| --- | --- | --- | --- | --- |
| ART-016 | **Product Requirements Document (PRD)** | D031 Product Manager | internal convention | Problem, users, scope, out-of-scope, success metrics, open questions; versioned. |
| ART-017 | **Business Requirements Document (BRD)** | D033 Business Analyst | internal convention | Business goals, constraints, stakeholders, and acceptance of the operating model. |
| ART-018 | **Software Requirements Specification** | D035 Requirements Engineer | S7 | Functional + non-functional requirements, uniquely identified and verifiable. |
| ART-019 | **Capability Map (L0/L1/L2)** | D034 Systems Analyst | internal convention | Every capability maps to a cell, a product area, and an owning role; no orphans. |
| ART-020 | **Domain Glossary / Ubiquitous Language** | D048 Domain Expert (Labour Market & Skills) | internal convention | Every term used in code, UI, and contracts has one definition; conflicts resolved. |
| ART-021 | **Role & Permission Matrix (RBAC/ABAC)** | D034 Systems Analyst | internal convention | Every actor x resource cell filled; least privilege; denied-by-default tested. |
| ART-022 | **User Story Map & Story Index** | D032 Product Owner | internal convention | Stories sliced by journey step; each has ID, Given/When/Then pointer, and priority. |
| ART-023 | **Use Case Catalogue** | D034 Systems Analyst | internal convention | Main, alternate, and exception flows for each actor goal; postconditions stated. |
| ART-024 | **Business Rules Catalogue (Decision Tables)** | D049 Business Rules Analyst | internal convention | Each rule has ID, trigger, condition table, outcome, and a unit test reference. |
| ART-025 | **NFRs & Quality Attribute Scenarios** | D036 Non-Functional Requirements Analyst | S8 | Each NFR is a measurable scenario (source/stimulus/response/measure), not an adjective. |
| ART-026 | **Definition of Ready / Done + AC Standard** | D043 Agile Coach | internal convention | Adopted by the team; checked in every backlog review; violations logged. |
| ART-027 | **Release Roadmap & Scope (MoSCoW)** | D031 Product Manager | internal convention | MVP / v1 / v2 with dates and the one metric each release must move. |
| ART-028 | **Requirements Traceability Matrix** | D033 Business Analyst | internal convention | Goal -> capability -> story -> test -> artefact; generated, not hand-maintained. |
| ART-029 | **Data Requirements & Privacy Impact Assessment** | D054 Data Protection Officer | S2, S3 | Every field: purpose, lawful basis, retention, sharing, cross-border; approved by DPO. |
| ART-030 | **Analytics & Measurement Plan** | D040 Product Analytics Lead | internal convention | Event taxonomy with names, properties, owner, and the decision each metric informs. |
| ART-097 | **Skills Taxonomy & Level Framework** | D048 Domain Expert (Labour Market & Skills) | internal convention | Skill families, canonical names, aliases, and level descriptors for L1-L5. |

## Architect — 19 artefacts

| ID | Artefact | Accountable owner | Standard / source | Definition of done |
| --- | --- | --- | --- | --- |
| ART-031 | **Architecture Decision Records (ADR index)** | D066 Software Architect | internal convention | Each ADR: context, options, decision, consequences, status, date; superseded ones kept. |
| ART-032 | **System Context Diagram (C4 L1)** | D067 Systems Architect | S9 | Every external system and actor; trust boundary drawn; data flows labelled. |
| ART-033 | **Container & Deployment Diagram (C4 L2/L3)** | D066 Software Architect | S9 | Runtimes, protocols, stores, queues, and failure domains labelled; matches IaC. |
| ART-034 | **Domain Model & Bounded Contexts (DDD)** | D070 Domain-Driven Design Lead | internal convention | Context map with relationships and ownership; aggregates named; invariants listed. |
| ART-035 | **Entity Relationship Diagram (ERD)** | D077 Database Designer / DBA | internal convention | Every table, key, cardinality, and constraint; generated from migrations. |
| ART-036 | **Data Dictionary** | D076 Data Architect | internal convention | Every column: type, nullability, meaning, owner, PII flag, retention. |
| ART-037 | **API Specification (OpenAPI 3.1)** | D071 API Designer / API Product Manager | S10 | Lints clean; every endpoint has auth scope, error model, pagination, and rate limit. |
| ART-038 | **Event Catalogue & Async Contracts** | D073 Event-Driven Architect | internal convention | Each event: schema version, producer, consumers, idempotency key, replay policy. |
| ART-039 | **Matching & Ranking System Design** | D084 Recommendation & Ranking Engineer | internal convention | Features, labels, objective, evaluation method, explainability, and cold-start plan. |
| ART-040 | **Trust & Reputation System Design** | D062 Trust & Reputation Architect | internal convention | Score inputs, weights, decay, appeal path, and anti-gaming controls documented. |
| ART-041 | **Payments, Escrow & Payout Design** | D100 Payments Engineer | S5, S11 | Every money state transition, double-entry ledger, fees, refunds, and licence position. |
| ART-042 | **Dispute & Resolution Workflow Design** | D062 Trust & Reputation Architect | internal convention | Deadlines, evidence rules, decision authority, appeals, and payout effects per outcome. |
| ART-043 | **Notification & Engagement Architecture** | D166 Notification & Messaging Platform Engineer | internal convention | Channel matrix (push/SMS/email/WhatsApp), cost per message, quiet hours, opt-out. |
| ART-044 | **Identity, KYC & Verification Design** | D099 Backend Developer (Python/Django/DRF) | S3 | ID types accepted in GH, liveness method, manual review queue, data minimisation. |
| ART-045 | **Design System & UI Kit** | D106 Design System Engineer | S12 | Tokens (colour/type/space/elevation), components, states, and a11y annotations. |
| ART-046 | **Screen Inventory & Navigation Map** | D105 Mobile UX/UI Designer | internal convention | Every screen: purpose, entry points, states (empty/loading/error/offline), owner. |
| ART-047 | **Interaction Prototype & Usability Test Plan** | D116 Prototyping Engineer | S13 | Clickable prototype; >=5 test participants; tasks, success criteria, findings log. |
| ART-049 | **Capacity, Cost & Scalability Model** | D224 Capacity & Performance Planner | internal convention | Requests/GB per 1k users, cost per user, the first bottleneck, and the scale-out trigger. |
| ART-050 | **AI/ML System Design & Model Cards** | D081 ML Engineer | S16 | Model purpose, data lineage, eval set, guardrails, fallback, monitoring, model card. |

## Build — 9 artefacts

| ID | Artefact | Accountable owner | Standard / source | Definition of done |
| --- | --- | --- | --- | --- |
| ART-051 | **Engineering Standards & Conventions** | D120 Code Review / Standards Owner | internal convention | Style, lint, review rules, commit format, and error-handling policy enforced in CI. |
| ART-052 | **Repository Structure & Branching Model** | D151 Application Security Manager | internal convention | Monorepo layout documented; branch protection on main; CODEOWNERS present. |
| ART-053 | **CI/CD Pipeline Specification** | D150 CI/CD Security Engineer | internal convention | Every stage: trigger, timeout, artefacts, gates, and who can bypass (nobody). |
| ART-057 | **Environment Matrix & Secrets Management** | D091 DevOps Engineer | internal convention | dev/staging/prod parity table; secret storage, rotation, and access recorded. |
| ART-060 | **Onboarding & Activation Funnel Spec** | D040 Product Analytics Lead | internal convention | Step-level funnel, drop-off hypotheses, and the experiment queue per step. |
| ART-061 | **Content & Localisation Style Guide** | D053 UX Writer / Content Designer | internal convention | Tone, reading level, en-GH conventions, which languages ship, and translation QA steps. |
| ART-063 | **Model Training & Evaluation Pack** | D133 ML / Model Test Engineer | internal convention | Dataset snapshot hash, training config, eval metrics, and acceptance thresholds. |
| ART-064 | **Prompt & Agent Library** | D089 Prompt Engineer | S16 | Each prompt: purpose, version, test cases, eval score, cost, and rollback copy. |
| ART-065 | **Integration & Webhook Catalogue** | D165 Business Continuity Manager | internal convention | Each external API: owner, auth, rate limits, retry policy, sandbox, and failure mode. |

## Assure — 13 artefacts

| ID | Artefact | Accountable owner | Standard / source | Definition of done |
| --- | --- | --- | --- | --- |
| ART-054 | **Test Strategy & Master Test Plan** | D173 Support Agent (Tier 1) | S17 | Risk-based; pyramid targets, coverage floors, environments, entry/exit criteria. |
| ART-055 | **Test Cases & Automation Matrix** | D141 SDET (Software Development Engineer in Test) | internal convention | Each REQ has >=1 positive and >=1 negative test; automation status tracked. |
| ART-056 | **Synthetic Data & Test Fixtures Policy** | D216 Synthetic Data & Fixtures Engineer | internal convention | No production PII in non-prod; generators documented; refresh cadence set. |
| ART-101 | **Quality Dashboard & Defect Trend Report** | D121 QA Lead / Test Manager | internal convention | Weekly; escape rate, defect age, severity mix, flake rate; reviewed in every go/no-go. |
| ART-102 | **Accessibility Conformance Report (WCAG 2.2 AA)** | D128 Accessibility Tester | S12, S29 | Sampled screens tested with TalkBack/VoiceOver; every failure has a ticket and an owner. |
| ART-103 | **UAT Sign-off Pack** | D142 UAT Coordinator | internal convention | Business scenarios executed by real users; accepted defects listed; named sign-off. |
| ART-104 | **Performance & Load Test Report** | D118 Performance Engineer | S31 | Modelled peak tested at 2x forecast; p95 against SLO; the first bottleneck named. |
| ART-105 | **Device & Network Compatibility Matrix** | D124 Mobile Test Engineer | internal convention | Top devices by market share for Ghana; 3G/4G/Wi-Fi paths; results per device and OS build. |
| ART-106 | **Beta / Field Test Report** | D135 Beta / Field Test Coordinator | S38, S39 | Cohort size stated; crash-free rate; top 10 findings triaged; release verdict with evidence. |
| ART-107 | **LLM Behavioural Test Suite & Golden Set** | D134 Prompt & LLM Evaluator | S16 | Golden set versioned; rubric; regression thresholds; judge calibrated on a human-labelled sample. |
| ART-108 | **Test Automation Health Report** | D139 Test Automation Architect | S44 | Flake rate, runtime, coverage of critical paths, and the cost per detected defect. |
| ART-109 | **Test Environment & Data Readiness Report** | D127 Test Environment Manager | internal convention | Env parity gaps, synthetic data freshness, and evidence that no production PII is present. |
| ART-110 | **Compliance Control Test Report** | D136 Compliance Test Analyst | S2, S30 | Each control tested with evidence; exceptions have remediation owners and dates. |

## Secure — 12 artefacts

| ID | Artefact | Accountable owner | Standard / source | Definition of done |
| --- | --- | --- | --- | --- |
| ART-048 | **Threat Model (STRIDE + LINDDUN)** | D187 Security Programme Manager | S14, S15 | Assets, actors, trust boundaries, threats, mitigations, residual risk accepted by owner. |
| ART-066 | **Security Architecture Review** | D096 Security Engineer | S14, S20 | Every trust boundary has a control; gaps have an owner and a dated remediation. |
| ART-067 | **ASVS Verification Report** | D177 Marketplace Operations Analyst | S20 | Requirements cited by versioned ID; pass/fail/not-applicable with evidence per item. |
| ART-068 | **MASVS Verification Report** | D179 Fraud Operations Specialist | S21 | Profile chosen (L1/L2/R/P); each control tested on device; evidence attached. |
| ART-069 | **Penetration Test Report & Remediation Log** | D182 Onboarding Specialist (Freelancer) | S22 | Findings rated CVSS; owner, deadline, retest evidence for every item. |
| ART-070 | **Compliance Register & Evidence Pack** | D201 Compliance Officer | S2, S5, S6 | Each obligation: status, evidence file, expiry date, accountable person. |
| ART-071 | **Privacy Notice, Consent & DSAR Runbook** | D202 Privacy Operations Analyst | S2 | Notice matches data inventory; consent captured with proof; DSAR SLA and script tested. |
| ART-072 | **Fraud & Abuse Playbook** | D195 Fraud Rules Engine Owner | internal convention | Scam patterns, signals, thresholds, actions, and false-positive handling documented. |
| ART-073 | **Incident Response Plan & Runbooks** | D192 Revenue Operations Analyst | S23 | Severity matrix, roles, comms templates, and a tabletop exercise record. |
| ART-075 | **Vulnerability Management Policy** | D190 Data Quality Engineer | S24 | Scan cadence, triage SLAs by severity, exception process with expiry. |
| ART-076 | **Supply Chain Security Pack (SBOM)** | D188 Third-Party Risk Analyst | internal convention | Dependency policy, licence check, SBOM per release, and provenance attestation. |
| ART-077 | **Vulnerability Disclosure Policy** | D191 BI / Reporting Developer | S25 | Public contact, safe-harbour text, triage SLA, and a recognition scheme. |

## Deploy — 14 artefacts

| ID | Artefact | Accountable owner | Standard / source | Definition of done |
| --- | --- | --- | --- | --- |
| ART-058 | **Release Notes & Changelog Standard** | D217 Launch Manager | internal convention | Every release has user-facing notes, migration steps, and rollback pointer. |
| ART-059 | **Mobile Store Readiness Checklist** | D135 Beta / Field Test Coordinator | S18, S19 | Privacy labels, data-safety form, permissions justification, review notes, screenshots. |
| ART-062 | **Support Playbook & Macros** | D235 Sales Operations Manager | internal convention | Top 20 intents, macros, escalation matrix, and first-response SLA. |
| ART-074 | **DR/BCP Plan & Restore Evidence** | D227 Disaster Recovery Engineer | internal convention | RTO/RPO per system; last successful restore test dated; gaps funded. |
| ART-078 | **Infrastructure as Code Specification** | D091 DevOps Engineer | internal convention | All prod resources declared in code; drift detection on; no console-only changes. |
| ART-079 | **Observability & Alerting Design** | D094 Observability Engineer | internal convention | Golden signals, trace propagation, log schema, and alert routing with runbook links. |
| ART-080 | **SLO/SLI & Error Budget Policy** | D094 Observability Engineer | internal convention | SLOs per user journey; error budget; the behaviour when budget is exhausted. |
| ART-081 | **Launch Readiness Checklist (Go/No-Go)** | D217 Launch Manager | S26 | Weighted gate list; named sign-offs; no launch with an open critical item. |
| ART-082 | **Release & Rollback Runbook** | D218 Rollout / Canary Manager | internal convention | Staged rollout %, kill-switch, data migration reversal, and comms steps. |
| ART-083 | **On-call, Escalation & Postmortem Kit** | D223 On-call & Incident Manager | S23 | Rota, escalation ladder, blameless template, and action-item follow-through. |
| ART-084 | **Trust & Safety Operations Manual** | D239 Community Moderator | internal convention | Queues, SLAs, decision guidelines, appeal path, and quality sampling. |
| ART-085 | **Data Retention & Deletion Schedule** | D203 Records & Retention Manager | S2, S27 | Per data class: retention period, legal basis, deletion mechanism, proof of deletion. |
| ART-086 | **Cost & Unit-Economics Dashboard** | D225 Cloud FinOps Analyst | internal convention | Infra + messaging + payment cost per active user and per matched job; alerting. |
| ART-087 | **Bot, Abuse & Rate-Limit Design** | D180 Dispute Resolution Officer | S28 | Per-endpoint limits, challenge strategy, blocklist ops, and appeals. |

## Sustain — 12 artefacts

| ID | Artefact | Accountable owner | Standard / source | Definition of done |
| --- | --- | --- | --- | --- |
| ART-088 | **Growth Experiment Backlog** | D249 Experimentation Platform Manager | internal convention | Each experiment: hypothesis, metric, sample size, duration, and decision rule. |
| ART-089 | **Marketplace Liquidity Playbook** | D240 Marketplace Supply Manager | internal convention | Supply/demand targets per city, match-fill rate dashboard, and intervention levers. |
| ART-090 | **Community & Events Playbook** | D255 HR Business Partner | internal convention | Calendar, budget, host kit, and the metric each event moves. |
| ART-091 | **Brand, Naming & Positioning Kit** | D282 Brand Strategist | internal convention | Shortlisted names screened for trademarks/domains; positioning statement; voice. |
| ART-092 | **Continuous Discovery Cadence** | D031 Product Manager | internal convention | Weekly customer touchpoint scheduled with notes; monthly insight digest. |
| ART-093 | **Quarterly OKR & Roadmap Review** | D042 Chief of Staff | internal convention | Objectives with measurable KRs; scoring recorded; next-quarter scope adjusted. |
| ART-094 | **Retrospective & Process Improvement Kit** | D044 Release Train Engineer | internal convention | Cadence, format, and a tracked improvement backlog with owners. |
| ART-095 | **Training & Enablement Curriculum** | D275 Internal Enablement Trainer | internal convention | Role-based paths, assessment, and refresh schedule for each internal role. |
| ART-096 | **Investor/Donor Reporting Pack** | D288 ESG / Social Impact Reporting Officer | internal convention | Monthly metrics, cohort retention, burn, and the ask; generated from dashboards. |
| ART-098 | **Assessment & Certification Design** | D277 Certification Board Chair | internal convention | Task bank, rubric, pass mark, proctoring rules, and appeal process. |
| ART-099 | **Impact Measurement Framework** | D272 Impact Measurement Lead | internal convention | Outcome definitions (jobs filled, income earned), attribution method, and data source. |
| ART-100 | **Master Index & Reading Order** | D031 Product Manager | internal convention | Generated; every document has an owner, a status, and a next review date. |

