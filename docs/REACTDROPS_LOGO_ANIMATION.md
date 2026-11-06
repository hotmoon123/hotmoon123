# ReactDrops × BiteKasa — logo animation documentation

> **Status: installed and live on the site.** Source pulled from the registry item `liquid-glass-logo` (four files, ~97 KB of TS/CSS, zero npm dependencies) into `bitekasa-site/src/components/`, mounted through `src/LogoReveal.tsx` as a black brand-reveal band between the product options and the closing call to action.
>
> | Check | Result |
> |---|---|
> | Typecheck | pass |
> | Tests | 10 pass (2 new for the reveal) |
> | Main JS | **118.5 KiB gzip** / 150 KiB budget |
> | Glass chunk | 53.7 kB raw, **18.9 KiB gzip**, lazy — never in main |
> | Logo asset | 35.8 kB (512 px, quantised) |
> | Reduced motion | renders the finished logo still |
> | WebGL missing | falls back to `<img>` of the mark |

**Source:** [reactdrops.dev](https://reactdrops.dev) · repo [crisjavr/reactdrops](https://github.com/crisjavr/reactdrops) · checked 6 Nov 2026

---

## 1. What it actually is

ReactDrops is **not an npm package**. It is a shadcn-style **registry**: you pick a component on the site, tweak it in a live preview, then either copy the source into your project or export a video. There is no `npm install reactdrops` and no version to pin.

| Fact | Detail |
|---|---|
| Output | Plain `.tsx` + `.css` files, copied into your repo |
| Stack | React 19, TypeScript 5, WebGL 2 for the glass/orb drops |
| Install | `npx shadcn@latest add https://reactdrops.dev/r/<slug>.json` |
| Components | 11, all marked **Free** on the site |
| Dependencies | Most need nothing; **Bubble UI** needs `html-to-image`, **Liquid Glass Orb** and **Showcase Pointer** need `gsap` |
| Accessibility | Components respect `prefers-reduced-motion`; the logo drop takes `aria-label` |
| Domain | Use `reactdrops.dev` — `reactdrops.com` only redirects |

**Licence — ReactDrops Component License 1.0.** Commercial use in unlimited End Products is allowed, including client work, and **no visible credit is required**. What you may not do is republish the component itself as a component library, UI kit, template or starter. For a restaurant website this is a clean fit. Keep the licence header that ships inside the `.tsx` file.

---

## 2. The catalogue

| Component | Category | Needs |
|---|---|---|
| **Liquid Glass Logo** | Text Reveal | — (the one for a logo) |
| Refracted Text | Text Effect | — |
| Bubble UI | Button | `html-to-image` |
| Chromatic Button | Button | — |
| Showcase Pointer | Cursor | `gsap` |
| Fractal Glass | Image | — |
| Liquid Glass Orb | AI | `gsap` |
| Fan Gallery | Gallery | — |
| Topographic Terrain | Background | — |
| Topographic Flow | Background | — |
| Shape Physics | Background | — |

---

## 3. Liquid Glass Logo — the component for this job

**What it does:** a droplet forms into a rounded glass tile, the glass refracts the artwork behind it, then the glass and its waves dissolve — leaving your logo sitting clean on the background. Optionally it loops, and the site can render it out as an **MP4**.

**Registry:** `https://reactdrops.dev/r/liquid-glass-logo.json`
**Files it drops in:** `liquid-glass-logo.tsx`, `liquid-glass-logo-renderer.*`, `liquid-glass-logo.css` — no npm dependencies.

### Props that matter

| Prop | Type | Default | Notes |
|---|---|---|---|
| `logo` | string | — | **Image URL** — SVG, PNG, WebP or data URL |
| `logoSize` | number | 256 | Glass tile edge in px |
| `logoScale` | number | 0.72 | Logo size as a fraction of the plate |
| `finalLogoScale` | number | 1 | Resting size after the glass fades |
| `tile` | boolean | true | Put the logo on a rounded icon plate |
| `theme` | `light` / `dark` | `dark` | Sets plate, logo and page colours |
| `logoColor` | string | `#ffffff` | Recolours the logo silhouette; pass **`"original"`** to keep your artwork's colours |
| `logoRelief` | number | 1 | Shading on a recoloured logo; 0 = flat. Original colours are always flat |
| `tileColor` | string | `#060c18` | Surface under the logo lens |
| `background` | string | `#000000` | Use `transparent` to sit on your own surface |
| `depth` | number | 1.2 | Optical depth — higher bends and magnifies more |
| `dispersion` | number | 1 | Colour fringing at the bevels |
| `caustics` / `highlights` / `bloom` | number | 1 / 1 / 0.55 | Light concentration, contour brightness, glow |
| `dropStrength` | number | 1 | Lens curvature |
| `speed` | number | 1 | Playback rate. Logo reveal ≈ **1.8 s** at 1 |
| `loop` / `loopDelay` | boolean / number | false / 1.6 | Restart after the artwork holds |
| `paused` | boolean | false | Hold the current frame |
| `backgroundImage` / `backgroundVideo` | string | — | Photo or muted looping video behind the glass (a BiteKasa pack shot, for example) |
| `backgroundTint` + `…Opacity` | string / number | #000000 / 0 | Darken the background |
| `maxDpr` | number | 2 | Canvas pixel-ratio ceiling — lower it on data-sensitive sites |
| `aria-label` | string | Logo | Accessible name |
| `height` / `className` / `style` | — | — | Size the container; the animation fits inside |

### Ref API

`replay()` · `seek(seconds)` · `pause()` · `play()` — via `ref`, typed `LiquidGlassLogoHandle`.

### Usage snippet (from the docs)

```tsx
import { LiquidGlassLogo } from './components/liquid-glass-logo';

export function Example() {
  return (
    <LiquidGlassLogo
      logo="/logo.svg"
      ending="logo"
      theme="light"
      depth={2.9}
      style={{ height: 480 }}
    />
  );
}
```

> `ending` appears in their example but not in the published property table — treat it as undocumented and leave it out unless the preview requires it.

---

## 4. The prerequisite this project was missing — now done

**The BiteKasa logo on the site is a JPEG** (`bitekasa-site/assets/bitekasa-logo.jpg`). JPEG has no transparency, and the component treats the file as artwork on a plate — a cream square would show inside the glass on any dark surface.

Worse for this job: the full lockup is a **crown + samosa + roll + “BiteKasa” script + BITES + tagline + two phone numbers**. At plate size (100–300 px) the phone numbers become unreadable.

**Created:** `bitekasa-site/assets/bitekasa-logo-mark.png` — 1024 × 1024, transparent, containing only the **crown + samosa + roll** mark, background knocked out to alpha from the original artwork. Nothing was redrawn and the original JPEG is untouched.

Use the mark for animation. Keep the full lockup for print and the header.

---

## 5. Two ways to use it — pick by purpose

### Path A — export an MP4 (no code, use for Instagram)

Best for Reels, Story intros and a video logo sting. Everything happens on the site.

1. Open [reactdrops.dev/components/text-reveal/liquid-glass-logo](https://reactdrops.dev/components/text-reveal/liquid-glass-logo)
2. **Images → Logo** → drop `bitekasa-logo-mark.png`
3. **Logo** panel → Theme **Light**, Tile size ~256, Logo scale ~0.72, Final logo scale 1, Logo colour **Original**
4. **Glass** panel → depth 1.2→2, dispersion ~1, bloom 0.55 (raise highlights if the mark looks flat)
5. **Motion** → drop strength 1, speed 1, **Loop off** for a sting, or loop on for a Story background
6. **Export** → Type **Video**, MP4, aspect ratio (16:9 for the site, 9:16 for Reels if offered), 1080p, 60 fps → **Export video**
7. Save into the project, then cut it to 2 s and put it at the head of a Reel

**Cost:** zero bytes added to the website. **Risk:** none.
**Licence:** exported video of your own logo is yours; the ReactDrops licence governs their code, not your mark.

### Path B — put the component on the website

Do this only if you want the animation *live* on the site.

```sh
cd bitekasa-site
npx shadcn@latest add https://reactdrops.dev/r/liquid-glass-logo.json
```

The CLI needs a `components.json`; the project does not have one yet, so the first run may ask to initialise (Tailwind 4 is already installed via `@tailwindcss/vite`, React is 19.3 — both compatible).

Then, **lazy-loaded**, never in the main bundle:

```tsx
import { lazy, Suspense } from 'react';
const LiquidGlassLogo = lazy(() => import('./components/liquid-glass-logo'));

<Suspense fallback={<img src={logoMark} alt="BiteKasa" width={220} height={220} />}>
  <LiquidGlassLogo
    logo={logoMark}
    theme="light"
    tileColor="#F7EEDB"
    logoColor="original"
    background="transparent"
    depth={1.6}
    speed={1}
    loop={false}
    maxDpr={1.5}
    aria-label="BiteKasa — samosas and spring rolls"
    style={{ height: 320 }}
  />
</Suspense>
```

**Budget check:** the site's CI fails if the main JS chunk exceeds **150 KiB gzip** (`scripts/check-bundle-size.mjs`). A WebGL renderer will blow that if it lands in `main-*.js` — hence `React.lazy`, which puts it in its own chunk that most visitors never download.

---

## 6. Recommended BiteKasa settings

| Setting | Value | Why |
|---|---|---|
| Theme | `light` | Cream and red brand; a dark plate fights it |
| `tileColor` | `#F7EEDB` | Brand cream |
| `logoColor` | `original` | Keeps the gold/orange illustration |
| `background` | `transparent` | Sits on the page instead of punching a black hole |
| `depth` | 1.4–2 | Enough refraction to read as glass, not enough to distort the mark |
| `loop` | `false` | One reveal, then leave it. Looping animation is banned by the project's UI rules |
| `speed` | 1 | 1.8 s reveal is right for a landing moment |
| `maxDpr` | 1.5 | Cuts GPU cost on mid-range Android |
| `aria-label` | `BiteKasa — samosas and spring rolls` | Screen readers |

---

## 7. Honest limits

- **Not for the sticky header.** The header logo is 56 px and loads first; replacing it with a WebGL canvas delays LCP and is the single worst place for this component.
- **Data cost is real.** BiteKasa's visitors are on Ghanaian mobile data. A glass renderer plus a pack-shot background video can cost several megabytes. The MP4 route costs the visitor nothing.
- **Old Android.** WebGL 2 is missing on some low-end devices; always ship the static `<img>` fallback above.
- **The aesthetic is “tech product launch”, not “food”.** Glass and refraction suit a SaaS hero. For a samosa brand it can read as borrowed and cold. The MP4 sting works because it is short and surrounded by food footage; a 6-second glass hero on a restaurant homepage may not.
- **The mark is a raster, not a vector.** At large sizes on a 3× phone screen a PNG will soften. If a designer ever supplies an SVG of the crown/samosa/roll mark, swap it in — same prop, better result.
- **`prefers-reduced-motion`** is respected by the component; keep the static fallback so reduced-motion visitors still see the brand.

---

## 8. Where this leaves the to-do list

| Item | State |
|---|---|
| Transparent logo mark for animation | ✅ `bitekasa-site/assets/bitekasa-logo-mark.png` |
| MP4 logo sting for Reels | ⬜ export from the site (Path A, ~10 minutes, no code) |
| Live animation on the website | ⬜ optional, Path B, needs the shadcn install + a chunk-budget check |
| Replace the header logo with animation | ❌ don't |

**Professional recommendation:** do **Path A** now — it gives you an animated logo for Instagram today, with no bundle cost, no fallback bugs and no performance risk. Treat Path B as a later experiment to be measured against the 150 KiB budget, not as part of the launch.


---

## 9. What was installed, exactly

| File | Size | Role |
|---|---|---|
| `src/components/liquid-glass-logo.tsx` | 13.2 KB | React component, props, ref handle, fallback |
| `src/components/liquid-glass-logo-renderer.ts` | 36.8 KB | Canvas/WebGL engine, image loading, measured fitting, reduced motion |
| `src/components/liquid-glass-logo-shaders.ts` | 41.7 KB | GLSL: bevel refraction, dispersion, caustics, streaks |
| `src/components/liquid-glass-logo.css` | 5.6 KB | Positioning, canvas visibility gating, fallback layout |

All four keep the ReactDrops Component License 1.0 header intact, as the licence requires.

### How it is wired

`src/LogoReveal.tsx`:

- **`React.lazy` + `Suspense`** — the ~92 KB engine is its own chunk (`liquid-glass-logo-*.js`, 18.9 KiB gzip). The main bundle stays at 118.5 KiB gzip against the 150 KiB CI gate.
- **`IntersectionObserver` at 0.35 threshold** — the canvas only mounts when the band is actually on screen, so the 1.8 s reveal plays where a visitor can see it instead of finishing above the fold.
- **Static `<img>` before mount, during load and when WebGL is unavailable** — the brand is never a blank box.
- **`ending="logo"`** — the sequence stops on the original logo at its normal size. No second text reveal, no wordmark.
- **`background="#000000"`, `logoColor="original"`, `logoRelief={0}`, `finalLogoScale={1}`** — black band, unaltered artwork colours, no recoloured silhouette.
- **`aria-label="BiteKasa — samosas and spring rolls"`**, heading visually hidden — the canvas is decorative but the section is announced.

The logo passed to the component is `assets/bitekasa-logo-mark.png`: the crown + samosa + roll, knocked out to transparency from the owner's original JPEG and cut to 512 px / 35.8 kB. The full lockup (with the BITES subline and both phone numbers) was deliberately **not** used — inside a 256 px plate the numbers become illegible. Swapping to the full lockup is one line in `LogoReveal.tsx` if that is ever wanted.
