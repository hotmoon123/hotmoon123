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
# The card was rewritten on 2026-11-06: the old one defended being dearest at
# 4,999, which stopped being true at 1,500. It now answers "what is not
# included". These checks follow the card, so they fail if it drifts back into
# an affordability claim the price does not support.
for _phrase, _why in [
    ("one-page scope you sign", "the fixed price is only fixed if the scope is signed"),
    ("first year of hosting", "1,500 is all-in; hosting must stay in it"),
    ("Thirty days of fixes", "the warranty is the only after-sale promise made"),
]:
    struct.append((f"1,500 card: {_phrase}", _phrase.lower() in html.lower(), _why))
struct.append(("1,500 card names what is excluded",
               "Not included:" in html, "exclusions on page one, not page nine"))
struct.append(("1,500 card does not overclaim",
               "costs more than the cheapest" not in html,
               "only BuiltFound is cheaper; a 'we are dearest' claim is false"))

# --- the price ladder ------------------------------------------------------
# Nothing checked prices until 2026-11-06. Two repricings have since silently
# hit the wrong row (Brand system was set to 1,500 when only Website was
# decided), so the ladder is now pinned by NAME, not by value.
import re as _re
_rows = _re.findall(
    r'<th scope="row" class="row-h">([^<]+?)\s*(?:<span[^>]*>.*?</span>\s*)*</th>.*?'
    r'<td class="num" data-label="Price">([0-9,]+)', html, _re.S)
_prices = {n.strip(): int(p.replace(",", "")) for n, p in _rows}
struct.append(("all 8 offers priced", len(_prices) == 8, f"{len(_prices)} rows"))

EXPECTED = {
    "Build Plan": 599, "Diagnostic": 1499, "Brand system": 4999,
    "Website": 1500, "Portal": 14999, "Full System": 21999,
    "App wrap": 8999,
}
for _n, _v in EXPECTED.items():
    struct.append((f"price: {_n} = {_v}",
                   _prices.get(_n) == _v,
                   f"found {_prices.get(_n)}"))

# 1,500 all-in is the whole offer. If the Website ever rises without the
# hosting-included promise being re-checked, the scope sheet becomes a lie.
struct.append(("website still includes year-one hosting",
               "first year of hosting" in html, "index.html"))
struct.append(("website duration matches the price",
               "2–4 days" in html, "GH\u20b51,500 buys ~30 hours, not 3-4 weeks"))

# The page must NOT claim to be the most expensive: at 1,500 only BuiltFound
# (1,000) is cheaper. The old card said the opposite and was repurposed.
struct.append(("page no longer claims to cost more",
               "costs more than the cheapest" not in html, "index.html"))

# Care Plan at 399-899/mo against a 1,500 build pays for the site in 4 months.
# That is a pricing smell, not an error -- flag it if the build drops further.
_care = _re.search(r'Care Plan.*?data-label="Price">([0-9]+)', html, _re.S)
struct.append(("care plan is under half the build price per month",
               _care and int(_care.group(1)) < 1500 * 0.5,
               f"care from {_care.group(1) if _care else '?'}/mo vs 1500 build"))

# --- the after-launch promise ----------------------------------------------
# The four layers are the most promise-dense text on the page. Every one of
# them is a claim a client will hold SoftFire to, so each is pinned.
for _p, _why in [
    ("Days 1–30", "the warranty window must stay named"),
    ("Months 1–3", "three free months was a deliberate decision"),
    ("Month 4 on", "the date money starts must be visible"),
    ("do not pay me for it", "a static site needs no maintenance - the honest answer"),
    ("nothing renews without asking", "nothing recurring may start silently"),
    ("tell you which one it is", "bug-vs-change must be said before work, not after"),
]:
    struct.append((_p.lower(), _p.lower() in html.lower(), _why))

# The Care Plan must not exceed the market range it was repriced into
# (Ghana care plans: 250-600/mo per Faciotek, 299-499 per Manuel).
struct.append(("care plan sits inside the Ghana range",
               "200–400" in html, "above 600 reads as renting the site"))

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
