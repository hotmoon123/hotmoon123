# v0.2.4 — 9 October 2026

- Addressed Android device user-acceptance observations from the payment and cancellation sheets.
- Payment/refund reference is visibly required, confirmation remains unavailable until amount and reference/reason are entered, and client validation gives a human-readable message rather than ordinary raw schema wording.
- Cleared stale errors before opening cancellation confirmation and suppressed background error duplication while an active modal is responsible for displaying an error.
- Added focused mobile UAT observation and regression-test documentation. Physical retest remains required after applying this update.

# v0.2.3 — 9 October 2026

- Converted the daily local workflow reminder into an authenticated, ordered daily check-in queue that prioritises overdue and ready work.
- Added explicit in-app forward actions: Booked → Cutting → Sewing → Ready → Collected, with existing server state/version/payment guards still authoritative.
- Added **Keep current status for now**, **Remind me tomorrow**, and **Open full order** actions to the queue.
- Preserved the distinction between a notification tap (opens review only) and a confirmed workflow action (records a truthful state change and audit event).
- Added daily check-in requirements, acceptance scenarios and design documentation. Android/iPhone physical notification/tap verification remains pending.

# v0.2.2 — 9 October 2026

- Added a coherent, original StitchLedger visual-asset system: primary iOS/general icon, scalable SVG masters, Android adaptive-icon foreground, splash mark and Android-compatible monochrome notification icon.
- Integrated the same brand mark into the app’s sign-in and desktop workspace lockups and configured the icon/splash assets for future native builds.
- Added `expo-splash-screen` at the Expo SDK 57-compatible version and regenerated Android/iOS native projects from the configuration.
- Added `docs/VISUAL-ASSET-SYSTEM.md`: design brief, rationale, asset inventory, do/don’t rules, rights boundary, anti-slop review, accessibility/platform constraints and verification record.
- TypeScript checking plus Android/iOS/web JavaScript exports passed. Native icon/splash and scheduled-notification behaviour remain physical-device checks, not fabricated success claims.

# v0.2.1 — 9 October 2026

- Added opt-in local Android/iPhone workflow reminders: one generic daily 08:00 check-in and a day-before/due-day collection reminder for active orders.
- Added privacy-preserving lock-screen content: no customer name, garment, due date, amount, balance or payment method appears in reminder text.
- Notification taps open authenticated review context; they never silently change a workflow stage or payment record.
- Added Expo SDK 57 compatible `expo-notifications`, Android notification permission/configuration, native project regeneration, requirements traceability and notification design documentation.
- TypeScript checking and Android/iOS/web JavaScript export passed. Native Android/iPhone scheduled-notification delivery remains a manual physical-device test.

# v0.2 — 8 October 2026

- Replaced browser-only frontend with shared Expo/React Native/TypeScript project.
- Added FastAPI backend with test accounts, revocable sessions and owner authorization.
- Added append-only receipt/refund records, version conflicts, idempotent financial requests and explicit lifecycle rules.
- Added exports, account deletion, local backup/restore checks and optional disabled-by-default AI drafting adapter.
- Added 26 backend tests, browser smoke test, native JavaScript bundle checks, dependency audit reports and expanded documentation.
- Preserved v0.1 separately. No automatic v0.1 database migration.

Not a production release: see docs/QUALITY-AND-SECURITY.md for missing identity recovery, financial corrections, durable retry reconciliation, native device tests, operational/privacy/billing gates and unresolved npm audit findings.
