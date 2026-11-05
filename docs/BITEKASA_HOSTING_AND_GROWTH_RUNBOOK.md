# BiteKasa free hosting, search, analytics and operations runbook

**Status:** deployment is prepared, not yet activated. The chosen initial address is `https://hotmoon123.github.io/hotmoon123/`. The repository is public; GitHub Pages has not yet been enabled, so this address must be tested after the Pages workflow is merged and run. **Do not print or distribute the QR artwork until that live test succeeds.**

This is a static-site deployment, not a rented server. GitHub Pages serves the built files through GitHub's HTTPS-enabled edge. There is no application server to patch, database to secure, or backend secret in the site. It is suitable for the current brochure/enquiry website; it is not suitable for checkout, payment processing, order storage, or private customer records.

## 1. What is prepared in the repository

- Pull-request CI: locked `npm ci`, TypeScript check, production dependency audit, production build and output checks.
- GitHub Pages workflow: builds the Vite app with the repository path base and deploys the static `dist` output after a push to `main`.
- Public-site smoke check: daily checks for the home page, three service pages, privacy notice, `robots.txt`, and sitemap. GitHub Actions failures are visible in the repository's Actions tab and GitHub notifications.
- Weekly backup job: creates a Git-history bundle and source/artwork archive as GitHub Actions artifacts retained for 90 days. This is a recovery convenience, not a separate-provider/off-site backup.
- Dependabot weekly update proposals for npm packages and GitHub Actions.
- Separate crawlable pages for fried, unfried, and frozen product options, linked to one another and back to packs/contact.
- Unique titles/descriptions/canonicals, Open Graph metadata, `robots.txt`, sitemap, and a draft privacy notice.
- Optional GA4 wiring. Analytics remains disabled until a Measurement ID is configured and a visitor explicitly consents.
- QR artwork variants for the approved flyer and 4:5/9:16 social exports. Originals remain untouched.

## 2. Activate free HTTPS hosting

1. Review and merge the BiteKasa changes to `main` in `hotmoon123/hotmoon123`.
2. In GitHub, open **Settings → Pages**. Choose **GitHub Actions** as the build/deploy source if it is not already selected.
3. Open **Actions → Deploy BiteKasa to GitHub Pages** and run it on `main` if the push did not start it automatically.
4. Wait for the deploy job to succeed. Confirm GitHub Pages shows `https://hotmoon123.github.io/hotmoon123/` and HTTPS is available.
5. Open the home page and each service page on a phone and desktop; test WhatsApp, telephone and Instagram links. Confirm the contact details are correct.
6. Do not print the QR until the exact URL encoded in it returns the real site over HTTPS. The current QR points to the chosen GitHub Pages URL. If the final URL changes, regenerate the QR artwork.

GitHub Pages is static hosting. Do not add API keys or private credentials to Vite `VITE_*` variables: these are compiled into public browser code. The optional GA4 measurement ID is public by design. Enable GitHub two-factor authentication, limit repository write access, review automated dependency PRs, and keep the Pages deployment permissions scoped as in the workflow.

### Cost and hosting limits

- The repository is public and GitHub Pages can serve this static site over HTTPS at no hosting charge while the account stays within GitHub's applicable free-use limits.
- There is no server, database, container cluster, paid monitoring agent, or cloud resource to provision. No Terraform/Kubernetes layer is justified for this static brochure site.
- A custom domain, if purchased later, has a registrar renewal cost even if hosting remains on GitHub Pages.
- The scheduled backup artifacts, CI minutes, GA4 limits, and any listing platform terms are subject to current provider quotas and may change. Keep a local/off-provider copy of important backups.

## 3. Google Search Console (owner must sign in)

1. Sign in to the BiteKasa-owned Google account and open Google Search Console.
2. Add a **URL-prefix** property for exactly `https://hotmoon123.github.io/hotmoon123/` (including the trailing slash). Do not select a domain property unless BiteKasa later controls a custom domain and DNS.
3. Choose the HTML-file verification method. Download the exact verification file Google provides and add it unchanged under `bitekasa-site/public/` so it is served at the root URL. Commit/deploy it, then click **Verify** in Search Console. Never invent or edit the token.
4. After verification, submit `https://hotmoon123.github.io/hotmoon123/sitemap.xml` under **Sitemaps**.
5. Use URL Inspection to request crawling of the home page and each of the three service pages. Watch indexing and page-experience reports over time; indexing is not guaranteed.

Google Search Console was not connected in this workspace. The owner must complete account sign-in and verification. No credentials, verification tokens, or recovery codes should be shared in chat.

## 4. Bing Webmaster Tools

After the site is public, create the site property for the exact HTTPS URL in Bing Webmaster Tools. Prefer importing the verified Search Console property. Otherwise choose Bing's HTML-file or meta-tag verification, add the exact owner-provided token/file, deploy, verify, then submit the same sitemap. A smoke-check HTTP 200 is not proof that either search engine has indexed the site.

## 5. Google Analytics 4 (optional; consent-gated)

1. Create a GA4 property and web data stream for the exact production URL while signed into the owner's account.
2. Copy the stream's `G-...` Measurement ID.
3. In GitHub, open **Settings → Secrets and variables → Actions → Variables → New repository variable**. Set the name to `VITE_GA_MEASUREMENT_ID` and the value to that public Measurement ID.
4. Redeploy. With a Measurement ID present, the site shows **Allow analytics** and **Reject** choices. The GA script is injected only after Allow; a visitor can reopen **Privacy settings** to change the decision. Without the variable, no GA script or consent banner is loaded.
5. Review the privacy notice, retention and data-sharing configuration, and the owner's Ghana data-protection obligations before enabling measurement. Do not send names, phone numbers, WhatsApp text, or other personal details to analytics.
6. Test using GA4 Realtime/DebugView after consent. A property existing does not mean it is receiving data.

The Google account/property and Measurement ID do not yet exist, so analytics is not active.

## 6. Google Business Profile and listing directory plan

The owner selected “not sure” about profile eligibility. **Do not create or verify a profile using a made-up address or a location that does not receive customers.** First confirm whether BiteKasa is an eligible storefront or a service-area business and which areas it actually serves. If customers are not received at a home kitchen, do not publish the private address; use Google's current service-area rules. Confirm current prices, hours, phone/WhatsApp ownership, delivery/collection, menu/service wording, and owner-approved real photos. The product images on the site are illustrative and must not be represented as verified product photos.

**Draft profile description (owner must review before use):** “BiteKasa offers samosas and spring rolls, with fried, prepared-unfried and frozen options to ask about. Contact us to confirm current availability, pack contents and ordering arrangements.” Keep the listing category, service area, hours, and any claims about ingredients, freshness or delivery out until verified.

Potential no-cost business discovery/profile destinations to assess once the owner confirms facts and controls the accounts:

1. Google Business Profile (only if eligible and verified).
2. Bing Places for Business.
3. Apple Business Connect.
4. Facebook business Page.
5. Instagram professional profile for `@bitekasa`.
6. LinkedIn company Page, if useful for the business.
7. GhanaYello business listing.
8. Hotfrog business listing.

**None of these listings has been submitted.** Confirm each platform's current Ghana availability, eligibility, and genuinely free tier before entering the business. For consistency, use the same owner-approved name, website, phone, hours, service area and category everywhere; avoid keyword-stuffing the business name. Keep a record of listing URLs, account owner, verification state, and update date. Social profiles are useful discovery profiles but are not all traditional web directories.

Before publishing any profile or directory entry, the owner needs to confirm:

- Is BiteKasa home-based/service-area, or is there a staffed customer-facing location?
- Which exact towns/areas are served, and are orders delivered, collected, or both?
- Are both listed telephone numbers current, and which number is the official WhatsApp account?
- Current opening hours and order lead time.
- Current stock, product mix, pack prices, ingredients/allergens, and collection/delivery arrangements.
- The owner-controlled account and preferred privacy-contact method.

## 7. Website speed and GTmetrix

A public GTmetrix report cannot be produced before deployment, and this environment cannot log into GTmetrix. After the site is live, enter the production home URL in GTmetrix and save the report URL/date. Also test each service page and a real mobile connection. Record LCP, CLS, TBT/INP, total transfer size and top recommendations; retest after changes. Do not promise a score or ranking. The workflow's build/type checks and daily HTTP smoke check are not substitutes for a Lighthouse/GTmetrix performance test.

## 8. QR code and flyer handling

Files ending `-website-qr.png` are new QR variants; source artwork is unchanged. The standalone `assets/bitekasa-website-qr.png` and three artwork variants encode `https://hotmoon123.github.io/hotmoon123/`. QR files should be tested with multiple phone cameras after Pages is live. Print a proof at the intended final size and scan it from paper before bulk printing. If using a custom domain later, decide whether the old GitHub URL will remain permanently redirected before reprinting.

### Print-ready QR pack (`bitekasa-site/assets/qr/`)

The recommended print file is `bitekasa-offer-flyer-qr-footer.png`: the original flyer artwork plus a cream footer band holding the QR, so nothing on the artwork is covered. `bitekasa-qr-vector.svg` and `bitekasa-qr-print-2400.png` are standalone sources for design work. `bitekasa-qr-scan-card.png` adds a “Scan to view” caption. All encode the same URL. The earlier `bitekasa-offer-flyer-website-qr.png` is superseded because its overlay hides part of the Premium pack text; it is kept only for history.

Never ask an AI image generator to draw, restyle or “add” the QR code to a flyer. Diffusion models repaint the pattern and the printed result does not encode the URL. Generate the artwork without a code, then place the real SVG/PNG as a separate layer in a layout tool, export at 300 dpi, and scan a paper proof with at least two phones before a bulk print run. Keep the white quiet zone, keep the code at least 2 cm wide on the printed sheet, and do not stretch it.

## 9. Backups and incident response

- Every source change should be reviewed and merged through GitHub PRs; Git history is the primary source backup.
- A weekly workflow retains a Git bundle and site/source archive artifact for 90 days. Download critical release artifacts to an owner-controlled location periodically for an independent copy.
- **Failed deployment:** check Actions logs, roll back by reverting the last site commit and merging a reviewed PR; rerun Pages deployment.
- **Wrong public content/contact:** remove or correct it in source, deploy, then verify the live site and replace affected flyer/QR files if the URL changed.
- **Unexpected tracking:** remove `VITE_GA_MEASUREMENT_ID` from repository variables, redeploy, review the GA property and privacy notice, then re-test in a clean browser.
- **GitHub account compromise:** use GitHub's account recovery/security controls, revoke sessions/tokens from the account, review repository collaborators/workflows, and restore from trusted history. Never put recovery codes or tokens into issues or commits.

## 10. Current limits / actions still requiring the owner

- GitHub Pages needs the workflow merged and the Pages source enabled; deployment is not yet confirmed live.
- Google Search Console, Bing Webmaster Tools, GA4 and Google Business Profile require owner account sign-in and verification; they are not connected here.
- GBP eligibility and the actual service area are not confirmed.
- Eight profile/directory submissions are prepared as a shortlist, not claimed as completed.
- GTmetrix must be run against the live public URL after deployment.
- QR artwork is generated for the chosen URL but must not be printed until live URL and physical scan tests succeed.
