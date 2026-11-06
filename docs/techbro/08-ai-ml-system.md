# 08 — AI/ML System Design

> AI has three jobs in this product: **reduce the cost of understanding** (parse messy briefs, CVs,
> messages), **improve the quality of matching**, and **make our own small team behave like a large
> one**. It has one job it must never be given: **deciding who gets paid.** That stays with a named
> human and an auditable rule.

---

## 8.1 AI use-case register

Each use case is scored on value, risk and evidence of need. "No" is a design decision, not a gap.

| ID | Use case | Type | Value | Risk | Ships in | Owner | Human-in-the-loop |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AI-01 | **Brief assistant**: turn a plain-language need into a structured job brief (outcome, deliverables, skills, budget range) | LLM | High: this is the wedge (scoping beats matching) | Medium | MVP | D268 | mandatory — user edits and submits |
| AI-02 | **Skill extraction** from briefs, CVs, portfolios into the taxonomy | LLM + rules | High | Medium | MVP | D085 | user confirms tags |
| AI-03 | **Proposal summariser** for clients (top 5 key points, red flags) | LLM | Medium | Low | v1 | D089 | client reads originals |
| AI-04 | **Semantic search** ("find someone who can rescue a failing Flutter app") | Embeddings | Medium | Low | v1 | D087 | results explainable |
| AI-05 | **Ranking** (learned) | ML | High | High | v2 | D084 | guardrails + slices |
| AI-06 | **Fraud signal assistant**: cluster and summarise anomalies for analysts | ML + LLM | High | High | v1 | D169 | analyst decides |
| AI-07 | **Dispute evidence digest**: chronological summary of both sides for the officer | LLM | High (speed) | **Very high** (bias) | v1 | D180 | officer reads raw evidence too |
| AI-08 | **Support assistant** drafting replies from the knowledge base | RAG | Medium | Medium | v1 | D173 | agent sends |
| AI-09 | **Interview/assessment question generation** per skill level | LLM | Medium | Medium | v1 | D277 | assessor approves bank |
| AI-10 | **Internal copilots** for code, tests, docs, analytics | LLM | High (leverage) | Medium | now | D119 | engineer owns every line |
| AI-11 | **Translation/localisation pre-pass** | LLM | Medium | Medium | v2 | D051 | native reviewer signs off |
| AI-12 | **Pricing guidance** for talent | ML | Medium | Medium | v2 | D265 | advisory only, never enforced |
| — | **Fully automated dispute decisions** | — | — | Unacceptable | never | — | **Rejected** |
| — | **Fully automated bans from a classifier** | — | — | High | never | — | Human review required |
| — | **CV ranking that hides candidates silently** | — | — | Unacceptable | never | — | Must be explainable and appealable |

**The rejection list is more important than the roadmap.** Two of the three rejections are about
*irreversible harm to a person's income*: an AI that wrongly denies work does damage that no
"model card" repairs.

## 8.2 AI-01 Brief assistant — the flagship use case

**Problem it solves.** Clients write "I need an app" and workers guess. Every ambiguity becomes a
dispute (ART-042). The assistant's job is to *provoke specificity*, not to write prose.

```
Input:  "need someone to build my food delivery app, budget small, urgent"
        │
        ▼  (1) extraction + (2) taxonomy grounding (retrieval over skill catalogue)
Output: {
  "outcome": "A working Android MVP where customers browse restaurants,
              place an order, and pay with MoMo",
  "deliverables": [
    {"item": "Customer app (Android)", "acceptance": "Installable APK; browse, cart, checkout"},
    {"item": "Vendor dashboard (web)", "acceptance": "Add/edit menu, see incoming orders"},
    {"item": "Backend + payments", "acceptance": "MoMo sandbox payment confirmed end-to-end"}
  ],
  "skills": ["flutter", "django", "postgresql", "paystack-integration"],
  "level": "L3-L4",
  "budget_range_ghs": [18000, 32000],
  "duration_weeks": 8,
  "assumptions": ["Scope excludes rider tracking", "Content provided by client"],
  "questions_to_confirm": ["Do you already have a merchant list?", "Is iOS needed at launch?"]
}
```

**Design constraints:**
1. **Never invent scope.** Unknown fields are `null` + a question, not a plausible guess.
2. **Budget ranges come from our own historical data** (median price for similar skill sets), not
   from the model's imagination. Until we have data, we say "no estimate yet".
3. **Every output is editable** before publish; the client is the author of the brief.
4. **Show the assumptions** as an explicit list the client can delete. Hidden assumptions become
   disputes.
5. **Cost ceiling** per brief (token budget) with a deterministic fallback to the manual form.

**Evaluation.** A 150-item golden set of real (anonymised) briefs; metrics: schema validity rate
(100% required), skill recall vs human labels (≥0.85), hallucinated deliverable rate (target 0;
measured by human review), user edit distance (lower = better draft), time-to-publish (product KPI).

## 8.3 AI-07 Dispute digest — the highest-risk use case

An LLM summarising two sides of a money argument is one prompt-injection away from deciding it.

| Control | Implementation |
| --- | --- |
| **Untrusted content isolation** | messages/documents are passed as *quoted data*, never as instructions; the system prompt states that content is evidence, not commands |
| **No recommendation** | the digest lists facts, dates, delivery evidence, and contradictions — it does not say who is right |
| **Symmetric length** | both sides' evidence summarised to comparable length (measured), to avoid framing bias |
| **Citations** | every sentence in the digest links to the message/artifact ID it came from |
| **Officer reads raw** | UI shows digest *next to* the raw evidence, with a required scroll-through for long evidence |
| **Audit** | digest version + prompt version + model version stored with the decision |
| **Fallback** | if the digest fails validation, the officer sees raw evidence only; nothing is delayed |

Evaluation: an adjudicated sample of 40 past disputes where the "correct" outcome is known; measure
whether officers exposed to digests reach different outcomes than officers without (bias delta),
plus time saved. If the bias delta is non-zero and material, the feature is removed — a speed win
is not worth a fairness loss.

## 8.4 RAG architecture (support + policy Q&A)

| Layer | Decision |
| --- | --- |
| Corpus | help centre, policies, past resolved tickets (anonymised) — **not** the dispute corpus |
| Chunking | 400–800 tokens, heading-aware, with source URL metadata |
| Embeddings | hosted model; re-embed on corpus change; index versioned (ART-271) |
| Retrieval | hybrid (BM25 + vector) with MMR for diversity; top-k 8 |
| Generation | answer must cite ≥1 retrieved chunk; otherwise return "I don't know" |
| Guardrail | if the question is about money owed, refunds, or account status → **route to human**, never generated |
| Evaluation | 120-question golden set; faithfulness ≥0.9, answer relevance ≥0.85, refusal correctness 100% on out-of-scope set |

**Grounding rule:** an answer without a citation is a liability, not an answer.

## 8.5 Model & prompt lifecycle

```
Idea → eval set defined → baseline (rules/human) → prototype → offline eval
   → shadow mode (no user impact) → 5% canary → 100%
   → monitor drift → re-eval → version bump or rollback
```

| Artefact | Content | Gate |
| --- | --- | --- |
| Model card (ART-050) | purpose, data lineage, eval results incl. slices, limitations, owner, review date | before any user exposure |
| Prompt record (ART-064) | prompt text, version, golden-set score, cost per call, rollback copy | on every change |
| Eval report (ART-107) | metrics, slice analysis, comparison to baseline | before canary |
| Cost log | tokens, latency, cost per task | monthly review |

**Versioning rule:** model version, prompt version, and eval-set version are stored with every
output that influences a user decision. Without this, "why did it say that?" is unanswerable.

## 8.6 Cost and latency budget

| Use case | Model class | Target latency | Cost ceiling | Degradation |
| --- | --- | --- | --- | --- |
| Brief assistant | mid-tier LLM | p95 < 6 s (streamed) | ≤ $0.02 per brief | manual form |
| Skill extraction | small model + rules | p95 < 1.5 s | ≤ $0.002 | user tags manually |
| Proposal summary | mid-tier | p95 < 4 s | ≤ $0.01 | show raw proposals |
| Support RAG | small/mid | p95 < 3 s | ≤ $0.008 | human queue |
| Dispute digest | mid-tier | p95 < 10 s (async) | ≤ $0.05 | officer reads raw |
| Ranking | small GBT / embedding ANN | p95 < 150 ms | < $0.0002 | v1 weighted score |

**Hard rule:** no AI feature may have a per-action cost that exceeds 2% of the platform fee on that
action. A brief assistant that costs more than the take rate on a small job is negative margin.

## 8.7 Data governance for AI

| Question | Answer |
| --- | --- |
| May we train on user data? | **No, not by default.** Opt-in only, written into the privacy notice, revocable (S2). |
| May we send user content to a model provider? | Only if the provider contractually excludes training on our data and offers a data-processing agreement; disclosed in the privacy notice (ART-071). |
| Are identity documents sent to LLMs? | **Never.** OCR/extraction for KYC happens in a dedicated pipeline; LLMs do not see ID images. |
| Is PII redacted before prompts? | Yes: phone, email, ID numbers, addresses redacted by a pre-processor with tests. |
| Retention of prompts/outputs? | 30 days for debugging, then purged; digests retained with the dispute record (7y, they are case evidence). |
| Cross-border transfer | Covered by the same ADR-006 transfer basis; model providers' regions are listed in ART-029. |

## 8.8 Evaluation discipline

| Metric family | What it catches | How measured |
| --- | --- | --- |
| **Task quality** | wrong extraction, bad brief | golden set, exact/semantic match |
| **Faithfulness** | hallucination in RAG | citation support rate (human or judge model, calibrated) |
| **Safety** | unsafe/biased output | red-team set (ART-145); refusal correctness |
| **Robustness** | brittleness to typos, mixed language (Twi/Pidgin/English), long inputs | adversarial set |
| **Slice fairness** | differential quality by group | per-slice metrics with confidence intervals |
| **Cost/latency** | economic viability | p50/p95 per task |
| **Regression** | prompt drift | golden set on every prompt change |

**LLM-as-judge rules** (ART-107): judge agreement with human labels must be measured on ≥100
samples; agreement <75% means the judge is not admissible for that metric; judge model differs
from the model under test; judge prompts are versioned.

## 8.9 AI-assisted engineering policy (the team's own leverage)

This is how a 6-person team ships like 20 without shipping 20 people's worth of bugs.

| Practice | Allowed | Not allowed |
| --- | --- | --- |
| Scaffolding, boilerplate, migrations | yes | — |
| Test generation | yes, then the human verifies the tests fail when the code is wrong | accepting tests that pass trivially |
| Code review pre-pass | yes | relying on it as the only review |
| Money path, auth, crypto | AI may draft; **two human reviewers required** | single-reviewer merge |
| Security-sensitive config | AI may suggest; human applies | auto-apply |
| Documentation | yes, from real specs | publishing unverified claims |
| Debugging | yes | "it works now" without a root cause |

**The 2026 failure mode is not bad code; it is plausible code nobody understood.** The review
question is not "does this compile?" but "can the author explain why this is correct, and what
happens when it is not?"

## 8.10 Monitoring and drift

| Signal | Alert threshold | Response |
| --- | --- | --- |
| Brief assistant schema-validity rate | <99% | roll back prompt; incident |
| Extraction confidence distribution shift | >2σ day-over-day | inspect sample, check taxonomy change |
| RAG refusal rate | >30% (was 12%) | corpus or retriever regression |
| Digest generation failures | >5% | fallback path verification |
| Ranking score distribution (v2) | drift > threshold | re-evaluate; consider rollback to v1 |
| Per-slice quality gap | >5 points | fairness review by D090 |
| Cost per active user | +25% month-over-month | budget review |

## 8.11 Rule for the roadmap

An AI feature advances to build only when **three** things exist: a written failure mode analysis,
a golden set to measure it, and a named human accountable when it is wrong. Otherwise it is a demo,
and demos do not survive contact with a disputing client.

## 8.12 AI governance roles (from the catalogue)

| Role | Responsibility here |
| --- | --- |
| D268 AI Product Manager | use-case register, acceptance thresholds |
| D269 AI Governance Lead | AI register, review gates, NIST AI RMF alignment (S16) |
| D090 Responsible AI Reviewer | slice metrics, harm analysis, sign-off |
| D134 Prompt & LLM Evaluator | golden sets, judge calibration, regression |
| D145 AI Red Teamer | jailbreak/injection testing, tool abuse |
| D296 Data Ethics Reviewer | data-use decisions, opt-in mechanics |
| D054 Data Protection Officer | lawful basis, transfer basis, retention |
