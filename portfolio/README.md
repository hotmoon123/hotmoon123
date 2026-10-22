# Software Engineer Portfolio

A static, frontend-only portfolio built with **React + TypeScript**, **Anime.js** for motion, and **Three.js** for the hero scene.
All content is hardcoded in TypeScript files. There is no backend, no database, and no server-side code.

## Stack

| Layer | Tool | Used for |
|---|---|---|
| UI | React 19, React Router 7 | Pages, components, client-side routes |
| Language | TypeScript (strict) | Typed content model and components |
| Motion | Anime.js 4 | Hero word reveal, scroll reveals, page fade |
| 3D | Three.js | Animated wireframe scene in the hero |
| Build | Vite | Static build to `dist/` |

## Run it

```bash
npm install
npm run dev        # http://localhost:5173
npm run typecheck  # TypeScript only
npm run build      # typecheck + production build to dist/
npm run preview    # serve dist/ on http://localhost:4173
```

## Where to edit content

Everything you need to change is in `src/data/`:

| File | Edit it to change |
|---|---|
| `site.ts` | Name, role, tagline, email, GitHub and LinkedIn links, availability, navigation |
| `projects.ts` | Projects, status, technologies, case-study sections, code samples |
| `skills.ts` | Python, PHP, MySQL, C++ capability lists and the projects that prove them |
| `experience.ts` | Experience timeline, education, certifications, services |
| `articles.ts` | Articles. Only items with `published: true` appear on the site |
| `types.ts` | The shape of each content type. Change it here first if you add a field |

Replace every bracketed placeholder (`[ ... ]`). Search the `src/` folder for `[` to find them.

### Project status

Use only these labels, and only when they are true:
`Planned` · `In progress` · `Implemented` · `Tested` · `Deployed`

### Adding a screenshot

1. Put the image in `public/images/`, for example `public/images/examination-system.png`.
2. In `projects.ts`, set `image: '/images/examination-system.png'` on that project.

### Adding the CV

Put the PDF at `public/resume.pdf`. The Experience and Resume pages link to it.

## Pages

| Route | Page | Scrollable sections |
|---|---|---|
| `/` | Home | Hero (Three.js + Anime.js), technology stack, featured projects, interests, experience highlights, call to action |
| `/about` | About | Journey, engineering philosophy, goals and learning |
| `/skills` | Skills | Core languages, database, engineering practice and tools |
| `/projects` | Projects | Project grid with language filters and an empty state |
| `/projects/:slug` | Project details | Problem, objectives, features, architecture, database, code sample, decisions, testing, results, limitations, future work |
| `/experience` | Experience | Timeline with context, actions and outcomes |
| `/education` | Education | Qualifications, certifications (completed only) |
| `/resume` | Resume | Summary, skills, projects, education, PDF download |
| `/case-studies` | Case studies | Projects marked `hasCaseStudy` |
| `/articles` | Articles | Published articles only |
| `/services` | Services | Services, process, quote request |
| `/contact` | Contact | Contact methods, what to expect, privacy note |
| `*` | Not found | Custom 404 with links back in |

The design reference is `docs/pages-and-sections.md` and the sketch board in `docs/sketches/`.

## Accessibility and motion

- Skip link, landmarks, one `h1` per page, labelled sections, visible focus rings, 44px minimum tap targets.
- `prefers-reduced-motion` turns off Anime.js reveals, the hero animation, page fades, and the Three.js loop. The static hero still renders.
- The Three.js scene is decorative (`aria-hidden`). The page works without WebGL.
- Scroll reveals watch for content added later, so lazy-loaded pages still reveal.

## Deploying (static hosting)

The build output is the `dist/` folder. Any static host works.

- **Netlify:** build command `npm run build`, publish directory `dist`. `public/_redirects` handles deep links.
- **Vercel:** the build is detected automatically. `vercel.json` handles deep links and sets security headers.
- **GitHub Pages:** set `base: '/your-repo-name/'` in `vite.config.ts`. GitHub Pages does not support client-side routing without a fallback, so copy `dist/index.html` to `dist/404.html` after building.

Always use HTTPS in production.

## Performance

- The Three.js scene is in its own chunk (about 130 KB gzip) and loads only on the home page.
- The scene pauses when off-screen or when the tab is hidden, and caps the pixel ratio at 1.5.
- Images should be compressed before you add them. Use `loading="lazy"` (already set on project images).

## Security

- Nothing secret belongs in this project. Anything in the bundle can be read by a visitor.
- The contact page uses a `mailto:` link, so there is no form and nothing to protect on the server.
- If you later add a form, you need a form service or a backend, and you must update the privacy notice.

## Checks before publishing

- [ ] `npm run build` succeeds with no TypeScript errors
- [ ] Every `[placeholder]` is replaced
- [ ] Every project status is true
- [ ] `public/resume.pdf` is current and matches the Resume page
- [ ] Email, GitHub and LinkedIn links point to your accounts
- [ ] Check on a phone, a tablet, and a laptop, in light and with reduced motion on
- [ ] Deep links such as `/projects/examination-system` open directly after deploy
