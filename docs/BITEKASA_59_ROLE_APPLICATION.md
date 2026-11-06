# BiteKasa — the 59-role prompt library, applied

**Prepared:** 5 November 2026 · **Branch:** `arena/e9f32386-hotmoon123`
**Scope:** all 58 numbered prompts pasted in the library (1–58), each mapped to BiteKasa's actual position as of today.

> **Numbering note.** The library header says “all 59 prompts”, but only **58** are supplied: Part A is 1–50 and Part B is 51–58. Prompt 59 is missing — section 3.10 records the gap rather than inventing content for it.

---

## 0. The filled context block

The library asks for a “MY CONTEXT” footer after each prompt. This is the BiteKasa version; paste it under whichever role prompt you run.

```text
MY CONTEXT (fill before running):

- What I am doing: BiteKasa — a samosa and spring-roll snack business in
  Accra, Ghana. The digital asset is a five-page static brochure and enquiry
  website plus a print flyer carrying a QR code. Ordering happens in WhatsApp;
  there is no checkout, account, cart, database or payment step.
- My jurisdiction: Ghana. Advertising and food claims: FDA Ghana guidelines for
  advertisement of regulated products. Data: Data Protection Act, 2012 (Act 843).
  Accessibility reference: WCAG 2.2 AA. Business registration and trademarks:
  Registrar General's Department; trademarks via WIPO/RGD.
- My audience/stage: owner-run small food business; beginner-to-intermediate in
  SEO, analytics and cloud tooling; no Google Business Profile yet; no Search
  Console, Bing Webmaster, GA4 or GTmetrix account yet.
- My domain: business + software (static web).
- My specific goal: convert the live site, the flyer and the QR code into repeatable,
  trustworthy WhatsApp enquiries — without claiming results that have not been measured.
- My constraints: free tiers only (GitHub Pages, GitHub Actions); accounts must stay
  owner-controlled; static hosting with no backend, no server headers, no order
  database; two phone lines (0595 638 696, 0552 727 051); Instagram @bitekasa;
  food photography on the flyer is illustrative, not verified product photography;
  Google Business Profile eligibility and service area are unconfirmed.
```

**Commercial facts in use (owner-supplied):** Silver GH₵100 / 30 pieces · Golden GH₵200 / 55 pieces + 500 ml Coca-Cola · Premium GH₵250 / 70 pieces + 1 litre Coca-Cola. Digital palette: red `#A71920`, cream `#F7EEDB`, gold `#D5A12E`; logo keeps the “BITES” subline.

---

## 1. Ground truth this document is built on

Everything below is either live, in the repository, or openly not done. Nothing here is extrapolated.

| # | Fact | State |
|---|---|---|
| G1 | Website live at `https://hotmoon123.github.io/hotmoon123/` over HTTPS | **Live** — owner screenshot; Pages deploy run #2 succeeded (build 24s, deploy 11s) |
| G2 | Five crawlable pages: home, Fried, Unfried, Frozen, privacy + `robots.txt` + `sitemap.xml` | **Live** |
| G3 | CI workflow: locked `npm ci`, typecheck, prod-dependency audit, Pages-base build, bundle budget, SEO/output checks | **Live on `main`** |
| G4 | QA test suite (8 tests), coverage gates, QA test plan, reliability runbook, postmortem template, workflow `v7` bumps | **PR #14 — open, mergeable, not merged** (`arena/d76eec50-hotmoon123`, head `ce31a43`) |
| G5 | Hourly public smoke check + weekly source/history backup artifacts | **Live** |
| G6 | Eight Dependabot PRs open (#6–#13) | **Open, unmerged** |
| G7 | Print-ready QR pack: vector SVG, 2400 px PNG, scan card, corrected flyer with footer band | **Delivered**, decoded with ZXing at 480–1748 px and 0–40° rotation |
| G8 | Google Search Console, Bing Webmaster, GA4, Google Business Profile, GTmetrix | **Not created. Not connected.** GA4 code exists but stays inert without a Measurement ID |
| G9 | Eight directory listings | **Shortlist only.** Nothing submitted |
| G10 | Paper QR scan, owner UAT on real devices, live performance test | **Not done** |

**Status legend used throughout**

| Label | Meaning |
|---|---|
| **DELIVERED** | Artefact exists and is verified in the repo or live site |
| **IN REVIEW** | Finished but sitting in an open PR |
| **PARTIAL** | Some real work exists; the deliverable is incomplete |
| **NOT STARTED** | No artefact |
| **NOT APPLICABLE** | BiteKasa has no such system today; revisit only if the model changes |

**Status roll-up (58 roles):** DELIVERED 3 · IN REVIEW 1 · PARTIAL 23 · NOT STARTED 7 · NOT APPLICABLE 24.

---

## 2. Part A — the 50 SDLC roles

#### 1 · Product Manager — PARTIAL
- **Applied:** the “product” is a five-page brochure plus a WhatsApp hand-off, not an app. The PM question is which enquiry path to invest in next.
- **Have:** live pages, packs and contact sections, sitemap, privacy notice.
- **Next:** a one-page PRD for the order journey — *see pack → tap WhatsApp → prefilled message → owner replies* — with acceptance criteria and one honest success measure (enquiries per week, counted manually).
- **Guardrail:** no conversion rate can be quoted until enquiries are counted.

#### 2 · Project Manager — NOT STARTED
- **Applied:** the programme is “get found, get trusted, get enquiries” across site, listings, flyer and social.
- **Next:** a one-page charter with scope, owners and the release gates already written into the runbook; a five-line risk register (unverified GBP eligibility, illustrative imagery, URL change, single-owner accounts, unmerged PRs).
- **Guardrail:** no Gantt or EVM ceremony for a one-person business; keep it proportionate.

#### 3 · Business Analyst — PARTIAL
- **Applied:** the requirement is “a hungry person in Accra can see the packs, prices and options and start an order in under a minute”.
- **Have:** implicit requirements embodied in the page structure; order workflow notes in `docs/BITEKASA_ORDER_WORKFLOW.md`.
- **Next:** a half-page BRD listing functional requirements (five pages, WhatsApp deep links, tel links, Instagram link) and non-functional ones (WCAG 2.2 AA, mobile-first, no tracking before consent).

#### 4 · System Analyst — PARTIAL
- **Applied:** the system is a static bundle on GitHub's CDN with no runtime dependencies beyond the owner's phone.
- **Have:** build pipeline and output contract enforced in CI (`dist/` file checks).
- **Next:** a context diagram showing browser → GitHub Pages → WhatsApp / phone / Instagram as the only outbound paths. Anything implying a backend should stay out.

#### 5 · Solution Architect — PARTIAL
- **Applied:** architecture is deliberately boring: Vite build, static hosting, no server, no secrets.
- **Have:** hosting decision and its limits documented in `docs/BITEKASA_HOSTING_AND_GROWTH_RUNBOOK.md`.
- **Next:** one Architecture Decision Record — “static hosting over a server” — recording the trade-offs (free, HTTPS, no headers, no order storage) so the decision is not relitigated.

#### 6 · System Designer — PARTIAL
- **Applied:** the design surface is component structure, route structure and the analytics-consent boundary.
- **Have:** `App.tsx`, route per service page, `AnalyticsConsent.tsx` gating script injection.
- **Next:** a short component/data map showing consent state as the only stored visitor state (localStorage), with a rule that no personal data is ever written to the browser or a third party.

#### 7 · UX/UI Designer — PARTIAL
- **Applied:** one job per screen; the visitor must find pack, price and contact without hunting.
- **Have:** flattened cards, real icons, unified radii, no looping motion, keyboard-focusable controls, skip link, cream/red/gold palette, a11y tests.
- **Next:** a five-person usability check on a phone (find the Premium price → tap WhatsApp) and a recorded pass/fail list. Manual screen-reader and zoom testing is still outstanding.

#### 8 · Software Developer — DELIVERED (QA additions IN REVIEW)
- **Applied:** React + TypeScript + Vite, static output, no runtime secrets.
- **Have:** source in `bitekasa-site/`, typecheck and build green, prod-dependency audit clean, bundle budget enforced.
- **Next:** merge PR #14 to bring the tests and coverage gates onto `main` and resolve the eight Dependabot PRs one at a time with CI green.

#### 9 · Frontend Developer — DELIVERED
- **Applied:** responsive, accessible marketing pages with semantic HTML and no client-side tracking by default.
- **Have:** service pages, palette tokens, focus states, reduced-motion handling, 8 component/a11y tests (PR #14).
- **Next:** manual WCAG 2.2 AA pass at 200% zoom and with a screen reader; record what fails rather than assuming a pass.

#### 10 · Backend Developer — NOT APPLICABLE
- **Applied:** there is no backend. Orders are WhatsApp messages; nothing is stored.
- **Revisit if:** BiteKasa ever takes paid orders online — that requires a real backend, payment handling, privacy impact assessment and Act 843 obligations, not a static page.

#### 11 · Full-Stack Developer — NOT APPLICABLE
- **Applied:** no database, no API, no session. Static build only.

#### 12 · Mobile App Developer — NOT APPLICABLE (deliberate)
- **Applied:** the site is already mobile-first; an app would add store accounts, review cycles and update overhead for a brochure.
- **Recommendation on record:** do not build a native app now. Revisit only if repeat ordering volume justifies it.

#### 13 · DevOps Engineer — PARTIAL
- **Applied:** delivery is GitHub Actions; environments are “draft PR” and “main”.
- **Have:** CI, Pages deploy, hourly smoke check, weekly backup, concurrency groups, scoped Pages permissions.
- **Next:** align all workflows on `v7` actions and delete the Node 20 deprecation exposure; add a deploy-failure notification path the owner will actually see (email or GitHub notification), because today a red run is silent.

#### 14 · Site Reliability Engineer — PARTIAL
- **Applied:** the only service indicators that exist without traffic data are availability and deploy success.
- **Have:** proposed SLIs/SLOs, incident steps, rollback-by-revert procedure, postmortem template (PR #14).
- **Next:** after the owner connects a free uptime checker, record real availability; until then the honest statement is “HTTP checks pass, not “99.x% uptime””.

#### 15 · QA Engineer — IN REVIEW
- **Applied:** risk-based testing for a brochure site: links, contact accuracy, mobile rendering, accessibility, deploy integrity.
- **Have:** `docs/BITEKASA_QA_TEST_PLAN.md`, 8 automated tests, coverage 96.05% lines / 71.73% branches, release gates (PR #14).
- **Next:** merge, then execute the manual matrix on two real phones and record results — the automated suite cannot see a wrong phone number.

#### 16 · Automation Test Engineer — PARTIAL
- **Applied:** component-level automation only; no browser E2E.
- **Have:** Vitest + Testing Library + jest-axe, coverage thresholds, CI reporting.
- **Next:** a single Playwright smoke test against the built `dist` (home loads, three service links resolve, WhatsApp href correct) would catch the failures that matter most.

#### 17 · Performance Test Engineer — NOT STARTED
- **Applied:** static site, so targets are Core Web Vitals and transfer size, not load tests.
- **Have:** compressed bundle budget gate in CI.
- **Next:** after the URL is final, one GTmetrix or Lighthouse run per page on a throttled mobile profile; record LCP/CLS/INP and the top three fixes. No score promise.

#### 18 · Security Engineer — PARTIAL
- **Applied:** threat surface is the repository, the workflow tokens and the owner's accounts — not a server.
- **Have:** HTTPS enforced, least-privilege Pages permissions, Dependabot, prod-dependency audit in CI, no secrets in client code.
- **Next:** a half-page threat model (account takeover, malicious dependency, workflow tampering) plus 2FA confirmation and a review of who has write access.

#### 19 · Information Security Engineer — PARTIAL
- **Applied:** the only personal data is what customers send by WhatsApp; the website must not collect more.
- **Have:** privacy notice, consent-gated analytics, no form fields, no cookies until consent.
- **Next:** confirm the privacy notice names the owner as data controller, the WhatsApp/phone retention practice, and how a deletion request is handled under Act 843.

#### 20 · Cybersecurity Engineer — NOT APPLICABLE (for now)
- **Applied:** no SIEM, no detection stack, no attackers with motive beyond opportunistic account attacks.
- **Next best action:** account hygiene — 2FA, no shared passwords, review collaborator list monthly.

#### 21 · Database Administrator — NOT APPLICABLE
- **Applied:** no database exists.

#### 22 · Data Engineer — NOT APPLICABLE
- **Applied:** no pipelines, no warehouse, no analytics history.

#### 23 · Machine Learning Engineer — NOT APPLICABLE
- **Applied:** no model, no training data, no personalisation.

#### 24 · Data Scientist — NOT APPLICABLE
- **Applied:** there is no data set yet. Any “best-selling pack” claim today would be invented.
- **Revisit if:** GA4 consent is on and 8–12 weeks of enquiry data exist.

#### 25 · System Administrator — NOT APPLICABLE
- **Applied:** no servers to patch. The nearest equivalent is keeping dependencies current — that is CI and Dependabot, not sysadmin work.

#### 26 · Network Engineer — NOT APPLICABLE
- **Applied:** GitHub Pages terminates TLS and serves through GitHub's CDN. No DNS, VLAN or firewall under BiteKasa's control.

#### 27 · Computer Network Engineer — NOT APPLICABLE
- **Applied:** same reason as 26.

#### 28 · Cloud Engineer — NOT APPLICABLE (by design)
- **Applied:** one managed static host, zero billable resources, no IaC justified. Cost review: free tier only; the material cost risk is a future custom domain renewal, not compute.

#### 29 · Platform Engineer — NOT APPLICABLE
- **Applied:** one small site, one maintainer. Golden paths and IDPs would be overhead.

#### 30 · Embedded Systems Engineer — NOT APPLICABLE
- **Applied:** no firmware, devices or sensors.

#### 31 · Hardware Engineer — NOT APPLICABLE
- **Applied:** no boards or enclosures. The only physical artefact is printed paper (flyer, QR proof).

#### 32 · Electrical/Electronics Engineer — NOT APPLICABLE
- **Applied:** no electrical design work.

#### 33 · Computer Architect — NOT APPLICABLE
- **Applied:** no ISA, pipeline or memory hierarchy work.

#### 34 · Systems Engineer — PARTIAL
- **Applied:** the “system” is site + flyer + QR + social + phone lines. Interfaces between them are the weak point.
- **Have:** URL consistency enforced in CI (`grep` for the Pages URL in built HTML); QR pack encoding the same URL.
- **Next:** one interface control sheet: URL, phones, Instagram handle, prices, pack contents — the single list every asset must match. A price change must update site, flyer, QR landing text and social in one pass.

#### 35 · Systems Thinker — PARTIAL
- **Applied:** enquiries depend on a loop — visibility → trust → contact → fulfilment → word of mouth → visibility.
- **Next:** a one-page causal map identifying the current binding constraint (probably visibility, not the website) so effort goes where the loop is broken rather than into more site polish.

#### 36 · Design Thinker — NOT STARTED
- **Applied:** no structured empathy work with actual customers.
- **Next:** five short customer conversations (what they order, when, how they hear about snacks, what stops them ordering) recorded as notes. This is also the input the PM and marketing roles are missing.

#### 37 · Mathematician — NOT APPLICABLE
- **Applied:** no modelling or proof work. The only arithmetic in scope is pack economics (price per piece), which belongs to the accountant.

#### 38 · Scientist — NOT APPLICABLE
- **Applied:** no research programme. Small-n customer conversations are design research precedent (36), not science.

#### 39 · Psychologist — NOT APPLICABLE
- **Applied:** no assessment, counselling or clinical work.

#### 40 · Physician — NOT APPLICABLE
- **Applied:** nothing clinical. Note for adjacent risk: food advertising claims and any health-adjacent wording fall under FDA Ghana advertising guidance, not medicine.

#### 41 · Researcher — PARTIAL
- **Applied:** competitive and audience research for a snack business in Accra is thin.
- **Next:** a light competitor sweep (who sells samosas nearby, at what price, on which channels) with sources and dates, feeding the marketing and brand roles. No fabricated market-size figures.

#### 42 · Reverse Engineer — NOT APPLICABLE
- **Applied:** no binaries or third-party protocols in scope; and lawful-analysis constraints make this irrelevant to a brochure site.

#### 43 · Technical Writer — DELIVERED
- **Applied:** owner-facing documentation is the real deliverable: runbooks, QA plan, QR print rules.
- **Have:** `BITEKASA_HOSTING_AND_GROWTH_RUNBOOK.md`, `BITEKASA_ORDER_WORKFLOW.md`, `BITEKASA_INSTAGRAM_POST_PACK.md`, site README, QR README, postmortem template.
- **Next:** a single “start here” index so the owner is not hunting across seven documents.

#### 44 · Scrum Master — NOT APPLICABLE
- **Applied:** one owner, no sprint cadence, no team to facilitate. Forcing Scrum here would produce ceremony without value.

#### 45 · Agile Coach — NOT APPLICABLE
- **Applied:** same. The useful Agile residue is small batch changes through PRs (see 48).

#### 46 · Release Manager — PARTIAL
- **Applied:** a release is a merged PR plus a green Pages deploy.
- **Have:** deploy workflow, release-gate wording, rollback-by-revert procedure.
- **Next:** a two-line release note per deploy (what changed, where to verify) so the owner can point at a date if something looks wrong.

#### 47 · Configuration Manager — PARTIAL
- **Applied:** Git history is the configuration item register; the built `dist/` is disposable.
- **Have:** protected-ish `main`, PR-only changes, backup bundle + source archive weekly.
- **Next:** a one-page register of the things that must match (URL, phones, prices, handles) with owner and last-verified date — the same list as role 34.

#### 48 · Change Manager — PARTIAL
- **Applied:** every website change is a reviewed PR; the “CAB” is the CI gate.
- **Have:** PR workflow, required checks, concurrency control.
- **Next:** an emergency path for wrong contact details, since a wrong phone number is the worst realistic incident and must not wait for a review queue.

#### 49 · Incident Manager — PARTIAL
- **Applied:** realistic incidents are site down, wrong contact details live, wrong price live, unexpected tracking, account compromise.
- **Have:** response steps and severities sketched in the reliability runbook (PR #14).
- **Next:** a single A4 incident card with those five scenarios, first action, and who to tell. No production incident has occurred, so this is preparation, not reporting.

#### 50 · Problem Manager — NOT STARTED
- **Applied:** no recurring incident history exists to analyse.
- **Next:** a known-error table with one honest, empty state; populate it only from real incidents.

---

## 3. Part B — the business roles (51–58) and the gap at 59

#### 51 · Business Manager — PARTIAL
- **Applied:** the business runs on owner time, two phones and a kitchen; the website supports it, it does not run it.
- **Have:** clear pack structure, prices, contact routes, ordering workflow.
- **Next:** a one-page operating plan — what gets checked weekly (enquiries, stock, site up, any new review), monthly (prices, listings, backups) and quarterly (brand, directory accuracy). No P&L is published here because none has been supplied.

#### 52 · Business Administrator — NOT STARTED
- **Applied:** the gaps are records and evidence — who was told what, when prices last changed, which listings exist.
- **Next:** three lightweight registers: obligations (FDA advertising check, Act 843 privacy notice, business registration), directory/listing status, and asset version (which flyer/QR is current). Proportional controls only.

#### 53 · Marketing Manager — PARTIAL
- **Applied:** brand-aware, demand-focused marketing for a small food business: packs, prices, WhatsApp call to action.
- **Have:** owner-approved branding, flyer, Instagram post pack (`docs/BITEKASA_INSTAGRAM_POST_PACK.md`), consistent WhatsApp CTA, QR assets.
- **Next:** a 30-day content calendar with five content pillars drawn from real product facts only, plus the channel plan (Instagram, WhatsApp status, flyer/QR, local directories, word of mouth). No fabricated followers, reviews or testimonials.

#### 54 · Sales Manager — NOT STARTED
- **Applied:** sales = WhatsApp conversations. There is no pipeline tooling and no qualification framework worth installing.
- **Have:** order workflow notes (enquiry → confirm pack → confirm collection/delivery → payment arrangement).
- **Next:** a five-line enquiry script and objection answers (availability, lead time, delivery, allergens) that the owner actually agrees with, plus a simple tally of enquiries and confirmed orders per week.

#### 55 · Accountant — NOT STARTED
- **Applied:** pack economics are the relevant slice — price per piece (GH₵3.33 / GH₵4.00 / GH₵3.57), Coca-Cola bundle value, and contribution after ingredient and packaging cost.
- **Next:** a one-page unit-economics sheet the owner can maintain in a spreadsheet, plus a simple sales/expenses log. No IFRS discussion: this is a micro-business, not a reporting entity.

#### 56 · Entrepreneur — PARTIAL
- **Applied:** opportunity is validated only by actual repeat orders — not by a live website.
- **Have:** live site, flyer, QR, brand assets, pack ladder (Silver → Golden → Premium as an upsell path).
- **Next:** a lean canvas with the honest evidence column mostly empty, plus one validation experiment: 20 flyers with the QR handed to existing customers and a count of scans/enquiries. That is the first real traction data point.
- **Guardrail:** the site being live is not traction. Say “the site is live”, never “the website is working”.

#### 57 · Brand Manager / Brand Strategist — PARTIAL
- **Applied:** three layers already partly exist — strategy (packs, tone), identity (logo with “BITES”, palette, typography), experience (site, flyer, WhatsApp).
- **Have:** logo, red `#A71920` / cream `#F7EEDB` / gold `#D5A12E`, tagline “hot · crispy · fresh”, consistent radii and icon style.
- **Next:** a one-page brand sheet: positioning sentence, three values with observable behaviours, do/don’t on imagery (including “illustrative, not verified product photography”), voice rules for WhatsApp replies. Trademark clearance remains owner/ counsel work, not a claim to make here.

#### 58 · Social Media Manager / Influencer — PARTIAL
- **Applied:** Instagram `@bitekasa` is the main discovery channel; WhatsApp is the conversion channel.
- **Have:** post pack, 4:5 and 9:16 artwork, QR variants, consistent handle and palette.
- **Next:** a 14-day content calendar from the post pack, a reply playbook for DMs, and a compliance line: paid partnerships must be disclosed; no invented reviews, engagement or results. Creator selection, if it ever happens, is on audience fit — not follower count.

#### 59 · Missing prompt — documented gap
- The library promises 59 prompts but supplies 58. Rather than back-filling an invented role, this entry stays open. If the missing prompt is a role BiteKasa needs (for example **Customer Support** or **Food Safety / HACCP**), send it and it gets the same treatment — and food safety is the one genuinely missing discipline for a snack business.

---

## 4. Consolidated action register

Priority is about consequence: **P0** = do before printing, distributing or claiming anything public.

| ID | Action | Why now | Owner | Done when |
|---|---|---|---|---|
| A1 | Merge PR #14 (QA docs, tests, coverage gates, `v7` actions) | The QA/reliability work is finished but not on `main`; the live CI is still the older version | Owner | PR merged, CI green on `main` |
| A2 | Resolve the eight Dependabot PRs one at a time | Unmerged bumps accumulate security drift | Owner | PRs closed/merged with green CI |
| A3 | Confirm both phone numbers and which one is the official WhatsApp account | A wrong number on a printed flyer is the worst realistic failure | Owner | Confirmed in writing; site + flyer match |
| A4 | Print one flyer at final size and scan the QR with two phones | Software decoding is not paper proof | Owner | Both scans open the live site |
| A5 | Decide Google Business Profile eligibility (storefront vs service-area) | Nothing can be created honestly until this is answered | Owner | Written decision; no invented address |
| A6 | Create owner Google account → Search Console URL-prefix property → verify → submit sitemap | The site is live but not submitted to search | Owner | Verification succeeded, sitemap accepted |
| A7 | Same URL in Bing Webmaster (import from Search Console if offered) | Second search surface, near-zero effort after A6 | Owner | Property verified |
| A8 | Confirm the advertising/claims position for the food and Coca-Cola bundle offer | Ghana FDA advertising guidance applies to food offers | Owner | Guidance checked, wording agreed |
| A9 | Review the privacy notice against Act 843 (controller, retention, deletion) | The site handles enquiries even without collecting data | Owner | Notice updated and dated |
| A10 | Decide GA4: on (consented) or off | Measurement cannot be retrofitted | Owner | Decision recorded; Measurement ID set only if “on” |
| A11 | Run GTmetrix/Lighthouse on the final URL, home + three service pages | No live performance evidence exists yet | Owner/agent | Report URL, date, LCP/CLS/INP recorded |
| A12 | Submit at least eight free listings from the verified shortlist | Requested scope; nothing is submitted | Owner | Eight entries with URL, date, verification state |
| A13 | Manual WCAG 2.2 AA pass (200% zoom, screen reader, keyboard) | Automated axe tests are not a conformance claim | Owner/agent | Pass/fail list recorded |
| A14 | Add one Playwright E2E smoke test against built `dist` | Catches broken links and wrong hrefs that unit tests miss | Agent | Test in CI, green |
| A15 | One-page brand sheet + interface control list (URL/phones/prices/handles) | Keeps site, flyer, QR and listings from drifting | Agent | Document committed |
| A16 | 30-day content calendar from the Instagram post pack | Marketing exists as assets, not as a schedule | Agent | Calendar committed |
| A17 | Five customer conversations recorded as notes | The missing input for PM, marketing and design work | Owner | Notes captured |
| A18 | One-page unit economics (price per piece, bundle value, contribution) | Needed before discounting or upsizing | Owner/agent | Sheet committed |
| A19 | Five-line WhatsApp enquiry script + objection answers | Fastest lever on conversion | Owner | Agreed wording in use |
| A20 | Start-here documentation index | Seven documents, no front door | Agent | `docs/BITEKASA_START_HERE.md` |
| A21 | Weekly release note line per deploy | Gives the owner a date to point at | Agent | Template in runbook |
| A22 | Emergency change path for wrong contact details | Realistic worst case | Agent | Steps in runbook |
| A23 | Incident card (five scenarios, A4) | Preparation, not posture | Agent | Committed |
| A24 | Uptime checker (free tier) once traffic matters | Real availability data instead of assertions | Owner | Monitor live, alert path tested |
| A25 | Custom domain decision (keep GitHub URL vs buy one) | Changes QR, canonical URLs, Search Console property | Owner | Decision recorded before printing |

---

## 5. Claims discipline

The most common failure in a document like this is writing down ambitions as achievements. This table is binding.

| Say this | Not this |
|---|---|
| “The website is live at …” | “The website is launched and being found on Google.” |
| “The site is submitted to GitHub Pages and the deploy is green.” | “The site is monitored 24/7 with 99.9% uptime.” |
| “Automated tests pass (8/8) and coverage gates exist.” | “The site is fully QA-approved.” |
| “A QR code is generated and decodes in software testing.” | “The printed QR code is verified.” |
| “Eight directory destinations are shortlisted.” | “We are listed in eight directories.” |
| “Google Business Profile requires an eligibility decision.” | “The business profile is set up and linked.” |
| “Images are illustrative.” | Presenting generated food imagery as BiteKasa product photography |
| “Analytics is consent-gated and currently off.” | “Website traffic is being tracked.” |
| “Free static hosting meets the current need.” | Implying a backend, checkout or order database exists |

---

## 6. How to run any prompt from here

1. Paste the role prompt exactly as supplied in the library.
2. Append the **BiteKasa context block** from section 0.
3. Append the matching role entry from sections 2–3 as the “current state” — that is what stops the model inventing progress.
4. Constrain the output: ask for the single next deliverable in the action register, in one page.

**On Bloom levels.** The prompts ask for L1–L6. BiteKasa realistically sits at **L1–L3** (`remember → understand → apply`) for SEO, analytics and listings, and **L4** (`analyse`) at most for QA. L5–L6 outputs — portfolio strategy, organisational transformation, causal inference on campaign data — have no data underneath them yet. Requesting them produces impressive-looking fiction. They become legitimate after A6, A10, A11 and A12 produce real numbers.

**Roles that should stay switched off:** all twenty-four entries marked **NOT APPLICABLE** — backend, full-stack, mobile app, cybersecurity operations, DBA, data engineering, ML, data science, sysadmin, both network roles, cloud, platform, embedded, hardware, electrical, computer architecture, mathematician, reverse engineering, Scrum Master, Agile Coach, psychologist, physician, scientist and security-operations defence. Twenty-four of the fifty-eight prompts describe systems BiteKasa does not have. Applying them would mean building architecture to justify the role, which is the opposite of what a snack business needs.
