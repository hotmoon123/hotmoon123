# TechBro — Complete System Design & Brainstorming Pack

> A cross-platform mobile marketplace where tech talent in Ghana finds paid work, delegates work it
> cannot do, and gets paid safely. This pack is the full design: **300 SDLC roles**, **110
> deliverables**, **57 verified sources**, and an honest review of **two competing blueprints** and
> **six existing platforms**.

**Status:** design v1, generated 2026-11-06 · **Branch:** `arena/cf370f1a-hotmoon123`
**Working name:** *TechBro* (placeholder — see §3.10 for the naming risk)

---

## Read in this order

| # | Chapter | What it gives you | Read if you… |
| ---: | --- | --- | --- |
| **0** | **[21-executive-blueprint.md](21-executive-blueprint.md)** | The whole system in 12 pages | want the complete picture first |
| 1 | [01-role-catalog.md](01-role-catalog.md) | 300 roles × 19 families, with inputs, outputs, Bloom level, AI leverage, KPI | asked "who does what" |
| 2 | [02-sdlc-framework.md](02-sdlc-framework.md) | 8 cells, 7 gates, RACI, cadence, tailoring | asked "how is this run" |
| 3 | [03-product-definition.md](03-product-definition.md) | Problem, users, wedge, MVP scope, metrics, kill criteria | want to know *what* is being built |
| 4 | [04-system-architecture.md](04-system-architecture.md) | C4 diagrams, money model, matching, capacity, failures | are building it |
| 5 | [05-data-model.md](05-data-model.md) | DDL, ledger, invariants, reconciliation, retention | are writing the schema |
| 6 | [06-api-contract.md](06-api-contract.md) | Conventions, errors, the four critical endpoints, events | are writing the API |
| 7 | [07-matching-reputation.md](07-matching-reputation.md) | Taxonomy, matching v0→v3, reputation, disputes | are building trust |
| 8 | [08-ai-ml-system.md](08-ai-ml-system.md) | 12 AI use cases, 3 explicit rejections, evals, cost ceilings | want AI without the liability |
| 9 | [09-security-and-compliance.md](09-security-and-compliance.md) | Threat model, ASVS/MASVS, Act 843, Ghana register | need to not get fined or breached |
| 10 | [10-ux-ui-design-system.md](10-ux-ui-design-system.md) | 42 screens, 4 flows, tokens, WCAG 2.2 AA | are designing screens |
| 11 | [11-testing-verification.md](11-testing-verification.md) | Risk-based strategy, money invariants, quality gates | are deciding when it is safe to ship |
| 12 | [12-runbooks-and-operations.md](12-runbooks-and-operations.md) | Kill switches, 15 runbooks, launch plan, Go/No-Go | are on call or launching |
| 13 | [13-business-model-and-gtm.md](13-business-model-and-gtm.md) | Revenue, unit economics, channels, liquidity, funding | are doing the business case |
| 14 | [14-team-roadmap-metrics.md](14-team-roadmap-metrics.md) | Team shapes, 12-month roadmap, metric tree | are planning capacity |
| 15 | [15-build-reorder-buy.md](15-build-reorder-buy.md) | What to build vs buy vs redesign away | are tempted to build everything |
| 16 | [16-requirements-traceability.md](16-requirements-traceability.md) | REQ IDs → design → test → evidence | need auditable requirements |
| 17 | [17-governance-decisions-risks.md](17-governance-decisions-risks.md) | 14 ADRs, risk register, policies, audit | need decisions on record |
| **18** | **[18-questionnaire-and-next-steps.md](18-questionnaire-and-next-steps.md)** | **12 questions that change the design + your next 14 days** | **want to start now** |
| **19** | **[19-competitor-teardown.md](19-competitor-teardown.md)** | **Upwork, Fiverr, Toptal, Braintrust, Andela, GH regional — strengths, weaknesses, what to copy** | **asked for competitor reference** |
| **20** | **[20-review-of-pasted-blueprints.md](20-review-of-pasted-blueprints.md)** | **Honest critique of DevMesh & TechRelay: what is brilliant, what is wrong** | **pasted those two documents** |
| **23** | **[23-brainstorm-the-system-reconsidered.md](23-brainstorm-the-system-reconsidered.md)** | **The brainstorm: the app is an unblocking network, not a hiring marketplace — plus VAT 20%, the missing competitors, and the net-vs-gross maths** | **are deciding what the app actually is** |
| **22** | **[22-source-library-review.md](22-source-library-review.md)** | **What the 15 uploaded files actually are: 73% method, 0% market — what to adopt, what is wrong, what they cannot tell you** | **pasted the 15-file library** |
| 99 | [99-sources-and-assumptions.md](99-sources-and-assumptions.md) | 57 sources + 10 labelled assumptions | want to check any claim |
| — | [artifacts/00-artifact-index.md](artifacts/00-artifact-index.md) | 110 deliverables with owners and definitions of done | asked "what is the output of each role" |

---

## The six documents to read if you read nothing else

1. **§21 executive blueprint** — the system on one page per layer.
2. **§3.5 wedge + §3.12 kill criteria** — the strategy, and when to stop.
3. **§4.5 money model** — the only part that must be right the first time.
4. **§19.10–19.11 competitor reality** — what the market already does, and the fork it forces.
5. **§18.2 the 12 questions** — what only you can answer.
6. **§18.4 next 14 days** — what to do on Monday.

---

## What makes this pack different

| Ordinary design doc | This pack |
| --- | --- |
| "We will validate the market" | 12 interviews, 3 personas, 5 paid concierge jobs, kill criteria (§3.12) |
| "We will handle payments securely" | Double-entry ledger, 8 tested invariants, reconciliation SQL, 3 licensing postures (§4.5, §5.4) |
| "AI-powered matching" | Rule-based v0 first, learned ranking only after 2,000 engagements, fairness slices (§7.4) |
| "Roles and responsibilities" | 300 roles × inputs/outputs/Bloom/AI-leverage/KPI, mechanically validated (§1) |
| "Industry-leading security" | STRIDE per boundary, ASVS 5.0 L2, MASVS 2.1 L2+P, named SLAs (§9) |
| "Large market opportunity" | No invented TAM; explicit assumptions with tests (§13, §99) |
| Citations that cannot be checked | 57 registered sources; anything unverified is labelled |

---

## The honest core (in five sentences)

1. **The idea is sound but narrow**: the defensible position is "trusted enough to be safe, open
   enough to be fast, local enough to be paid in cedis by Friday" (§19.13).
2. **The money model is the hard part, not the app**: Ghana requires care around Act 987, and Stripe
   Connect is not available to a Ghanaian entity (§4.5, §19.6).
3. **Scoping beats matching**: most disputes are specification failures, and an AI brief assistant is
   the cheapest differentiator you can build (§3.11, §8.2).
4. **Charge clients, not workers**: Braintrust charging talent 0% makes a 10% worker fee
   indefensible (§19.5).
5. **Do not build the Kubernetes/Rust/Kafka architecture** in either pasted blueprint. Four people
   need one Postgres, one deployable, and a ledger that balances (§20.2).

---

## Repo artefacts (regenerable, not hand-written)

```
docs/techbro/            ← this pack (10,000+ lines)
tools/data/roles/*.yaml  ← 300 roles (source of truth)
tools/data/artifacts.yaml← 110 artefacts + definitions of done
tools/data/sources.yaml  ← 57 sources + verification status
tools/gen_blueprint.py   ← validates every cross-reference, then renders
```

```bash
python3 tools/gen_blueprint.py     # fails closed on: dangling refs, duplicate ids,
                                   # missing DoD, unowned artefacts, role/artefact drift
```

**The generator is the quality guarantee.** If a role claims an artefact it does not own, or an
artefact cites a source that does not exist, the build fails. The tables in chapters 1 and the
artifact index are generated — they cannot drift from the data.

---

## Honesty clause

No invented market statistics. No fabricated user quotes. No unverified legal claim stated as fact.
Where a number was needed and unavailable, it is an `H-###` assumption with a test and a review date.

Every regulatory citation was checked on **2026-11-06** and registered in §99 — but laws change, and
nothing here is legal advice. Take the payments, labour-classification and data-protection questions
to a qualified Ghanaian professional before you rely on them (§9.6, §18.4 day 3).
