# BiteKasa QA plan and test summary

**Version/date:** 1.0 · 5 November 2026
**Scope:** public-facing static React site, linked service pages, contact links, optional analytics consent, SEO/discovery files, CI build and deployment artifacts.
**Release status:** automated checks pass locally and PR CI passed before the QA suite was added; a new CI run is required after this test-suite change. Production/UAT sign-off is **pending** because GitHub Pages is not live and owner contact/business facts are unverified.

## 1. Quality objectives

- Preserve the advertised offer facts: Silver GH₵100/30 pieces; Golden GH₵200/50 pieces + 500 ml Coca-Cola; Premium GH₵250/70 pieces + 1 litre Coca-Cola.
- Make the home, fried, unfried, frozen, and privacy pages resolve and navigate correctly under the GitHub Pages repository path.
- Verify enquiry links, illustrative-image labeling, reduced-motion-compatible UI, and analytics opt-in behavior.
- Prevent bad releases with typecheck, component tests, production dependency audit, page/SEO checks, and compressed bundle budgets.
- Do not publish unverified contact, location, availability, health, food-safety, or product-photo claims.

## 2. Test strategy and environments

### Automated layers

1. **Static/metadata checks:** `npm run check:seo` checks unique titles, descriptions, canonicals, sitemap entries and robots sitemap reference.
2. **Unit/component tests:** Vitest + React Testing Library + jsdom run in CI; test-only GA ID is `G-TEST000000`, never used by production builds.
3. **Build/integration checks:** Node 22 `npm ci`, TypeScript check, production audit, GitHub Pages-base build, output-file checks and gzip-size budgets.
4. **Deployment smoke probes:** hourly GitHub Actions checks of the live URL after activation. These are synthetic HTTP checks, not browser rendering or a provider-independent uptime monitor.

### Manual/UAT layers still required

- Current Chrome, Safari and Firefox; Android/iOS layout and navigation; keyboard-only and screen-reader spot checks.
- Real phone/WhatsApp/Instagram destinations and owner-supplied copy.
- Search Console/Bing verification, GA4 realtime after consent, Google Business Profile eligibility and published listing review.
- QR scan from physical print proof; GTmetrix/Lighthouse and mobile network performance after production deployment.

### Test data and boundaries

- Pack labels, prices and quantities use owner-approved values; the exact food mix and conditions covered by each price remain unconfirmed.
- Generated images are illustrative only.
- WhatsApp number and both phone numbers are provisional until the owner verifies them.
- No payment, order submission, inventory or customer-data backend exists; these flows are not tested as product features.
- Test-only analytics ID is non-production. Never put credentials or private tokens in tests, source, Vite variables, or issue comments.

## 3. Risk-based test cases

| ID | Priority | Test | Expected result | Automation/status |
|---|---|---|---|---|
| BK-QA-001 | P0 | Render home page | Main heading, all three exact packs, and contact actions are present | Vitest component test; pass |
| BK-QA-002 | P0 | Follow each preparation link | Fried, unfried and frozen cards point to their dedicated path | Vitest component test; pass |
| BK-QA-003 | P0 | Render dedicated frozen page | Correct heading, related-service cross-links, packs link and availability caveat appear | Vitest component test; pass |
| BK-QA-004 | P0 | First visit with GA configured | Consent appears; Google tag is absent before choice | Vitest component test; pass |
| BK-QA-005 | P0 | Reject analytics | Rejection persists; no Google tag is appended | Vitest component test; pass |
| BK-QA-006 | P0 | Accept analytics | Acceptance persists; tag uses configured test measurement ID | Vitest component test; pass |
| BK-QA-006A | P1 | Mobile navigation | Menu opens, reports expanded state and closes on Escape | Vitest component test; pass |
| BK-QA-006B | P1 | Automated accessibility smoke | Axe finds no semantic/accessibility violations in home markup; color contrast remains a manual/browser check | Vitest + axe-core; pass |
| BK-QA-007 | P0 | TypeScript validation | No type errors | `npm run typecheck`; pass |
| BK-QA-008 | P0 | Clean dependency install and dependency audit | Lockfile install succeeds; no high/critical dependency findings | `npm ci`, `npm audit --audit-level=high`; pass locally, 0 vulnerabilities |
| BK-QA-009 | P0 | GitHub Pages build | Root and three service-page HTML outputs use the repo-path base | Vite production build + CI output checks; pass locally |
| BK-QA-010 | P1 | SEO metadata/sitemap | Every declared page has unique title/description/canonical and sitemap entry | `npm run check:seo`; pass locally |
| BK-QA-011 | P1 | Bundle budgets | Gzipped app JS ≤150 KiB and CSS ≤20 KiB | `npm run check:bundle`; pass: 117.3 KiB JS, 4.2 KiB CSS |
| BK-QA-012 | P1 | QR payload | Standalone and three artwork QR codes decode to the intended GitHub Pages URL | ZXing decode; pass. Live destination/print proof pending |
| BK-QA-013 | P0 | Public availability | All public pages and discovery files return HTTP 200 over HTTPS | Hourly scheduled action after launch; not yet measurable |
| BK-QA-014 | P0 | Phone, WhatsApp and social destinations | Owner confirms numbers/account ownership and links open the intended account | Manual UAT; blocked on owner verification |
| BK-QA-015 | P1 | Responsive/keyboard/accessibility | Layout, focus, menu state, contrast, reduced motion and alt text work on real devices | Manual UAT; pending |
| BK-QA-016 | P1 | Search engine ownership and crawl | Search Console/Bing verify and accept sitemap; canonical URLs match production | Manual external setup; pending |
| BK-QA-017 | P1 | Performance and print | GTmetrix/Lighthouse reviewed; QR scans from final-size print proof | External/manual; pending live deployment |

## 4. Execution summary

Latest local execution after the changes:

- `npm run typecheck`: **pass**.
- `npm run test:coverage`: **8/8 component/accessibility tests pass**.
- Coverage: **96.05% lines, 92.04% statements, 96.87% functions, 71.73% branches** for `App.tsx` and `AnalyticsConsent.tsx`; configured gates are 85/80/75/50 respectively.
- `npm audit --audit-level=high`: **pass, zero vulnerabilities across the dependency tree**.
- GitHub Pages build, `check:bundle`, `check:seo`, QR decode and local route smoke: **pass**.
- GitHub Actions PR validation is configured in this revision; verify the latest required check on the pull request before merge.
- Public deployment, browser matrix, accessibility audit, GTmetrix, real contact verification, and Search Console/Bing validation: **not run**; see launch gates.

## 5. Defect reporting and triage

Track defects as GitHub Issues using labels `bug`, `accessibility`, `security`, `content`, and severity `P0`–`P3`. Include environment/browser, route, reproducible steps, expected/actual result, screenshot/log with private data removed, and regression-test link. Do not place credentials or customer communications in issues.

No application defect was found by the current automated suite. The following are **release blockers / owner actions**, not misreported code bugs:

1. GitHub Pages enablement/deploy remains pending (repository settings API permission was insufficient); merge the PR and select **Settings → Pages → GitHub Actions**.
2. Verify the published URL before using QR artwork.
3. Owner must verify phone/WhatsApp details, current offers and business profile eligibility/area.
4. Complete Google/Bing property verification, GA4 account setup, listing submissions and privacy review.

## 6. Release entry/exit criteria

**Entry:** source reviewed; owner-approved offer details retained; dependency lockfile present; no live tracking ID in tests.
**Exit:** CI green; Pages deployed; routes and QR destination checked over HTTPS; owner validates all contacts and claims; Search Console sitemap submitted; privacy/analytics settings reviewed; manual mobile/accessibility checklist signed. Do not represent the current state as full QA sign-off until all exit criteria are met.

## 7. CI integration

`.github/workflows/bitekasa-ci.yml` runs clean install, typecheck, component coverage tests, production dependency audit, Pages build, SEO metadata check, compressed bundle budget and output validation on PRs. Coverage HTML/JSON is retained as a 30-day Actions artifact. The deployment workflow repeats critical validation before publishing.
