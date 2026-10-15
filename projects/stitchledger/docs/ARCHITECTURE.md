# Architecture and engineering decisions

## 1. Logical system

```text
Owner
  │
  ├── Android / iPhone app (Expo + React Native + TypeScript)
  │      └── token in native SecureStore; no offline financial database
  │
  └── Browser build (React Native Web)
         └── token in sessionStorage for this pre-release
                  │
                  ▼
           HTTPS API boundary (local HTTP for development)
                  │
         Request middleware
         body size · rate limit · request ID · response headers
                  │
         FastAPI / Pydantic contracts
         authentication · owner authorization · validation
                  │
         Application / domain rules
         workflow · exact money · idempotency · optimistic version
                  │
         Repository boundary (db.py)
         parameterized queries · BEGIN IMMEDIATE · commit/rollback
                  │
                  ▼
         SQLite on a persistent local volume
         users / sessions / orders / payments / audit / operations

Optional explicit-consent draft request
  → limited status/date context → AI adapter → external provider
  → draft text → owner review → manual sharing
```

These are responsibility boundaries, not seven independent microservices. APIs are contracts; middleware handles shared request processing; the backend owns rules; data access owns transactions. Networking and security cross all boundaries. This teaching model is not the OSI networking model.

## 2. Deployment choices

### Current tested path

One Uvicorn/FastAPI process serves both the exported browser files and `/api`. Browser calls are relative, avoiding localhost mistakes and cross-origin configuration. Development binds localhost by default in the supplied script; the hosted workspace preview binds 0.0.0.0 so its proxy can reach it.

SQLite is appropriate for a small single-host pilot. WAL and transaction locking support this test workload. A shared network filesystem, many write-heavy workers or multiple independently scaled app hosts is not an approved architecture. Move to a properly migrated PostgreSQL deployment if load/availability needs justify it.

### Native path

The same frontend source builds mobile JavaScript. Native apps require `EXPO_PUBLIC_API_URL` pointing at a reachable backend, preferably an owned HTTPS domain. A phone's localhost means the phone, not the Kali laptop. Public Expo variables are not secret storage.

App signing, installation, platform permissions, real device storage behavior, accessibility and distribution are separate validation steps. Successful JavaScript export does not prove a signed native application works.

## 3. Sequence — record a payment

```text
Owner → App: enter GHS amount, method, reason
App → App: parse decimal string to integer pesewas
App → API: bearer token + Idempotency-Key + JSON
API → Session store: verify token digest and expiry
API → Database: BEGIN IMMEDIATE
API → Idempotency store: look up owner/key
  Existing same payload → return original result
  Existing different payload → conflict
  New key:
    load owned order
    reject closed order
    calculate SUM(payment.amount)
    validate resulting paid amount is between zero and price
    append payment event
    increment order version
    append activity event
    save original response under idempotency key
    COMMIT
API → App: authoritative order state
App → Owner: refreshed detail and ledger
```

If any step before commit fails, roll back all writes. Existing payment rows are not overwritten. Keys are scoped per owner, and the digest includes the route action and order ID. Client retries within an open form reuse a key. Durable replay/reconciliation across app termination is still missing and explicitly tracked.

## 4. State model

```text
Booked → Cutting → Sewing → Ready → Collected
   ↑        │  ↑      │  ↑      │
   └────────┘  └──────┘  └──────┘
          limited one-step rework

Any active state → Cancelled (only if net paid = 0)
Ready → Collected (only if balance = 0)
Collected / Cancelled → no further transitions in v0.2
```

Rework is an explicit action, not a background guess. Every transition requires the version most recently read by the client; a stale version returns conflict instead of silently overwriting another device's work. Partial fulfillment, split orders, post-collection returns and retention of cancellation fees are out of scope.

## 5. Data model

```text
User 1 ── many Session
User 1 ── many Order
Order 1 ── many Payment
Order 1 ── many AuditEvent
User 1 ── many IdempotencyOperation
```

- Foreign keys are enabled for every connection.
- Owner ID is attached by the server from the authenticated session, not accepted from submitted JSON.
- The database stores total price; paid and remaining are derived.
- Payment signed integers represent receipts (+) and genuine refunds (−).
- Activity records document changes but are not a cryptographically tamper-evident log.
- Account deletion cascades over active records, which is different from editing an individual financial event.
- Baseline schema is version 1 of v0.2. No migration from v0.1 exists. Before future migrations, back up, test upgrade/restore, and define rollback behavior.

## 6. Security design

**Authentication:** passwords use PBKDF2-HMAC-SHA256, 600,000 iterations and random 16-byte salts. Sessions use random opaque tokens, store only a SHA-256 digest on the server, expire after 12 hours and are revocable on logout. This is not a complete identity platform: verification, reset, password changes, all-session revocation and MFA decisions remain outstanding.

**Authorization:** every order/detail/update/payment/ledger/export query scopes to authenticated owner. ID knowledge alone is insufficient. No staff-role expansion is implied.

**Device storage:** SecureStore integration for native; sessionStorage in browser. Browser XSS could read a token, so deployment should use a stronger browser authentication/CSP design and external assessment. Native encryption and keychain behavior have not been physically tested.

**Network:** release native client requires an HTTPS URL; backend TLS is a reverse-proxy/hosting responsibility. No wildcard browser CORS. Local HTTP only for development.

**Input/output:** JSON schema validation, bounded fields, 32KB body cap, integer money, parameterized SQL, React text rendering and CSV formula neutralization. No uploads or rich HTML interpretation.

**Abuse controls:** per-process in-memory request limits and AI request limit. These reset with the process and are neither global budget enforcement nor production-grade distributed abuse protection. Proxy/IP configuration and quotas need review before deployment.

**Data minimization:** no measurements, ID documents, payment account credentials, bank connection, automatic contacts access or background location. Do not put secrets into free-text notes.

**Availability:** client and provider timeouts, bounded database lock timeout, tested backup utility. No production monitoring, failover, restore schedule or SLO proof.

## 7. Optional AI adapter

The adapter uses an operator-configured `OPENAI_API_KEY` and `AI_MODEL` only on the backend. Configuration is not included and no live API call was made. It requests a short status/date draft with provider-side storage disabled in the request; that flag alone is not a contractual data-retention guarantee. Verify the provider's actual policies before activation.

Only status and due date are passed. Customer names, garment free text, notes, amounts and credentials are excluded. No tools are provided to the model. AI output is untrusted text and always labeled for human review. A model may still invent or misstate information; no draft may be automatically sent or used to mutate data. Templates remain the no-cost alternative.

The provider request cap is per-process. Set vendor-level spending limits and obtain the owner's approval before use. Model availability and price must be checked at configuration time rather than assumed.

## 8. Architecture decision records

| ADR | Decision | Benefit | Cost / reason to revisit |
|---|---|---|---|
| 001 | Expo + React Native shared client | One codebase for Android/iOS/web | Native builds/toolchain dependencies still need validation |
| 002 | Modular monolith backend | Easy local operation, coherent transactions | Larger team/load may need module extraction—not premature microservices |
| 003 | SQLite for local development/pilot | No database-server account or fee | Limited multi-host scaling and recovery automation |
| 004 | Append-only financial entries | Reviewable history, fewer silent errors | Requires full correction/reversal policies before real use |
| 005 | Derived balances + integer money | Avoid float rounding and duplicate truth | Multi-currency/tax needs separate design |
| 006 | Explicit optimistic versions | Detect concurrent edit conflicts | User must refresh after conflict |
| 007 | AI optional, drafts only | Product still works without paid inference | AI value remains unvalidated |
| 008 | No offline writes yet | Avoid unreliable sync of money records | Connectivity-dependent; offline demand must be researched |
| 009 | No live payment provider yet | No custody/settlement claims or accidental charges | Monetization and verified payment workflows are incomplete |

## 9. API contract and ownership

`openapi.json` is generated from the actual FastAPI models, not manually invented. `/docs` exposes the interactive contract for development. Routes include auth, account identity, orders/detail/edit/status, append-only payment recording, ledger, capabilities, exports, deletion and opt-in AI drafting.

API version is 0.2.0. URL paths are currently `/api` rather than a long-lived public versioned partner API. Stabilize response/error contracts and pagination before promising external integrations. No client SDK compatibility guarantee exists yet.
