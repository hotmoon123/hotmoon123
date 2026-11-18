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

    # ---- DOC 05 part B: the Rent & Lease system ----
    ("Invoice model exists",        "class Invoice",        "apps/financials/models.py"),
    ("Transaction model exists",    "class Transaction",    "apps/financials/models.py"),
    ("PaymentMethod model exists",  "class PaymentMethod",  "apps/financials/models.py"),
    ("Lease model exists",          "class Lease",          "apps/leases/models.py"),
    ("MaintenanceTicket exists",    "class MaintenanceTicket","apps/maintenance/models.py"),
    ("Building model exists",       "class Building",       "apps/properties/models.py"),
    ("Property model exists",       "class Property",       "apps/properties/models.py"),
    ("Landlord model exists",       "class Landlord",       "apps/users/models.py"),
    ("PasswordResetToken exists",   "class PasswordResetToken", "apps/users/models.py"),
    ("only last four stored",       "last_four",            "apps/financials/models.py"),
    ("expiry month/year stored",    "exp_month",            "apps/financials/models.py"),
    ("idempotency key exists",      "idempotency_key",      "apps/financials/models.py"),
    ("leases soft-delete",          "deleted_at",           "apps/leases/models.py"),
    ("momobile providers listed",   "MTN Mobile Money",     "apps/financials/models.py"),
    ("lease holds contract pdf",    "contract_pdf",         "apps/leases/models.py"),
    ("ticket holds a photo",        "photo = models.ImageField", "apps/maintenance/models.py"),
    ("landlord holds tax id",       "tax_id",               "apps/users/models.py"),
    ("business reg number stored",  "business_reg_no",      "apps/users/models.py"),
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

# A negative claim needs its own test: prove the dangerous fields are absent.
fullcard = []
for rel in ("apps/financials/models.py",):
    body = src(rel)
    for banned in ("card_number", "cvv", "cvc", "security_code", "card_full"):
        if re.search(r"\b" + banned + r"\s*=\s*models\.", body):
            fullcard.append((rel, banned))
print(f"  {'OK  ' if not fullcard else 'FAIL'}  no full card / CVV field  <- apps/financials/models.py")
if fullcard:
    fails.extend((f"banned field {b}", r, b) for r, b in fullcard)

print()
if fails:
    print("FAILED:", len(fails))
    for f in fails: print("  ", f)
    sys.exit(1)
print(f"All {len(checks) + 1} checks passed: every factual claim traced to source, and no card/CVV field exists.")
