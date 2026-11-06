# 15 — Build, Reorder, Buy: Engineering Economics for a Small Team

> A 4-person team that builds its own chat, KYC, and payments will run out of money before it runs
> out of features. This chapter is the discipline that protects the only two finite resources:
> **engineering weeks** and **cash**.

---

## 15.1 The decision rule

**Build** only when the capability is *core to the differentiation* **and** no vendor can deliver
80% of it at under 20% of the cost. **Buy** when the capability is commodity, regulated, or
requires specialist operations. **Reorder** (change the product so the hard problem disappears)
when the capability is expensive and *not* load-bearing.

The question is never "can we build it?" — a small team can build anything badly. It is:
**"is this where our scarcity should be spent?"**

| Category | Posture | Test |
| --- | --- | --- |
| Trust & reputation logic | **Build** | It is the moat; nobody else's model fits our disputes data |
| Brief/scoping assistant | **Build** (on top of a hosted model) | It is the wedge; the prompts and eval set are the asset |
| Matching v0/v1 | **Build** (simple) | Needs to be explainable and tied to our taxonomy |
| Money ledger & reconciliation | **Build** | Non-negotiable; vendor ledgers do not model our escrow states |
| Payment rails & settlement | **Buy** | Regulated; PSP has licences and bank relationships |
| Escrow custody (as we scale) | **Buy** (licensed partner) | Regulated; cannot self-license early (S5) |
| KYC/identity verification | **Buy** | Specialist vendor; data-heavy; liability shifts |
| SMS/OTP/WhatsApp delivery | **Buy** | Commodity with route quality differences |
| Push notifications | **Buy** | Commodity |
| Email | **Buy** | Commodity |
| Chat/messaging UI | **Build thin** on a real-time transport | Differentiation is in-system; but do not build a messaging infrastructure |
| Video calls | **Buy** / link out | Not core |
| Analytics pipeline | **Buy** (managed) early, **build** the metrics layer | Definitions are ours; ingestion is commodity |
| Error tracking | **Buy** | Commodity |
| Search index | **Buy** (managed) | Commodity at our scale |
| Object storage/CDN | **Buy** | Commodity |
| Admin console | **Build** (server-rendered) | Ops workflows are specific; this is where money is protected |
| Feature flags | **Buy** or open-source self-host | Commodity, but essential |
| Auth | **Build thin** (OTP) with vendor SMS | Phone-first flows are specific to the market |
| Design system | **Build thin** | 32 components; a heavy library would fight the design |
| Dispute arbitration tooling | **Build** | Core trust workflow |

## 15.2 Build-vs-buy scorecard

Score each candidate on five axes (1–5), then read the totals as advice, not arithmetic:

| Axis | Question | Weight |
| --- | --- | ---: |
| Differentiation | Does it create an advantage a customer can feel? | ×3 |
| Cost to build | Engineer-weeks to a *maintainable* v1 | ×2 |
| Cost to run | Ongoing ops burden + on-call surface | ×2 |
| Risk transfer | Does buying shift liability/regulation off us? | ×2 |
| Lock-in | How painful is switching in 24 months? | ×1 |

Built examples from §15.1: brief assistant (diff 5, build 6 weeks, run low, risk low, lock-in medium)
scores high. KYC (diff 1, build 20+ weeks, run high, risk high, lock-in medium) scores low. That is
the whole method.

## 15.3 Vendors shortlisted (verify before committing)

No vendor is selected in this document; selection requires a spike and commercial terms.

| Need | Candidates (Ghana/Africa + global) | Evaluation criteria | Decision owner |
| --- | --- | --- | --- |
| Payments/splits | Paystack, Flutterwave, Hubtel; banks with PSP services | settlement speed, split/delayed settlement support, refund mechanics, pricing, support SLA, compliance posture | D018 + D100 |
| Payouts | same as above + direct MoMo/bank | coverage of MTN/Telecel/AT, failure rates, fees, reconciliation files | D193 |
| KYC | local identity vendors, regional providers | Ghana Card support, liveness quality, false-reject rate, data-processing terms, latency, price | D154 |
| SMS/OTP | local aggregators, global providers with GH routes | delivery rate by network, latency, price, sender ID registration | D166 |
| Push | Expo push, OneSignal, FCM direct | reliability, cost, SDK weight | D098 |
| LLM | multiple providers | quality on our golden set, cost, data-retention terms, regional availability | D268 |
| Hosting | regional/managed clouds | data residency, latency from Accra, cost, managed Postgres | D228 |
| Observability | Sentry + metrics/tracing stack | cost at our volume, PII scrubbing | D094 |
| Analytics | managed warehouse + product analytics | event volume cost, export freedom | D040 |

**Vendor rules:**
1. Never a single vendor for anything that can take the platform down (two SMS routes; two LLM providers).
2. Every vendor has a **data-processing agreement** before personal data flows (S2).
3. Every vendor has an **exit plan** written at selection time (how we leave, in what order).
4. Contract terms on **price changes, SLA credits, and data export** are read before signature, by
   someone who is not the person who wants the vendor.

## 15.4 The five-year cost of a shortcut

| Shortcut | Looks like | Real cost |
| --- | --- | --- |
| Custom chat infrastructure | "We'll just use sockets" | 6–10 engineer-weeks, then reliability bugs forever; buy transport, build the UX |
| Own SMS gateway contracts | "Cheaper per message" | Ops + compliance + route quality; only worth it above ~1M messages/month |
| Self-built KYC | "We can OCR the Ghana Card ourselves" | Accuracy, fraud, and legal liability; vendors specialise for a reason |
| Vendor escrow described as escrow | "It's basically an escrow" | Regulatory misrepresentation; terms must describe the actual mechanism |
| Hand-rolled auth | "OTP is simple" | Rate limiting, replay, device binding, SIM-swap defences — each is a bug class |
| No metrics layer | "Just query production" | Decisions made on inconsistent numbers; a metrics dispute every quarter |

## 15.5 Reorder examples (the cheapest engineering)

| Problem | Build/buy answer | **Reorder** answer |
| --- | --- | --- |
| Complex real-time collaboration on deliverables | expensive | milestone-based deliverables with async review |
| Multi-currency at launch | expensive, regulated | GHS only; add later with a treasury partner |
| Instant payouts | expensive (liquidity + risk) | next-business-day settlement, clearly stated |
| Video interviews | infrastructure + cost | structured written assessments + a call link |
| Time tracking | product complexity | outcome-based milestones (also better for workers) |
| Global supply | moderation + payments complexity | verified local supply, one city at a time |

**Reorder is not a compromise; it is design maturity.** Most "requirements" are inherited assumptions
nobody examined.

## 15.6 Engineering capacity model (reality check)

| Activity | Share of a 4-person team's week |
| --- | ---: |
| Feature work | 45% |
| Bug fixing & support engineering | 20% |
| Reliability, security, upgrades | 15% |
| Reviews, planning, coordination | 12% |
| Interrupts (incidents, vendor issues) | 8% |

**Implication:** a 4-person team has roughly **7 engineer-days of feature work per week**, not 20.
Any roadmap that assumes otherwise is a roadmap that will be "late" for reasons that were knowable
on day one. Plan in *capacity*, not in *wishes*.

## 15.7 What we deliberately keep boring

Boring is a feature. Every exotic choice is a future 2 a.m. page.

| Area | Choice | Why boring wins |
| --- | --- | --- |
| API style | REST + JSON, OpenAPI | universal tooling, easy debugging, cacheable |
| Auth | JWT access/refresh with rotation | well-understood failure modes |
| Background jobs | Celery + Redis | mature, documented, hireable skills |
| Database | single PostgreSQL primary + read replica | transactions, one source of truth |
| Deploy | containers on a managed platform | no bespoke orchestration |
| Frontend state | server-state library + small UI store | avoids the global-store trap |
| Feature flags | managed service | instant kill switches |
| Money | integer minor units, double-entry | correctness by construction |

## 15.8 The one thing worth building expensively

**The trust layer** — brief structuring, verification, escrow states, dispute workflow, reputation.
It is the only part a competitor cannot copy by signing the same vendors. Everything else should be
as boring and as bought as possible, so that the team's scarce attention lands here.
