# Verification evidence and release gates

Version 0.2.4 · 9 October 2026

## Executive decision

**Suitable for local development and fictional-data demonstrations. Not approved for public commercial deployment or real financial/customer records.** Passing tests is evidence for specific scenarios, not proof of overall safety, business value or native-device compatibility.

## Completed checks

| Check | Result | Boundary |
|---|---|---|
| Backend/API test suite | 26 tests passed | Covers listed auth, tenancy, validation, payments, concurrency, workflow, deletion, AI-boundary and backup scenarios |
| TypeScript | `tsc --noEmit` passed | Static checking, not runtime correctness |
| Expo dependency compatibility | Reported dependencies up to date | Does not clear security advisories |
| Web export | Successful | Browser assets generated from shared mobile source |
| Android JavaScript export | Successful | Hermes bundle generation only, not APK/AAB/native compilation |
| iOS JavaScript export | Successful | Hermes bundle generation only, not IPA/signing/device test |
| Local-reminder and daily-check-in source/configuration | Added and type-checked | Shared source schedules generic opt-in local reminders and opens a validated check-in queue; physical Android/iPhone delivery, permission, tap and workflow tests are still manual checks |
| Chromium end-to-end smoke | Passed for v0.2 baseline | Demo → booking → deposit/payment → status → collection → message → CSV export → mobile search/filter; it cannot verify native OS notifications |
| Mobile-sized web viewport | No document-level horizontal overflow at 390px in smoke test | Not all screen sizes, text scales or native devices |
| Browser errors | No uncaught page errors during smoke scenario | Not exhaustive |
| Backup/restore verification | Test passed | Local copy, integrity/FK check and record count; no scheduled/off-site recovery |
| Python dependency audit | No known vulnerabilities reported after upgrading Starlette | Database coverage is time-sensitive; not proof of zero vulnerabilities |
| npm dependency audit | 24 findings: 15 high, 9 moderate | Unresolved, primarily transitive toolchain paths; release review required |

Evidence files: `backend-test-results.txt`, `browser-test-results.txt`, `native-bundle-results.txt`, `expo-compatibility.txt`, `npm-audit.json`, `python-audit.json`, and screenshots. One Python test-client deprecation warning remains; it is recorded in the test output.

## Mobile UAT screenshots and remediation

Screens captured during Android Expo Go use showed the real payment and cancellation paths running. They also exposed two usability defects: an empty payment/reference field surfaced a raw validation phrase (`String should have at least 1 character`), and a stale cancellation error could appear behind/repeat within a later confirmation sheet. Version 0.2.4 adds client-side required-reference validation, disables ordinary invalid confirmation attempts, clears stale error state before cancellation confirmation, and confines modal-specific errors to the active modal. This is a source-level remediation; a physical regression retest is still required.

## Dependency findings and response

The initial Python audit identified Starlette advisories. The installed dependency was upgraded to 1.7.0, package consistency checked, and the backend test suite rerun. The subsequent audit reported no known findings.

The mobile project uses Expo SDK 57 with compatible package versions and a lockfile. `npm audit fix` did not safely remove all findings. Reports include transitive `braces`, `node-forge`, and `uuid` paths. The automatic force-fix suggestion would downgrade Expo to an incompatible older major release; it was not blindly applied.

Required next action: triage each advisory for reachability and affected build/signing/runtime context, use compatible patched dependencies when available, test alternatives, and document any defensible time-limited exception with an owner. Do not declare these advisories harmless merely because several are build-tool dependencies. Do not expose Metro/EAS development tooling to untrusted users. No mobile commercial release is approved by this report.

## Security threat review

| Threat | Current control | Residual risk / required work |
|---|---|---|
| Cross-workspace record access | Server-derived owner scope on data access | Independent review, broader fuzzing and property tests |
| Duplicate/competing payments | Idempotency records + serialized transactions | Durable mobile keys/reconciliation across app restarts |
| Password theft | Salted KDF; opaque hashed sessions | Recovery, MFA decision, session inventory, breach response |
| Credential stuffing/abuse | Per-process/IP rate limits | Durable distributed limits, verified proxy setup, monitoring |
| XSS/token disclosure in browser | React text rendering; no rich HTML injection | sessionStorage exposure; stronger CSP/session design and audit |
| Device theft | Native SecureStore integration | Actual device backup/keychain tests and lifecycle review |
| Insecure transport | HTTPS enforcement in release native client | Real TLS deployment, certificate and platform verification |
| CSV injection | Formula-leading values neutralized | Spreadsheet compatibility/security review |
| Incorrect financial corrections | No event overwrite through API | Dedicated reversal/correction policy remains missing |
| Data loss | Local backup and verification tool | Encrypted off-site backups, scheduling, alerting and recovery rehearsal |
| AI hallucination/data disclosure | Minimal status/date only; consent; no tools; reviewed drafts | Live provider evaluation/terms and durable spend limits |
| Supply chain | Version lock, compatibility check, audits | Unresolved npm findings and controlled signing pipeline |
| Privacy noncompliance | Minimal fields, export/delete, no live data in demos; generic local lock-screen reminders | Owner/controller responsibilities, DPC registration, lawful basis, notices, retention and processor contracts; remote-notification token/policy review before implementation |

## Test details

Backend tests include unauthenticated access, registration/login/logout, weak input, wrong password, session expiry, tenant isolation, idempotent create/payment, changed-payload key conflict, overpayment/refund bounds, integer validation, extra-field rejection, lifecycle/closure, cancellation, stale-version conflict, editing below paid amount, lack of payment mutation endpoint, concurrent receipts, account deletion cascade, CSV safety/JSON export, demo isolation, AI disabled/consent/minimal-context adapter mock, body-size limits, auth rate limits, response headers and backup/restore.

Browser smoke uses Chromium and fictional records. It does not test Firefox/Safari, native OS APIs, EAS signing, slow/interrupted networks, keyboard-only completion, screen readers, large text, localization, load, battery use or all error paths.

AI tests use a mock or disabled provider; no paid model response was generated. The Dockerfile is supplied but has not been built or deployed in this session.

## Release-blocking gaps

1. Resolve/triage npm advisories and verify the actual native build/signing chain.
2. Produce signed Android/iOS test builds and complete real-device tests.
3. Add truthful mistaken-entry reversals/corrections and required post-collection/return policies.
4. Add verified identity, password recovery/change, all-session management and appropriate browser session protection.
5. Make payment retries/reconciliation durable across app termination.
6. Review privacy, jurisdiction, controller/processor registration, terms, support and retention before live personal data.
7. Deploy HTTPS, durable database storage, access controls, backups, restore drills and incident monitoring.
8. Complete accessibility/security review and measurable performance/availability tests.
9. Validate willingness to pay; configure a legitimate billing provider only with authorization.
10. Agree production responsibility, operating budget, support and release/rollback authority.

## Eight readiness dimensions

| Dimension | Current assessment |
|---|---|
| Product-ready | Core development workflow works; major commercial gates remain |
| Standards/protocol-ready | Structured contracts and reference-informed controls; no conformance certification |
| Professional craft | Coherent design inspected in desktop/mobile browser views; user testing pending |
| Project-ready | Source, tests, setup, architecture and requirements supplied; budget/timeline still unvalidated |
| Academically sound | Claims separated from hypotheses; references provided; no original field study |
| Industry-ready | Not yet; independent review, native testing and operations absent |
| Business-ready | Pricing hypothesis and validation plan, not demonstrated revenue |
| Marketing/sales-ready | Honest positioning and demo; no validated claims, acquired customers or sales operation |

Stop/go decision: **GO for fictional-data development and research demonstrations; NO-GO for public commercial launch.**
