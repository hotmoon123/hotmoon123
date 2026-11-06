# 09 — Security, Privacy & Compliance (Ghana-first)

> Security here is not a checklist appended to delivery; it is a set of **specific threats to real
> people**: a worker's ID sold on a Telegram channel, a client's deposit released to a fake
> profile, a woman harassed through a DM she cannot escape. Severity is measured in harm, not in
> CVSS alone.

---

## 9.1 Threat model frame

**Assets** (ranked by harm if compromised):

| Rank | Asset | Harm | Primary threats |
| ---: | --- | --- | --- |
| 1 | Escrow funds in flight | Direct financial loss; platform insolvency | webhook forgery, insider adjustment, payout redirection |
| 2 | Identity documents + selfies | Identity theft, sextortion, fraud | storage leak, over-broad access, log leakage, vendor compromise |
| 3 | Payout destinations (MoMo/bank) | Theft of earnings | account takeover, SIM swap, change-without-verification |
| 4 | Account sessions | Full account control | OTP interception, token theft on rooted device, credential stuffing |
| 5 | Private work content (briefs, files) | Commercial harm, harassment | BOLA/IDOR, signed-URL leakage, share link abuse |
| 6 | Reputation data | Economic harm, unfair exclusion | manipulation, bias, unauthorised disclosure |
| 7 | Admin console | Everything above at once | phishing of staff, session hijack, over-privileged roles |

**Attackers:** opportunistic fraudsters (most common), organized scam rings, malicious insiders
(including a bribed support agent), competitors scraping supply, and — rarely but expensively —
targeted attackers after a specific person.

## 9.2 STRIDE per trust boundary (STRIDE — S14)

| Boundary | Spoofing | Tampering | Repudiation | Info disclosure | DoS | Elevation |
| --- | --- | --- | --- | --- | --- | --- |
| Device ↔ API | SIM swap → OTP; stolen refresh token | replayed money requests | "I never accepted" | PII in responses to wrong user | SMS/OTP cost bombing | mobile token used on admin API (audience split prevents) |
| API ↔ PSP | forged webhook | amount tampering | chargeback denial | provider key leak | — | fake "funded" state |
| API ↔ storage | signed URL guessing | file replacement | upload denial | public bucket misconfig | upload flood | path traversal |
| API ↔ KYC vendor | spoofed callback | tampered verdict | — | ID images in logs | vendor outage | auto-approval on failure |
| Ops ↔ admin | phishing staff | mass export | shared logins | bulk export | — | self-granted role |
| CI/CD ↔ prod | stolen deploy key | malicious dependency | unsigned deploys | secrets in logs | — | pipeline → prod shell |

**Mitigations in priority order** (each becomes a ticket with an owner):

1. **Webhook signature verification + replay protection** before any state change (ART-041).
2. **OTP hardening**: rate limits per phone/IP/device, attempt caps, SMS pumping detection
   (S28 OAT), and **no OTP-only re-authentication for payout-destination changes** — require
   KYC re-match or a 24h cooling period with notification to the old number.
3. **Object-level authorization everywhere** (BOLA/IDOR — S34 is the #1 API risk): every read
   scoped by ownership; signed URLs expire in 10 minutes and are per-object.
4. **Separate admin identity plane**: distinct token audience, MFA (TOTP/hardware), IP allowlist
   for bulk actions, and **4-eyes** on money adjustments.
5. **Append-only audit** with tamper evidence (hash chain) for privileged actions.
6. **Secret management**: no secrets in the repo, in mobile bundles, or in CI logs; rotation
   recorded (ART-057).
7. **Least privilege in CI**: OIDC to cloud, no long-lived keys, branch protection, signed commits
   for release tags (ART-076).

## 9.3 Web & API security baseline

| Control area | Requirement | Verification |
| --- | --- | --- |
| Authentication | OTP + device binding; refresh rotation with reuse detection; session revocation on password/phone change | ASVS V6/V7 tests (S20) |
| Authorization | deny-by-default; policy functions tested per role; no client-side enforcement | ART-146 role×endpoint suite |
| Input handling | schema validation at the edge (Zod/DRF serializers), output encoding, no string-built SQL | ART-147 review + fuzzing (ART-140) |
| File uploads | type sniffing, size limits, AV scan, strip EXIF, never served from the API origin | ART-055 cases |
| Rate limiting | per identity + IP + device; stricter on OTP, payouts, reports | ART-087 |
| Transport | TLS 1.2+ only, HSTS, certificate pinning in the app (**with a rotation plan**) | ART-068 |
| Headers/CSP | strict CSP for admin console; no inline scripts | ART-067 |
| Logging | no PII, no tokens, no full phone numbers; structured events with trace ids | log review sample |
| Dependencies | lockfiles, automated update PRs, SCA in CI, SBOM per release | ART-076 |
| Error handling | no stack traces or SQL in responses; correlation id only | ART-067 |

Target: **OWASP ASVS 5.0.0 Level 2** for the API (S20), with Level 3 items reviewed for the money
and identity paths.

## 9.4 Mobile security baseline

Target: **OWASP MASVS 2.1.0, profile L2 + P** (S21).

| Group | What we do | Test (MASTG/ART-068) |
| --- | --- | --- |
| STORAGE | tokens in SecureStore/Keychain; no PII in AsyncStorage/logs/cache; screenshots blocked on sensitive screens | inspect app data dir, logcat/oslog |
| CRYPTO | platform primitives only; no custom crypto; keys in Keystore/Keychain | static + runtime inspection |
| AUTH | short-lived tokens; biometric unlock optional but never the only factor; re-auth for payout changes | flow tests |
| NETWORK | TLS enforced; cleartext blocked; pinning with backup pins | proxy test (mitmproxy) |
| PLATFORM | no exported components without permission; deep links validated; no WebView for sensitive flows | manifest/entitlement review |
| CODE | release builds not debuggable; no secrets in bundle; R8/obfuscation for release | build inspection |
| RESILIENCE | root/jailbreak signals used as risk input (not a hard block — many honest users have rooted devices) | Frida attempt |
| PRIVACY | data-safety declarations match actual collection; analytics minimised; consent recorded | store form vs code diff |

**Honest note on root detection:** in this market, blocking rooted devices would exclude legitimate
users (shared phones, cheap devices with custom ROMs). We use it as a *risk signal* for money
operations, not as a lockout.

## 9.5 Privacy by design (Act 843)

| Obligation | Implementation | Evidence |
| --- | --- | --- |
| **Register as data controller before processing** (s.27(1), S2) | file with DPC; certificate kept; renewal at 2 years diarised | ART-070 |
| Lawful basis & consent | notice at signup; granular consent for analytics/marketing; records with timestamp+version | ART-071 |
| Data minimisation | collect only what the flow needs (e.g. no date of birth unless required for ID match) | ART-029 review |
| Purpose limitation | analytics events defined in ART-030; no secondary use without a new basis | quarterly review |
| Retention & deletion | per-class schedule (ART-085); deletion jobs tested; **7-year retention for financial records** (S27) | deletion certificates |
| Data subject rights | access/correction/deletion workflow with SLA; in-app request path | DSAR log |
| Cross-border transfer | adequacy/safeguards/BCR basis documented; provider regions listed (S3) | ADR-006 |
| Security safeguards | encryption at rest (KMS) and in transit; access control; audit | pen-test + audit |
| Breach response | detect → contain → assess → notify DPC and data subjects per applicable duty and good practice | ART-073 |

**Special-category care:** ID documents, selfies, and any health or biometric data are treated as
high-sensitivity: encrypted with a separate key, access requires a ticket reference, and every
access is logged and reviewed monthly.

**The privacy question we must answer in plain language before launch:** *"Why do you need my
Ghana Card, who can see it, and what happens if I refuse?"* If the answer is not one sentence, the
flow is wrong.

## 9.6 Regulatory register (Ghana, as at 2026-11-06)

| Area | Instrument | Obligation | Owner | Status / next action |
| --- | --- | --- | --- | --- |
| Data protection | Data Protection Act, 2012 (Act 843) (S2) | register with DPC before processing; 8 principles; rights | D054 | **must register pre-launch** |
| Cross-border data | Act 843 transfer rules (S3) | adequacy / safeguards / BCR basis | D054 | ADR-006 written position |
| Payments | Payment Systems and Services Act, 2019 (Act 987) (S5) | no payment system/service without BoG licence | D018 | posture A (provider split) with written counsel opinion |
| Electronic transfer levy | Repeal Act, 2025 (Act 1128) (S6) | e-levy abolished 2 Apr 2025 — do not price it in | D025 | confirm with PSP statements |
| Tax & records | Revenue Administration Act, 2016 (Act 915) s.27(3) (S27) | keep transaction records ≥6 years | D025 | retention in ART-085 |
| Identity | NIA Ghana Card verification (S36) | acceptable KYC document; use NIA-verified services where possible | D154 | vendor selection |
| Consumer protection | Consumer Protection Act, 2022 (Act 1085) — *to be confirmed with counsel* | fair terms, no misleading claims, complaint handling | D017 | legal review before T&Cs |
| Labour classification | Labour Act, 2003 (Act 651) + practice | workers are independent contractors, not employees — the T&Cs and control model must match | D017 | counsel sign-off on contractor terms |
| Cybersecurity | Cybersecurity Act, 2020 (Act 1038) | report significant incidents to CSA where applicable | D187 | confirm applicability with counsel |
| App stores | Apple 3.1.3(d)/(e) (S18); Google Play payments policy (S19) | real-world services use external payment; data-safety declarations | D059 | review notes prepared |

**Rules for this register:**
1. Every row has an **owner**, an **evidence link**, and a **next action date**.
2. Anything marked *to be confirmed with counsel* is **not** relied upon in product copy until confirmed.
3. The register is reviewed **quarterly** and after any regulator publication (ART-070).
4. We do not claim certifications we do not hold. No "GDPR compliant" badge, no "ISO 27001" until audited.

## 9.7 App-store compliance (it is a compliance surface, not marketing)

| Requirement | Our position | Source |
| --- | --- | --- |
| Paying for real-world services | Use our own PSP flow, **not** in-app purchase, for work performed outside the app | Apple 3.1.3(d)/(e) (S18); Google Play payments policy (S19) |
| Digital-only goods (e.g. a paid assessment, profile boost) | If we ever sell digital content consumed *in* the app, it must use the store's billing | S18/S19 |
| User-generated content (chat, reviews, profiles) | Report + block + moderation SLA + published policy; app must filter objectionable content and act on reports | Apple 1.2; Google UGC policy |
| Account deletion | In-app path to delete account and data, with the financial-retention exception explained | Both stores require deletion |
| Data safety / privacy labels | Generated from ART-029 data inventory, not typed from memory | S19 |
| Sign-in | If third-party sign-in is offered (Google/Apple), Apple requires Sign in with Apple for iOS | S18 |
| Payments disclosure | Terms must state fees, escrow mechanism, and refund policy in plain language | S18/S19 |

## 9.8 Security programme cadence

| Activity | Frequency | Owner | Evidence |
| --- | --- | --- | --- |
| Dependency and container scanning | every PR + nightly | D150 | CI logs, ART-076 |
| SAST | every PR | D097 | triage log |
| DAST on staging | weekly | D148 | scan report |
| Authz matrix regression | every release | D146 | test report |
| Threat model review | per major feature | D068 | ART-048 update |
| Pen test (external) | pre-launch, then annual | D147/D148 | ART-069 |
| Access review | quarterly | D187 | access list diff |
| Restore drill | quarterly | D227 | ART-074 evidence |
| Incident tabletop | twice yearly | D156 | ART-073 record |
| Privacy review of new data fields | per PR that adds PII | D297/D054 | checklist |

## 9.9 Incident severity and response

| Sev | Definition | First response | External comms | Owner |
| --- | --- | --- | --- | --- |
| **S1** | Money loss, data breach with PII, total outage | 15 min, all-hands page | status page + affected users + DPC where required | D005 |
| **S2** | Partial outage, one critical function down, suspected fraud ring | 30 min | status page | D223 |
| **S3** | Degraded performance, single-user data issue | 4 h | direct to affected user | D092 |
| **S4** | Cosmetic, workaround exists | next business day | none | D121 |

Blameless postmortem within 5 business days for S1/S2; action items tracked to closure; a postmortem
without a **systemic** fix is a complaint, not a postmortem (S23/S26).

## 9.10 Security metrics that matter

| Metric | Target | Why |
| --- | --- | --- |
| Critical vulnerabilities outside SLA | 0 | obvious |
| Mean time to remediate (high) | <7 days | |
| Authz test coverage of endpoints | 100% | BOLA is the top API risk |
| Secrets found in repo (scans) | 0 | |
| Phishing simulation failure rate (staff) | <5% | admin accounts are the crown jewels |
| Fraud loss / GMV | <0.3% | trust economics |
| Customer reports per 1,000 completed jobs | <10, with >90% resolved <48h | safety |
| DSAR response time | <30 days, target 10 | legal + trust |
| Backup restore success | 100%, last test <90 days | survivability |

## 9.11 What we will not do (security ethics)

1. We will not sell or share user data with advertisers or data brokers.
2. We will not use dark patterns to obtain consent, or make withdrawal of consent harder than giving it.
3. We will not silently read user chats; moderation access is logged, scoped to reported content,
   and reviewed.
4. We will not publicly shame users in dispute outcomes; decisions are private, rationales are
   shared with the parties.
5. We will not claim security certifications we have not earned.
