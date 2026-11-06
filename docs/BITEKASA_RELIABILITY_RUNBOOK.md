# BiteKasa reliability plan and operations runbook

**Service model:** static Vite/React assets deployed by GitHub Actions to GitHub Pages. No API, database, container, VM, customer records, or server-side application exists. GitHub operates the TLS edge and static serving; BiteKasa owns source, content correctness, deploy workflow, account access, and response.

**Current state:** Pages has not been enabled and no production probes have run. All objectives below are proposed launch targets, not observed reliability or a contractual commitment.

## 1. SLIs, SLOs and error budget

| SLI | Proposed objective | Measurement / caveat |
|---|---|---|
| Public-site availability | ≥99.0% successful monthly probe runs | An hourly GitHub Actions probe checks home, three service pages, privacy notice, robots and sitemap. A run passes only if all seven return HTTP success. GitHub scheduled jobs can be delayed, and an hourly probe misses short interruptions; do not call this provider-grade uptime. |
| Deployment reliability | ≥95% successful production deployment runs in a rolling 30 days | Count completed Pages deployment workflows, excluding cancelled runs. With a small number of deployments this is directional, not statistically strong. |
| Recovery time | Restore or roll back a confirmed site outage within 2 hours during owner-supported hours | Measure from first confirmed incident to verified recovery; no on-call coverage is configured. |
| Content correctness | 100% of launched offer/contact data owner-verified | Binary release check, not a traffic metric. Current contact and service-area details remain unverified. |

For a 30-day month there are about 720 hourly probe opportunities. At 99.0%, the synthetic availability error budget is approximately **7 failed hourly runs** (7.2 mathematically). Use workflow run history as the initial record. A single prolonged outage may consume several runs. The budget is not a downtime guarantee and excludes intervals between probes.

**Dashboard / alerts:** each smoke-check Action writes a per-run table and failure count to its GitHub Actions job summary; the Actions history is the initial lightweight dashboard. Configure repository administrators to receive workflow-failure notifications. No 24/7 pager, external monitor, or alert escalation contact is wired. For stronger measurement, an owner should add a provider-independent HTTPS monitor with a 5-minute probe and email alerts after launch, then compare it with Actions probes.

## 2. Architecture, capacity and cost

- Static assets served from the GitHub Pages CDN over HTTPS; build/deploy happens in GitHub Actions.
- Current production build budget: app JavaScript ≤150 KiB gzip, CSS ≤20 KiB gzip. Latest measured app JS: 117.3 KiB gzip; CSS: 4.2 KiB gzip. Images are static and below roughly 175 KiB each in the production build.
- Browser loads the hero image eagerly and lower product-option images lazily. There is no database connection pool, request queue, CPU/RAM reservation, autoscaler, or container cluster to size.
- Capacity is primarily CDN bandwidth and provider quota. No load test has been run; do not load-test GitHub Pages aggressively. Use normal synthetic checks and a controlled, low-rate test against a staging copy if a future dynamic backend is added.
- Hosting can remain no-cost within the public repository/account's current provider limits. A separately registered domain and external monitoring services can cost money. Weekly GitHub artifact backups are retained for 90 days and are not an independent off-provider backup.
- Terraform/Kubernetes/Docker would add operational complexity without managing a real server. Reassess if checkout, payments, inventory, private data or server-side APIs are introduced.

## 3. Monitoring and operational automation

1. `.github/workflows/bitekasa-smoke-check.yml` runs hourly at minute 23 after deployment and can be run manually. It checks 7 production URLs, retries transient HTTP/network errors, records a workflow summary and fails the job if any endpoint remains unavailable.
2. `.github/workflows/bitekasa-pages.yml` type-checks, runs component tests/coverage, builds, checks SEO and bundle budgets, then deploys Pages with least-privilege `pages:write` and `id-token:write` permissions.
3. `.github/workflows/bitekasa-ci.yml` blocks pull requests on failed tests, audit, build or SEO/bundle checks.
4. `.github/workflows/bitekasa-backup.yml` weekly uploads a Git bundle and source/artwork archive; download a copy to an owner-controlled separate provider periodically.
5. Dependabot proposes weekly npm/action updates. Review lockfile diffs, audit result and CI before merging.

**Alert response:** GitHub Actions failure notification → open the failing run → distinguish endpoint failure from runner/scheduler failure → verify the site independently in a browser/phone → follow the incident playbook below. A failed scheduled run is not automatically a user-impacting outage; repeated failures or a user-visible broken page are.

## 4. Incident response

### Severity guide

- **SEV-1:** homepage or all enquiry routes unavailable for >30 minutes; wrong/unsafe published claims; account compromise or exposed private data. Owner reviews immediately during business hours; disable risky functionality or restore previous release.
- **SEV-2:** one service route, navigation, QR path, or contact action broken; analytics misbehaves; accessibility regression blocks key use. Fix or roll back same day.
- **SEV-3:** cosmetic issue, one stale meta description, or noncritical content problem. Track and schedule.

### First response and recovery

1. Record detection time, failing URL, Actions run ID, browser/device and screenshot; redact personal data.
2. Check GitHub Pages/Actions deployment status and latest merged commit. Validate both a direct page URL and assets; a healthy homepage alone does not prove service routes work.
3. If a release caused the problem, revert the specific site change through a reviewed PR and let the Pages workflow deploy the known-good source. Avoid force pushes or manual edits to generated `dist` files.
4. For incorrect contact/offer content, correct the source and redeploy; tell the owner before flyers or QR codes are circulated. If the canonical domain changed, replace affected codes and verify redirects.
5. For unexpected tracking, remove `VITE_GA_MEASUREMENT_ID` from repository Actions variables and redeploy; review analytics/property settings and the visitor-consent flow.
6. Verify home, all service pages, privacy page, robots, sitemap, mobile layout, and enquiry links; record recovery time and any follow-up tasks.
7. For suspected GitHub account compromise, secure the owner account, revoke suspicious sessions/tokens, review collaborators and workflow changes, and restore only from trusted history. Never paste recovery codes into an issue or chat.

## 5. Safe chaos / resilience exercises

Do not inject failure into the public site or stress GitHub's free service. Run these only in a PR/local build:

- Temporarily change one smoke-test URL to a known 404 and confirm the Action fails with a clear summary; restore before merge.
- Temporarily break a service-page canonical or omit a sitemap entry and confirm `check:seo` fails; restore and rerun.
- Temporarily exceed the bundle budget with a test fixture and confirm the size gate fails; restore.
- Practice a rollback using a local temporary branch or a nonproduction PR, then validate the normal Pages workflow path. Do not merge a deliberately broken production deploy.
- Rehearse the account-compromise and analytics-disable steps from the playbook without exposing credentials or collecting real customer data.

## 6. Reliability risks and recommendations

| Risk | Mitigation / owner action |
|---|---|
| Pages not enabled; QR points to an unavailable URL | Merge approved PR, enable GitHub Actions as Pages source, verify live URL and QR before print. |
| Wrong phone, WhatsApp, availability, area, or hours | Owner UAT and a single source-of-truth update before public listings/printing. |
| GitHub Actions/Pages outage is detected late | Add an independent 5-minute monitor and owner alert recipient after activation. |
| Weekly artifact loss/provider account issue | Download backups to a separate owner-controlled provider; maintain two-factor authentication and least-privilege repository access. |
| GA tag loads without valid visitor choice | Current code gates tag injection on consent; test production variable and both accept/reject paths before enabling GA. |
| Large image/content regression | Keep the existing bundle/asset checks; run GTmetrix/Lighthouse on public mobile and desktop after deployment. |
| Future e-commerce increases data/security risk | Do not bolt payments/customer data onto Pages; perform architecture, privacy and threat review first. |

## 7. Post-incident review

No production incident has been observed because production deployment is pending. Use `docs/INCIDENT_POSTMORTEM_TEMPLATE.md` for any future user-impacting event. Record customer impact without personal identifiers, SLI/error-budget effect, what happened, contributing factors, detection/recovery timeline, and blameless actions with owners/dates.

## 8. Operational exit criteria

Before describing the site as production-ready: Pages live at the canonical URL; hourly probes passing for at least 24 hours; owner verifies contacts/offers/service area; QR scan succeeds from a print proof; Search Console sitemap submitted; analytics remains off until owner setup/privacy review; manual mobile/accessibility and post-deploy performance review complete.
