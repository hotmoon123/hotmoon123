# Maintenance, management, support and warranty

Deep research into the four things clients call "maintenance", why they must be
priced and promised separately, and how to structure three free months so they
build a paying relationship instead of a churn statistic.

Researched **2026-11-06**. Marked **FACT** (sourced), **INFERENCE** (my reasoning),
**PROPOSED** (a decision that is not yet made).

---

## The short version

**On a static site there is almost nothing to maintain.** No database, no plugins,
no CMS to patch, SSL renewed automatically by the host. Sourced, twice:

> "A static site with no database, no plugins and no transactions has a fraction
> of the attack surface, so a quarterly once-over of content, links, forms and
> certificate renewal can genuinely be enough." — redeagle.tech, 2026

> "Less, but not zero... What remains: keep the domain renewed in your own account,
> test the contact form monthly, keep content current, and check analytics still
> fire." — rmcm.io, 2026

**That is the finding the whole model has to be built around.** If SoftFire sells
"maintenance" after a GH₵1,500 static build, it is charging a monthly fee for
work that does not exist — exactly the quiet dishonesty this brand is built
against. **The product is management, not maintenance.** They are not the same
job, and the difference is what the client is actually paying for.

---

## 1. Four words, four different jobs

Most studios sell one thing and call it three. They are separable, and the axis
that separates them is not "how much" — it is **what triggers the work and what
proves it happened.**

| | **Warranty** | **Support** | **Maintenance** | **Management** |
|---|---|---|---|---|
| **The question** | Who pays when it's broken because of you? | Who do I message? | Is it still working? | Is it still useful? |
| **Trigger** | you report a defect | you have a problem | the calendar, or an alert | you have a new fact |
| **What it covers** | bugs against the signed scope | the human layer between you and a fix | updates, backups, uptime, SSL, security | content, prices, photos, sections, search visibility |
| **Who pays** | nobody — it is our mistake | nobody, within the plan | the retainer, or nobody on a static site | the retainer |
| **Evidence it happened** | a fixed defect, same spec | a reply, within an agreed time | change log, restore test | an updated page, approved |
| **Fails when** | scope was not written down | nobody answers | there is nothing to update | nobody knows what changed in the business |
| **Ends** | on a named date | usually never | when the platform needs nothing | when the client stops changing |

**FACT — the industry treats these as distinct.** A 2026 comparison defines care
as keeping content current, maintenance as keeping the platform stable and
recoverable, and management as "operating the website as an accountable business
asset" — with different evidence for each: updated URLs, backup logs, and an
operations report. Another source puts the split plainly: *"maintenance is about
support, management is about growth."*

**INFERENCE — the sentence that makes it obvious to a client:**

> **Maintenance asks "is it still working?" Management asks "is it still true?"**

A shop changes its prices. That is management. A form stops sending. That is
maintenance — but on a static site it is almost always the mail provider's fault,
not the site's.

---

## 2. What a static site actually needs, month by month

This matters because the retainer must be priced against real work, and the real
work is small. **FACT** — the published cadence for a static brochure site:

| Cadence | Time | What |
|---|---|---|
| **Weekly** | ~0 min | nothing. No plugins, no core, no database |
| **Monthly** | 10–15 min | submit the contact form and check it landed · click the main links · confirm SSL is valid |
| **Quarterly** | 30–60 min | sweep for stale content (hours, prices, staff, copyright year) · re-read the two most important pages as a stranger · check images are not huge |
| **Annually** | 15 min | domain renewal — **which the client owns**, so it is their reminder, not ours |

**That is roughly two hours a year of genuine technical work.** A GH₵1,500 build
does not justify a GH₵300/month maintenance plan, and a client who works it out
will feel cheated — correctly.

**INFERENCE — what the retainer must therefore be.** Not "we keep it running."
That is nearly free and nearly meaningless. The retainer sells:

1. **Someone accountable who answers.** The support layer. This is what small
   businesses in this market actually cannot buy elsewhere.
2. **Changes made without a project.** New prices, new photos, a new section, a
   seasonal banner. Each one is 20 minutes and each one would otherwise sit undone
   for a year.
3. **A judgement about whether the site is still true.** The quarterly sweep is
   the only piece of real technical work, and it takes an hour.

---

## 3. The three-months-free problem

Three free months is a **generous** decision and a **risky** structure. Four
pieces of evidence say why.

### 3.1 What it costs at GH₵1,500

The build is GH₵1,500 for about 30 hours — **GH₵50/hour**, the local freelance
floor. Whatever is given free in months 1–3 comes straight off that.

| Design | Free hours | Value at GH₵50/h | % of the build |
|---|---|---|---|
| "Unlimited changes, 3 months" | 12–20 | GH₵600–1,000 | **40–67%** — the job runs at a loss |
| 2 changes/month + monthly check | ~7.5 | GH₵375 | 25% |
| **1 hour per month, capped** | **3** | **GH₵150** | **10% — affordable** |

**INFERENCE:** the free period only works if it is **capped in hours, in writing,
at handover**. "Three months free" without a cap is an open-ended promise at
GH₵50/hour, and the client who uses it most is the one who pays least.

### 3.2 Free trials convert worse, and churn more

**FACT — the benchmarks** (2026 surveys of 200 products and 89 SaaS companies):

| Structure | Trial → paid |
|---|---|
| Free trial, no card | **4–6% good; 10–15% great** |
| Free trial, card required | 25–35% good |
| Median across all | **8%** |

**FACT — and the one that matters most.** A study of **16,512 customers** of a
subscription service offering a three-month free trial found:

> **48% of free-trial customers churned**, against **34%** of customers who signed
> a regular contract.

**INFERENCE — read that carefully.** A three-month free trial does not just fail
to convert; it **attracts a population that leaves more often.** Being free for a
quarter teaches the client that the service costs nothing, and the moment it
stops being free is the moment the relationship is tested. The trial selects for
people who were never going to pay.

That is not an argument against three free months. It is an argument for
**structuring it as an onboarding period, not a trial** — see §4.

### 3.3 The conversion moment is where it goes wrong

Three failure modes, all common:

1. **The surprise invoice.** Month 4 arrives, the client did not know, feels
   trapped, pays once, cancels. **Avoidable with one sentence at handover.**
2. **The silent lapse.** Nobody says anything, the client assumes it is still
   free, three more months pass, and asking for money now is awkward. **Avoidable
   with a date.**
3. **The empty invoice.** The client used nothing for three months, then is asked
   for GH₵200/month. There is no evidence the service does anything. **This is the
   one that kills it, and it is the most likely.**

### 3.4 The invoice that has nothing behind it

**INFERENCE — the decisive risk.** On a static site, a client who asked for zero
changes in three months has received, in truth, nothing they can point to. Asking
them to start paying is asking them to buy an absence.

The fix is not salesmanship. It is **making the three months produce visible
artefacts**: three monthly check notes, a written list of what was checked, and at
least one change they asked for. Then month four has a receipt.

---

## 4. The recommended structure: three layers, three dates

**PROPOSED.** Each layer has a different job, a different boundary and a different
price — and the client is told all three at handover, in writing, with dates.

### Layer 1 — Warranty: **30 days, free, bugs only**

**FACT — 30–90 days is the industry norm** for post-launch defect fixes. Thirty
days is defensible at GH₵1,500; ninety is what a larger project would buy.

**The boundary is the whole thing.** Every source agrees that disputes start where
"bug" meets "change":

> A bug is something built that does not work as specified. A change is something
> that works correctly but that you now want differently.

The clause, in SoftFire's voice — plain, no legal fog:

> **For 30 days after launch I fix, free, anything that does not work the way the
> signed scope said it would. If it works and you want it different, that is a
> change, and changes are quoted before I start. I will always tell you which one
> it is before I touch it.**

**INFERENCE:** that last sentence is worth more than the clause. It converts a
boundary from a trap into a service.

**Start date:** the launch date, not the acceptance date — but state which. The
research recommends tying it to acceptance, because a slow client ramp means bugs
surface late. At GH₵1,500 with a 2–4 day build, the gap is not material. **Use
launch, and say "launch" explicitly.**

### Layer 2 — Onboarding: **months 1–3, free, capped at 1 hour per month**

Rename it. It is **not a trial**, and the word "trial" is what produces the 48%
churn. It is the period where the client learns what the plan does.

**What is included, in writing:**

| | What |
|---|---|
| **Up to 1 hour of changes per month** | one price change, one photo swap, one paragraph — not three |
| **One monthly check note** | sent by WhatsApp: what I checked, what I found, what I changed. **This is the receipt** |
| **The 30-day warranty runs inside it** | months 1–3 include bugs, at no cost, as Layer 1 |
| **A reply within 48 hours** on weekdays | stated, and kept, because it is countable |
| **Unused hours do not roll over** | otherwise month 4 is a negotiation about a bank balance |

**What is not included:** new pages, new sections, a redesign, copywriting,
photography, hosting moves, or anything over an hour. Those are quoted.

**Why cap at one hour:** it is 3 hours total, **GH₵150 at GH₵50/hour, 10% of the
build.** Affordable, bounded, and enough to prove the service works. Uncapped, the
same promise is a 40–67% loss on the job.

### Layer 3 — Care Plan: **month 4 onward, paid**

This is where the money either is or is not. **PROPOSED pricing below.**

| | **Care** | **Care Plus** |
|---|---|---|
| **PROPOSED price** | **GH₵200/month** | **GH₵400/month** |
| Changes included | 2 per month (≈2 h) | 5 per month (≈5 h) |
| Monthly check note | yes | yes |
| Reply time | 48 h weekdays | 24 h weekdays |
| Quarterly content sweep | yes | yes |
| Domain + SSL renewal reminder | yes | yes |
| Monthly one-page report | — | yes |
| Implied hourly rate | **GH₵100/h** | **GH₵80/h** |

**The arithmetic that makes it honest:** at GH₵200 for ~2 hours, the implied rate
is GH₵100/hour — **the middle of the local freelance range (GH₵50–200)** and
double what the build earns. That is not a rip-off; it is what small, frequent,
interrupting work is worth.

**Market check — FACT:** Ghana care plans run **GH₵299–499/month** (Manuel
Technologies) and maintenance packages **GH₵250–600/month** (Faciotek).
International management retainers run **$79–299/month** (GH₵950–3,600). At
GH₵200 SoftFire sits **below the Ghanaian market** — consistent with a GH₵1,500
build that is also below it.

**INFERENCE — the honest caveat to put in the plan document:** *"Most months
there will be less than an hour of work. You are not paying for hours; you are
paying for someone to be there and to notice."* Saying that out loud is what makes
the fee survivable when a quiet month comes.

---

## 5. Making the three months produce a receipt

The month-4 conversation should be about evidence, not opinion. Four things, all
free to produce, all hard to argue with:

1. **Three check notes.** One per month, WhatsApp. "Checked: form sends, all links,
   SSL valid, page loads in 1.2s on 3G. Changed: your Saturday hours. Nothing
   broken." Twelve lines. **This is the artefact.**
2. **A change count.** "You asked for four changes in three months. The plan
   covers two a month. You used it." — or, if they used none: *"you did not need
   it, so do not pay for it."* **Say that. It is the brand.**
3. **One thing found and fixed that they did not ask about.** A broken link, a
   price that no longer matched, a 4 MB photo. Management is *noticing*.
4. **A dated sentence at handover:** *"Your first three months are included. On
   **4 February 2027** the plan costs GH₵200 a month. Nothing happens
   automatically. If you do nothing, the site stays up and I stop."*

**INFERENCE — that last line is the most important sentence in this document.**
Nothing recurring should ever start without an explicit yes. A silent rollover is
how a studio that trades on fixed, written prices loses the plot.

---

## 6. What this does to the business

**FACT by arithmetic.** The build is GH₵1,500, once. The plan is GH₵200/month.

| Clients on the plan | Year 1 recurring | What it compares to |
|---|---|---|
| 5 | GH₵12,000 | 8 builds |
| 10 | GH₵24,000 | 16 builds |
| 20 | GH₵48,000 | 32 builds |

**INFERENCE — the retainer is the business, not the afterthought.** Ten retained
clients earn more per year than sixteen builds, and they do it without a new
sales conversation. This is the same logic as the stated vision: the way out of
"revenue is bounded by hours" is a recurring product, not more projects.

**And it is why the GH₵1,500 build is defensible at all.** A cheap build that
converts to a retainer is a customer acquisition cost. A cheap build with no
retainer is just cheap.

**WARNING — INFERENCE.** That makes the three free months a **sales cost**, and it
must be counted as one. If 3 clients take the free months and 0 convert, the cost
is 9 hours — GH₵450 — spread across those builds. Tolerable. If the pattern
repeats across a year, the model is broken and the free period should shrink to
30 days.

**The test to run for the first three clients:** how many converted, and how many
changes did they ask for? Those two numbers decide whether GH₵200 or GH₵150 is the
right price, and whether three months was too generous.

---

## 7. The words to use

| Do not say | Say |
|---|---|
| "maintenance plan" | "the monthly plan" — because you are not maintaining anything |
| "3-month free trial" | "your first three months are included" |
| "unlimited changes" | "two changes a month" |
| "we keep your site secure" | "I check it once a month and tell you what I found" |
| "24/7 support" | "a reply within 48 hours on weekdays" |
| "cancel anytime" | "cancel by the 25th and the next month is not billed" |

**INFERENCE:** every right-hand column is smaller, less impressive, and true. That
is the trade this brand makes everywhere, and it is the same trade here.

---

## 8. The deal in one paragraph, for the client

> **Your first three months are included.** That is up to an hour of changes each
> month — a price, a photo, a paragraph — plus a note from me saying what I
> checked. The 30-day warranty on the build runs inside that first month. After
> three months, the plan is GH₵200 a month for two changes a month and the same
> monthly note. Nothing starts automatically and I will not invoice you without
> asking. If you never change anything, do not pay me — a static site does not
> need looking after, and I would rather tell you that than sell you something.

---

## 9. What I could not verify

| Unknown | Why it matters |
|---|---|
| **What SoftFire's clients will actually ask for** | The whole plan is priced on "2 changes/month". Nobody has asked yet. Track the first three clients |
| **Whether GH₵200 converts in Ghana** | The market benchmarks are GH₵250–600, which is *higher*; conversion is untested at either number |
| **Real hours per change** | "One hour per month" is my estimate, not a stopwatch. Time the first ten changes |
| **Whether 48 hours is keepable** | One person, no backup. A promise you miss is worse than a slower promise you keep. Consider 72 hours |
| **The 3-month churn finding's applicability** | The 48%-vs-34% study was subscription TV, not web care. The direction is instructive; the magnitude is not transferable |
| **Ghanaian consumer-protection limits on auto-renewal** | Not researched. The recommendation to make every renewal explicit is a brand decision that happens to be safe either way |

---

## Sources

- Care / maintenance / management distinctions: itsystems.vn comparison, cindaro.com,
  webcarestudios.com, brandstoryglobal.com, gairy.co, creatricx.com, emilyjourney.com
  — all read November 2026.
- Static-site maintenance cadence and attack surface: redeagle.tech "Website
  Maintenance UK" (2026), rmcm.io "Website maintenance: what breaks, what it costs"
  (Jul 2026), solodigitaldesign.com (Aug 2026), web.adhdaptive.org.
- Warranty norms and the bug/change boundary: story.law "Dev agency warranty and
  support terms" (Aug 2026), witscode.com "Web design contracts: 7 clauses"
  (Mar 2026), hyberx.com contract guide (Jul 2026).
- Free-trial conversion and churn: ChartMogul 2026 survey of 200 products;
  FirstPageSage conversion benchmarks (Nov 2026); 1capture.io (Oct 2026);
  Datta, Foubert & van Heerde study of 16,512 free-trial customers (reported 2026).
- Ghana retainer pricing: Manuel Technologies, Faciotek "Website Maintenance Costs
  Ghana 2026".
