# 07 — Matching, Trust & Reputation

> Three systems decide whether this marketplace is trusted: **who gets shown** (matching), **who is
> believed** (reputation), and **what happens when it goes wrong** (disputes). They are designed
> together because they feed each other — matching consumes reputation, disputes consume matching
> quality evidence, reputation consumes dispute outcomes.

---

## 7.1 Skills taxonomy (the foundation everything else stands on)

A marketplace matches on **skills**, so the skill model is a product asset, not a config file.

| Level | Name | Observable evidence | Interview proxy |
| --- | --- | --- | --- |
| L1 | Aware | Has read about it; cannot ship | — |
| L2 | Guided | Ships with step-by-step help | 1–2 years / bootcamp grad |
| L3 | Independent | Ships a defined feature; needs review | 2–4 years |
| L4 | Owns | Designs and ships systems; reviews others | 4–7 years |
| L5 | Authority | Sets standards; debugged the hard failures | 7+ years / public artefacts |

**Taxonomy rules:**
1. **Canonical slug + aliases** (`flutter`, `dart-ui`, `flutter-dev`) so search and matching share
   one vocabulary (ART-097, owner D048, curated by D285).
2. **Parent/child** for hierarchy (`mobile > cross_platform > flutter`) enabling fuzzy matching
   without a model.
3. **Adjacent skills** declared explicitly (`django ↔ drf ↔ postgresql`) — adjacency is a ranking
   signal for "can learn quickly", never a substitute for the required skill.
4. **Every skill level a worker claims is either self-declared or assessed**, and the UI always
   shows which (this is an honesty feature, and it protects the assessment product later).
5. **Taxonomy changes are versioned**; matches store the taxonomy version they used so a ranking
   decision can be explained after the fact.

## 7.2 Matching v0 — hard filters (MVP)

```sql
-- illustrative: eligible candidates for a job
SELECT tp.user_id
FROM talent_profile tp
JOIN talent_skill ts ON ts.user_id = tp.user_id
WHERE ts.skill_id = ANY(:required_skill_ids)
  AND ts.level >= :required_level          -- no "close enough" at L1/L2
  AND tp.availability <> 'unavailable'
  AND tp.is_verified
  AND (:city IS NULL OR tp.city = :city)
  AND (:budget_min IS NULL OR tp.hourly_min_ghs <= :budget_min)
GROUP BY tp.user_id
HAVING COUNT(DISTINCT ts.skill_id) = :required_skill_count;   -- all required skills present
```

Then order by a transparent score (§7.3). **Why filters first:** a brilliant ranking of people who
cannot do the job is worse than a plain list of people who can.

### Cold-start rules (until each side has history)

| Situation | Rule |
| --- | --- |
| New talent, zero reviews | "New" badge; up to 3 proposal boosts/week; excluded from top slots only for high-budget jobs |
| New client, zero hires | Escrow funding required before contact; shorter proposal cap |
| Thin skill supply | Widen city radius first, then adjacent skills (labelled clearly: "can ramp in Flutter") |
| No match at all | Show "what to change" suggestions (budget, deadline, skill) instead of an empty state |

## 7.3 Matching v1 — transparent weighted score

| Signal | Weight (start) | Measurement | Gaming risk | Countermeasure |
| --- | ---: | --- | --- | --- |
| Required-skill match depth | 0.30 | fraction of required skills at or above level | keyword stuffing | assessed levels weighted higher than self-declared |
| Reputation (Bayesian-smoothed) | 0.20 | (Σ ratings + C·m) / (n + C), C=5, m=4.2 | fake reviews | reviews only from funded engagements; ring detection (ART-286) |
| Completion & reliability | 0.15 | completed ÷ accepted, on-time % | cherry-picking easy jobs | expose "accepts then cancels" rate to clients |
| Response time | 0.10 | median minutes to first reply | bots online 24/7 | active-presence only counts human actions |
| Price fit | 0.10 | rate vs job budget range | lowball then upsell | scope is locked at acceptance; change requests are explicit |
| Recency & availability | 0.10 | last active, availability flag | notification spam | quiet hours |
| Repeat-client signal | 0.05 | same client hired before | collusion | cap contribution; detect mutual-only rings |

**Rules that make the score trustworthy:**
- Weights live in configuration with a version; every match stores `score_version`.
- The explanation string is generated from the top three contributing signals, in plain language.
- Weights are changed only with an offline evaluation (ART-063) and a documented rationale.
- **No paid placement in year one.** The moment ranking can be bought, the explanation becomes a lie.

## 7.4 Matching v2 — learned ranking (only after labels exist)

**Preconditions before a single gradient is computed:** ≥2,000 completed engagements, ≥6 months of
data, a stable taxonomy, and a fairness baseline.

| Element | Choice | Why |
| --- | --- | --- |
| Task | Learning to rank (pairwise) over (job, candidate) | relevance is relative, not absolute |
| Labels | hired=3, completed with rating≥4=2, proposal sent=1, shown-but-ignored=0 | outcome-weighted, not click-weighted |
| Features | skill depth, Bayes rating, completion, response, price fit, recency, cohort, assessment scores | keep the v1 signals so the model degrades gracefully to rules |
| Model | Gradient-boosted trees first (interpretable, small, fast) | a small model you can explain beats a large one you cannot |
| Guardrails | hard filters always applied pre-ranking | model cannot override eligibility |
| Evaluation | offline nDCG@10 on a time-based split + online A/B on match-fill rate | offline alone lies |
| Fairness slices | gender, city, new vs established, assessment vs self-declared | undisclosed bias kills supply |
| Monitoring | score distribution drift, slice-level fill-rate gaps, exposure concentration (Gini) | |
| Fallback | if model service fails → v1 weighted score | matching must never be down |

**Rejected by design:** ranking by predicted revenue from the job (inverts the incentive: the
best-paid jobs would crowd out good matches), and ranking by predicted *client* spend (punishes
small businesses, our wedge).

## 7.5 Reputation

### Inputs and weights

| Input | Weight | Window | Notes |
| --- | ---: | --- | --- |
| Client ratings of talent | 40% | last 24 months, exponential decay (half-life 9 months) | only from funded engagements |
| Completion rate | 20% | lifetime | completed ÷ accepted |
| On-time delivery | 15% | last 20 milestones | deadline vs accepted_at |
| Responsiveness | 10% | last 90 days | median first-response time |
| Dispute outcomes against them | 10% | lifetime | lost disputes reduce; won disputes neutral |
| Verification & assessments | 5% | current | verified ID, passed assessments |

**Displayed as:** a 5-point average (familiar) + a trust band (New / Established / Trusted / Elite)
+ the inputs that produced it. **Never** a single opaque number that users cannot interrogate.

### Anti-gaming controls (mandatory)

| Attack | Signal | Control |
| --- | --- | --- |
| Fake reviews / reciprocal rings | mutual-only review graph, clustered timing, device/IP overlap | graph analysis; exclude; flag (ART-286) |
| Review extortion ("5 stars or I dispute") | message content + dispute timing | policy + detection in chat; review removal path |
| Rating bombing after a dispute | burst of 1-star from one client | require funded engagement; rate-limit rating impact pending dispute |
| Identity recycling after suspension | device, phone reissue, ID similarity | device binding + ID hash checks |
| Account farms for referrals | graph + payout destination reuse | destination and device clustering |

### Decay and forgiveness

Scores decay so that a good worker who had one bad month is not punished forever, and an
old 5-star profile cannot coast. Both directions matter for a healthy supply side.

## 7.6 Disputes

**The three-layer ladder** — most disputes must never reach a human:

| Layer | Mechanism | Target | Cost |
| --- | --- | --- | --- |
| L0 | **Prevention**: structured brief + acceptance criteria + milestone split | 60% of potential disputes never occur | product |
| L1 | **Self-resolution**: in-app "request changes" with a checklist and 72h window | 30% | free |
| L2 | **Mediation**: ops officer reviews evidence against the acceptance criteria | 9% | low |
| L3 | **Adjudication**: panel decision with written rationale; one appeal | 1% | highest |

**Rules:**
1. A dispute **freezes the escrow** for that milestone; nothing auto-releases while it is open.
2. **Evidence is append-only**, timestamped, and visible to both parties (symmetry is fairness).
3. The decision is made **against the written acceptance criteria**, not against who is more
   articulate. If the criteria were vague, that is a *scope defect* — record it, because it is a
   product bug in the brief template.
4. **SLA:** first response 24h, decision 5 business days, appeal 5 business days.
5. **Written rationale is mandatory** (≥80 chars, schema-enforced) and is shown to both sides.
6. Outcomes feed reputation asymmetrically: a lost dispute hurts; a won dispute is neutral (so
   workers are not punished for being disputed at).
7. **Fraud exits the dispute flow** and goes to Trust & Safety with its own playbook (ART-072).

**Dispute economics** (tracked monthly): cost per case, hours per case, reversal rate, and the
percentage of cases traceable to a brief defect. If the last number is above 20%, fix the brief
template before hiring more dispute officers.

## 7.7 Trust & safety operating model

| Risk | Detection | Action | Owner |
| --- | --- | --- | --- |
| Fake job posts (phishing, advance-fee) | new account + off-platform link + urgency language | hold, manual review, ban on repeat | D178 |
| Off-platform payment solicitation | message classifier + user reports | warn, then restrict, then ban | D168 |
| Identity fraud | KYC mismatch, duplicate ID hash | block payout, manual review | D154 |
| Harassment | report + message evidence | warn/suspend with appeal | D167 |
| Rating manipulation | graph analysis | remove reviews, restore score | D286 |
| Money laundering patterns | structuring, rapid in-out, mismatched profiles | freeze, escalate to compliance | D201 |

Every action has: a **rule ID**, an **evidence reference**, an **appeal path**, and a **review
date**. Enforcement without appeal is how platforms become the villain in their own story.

## 7.8 Metrics for this system

| Metric | Definition | Target |
| --- | --- | --- |
| Match-fill rate | filled jobs ÷ posted jobs (7d) | ≥55% |
| Match precision @5 (sampled) | % of top-5 candidates a client would contact | ≥60% |
| Explanation usefulness | % of clients who open "why this match" | ≥30% |
| Proposal-to-hire rate | hires ÷ proposals | 10–20% |
| Time to first proposal | median hours | <24h |
| Dispute rate | disputes ÷ completed engagements | <5% |
| Dispute reversal rate on appeal | overturned ÷ appealed | <15% |
| Review authenticity | sampled reviews with verifiable engagement | 100% |
| Exposure Gini (talent) | inequality of impressions | flag >0.7 |

## 7.9 Failure modes of the trust system itself

| Failure | Mechanism | Early warning | Mitigation |
| --- | --- | --- | --- |
| **Rich-get-richer** | top-rated get all work; new talent never starts | rising exposure Gini; new-talent 90d retention falling | constrained exposure slots, rotation |
| **Rating inflation** | everyone is 4.8★; signal dies | distribution compression | dimension ratings, forced-choice comparisons |
| **Dispute avoidance** | workers refuse risky-but-fair jobs | declining proposal rate on complex jobs | insurance-like protection for well-documented scopes |
| **Over-moderation** | legitimate users banned by classifier | appeal overturn rate >15% | human review of classifier-driven bans |
| **Escrow theatre** | "protected" but practically unenforceable | refunds take >30 days | publish real resolution times |
