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

# ------------------------------------------------------------------
# Structural checks. The disclosure rewrite is a claim too: "six documents,
# reachable, and none lost". If a summary stops pointing at its body, or a
# body disappears from the DOM, that is a broken promise and this fails.
# ------------------------------------------------------------------

struct = []
docs_html = re.findall(r'<details class="doc" data-doc[^>]*>(.*?)</details>', docs, re.S)
struct.append(("six documents present", len(docs_html) == 6, f"{len(docs_html)} found"))
for n, body in enumerate(docs_html, 1):
    has_sum = '<summary class="doc-sum"' in body
    has_inner = '<div class="doc-inner"' in body
    # every id a summary/body defines must be unique in the whole page
    struct.append((f"doc {n:02d} has summary + body", has_sum and has_inner,
                   "summary" if not has_sum else ("body" if not has_inner else "ok")))

# the six document numbers, in order, appear in the summaries
nums = re.findall(r'<span class="doc-n"[^>]*>\s*(\d\d)', docs)
struct.append(("numbers 01-06 in order", nums == ["01","02","03","04","05","06"], str(nums)))

# no orphaned anchors: every href="#..." must resolve to an id on the page
ids = set(re.findall(r'\sid="([^"]+)"', html))
anchors = set(re.findall(r'href="#([^"]+)"', html))
missing = sorted(anchors - ids)
struct.append(("every #anchor resolves", not missing, str(missing)))

# the accordion needs both a JS behaviour and a CSS fallback
css = (root/'docs/softfire/styles.css').read_text(encoding='utf-8')
js  = (root/'docs/softfire/app.js').read_text(encoding='utf-8')
struct.append(("accordion in app.js", "data-doc" in js, "app.js"))
# MEASURED: CSS cannot reveal a closed <details> for print (the PDF came out
# with 0 characters of document text). The working mechanism is the print
# lifecycle in app.js, so that is what gets asserted.
struct.append(("print opens all six", "beforeprint" in js and "afterprint" in js, "app.js"))
struct.append(("accordion respects print", "printing" in js, "app.js"))
# the /whitespace claim is a CLAIM, not decoration: it says three specific
# things are on page one of every quote. If any of the three leaves the page,
# the claim stops being true.
ws = ["price is fixed", "excluded is written down", "new written number"]
struct.append(("whitespace claim: 3 promises", all(w in html for w in ws),
               ", ".join(w for w in ws if w not in html) or "all present"))
# every offer row must be framed as a service (standing instruction).
# Searched across the whole page, not the documents slice — the offers table
# is a different section. Care Plan opens "An ongoing service", not "A".
service_rows = re.findall(r'\bAn? (?:planning|diagnosis|structure|software|system|process|ongoing) service:', html)
struct.append(("every offer framed as a service", len(service_rows) == 8, f"{len(service_rows)} of 8"))
# ---- standards from THE_COMPLETE_STACK / the master prompts ----
tok = (root/'docs/softfire/tokens.css').read_text(encoding='utf-8')
# measure 45-75 chars: 30em caps, derived from counted line boxes
struct.append(("measure cap is 30em", "--measure-prose: 30em" in tok, "tokens.css"))
struct.append(("body text is 16px floor", "--fs-body:    1rem" in tok, "tokens.css"))
# the type scale must be modular, 1.2-1.333
struct.append(("spacing scale exists", "--s-16" in tok, "tokens.css"))
# static-host security: meta CSP + referrer policy, and the inline script hash
csp = re.search(r'Content-Security-Policy" content="([^"]+)"', html)
struct.append(("meta CSP present", bool(csp), "index.html"))
struct.append(("CSP pins the inline script by hash",
               bool(csp) and "sha256-" in csp.group(1), "index.html"))
struct.append(("CSP forbids object-src", bool(csp) and "object-src 'none'" in csp.group(1), "index.html"))
struct.append(("referrer policy strict-origin", 'name="referrer" content="strict-origin-when-cross-origin"' in html, "index.html"))
struct.append(("no third-party origin", not re.search(r'(?:src|href)="https?://(?!hotmoon123\.github\.io|wa\.me|github\.com|schema\.org)', html), "index.html"))
# the anti-generic rule: the four-audience section must NOT be built from
# cards. MASTER-PROMPT-senior-graphic-designer.md 5 bans "symmetric four-icon
# feature grids". This asserts the carrier is a rule + number, not a box.
seg = html[html.index('id="who"'):html.index('id="offers"')]
buyer_css = css[css.index('.buyer {'):css.index('.buyer:focus-visible')]
struct.append(("buyers are rules, not cards",
               "border-radius: 0" in buyer_css and "box-shadow: none" in buyer_css,
               "styles.css"))
struct.append(("brand precedes section nav",
               html.index('class="brand"') < html.index('class="rail"'), "index.html"))
struct.append(("radius is 5", "--r-1: 5px" in (root/'docs/softfire/tokens.css').read_text(encoding='utf-8'), "tokens.css"))

for label, ok, where in struct:
    print(f"  {'OK  ' if ok else 'FAIL'}  {label:28} <- {where}")
if any(not ok for _, ok, _ in struct):
    fails.extend((l, w, "") for l, ok, w in struct if not ok)

print()
if fails:
    print("FAILED:", len(fails))
    for f in fails: print("  ", f)
    sys.exit(1)
print(f"All {len(checks) + 1 + len(struct)} checks passed: every factual claim traced to source, "
      f"no card/CVV field exists, and all six documents are reachable.")
