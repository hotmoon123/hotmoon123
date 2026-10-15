# Kali Linux, Android/iPhone builds and operations

## 1. Local browser run (recommended first)

The prebuilt web frontend is bundled with the source. Python 3.10+ and the packages in `backend/requirements.txt` are enough to run it locally.

```bash
sudo apt update
sudo apt install python3 python3-venv unzip
mkdir -p /home/caleb/Projects
unzip /home/caleb/Downloads/stitchledger-mobile-v0.2.zip -d /home/caleb/Projects
cd /home/caleb/Projects/stitchledger-mobile
bash scripts/run-local.sh
```

Open `http://127.0.0.1:8000`. Select **Explore a private demo** or create a test account. Do not use real customer data. Keep the terminal running; stop with Ctrl+C.

Persistent database: `backend/data/stitchledger.sqlite3`. Do not delete it if you want to retain local accounts/records. Keep it outside version control. Demo access depends on the client session; a registered test account can sign in again. Session lifetime is 12 hours. Email verification and recovery are not provided, so a forgotten test password cannot be reset through the app.

A new demo account is created each time you select Explore a private demo. It is not shared with other visitors. There is no automatic cleanup scheduler; use account deletion or implement an operator-approved retention job before deployment.

## 2. Rebuild the shared frontend

Install a supported Node version. This release was built with Node 20.20.2, Expo SDK 57, its compatible React Native packages and TypeScript 6.0.x. Check actual versions rather than assuming Kali's package defaults match.

```bash
node --version
npm --version
cd /home/caleb/Projects/stitchledger-mobile/mobile
npm ci
npm run typecheck
npx expo install --check
npm run export:web
```

Serve the resulting `web-build/` using the backend. The default web API base is relative, so browser requests stay on the same origin. Running `npm run web` on another origin without a configured API/proxy is not the documented integrated setup.

## 3. Android and iPhone project setup

**Important:** the ZIP is source plus a web build, not an APK, AAB or IPA. Successful Android/iOS JavaScript exports are not signed native builds.

First obtain a reachable HTTPS backend. In `mobile/`, create `.env` from `.env.example` and set:

```text
EXPO_PUBLIC_API_URL=https://YOUR-OWNED-API-DOMAIN
```

This is a public server URL, never an API key. Restart Expo/rebuild after changing it. A native device cannot reach your laptop using `127.0.0.1`; that address points to the device itself. For a restricted local Android development network, use your laptop's LAN address and a debug build, bind the backend to that interface, and restrict the firewall to your trusted network. Do not open a public port. iOS platform transport rules may reject local HTTP, so prefer HTTPS rather than weakening release security.

Review `app.json` before linking/signing: name, icon, package/bundle ID, permissions and transport settings. `com.caleb.stitchledger` is a proposed identifier, not a registered/approved application identity. Validate trademark/name ownership and export/privacy declarations before store submission.

### Managed build path (requires your Expo account and signing setup)

From `mobile/`:

```bash
npx eas-cli@latest login
npx eas-cli@latest init
npx eas-cli@latest build:configure
npx eas-cli@latest build --platform android --profile preview
npx eas-cli@latest build --platform ios --profile preview
```

Read provider prompts before approving. Account ownership, signing credentials and potential fees belong to you. The assistant has not opened accounts, generated credentials, registered devices or submitted builds.

Expo documents cloud builds for both platforms, with Android on Linux workers and iOS on macOS workers. [1](https://docs.expo.dev/build/introduction/) Configuration links a project to the owner's EAS account. [2](https://docs.expo.dev/tutorial/eas/configure-development-build/)

The Android preview profile requests an APK. An iOS device build requires appropriate Apple signing/provisioning; simulator builds run on macOS simulators, not directly on Kali. Kali can be used to initiate a cloud build, but it does not supply Apple's local Xcode toolchain.

Do not rely on the currently installed Expo Go version being compatible with this SDK. Use a matching supported client or a properly configured development/native build and consult Expo's current instructions.

### Local Android alternative

Install the Android SDK, a compatible JDK and emulator/device tooling following official documentation. Then use `npx expo run:android`. This was not performed here. Local iOS native compilation requires macOS/Xcode; `npx expo run:ios` is not a Kali build solution.

## 4. Tests

Backend:

```bash
cd backend
.venv/bin/python -m pytest -q
```

Web/native JavaScript:

```bash
cd mobile
npm run typecheck
npm run export:web
npx expo export --platform android --platform ios --output-dir ../native-js-export
```

Chromium smoke (backend must already be running on local port 8000):

```bash
cd qa
npm ci
npx playwright install --with-deps chromium
node browser-test.cjs
```

The browser test creates fictional demo data. It covers the happy path and selected layout/search/export checks, not exhaustive validation.

## 5. Backup and restoration

The supplied utility uses SQLite's backup API rather than copying a potentially active WAL database file blindly.

```bash
cd backend
mkdir -p ../backups
.venv/bin/python backup.py backup ../backups/studio-2026-10-08.sqlite3
.venv/bin/python backup.py verify ../backups/studio-2026-10-08.sqlite3
```

Choose a new filename each time. Existing backup files are never overwritten by the tool. New files are created with mode 0600 on this platform. The verify command restores into an isolated temporary database and checks integrity, foreign keys and record counts. It does not replace the running database.

A real restore should be rehearsed: stop the server, preserve the damaged database/WAL/SHM for investigation, restore to a new clean location, verify, point `STITCH_DB` to it, revoke restored sessions, and validate business records before allowing writes. Do not overwrite a live database. Backups contain personal/account information and require encryption, access controls and retention decisions. No automated off-site schedule is installed.

## 6. Optional AI setup

Disabled by default. To activate only after approving provider cost/privacy conditions, set `OPENAI_API_KEY` and `AI_MODEL` in the backend environment and restart. `.env.example` is documentation; the backend does not automatically load a dotenv file. Use your process manager's secret mechanism; never commit credentials or put them in an `EXPO_PUBLIC_*` variable.

The backend requests short drafts from the configured provider. The app asks for consent before each call and only sends status/date. Verify current API/model support, costs, data terms and live outputs. The adapter has only been tested with a mock/disabled configuration. Keep provider billing caps; the local per-process rate limit is not a hard financial budget.

## 7. Production deployment outline — not yet executed

1. Satisfy the quality/security release gates; approve jurisdiction, privacy notice, terms and support ownership.
2. Choose and fund hosting with HTTPS, a persistent volume, restricted administration and monitoring.
3. Configure trusted proxy behavior correctly; do not trust arbitrary forwarded IP headers.
4. Disable unauthenticated demo creation if inappropriate (`ALLOW_DEMO=0`). Implement retention/abuse controls.
5. Keep one writer-host architecture for SQLite; switch databases through a tested migration when scaling requires it.
6. Schedule encrypted backups, test recovery and establish alerts.
7. Remove test accounts, secure API documentation as appropriate, tighten host/CSP/session settings.
8. Build signed apps against the approved HTTPS API, test on real phones, and complete store privacy/signing/review processes.
9. Add legitimate billing/entitlements only after owner/provider authorization and tests.

A Dockerfile is included as a deployment starting point. It has not been built/tested in this session. Mount persistent database storage with appropriate ownership; container recreation without persistence can lose records. A container alone does not supply TLS, security certification or operational readiness.

## 8. Troubleshooting

| Symptom | Check |
|---|---|
| `externally-managed-environment` | Use the provided virtual environment; do not use system `pip install` or `--break-system-packages`. |
| Port already in use | Choose another Uvicorn port, e.g. 8001, and open that URL. |
| Web page missing after source-only rebuild | Run `npm run export:web`; start/restart backend after `web-build` exists. |
| Phone cannot reach API | Use a reachable HTTPS URL; laptop localhost is not phone localhost. |
| Unauthorized/session expired | Sign in again; lifetime is 12 hours. |
| Version conflict | Refresh/open order again before changing it. Another device may have modified it. |
| Ambiguous payment save | Inspect the ledger; retry the unchanged still-open form. Do not create a new entry blindly. |
| Cancel rejected | Net recorded payments must be zero; record real refunds only. |
| Collection rejected | Pay/record remaining balance and follow the state sequence. |
| AI unavailable | Expected without backend credentials/model; use the free template. |
| npm audit findings | Read the quality report. Do not blindly force a breaking Expo downgrade. |

The workspace preview is a temporary demonstration environment, not a hosting contract or business continuity service.
