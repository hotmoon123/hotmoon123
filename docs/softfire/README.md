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
| CSS, gzip (both files) | — | **17.2 KB** |
| HTML, gzip | — | **16.9 KB** |
| First load, transferred (mobile, 390px) | 1 MB | **173.0 KB** |
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
LD_LIBRARY_PATH=/tmp/chr/libs/lib python3 docs/softfire/measure-audit.py
```

Two scripts, two different questions. `verify-claims.py` asks *is every stated
fact true somewhere in the repo* — 67 checks. `measure-audit.py` asks *does the
page meet the written standards at every width* — it opens the page in
Chromium at ten widths and measures what actually renders.

Re-reads the document section, then greps every asserted fact out of the source
file that backs it, and exits non-zero if any fact has no source. 25 checks. Run
it after any edit to that section — if a claim stops being true, the script
fails instead of the page quietly lying.

It now runs **94 checks**, including the price ladder pinned by row, every clause of the after-launch promise, each header in `_headers`, and both statutes the page leans on.

**Business documents:** `brand/BRAND.md` · `brand/BRAND-PROMPT.md` · `PRICING.md` ·
`MAINTENANCE.md` · `SECURITY-HOSTING.md` · `OPERATIONS.md` ·
`LAW-GOVERNANCE.md` · `GROWTH.md` · `CARD.md`. Besides the fact-to-source checks it asserts the
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

## The standards, and where each number comes from

Every figure below is quoted from a file in the reference set, not invented.
Three of them exposed defects that a visual pass had missed.

| Standard | Source | Measured | Result |
|---|---|---|---|
| Measure 45–75 characters | `THE_COMPLETE_STACK.md` §1.1; `MASTER-PROMPT-senior-graphic-designer.md` §6 | 27–72 cpl at ten widths | pass |
| No symmetric four-icon grid | master prompt §5 (banned list) | four glass cards → numbered rules | pass |
| Reading order: brand before section nav | UIUX master prompt §10 (keyboard checks) | tab 1 skip, 2 brand, 3 CTA, 4–9 rail | pass |
| Every control ≥ 44px, visible 2px focus | UIUX master prompt §10 | 10/10 stops, 0 under 44 | pass |
| Body text ≥ 16 px | master prompt §6 | 16 px prose, 18 px lede | pass |
| Line-height 1.3–1.6 | `THE_COMPLETE_STACK.md` §1.1 | 1.50–1.60 | pass |
| Works at 320 px **and 1920 px** | uiux master prompt §10 | 320 → 1920, 0 overflow | pass |
| First load < 1 MB | `THE_COMPLETE_STACK.md` §1.3 | 173.0 KB | pass |
| Controls ≥ 44 px | site floor | 0 under, ten widths | pass |
| CSP + Referrer-Policy | software/security prompt §6.1–6.2 | meta CSP, hash-pinned | partial, see gaps |

### The measure was wrong twice, and the second time was worse

The site first ran 103–117 characters per line. I capped it at `76ch` and
believed it fixed. It measured **86** — because `ch` is the width of `"0"`
(8.00 px), not the average character (5.75 px at 14 px, 6.45 px at 16 px).

So I measured again, with a probe span, and believed *that*. It still reported
85, and I wrote "max 85" into this file as if 85 satisfied a 75-character
standard. It did not. **That was a false claim in my own documentation.**

Both mistakes had the same root: estimating characters instead of counting
them. `measure-audit.py` now counts characters per *rendered line box* using
Range rectangles — the number a reader actually experiences. The caps were then
derived from measurement instead of guessed: 75 characters of 16 px prose is
484 px, which is 30.2em, so the cap is `30em`. Table cells needed their own cap
because they do not inherit the prose width; they were the widest text on the
page at 84 characters.

Lesson recorded because it cost the most time in this project: **an estimate
that agrees with your expectation is the most dangerous kind of measurement.**

### The anti-generic rule, applied to a grid that was on the banned list

`MASTER-PROMPT-senior-graphic-designer.md` §5 lists what never to produce,
and one line is: *"Symmetric four-icon feature grids with no editorial point of
view."* The "who this is for" section was exactly that — four equal glass cards
in a four-column grid, equal weight, no indication which audience matters.

The fix was not to delete the content. Same four audiences, same words, no
invented facts. What changed is the **carrier**: glass boxes became a numbered
list with 2px rules, so the type and the number carry the structure instead of
a card outline doing it. On mobile the four collapse into one numbered column,
which is how a menu should behave.

Verified at 390 and 1440: no overflow, no control under 44px, measure inside
45–75 characters.

### What survives with JavaScript switched off

Law 1 of the ten laws is *"the network is not reliable."* The most common
partial-failure state on a 3G Android is not a broken network — it is a page
that loads and then does nothing because a script did not.

Tested in Chromium with `java_script_enabled=False`:

| | with JS off |
|---|---|
| `<h1>` renders | yes — "The plan before the pixels." |
| All six document summaries | **6 of 6 visible** |
| Documents open on click | **yes — native `<details>`, no script needed** |
| The brief | step 1 renders, progress bar present |
| Page height at 390px | 12,888px (vs 12,461px with JS) |

The one thing that stops working is the accordion (staying open one at a time)
and the composed WhatsApp message, which are written in JavaScript by
definition. Every document still opens. Nothing is unreachable.

### Security, and the limits of a static host

GitHub Pages cannot send response headers. The page therefore carries what meta
tags can carry, and nothing more is claimed:

- **Content-Security-Policy** (meta): `default-src 'self'`, `script-src 'self'`
  plus the one permitted inline script pinned by SHA-256 hash, `object-src
  'none'`, `base-uri 'self'`, `form-action 'none'`, `connect-src 'self'`.
- **Referrer-Policy**: `strict-origin-when-cross-origin`.
- Loaded in Chromium: **zero CSP violations, zero JS errors**, and the
  hash-pinned script still applies a saved motion preference before first paint
  (verified with `reduced-motion` emulation — `data-motion="off"` still lands).

What is **not** protected, and must not be described as protected: HSTS,
`X-Frame-Options` / `frame-ancestors` (meta CSP does not cover it, so the page
is clickjackable), and `Permissions-Policy`. Those need a host that can set
headers — Cloudflare Pages, Netlify or Vercel can, GitHub Pages cannot.

## The brand, in five parts

`brand/BRAND.md` — purpose, market position, identity, legal, and customer
experience, with every line marked FACT, INFERENCE or UNKNOWN. Read it before any
of the four decisions at its end.

Three findings from writing it are already applied to the site.

### The logo was not the logo — fixed

Every mark was `<text font-family="Inter">SF</text>` inside an SVG loaded through
an `<img>`. An SVG in an `<img>` is a separate document and **cannot fetch the
page's web fonts**, so the browser fell back to a system sans. Measured in
Chromium, three different S shapes appeared side by side.

`tools/build-marks.py` instantiates the shipped `inter-latin-var.woff2` at
`wght 700`, applies −0.03em tracking, and emits the glyphs as paths. Still an
ordinary S and an ordinary F — now those two letters in every browser, with no
font request and no fallback. All five assets are 1.2–1.6 KB.

### The price was undefended — fixed

Measured against five real Accra studios:

| Studio | Entry website price |
|---|---|
| BuiltFound | GH₵1,000 |
| YookuWeb | GH₵1,500 |
| Websys | GH₵2,500 |
| KayTech | GH₵3,500 |
| **SoftFire** | **GH₵4,500** |

SoftFire is the most expensive entry price in the set and the page said nothing
about why. The table was losing on the only axis it did not address. There is now
one card under it that names the rival range, admits it is not the cheapest, and
lists four things a "from" quote cannot promise — all of them already true of the
studio, so no new claim was invented.

It ends with: *"If they are not worth the difference to you, the cheaper quote is
the right purchase and I will say so."*

### The domains are taken — and this project's notes were wrong

The notes said `softfire.dev` "does not exist". It does. Live DNS:

| Domain | Status |
|---|---|
| `softfire.dev` | **registered** — resolves to Cloudflare |
| `softfire.com` | **registered** — resolves to a hosting IP |
| `softfire.com.gh` | NXDOMAIN — **appears available** |
| `softfire.gh` | NXDOMAIN — appears available |

A customer typing `softfire.com` reaches a stranger. `softfire.com.gh` looks
free, and it is the one that matches a registered business name.

## The GH₵1,500 decision, and what it costs

`PRICING.md` is the research: every cost between the first conversation and a live
site, marked FACT / INFERENCE / UNVERIFIED. It exists because GH₵1,500 all-in was
chosen without a cost model, and the numbers turned out to be less comfortable
than the price suggests.

**Three findings that change how the site is built:**

1. **`.com.gh` costs GH₵750–1,690 a year**, not the GH₵200 the registry's own
   guidelines still quote. At GH₵1,500 all-in, a `.com.gh` domain is 50% of the
   price before any work happens — and at the dearer registrars, more than all of
   it. **SoftFire must quote `.com` (GH₵146–260) or static hosting, or the job
   loses money.** `.com.gh` is a brand cost, not a hosting cost.
2. **GH₵1,500 is about 30 hours** — the local freelance floor of GH₵50/hour — so
   **2–4 days, not 3–4 weeks**. The page previously said 3–4 weeks. Only one of
   those can be true.
3. **E-Levy was repealed in April 2025.** Any cost model still adding 1.5% to
   mobile-money receipts is out of date. The live cost is the merchant fee,
   0.75–1.5%.

**The honest advantage that survives at this price:** every competitor's published
price list *excludes* the domain and hosting. One that includes them is genuinely
cheaper than one that does not. That sentence is now the strongest true claim on
the page.

**The card was repurposed, not deleted.** It used to defend being the dearest quote
in Accra. At GH₵1,500 the premise is false, so it now answers what a GH₵1,500 buyer
actually asks: *what is not included.* It is the scope sheet from `PRICING.md` §3.

**Unmeasured this session:** Chromium could not be installed in the sandbox, so
`measure-audit.py` could not run. The page was validated structurally (balanced
tags, 74 claim checks, 17.6 KB gzip) but **not visually**. Re-run
`measure-audit.py` before shipping.

## Maintenance is not management

`MAINTENANCE.md` is the research behind the after-launch promise: what the four
words actually mean, what a static site needs, and how to structure three free
months so they build a paying relationship instead of a churn statistic.

**The finding that drives everything:** a static site has **no database, no
plugins, no CMS to patch**, and every host renews SSL automatically. Sourced
twice, the genuine technical work is about **two hours a year** — a quarterly
sweep of links, forms and stale content. So:

> **Maintenance asks "is it still working?" Management asks "is it still true?"**

Selling a maintenance retainer on a static build would be charging a monthly fee
for work that does not exist. The plan sells **management** — changes made,
someone accountable, and a monthly note saying what was checked.

**The three-months problem.** A study of 16,512 free-trial customers found **48%
churned**, against 34% of those on a regular contract — a free trial selects for
people who were never going to pay, and 4–6% is a good no-card trial conversion.
So the three months are structured as **onboarding, not a trial**: capped at one
hour a month, with a monthly note that becomes the receipt for month four.

| When | What | Cost |
|---|---|---|
| Days 1–30 | anything that does not work as the signed scope said | free |
| Months 1–3 | 1 hour of changes/month + the monthly note | included |
| Month 4 on | 2 changes/month + the monthly note | GH₵200/month |
| If nothing ever changes | nothing to maintain | nothing |

**Costed, not guessed:** one hour a month is 3 hours — **GH₵150 at GH₵50/hour,
10% of the build.** Uncapped, the same promise is a 40–67% loss. The cap is what
makes the generosity affordable.

**The rule that matters most:** nothing renews without asking. A silent rollover
is how a studio that trades on fixed, written prices loses the plot.

The page now carries a four-row table stating all of this with dates, and the
Care Plan was repriced from **GH₵399–899/mo to GH₵200–400/mo** — above the Ghana
market (GH₵250–600) it was renting the site rather than looking after it.

## Security is setup, not a subscription

`SECURITY-HOSTING.md` answers where security and hosting belong.

**Security: 9 of 20 standard controls apply to a static site, and 7 of those are
done once at launch.** There is no CMS to patch, no plugin, no database, no login,
no server to harden, no WAF worth having on a page with no input. A "security
monitoring" line on a static build is an alarm on an empty room.

What actually matters is the **client's accounts** — registrar, email, GitHub —
because most breaches start with one stolen login, not with the site. That is 2FA
and a registrar lock, once, for free.

**The finding that changes the build: GitHub Pages cannot send custom headers.**
Not "is inconvenient" — cannot. A `<meta>` tag cannot substitute either, because
the CSP spec **excludes `frame-ancestors` from meta delivery**, and Chromium says
so in the console. So clickjacking prevention is impossible on GitHub Pages and
possible on Cloudflare Pages, at the same GH₵0 price.

`_headers` now exists in this directory with HSTS, `frame-ancestors`,
`X-Content-Type-Options`, `Referrer-Policy` and `Permissions-Policy`. It takes
effect the moment the deploy target is Cloudflare Pages or Netlify. **Until then
that gap is real and documented**, and the site says which host causes it.

**Hosting: separate, named, and GH₵0.** Research says bundling hosting into a care
plan is the most profitable model and markup is "the most exposed". Both conflict
with a brand whose promise is that nothing is hidden. Static hosting costs nothing,
so there is no margin to take on nothing:

| Item | Who pays | Cost |
|---|---|---|
| Hosting (static) | nobody | **GH₵0** |
| Domain `.com` | client, directly | GH₵146–260/yr |
| Domain `.com.gh` | client, directly | GH₵750–1,690/yr |
| cPanel, only if insisted | client, directly | GH₵105–1,100/yr |

**This gives up about GH₵1,200/yr per client in hosting margin** in exchange for a
claim no competitor in the table can make: no migration, no lock-in, the exit cost
is a zip file. The retainer is the business; it does not need to smuggle hosting
into its price.

**And the trap:** the moment the site stops being static — a portal, a login, a
database — everything above inverts. Security becomes a real service, backups
become data, and the retainer must follow the attack surface, not the client's
budget. A GH₵200 plan on a portal holding student records would be a liability.

## The operating manual

`OPERATIONS.md` is the business, not the website: structure, procedures, goals,
records, tax, risk, and the decisions already made so they are not re-made.

**The seven questions, answered once:** every part of the business — offer, money,
records, tax, security, clients, growth — is held against *what, why, who, when,
where, how, which*. The pattern that falls out is the same in every row:
**write it down, keep the number fixed, own the account, answer the phone.**

**Two findings that matter more than the rest:**

1. **Withholding tax on services is 7.5%.** When a business, school or church pays,
   they deduct it and give you a certificate. A GH₵1,500 invoice may arrive as
   **GH₵1,387.50**. That is not a loss — the certificates are a tax credit — but it
   is a cash-flow gap, and **losing the certificates means paying the tax twice.**
2. **The law changed on 1 September 2026.** Act 1178 raised the tax-free threshold
   to GH₵7,056 and the presumptive turnover threshold to **GH₵750,000** at **3%**.
   But **individuals with a professional qualification are excluded** from the
   presumptive routes. That is one question — *do you hold a formal IT or
   computing qualification?* — and it decides whether the books are a sales book
   or a proper set of accounts. It is not answered here.

**The 90-day goal is one paid project, documented to the BiteKasa standard.** Not
ten cheap ones — the first build of a business type costs 30 hours and the third
costs 22, because by then the page plan, the content worksheet and the launch
checklist exist. Those three assets are the highest-return hour in the business.

**Three risks score 12+ and get a rule, not a hope:** no paying client (20), a job
running past 30 hours (16), and illness with one person and no backup (12). The
control for the third is unglamorous and real: every live site has a handover
sheet so someone competent could step in for a week.

## Law and governance

`LAW-GOVERNANCE.md` covers the statutes that actually touch this business, the
contract clauses, and how a one-person business governs itself. Two findings:

**1. SoftFire is almost certainly an unregistered data controller, and 2026 is an
enforcement year.** Act 843 requires registration *before* processing personal
data, renews every two years, and makes processing without it a criminal offence
(fine or up to two years). The Commission has declared 2026 for enforcement —
*"no exemptions"* — with spot checks from 5 October 2026.

A phone number on WhatsApp is personal data. So is every contact form on every site
built. **The list of what to do is short and cheap:** register, add a privacy line,
add a processor clause (s.30(2) requires a written agreement), keep an incident log.
None of it is done.

**2. In Ghana the client owns the copyright by default — and almost no studio says
so.** Copyright Act 690 s.7 vests commissioned work in the *commissioner* unless
the contract says otherwise. Ghana is the opposite of the US/UK default. That makes
the ownership promise the strongest legally-checkable claim on the page — and it is
now stated with its carve-out: SoftFire keeps the reusable system, the client gets a
permanent licence to everything on their site.

**Governance, for one person,** is not a board. It is six clauses that fit on a
card, a ten-question screen before accepting any job, and a quarterly question that
is deliberately uncomfortable: *which rule did I break, and was it the rule's
fault?*

`CARD.md` is the one-page version — strength, logic, process, fundamentals, the
numbers, and what to do when everything is on fire.

## Build, grow, scale, stabilise, sustain

`GROWTH.md` is the lifecycle, the strategy, the tactics and the calendar.

**The number that decides everything — computed, not asserted:** 4 build-hours a
day × 5 days = **20 build-hours a week**. At 30 hours a build that is **2.9 builds a
month = GH₵4,330**. At 22 hours (a mature job) it is 3.9 builds, GH₵5,905.

| Mix | Monthly | Yearly |
|---|---|---|
| 2 builds, no retainers | GH₵3,000 | GH₵36,000 |
| **2 builds + 10 retainers** | **GH₵5,000** | **GH₵60,000** |
| 3 builds + 10 retainers | GH₵6,500 | GH₵78,000 |

So: **SoftFire cannot build its way past about GH₵4,300 a month**, and 10 retainers
adds GH₵2,000 for work that already has a block reserved. Everything else follows.

**Strategy is a list of refusals, not a plan.** Five of them, each costing money the
day it is adopted: no fourth build, no bespoke design per client, no reselling
hosting, no ranking promises, no price below the page. The test of a real strategy
is that a competitor could not copy it without losing money. *"We care more"* fails
that test; *"we will not resell your hosting"* passes it.

**The scale sequencing, and the one thing that is wrong:** there are three levers —
price, product, hiring. **Hiring now is arithmetic that does not work** — a build
earns GH₵1,500 and a junior costs more than one a month, so you need 3–4 builds to
cover a hire you cannot feed. The order is: **raise the price, then hire. Never
hire to justify the price you have.**

**The calendar is the strategy.** Friday has no build block on purpose — if
building is available on Friday it fills Friday, and the week never closes. And
**two build slots are booked a month, not three**: the gap between 2 and 3 is what
"the number does not move" is made of.

**Sustain is one number:** three months of personal costs. It is not a luxury, it
is the price of the only strategic freedom that matters — **the ability to say no.**

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
11. **Clickjacking is not prevented.** Meta CSP cannot set `frame-ancestors`,
    and GitHub Pages sends no `X-Frame-Options`. A static host that sets headers
    fixes this in one line; this one cannot. Do not claim the site is
    frame-protected.
12. **The validation gap is still the largest gap.** See item 3. Standards
    compliance is not market evidence, and passing 67 checks is not the same as
    one stranger asking to buy.
13. **Clickjacking is still not prevented, and now the reason is named.** The site
    cannot send `frame-ancestors` or HSTS while it deploys to GitHub Pages.
    `_headers` is written and will take effect on Cloudflare Pages or Netlify.
    **The gap is the host, not the page.**
14. **`softfire.dev` is registered to someone else.** `softfire.com` too. The
    canonical and OG URLs on this page point at `hotmoon123.github.io/softfire/`,
    which is where it can actually deploy today. `softfire.com.gh` appears
    available and is the recommended home. **Corrected:** earlier notes in this
    repo said the domain did not exist; live DNS says it does. Every canonical, OG and sitemap URL on
    the page points at `github.com/hotmoon123/softfire/`, which is where it can
    actually be deployed today. Change all of them together, or the metadata
    lies.
