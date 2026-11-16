# BiteKasa — case study

**One line:** a static ordering site for a Ghanaian samosa and spring-roll business, built to
explicit size, accessibility and honesty constraints, published free on GitHub Pages.

- **Live:** https://hotmoon123.github.io/hotmoon123/
- **Source:** `bitekasa-site/` in this repository
- **Status:** live and used as the business's link-in-bio destination
- **Document version:** 1.0, 13 November 2026

---

## 1. The brief, as given

1. One page that answers three questions: what is it, how much is it, how do I order.
2. No backend, no payments, no database, no accounts. Orders arrive on WhatsApp.
3. Free static hosting only.
4. Food imagery must be labelled as illustrative, never passed off as product photography.
5. Ghanaian consumer-protection and advertising practice; WCAG 2.2 AA as the accessibility target.

The constraint that shaped everything: **there is no server.** Every decision below follows from
that, not from preference.

---

## 2. What was built

| Surface | What it does |
|---|---|
| Home | Hero, three packs with fixed prices, order builder, how-it-works, preparation options, questions, contact |
| `/services/fried/` · `/unfried/` · `/frozen/` | One page per preparation option, indexable in search |
| `/privacy.html` | Plain-language privacy notice — no cookies, no accounts, nothing stored |
| Order builder | Quantities → running total → one tap opens WhatsApp with a pre-filled order message |
| Brand splash | One-time animation, skippable by tap, Enter, Space or Escape; suppressed for reduced-motion users and returning visitors |
| Discovery files | Favicons, web manifest, sitemap, robots |

Nothing in the build collects, transmits or stores personal data. The order leaves the site as a
`wa.me` deep link the customer sends themselves.

---

## 3. Engineering decisions that shaped it

**Static, deliberately.** No server means nothing to breach, nothing to pay for monthly, and
nothing to patch. On free GitHub Pages this costs GH₵0 to run.

**Budgets enforced in CI, not aspirational.** The build fails if JavaScript exceeds 150 KiB gzip
or CSS exceeds 20 KiB gzip. Current: **122.1 KiB** and **7.6 KiB**.

**Motion that confirms, never decorates.** Durations of 140/180/240 ms, transform and opacity
only, a 60 ms stagger across three cards, and every value zeroed under `prefers-reduced-motion`.
The motion language is documented in `docs/DESIGN_SYSTEM.md`.

**Honesty enforced by construction.** Illustrative images are labelled in their alt text and in
visible captions. There are no reviews, no star ratings, no invented statistics and no urgency
timers — because none of those could be substantiated.

---

## 4. Verified at the time of writing

Re-run from a clean install on 13 November 2026:

| Check | Result |
|---|---|
| Type-check (`tsc --noEmit`) | clean |
| Automated tests | **35 / 35 passed** across 5 files |
| JavaScript budget | **122.1 KiB / 150 KiB** gzip |
| CSS budget | **7.6 KiB / 20 KiB** gzip |
| SEO metadata and sitemap | **5 / 5** |
| Dependencies (`npm audit --audit-level=high`) | **0 vulnerabilities** |
| Deployment | GitHub Pages workflow green |

---

## 5. What this case does **not** claim

Stated plainly, because a case study that overstates is worse than none:

- **No sales, revenue or conversion figures.** None have been measured.
- **No follower growth or reach figures** attributed to this site.
- **No third-party accessibility audit.** Built to WCAG 2.2 AA practice — focus states, 44 px
  touch targets, labelled images, reduced-motion handling — but not certified by anyone.
- **No field performance claim** on low-end Android hardware. The budgets are measured on the
  build, not on real user devices.
- **No claim that the food photographs are real product photography.** They are illustrative and
  labelled as such throughout.

---

## 6. Permission

The site is BiteKasa's own, and the work was done for and with the business.

- Portfolio use authorised by: ________________________  Date: ____________
- If BiteKasa is **your own business**, you are the client — record that here.
- If it is a **third party's**, obtain written consent before this document or any recording of it
  is shown to anyone else. A message saying "yes, you can show it" is enough, kept as a screenshot.

---

## 7. What this case is useful for

It demonstrates, with evidence a sceptical reader can check:

- shipping a production site against **enforced** budgets rather than stated goals;
- designing under a hard constraint (no backend) instead of adding infrastructure to avoid one;
- accessibility and reduced-motion handled as architecture, not as a patch;
- refusing to fabricate reviews, ratings or urgency — and writing that refusal down.

That last point is the one most portfolios cannot show.
