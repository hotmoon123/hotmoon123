# Requirements specification — v0.2.4

**Authority:** current user request, established StitchLedger decisions, and explicit technical constraints. This document supersedes v0.1 implementation-status claims. Requirement IDs are local to this release.

**Standards boundary:** the public IEEE description of ISO/IEC/IEEE 29148:2018 addresses requirements processes/products and the characteristics of good requirements. We use identifiable, testable requirements and traceability; we have not reviewed the full paid standard or demonstrated clause-level conformance. https://standards.ieee.org/ieee/29148/6937/

## 1. Scope and context

A single-owner tailoring workspace, usable through a shared Android/iOS codebase and a browser build. The backend is the source of truth. Devices must be online for reads/writes. No funds are held or transferred. Initial currency is GHS. The owner may record minimal customer information but must not use live personal data until deployment/privacy gates are complete.

Actors: workspace owner, unauthenticated visitor, optionally configured AI provider, future operator/maintainer. A demo visitor receives a separate ephemeral-access owner account with fictional data. There are no staff/customer/admin-console roles in this release.

## 2. Functional requirements and evidence

Priority P0 = essential for this development milestone. P1 = commercial-release gate or next increment. “Tested” describes the supplied test coverage, not a universal guarantee.

| ID | Requirement / rationale | Acceptance condition | Implementation / evidence |
|---|---|---|---|
| AUTH-01 P0 | Register a studio owner | Valid email syntax, 12–128 character password, 2–80 character studio; duplicate email rejected | Implemented; auth/validation tests |
| AUTH-02 P0 | Authenticate and revoke sessions | Correct credentials create a session; wrong credentials reject; logout invalidates that token; expired token cannot read | Implemented; auth, expiry tests |
| AUTH-03 P0 | Keep raw credentials out of database | Salted password KDF and SHA-256 session token digest stored; bearer token returned only to client | Implemented; code review, not independent cryptographic audit |
| AUTH-04 P1 | Establish and recover real identity | Verified email, tested password recovery, change password and revoke all sessions, MFA decision | Not implemented; release blocker |
| DEMO-01 P0 | Provide isolated fictional workspaces | Two demo sessions have distinct IDs and cannot access each other's records | Implemented; demo/isolation tests |
| ORDER-01 P0 | Book an order atomically | Required fields validated; deposit ≤ price; order and any opening receipt both commit or neither | Implemented; create/validation tests + browser flow |
| ORDER-02 P0 | Persist exact amounts | API accepts bounded nonnegative integer pesewas, not floats/strings/booleans | Implemented; integer-money tests |
| ORDER-03 P0 | Edit active orders | Changed fields saved with matching version; total cannot drop below net paid; closed orders reject changes | Implemented; edit/version tests |
| ORDER-04 P0 | Enforce state model | Allowed transitions only; collection requires zero remaining balance | Implemented; status tests + browser flow |
| ORDER-05 P0 | Cancel safely | Cancellation allowed only before closure and with zero net paid | Implemented; cancellation test |
| ORDER-06 P0 | Find work quickly | Customer/garment search and explicit filters return matching records | Implemented; browser search/filter smoke test |
| ORDER-07 P1 | Correct closed-order mistakes | Authorized reopen/correction policy preserves immutable history and customer obligations | Not implemented |
| REM-01 P0 | Offer an owner-controlled daily workflow check-in on a native device | Owner can opt in/out of one generic daily 08:00 local notification; permission denial is explained | Implemented in mobile source; Android/iPhone manual delivery verification pending |
| REM-02 P0 | Offer a focused due-date reminder for an active order | Owner can schedule 08:00 local day-before or due-day reminder; tap opens review context, not an automatic state change | Implemented in mobile source; Android/iPhone manual delivery verification pending |
| REM-03 P0 | Protect customer/financial information on the lock screen | Reminder text contains no customer name, garment, date, amount, payment method or balance | Implemented fixed generic notification content; physical inspection pending |
| REM-04 P1 | Deliver reliable server-originated reminders across devices | Token lifecycle, opt-out, quiet hours, provider receipts, monitoring, credentials and privacy review complete | Not implemented; Expo Go does not support remote push testing |
| REM-05 P0 | Turn a daily reminder into an accountable workflow review | Tapping the daily local reminder opens an active-order queue; user may confirm one valid next stage, keep current stage, open full order, or set tomorrow reminder | Implemented mobile source; physical Android/iPhone notification/tap test pending |
| REM-06 P0 | Preserve workflow and financial integrity during daily check-in | Overdue remains derived; collection cannot bypass zero balance; server validates current version/transition; notification tap alone changes nothing | Implemented through existing backend rules plus check-in UI; physical test pending |
| BRAND-01 P0 | Supply consistent platform and in-app brand assets | App icon, adaptive foreground, splash mark, notification silhouette and in-app mark derive from one original design system | Implemented; assets/configuration inspected, physical platform rendering pending |
| BRAND-02 P1 | Clear rights and store presentation before commercial release | Trademark/name, store feature-graphic requirements and commercial-use review completed by owner/qualified adviser | Not implemented; a simple original asset is not trademark clearance |
| PAY-01 P0 | Record actual money received elsewhere | Positive receipt ≤ remaining balance; required method and reason/reference | Implemented; payment tests |
| PAY-01a P0 | Explain required payment/refund reference before request | Payment/refund confirmation is unavailable until a non-whitespace reason/reference is supplied; accessible in-app copy explains why | Implemented mobile source; physical retest pending |
| PAY-02 P0 | Record actual money returned elsewhere | Refund ≤ net recorded payments; append negative entry without changing earlier entries | Implemented; refund tests |
| PAY-03 P0 | Prevent duplicate financial requests | Same key+payload returns original result; same key+different payload rejects; key scoped to owner | Implemented; idempotency tests |
| PAY-04 P0 | Prevent concurrent overcollection | Simultaneous writes serialize; only one of two conflicting receipts succeeds | Implemented; concurrency test |
| PAY-05 P0 | Preserve payment history through API | No payment edit/delete endpoint; detail and exports contain prior entries | Implemented; no-mutation test |
| PAY-06 P1 | Correct erroneous entries truthfully | Separate non-cash reversal event links to original; cannot reverse twice; downstream balances revalidated | Not implemented; real-money usage blocker |
| PAY-07 P1 | Survive client termination during retries | Persist queued idempotency keys and reconcile unknown outcomes across restarts | Not implemented; current key lasts while form remains open |
| DATA-01 P0 | Authorize every record access | User B cannot read/write/export User A's records using known IDs | Implemented; tenant-isolation tests |
| DATA-02 P0 | Export owner data | JSON includes user metadata, orders, payments and activity; excludes passwords/tokens | Implemented; JSON test |
| DATA-03 P0 | Neutralize dangerous CSV cells | Formula-leading customer/garment fields prefixed before CSV export | Implemented; CSV safety test + download smoke test |
| DATA-04 P0 | Delete account with confirmation | DELETE phrase + password for registered owner; dependent active records/sessions removed | Implemented; deletion test |
| DATA-05 P1 | Meet data-subject rights and retention duties | Confirm lawful basis, notice, controller/processor duties, retention/backup treatment and legal holds | Legal/operator review pending |
| MSG-01 P0 | Draft reviewed customer messages | Template uses current server data; explicitly not AI; copy/share requires user action | Implemented; browser template test |
| AI-01 P0 | Fail safely when AI is absent | Capability false when key/model missing; AI route returns unavailable; templates continue to work | Implemented; disabled-AI tests |
| AI-02 P0 | Minimize AI disclosure | Explicit consent; only status and due date passed to adapter; no customer name, note or amount | Implemented; mocked adapter test |
| AI-03 P1 | Verify real provider behavior and spending | Live contract/evaluation tests, durable quotas, provider terms and cost cap | Not completed; no live provider call made |
| OPS-01 P0 | Make and verify a local database backup | Backup refuses overwrite; restricted file permission; restored copy passes integrity/FK checks | Implemented; backup/restore test |
| OPS-02 P1 | Meet operational recovery objectives | Encrypted off-site scheduled backups, alerts, restore rehearsal and owner-approved RPO/RTO | Not implemented |
| BILL-01 P1 | Collect legitimate subscription revenue | Chosen provider, verified webhooks, idempotency, entitlements, cancellation/refund/tax policy | Not implemented; no charges active |

## 3. Business rules

- Price and every payment use integer pesewas. Maximum individual amount: GHS 1,000,000.
- Net paid = sum of signed receipt/refund entries; 0 ≤ net paid ≤ agreed total.
- Remaining balance = total − net paid. Do not store a second independently editable balance.
- Production state is explicit; dates do not silently change status. Overdue is a derived alert condition—due date before the local calendar date while the status is still active—not a stored replacement for Booked, Cutting, Sewing or Ready.
- The owner may opt into a generic 08:00 local-device workflow reminder and may add one day-before/due-day local reminder per active order. A daily notification opens a check-in queue; only an explicit in-app confirmation can submit one permitted forward stage. The owner may keep the current stage or set a tomorrow reminder. Notifications never directly change order status or payment data.
- Closed means Collected or Cancelled. No edits/payments/reopening on closed orders in v0.2.1.
- Collected requires net paid = total; Cancelled requires net paid = 0.
- Opening deposit is recorded as Cash. For a bank/MoMo deposit, create with zero opening cash and record the actual method afterward.
- No direct deletion of individual orders or events. Owner-level account deletion is an explicit separate privacy operation.
- “Immutable” means append-only through this API, not cryptographically tamper-proof against a database administrator.
- AI cannot modify data, authorize payments, set deadlines or send messages.
- All-time receipt/refund totals represent recorded movements, not recognized revenue or taxable profit.

## 4. Data definitions

| Entity | Fields and purpose |
|---|---|
| User | ID, normalized email, password KDF, studio name, demo flag, creation time |
| Session | Hashed bearer token, user FK, expiry timestamp |
| Order | ID, owner FK, customer display name, garment, ISO date-only deadline, total integer, status, notes, version, UTC creation time |
| Payment | ID, owner FK, order FK, signed integer amount, method, note, UTC creation time |
| Audit event | ID, owner FK, order FK, action, brief change detail, UTC creation time |
| Idempotency operation | Owner + key PK, request digest, original JSON result |

Customer names are not unique identifiers. Two different customers can have the same name, and one customer can be entered inconsistently. A separate Customer entity and reconciliation workflow are future scope, not silently implied by name counts.

## 5. Non-functional requirements

| ID | Target | Evidence / gap |
|---|---|---|
| NFR-01 | Type-safe mobile client; strict JSON body validation | TypeScript check passes; Pydantic rejects unexpected fields |
| NFR-02 | No horizontal overflow at a 390px web viewport | Chromium smoke check passes; not proof for every font/locale/device |
| NFR-03 | Accessible core workflows on mobile/web | Labels, text status, safe areas, practical targets implemented; full WCAG/VoiceOver/TalkBack audit pending |
| NFR-04 | No sensitive values in URLs; authenticated API responses not cached | Bearer header and no-store implemented; infrastructure logging review pending |
| NFR-05 | TLS for live traffic | Native release client rejects non-HTTPS API base; deployment TLS not provisioned |
| NFR-06 | Defined response/cost limits | Request body 32KB limit; per-process rate limits; 25s client timeout; bounded AI output; no production load test |
| NFR-07 | Reliable concurrent money writes | SQLite BEGIN IMMEDIATE with bounded busy timeout; API concurrency test passes |
| NFR-08 | Practical performance at agreed pilot size | No formal p95 benchmark; full-list API is unsuitable for unbounded datasets; pagination required before scale |
| NFR-09 | Usable error states | Inline errors, refresh, explicit conflict errors; offline edits intentionally unsupported |
| NFR-09a | Notification privacy and consent | Notification opt-in is explicit; lock-screen content is generic; scheduling errors explain permission/device/time boundary | Implemented source logic; physical native verification pending |
| NFR-09b | Asset quality and platform suitability | Vector masters and required raster derivatives exist; notification icon is monochrome; app text is not replaced by image text | Implemented source/configuration; native rendering and store policy checks pending |
| NFR-10 | Reproducible delivery | npm lockfile, pinned Python requirements, API contract, versioned source and test records included |
| NFR-11 | Vulnerability findings resolved/accepted before release | Python audit has no known findings at this check; mobile audit unresolved—see quality report |
| NFR-12 | Recovery objective | Proposed pilot RPO/RTO 24h each; local backup utility exists but operational objectives not proven |

## 6. Acceptance scenarios

A. **Happy path:** register → book GHS 100 / deposit GHS 20 → record GHS 80 → Cutting → Sewing → Ready → Collected. Ledger contains two receipts, total 100, balance zero.

B. **Network ambiguity:** retry the unchanged payment form after a timeout. Same idempotency key returns the same result. Closing/reopening the form loses the key; inspect the ledger before a new entry until durable reconciliation exists.

C. **Concurrency:** two GHS 8 receipts compete against a GHS 10 remaining balance. One succeeds; the second is rejected, leaving GHS 2—not a negative balance.

D. **Tenant boundary:** another authenticated owner supplies a valid foreign order ID. Server returns not found and discloses no payment details.

E. **Cancellation:** paid order cannot be cancelled until real funds have been returned and recorded, leaving net paid zero. This policy is a product assumption requiring customer validation.

F. **AI unavailable:** no configured provider → feature not advertised as connected, deterministic draft remains available.

G. **Account deletion:** incorrect password fails; explicit authorized deletion removes active database rows/sessions. Backup retention is a separate operational responsibility.

H. **Reminder safety:** owner opts into the generic daily reminder on a physical native device, grants OS permission, and then turns it off. The daily notification opens a queue that prioritises overdue/ready work. A future-order reminder opens the matching order after a notification tap; a stage remains unchanged until the owner confirms a valid in-app transition. Lock-screen text reveals no customer or money details.

## 7. Traceability and change control

User need “do not lose track of what is owed” → PAY-01/02/03/04 → event ledger + transaction boundary → idempotency/concurrency tests → pilot reconciliation observations.

User need “know the next commitment” → ORDER-04/06 → due-ordered list/state machine → browser flow → observed task completion.

User need “keep records private” → AUTH-02/DATA-01 → hashed sessions + owner predicates → isolation/expiry tests → external security review.

Every requested enhancement must state the need, affected requirement, acceptance test, data/privacy effect and commercial benefit. Reject scope that does not help the agreed studio workflow or business validation.
