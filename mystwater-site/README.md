# Myst Water — website concept (proposal build)

> **What this is:** a private website proposal for **MYST WATER COMPANY** — “The Feel Good Water”, the aquifer‑sourced natural mineral water brand of **PNF Industries Limited** (Accra, Ghana), “Proudly made in Ghana”.
> **Who made it:** Caleb Bentum — a speculative concept. It is **not** an official website and carries no affiliation until the company adopts it.
> **Why it exists:** the company's official `drinkmyst.com` currently answers HTTP 503 and the Google Business Profile shows no website — so the pitch is “this is how MYST WATER should look and sell online”.

## Run locally

Requires Node.js 20.19+ or 22.12+.

```bash
cd mystwater-site
npm ci
npm run dev        # http://localhost:5173
npm run build      # production build → dist/
npm run preview    # serve the production build
npm run typecheck  # TypeScript, no emit
npm run test:coverage
npm run check:content  # concept-integrity gate (noindex, phones, credit…)
npm run check:bundle   # compressed-asset budget
```

## Stack

React 19 · TypeScript · Vite · Tailwind CSS 4 · `motion`/`lucide-react`/`react-icons` · self‑hosted fonts (Archivo Black for display, Inter for body via Fontsource — **zero third‑party requests at runtime**) · Vitest + jest‑axe for tests · static hosting (GitHub Pages subpath `/hotmoon123/mystwater/`).

## Content & data provenance (no invented facts)

| Fact on the page | Source |
|---|---|
| Brand, tagline “The Feel Good Water”, “Proudly made in Ghana”, PNF Industries Limited | Instagram `@mystwater` bio + Facebook `@mystnaturalwater` bio (visited 2026‑11‑06) |
| Dodowa aquifer, filtered & packaged at origin, natural mineral water | PNF Industries Limited LinkedIn (via search, 2026‑11‑06) |
| Sizes 500 ml / 750 ml / 1 Litre; designs blue / clear / green | PNF LinkedIn + supplied product photography |
| 5.0 ★ Google rating, 6 reviews (all five stars); quotes reproduced verbatim | Google Maps listing paste/screenshot (2026‑11‑06) |
| Phone **020 410 2171** (Google Maps) | Google Maps listing |
| Phone **+233 59 699 5220** (Facebook bio) | Facebook page bio |
| `info@drinkmyst.com`, `drinkmyst.com` (HTTP 503 at time of writing) | Facebook bio + direct fetch (2026‑11‑06) |
| Address “Accra – Tema Beach Road, Accra”, plus code JW3C+MH | Google Maps listing |
| Accessibility/amenities (wheelchair access, hearing loop, nursing room, changing table, recycling: batteries/bulbs/cans, gender‑neutral toilets, free parking) | Google Maps listing |
| Campaign lines: “The Feel Good Water” (FB/IG cover), “Drip too nice”, “Sipping is believing”, “Purely sourced — bottled at the origin”, “Detty December” | Supplied artwork files |
| Prices, MOQ, delivery zones/fees/hours, FDA registration | **NOT PUBLIC — intentionally shown as “on enquiry”. Never hard‑code guesses.** |

Where the two published phone numbers disagree, **both are shown, labelled by source** — the company should retire one on adoption.

## Concept honesty rules baked into the build

- `<meta name="robots" content="noindex,nofollow">` and a `Disallow: /` `robots.txt` — the concept will not squat on the company's SERP.
- Footer credit: “Website concept for MYST WATER COMPANY … prepared by Caleb Bentum … not an official website”.
- Reviews reproduced verbatim from the public Google listing with attribution and access date.
- No prices, MOQ, hours, FDA claims or delivery promises anywhere without the owner's confirmation.
- Form does **not** silently submit: it opens WhatsApp/email with the message pre‑filled (or a Netlify Form if deployed on Netlify with `data-netlify`). No analytics, cookies or trackers.
- Imagery is the supplied brand artwork, unmodified, used for proposal evaluation only.

## Adoption checklist (what changes the day MYST WATER says yes)

1. Replace placeholder contact labels with the company's decision (retire one phone number; publish hours, MOQ, price list, delivery zones — edit `src/content.ts` only).
2. Flip `robots` meta to `index,follow`, rewrite `public/robots.txt` to allow + sitemap, wire `Sitemap:` reference, drop the concept credit for the company's own notice.
3. Point `drinkmyst.com` DNS at the host (Netlify or GitHub Pages) — currently 503, so any adoption is an instant win; update canonical/OG URLs in `index.html`.
4. Add `sitemap.xml`, LocalBusiness JSON‑LD is already in place (extend with `aggregateRating` only if reviews stay on Google and the company wants rich results).
5. Optional: consent‑gated GA4 (bitekasa pattern — not enabled here), online ordering/payment (this v1 is deliberately enquiry‑first), 1 Litre design imagery, real delivery‑coverage data.
6. Link the site from the Google Business Profile (“Add website” button) and both social bios — currently neither has one.

## Repository placement

`mystwater-site/` at the repo root. CI: `.github/workflows/mystwater-ci.yml` (typecheck + tests + build + concept‑integrity gate). Deploy: folded into the existing `bitekasa-pages.yml` artifact as the `/mystwater/` subpath of the GitHub Pages site, so the live BiteKasa site is not disturbed.

© All brand marks, photography and campaign artwork belong to MYST WATER COMPANY / PNF Industries Limited. Code in this folder © 2026 Caleb Bentum.
