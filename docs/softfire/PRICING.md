# What ₵1,500 actually buys

Research into every cost between first conversation and a live site, done on
**2026-11-06**, so a flat ₵1,500 price can be quoted without discovering the loss
afterwards.

Every figure is marked **FACT** (published, sourced), **INFERENCE** (my
arithmetic) or **UNVERIFIED** (I could not confirm it and will not assume it).

---

## The short version, before the tables

**₵1,500 all-in is survivable — but only if the domain is `.com` and the hosting
is static.** The moment a `.com.gh` domain goes into the price, the job runs at a
loss on day one.

| | Cheapest | What it means at ₵1,500 |
|---|---|---|
| `.com` domain, 1 year | ₵146 | 10% of the price |
| `.com.gh` domain, 1 year | ₵750 | **50% of the price, every year** |
| `.com.gh` at the dearer registrars | ₵1,690 | **more than the entire price** |

And the second finding matters more than the first: **₵1,500 is about 15–30 hours
of work.** That is two to four working days, not three to four weeks. The current
page promises the Website in "3–4 weeks". Those two numbers cannot both be true.

---

## 1. What everything costs — the research

### Domains (FACT — registrar price lists, November 2026)

| Extension | Registrar | First year | Notes |
|---|---|---|---|
| `.com` | NindoHost | ₵146 | |
| `.com` | GOnline | ₵190 | |
| `.com` | HostAfrica | ₵260 | |
| `.com` | Truehost | $7.75 (~₵95) | |
| `.com.gh` | GOnline | **₵750** | |
| `.com.gh` | NindoHost | **₵1,690** | |
| `.com.gh` | Nakroteck | $80 (~₵980) | |
| `.com.gh` | register.domains | $148.99 (~₵1,820) | on sale 1st year |
| `.com.gh` | Intername | £124 (~₵1,950) | + £124/yr local agent |

**The Ghana registry's own guideline still quotes ₵200** for a `.gh` domain. That
page is stale — every accredited registrar sells `.com.gh` at **4–9× that**. Treat
the registry figure as historical, not a price you can get.

**FACT — requirements for `.com.gh`:** you must produce either a **company
registration certificate** or, as an individual, a **passport or Ghana Card**, and
registration takes **about 10 days**. That means the `.com.gh` cannot be bought
during the build — it has to be started in week one, or the site launches on
something else.

**INFERENCE:** `softfire.com.gh` at ₵750 is not a hosting cost, it is a **brand
cost** that recurs every year forever. It is cheaper to register the business name
(₵190) and park the domain than to buy the domain before the business exists.

### Hosting (FACT — Ghanaian hosts, November 2026)

| Type | Annual cost | Who |
|---|---|---|
| **Static (GitHub Pages / Cloudflare Pages)** | **₵0** | what this site already uses |
| Shared cPanel, entry | ₵105–275 | UltraHost ¢105, VumaHost ₵275 |
| Shared cPanel, mid | ₵480–1,100 | OvationHall ₵480, VumaHost ₵1,100 |
| Business hosting | ₵200–500 | Faciotek market guide |
| VPS | ₵500–2,000+ | Faciotek market guide |
| SSL certificate | ₵0 | Let's Encrypt, included by every host above |

**FACT:** the site this brand is built on transfers **178 KB total** and serves
from a static host. It needs none of the above. A cPanel plan at ₵275 would be
buying a database, email accounts and a control panel that a five-page brochure
site does not use.

### The rest of the stack

| Item | Cost | Mark |
|---|---|---|
| Business name registration (ORC, 2026 schedule) | ₵130 + ₵30 name search + ₵30 certified copy = **₵190 once** | FACT |
| Business name annual renewal | ₵70/yr | FACT |
| Limited company (if ever needed) | ₵585 + 1% capital duty on stated capital | FACT |
| MoMo merchant fee on the receipt | **0.75–1.5%** of the job | FACT |
| Mobile-money E-Levy | **abolished** — repealed 2 April 2025 | FACT |
| MoMo → bank transfer fee | 0.75% capped ₵5, announced June 2026, **suspended by Bank of Ghana** | FACT |
| VAT | **20–21.9% effective**, but only above ₵200,000 turnover | FACT |

**Two corrections to things commonly believed:**

1. **E-Levy is gone.** It was repealed on 2 April 2025. Any cost model that adds
   1.5% to mobile-money receipts is out of date.
2. **You are not VAT-registered and should not be.** The threshold is
   ₵200,000 annual turnover. At ₵1,500 a site that is 133 sites a year. Prices
   should be quoted **VAT-inclusive as a flat number** and the page should not
   discuss VAT at all — mentioning it invites a question with no good answer.

### What the market charges (FACT — published 2026 price lists)

| Source | Price for a small business site |
|---|---|
| Study of 75 Ghanaian firms (2024) | average **₵2,660**; agencies **₵3,460**; freelancers **₵827** |
| Manuel Technologies | starter ₵2,000–3,500; business ₵4,500–6,000 |
| Websys | 5 pages ₵2,500 |
| YookuWeb | ₵1,500 starter, ₵2,500 business |
| BuiltFound | ₵1,000–1,600 |
| KayTech | ₵3,500 |
| Ghanaian developers on r/TechGhana | "with hosting and domain, I charge ₵3,000 and above" |
| Hourly rates | freelancers **₵50–200/hr**; agencies ₵100–500/hr |

**INFERENCE — the one real advantage of ₵1,500 all-in:** every competitor above
**excludes** the domain and hosting. Manuel Technologies says so explicitly on its
price list. A ₵1,500 that *includes* year-one hosting is genuinely cheaper than a
₵1,500 that does not. That is worth one sentence on the page and it is the
strongest honest claim available at this price.

---

## 2. The arithmetic

### Cost of goods on a ₵1,500 job

| Line | `.com` + static | `.com.gh` + cPanel |
|---|---|---|
| Domain, year 1 | −146 | −750 to −1,690 |
| Hosting, year 1 | 0 | −105 to −480 |
| SSL | 0 | 0 |
| MoMo merchant fee (1%) | −15 | −15 |
| **Direct cost** | **−161** | **−870 to −2,185** |
| **Left before your time** | **₵1,339** | **₵630 to −₵685** |

**FACT by arithmetic:** the `.com.gh` version is loss-making at the cheap end
(−₵685) and impossible at the dear end. The `.com` version leaves ₵1,339 for
your labour.

### What your labour is worth at ₵1,500

| If you bill | Hours available | Working days (8h) |
|---|---|---|
| ₵50/hr — the local freelance floor | **30** | 3.75 |
| ₵100/hr | 15 | 1.9 |
| ₵200/hr — the freelance ceiling | 7.5 | 0.9 |
| ₵350/hr — agency mid-rate | 4.3 | 0.5 |

**INFERENCE:** ₵1,500 buys between **15 and 30 hours**. Not 3–4 weeks. Call it
**2–4 working days**, and the scope must be written to fit in 30 hours or the
margin disappears silently while you are being helpful.

### The only way 30 hours is enough

A five-page custom site designed from nothing takes 60–80 hours. At ₵1,500 that
is **₵19–25/hour**, below the market floor, for the hardest work.

Thirty hours is enough **only if the site is assembled from a system you already
own** — the layout, type scale, components and checks that built this very page.
Then the work is content and configuration, not design.

**This is the whole decision.** ₵1,500 is a viable price for a *productised* site.
It is not a viable price for a bespoke one. The difference is not effort — it is
whether you are designing or configuring.

---

## 3. What ₵1,500 includes — the scope sheet

Written as the client would read it. This is the document that goes on page one of
the quote.

### Stage 1 — Requirements (2 hours)
- One 45-minute call, video or in person
- You tell me what the business does, who buys, and what a visitor must be able to
  do in the first five seconds
- I send a **one-page written scope**: pages, sections, exclusions, price, date.
  **This is the fixed price.** It does not move after you sign it.
- You send what you have: logo, photos, price list, phone number, any text

### Stage 2 — Structure (2 hours)
- Page plan and section order, sent for one round of comments
- **One revision round on the plan.** A second round is a new written number.

### Stage 3 — Content (3 hours)
- I place your text and images
- **Light editing only**: spelling, grammar, trimming to fit. I do not write your
  copy from nothing, and I do not research your industry for you
- If you have no text, I send a **one-page worksheet** with the questions to answer.
  Filling it in is your job, and the date moves if it arrives late

### Stage 4 — Build (12 hours)
- **Up to 5 sections** (Home, About, Services/Products, Contact, and one more)
- Assembled from the existing SoftFire system — the same type scale, spacing,
  components and checks as this page
- Responsive at 320, 360, 390, 430, 480, 768, 1024, 1280, 1440 px
- No custom illustration, no bespoke art direction, no new component library
- One contact route: WhatsApp click-to-chat, a form, or a phone number. **One.**

### Stage 5 — Test (3 hours)
- Every link followed, every form sent to a real inbox
- Contrast checked against WCAG 2.2 AA on every text/background pair
- Widths checked for horizontal scroll
- Load measured on a throttled connection — **budget: under 1 MB, and it will be
  far under because it is static**
- Mobile checked on a cheap Android, not on a laptop with a narrow window

### Stage 6 — Domain and hosting (2 hours)
- **You buy the domain in your own name.** I sit with you or walk you through it.
  ₵146–260 for a `.com`, paid by you, in your account
- DNS pointed, SSL issued, `www` and non-`www` both resolving
- Hosting: **static, on GitHub Pages or Cloudflare Pages, year one included at
  ₵0 cost.** No cPanel, no database, no monthly bill
- Email: **not included.** A business inbox is a separate purchase — Zoho or Google
  Workspace, from about $1/user/month, bought in your name

### Stage 7 — Handover (2 hours)
- One 30-minute session, recorded, showing you how to change text and photos
- **Every account in your name**: domain registrar, hosting, GitHub, analytics. You
  keep them if we ever stop working together
- Written handover sheet: what is where, who to call, what to do if the site breaks
- **30-day warranty**: anything that does not work as specified, I fix free. New
  requests are not warranty

**Total: about 30 hours.**

### What ₵1,500 does not include
Logo or brand design · copywriting beyond light editing · photography ·
e-commerce or payments · customer accounts or logins · a database · booking
systems · more than 5 sections · more than one revision round · content migration
from an old site · email hosting · `.com.gh` domain fees · anything after day 30 ·
SEO beyond the basics (titles, descriptions, one clean structure — **no ranking
promise, ever**)

### Why the exclusions are this specific
Because ₵1,500 only works if the boundary is real. A single "can you also just—"
is fine once. Three of them is a different job sold at the wrong price. The
exclusions are on page one so that saying no later is not a surprise.

---

## 4. Maintenance is not management

The instruction was that maintenance and management are separate things. They are,
and the difference decides whether you can sell either one honestly.

| | **Maintenance** | **Management** |
|---|---|---|
| What it is | keeping it working | running it for you |
| Work | updates, backups, SSL renewal, broken links, uptime, security patches | new photos, price changes, new pages, news posts, answering enquiries |
| When | reactive — something breaks | planned — you want something changed |
| Frequency | near zero on a static site | a few times a month |

**FACT:** a static site has no database, no plugins and no CMS to patch. There is
almost nothing to maintain. **INFERENCE:** that means a monthly *maintenance*
retainer on a static build is charging for work that does not exist. Selling one
would be exactly the kind of quiet dishonesty this brand is built against.

**What to sell instead:**

1. **Nothing.** ₵0/month, and say so. "Your site has no database and no plugins.
   There is nothing to maintain. I will fix it free for 30 days, then it is yours."
   That is a stronger differentiator than any care plan, because every competitor
   is selling the retainer.
2. **Management, priced per change.** A published rate — e.g. ₵250 per change
   request, or ₵600/month for up to 3 changes. Honest, because you do the work.
3. **A managed rebuild** only if they move to a CMS, which is a different — and
   much more expensive — product.

**Market comparison (FACT):** care plans in Ghana run **₵299–499/month**
(Manuel) and maintenance packages **₵250–600/month** (Faciotek). The existing
₵300–700/month Care Plan on the page sits at the top of that range. **INFERENCE:**
at a ₵1,500 build, a ₵300/month plan pays for the site in five months — which
reads to a buyer as *"the retainer is where the money really is"*, and at these
volumes it is the honest reading.

---

## 5. What this does to the site as it stands

Published before this research, now contradicted:

| On the page now | Problem |
|---|---|
| Website **₵4,999** | becomes ₵1,500 |
| Website **"3–4 weeks"** | is really **2–4 working days** at this price |
| **"Why this costs more than the cheapest quote"** card | **false at ₵1,500.** BuiltFound 1,000, YookuWeb 1,500, Websys 2,500, KayTech 3,500 — SoftFire would be tied-second-cheapest, not dearest |
| Care Plan **₵399–899/mo** | above market, and implies maintenance that a static site does not need |
| Portal ₵14,999 · Full System ₵21,999 | still defensible — a portal is genuinely a different product — but the **10× jump** from ₵1,500 needs one sentence explaining why |
| Build Plan **₵599** credited | at ₵1,500 a ₵599 deposit is 40% and leaves ₵901 for the build. Thin |

**The card does not get deleted. It gets repurposed.** At ₵1,500 the risk inverts:
the danger is no longer "why are you expensive", it is **_"what is not included for
₵1,500"_**. The card should become the scope sheet from section 3 — which is
exactly the document requested, and the thing no competitor publishes.

**INFERENCE — the strategic cost, stated plainly.** ₵1,500 puts SoftFire at the
freelancer average (₵827) end of the market rather than the agency end (₵3,460).
The price stops being evidence of quality and becomes evidence of accessibility.
That is a legitimate choice — it is *not* a mistake — but the brand then has to do
the trust work entirely through published process, because the price is no longer
signalling anything. The "fixed price" position survives. The "premium" one does
not, and was never really there.

---

## 6. The recommended ladder

Every number below is **PROPOSED**, not decided. Only ₵1,500 is your instruction.

| Offer | Now | Proposed | Why |
|---|---|---|---|
| **Website** | 4,999 | **₵1,500** | your decision. 5 sections, year-1 hosting included |
| **Build Plan** | 599 | **₵300** credited in full | at ₵1,500 a ₵599 deposit is 40%; ₵300 is a real commitment without eating the margin |
| **Brand system** | 4,999 | **₵2,500** | cannot exceed 1.7× the site it dresses |
| **Diagnostic** | 1,499 | **₵800** | a week of thinking |
| **Portal** | 14,999 | **₵9,999** | still 6.7× — a genuine software product |
| **Full System** | 21,999 | **₵16,999** | |
| **App wrap** | 8,999 | **₵4,999** | |
| **Care Plan** | 399–899/mo | **₵250 per change, or ₵600/mo for 3** | management, not maintenance — see §4 |

**`.99` is gone, as instructed.** ₵1,500 exactly, and whole numbers elsewhere.

---

## 7. What I could not verify

| Unknown | Why it matters |
|---|---|
| **Ghanaian VAT on services under ₵200,000** | I found the threshold and the rates, not a worked example for a sole trader. **Ask an accountant before printing "VAT inclusive".** |
| Actual `.com.gh` price at the registry counter | Registrars quote 4–9× the registry's own stale figure. Only the counter knows |
| Hosting renewal prices after year 1 | Several hosts discount year one. Static hosting at ₵0 has no renewal trap, which is another argument for it |
| Your real hours per site | The 30-hour budget is my estimate from the scope, not your stopwatch. **Track the first one.** |
| MoMo merchant rate you would actually get | 0.75–1.5% is an industry range. Your registration decides it |

---

## Sources

- Domain and hosting prices: Truehost GH, HostAfrica, NindoHost, GOnline, Nakroteck,
  register.domains, Intername, VumaHost, UltraHostGhana, OvationHall, Bavin —
  published price pages, read November 2026. Registry guidelines: register.com.gh.
- Hosting and maintenance ranges: Faciotek "Website Maintenance Costs Ghana 2026".
- Market pricing: Manuel Technologies, Websys, YokuWeb, BuiltFound, KayTech,
  GHReact study of 75 firms, r/TechGhana — read November 2026.
- MoMo fees: MTN Ghana published tables; E-Levy repeal 2 April 2025; BoG statement
  suspending the 0.75% wallet-to-bank fee, May 2026.
- VAT: GRA; Act 1082; 2026 commentary on the 20% combined effective rate and the
  ₵200,000 threshold.
- Business registration: ORC 2026 fee schedule, effective 2 February 2026.
