# Personal Portfolio — Starter

A dependency-free static portfolio (HTML, CSS, a small JS file). No build step, no framework, no packages to install.

## Preview locally

```bash
cd portfolio
python3 -m http.server 8080 --bind 0.0.0.0
# open http://localhost:8080
```

## Make it yours

1. Replace every bracketed placeholder in `index.html` (`[Your Name]`, `[Project one name]`, and so on). Search for `[` to find them all.
2. Keep three case studies. Each one should answer: the problem, the decision you made, and the result.
3. Remove any section you cannot fill with real material. An honest short page beats a padded one.
4. Change the accent colour once, in the `:root` tokens at the top of `styles.css`.
5. Add real images to `assets/` only when they add information (a screenshot, a diagram, a before/after). Compress them first.

## Design decisions (and where they came from)

I read the uploaded reference files and kept the principles that apply to a personal site. I left out the parts about SaaS products, CRMs, and the Django rental app in this repo.

| Decision | Why | Source in the uploads |
|---|---|---|
| One hero idea and one primary action (*See selected work*) | A portfolio has one job: get the visitor to the work. | `prompter.md` decision rules; `ULTIMATE_DESIGN_SYSTEM.md` "one primary action per screen" |
| Real, specific content with no lorem ipsum, no fake testimonials, no fake metrics | Anti-generic and ethics rules: never fabricate proof. | `prompter.md` anti-AI rules; `MB atelier design.md` "never fabricate…" |
| No stock hero photo, gradient blobs, or glassmorphism | Named as "AI landing page" clichés to avoid. | `prompter.md` anti-AI rules; `software prompt.md` style taxonomy |
| Warm paper, ink, and one ember accent, with a serif display face and a system sans body | Restrained palette with 60/30/10 weighting. Each choice can be explained in one sentence. | `prompter.md` colour rules; `ULTIMATE_DESIGN_SYSTEM.md` typography |
| All text pairs ≥ 4.5:1 contrast in light and dark mode | WCAG 2.2 AA is listed as non-negotiable. | `prompter.md` technical non-negotiables; `ULTIMATE_DESIGN_SYSTEM.md` accessibility |
| 16 px body, 1.6 line height, 45–75 character measure, 44 px tap targets | Readability and touch standards from the same docs. | `prompter.md` technical non-negotiables; `prompter.md` "tap targets 44 pt" |
| Dark mode designed separately, not inverted | Explicitly required. | `prompter.md` colour rules |
| Motion is subtle, runs once, and is off for `prefers-reduced-motion` | Motion over 500 ms and scroll-jacking are called out as things to avoid. | `prompter.md` anti-AI rules; `ULTIMATE_DESIGN_SYSTEM.md` reduced-motion rule |
| Case-study structure (Problem → Decision → Result) | Outcome-framed case studies are the strongest portfolio format. | `prompter.md` "portfolio/case-study thinking" |
| Works without JavaScript | Progressive enhancement; the content is never hidden behind JS. | `MD files for development.md` non-functional requirements |

## What I did not take

- The Django/rent-lease product docs in `docs/` are about a different system. They were not used.
- The AI portfolio-builder TRD in `MD files for development.md` describes a multi-user SaaS. It is useful later if you want a generator, but it is more than a personal site needs.
- Brand-strategy and business frameworks are useful for positioning, but I did not invent a brand identity. Add one when you have decided your positioning.

## Open questions for you

- Your name, role, city, and the one-sentence positioning you want to be known for.
- Three projects you can show publicly, with the outcomes you are willing to state.
- Whether you want a custom domain and a contact form (a form needs a backend or a form service; `mailto:` is the zero-dependency option used here).
