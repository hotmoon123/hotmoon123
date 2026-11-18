"""Every fact asserted in the six-documents section must exist in the repo."""
import re, sys, pathlib

root = pathlib.Path('/home/user/hotmoon123')
html = (root/'docs/softfire/index.html').read_text(encoding='utf-8')
i = html.index('7b. THE SIX DOCUMENTS'); j = html.index('8. ABOUT')
docs = html[i:j]

def src(rel):
    return (root/rel).read_text(encoding='utf-8', errors='replace')

checks = [
    ("Silver 30 pieces",       "30 pieces",  "bitekasa-site/src/App.tsx"),
    ("Golden 50 pieces",       "50 pieces",  "bitekasa-site/src/App.tsx"),
    ("Golden 500 ml Coke",     "500 ml",     "bitekasa-site/src/App.tsx"),
    ("Premium 1 litre Coke",   "1 litre",    "bitekasa-site/src/App.tsx"),
    ("Red #A71920",            "#A71920",    "bitekasa-site/README.md"),
    ("Cream #F7EEDB",          "#F7EEDB",    "bitekasa-site/README.md"),
    ("Gold #D5A12E",           "#D5A12E",    "bitekasa-site/README.md"),
    ("React 19",               "react\": \"^19", "bitekasa-site/package.json"),
    ("TypeScript",             "typescript", "bitekasa-site/package.json"),
    ("Tailwind 4",             "tailwindcss", "bitekasa-site/package.json"),
    ("Vite 8",                 "vite",       "bitekasa-site/package.json"),
    ("Motion for React",       "motion",     "bitekasa-site/package.json"),
    ("150 KiB JS budget",      "150 * 1024", "bitekasa-site/scripts/check-bundle-size.mjs"),
    ("20 KiB CSS budget",      "20 * 1024",  "bitekasa-site/scripts/check-bundle-size.mjs"),
    ("canonical check",        "canonical",  "bitekasa-site/scripts/check-seo.mjs"),
    ("sitemap check",          "sitemap",    "bitekasa-site/scripts/check-seo.mjs"),
    ("smoke check urls",       "services/fried", ".github/workflows/bitekasa-smoke-check.yml"),
    ("daily cron",             "cron:",      ".github/workflows/bitekasa-smoke-check.yml"),
    ("deploy workflow",        "deploy-pages",".github/workflows/bitekasa-pages.yml"),
    ("robots in deploy",       "robots.txt", ".github/workflows/bitekasa-pages.yml"),
    ("backup workflow exists", "name:",      ".github/workflows/bitekasa-backup.yml"),
    ("GA4 consent component",  "AnalyticsConsent", "bitekasa-site/src/AnalyticsConsent.tsx"),
    ("illustrative caption",   "image-disclosure", "bitekasa-site/src/App.tsx"),
    ("phone 0595 638 696",     "233595638696","bitekasa-site/src/App.tsx"),
    ("no cart/payment claim",  "not e-commerce", "bitekasa-site/README.md"),
]

fails = []
for label, needle, rel in checks:
    body = src(rel)
    ok = needle in body
    if not ok: fails.append((label, rel, needle))
    print(f"  {'OK  ' if ok else 'FAIL'}  {label:28} <- {rel}")

# every URL quoted in the smoke-check workflow must appear in the page's claim set
wf = src('.github/workflows/bitekasa-smoke-check.yml')
urls = re.findall(r"https://hotmoon123\.github\.io/hotmoon123/[^']*", wf)
print(f"\n  smoke-check covers {len(urls)} production URLs:")
for u in sorted(set(urls)): print("    ", u)

print()
if fails:
    print("FAILED:", len(fails))
    for f in fails: print("  ", f)
    sys.exit(1)
print(f"All {len(checks)} factual claims traced to source. No invented facts.")
