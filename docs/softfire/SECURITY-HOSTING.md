# Where security and hosting belong

Two questions: **is security part of maintenance/management?** and **should hosting
be separate, or bundled in?** The answers are not the same shape, and the security
one is counter-intuitive.

Researched **2026-11-06**. **FACT** (sourced), **INFERENCE** (my reasoning),
**PROPOSED** (not decided).

---

## The answers, before the reasoning

**Security: mostly not a service on a static site — it is a launch checklist.**

Of the 20 controls a security guide lists for a typical website, **eleven do not
apply at all** to a static site: there is no CMS to patch, no plugins, no
database, no login, no server to harden, no WAF needed for a page with no input.
What remains is **account security and DNS** — and that is *setup*, done once,
not a monthly task. Charging a retainer for "security monitoring" on a static
site is selling an alarm on an empty room.

**The exception, and it is the real risk: the client's accounts.** Registrar,
email, GitHub, hosting. Most breaches start with one stolen login — not with the
website. That risk is reduced by **2FA and registrar lock**, once, for free.

**Hosting: separate, named, and at cost — GH₵0.**

Because it genuinely is GH₵0 on static hosting, and a named GH₵0 line is a
**marketing asset** rather than a missing revenue stream. Every competitor hides
hosting inside a retainer so the client cannot compare. Publishing "hosting: free,
because there is no server" is the same move as publishing the price.

---

## 1. Security: what actually applies

The standard agency security checklist has 20 items. Applied honestly to a
5-section static site:

| Control | Applies? | Why |
|---|---|---|
| Patch CMS / plugins / themes | **No** | there are none |
| Harden server / disable directory listing | **No** | no server of ours; the host's job |
| Database privileges, SQL injection | **No** | no database |
| Login hardening, lockout, admin usernames | **No** | no login |
| WAF, rate limiting, bot mitigation | **No** | no input to abuse; a CDN already absorbs load |
| Malware scanning | **No** | static files cannot execute |
| Vulnerability/dependency scanning | **No** | no dependencies shipped to the browser |
| Daily backups | **Mostly no** | the source is in git, on the client's own account. A backup is a copy of a repo |
| **HTTPS enforced** | **Yes** | automatic on the host, but must be *verified* |
| **TLS current, cert renewed** | **Yes** | automatic; verified once |
| **Security headers** | **Partly** | see §2 — depends on the host, not on us |
| **Registrar lock + transfer lock** | **Yes** | free, one click, prevents hijacking |
| **2FA on registrar / email / GitHub** | **Yes** | the single highest-value control there is |
| **DNSSEC** | **Yes if supported** | free-ish, prevents DNS spoofing |
| **SPF / DKIM / DMARC** | **Yes, if email is on the domain** | prevents someone invoicing a customer as you |
| **Uptime monitoring** | **Yes** | free, and the one genuinely recurring check |
| **Domain expiry watch** | **Yes** | the most common way a small site dies |
| **Quarterly record audit** | **Yes** | 15 minutes, catches drift |
| Privacy / cookie policy | **No** | no cookies, no analytics that track, no tracking scripts |

**INFERENCE — the honest count: 9 of 20 apply, and 7 of those 9 are done once at
launch.** The two that recur are uptime alerting and the domain renewal watch,
and both are free automation plus a calendar reminder.

**FACT — the checklists themselves say the risk is accounts, not the site:**
*"Most breaches start with one stolen or reused login"* (securelayer7, 2026);
*"If someone else gets the keys, encryption and firewalls downstream won't
matter"* (viserx, 2026). Another puts the domain plainly: *"the registrar account
is the master key; treat it accordingly."*

**That is the tell.** The thing worth securing on a static site is not the site.
It is the client's registrar and email — and no retainer can secure those for
them. They have to hold the keys, which is exactly what this brand already
promises.

---

## 2. The finding that decides it: GitHub Pages cannot send headers

This closes a gap that has been open in this project since the first audit
("clickjacking not prevented") and it turns out to be an **architecture**
decision, not a code one.

**FACT:** GitHub Pages does not support custom HTTP response headers and ignores
a `_headers` file. A `<meta>` tag cannot substitute — the CSP spec **excludes
`frame-ancestors` and `report-uri` from meta delivery**, and Chromium says so in
the console:

> The Content Security Policy directive 'frame-ancestors' is ignored when
> delivered via a `<meta>` element. X-Frame-Options may only be set via an HTTP
> header sent along with a document.

**FACT:** Cloudflare Pages and Netlify both read a `_headers` file and send real
headers, so `X-Frame-Options`, `frame-ancestors`, `HSTS` and `Referrer-Policy`
all work there. A hosted-blog scan scores **GitHub Pages at F (10)** on security
headers, largely for this reason.

**INFERENCE — what it means for SoftFire, measured against its own standards.**
The site already documents that HSTS, `frame-ancestors` and `Permissions-Policy`
are **not covered**, and that meta CSP is all it can do. That is not a bug in the
page; it is the host. Therefore:

| | GitHub Pages | Cloudflare Pages |
|---|---|---|
| CSP | meta only | real header |
| HSTS | **impossible** | yes |
| `frame-ancestors` (clickjacking) | **impossible** | yes |
| `Referrer-Policy` | **impossible** | yes |
| Cost | free | free |
| Custom `_headers` file | no | yes |

**The decision this forces — PROPOSED:** build on **Cloudflare Pages**, not GitHub
Pages. It costs the same (GH₵0), and it is the difference between *"we cannot
prevent clickjacking"* and *"we can"*. This is a one-line change to the deploy
target and it removes a documented gap.

**And it changes what security can be promised at all** — which is why security
belongs in the **build**, not the retainer: whether the client gets HSTS is
decided when the host is chosen, before anyone is paying monthly.

---

## 3. So where does security sit?

Three postures exist in the market. Only one is honest at this scale.

| Posture | Where security sits | Honest? |
|---|---|---|
| **Industry default** | inside the care plan, unnamed | No — it prices a static site as if it were WordPress |
| **Agency economics** | a separate "security monitoring" line | No — nothing to monitor; it is an alarm on an empty room |
| **Correct for a static site** | **a launch deliverable + three habits** | Yes |

**The prescription:**

| When | What | Charged? |
|---|---|---|
| **At launch** | 2FA on registrar, email, GitHub, host · registrar lock · DNSSEC if supported · SPF/DKIM/DMARC if email is on the domain · HTTPS forced and verified · security headers via `_headers` · CSP tightened | **inside the build** — it is part of handover, 45 minutes |
| **Free 3 months** | uptime alerting wired to a channel · domain expiry watched · first quarterly record audit | **included** |
| **Care plan, month 4+** | uptime alerting · domain expiry watched · quarterly record audit · a note saying what was checked | **inside the GH₵200** — it is 15 minutes a quarter |
| **Annually** | re-run the audit, confirm recovery contacts current, confirm 2FA still on | **included** |

**INFERENCE — do not sell security separately, and do not hide it either.** Name
it as a thing that was **done** at launch, list it in the handover sheet, and let
the care plan mention that the checks continue. That is more convincing than a
"security package", because it produces evidence — a screenshot of the registrar
lock, a DMARC record that resolves — instead of a monthly invoice.

**The one honest upsell:** if the client has **email on the domain** and sends
invoices or quotes from it, then SPF/DKIM/DMARC maintenance is real work — a new
booking tool or newsletter means new records. That is **management**, priced per
change, not a security retainer.

---

## 4. The trap: security becomes real the moment the site stops being static

This is the part that matters for the vision, because the stated plan is a
**school portal**. Everything above inverts.

| | Static site | Portal / app / CMS |
|---|---|---|
| Attack surface | files | logins, a database, user data |
| Patching | none | continuous |
| Backups | a git repo | **data**, with retention and restore tests |
| Security | a launch checklist | **a service**, with monitoring and response |
| Compliance | none | possibly Ghana's Data Protection Act (Act 843) |
| Retainer | GH₵200, mostly changes | **GH₵1,000+**, because the work is real |

**INFERENCE — say this in writing to every client before they buy a portal.** On a
static site the honest answer is "there is nothing to maintain." On a portal the
honest answer is the opposite, and a GH₵200 plan covering a portal that holds
student data would be a liability, not a bargain.

**The rule:** the price of the retainer must follow the attack surface, not the
client's budget.

---

## 5. Hosting and deployment: separate, named, at cost

### 5.1 The four models the market uses

**FACT** — how agencies bill hosting:

| Model | What the client sees | Margin | Where it goes wrong |
|---|---|---|---|
| **Pass-through** | the agency's cost, itemised | none | unpaid support work |
| **Markup** | a "hosting" line | modest | *"the most exposed"* — awkward the moment the client compares |
| **Bundled in a care plan** | one monthly fee | best | hides the cost, invites the "what am I paying for" question |
| **Tiered products** | named plans | best at scale | needs volume |

The research is blunt about the second: markup *"works while the client does not
compare, and becomes awkward the moment they do."*

And about bundling: *"The client buys an outcome rather than a component. There is
no line item to compare against a public price."* — which is precisely why it
conflicts with a brand whose whole promise is that **nothing is hidden**.

### 5.2 The recommendation for SoftFire

**PROPOSED — a fifth model: pass-through at GH₵0, named.**

| Item | Who pays | How much | Where |
|---|---|---|---|
| **Hosting (static, Cloudflare Pages)** | nobody | **GH₵0** | stated on the page |
| **Domain `.com`** | the client, directly | **GH₵146–260/yr** | their own registrar account |
| **Domain `.com.gh`** | the client, directly | **GH₵750–1,690/yr** | their own registrar account |
| **Email** (if wanted) | the client, directly | from about $1/user/mo | Zoho or Google, in their name |
| **SSL** | nobody | **GH₵0** | automatic |
| **cPanel hosting** (only if they insist) | the client, directly | **GH₵105–1,100/yr** | their own account |

**Why not resell, when the research says reselling is more profitable:**

1. **It contradicts the brand.** The page already says *"every account in your
   name"*. A GH₵275/plan bought for the client and billed at GH₵500 is the
   opposite, and a client who finds the host's price list will conclude that
   everything else on the page was marked up too.
2. **Static hosting is GH₵0.** There is no margin to take on nothing. A "hosting"
   line at GH₵200/month for a free service is the clearest possible breach of
   *"the price does not move"* ethics.
3. **The support burden is real either way.** The research notes freelancers
   answer the "my email stopped working" call regardless of who bills for the
   server — and the fix is to bill for **management**, not for the server.
4. **No lock-in is the differentiator.** Every competitor's exit cost is a
   migration. SoftFire's is a zip file.

**The trade, stated honestly — INFERENCE:** this gives up roughly GH₵1,200/year per
client in hosting margin in exchange for a claim no competitor in the table can
make. At GH₵1,500 a build, that margin was never going to be the business. **The
retainer is the business** (`MAINTENANCE.md` §6), and it does not need to smuggle
hosting into its price to work.

### 5.3 Deployment: whose job is it?

**Deployment is part of the build, not a service.** But it produces something that
recurs, and that belongs in the plan:

| Task | When | Whose |
|---|---|---|
| Register the domain, in the client's name | build | SoftFire, with them |
| Point DNS, issue SSL, verify `www` + apex | build | SoftFire |
| First deploy, verify all pages | build | SoftFire |
| **Monitor that the site is up** | continuous | **care plan** — free automation |
| **Watch the domain expiry** | annual | **care plan** — the one that actually kills sites |
| Redeploy after a change | per change | care plan (management) |
| Migrate host, if ever | project | quoted |

**INFERENCE — the one real risk this creates.** The research puts it well: *"A
client who misses a renewal notice from a host they chose two years ago loses the
site, and rebuilding it falls to the freelancer."* So the care plan must own
**watching the expiry**, even though the client owns the account. That is a
genuine service worth naming, and it costs a calendar reminder.

---

## 6. The plain statement for the page

> **Your accounts stay yours.** The domain, the hosting account, the code and the
> email are in your name from day one, and I set them up with you. Hosting costs
> **nothing** because the site is static — there is no server, no database and no
> monthly bill. The domain is about GH₵146–260 a year and you pay it to the
> registrar yourself.
>
> At launch I turn on two-factor authentication and the transfer lock on your
> domain, publish the email records that stop someone invoicing a customer as you,
> and check the security headers. That is included, because it takes 45 minutes
> and it is the part that actually matters.
>
> After that, the only ongoing security work is that **I notice if the site goes
> down and I notice if your domain is about to expire.** That is in the monthly
> plan. If someone offers you a "security package" for a five-page brochure site,
> ask them what they are monitoring.

---

## 7. What I could not verify

| Unknown | Why it matters |
|---|---|
| **Whether Cloudflare Pages is reachable from Ghana on typical mobile networks** | Ghanaian ISP routing to Cloudflare is generally good, but I did not test it. GitHub Pages is the incumbent because it was already working |
| **Whether the `.com.gh` registrar supports DNSSEC** | Not checked. If not, DNSSEC is unavailable on the recommended local domain |
| **Whether any Ghanaian registrar offers registry lock** | Only standard registrar lock is confirmed across the price lists read |
| **Ghana Data Protection Act (Act 843) duties for a sole trader** | Not researched. Becomes material the moment a portal holds names or student records |
| **Real incidence of domain hijacking or email spoofing among Ghanaian SMEs** | No data found. The control is standard practice, not a measured local risk |
| **Whether `_headers` on Cloudflare Pages covers every response** | Docs note it does not apply to Pages Functions responses — irrelevant for a static site, material if one is added |

---

## Sources

- Static-site attack surface and account-first security: wpcto.net agency checklist
  (Aug 2026), securelayer7 small-business checklist (Sep 2026), viserx (Aug 2026),
  nameexperts domain security (Apr 2026), dnsvigil DNS checklist (Mar 2026),
  techhelp.ca secure-website blueprint (Aug 2026), dchost 20 hosting controls
  (Nov 2026).
- Header support: GitHub Community discussion #54257; nooshu.com on headers per
  host (Dec 2024); dev.to analysis of what a meta tag can and cannot deliver
  (Oct 2026); CSP specification on `frame-ancestors` exclusion from meta.
- Hosting billing models: fastcow.com "How agencies should bill clients for
  hosting" (Aug 2026); massivegrid.com agency hosting guide (Sep 2026);
  greengeeks.com reseller threshold (Aug 2026); serverfellows.com white-label
  ownership (Oct 2026).
- Hosting and domain prices: see `PRICING.md` §1.
