# 18 — The Brainstorming Instrument & Next 14 Days

> This pack is a **default design**, opinionated where it must be and explicitly unsure where it
> should be. This chapter is how you and I turn the default into *your* design: answer the questions
> below, and only the sections whose answers change get rewritten. Unknown answers stay as `H-###`
> assumptions with tests — that is not a gap in the document, that is honesty.

---

## 18.1 How to use this chapter

1. Answer §18.2 (12 questions, 10 minutes). Rough answers are fine; "not sure" is a valid answer and
   becomes an assumption.
2. Anything you mark **A / B** (mutually exclusive choices) changes specific chapters — the map is in §18.3.
3. §18.4 is your next 14 days, ordered by risk, not by comfort.
4. §18.5 lists what I will produce next, once the answers exist.

---

## 18.2 The 12 questions

| # | Question | Why it changes the design | Options |
| ---: | --- | --- | --- |
| Q1 | **Who is the first customer you can personally reach 50 of?** | Determines the wedge (J1 freelancer-overflow vs J2 SME demand vs J3 junior talent) | A) Freelancers/seniors with overflow work · B) SMEs/founders needing work done · C) Juniors seeking first paid work · D) Agencies needing subcontractors |
| Q2 | **Are you building this to make a profit, or as an impact/social project first?** | Changes funding plan (grants vs angels), pricing sensitivity, and impact metrics | A) Venture-backable business · B) Profitable small business · C) Impact-first with revenue · D) Not sure yet |
| Q3 | **How do you want to be paid?** | Determines whether escrow is even necessary at launch | A) % take rate on each job · B) Client subscription · C) Talent subscription · D) Free now, monetise later |
| Q4 | **Will money move through the app at launch?** | The single biggest legal/engineering fork (licensing posture, ledger, disputes) | A) Yes, full escrow at launch · B) Milestone payments but no hold · C) No payments at launch, introductions only · D) Not sure |
| Q5 | **Who verifies a worker's skill?** | Determines v1 cost and trust model | A) Self-declared only · B) ID verified + self-declared skills · C) ID + paid practical assessment · D) Peer endorsements |
| Q6 | **What is your launch geography?** | Affects supply density, language, payments, and city-by-city rollout | A) Accra only · B) Accra + Kumasi · C) All Ghana · D) Ghana + diaspora clients |
| Q7 | **Which skills first?** | Depth beats breadth for liquidity; the taxonomy and matching are built around this | A) Software dev (web/mobile) · B) Data/AI · C) Design/product · D) Security/cloud · E) Broad tech |
| Q8 | **How technical is the founding team?** | Changes build-vs-buy and the staffing plan | A) Strong engineers building it ourselves · B) One technical founder + contractors · C) No technical founder, hiring · D) Using no-code first |
| Q9 | **What is your budget and runway for the next 6 months?** | Sets scope realism: the MVP list is cuttable in a known order | A) < GHS 50k · B) GHS 50–200k · C) GHS 200k–1M · D) > GHS 1M / funded |
| Q10 | **Do you already have a community or audience?** | Changes GTM from cold-start to activation | A) Yes, a large tech community · B) Small but engaged · C) None yet · D) An employer network instead |
| Q11 | **What is the one thing that would make you shut this down in 6 months?** | Defines kill criteria and prevents sunken-cost drift | free text |
| Q12 | **What does success look like in 12 months, in numbers?** | Anchors the North Star and roadmap | free text |

### Defaults used in this pack (stated so they can be argued with)

| Question | Default taken | Consequence if you choose differently |
| --- | --- | --- |
| Q1 | **A + a slice of B** (freelancer overflow + SMEs) | A C-first answer makes assessments and mentorship, not escrow, the launch feature |
| Q2 | A (venture-backable, but cash-disciplined) | C pivots the funding plan to grants and the metrics to jobs created |
| Q3 | A (8–12% take rate) | B/C need billing infra before escrow; D defers all payment complexity |
| Q4 | A (escrow-style at launch, provider posture) | C removes ~40% of the MVP and most of the legal risk — a legitimate first version |
| Q5 | B (ID verified + self-declared, assessed later) | C adds 6–10 weeks and assessor operations; A caps trust and invites fraud |
| Q6 | A (Accra only) | Broader geography needs supply seeding per city — usually a fatal dilution at MVP |
| Q7 | A (software dev) | B/C/D change the skill taxonomy seed and the assessor bench, not the architecture |
| Q8 | A (technical founders) | C changes the build plan toward a smaller v0 and a senior hire |
| Q9 | B (GHS 50–200k) | A forces a 6–8 week scope (§18.4 already reflects this) |
| Q10 | B (small but engaged) | C makes community-building the first workstream, before product |
| Q11 | not invented | written by you; it goes into ART-009 |
| Q12 | not invented | written by you; it feeds the KPI tree (ART-010) |

---

## 18.3 Answer → chapter impact map

| If your answer is… | Then these change | How |
| --- | --- | --- |
| Q4 = C (no payments at launch) | 04 §4.5, 05 §5.4, 07 §7.6, 09 §9.6, 13 §13.1–13.3 | Remove escrow/ledger from MVP; keep identity, matching, chat, reputation; add a "payment arranged off-platform" disclaimer and an anti-fraud playbook; revenue becomes introductions/subscriptions |
| Q3 = B or C (subscription) | 04 §4.5, 06 §6.3, 13 §13.1 | Add billing, dunning, plan limits; escrow becomes optional add-on |
| Q5 = C (assessments) | 03 §3.6 v1→MVP, 07 §7.1, 08 §8.1 (AI-09), 14 §14.5 | Add assessment product, assessor capacity plan, question bank, proctoring |
| Q1 = C (juniors) | 03 §3.5, 07 §7.2 cold start, 13 §13.4 | Add mentorship, squads-first supply model, employer partnerships for first jobs |
| Q2 = C (impact-first) | 12 §12.9 (add funder gates), 13 §13.9, 17 §17.8 | Impact metrics become primary; grants plan expands; commercial metrics stay as guardrails |
| Q6 = B/C | 03 §3.5, 13 §13.5, 04 §4.12 | Per-city supply seeding plan, multi-city ops, capacity recalc |
| Q8 = C (non-technical founder) | 14 §14.1–14.4, 15 §15.1 | Smaller v0, buy more, hire senior engineer first, longer timeline |
| Q10 = C (no community) | 13 §13.4, 14 §14.5 | Community workstream before paid acquisition; events and content earlier |

---

## 18.4 Your next 14 days (risk-ordered, not comfort-ordered)

| Day | Action | Output | Why this order |
| --- | --- | --- | --- |
| 1–2 | Write ART-001 (one page) and ART-009 kill criteria | signed one-pager | Without a refusal list, the project drifts into a job board |
| 2–4 | 6 customer conversations: 3 freelancers with overflow, 3 SMEs needing work | raw notes, 3 quotes each | Tests the wedge before any code |
| 3 | Send the letter to counsel on the payments question (ART-041/§9.6) | appointment booked | Long lead time; start it now |
| 5 | Price test: ask 5 people "would you pay 10% for escrow + dispute protection?" and record the answer verbatim | evidence log entries | Tests H-001 cheaply |
| 6–7 | Build the **brief template** on paper/Notion; run 3 real briefs through it manually | brief v1 + observed friction | The scoping product is the wedge; it needs no app |
| 8–10 | Concierge match: hand-match 3 real jobs using WhatsApp + the template; take a fee | first revenue (even GHS 100) | Proves willingness to pay and reveals the dispute patterns |
| 9 | File DPC registration (or start the application) | application receipt | Legal gate with a long clock (S2) |
| 11 | Choose the payment provider posture with counsel's input; open sandbox accounts | written posture note | Determines whether MVP needs a ledger in week 6 |
| 12–13 | Draft the 12 MVP screens (paper or Figma) and test with 3 users | screen inventory v1 (ART-046) | Cheap design before expensive code |
| 14 | Decide: proceed to build, or re-test the wedge | written decision + next 30 days | The forced honest checkpoint |

**Success bar for day 14:** at least **2 paid jobs completed through your manual process** and
**1 written legal position** on payments. If not, the honest move is more discovery, not more code.

---

## 18.5 What I can produce next (pick any, in this chat)

| Deliverable | Format | Depends on |
| --- | --- | --- |
| Repo scaffold (Django apps, models from §5.3, OpenAPI from §6.3, CI pipeline) | code in this repo | Q4, Q8 |
| Working escrow ledger module with property tests | code + tests | Q4 = A/B |
| Figma-ready screen specs for the 42 screens | markdown tables + component list | Q1, Q7 |
| React Native app skeleton (Expo Router, 12 screens, design tokens) | code | Q7 |
| Financial model spreadsheet (unit economics + 12-month plan) | CSV/XLSX | Q3, Q9 |
| Investor/grant one-pager and pitch outline | markdown | Q2, Q9 |
| Legal review pack (questions for counsel, T&Cs outline) | markdown | Q4 |
| User interview script + evidence template | markdown | Q1 |
| Skill taxonomy seed (200 skills, levels, aliases) | CSV | Q7 |
| Assessment task bank (20 practical tasks with rubrics) | markdown | Q5 = C |

---

## 18.6 Honesty clause

This pack deliberately contains **no invented market statistics, no fabricated user quotes, and no
unverified legal claims stated as fact.** Where a number was needed and not available, it is labelled
an assumption with a test (`99-sources-and-assumptions.md`). Where a regulation was cited, it was
verified on 2026-11-06 and the citation is in the source register — but regulations change, and
anything legal or financial in here must be confirmed with a qualified Ghanaian professional before
you rely on it.

The document's usefulness is not that it is complete; it is that **every claim in it can be checked,
and every gap in it is named.**
