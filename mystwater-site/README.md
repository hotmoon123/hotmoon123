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

## Intro / splash — “Liquid Glass Logo” (what it is, and how to swap it)

On every page load the app opens with a full‑screen MYST‑indigo intro: the supplied logo (`public/assets/myst-logo.jpg`, byte‑identical to the file shared on 2026‑11‑07) plays a liquid‑glass entrance — a glossy sphere morphs into the mark, with a wavelength‑ordered bevel ring, chromatic edge streaks and a measured, responsive fit — and then finishes on the original logo alone. **No button is required**: the animation auto‑completes (~2.7s, or ~0.35s under `prefers-reduced-motion`), and tapping/clicking anywhere (or pressing `Escape`/`Enter`/`Space`) reveals the site immediately. The rest of the site renders underneath the overlay, so nothing else waits on it. The splash background is drawn from the sampled MYST palette (indigo `#012885`, deep navy, campaign blue `#0257CC`, cyan `#25AAE2`, leaf `#8DC540`) — never red.

**Sound.** A short (2.6s) water chime plays with the intro — a rising "filling" swell, a droplet plink with soft slapback, and a warm C–E–G bell as the logo settles. It is **original, synthesized with an ad‑hoc numpy script** (committed as `public/assets/audio/myst-splash.wav`; no third‑party samples, no licence obligations). Browser autoplay rules may block it before the first user gesture; the intro then retries the chime on the first tap/click (when playback is permitted) and otherwise runs silently. Press **M** anywhere on the intro to mute it (no extra button — deliberate). If audio is unavailable or the file fails to load, the site simply runs silent. Screen‑reader users get the visual experience only, which is unchanged.

**Provenance — read this honestly.** The brief asked to install the ReactDrops “Liquid Glass Logo” component (ID `liquid-glass-logo`) via `npx shadcn@latest add https://reactdrops.dev/r/liquid-glass-logo.json`. That registry file could not be fetched from this sandbox (network is restricted to npm/GitHub; the fetch fails at the TLS handshake), so what ships is an **original implementation** in `src/components/liquid-glass-logo.tsx` + `src/components/SplashScreen.tsx`, written to the requested feature set (sphere‑to‑tile entrance, wavelength bevel, chromatic fringes, measured fitting, reduced‑motion support, image fallback with a CSS‑only wordmark, single `ending="logo"`, `depth={2.9}`, intro chime `assets/audio/myst-splash.wav`). It is **not** the ReactDrops component and carries no ReactDrops licence terms.

**Swap in the real ReactDrops component:** from a network‑open machine, fetch the JSON, copy its `files[]` contents over `src/components/liquid-glass-logo.tsx` (and any dependencies it declares), keep the `SplashScreen.tsx` call site (`<LiquidGlassLogo logo={asset('assets/myst-logo.jpg')} ending="logo" theme="dark" depth={2.9} style={{ height: 480 }} onFinish={requestDone} />`) and re‑run `npm run typecheck && npm run test`.

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
