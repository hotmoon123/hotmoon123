# SoftFire — site notes

Static one-page site. No build step, no framework, no dependencies,
no third-party request of any kind.

```
docs/softfire/
├── index.html          10 sections, one page, incl. six filled-in documents
├── tokens.css          four tiers — primitive → semantic → component → layout
├── styles.css          22 numbered blocks, incl. a print sheet
├── app.js              6 islands: crawlers · rail · carousel · brief ·
│                          motion toggle · year
└── assets/
    ├── inter-latin-var.woff2              47 KB, weights 100–900
    ├── jetbrains-mono-latin-var.woff2     40 KB, weights 100–800
    ├── sf-mark.svg       transparent SF, used by the crawler field
    ├── favicon.svg       32×32, Tier C
    ├── logo-a-dark.svg   Tier A — gradient on charcoal, ≥64px cap
    ├── logo-a-light.svg  Tier A — gradient on cream (paper only)
    ├── logo-b.svg        Tier B — two colour, 24–63px
    └── logo-c.svg        Tier C — one colour, ≤24px and all print
```

## Run

```bash
python3 -m http.server 8000 --directory docs/softfire
```

## Deploy — free, either way

| Route | Address |
|---|---|
| GitHub Pages, source = this folder | `hotmoon123.github.io/softfire/` |
| Netlify / Vercel drag-and-drop | `softfire.netlify.app` |

All links are relative. A domain later prepends to the same files and
nothing in them changes.

## Measured

| | Budget | Shipped |
|---|---|---|
| JS, gzip | 180 KB | **4.4 KB** |
| CSS, gzip (both files) | — | **17.0 KB** |
| HTML, gzip | — | **16.6 KB** |
| Fonts | — | **87 KB**, self-hosted, 2 files |
| Third-party requests | 0 | **0** |
| Above-the-fold images | 0 | 0 |
| `backdrop-filter` regions | — | **1** (the sticky header only) |
| Horizontal overflow at 320/390/430/480/768/1024/1280/1440 | none | **none** |
| Controls under 44 px, all widths | 0 | **0** |

## The crawler field

Requirement: 8–12 columns of bottle-cap-sized SF marks, adjacent
columns moving in opposite directions, continuous.

- **12 DOM nodes**, one per column (8 painted under 768 px). Each holds
  its marks as a single `translate3d` track, 46 s, linear, infinite.
  JS builds 9 marks and duplicates them so the −50 % loop seam is
  invisible.
- **A grid, not a flex row.** The first version used `flex: 1 1 0` with a
  64 px gap; on a 390 px phone the twelve columns needed 1,412 px, so each
  compressed to **2.75 px** and the field was invisible for the entire
  build. Equal grid tracks cannot collapse.
- **No `backdrop-filter` over the crawlers.** Glass is layered alpha
  surfaces with a 1px inset highlight instead. The single
  `backdrop-filter` is the sticky header, over static content.
- **Opacity .03, not .055.** With the field actually painting, .055 made
  body copy compete with the marks. It is texture, not a pattern to read.
- **Stoppable.** WCAG 2.2.2: the crawl exceeds five seconds and cannot be
  paused by hover, so the footer carries a Pause control. It is remembered
  in `sessionStorage` and applied *before first paint*, so a return
  visitor never sees a frame of motion they opted out of.
- `prefers-reduced-motion: reduce` → `animation: none`, and the toggle
  starts in the pressed state.
- `pointer-events: none`, `aria-hidden="true"`, masked top and bottom.

**If you ever add a blurred region over the crawlers, expect the frame
rate to collapse.** That is the one rule this file exists to record.

## The gamified brief

Four steps, one question per screen, choices as pressable cards.

- **Nothing is stored, with one deliberate exception.** The four brief
  answers never touch localStorage, a cookie or the network — they live
  in memory and vanish when the tab closes. The *motion preference* is
  written to `sessionStorage` under `sf-motion`. It is not sent anywhere
  and it expires with the tab.
- **Nothing is sent** until the person presses the WhatsApp link.
- The send control is a real `<a href>` with a `?text=` parameter. Only
  the *composed* message needs JS; the link itself does not.
- "Start again" clears the composed message and the link as well as the
  answers, so the next person does not inherit them.
- Progress is `1 / 4` with a bar, not a percentage — a percentage of four
  is noise.

## Accessibility

- WCAG 2.2 AA. Every colour pair and its measured ratio is recorded in
  `tokens.css`.
- **Control borders are 3:1, not hairline.** `.iconbtn`, inputs, the
  rail's CTA and the brief's choice cards all use `--border-control`
  (cream 38 % on charcoal = 3.16). At the original 28 % these measured
  2.28 and failed 1.4.11.
- **Placeholders are 4.93:1.** The original 45 % cream measured 3.36 —
  below 4.5, and a placeholder is text.
- Skip link is the first focusable element, moves into view on focus with
  `transform` only (not `top`), and is *not* `visibility: hidden` — that
  removes it from the tab order and defeats it.
- Every control ≥ 44×44 at every breakpoint, verified by script.
- Carousel: arrow keys, Enter/Space on side cards, swipe, `aria-live`
  counter. Below 1024 px the side cards are hidden rather than cramped.
- Brief: focus moves to each step heading on change.
- `lang="en-GH"`; headings descend h1 → h2 → h3 with no skipped level.

## The six documents — and where every fact comes from

`#documents` does not describe six planning documents. It prints them, filled
in for **BiteKasa**, the one project SoftFire has shipped. This follows the
guide's own instruction (*"each one filled in, so you can see what good looks
like"*) and page 08's six-box check, which is reproduced verbatim at the end.

Nothing in that section is invented. Every factual claim traces to a file in
this repository:

The data sheet (05) now covers **two** systems, because the two are genuinely
different cases: BiteKasa stores nothing, and the Rent & Lease system holds
real financial records. That second table is the one that matters, and every
row in it comes from the Django models in this repo.

### Diagrams

Document 03 and 05 each carry a real diagram, drawn in the notation the
corpus supplied (six-shape flowchart: oval start/end, rectangle action,
diamond decision, parallelogram input, small circle connector, arrow):

- **App flow** — `flow-svg`, the BiteKasa customer journey including the
  "no" branch back to the packs and the "call instead" escape hatch.
- **Sequence** — `seq-svg`, six numbered messages across four lifelines,
  showing that the payment gateway holds the card and this system holds
  only a reference. Solid arrow = request, dashed = reply.

Both are inline SVG with `<title>` and `<desc>`, so a screen reader reads the
whole flow as prose. Every node is distinguished by **shape as well as
colour** — the diagram survives a monochrome screen or forced-colors mode.

| Claim in the document | Source file |
|---|---|
| Silver 30 pcs / Golden 50 + 500 ml / Premium 70 + 1 L | `bitekasa-site/src/App.tsx`, `PACKS` |
| Phone numbers 0595 638 696 and 0552 727 051 | `bitekasa-site/src/App.tsx`, `PHONE_NUMBERS` |
| React 19, TypeScript, Tailwind 4, Motion, Vite 8 | `bitekasa-site/package.json` |
| GitHub Pages hosting, Actions deploy | `.github/workflows/bitekasa-pages.yml` |
| 150 KiB JS / 20 KiB CSS budgets | `bitekasa-site/scripts/check-bundle-size.mjs` |
| Per-page title, description, canonical, sitemap | `bitekasa-site/scripts/check-seo.mjs` |
| Five pages + robots + sitemap tested after deploy | `bitekasa-pages.yml`, "Verify required pages" |
| Everything live, checked daily | `.github/workflows/bitekasa-smoke-check.yml` |
| Palette #A71920 / #F7EEDB / #D5A12E | `bitekasa-site/README.md` |
| No stored customer data, no cart, no payment | `bitekasa-site/README.md` |
| "Illustrative" image disclosure | `bitekasa-site/src/App.tsx`, `figcaption.image-disclosure` |
| GA4 off until key set *and* visitor accepts | `bitekasa-site/src/AnalyticsConsent.tsx` |

And for the Rent & Lease half of the data sheet:

| Claim in the document | Source file |
|---|---|
| Ten record types, by class name | `apps/*/models.py` |
| Only last four digits and expiry stored | `apps/financials/models.py`, `PaymentMethod` |
| Idempotency key on every transaction | `apps/financials/models.py`, `Transaction` |
| Leases soft-delete via `deleted_at` | `apps/leases/models.py` |
| Landlord holds tax ID and business reg. number | `apps/users/models.py` |
| **No full card number and no CVV field** | verified absent from `apps/financials/models.py` |

**Live status — verified by proxy.** `github.io` is blocked from this sandbox,
so the live page cannot be fetched here. The GitHub API is reachable and shows
the `BiteKasa public-site smoke check` workflow **passing**, which curls all
seven production URLs with `--fail` and would fail loudly on any of them.
Latest passing run: `github.com/hotmoon123/hotmoon123/actions/runs/44238191493`.

### Prove it yourself

```bash
python3 docs/softfire/verify-claims.py
```

Re-reads the document section, then greps every asserted fact out of the source
file that backs it, and exits non-zero if any fact has no source. 25 checks. Run
it after any edit to that section — if a claim stops being true, the script
fails instead of the page quietly lying.

It now runs **57 checks**. Besides the fact-to-source checks it asserts the
structure the page now depends on: six `<details>` exist, each has a summary and
a body, the numbers run 01–06 in order, every `#anchor` on the page resolves to a
real id, the accordion and print behaviour are present in `app.js`, and radius is
still 5.

One check is negative: it greps for `card_number`, `cvv`, `cvc`, `security_code`
and `card_full` in the financials model and fails if any of them exists. The claim
"the full card is never stored" is proven by the absence of the field, not by
assertion.

## Hierarchy, applied and measured

The design corpus this project was built against states the position plainly
(`graphic-design-principles.md`): *"Hierarchy is the single most important
principle in graphic design: it tells the viewer where to start, what matters
most, and how to proceed."* Measured against that, the page failed.

| Measured at 390 px | Before | After |
|---|---|---|
| Total page height | 25,654 px | **12,461 px** (−51%) |
| `#documents` section | 14,742 px — **57%** of the page | **1,561 px — 12.5%** |
| Words in `#documents` | 2,149 | 1,109 |
| Scroll before the first document | 8,425 px (≈10 screens) | **8,341 px, list of six visible together** |
| Scroll to reach the last document | 13,412 px of documents | **553 px of list** |
| Largest section on the page | documents (57%) | offers (18%) |

The change was structural, not cosmetic. Each document became
`<details class="doc" data-doc>` with a summary carrying its number, title, the
one-line "whose document is this" and a chevron. Native `<details>` means it
opens with no JavaScript, is keyboard operable with no script, and exposes the
right role to assistive technology. `app.js` adds only the accordion rule — one
open at a time — so the section cannot grow back into the wall it was.

Nothing was deleted. All six documents are still in the page, still fully
readable, and still printed: a closed `<details>` prints nothing, and CSS
**cannot** open one. That was measured, not assumed — the first attempt set
`display:block` on the child and the PDF came out with **0 characters** of
document text. The working mechanism is `beforeprint`/`afterprint` in `app.js`,
and it is verified against the generated PDF: **21 pages, 19,245 characters, all
six titles present.**

### Alignment, proximity and measure — the same audit method

Three more of the corpus principles were checked by measurement rather than by
eye. Each found a real defect.

| Principle | What was measured | Found | Fixed |
|---|---|---|---|
| Alignment (`terminology`: "lining up elements along a common edge") | Left edge of every text block at 1440 px | Price-table caption at x=309 while its own column headers sat at x=285 | `caption.caption-flush` — caption and table now share the spine |
| Proximity (Gestalt: related items group) | Gap from eyebrow to heading, every section | 24/48/48/48/48/48/48/48/48/**0** px | `#brief` had a bare `<p>` where every other section uses `.fig`; now 48 px in all nine |
| Measure (`terminology`: "line length in characters") | Characters per line, probed with a hidden span | Nine blocks at 103–117 characters | Caps in `em`; **max now 85** at 1440 px, 54 at 390 px, none over |

Measure was wrong twice before it was right, which is worth recording:
`76ch` still measured 86 characters because `ch` is the width of `"0"`
(8.00 px here) while this prose averages **6.45 px** per character. `em` tracks
the text, so the cap is set in `em` and re-measured after every change.

### Contrast — every rendered pair, not the palette in the abstract

Instead of trusting the token table, the page was walked element by element,
resolving each text colour against the first opaque background behind it, at the
font size and weight actually computed, against the WCAG 2.2 AA threshold that
applies to that size.

**Result: zero failures.** The single reported hit was the word *plan*, which is
gradient-filled with `background-clip:text` and therefore has a transparent
`color`; measured against its real gradient stops at 67 px bold (3:1 required):

| Stop | Colour | Against `#16100D` | |
|---|---|---|---|
| 0% | `#B33A16` | **3.17** | pass |
| 45% | `#E85D04` | **5.38** | pass |
| 100% | `#F4A300` | **9.05** | pass |

## Known gaps — read before shipping

1. **The price table is published and the pricing is not settled.** The figures
   are provisional and the user is still researching the market. This is the
   largest unsourced claim on the page.
2. **Delivery durations are new.** "2–3 days", "3–4 weeks" and the rest were
   added to frame each offer as a service. They are estimates, not measured
   delivery history. Confirm or remove them.
3. **Nothing has been validated with a real buyer yet.** The idea-to-product
   sheet puts *Research & Validation* before *Strategy* and *Design*, and that
   stage has not happened. There is no interview, no message thread, no
   enquiry from a stranger — so every claim on the page about what a church,
   school or retailer needs is an inference from the work, not evidence from
   the market. The page does not pretend otherwise, and it should not until
   there is a real conversation to point at.
4. **The Rent & Lease system's live status is unproven.** Its models and routes
   are in this repo and its data sheet is real, but there is no deploy
   workflow, no smoke check and no hosting URL for it — unlike BiteKasa, which
   has all three. The page does not claim it is live, and must not start
   claiming that without the same evidence BiteKasa has.
5. **The sequence diagram describes the intended payment path, not a verified
   gateway integration.** No Paystack, Flutterwave, Stripe or Hubtel code
   exists in the repo; `gateway_customer_id` and the reference fields are
   present but nothing is wired to a provider. The diagram is accurate about
   what gets *stored*, and it is a design, not a receipt.
6. **Anchors, not routes.** `#offers`, `#work`, `#process` are sections, not
   URLs. Nothing here is indexable per section, and a shared link always lands
   at the top of the page.
7. **No mobile menu.** Nav hides under 860 px; the WhatsApp button carries the
   CTA alone. The rail covers ≥1024 px. 768–1023 px has no section nav.
8. **LCP is unmeasured.** **Nothing has been measured on a real phone on a
   Ghanaian network.** Do that before calling any of this done.
9. **The carousel holds three cards.** It loops correctly at three. Test at two
   and at five before reuse.
10. **Inter and JetBrains Mono are the variable latin subsets only.** No Greek,
    Cyrillic or Vietnamese. Correct for this audience, wrong if the site is
    ever translated.
11. **`softfire.dev` does not exist.** Every canonical, OG and sitemap URL on
    the page points at `github.com/hotmoon123/softfire/`, which is where it can
    actually be deployed today. Change all of them together, or the metadata
    lies.
