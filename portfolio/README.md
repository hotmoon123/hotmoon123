# Caleb Bentum — Portfolio

A single-page, frontend-only portfolio for Caleb Bentum, IT student and backend developer. Built with **React**, **TypeScript**, **Anime.js** and **Three.js**. All content is hardcoded, and there is no backend, database or secret.

- Page and section specification, with the sketches: [`docs/PAGES-AND-SECTIONS.md`](docs/PAGES-AND-SECTIONS.md)
- Original sketches: [`../docs/sketches/`](../docs/sketches/)

## Run it

```bash
npm install
npm run dev          # http://localhost:5173
npm run typecheck    # TypeScript only
npm run build        # type check, then production build to dist/
npm run preview      # serve dist/ on http://localhost:4173
```

## Edit the content

Everything you are likely to change is in `src/data/`. You should not need to touch the components.

| File | What it controls |
|---|---|
| `profile.ts` | Name, role, university, email, GitHub link, hero text, bio, navigation |
| `projects.ts` | Projects, status, period, role, stack, case-study text, links |
| `skills.ts` | Skill cards, the "Used in" links, the "Built with" row, the timeline and the approach steps |
| `types.ts` | The shape of each content type. Change this first if you add a field. |

**Status labels** must be true: `Planned`, `In progress`, `Implemented`, `Tested` or `Deployed`.

**Screenshots:** place the image in `public/images/` and set `image` and `imageAlt` on the project in `projects.ts`. Until then, a labelled placeholder is shown.

## Structure

```
src/
├── App.tsx             one page, seven sections, header, footer
├── main.tsx            entry point; sets the reduced-motion flag
├── components/         Header, Footer, Section, ProjectCard, SkillCard, CopyEmail, BackToTop, StatusBadge
├── sections/           Hero, About, Skills, Projects, Approach, Experience, Contact
├── data/               profile, projects, skills and types (all hardcoded)
├── animations/motion.ts  Anime.js helpers and scroll reveals (all respect reduced motion)
├── three/HeroScene.tsx   Three.js hero scene, lazy-loaded, pauses off-screen
└── styles/             tokens.css (palette), global.css, responsive.css
```

## Design

- Palette: charcoal `#17191C`, warm ivory `#F4F1E8`, electric lime `#C5F467`, slate `#777F8C` (decorative only).
- Hybrid layout: dark sections for the hero, skills, projects and contact; light sections for about, approach and experience.
- Text contrast meets WCAG AA. Body text is at least 16px, and the layout works from 320px wide.

## Accessibility and motion

- Skip link, one `h1`, one `h2` per section, labelled regions, visible focus rings, targets of at least 44px.
- The menu, project disclosures and copy button use correct ARIA attributes.
- `prefers-reduced-motion` removes Anime.js motion and CSS transitions, and draws the 3D scene as a still frame.
- The page works without WebGL and without JavaScript reveal animations.

## Deploy

The build is static: `npm run build` produces `dist/`, which any static host can serve.

- **Netlify:** build command `npm run build`, publish directory `dist`. `public/_headers` sets the security headers and a Content Security Policy.
- **Vercel or GitHub Pages:** serve `dist/` as a static site. This is a single page, so no SPA rewrite rules are needed.
- Replace the placeholder canonical URL in `index.html` with your domain before you publish.

## Before publishing

- [ ] Every `[placeholder]`-style gap in the copy is filled, and the statuses are true.
- [ ] The Rent & Lease repository link is the one you want to show.
- [ ] Real screenshots are added, or the placeholders are acceptable for now.
- [ ] Email, GitHub and the canonical URL are correct.
- [ ] Checked on a phone, a tablet and a laptop, and with reduced motion on.
