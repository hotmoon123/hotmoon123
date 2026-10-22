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

## Security

This is a static site with no server code, no database, and no secrets, so the attack surface is small. Still:

- `_headers` sets a strict Content Security Policy. The page uses only external `styles.css` and `script.js`, with no inline scripts or styles, so the policy works without exceptions. If you add an inline script or a third-party embed, you must update the policy.
- Do not add API keys, tokens, or private email addresses to the HTML or JavaScript. Anything in the page is public.
- The contact email is visible in the HTML, so expect some spam. You can reduce it with a contact form from a form service, which adds a third-party dependency and should go into the CSP.
- Only link to external sites you trust, and add `rel="noopener"` to any link that opens in a new tab.

## Visitor flows

`docs/visitor-flows.md` maps who visits the site, what each visitor is trying to do, and the path from landing to contact. Use it to check that every section supports one of those paths.

## Before you launch

Based on the launch and growth stages in the idea-to-product guides:

1. **Benchmark first.** Pick 5 portfolios in your field that you admire or compete with. For each, note: what they lead with, how many projects they show, whether outcomes are stated, and how long it takes to reach a contact link. Then write one sentence on the gap you can own. Do this by hand; the slash-style prompt codes in the uploads are conventions, not built-in features, so they will not run this for you.
2. **Check the page on a real phone** at 320 px width and in both light and dark mode.
3. **Replace every placeholder.** Search for `[` in `index.html`. Nothing in square brackets should go live.
4. **Set the social preview.** Fill in the `og:` tags and the `og:url`. Add a 1200×630 image only if it is real work or a real photo.
5. **Test the contact link** by sending yourself an email from it.
6. **Run a quick accessibility check** with your browser's built-in Lighthouse or accessibility audit. Fix anything it flags in contrast, labels, or focus order.
7. **Run the 60-second check.** Open every page at 100% zoom, view it on a phone, squint to check the hierarchy, read the headline aloud, and ask whether you would be proud to show it.
8. **Check permissions.** Confirm in writing that you may show any client work. Many client contracts reserve portfolio-use rights, so remove or anonymise anything you are not cleared to show.
9. **Publish** on a static host of your choice (for example GitHub Pages or Netlify). Both serve this folder as-is.

## What I did not take

- The Django/rent-lease product docs in `docs/` are about a different system. They were not used.
- The AI portfolio-builder TRD in `MD files for development.md` describes a multi-user SaaS. It is useful later if you want a generator, but it is more than a personal site needs.
- Brand-strategy and business frameworks are useful for positioning, but I did not invent a brand identity. Add one when you have decided your positioning.

## Open questions for you

- Your name, role, city, and the one-sentence positioning you want to be known for.
- Three projects you can show publicly, with the outcomes you are willing to state.
- Whether you want a custom domain and a contact form (a form needs a backend or a form service; `mailto:` is the zero-dependency option used here).
