# Packaging, presentation, and showing the work

How the offers are bundled, how they are presented, and how a studio with **no
portfolio** shows something worth looking at. Researched **2026-11-06**.

**FACT** (sourced), **INFERENCE** (my reasoning), **PROPOSED** (not decided).

---

## The finding that contradicts the current page

**FACT — the packaging research is unanimous, and it says the opposite of what the
site does.** A productised service should be sold as **three tiers**, named after
outcomes, with the **middle tier designed to be the one people choose**:

| | |
|---|---|
| Two tiers vs one | **~15% higher average revenue per user** |
| Including a middle tier | **17–25% higher conversion** |
| **Removing** the middle tier | **48–60% drop in revenue** |
| The classic decoy effect | preference for the target option shifting from **32% to 84%** |
| More than 3–4 options | **decision paralysis, lower conversion** |

**What SoftFire publishes today: eight offers in one table.** Build Plan,
Diagnostic, Brand system, Website, Portal, Full System, App wrap, Care Plan — all at
once, none recommended.

**INFERENCE — eight is not a menu, it is a decision the buyer has to make for you.**
Every extra row is a question they now have to answer, and the research says the
effect is a measurable drop in conversion. **The table is not wrong because it is
long. It is wrong because it does not say which one to buy.**

**PROPOSED — the fix, without deleting work already done:** keep the eight offers
(the vertical ladder is real, and the Portal→Full System jump needs explaining), but
add **one packaged card above the table** with three named tiers, and mark one as
the recommendation. The table becomes the *reference*; the card becomes the
*decision*.

---

## 1. The packaging: three tiers, named after the outcome

Tiers are named for what the client ends up with, not for the work. **The research
is explicit:** *"Launch-Ready Brand" beats "Brand Package B."*

| | **Launch** | **Operate** ← recommended | **System** |
|---|---|---|---|
| **For** | a business with nothing online | a business that is already trading | a business running on memory and paper |
| **You get** | 5 sections, live, in your name | everything in Launch, then looked after | a portal: records, staff, a process |
| **Sections** | 5 | 5 | 5 + up to 6 screens |
| **Hosting, year 1** | included, GH₵0 | included, GH₵0 | included |
| **Domain set up in your name** | yes | yes | yes |
| **Warranty** | 30 days | 30 days | 30 days |
| **Included after launch** | — | **3 months of changes + a monthly note** | 3 months |
| **Then** | — | GH₵200–400/mo, optional | quoted |
| **Delivery** | 2–4 days | 2–4 days | 6–8 weeks |
| **Price** | **GH₵1,500** | **GH₵2,250** | **GH₵9,999** |

### Why the middle one is the hero — and why it is honest

**FACT — the design rule:** the recommended tier should be **the highest-margin
option**, and priced at roughly double the entry tier, with the premium at 2–3× that.

| Tier | Price | Margin logic |
|---|---|---|
| Launch | GH₵1,500 | 30 hours = **GH₵50/h** — the floor |
| **Operate** | **GH₵2,250** | 30 hours + 3 months of onboarding at **1 hour/month** = 33 h → **GH₵68/h** |
| System | GH₵9,999 | 6–8 weeks; a different product entirely |

**INFERENCE — Operate is the hero for a real reason, not a trick.** The three free
months are already a decided cost (`MAINTENANCE.md`). Bundling them into the price
converts a **free gift into paid onboarding** — the client pays GH₵750 for twelve
hours of work that was going to be given away, and *both* sides are better off:
the client gets a relationship instead of a handover, and SoftFire stops absorbing
the 10% of build cost that the free months represent.

**And it fixes the biggest structural risk in the business:** the free months
currently have no invoice behind them, which is exactly how month four produces an
empty bill (`MAINTENANCE.md` §3.4).

### The premium tier's job — anchoring, not selling

**INFERENCE:** System at GH₵9,999 is not there to be bought often. It is there so
that GH₵2,250 reads as reasonable. **That is the honest use of anchoring** — the
anchor is a real product at a real price that a real client can buy, not a decoy
designed to be rejected. The research makes the distinction:

> *"For expensive, mission-critical expertise, I prefer the anchoring technique
> because it is more aligned with the best interests of the client, and there is
> nothing fake about it."*

**DECIDED — do not build a decoy.** A deliberately bad option to steer the buyer is
the one packaging tactic this brand cannot use, because it depends on the buyer not
understanding what they are looking at.

### What is not bundled, and why

| Not bundled | Why |
|---|---|
| the domain | the client pays the registrar directly — it is the ownership promise |
| email hosting | a separate purchase in their name |
| copywriting | the most common scope-creep source |
| the Brand system | it is a different decision, and bundling it forces it too early |

**INFERENCE:** bundling the domain would let SoftFire buy it "for" the client, which
is the exact thing `SECURITY-HOSTING.md` says not to do. **The packaging must not
quietly undo a principle.**

---

## 2. Presenting it: what the buyer sees, in what order

**FACT — the presentation rules from the research:** lead with the outcome, not the
deliverables; show three tiers side by side, cheapest left; highlight the middle;
name tiers after results; put subheaders saying who each is for.

**The order that follows, and why:**

| # | What the buyer sees | Why here |
|---|---|---|
| 1 | **The problem, in their words** | they must recognise themselves before they read a price |
| 2 | **Three tiers, side by side** | one decision, made once |
| 3 | **The middle one marked** | it is the one with the best outcome for both sides |
| 4 | **What is excluded** | before they ask, not after |
| 5 | **The eight-offer table** | reference, for the buyer who wants to compare |
| 6 | **The evidence** | the part that is currently empty — see §3 |

**INFERENCE — the order is the opposite of the current page.** Today the buyer meets
a ten-section page, then an eight-row table, then a defence of the price. **The
first thing they should meet is a decision.**

### 2.1 Raising the presentation, specifically

"Presentation" is not decoration. It is five observable things, all of them already
possible on this page:

| Element | The standard to hold |
|---|---|
| **Type** | one measure, 45–75 characters, already enforced at ten widths |
| **Whitespace** | the spacing scale, already in `tokens.css` — 0·4·8·12·16·24·32·48·64·96·128 |
| **Contrast** | every pair measured, already 0 failures at WCAG 2.2 AA |
| **Proof** | a number on the page that the buyer can check — 94 checks, 178 KB, 0 third-party |
| **Silence** | no stock photos, no icons, no "our values" tiles |

**INFERENCE — the last row is the one that raises presentation most.** A page that
shows fewer things, at a higher standard, reads as more expensive than a page that
shows everything. The three-tier card is *more* impressive than the eight-row table
even though it contains less, because it decides something for the reader.

### 2.2 The one presentation asset that does not exist yet

**FACT — the case study frame buyers recognise,** four blocks:

1. **Context** — who the client is and where the work sits
2. **Constraints** — time, budget, stack, approvals
3. **What you did** — the decisions and trade-offs, not the final file
4. **Outcome** — a metric if you have one, an honest reflection if you do not

**INFERENCE:** SoftFire has **exactly one** of these — BiteKasa — and it cannot be
used as a case study, because it is family, unpaid, and the brand says so
(`BRAND.md`). That leaves the portfolio genuinely empty. §3 is the answer.

---

## 3. Showing the work with no clients

There is a real, non-deceptive answer, and the research is specific about it. **It
has three parts: spec work, labelled honestly; the process made visible; and the
proof that already exists.**

### 3.1 What already exists and is not being shown

**INFERENCE — SoftFire is sitting on a portfolio it has not noticed.** Four assets,
all real, none of them a client:

| Asset | What it proves | How to show it |
|---|---|---|
| **This site** | a 178 KB page, ten widths, 94 verified claims, WCAG AA, 0 third-party | a "how this page was built" case study — the decisions, not the screenshots |
| **The six-document pack** | the thinking a client is buying | publish it. It is already published on the page |
| **The verifier** | a claim process no competitor has | 30 seconds of it running, or one screenshot of a failing check |
| **BiteKasa** | a live business, on WhatsApp, with a daily uptime cron | show it as **work built for family, with permission** — the brand already says exactly this |

**INFERENCE — the site itself is the strongest case study available,** because it is
the only one where every claim can be checked by the reader. *"This page is the
portfolio piece: here is why it is 178 KB, here is why the measure is 30em, here is
what a failing check looks like."* That is a studio showing its thinking rather than
its screenshots.

### 3.2 Spec work — the rule that makes it legitimate

**FACT — the only rule that matters:** label it, in the first ten seconds, every
time. *"Spec project, educational, not a live client engagement."* The research is
blunt about the alternative:

> *"Unlabeled spec work presented as if a real client paid for it — this is the
> fastest way to lose trust if a buyer asks a follow-up question you cannot
> answer."*

**FACT — the method that makes spec work credible:** pick a **real** subject, not a
fictional one. Redesign a real Accra business's clunky site, a real church's
nonexistent page. Real subjects allow a before-and-after and a real argument.

**PROPOSED — the spec piece worth doing:** take **one real local organisation** —
a church, a school, a shop with no website — rebuild one page, and publish the
case study with the label. Then ask them if they want the rest.

**INFERENCE — that is simultaneously a portfolio piece and a sales approach.** It
is the only asset in this document that is both.

### 3.3 The honest first-client offer, and why it is not "free"

**FACT — the research's advice, which matches what this repo already decided:**

> *"Free work attracts people who don't value it. A low, honest intro rate attracts
> real clients... Offer three or four introductory projects, deliver like it's a
> $5,000 job, and ask for a testimonial in return."*

**DECIDED — and this overrides the research's advice, deliberately: no discount.**
Not for the first three, not for anyone. The standard advice is an intro rate, and
it is wrong here for one reason: **this brand's entire claim is a number that does
not move.** A launch price is a number that moved.

**What replaces it — the offer gets bigger, not cheaper:**

| | |
|---|---|
| **Price** | GH₵1,500 — unchanged, published |
| **Scope** | the standard five sections, plus **a written case study**, published with permission, dated, and credited to them if they allow it |
| **Cost to SoftFire** | about two hours of writing it would do anyway |
| **What the client gets** | a published record of their project they can show their board, their family, their customers |

**INFERENCE — this is the better trade, and the arithmetic is on its side.** A
discount spends GH₵500 to buy a case study. **Adding the case study to the
deliverable spends two hours and zero cedis**, and it produces a *better* case
study — because the client has consented to it from the start and helped shape what
is said.

**And it protects the position.** A client who paid GH₵1,000 has learned the price
is negotiable and will tell the next buyer. A client who paid GH₵1,500 and got a
published case study has learned the price is real, and will also tell the next
buyer.

### 3.4 The case study, written for the first client

Using the four-block frame, with the honesty the research demands:

```
TITLE      A five-page site for [business type] in [area]
ONELINE    [They] had no website. They now have one that loads in under a
           second on a cheap phone, and they own every part of it.
CONTEXT    Two or three sentences. What the business does, who buys, what
           was wrong before.
CONSTRAINT Time. Budget GH1,500. One person. Content arrived late.
WHAT I DID The two or three decisions that mattered, and one thing I chose
           NOT to do. Include the excluded list.
OUTCOME    A number if there is one (load time, pages, checks passing).
           If there is not, say what you would measure next. Never invent one.
ARTIFACT   The live URL, and one screenshot at a readable size.
LABEL      If unpaid: "Built at an introductory rate in exchange for
           permission to publish this."
```

**INFERENCE — the "one thing I chose not to do" line is the most persuasive part of
a case study.** Anybody can list what they built. Naming what you refused — the
extra page, the animation, the stock photo — is the only part that proves judgement.

---

## 4. Bundling: the rules that keep it honest

| Rule | Why |
|---|---|
| **Bundle work, never bundle ownership** | the domain and accounts stay the client's, however the offer is packaged |
| **A bundle must be cheaper than its parts, and say so** | otherwise it is a bundle for your convenience |
| **No bundle may hide a cost the client will meet later** | the domain is GH₵146–260/yr and that is stated, not buried |
| **Never bundle a thing the client did not ask for** | the Brand system is not included because it forces a decision too early |
| **The middle tier must be the best outcome, not just the best margin** | if it is only better for SoftFire, the client finds out at renewal |

**INFERENCE — the last rule is the whole brand in one line.** Packaging is where a
studio is most tempted to optimise for itself. The test is whether the recommended
option is genuinely the one you would pick for a friend.

---

## 5. What to change on the page, in order

| # | Change | Effort |
|---|---|---|
| 1 | **Add the three-tier card above the offers table** — Launch / Operate / System, Operate marked | one section |
| 2 | **Retitle the offers table** from *"Eight ways in"* to *"Every offer, for reference"* — the table becomes the appendix, not the decision | one line |
| 3 | **Add the "how this page was built" case study** — the decisions, not the screenshots | one page |
| 4 | **Add the honest BiteKasa line** — built for family, with permission, not a client | already written in `BRAND.md` |
| 5 | **Publish the spec piece** once it exists, labelled | after §3.2 |

**INFERENCE — items 1 and 2 are one hour of work and they change what the page
*is*.** Today it is a reference document that happens to have prices. After them it
is a decision with a reference attached.

---

## 6. What I could not verify

| Unknown | Why it matters |
|---|---|
| Whether GH₵2,250 sells in this market | the middle tier is the whole model, and no one has tested it |
| Whether three tiers convert better than eight rows **here** | the benchmarks are SaaS and Western freelancers; Ghanaian buyers may read a long table as thoroughness rather than confusion |
| Whether a spec piece is read as generosity or as filler | cultural, untested |
| Whether a published case study is worth GH₵500 to a buyer | it is the replacement for a discount and nobody has been offered it yet |
| Whether the case study format works in a market that buys on WhatsApp | a PDF may never be opened; the case study may need to be a message |

---

## 7. Sources

- **Packaging and tiers:** aviy.ai package pricing guide (Jun 2026); mybworkshops.com
  (Sep 2026) on 1.5–2× delivery cost and tier spacing; damongo.com productised
  services (Sep 2026); assassinsonly.com agency productisation (May 2026);
  sarahzou.com Good-Better-Best (Jul 2026) — 15% ARPU, 17–25% conversion, 48–60%
  revenue drop, 32%→84% decoy shift; entrepedia.co bundle pricing (Feb 2026);
  botensten.com (Aug 2026); winwithoutpitching.com on decoy versus anchor.
- **Portfolio with no clients:** 1000incomes.com four-block case study frame
  (Jul 2026); remoteworks.pro (Feb 2026); mindhyv.com (Aug 2026); techcrier.com
  (Sep 2026); agencyshowcase.co.
- **Everything else:** this repository — `PRICING.md`, `MAINTENANCE.md`,
  `GROWTH.md`, `BRAND.md`.
