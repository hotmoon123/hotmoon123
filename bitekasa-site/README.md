# BiteKasa — React landing page

A responsive, component-based marketing website for BiteKasa, built with React and TypeScript, Tailwind CSS, Motion for React, and Three.js through React Three Fiber. It presents the corrected advertised packs, clarifies that product mix and condition must be confirmed, and drives enquiries to WhatsApp or phone. It is not e-commerce: there is no cart, payment system, backend, inventory, analytics, or customer-data storage.

## Stack

- **React 19 + TypeScript** for typed, reusable page components.
- **Tailwind CSS 4** for responsive layout and the approved brand tokens.
- **Motion** (`motion/react`) for short, reduced-motion-aware entrance reveals.
- **Three.js via React Three Fiber** for one low-poly samosa accent. Its canvas is intersection-lazy-loaded, small, and subordinate to the food photo.
- **Vite 8** for local development and production builds.

No additional component or icon library is used; small icons are inline SVGs.

## Run locally

Requires Node.js 20.19+ or 22.12+ and npm.

```bash
cd bitekasa-site
npm install
npm run dev
```

Vite binds to `0.0.0.0` for preview compatibility. Run `npm run typecheck` for TypeScript validation, `npm run build` for a production build, and `npm run preview` to inspect that build.

## Brand palette

- BiteKasa Royal Red: `#A71920`
- Warm Cream: `#F7EEDB`
- Royal Gold: `#D5A12E`

These are the owner’s recommended digital HEX values and have been applied consistently. They are not print color specifications.

## Offers shown

- **Silver:** GH₵100 · 30 pieces · no drink specified.
- **Golden:** GH₵200 · 50 pieces · 500 ml Coca-Cola.
- **Premium:** GH₵250 · 70 pieces · 1 litre Coca-Cola.

The exact samosa/spring-roll mix and whether listed prices apply to fried, unfried, or frozen products are not established in the flyer. Confirm before accepting an order.

## Before sharing publicly

Verify both telephone numbers, whether either is WhatsApp-enabled, current prices/stock, package mix, product state, service area, collection/delivery, hours, payment terms, capacity, and any storage/preparation/allergen information. The phone/WhatsApp integration is provisional until the owner verifies the numbers and account status. The generated product images (`assets/food-fried.jpg`, `assets/food-unfried.jpg`, and `assets/food-frozen.jpg`) are clearly labelled illustrative examples, not verified photographs of BiteKasa products. Replace them with owner-approved product photos before making them representative of the real products.

`assets/premium-combo-poster.png` and `assets/bitekasa-logo.jpg` remain unchanged owner-approved source images. The supplied master logo, including its “BITES” subline, is used in the site and corrected flyer. The site links to Instagram `@bitekasa` based on the owner-provided profile screenshot; confirm that the spelling and destination are correct. `assets/bitekasa-offer-flyer.png` is a corrected copy of the owner-approved 2:3 poster composition (1024 × 1536), with the rejected upgrade copy removed and Golden changed to 50 pieces. Feed and Story exports fit the complete artwork without cropping: `assets/bitekasa-instagram-feed-4x5.png` (1080 × 1350) and `assets/bitekasa-instagram-story-9x16.png` (1080 × 1920). These raster files are for digital use, not print-preflighted artwork.

See `../docs/BITEKASA_STARTER_BRIEF.md` for business facts and assumptions, `../docs/BITEKASA_ORDER_WORKFLOW.md` for the proposed workflow, and `../docs/BITEKASA_INSTAGRAM_POST_PACK.md` for posting guidance.
