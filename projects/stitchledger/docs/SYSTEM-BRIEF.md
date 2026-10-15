# StitchLedger — the system we are building

Version 0.2 · 8 October 2026

## 1. Understanding your request

You want a coherent mobile-app business, not a collection of unrelated screens: a worthwhile problem, researched decisions, disciplined requirements, an understandable architecture, a professional interface, functioning software, test evidence and a path to revenue. You have delegated initial product and technical choices and selected **Android and iPhone with a shared backend**. You use Kali Linux locally.

The established product is **StitchLedger**, a tailoring-studio order, deposit and delivery tracker. The current release replaces the first browser-only prototype with a React Native/Expo project targeting Android, iOS and web, backed by an authenticated API and a transactional database. It is a development release, not a claim that the entire commercial lifecycle is complete.

## 2. Vision, mission and purpose

**Vision:** independent makers can run dependable businesses without administrative overload.

**Mission:** make it easy to know what has been promised, what needs attention and what remains unpaid—from a phone.

**Purpose:** connect a studio's customer promises, production work and payment records in one small, comprehensible system.

**Positioning hypothesis:** a focused order-to-collection companion for small tailoring studios, not a full accounting package, general-purpose ERP, lending platform, marketplace or generic chatbot.

**Working promise:** “Your craft. Your customers. All in order.” This is positioning, not proof of business outcomes.

## 3. Why, what, who, whom, when, which, where and how

| Question | Product answer | Consequence for implementation |
|---|---|---|
| Why? | Test whether a clearer order book reduces missed commitments and administrative effort. | Prioritize deadlines, status and balances—not decorative analytics. |
| What? | Order management plus a record of deposits, additional receipts and actual refunds. | Every amount has an explicit meaning and every payment entry is retained. |
| Who? | A studio owner; future staff access requires a separate permissions design. | Current tenant model is one owner/workspace. |
| Whom? | Small tailoring businesses initially; their customers benefit indirectly. | No customer app, customer login or marketplace is necessary. |
| When? | At booking, during production review, when money changes hands elsewhere, and at collection. | Organize around a complete workflow rather than many disconnected features. |
| Which? | A narrow, testable product over a broad “everything app.” | Four primary navigation destinations; a deliberately limited state machine. |
| Where? | Android/iPhone project and browser preview; Ghana-first/GHS as provisional defaults. | Cross-platform UI; integer pesewas; network required. |
| How? | Requirements → design → implementation → tests → customer pilot → controlled release. | No assertion of readiness without evidence at each gate. |

## 4. Four clear product areas

### Today — decide what needs attention

- Outstanding balance across active orders.
- Work in production and items ready for collection.
- Earliest-due active orders.
- Overdue review and simple production counts.

All values are calculated from the workspace database. The guidance is **rules-based**, labeled accordingly. There are no fabricated growth percentages, customer testimonials or AI predictions.

### Order book — fulfill the promise

- Create, inspect and edit a customer/garment order.
- Record price, cash opening deposit, collection date and notes.
- Search by customer/garment; filter by status or lateness.
- Follow explicit production and rework transitions.
- Review payment events and an order activity trail.
- Draft a customer update, review it, then copy/share.

### Money — understand recorded cash movements

- Recorded receipts, recorded refunds and net recorded amount.
- Payment method and owner-entered reason/reference.
- CSV export of orders; full JSON export through Studio.

These are **owner-entered records**, not bank-verified transactions. Deposits are not automatically earned revenue. Net recorded cash is not profit. No funds move through the app.

### Studio — manage the workspace

- Account identity and demo/real-test workspace labeling.
- Full record export, sign out, and confirmed account deletion.
- Clear disclosure of connected and unavailable capabilities.
- Privacy and pre-release limitations.

## 5. Deliberate design principles

1. **Content before decoration:** the garment, owner commitment, date, status and balance define the layout.
2. **A clear hierarchy:** the next action is visible; secondary settings stay out of the daily workflow.
3. **Recognition rather than recall:** names, explicit labels and status words accompany icons/colors.
4. **Consistency:** the same money formatting, spacing, buttons and status treatments across screens.
5. **Error prevention:** validate before saving; validate again on the server; show actionable errors.
6. **Financial truthfulness:** never label cash movements as profit; no invented transactions.
7. **Reversible exploration:** private fictional demos; confirmation for cancellation/deletion/AI disclosure.
8. **Purposeful restraint:** no ornamental 3D, autoplay, excessive animation, cluttered gradients or unrelated dashboards.
9. **Accessible intent:** clear labels, practical touch targets, safe-area layout, readable contrast and keyboard-capable web controls. Full conformance remains unverified.
10. **No false expertise:** methods and roles describe perspectives, not independent professionals who actually reviewed the release.

Visual direction: warm off-white working surface, dark green for primary actions and emphasis, restrained status colors, simple typography, a scissors identity, and calm spacing. Mobile uses bottom navigation; desktop uses a sidebar. These choices are justified by product tasks, not claimed as universal design laws. Name/logo ownership and trademark clearance remain unchecked.

## 6. End-to-end example

1. The owner signs in or opens a private demo.
2. A customer orders a GHS 100 garment and pays GHS 20 in cash elsewhere.
3. The owner creates the order. The API stores an order and a separate GHS 20 receipt in one transaction.
4. Remaining balance is computed as GHS 80—not stored as an independently editable number.
5. Production moves from Booked to Cutting to Sewing to Ready.
6. The customer pays GHS 80 elsewhere. The owner records the method/reference.
7. A repeated network request with the same key does not add a second receipt.
8. The owner can mark the fully paid order Collected.
9. Original payment entries remain in the ledger and the workflow change is recorded in the activity trail.

If payment was entered incorrectly, do **not** pretend money was refunded. A dedicated mistaken-entry reversal/correction workflow is not yet implemented and is a release blocker before routine real-money recordkeeping.

## 7. Commercial logic and evidence limits

Ghana's 2024 business census reports approximately 1.9 million establishments and a predominance of microbusinesses; this is a broad context indicator, not StitchLedger's obtainable market. [5](https://statsghana.gov.gh/gssmain/fileUpload/pressrelease/factsheet.pdf)

Existing products such as Oze already offer bookkeeping, invoicing, inventory and payment reminders. The proposed differentiation must therefore be validated around tailoring workflow, not an unsupported claim that competition is absent. [2](https://getoze.com/business-app/)

Provisional monetization: GHS 30/month per studio after validation. Example arithmetic: 50 paying studios would generate GHS 1,500/month gross, before hosting, support, customer acquisition, payment fees, taxes and founder labor. This is neither a forecast nor a profit claim. Subscription collection is not implemented.

Before committing to commercial infrastructure, run interviews, observed tasks and a clearly explained paid pilot. No such interviews, sales or paid commitments have occurred in this conversation.

## 8. Honest delivery boundary

Delivered: mobile source for both platforms, working backend/database, browser build, tests, documentation, optional AI integration code and local operations tooling.

Not delivered: signed native installation files, app-store approval, verified demand, production hosting, live payment/subscription integration, provider credentials, independent audit or guaranteed income. Completing these requires further engineering, owner decisions, third-party approval and external evidence—not a stronger prompt.
