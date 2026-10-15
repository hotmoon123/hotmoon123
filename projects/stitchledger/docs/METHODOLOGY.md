# Delivery methodology, governance and business validation

## 1. Method

Use iterative, risk-driven delivery. Discover the problem, define testable requirements, model the critical flows, implement a small vertical slice, verify it and obtain feedback. Do not confuse shipping code with validating a business.

NIST SSDF describes secure practices that can be integrated into SDLC implementations; security is part of the lifecycle rather than a final decorative checklist. [1](https://csrc.nist.gov/projects/ssdf)

The uploaded Great Loop and design/engineering guides inform the working method: discover → execute → verify → persist; clear requirements; appropriate discipline perspectives; and explicit stopping conditions. Their sweeping guarantees and old “complete” labels are not accepted as evidence. We have not retroactively claimed to read every uploaded page.

## 2. Phases and role connections

| Phase | Relevant perspectives | Inputs → work → outputs | Gate / next handoff |
|---|---|---|---|
| Opportunity | Entrepreneur, researcher, analyst | Market context → compare alternatives → problem hypothesis | Decide whether to interview and prototype |
| Discovery | UX researcher, business analyst | Consented interviews/current workflow → synthesize problems → evidence and assumptions | Product owner accepts a specific problem |
| Product definition | Product manager, accountant, strategist | Evidence + constraints → scope/price/cost model → PRD and acceptance goals | Research and engineering agree on what “done” means |
| Requirements | Systems analyst, security engineer | Product goals → testable functions/constraints → SRS and traceability | Ambiguities and critical risks identified |
| Design | UX/UI, graphic designer, architect | Flows/data/rules → sketches/components/contracts → architecture and design decisions | Core happy/error paths understandable |
| Build | Mobile/backend/data engineers | Approved requirements → vertical implementation → source and migrations | Tests and review evidence |
| Verify | QA, security, accessibility reviewer | Builds + test plan → checks/defect reports → readiness assessment | Unresolved blockers prevent commercial release |
| Pilot | Operations, support, marketer | Consented users + safe build → onboarding/observation → retention and value evidence | Decide price test/pivot/stop |
| Release | Owner, legal/privacy adviser, DevOps | Approvals + funded operations → deployment/store build → monitored release | Human authorization, rollback and support in place |
| Operate | Maintainer, support, product/finance | Incidents/metrics → fixes/reconciliation/learning → updated backlog | Continue only when value justifies cost |

These are role responsibilities, not claims that separate credentialed specialists have performed all the work. The assistant can supply artifacts and analysis; the owner retains business/account/legal authority.

## 3. Thinking methods applied to this app

- **Design thinking:** observe how studios book/collect, define the real friction, explore alternatives, test a focused workflow.
- **Systems thinking:** a late order affects customer trust, owner workload, refunds, payment records and support—not just a red badge.
- **Architecture thinking:** isolate UI, contracts, domain rules, data access and external dependencies; choose simple deployment first.
- **Pattern thinking:** use explicit state machines, transaction boundaries, idempotency, optimistic concurrency and least privilege where the problem warrants them.
- **Algorithmic thinking:** define invariants and prove them with examples/tests; compute balances deterministically.
- **Research thinking:** distinguish observed behavior, participant claims, desk-research facts, assumptions and design preferences.
- **Economic thinking:** willingness to pay, acquisition effort, support cost, contribution margin, retention and opportunity cost matter more than download counts.
- **Ethical influence:** explain real benefits without false urgency, fabricated testimonials or guaranteed-income claims.

Unrelated electrical, neuroscience or hardware theory is not added simply because the user named those disciplines. Introduce it only when it changes a product decision.

## 4. Research and pricing experiment

### Assumptions to test

A1: recurring order/deposit confusion is material for the target studio.
A2: entering records on a phone is easier than the current method.
A3: connectivity is adequate for an online first release.
A4: an owner can independently use the workflow.
A5: a meaningful subset will actually pay an affordable recurring price.
A6: founder acquisition and support effort can be sustainable.

### Interview guide

1. Walk through the most recent order from booking to collection.
2. Where did you record the date, agreed price and payments?
3. Describe the last actual problem with one of those records.
4. What happened next? Was time/money lost, and how do you know?
5. What system do you use now? Why have you kept it?
6. Who enters records, on which phone, with what network access?
7. Show this fictional workflow. What is confusing or unnecessary?
8. After using a safe pilot, would you purchase at GHS 30/month? What would justify or prevent that decision?

Do not present compliments or survey intentions as sales. Obtain permission before recording notes; avoid collecting identifiable customer records during research. An initial convenience sample is not representative of Ghana's entire market.

### Suggested experiment

Interview 10 owners → observe five completing fictional tasks → fix critical usability problems → complete release/privacy gates → limited real-data pilot → explicit paid offer.

Proposed decision thresholds, not universal research laws: five interviewees provide recent concrete problem examples; four of five task participants complete booking/payment unassisted; three meaningful paid-pilot commitments. Actual payments and repeat use are stronger evidence. Failures trigger revised scope or stopping, not endless feature accumulation.

## 5. Business arithmetic

Initial price test: GHS 30/month/owner workspace. No ads, no sale of personal records, no lending or custody of funds.

Gross subscription revenue = paying workspaces × price. Contribution per workspace = price − payment fees − variable service/support costs. Break-even count = fixed costs / contribution, rounded up, when contribution is positive. Founder time, tax and customer acquisition must not be omitted.

Example only: 50 × 30 = GHS 1,500 gross per month. It is not a forecast, verified demand, take-home income or proof of profitability. Hosting/domain/store/provider fees must be quoted when providers are chosen. Billing and entitlements are not implemented.

## 6. Governance

- Every change identifies the user need, requirement, acceptance criterion, privacy effect and test.
- Critical bugs and financial integrity take precedence over visual novelty.
- No external spending, account creation, customer outreach or real-data migration without approval.
- No anonymous or uncontrolled messaging to customers.
- Do not run a background autonomous loop indefinitely. Stop at a missing approval, unsafe operation, failed acceptance condition, unresolved release blocker or exhausted agreed scope.
- Record architectural trade-offs and unmet requirements instead of claiming universal compliance.
- Review primary sources before using standards/version-specific guidance.
- Document assumptions that must be revisited when real evidence arrives.

## 7. Learning progression (Bloom L1–L6)

| Level | Task tied to this system |
|---|---|
| Remember | Identify frontend, API, domain logic, repository and database. |
| Understand | Explain why a deposit is not automatically profit, and why client-side checks are insufficient. |
| Apply | Create a fictional order and record an actual-scenario payment correctly. |
| Analyze | Trace a duplicate request and explain how the idempotency record prevents duplication. |
| Evaluate | Compare the workflow with paper/Oze/another real alternative against user-selected criteria. |
| Create | Design one validated improvement, write acceptance tests and implement it without breaking invariants. |

Begin with your explanation of the concept, correct misconceptions, then practice. Keep instruction within the app's active phase.

## 8. Next release priorities

1. Dedicated payment correction/reversal and post-collection policy.
2. Email verification/recovery, session management and stronger browser session design.
3. Dependency-audit triage and a supported native build pipeline.
4. Actual Android/iPhone tests, accessibility and network interruption tests.
5. Durable retry reconciliation; performance/pagination; operations monitoring.
6. Privacy/legal registration and retention decisions, encrypted backup schedule and restore rehearsal.
7. Real user validation and only then billing/store publication.

Order may change with evidence. No calendar or cost estimate is presented as certain without the missing resources and approvals.
