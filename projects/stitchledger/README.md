# StitchLedger · Android + iPhone project · v0.2.4

**Your craft. Your customers. All in order.**

A cross-platform tailoring-studio order and payment-record system: Expo/React Native/TypeScript frontend, FastAPI backend, SQLite data access, explicit workflow rules, auditable payment entries, and an optional AI drafting adapter.

**Status: tested development release, NOT a commercially launched or independently security-certified product.** Android and iOS JavaScript bundles were exported successfully; signed APK/AAB/IPA files have not been built or device-tested. The included browser build is immediately runnable. Use fictional data only until the release gates in `docs/QUALITY-AND-SECURITY.md` are satisfied.

## Start on Kali Linux — simplest path

Download `stitchledger-mobile-v0.2.zip` into `/home/caleb/Downloads/`, then:

```bash
sudo apt update
sudo apt install python3 python3-venv unzip
mkdir -p /home/caleb/Projects
unzip /home/caleb/Downloads/stitchledger-mobile-v0.2.zip -d /home/caleb/Projects
cd /home/caleb/Projects/stitchledger-mobile
bash scripts/run-local.sh
```

Open **http://127.0.0.1:8000** and choose **Explore a private demo**. Keep the terminal open; Ctrl+C stops the server. The script installs pinned Python dependencies in a virtual environment; it does not install system Python packages. Internet access is needed for the first dependency installation. Requires Python 3.10+.

The ZIP includes the web build, so Node.js is **not required for this first browser run**. This creates a new folder and does not overwrite the older `stitchledger` prototype. Do not copy the old SQLite database into the new project; the schemas are different and no migration from v0.1 is supplied.

### Subsequent startup

```bash
cd /home/caleb/Projects/stitchledger-mobile/backend
.venv/bin/uvicorn main:app --host 127.0.0.1 --port 8000
```

If port 8000 is occupied, choose `--port 8001` and open that port instead. No source-code edit is necessary.

## What works

- Register/sign in with a password; expiring revocable sessions; sign out.
- A private, separate demo workspace containing fictional orders.
- Create/edit orders, collection dates and notes; search and filter.
- Explicit Booked → Cutting → Sewing → Ready → Collected workflow, with limited rework transitions and cancellation rules.
- Cash opening deposit; subsequent Cash/MoMo/Bank receipt and refund records.
- Integer money arithmetic; no overpayment or excessive refund; serialized financial writes.
- Append-only payment entries through the API, order activity trail, idempotent order/payment retries.
- Outstanding balances, deadline guidance and ledger summaries calculated from actual stored records.
- Optional local 08:00 workflow reminder opens a daily active-order check-in; explicit in-app confirmation moves a valid order stage forward, while notification taps alone never change business data.
- Payment/refund entry form validates the required reference/reason in the app before an API request, avoiding raw backend schema wording in ordinary mobile use.
- Original, platform-specific app icon, Android adaptive foreground, launch mark and small notification silhouette; no stock/customer imagery is required for the operational UI.
- Reviewed message templates; optional opt-in AI provider adapter, disabled without credentials/model configuration.
- CSV order export, JSON account export, account deletion.
- Backup and isolated restore-verification utility.
- OpenAPI contract in `docs/openapi.json`; interactive API docs at `/docs` while the backend runs.

## Deliberate limitations

No real payment collection, subscription billing, store release, production hosting, email verification, password recovery, staff permissions, offline synchronization, production remote push notifications, live AI credentials, or demand validation. Local device reminders are implemented for Expo Go/native development testing; they are not a delivery-guaranteed server push service. Payment correction/reversal workflows beyond genuine refunds remain a release blocker; never record a fictitious refund to fix a typo. Closed orders are immutable in this release. Name-based customer counts are not a dedicated customer directory.

The app does not guarantee revenue. GHS 30/month is still a price-test hypothesis, not a validated price. No charge is active.

## Code layout

```text
mobile/                    Expo app for Android, iOS and web
  App.tsx                  Screens, forms and interactions
  api.ts                   Network client, token storage and types
  app.json / eas.json       Native app and build configuration
backend/
  main.py                  API, middleware and application rules
  db.py                    SQLite schema and transaction boundary
  security.py              Password hashing, session token hashing, local rate limits
  ai.py                    Optional AI drafting provider adapter
  backup.py                Local backups + restore verification
  tests/test_system.py     Automated API/domain tests
web-build/                 Prebuilt browser app served by FastAPI
scripts/run-local.sh       Kali-friendly local startup
qa/browser-test.cjs        Chromium end-to-end smoke test
```

## Documentation map

1. `docs/SYSTEM-BRIEF.md` — vision, mission, why/what/who/whom/when/where/which/how and product decisions.
2. `docs/REQUIREMENTS.md` — functional/non-functional requirements and acceptance evidence.
3. `docs/ARCHITECTURE.md` — component, data, security and workflow design.
4. `docs/METHODOLOGY.md` — phases, roles, governance, business validation and learning progression.
5. `docs/QUALITY-AND-SECURITY.md` — test evidence, dependency findings and launch blockers.
6. `docs/RUNBOOK.md` — Kali, native builds, backups, troubleshooting and operational responsibilities.
7. `docs/SOURCES.md` — research provenance and limitations.
8. `docs/NOTIFICATIONS-DESIGN.md` — local reminder workflow, privacy boundary, verification plan and production push-notification requirements.
9. `docs/VISUAL-ASSET-SYSTEM.md` — asset inventory, visual rationale, usage rules, rights boundary and device verification plan.
10. `docs/DAILY-CHECK-IN-WORKFLOW.md` — daily notification-to-review queue, truthful status progression, rules and acceptance scenarios.

## Development and tests

From `backend/`, after installing requirements:

```bash
.venv/bin/python -m pytest -q
```

From `mobile/`, with a compatible Node.js installation (tested here on Node 20.20.2):

```bash
npm ci
npm run typecheck
npm run export:web
```

The exported web app uses relative `/api` URLs. Restart the backend after the first export if the directory did not previously exist. For the included setup, open the backend URL, not a separately hosted web development port; no cross-origin browser configuration is needed.

Native build/setup details are in `docs/RUNBOOK.md`. Do not publish unchanged development configuration or test accounts.
