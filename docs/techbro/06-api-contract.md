# 06 — API Contract

> Contract-first (OpenAPI 3.1 — S10). The mobile app generates its client from this spec; the
> backend generates its schema and tests from it. **The spec is the source of truth; the code
> follows it**, because a contract derived from code documents the bugs.

---

## 6.1 Conventions

| Topic | Rule | Rationale |
| --- | --- | --- |
| Base path | `/api/v1` | Breaking changes → `/api/v2`, never mutate v1 silently |
| Auth | `Authorization: Bearer <JWT>` for mobile; separate audience/token for admin | A stolen mobile token must never reach admin endpoints |
| Token lifetime | Access 15 min, refresh 30 days (rotating, reuse-detected) | Balance of UX on 3G vs blast radius |
| Idempotency | `Idempotency-Key` header **required** on all POST that touches money | Retries on bad networks are normal, not exceptional |
| Pagination | Cursor-based: `?cursor=&limit=` (default 20, max 100) | Stable under insertion; offset pagination duplicates rows |
| Errors | RFC 9457 `application/problem+json` | One error shape for every client |
| Time | ISO 8601 UTC (`2026-11-06T10:00:00Z`); localise client-side | |
| Money | **Integer minor units** + `currency` object: `{"amount": 150000, "currency":"GHS"}` | No floats over the wire |
| Versioning | Additive fields are non-breaking; removing/renaming is a new version | |
| Rate limits | Per identity + per IP; `429` with `Retry-After` | Bots cost real money (SMS, KYC) |
| Tracing | `X-Request-Id` echoed; propagated to logs and traces | Support becomes possible |
| Language | English (`en-GH`) in v1; `Accept-Language` respected once i18n lands | |

## 6.2 Standard error model

```json
{
  "type": "https://api.techbro.example/problems/insufficient-funds",
  "title": "Escrow funding failed",
  "status": 402,
  "detail": "The client's payment was declined by the provider.",
  "instance": "/api/v1/milestones/6f1c.../fund",
  "code": "PAYMENT_DECLINED",
  "request_id": "req_01J...",
  "errors": [{"field": "amount", "reason": "exceeds_job_budget"}]
}
```

**Error codes are a contract too.** Clients branch on `code`, not on prose. Every code is listed in
the generated reference and covered by a test (ART-055).

| HTTP | When | Client behaviour |
| ---: | --- | --- |
| 400 | validation | show field errors; never lose the form |
| 401 | missing/expired token | refresh once, then re-auth |
| 403 | authenticated but not allowed | explain; do not retry |
| 404 | absent **or** not visible to this user | deliberately indistinguishable (anti-enumeration) |
| 409 | state conflict (e.g. milestone already accepted) | refetch state, reconcile |
| 422 | business rule violation | show rule in user language |
| 429 | rate limited | back off per `Retry-After`, never hammer |
| 5xx | server | retry with exponential backoff + jitter, max 3, then queue |

## 6.3 Resource map

| Group | Endpoints | Notes |
| --- | --- | --- |
| Auth | `POST /auth/otp/request`, `POST /auth/otp/verify`, `POST /auth/refresh`, `POST /auth/logout`, `POST /auth/devices` | phone-first; no passwords in v1 |
| Profile | `GET/PATCH /me`, `GET/PUT /me/skills`, `POST /me/portfolio`, `GET /talent/{id}` | public view is a separate, redacted schema |
| Verification | `POST /verification/ghana-card`, `POST /verification/liveness`, `GET /verification/status` | uploads via signed URLs, never through the API |
| Jobs | `GET /jobs`, `POST /jobs`, `GET /jobs/{id}`, `PATCH /jobs/{id}`, `POST /jobs/{id}/publish`, `POST /jobs/{id}/pause` | brief validation is server-side |
| Matching | `GET /jobs/{id}/matches`, `GET /talent/search` | every item carries `match_reasons[]` |
| Proposals | `POST /jobs/{id}/proposals`, `GET /proposals`, `POST /proposals/{id}/accept`, `POST /proposals/{id}/withdraw` | accept creates engagement + milestone drafts |
| Contracts | `GET /engagements/{id}`, `POST /engagements/{id}/milestones`, `POST /milestones/{id}/fund`, `POST /milestones/{id}/submit`, `POST /milestones/{id}/accept`, `POST /milestones/{id}/request-changes` | accept/release is the money path |
| Wallet | `GET /wallet`, `GET /wallet/transactions`, `POST /payouts`, `GET /payouts/{id}` | balances derived from ledger |
| Disputes | `POST /milestones/{id}/disputes`, `POST /disputes/{id}/evidence`, `GET /disputes/{id}`, `POST /disputes/{id}/appeal` | evidence is append-only |
| Chat | `GET /conversations`, `GET /conversations/{id}/messages`, `POST /conversations/{id}/messages` (WS for live) | REST history + WebSocket live |
| Reviews | `POST /engagements/{id}/reviews`, `GET /talent/{id}/reviews` | one per side, 14-day editable window |
| Notifications | `GET /notifications`, `POST /notifications/read`, `POST /devices/push-token` | |
| Safety | `POST /reports`, `POST /users/{id}/block` | one-screen reporting flow |
| Admin (separate audience) | `/admin/v1/*` — verification queue, disputes, ledger, payouts, users, feature flags | MFA + IP allowlist + full audit |

## 6.4 The four endpoints that must never be wrong

### 6.4.1 Fund a milestone

```http
POST /api/v1/milestones/{id}/fund
Idempotency-Key: fund_ms_6f1c_20261106T1000
Content-Type: application/json

{ "provider": "paystack", "channel": "momo_mtn", "amount": {"amount": 150000, "currency": "GHS"} }
```

```http
202 Accepted
{ "payment_intent_id": "pi_...", "authorization_url": "https://checkout...", "expires_at": "..." }
```

Rules: only the client of the engagement may fund; amount must equal the milestone; the milestone
must be `unfunded`; the platform **never** marks a milestone funded from a redirect — only from a
**signature-verified webhook** (see §6.6).

### 6.4.2 Accept a milestone (release funds)

```http
POST /api/v1/milestones/{id}/accept
Idempotency-Key: accept_ms_6f1c_v3

{ "rating": 5, "note": "Delivered early with tests." }
```

Effects, in one transaction: milestone → `accepted`; ledger release entry (escrow → talent wallet,
minus platform fee + provider fee); outbox event `MilestoneAccepted`; reputation recompute queued;
notification to talent. Response includes `payout_eta` (next settlement cycle, not "instant").

### 6.4.3 Request payout

```http
POST /api/v1/payouts
Idempotency-Key: payout_u_8a2e_20261106T1030

{ "amount": {"amount": 80000, "currency": "GHS"}, "rail": "momo_mtn", "destination_id": "dst_..." }
```

Rules: KYC approved; amount ≤ wallet balance (row lock); one payout in flight per user per rail;
destination belongs to the user; the request never says "paid", only `queued` → `processing` →
`paid` (webhook-confirmed) or `failed` with a code.

### 6.4.4 Open a dispute

```http
POST /api/v1/milestones/{id}/disputes
{ "category": "quality", "claim": "...", "amount": {"amount": 150000, "currency": "GHS"} }
```

Rules: only on `submitted` or `accepted` (within a 72h cooling window); freezes the escrow release;
sets an SLA deadline; notifies both parties with the evidence checklist and the deadline.

## 6.5 Webhook contracts (inbound, from providers)

| Provider event | Verification | Effect | Idempotency |
| --- | --- | --- | --- |
| `charge.success` | HMAC signature + event id | milestone → `funded`; escrow_hold created; ledger txn | event id unique index |
| `transfer.success` | signature + reference | payout → `paid`; ledger settle | provider reference unique |
| `transfer.failed` | signature + reference | payout → `failed`; wallet re-credited via compensating entry | provider reference |
| `charge.dispute.created` | signature | payout hold; alert finance | event id |
| `refund.processed` | signature | refund ledger entry; escrow → `refunded` | event id |

**Webhook handling rules (all four are mandatory):**
1. **Verify signature before parsing the body**; reject unsigned.
2. **Persist the raw event** to a `provider_event` table, unique on `provider_event_id`.
3. **Process asynchronously** from the persisted event (the HTTP response must be fast).
4. **Never trust the amount in the webhook alone** — cross-check against the intent we created.

## 6.6 Outbound webhooks (v2, for agencies)

Signed with HMAC-SHA256 over `timestamp + body`; retried 8 times with exponential backoff over 24h;
delivery log visible to the customer; replay endpoint for missed events; per-consumer secret rotation.

## 6.7 Real-time channel (chat)

- Transport: WebSocket (Django Channels), authenticated by short-lived ticket (not the access token).
- Message send is REST (durable, idempotent) and the socket only **broadcasts** — this avoids
  "message lost because the socket dropped mid-send".
- Ordering: server-assigned monotonic `seq` per conversation; clients reconcile by `seq`.
- Presence is best-effort and never used for money or dispute decisions.

## 6.8 Authorization model

Three layers, all enforced server-side:

1. **Scope**: token carries scopes (`talent`, `client`, `admin:*`); endpoints declare required scope.
2. **Ownership**: object-level checks (BOLA prevention — S34). Every query is scoped to the caller's
   identity; there is no "get by id" without a tenancy predicate.
3. **Policy**: business rules (e.g. only the client may accept; only talent may submit) expressed as
   explicit policy functions with unit tests, not scattered `if`s.

The permission matrix (ART-021) is the source; the test suite (ART-146) enumerates every
role × endpoint pair and asserts deny-by-default.

## 6.9 Performance targets (contractual, tested in ART-104)

| Endpoint class | p95 target | p99 | Notes |
| --- | --- | --- | --- |
| Auth / OTP verify | 300 ms | 800 ms | excludes SMS delivery time |
| Feed & search | 400 ms | 900 ms | cached facets |
| Job detail / contract view | 250 ms | 600 ms | |
| Money mutations | 500 ms | 1200 ms | excludes provider latency (async) |
| Chat history (50 msgs) | 200 ms | 500 ms | |
| Admin queues | 800 ms | 2 s | internal |

## 6.10 Backward-compatibility policy

- **Additive only** within v1: new optional fields, new endpoints, new enum values (clients must
  tolerate unknown enum values — documented in the client guide).
- **Deprecation**: announce in changelog, emit `Deprecation` + `Sunset` headers, minimum 90 days,
  and monitor usage by client version before removal.
- **Mobile reality**: old app versions live in the wild for years on low-end devices. The server
  must support the last 12 months of released app versions, which is a design constraint on
  every breaking idea.

## 6.11 Artefacts this document depends on

| Artefact | Link |
| --- | --- |
| ART-037 OpenAPI spec (generated, linted in CI) | §6.1–6.10 |
| ART-038 Event catalogue | §6.12 |
| ART-048 Threat model | §6.8, §6.6 |
| ART-055 Test matrix | §6.9, §6.8 |
| ART-021 Permission matrix | §6.8 |

## 6.12 Event catalogue (async, internal)

| Event | Producer | Consumers | Payload (key fields) | Idempotency |
| --- | --- | --- | --- | --- |
| `user.verified` | Identity | Matching, Notifications | `user_id`, `kind`, `verified_at` | `user_id+kind` |
| `job.published` | Demand | Matching, Search index, Notifications | `job_id`, `skills[]` | `job_id+version` |
| `proposal.accepted` | Contracts | Contracts, Notifications, Analytics | `proposal_id`, `engagement_id` | `proposal_id` |
| `milestone.funded` | Money | Contracts, Notifications | `milestone_id`, `amount` | `milestone_id` |
| `milestone.accepted` | Contracts | Money, Reputation, Notifications | `milestone_id`, `actor_id` | `milestone_id+seq` |
| `payout.settled` | Money | Notifications, Finance | `payout_id`, `amount`, `rail` | `payout_id` |
| `dispute.opened` | Disputes | Money (hold), T&S, Notifications | `dispute_id`, `milestone_id` | `dispute_id` |
| `review.created` | Reputation | Matching, Notifications | `review_id`, `subject_id`, `rating` | `review_id` |
| `user.suspended` | T&S | Auth (revoke sessions), Matching | `user_id`, `reason_code` | `user_id+action_id` |

Rules: every event is versioned (`v1`), carries `occurred_at`, `actor_id`, `trace_id`; consumers
must be idempotent; the outbox is the only producer path (no "publish then commit").
