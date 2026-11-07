# BiteKasa design system — v2 "warm editorial"

Status: implemented in code (`src/styles/tokens.css`, `src/styles.css`, `src/site/*`).
Owner: BiteKasa (Princess Esson). Last reviewed: 6 November 2026.

This document is the contract. If the code and this document disagree, the code is
wrong — or this document needs updating in the same change.

---

## 1. Why this direction

The site is not competing with a delivery app; it is competing with a blurry
Instagram post and a flyer with no price. The reference point is a **printed
menu from a good kitchen**: warm paper, one confident red, a serif that carries
authority, prices that are the loudest thing on the page.

Every decision below serves two questions a first-time visitor asks in under
five seconds:

1. What does it cost?
2. What do I do next?

If a design choice does not help answer one of those, it does not ship.

---

## 2. Colour

| Token | Value | Use |
|---|---|---|
| `--paper` | `#F7EEDB` | Page background (brand cream) |
| `--paper-raised` | `#FCF7EA` | Cards, form surfaces, consent panel |
| `--paper-deep` | `#EFE3CC` | Alternating band (order builder section) |
| `--ink` | `#241B18` | Primary text, primary buttons |
| `--ink-soft` | `#5C4A40` | Secondary text (7.1:1 on paper) |
| `--ink-muted` | `#7A675C` | Captions, meta (4.9:1 on paper) |
| `--red` | `#A71920` | Brand red — **one event per screen** |
| `--red-deep` | `#7E1116` | Red where it carries text (7.4:1 on paper) |
| `--gold` | `#D5A12E` | Hairlines, rules, 2px accents only — **never a fill** |
| `--gold-deep` | `#8A6516` | Gold where it must carry text |
| `--line` | `rgb(36 27 24 / 14%)` | Standard hairline |
| `--line-strong` | `rgb(36 27 24 / 30%)` | Emphasised hairline, outlined buttons |
| `--on-dark` | `#F7EEDB` | Text on ink and on red |

### Rules

- **One red event per screen.** Red is reserved for the single action that matters:
  the hero CTA, the builder's send button, the closing plate. Never two competing
  red fills in one viewport.
- **Gold is ink, not paint.** Gold appears as a 1px rule, a 2px accent, or an
  eyebrow tick. Large gold fills were removed in v2 because at that scale the
  cream/gold pair loses contrast and looks inexpensive.
- **No gradients. No glassmorphism on content surfaces.** The only blur allowed is
  the sticky action bar, where legibility over scrolling content requires it.
- **Body text on cream is never lighter than `--ink-muted`.** `--gold` is never
  used for text below 24px.

### Contrast (measured, not assumed)

`--ink` on `--paper` 13.6:1 · `--ink-soft` 7.1:1 · `--ink-muted` 4.9:1 ·
`--red-deep` on `--paper` 7.4:1 · `--on-dark` on `--red` 6.4:1 · `--on-dark`
on `--ink` 13.6:1. All pass WCAG 2.2 AA for their use.

---

## 3. Type

Two families. No third.

- **Display:** Newsreader Variable (SIL OFL 1.1), self-hosted latin subset,
  weights 200–800, italic available. Used for `h1`–`h4`, prices, step numerals.
- **Text/UI:** system sans stack. Zero download, renders natively on Android,
  iOS and Windows.

| Token | Size | Use |
|---|---|---|
| `--text-xs` | 12px | Labels, captions, legal notes |
| `--text-sm` | 14px | Meta, secondary rows, buttons |
| `--text-base` | 17px | Body copy |
| `--text-md` | 19px | Lead paragraphs, pack contents |
| `--text-lg` | 24–30px | Section sub-heads, order total |
| `--text-xl` | 30–42px | Section titles |
| `--text-2xl` | 38–60px | Hero |
| `--text-3xl` | 44–80px | Closing plate only |

Rules:
- Body minimum is **17px**. The v1 site shipped 11–13px body copy; that is the
  single biggest quality change in v2.
- Display weights sit at **400/500**. Bold serif at large sizes reads as shouting.
- Display tracking `-0.02em`; label tracking `+0.16em` uppercase.
- `text-wrap: balance` on all headings.
- Measure is capped at `--measure` (34rem ≈ 60 characters).

---

## 4. Space, radius, elevation

- 4px base scale: `4 8 12 16 24 32 48 64 96` (`--space-1` … `--space-9`).
- Section padding: 56px mobile → 80px tablet → 96px desktop.
- Gutters: 16px → 28px → 48px. Content max width 76rem.
- Radius — soft, and one value per element type (owner direction, v2.1):

  | Token | Value | Applies to |
  |---|---|---|
  | `--radius-xs` | 6px | chips, tags, tiny controls |
  | `--radius-sm` | 12px | utility links only (skip link) |
  | `--radius-md` | 18px | cards, images, panels, FAQ rows, step cards |
  | `--radius-lg` | 24px | order panel, consent panel |
  | `--radius-pill` | 999px | **every interactive control** — buttons, steppers, menu toggle, badges |

  Rule: **never mix radii on the same element type.** Three tiers and no others:
  *content* sits at 18px, *containers* at 24px, *anything you can tap* is a pill.
  Flat by exception only (the WhatsApp message preview is a ruled quote, 0px).
- Elevation: `--shadow-card` (1px, 5% warm ink) for resting cards so a rounded
  surface reads as a surface; `--shadow-float` for the consent panel only.
  Nothing hovers above the page.
- **Declutter rule:** separation comes from *surface and space* before lines.
  Cards carry a 1px hairline instead of a heavy rule; FAQ and service links are
  rounded rows with gaps rather than a stack of dividers; section headers use one
  small accent tick, not a full-width bar.

---

## 5. Motion

- Durations: `140ms` (state), `180ms` (hover/transition), `240ms` (entrance).
- Easing: `cubic-bezier(0.22, 0.61, 0.36, 1)`. No bounce, no spring, no looping.
- One shared entrance (`Reveal`): fade + 10px rise, `once: true`.
- Nothing animates on scroll repeatedly, and nothing animates for decoration.
- `prefers-reduced-motion` collapses every duration to 1ms and disables the
  splash's fade.

---

## 6. Components

Each component lists anatomy, variants, states and the accessibility contract.
Source of truth is `src/site/`.

### 6.1 Header (`Header.tsx`)
Sticky, 68px, cream at 94% with 8px blur, 1px bottom hairline.
Anatomy: logo link (48px) → nav links → WhatsApp CTA → menu toggle (<768px).
States: resting, scrolled (hairline, no shadow), menu open (`aria-expanded`),
Escape closes, focus returns sensibly. Nav links carry a 1px red underline that
scales from the left on hover/focus — no colour-only hover cue.

### 6.2 Buttons
| Variant | Class | Fill | Border | Text |
|---|---|---|---|---|
| Primary (conversion) | `.whatsapp-button`, `.builder-cta`, `.sticky-cta-primary` | `--red` | `--red` | `--on-dark` |
| Secondary | `.call-button`, `.builder-reset`, `.sticky-cta-secondary` | transparent | `--line-strong` | `--ink` |
| Quiet | `.header-cta`, `.analytics-accept` | `--ink` | `--ink` | `--on-dark` |
| Ghost link | `.pack-link`, `.option-detail-link` | — | bottom hairline on hover | `--red-deep` |

All buttons: min height 44px (48–50px for primary), 4px radius, `--text-sm`,
weight 550–600, transition on `background-color` and `border-color` only.
Disabled: `opacity: .4` **plus** `cursor: not-allowed` **plus** the `disabled`
attribute. Colour is never the only disabled signal.

### 6.3 Pack card (`Packs.tsx`)
Anatomy: 2px accent rule → name label → price (display, `--text-xl`) → contents →
per-piece price → two points → WhatsApp link.
Variants: `pack-golden` (gold rule), `pack-premium` (red rule), default (ink rule).
No card background, no shadow: separation comes from the rule and whitespace.
Accessibility: link has an explicit `aria-label` naming the pack.

### 6.4 Order builder (`OrderBuilder.tsx`, `src/lib/order.ts`)
The only interactive surface on the site. A `<fieldset>` with a visually hidden
`<legend>`, one row per pack, each row a 44px stepper with an `<output>`.
- Quantity clamps to 0–20 per pack; the maths lives in `src/lib/order.ts` and is
  unit-tested independently of React.
- Summary region is `aria-live="polite"` and announces total, pack count and piece count.
- Primary CTA is a `<button disabled>` when empty and an `<a>` to `wa.me` when not —
  never a link that goes nowhere.
- Message preview is a `<details>` so the visitor can read exactly what will be sent.
- The WhatsApp message always ends with "Please confirm availability" — the site
  never implies an order is placed or a payment taken.

### 6.5 Steps (`HowItWorks.tsx`)
An `<ol>` of three `<li>` (numbers are decorative `aria-hidden` spans; the list
semantics already convey order). 1px top rule, large gold-deep numeral, sans title.

### 6.6 Preparation option (`PreparationOptions.tsx`)
Image (4:3, hairline, 4px radius) → label → state line → link to the detail page.
Every image carries the illustrative caption.

### 6.7 FAQ (`Faq.tsx`)
Native `<details>`/`<summary>`. Hairline rows, no cards. First item open on load.
Question 19px display; answer 17px body capped at `--measure`. Marker colour is
gold-deep so the affordance is visible without adding an icon.

### 6.8 Closing plate (`ContactCta.tsx`)
The one full-bleed red surface. Cream text, cream primary button that inverts on
hover. Phone rows are 52px with a cream hairline, gold trailing arrow.

### 6.9 Sticky mobile actions (`StickyCta.tsx`)
Fixed bar, visible below 768px only, 96% cream with 10px blur, respects
`env(safe-area-inset-bottom)`, and `body` reserves 76px so nothing is trapped
under it. Two actions maximum: build an order, WhatsApp.

### 6.10 Consent panel (`AnalyticsConsent.tsx`)
Raised paper, 1px line, `--shadow-float`, 44px buttons. On mobile it sits above
the sticky bar (offset by 68px) so the two never overlap.

### 6.11 Splash (`LogoIntro.tsx`)
Once per session, black, the logo finishes alone, `?intro=1` replays, `?intro=0`
suppresses, focus restored, reduced motion honoured. **No button:** it ends on
its own after the reveal (2.4s, then a 260ms fade) or early with Escape. Taps and
scrolls deliberately do nothing, so the animation is never swallowed and a tap
meant for the page underneath is never eaten by the overlay.

---

## 7. Images

- Every food image is labelled **"Illustrative product image"**. The caption is
  part of the component, not optional copy.
- 4:3 on pack/hero frames, 1px hairline, 4px radius, `object-fit: cover`.
- No stock people, no AI-generated people, no images that imply a real customer
  or a verified photo of a specific pack.
- Owner-supplied photography can replace an illustrative image only together with
  the caption being removed in the same change.

### Icon set (favicon / app icons)

The icon is the owner's **full logo lockup** — crown, samosa, spring roll,
BiteKasa wordmark, BITES, tagline and both phone numbers — on brand cream
`#F7EEDB`. The owner chose the lockup over an emblem-only crop, so every size
shows the same design.

Because a detailed lockup cannot survive being upscaled, **each size is rendered
from the 1254×1254 original** rather than enlarged from a small bitmap:

| Frame | Source |
|---|---|
| 16px | the owner's supplied `favicon.ico` bitmap, kept pixel for pixel |
| 32px, 48px | lockup rendered from the 1254px original |
| 180px | lockup, opaque full-bleed square (iOS applies its own mask) |
| 192px, 512px | lockup, 20% rounded corners, for install |
| 512px maskable | lockup inside a 78% safe zone for Android |

Files live in `public/`: `favicon.ico` (16/32/48), `favicon-32.png`,
`apple-touch-icon.png`, `icon-192.png`, `icon-512.png`, `maskable-512.png`,
`site.webmanifest`. Source artwork is the lockup supplied on 6 November 2026;
the original file is never modified.

Trade-off, stated plainly: at 16px the lockup reduces to a warm smudge with a red
band — no detailed logo can do better at that size. It reads clearly from 32px up
and is fully legible at 180px on a home screen. If tab clarity is ever preferred
over the full lockup, swapping in the emblem crop is a one-file change.

---|---|
| `favicon.ico` | 16 / 32 / 48 multi-size, legacy tabs and bookmarks |
| `favicon-32.png` | modern browsers |
| `apple-touch-icon.png` | 180px, **opaque square** — iOS applies its own mask |
| `icon-192.png`, `icon-512.png` | installable app icon, rounded corners |
| `maskable-512.png` | Android maskable, emblem inside the 62% safe zone |
| `site.webmanifest` | name, theme `#F7EEDB`, icon set |

**v2.2 (7 Nov 2026): replaced at the owner's request.** The owner supplied a
16×16 ICO showing the full lockup and asked for it to become the favicon. That
frame is now the source for every size, so all surfaces show the same artwork.

*Resolution limit, recorded honestly:* a 16×16 source cannot carry a wordmark.
The tab icon is pixel-exact, but `icon-192`, `icon-512` and the maskable icon are
honest upscales of it and read soft at home-screen size. The previous emblem set
(cut from the 1254×1254 lockup) remains reproducible from that JPEG if a crisp
large icon is wanted later.


---

## 8. Voice

- Plain, warm, specific. Short declaratives. Second person.
- Prices in numerals: `GH₵200`, never "two hundred cedis".
- No exclamation marks, no "delicious!", no scarcity theatre, no invented reviews.
- Claims are limited to what is verified: three packs, fixed prices, WhatsApp
  ordering, collection or delivery agreed in chat, fried/unfried/frozen *where available*.
- Anything unverified is either omitted or explicitly hedged ("confirm on WhatsApp").

---

## 9. Accessibility contract (WCAG 2.2 AA)

- Landmarks: one `banner`, one `main#main`, one `contentinfo`; skip link first in
  tab order.
- Visible focus ring: `3px solid --red-deep`, offset 3px, never removed.
- All targets ≥ 44×44px (nav, steppers, phone rows, FAQ summaries at 60px).
- Text contrast ≥ 4.5:1; large display text ≥ 3:1.
- No information conveyed by colour alone (underlines, markers, text labels).
- `aria-live` on the order summary; `aria-expanded`/`aria-controls` on the menu;
  `aria-label` on icon-only controls.
- Reduced motion honoured at both CSS and component level.
- Automated axe check runs on the home page, service page and consent in the test suite.

---

## 10. The five-second test

Before any release, look at the home page for five seconds on a phone, then answer:

1. What are the prices? (Silver GH₵100 · Golden GH₵200 · Premium GH₵250)
2. What do I do next? (Build an order → WhatsApp)

If either answer requires scrolling past a decoration, the page fails, however
handsome it is.

---

## 11. Decisions log

| # | Decision | Alternative rejected | Why |
|---|---|---|---|
| 1 | Warm editorial direction | Bold street-food; minimal menu-board | Credibility with a first-time buyer; ties to the printed flyer |
| 2 | Display serif + system sans | Two web fonts; all-sans | One font download (~122 kB latin, swap), text renders instantly |
| 3 | Gold demoted to hairlines | Gold CTA fills (v1) | Cream-on-gold fails contrast at scale and reads cheap |
| 4 | Primary conversion buttons red | Gold buttons | Red is the brand's strongest signal and passes 6.4:1 with cream |
| 5 | Body 17px | 12–13px (v1) | Readability on a phone held at arm's length |
| 6 | **Radius scale 6 / 12 / 18 / 24 / pill** (v2.1, owner direction) | 2–8px tight corners (v2.0) | Owner asked for softer, friendlier corners; the Janus Tiu design-system prompt requires one consistent radius per element type — so the scale is now documented rather than improvised |
| 7 | No shadows on content | Cards with soft shadows | Hierarchy from rules and space, not blur |
| 8 | One shared entrance animation | Per-section effects | Consistency, and cheaper to audit for reduced motion |
| 9 | Order maths extracted to `src/lib/order.ts` | Logic inside the component | Testable without a DOM; one place to change the message format |
| 10 | Prices only in `src/data/catalogue.ts` | Prices in copy | A price change is one edit and cannot drift between sections |
| 11 | Cards carry the content; rules were reduced to a small accent tick | Full-width 2px rules (v2.0) | Less visual noise at phone width — the owner's "not cluttered" test |
| 12 | Navigation trimmed to four items (Packs · Build an order · Questions · Contact) | Five items incl. "How it works" | The section still exists; the header stops competing with the hero |

---

## 12. How to change this system

1. Change the token in `src/styles/tokens.css` first; never hardcode a hex or a
   px value that exists as a token.
2. If a change alters how a component looks or behaves, update §6 here in the
   same commit.
3. Run the full gate: `npm run typecheck && npm test && npm run build &&
   npm run check:bundle && npm run check:seo`.
4. If a change affects price, availability or a claim, it needs the owner's
   confirmation — not a developer's judgement.

---

## 13. Known gaps

- No real-device or real-browser visual pass in this environment (Playwright
  Chromium cannot be installed here). Layout has been verified by tests, build
  output and CSS review, not by screenshot.
- No photography yet, so every food image remains illustrative.
- The design system covers the marketing site only; the Instagram grid, flyer and
  video are governed separately by the brand documents.
