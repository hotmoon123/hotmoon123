# 📁 Complete `.md` File Suite
## Rent & Lease Management System
### Based on Every Conversation, Decision, Architecture, and Principle Discussed

---

# FILE 1 — `AI_rules.md`

```md
# 🤖 AI_rules.md
# Rent & Lease Management System — AI Behaviour Rules
# Every AI tool, assistant, or code generator working on this project must follow these rules without exception.

---

## 🎯 PROJECT IDENTITY

- Project Name   : Rent & Lease Management System
- Type           : Full-Stack Web Application (SaaS)
- Tech Stack     : HTML + CSS + JavaScript (Frontend) | Python (Backend + Middleware + API) | SQL (Database)
- Users          : Landlords (Desktop) | Tenants (Mobile-first)
- Total Pages    : 38 (14 Landlord + 11 Tenant + 13 External/System)
- Architecture   : 9-Layer System (Structure → Styling → Behavior → Middleware → API → Business Rules → Business Logic → Data Retrieval → Data Storage)

---

## 🧠 THINKING RULES

1. Read every instruction fully before generating anything
2. Think in systems — every decision affects every layer
3. Apply Bloom's Taxonomy levels 1–6 before producing output
4. Reason from first principles — do not guess
5. If uncertain, state the uncertainty clearly and stop
6. Never produce output that violates a principle stated in this file
7. Think in the box — stay within the scope of what is asked

---

## 🏗️ ARCHITECTURE RULES

1. Every feature must be designed across all 9 layers explicitly
2. Structure (HTML) only declares existence — never style or behavior inline
3. Styling (CSS) only handles visual appearance — never business decisions
4. Behavior (JavaScript) is for UX only — never security enforcement
5. Middleware runs first — always in this order:
   Security Headers → CORS → Request Logging → Rate Limiting → Authentication → Authorization (IDOR)
6. API routes never touch the database directly — always via Business Logic
7. Business Rules are checked before Business Logic executes
8. Data Retrieval and Data Storage are always separate functions
9. Every database write uses parameterized queries — no string concatenation ever
10. Every database transaction that involves multiple writes is atomic (ACID)

---

## 📐 ENGINEERING PRINCIPLES (NON-NEGOTIABLE)

1. Single Responsibility Principle — every function does exactly one thing
2. Separation of Concerns — each layer owns only its concern
3. DRY (Don't Repeat Yourself) — every piece of logic lives in exactly one place
4. Defence in Depth — security is enforced at every layer independently
5. Principle of Least Privilege — every component accesses only what it needs
6. Fail Fast, Fail Safely — detect errors early, never expose internal details to users
7. Explicit over Implicit — never rely on hidden defaults or magic behavior
8. Optimistic UI with Safe Rollback — update UI instantly, roll back on server rejection
9. Stateless API — every request carries all information needed to process it
10. Idempotency on critical endpoints — submitting the same request twice produces the same result as once

---

## 🔐 SECURITY RULES

1. Never trust the frontend — every frontend validation must be re-enforced server-side
2. Never store passwords in plain text — bcrypt hashing only
3. Never expose stack traces, error details, or file paths to the browser
4. Never concatenate user input into SQL queries
5. Never store secrets (API keys, JWT secrets, DB passwords) in source code
6. All secrets live in environment variables only
7. JWT tokens are short-lived and verified on every request
8. IDOR protection is applied at both Middleware and query level (WHERE owner_id = authenticated_user_id)
9. Rate limiting is applied at both Middleware level (broad) and API endpoint level (specific)
10. HTTPS is enforced on all production traffic
11. CSRF tokens on all state-changing forms
12. CORS is configured to allow only known, trusted origins
13. Input is validated, sanitized, and type-checked at the API boundary before reaching business logic
14. Audit logs are append-only and immutable
15. Soft deletes only — critical data is never hard deleted

---

## 🎨 DESIGN RULES

1. Design System tokens from design.md must be used — no arbitrary values
2. 4px base spacing unit — all spacing is a multiple of 4
3. Desktop-optimized F-Pattern layout for Landlord pages
4. Mobile-first design for all Tenant pages — minimum 48px touch targets
5. Deep Blue (#0F172A) is the primary action color
6. Muted Red (#EF4444) is exclusively for errors, warnings, and overdue states
7. Muted Emerald (#10B981) is exclusively for success and active states
8. All animations use cubic-bezier easing — no linear transitions on interactive elements
9. Loading states, error states, and empty states must be designed for every component
10. Accessibility (A11Y) is required — keyboard navigation, screen reader labels, color contrast

---

## 📏 CODE QUALITY RULES

1. Every function has one job — if it does two things, split it
2. Every function can be described in one sentence without the word "and"
3. No function is longer than it needs to be
4. Error handling is explicit — no silent failures
5. All user-facing error messages are generic — all internal errors go to the log
6. Naming is explicit and descriptive — no abbreviations, no magic numbers
7. File structure follows the defined project structure in file_structure.md
8. Naming follows the conventions in naming_patterns.md

---

## 🚫 FORBIDDEN ACTIONS

- Never introduce colors outside the design system palette
- Never write business logic inside HTML templates
- Never query the database inside an API route handler directly
- Never skip the middleware order
- Never submit a form without CSRF validation
- Never return HTTP 200 for an error response
- Never store the full payment card number
- Never log sensitive user data (passwords, tokens, card numbers) to log files
- Never allow a user to access another user's resource without explicit ownership verification
- Never deploy with debug mode enabled

---

## ✅ STOPPING RULE

Stop generating when:
- The requested feature is complete across all relevant layers
- Every security rule has been applied
- Every principle has been respected
- The output is clear, correct, and self-explanatory

Do not add unrequested features.
Do not over-engineer beyond the defined scope.
Do not continue if a rule conflict is detected — flag it first.
```

---

# FILE 2 — `plan.md`

```md
# 📅 plan.md
# Rent & Lease Management System — Project Plan
# Semester Build Plan | Week-by-Week | Milestones | Deliverables

---

## 🎯 PROJECT GOAL

Build a full-stack, production-ready Rent & Lease Management System that serves two user types
(Landlords and Tenants) across 38 pages, with real-time chat, automated billing, Kanban
maintenance management, analytics, and a complete security perimeter.

---

## 👥 TEAM

- Roles              : Full-Stack Engineers
- Frontend Stack     : HTML, CSS, JavaScript
- Backend Stack      : Python (Flask or FastAPI)
- Database           : SQL (PostgreSQL or SQLite for development)
- Architecture       : 9-Layer System

---

## 📆 SEMESTER TIMELINE — 15 WEEKS

---

### 🏗️ PHASE 0 — FOUNDATION (Week 1)
**Goal: Establish all project scaffolding before writing any feature code**

Deliverables:
- [ ] All .md files created and committed (this file included)
- [ ] Project folder structure created per file_structure.md
- [ ] Design system CSS variables and base components built
- [ ] Database schema written and reviewed
- [ ] Environment variables configured
- [ ] Git repository initialized with .gitignore
- [ ] Base HTML templates (layout_landlord, layout_tenant, layout_auth) created
- [ ] Development environment verified working end-to-end

Exit Criteria: A blank-but-structured project where every layer has its home

---

### 🔐 PHASE 1 — AUTHENTICATION & SECURITY PERIMETER (Weeks 2–3)
**Goal: Build the complete identity and access layer before any feature**

Week 2 Deliverables:
- [ ] Database: users table, roles, tokens
- [ ] Registration page (External Page 2) — Role toggle, form, validation
- [ ] Login page (External Page 3) — JWT issue, role-based routing
- [ ] Email verification flow (External Page 5)
- [ ] Authentication Middleware — JWT verification
- [ ] Rate Limiting Middleware — login endpoint (10 attempts / 15 min)
- [ ] CORS Middleware configured
- [ ] Security Headers Middleware

Week 3 Deliverables:
- [ ] Forgot Password page (External Page 6)
- [ ] Reset Password page (External Page 7) — 15-minute token expiry
- [ ] Authorization Middleware — IDOR prevention base layer
- [ ] Request Logging Middleware — audit trail initiated
- [ ] Lease Invitation Gateway (External Page 4) — encrypted URL flow
- [ ] 403, 429, 404, 503 error pages (External Pages 10–13)

Exit Criteria: Complete user registration → login → dashboard routing working securely

---

### 🏠 PHASE 2 — LANDLORD CORE (Weeks 4–6)
**Goal: Build the primary Landlord management workflow**

Week 4 Deliverables:
- [ ] Landlord Dashboard (Landlord Page 1) — metrics, transactions, expiring leases
- [ ] Property Portfolio (Landlord Page 2) — grid, add/edit/delete with active lease block
- [ ] Database: properties table, status constraints

Week 5 Deliverables:
- [ ] Leases & Tenant Onboarding (Landlord Page 3) — table, create modal, overlap validation
- [ ] Tenant Directory CRM (Landlord Page 7) — slide-out drawer
- [ ] Database: leases table, invitations table, enrollments

Week 6 Deliverables:
- [ ] Financials & Billing (Landlord Page 4) — invoice ledger, late fee rows, export
- [ ] Expense & ROI Ledger (Landlord Page 12) — expense log, net income calculator
- [ ] Database: invoices table, transactions table, expenses table

Exit Criteria: A Landlord can register, add properties, create leases, invite tenants, and view financials

---

### 📱 PHASE 3 — TENANT CORE (Weeks 7–8)
**Goal: Build the complete Tenant living experience**

Week 7 Deliverables:
- [ ] Tenant Dashboard (Tenant Page 1) — hero card, balance states, quick actions
- [ ] Rent Payment & Invoices (Tenant Page 2) — locked amount, payment submission
- [ ] Payment Success page (External Page 8)
- [ ] Payment Cancelled page (External Page 9)
- [ ] My Lease & Property Details (Tenant Page 3) — progress bar, document view

Week 8 Deliverables:
- [ ] Payment Methods & Auto-Pay (Tenant Page 7) — card management, toggle
- [ ] Profile & Settings (Tenant Page 10) — locked email, emergency contact
- [ ] Compliance & Insurance (Tenant Page 9) — upload blocks, expiry tracking
- [ ] Database: payment_methods table, automation_settings table, compliance_documents table

Exit Criteria: A Tenant can log in, see their balance, pay rent, and manage their account

---

### 🔧 PHASE 4 — MAINTENANCE & OPERATIONS (Week 9)
**Goal: Build the maintenance helpdesk workflow for both users**

Deliverables:
- [ ] Maintenance Helpdesk Kanban (Landlord Page 6) — drag-and-drop, priority tags
- [ ] Maintenance Helpdesk Tenant (Tenant Page 4) — ticket submission, spam limit, status tracker
- [ ] Move-In/Move-Out Inspection (Tenant Page 6) — accordion checklist, progress-gated submit
- [ ] Multi-Unit & Building Management (Landlord Page 13) — tree view, bulk operations
- [ ] Database: maintenance_tickets table, ticket_comments table, inspections table, buildings table

Exit Criteria: Complete ticket lifecycle from Tenant submission to Landlord resolution

---

### 💬 PHASE 5 — REAL-TIME FEATURES (Week 10)
**Goal: Build all WebSocket-driven real-time communication**

Deliverables:
- [ ] Real-Time Chat Landlord (Landlord Page 5) — two-pane, contact list, read receipts
- [ ] Real-Time Chat Tenant (Tenant Page 5) — single thread, typing indicator
- [ ] Notice Board Tenant (Tenant Page 8) — read-only broadcast feed
- [ ] WebSocket connection management, authentication, reconnection logic
- [ ] Database: messages table, conversations table, notices table

Exit Criteria: Landlord and Tenant can exchange real-time messages with read receipts

---

### 📊 PHASE 6 — INTELLIGENCE & AUTOMATION (Weeks 11–12)
**Goal: Build analytics, reporting, and all automated background processes**

Week 11 Deliverables:
- [ ] Advanced Analytics (Landlord Page 9) — revenue chart, donut charts, Chart.js integration
- [ ] System Notifications (Landlord Page 10) — chronological feed, icon states
- [ ] Notification & History Center Tenant (Tenant Page 11) — audit log, infinite scroll
- [ ] Database: notifications table, audit_log table

Week 12 Deliverables:
- [ ] Automated Reminders Control Panel (Landlord Page 14) — cron toggle switches
- [ ] Python Scheduler — nightly late fee application
- [ ] Python Scheduler — lease expiry warning (60-day scan)
- [ ] Python Scheduler — rent reminder emails (3-day)
- [ ] Auto-Pay cron job — 1st of month deduction
- [ ] Database: cron_jobs table, automation_settings table

Exit Criteria: System runs automated processes without human intervention

---

### 🗂️ PHASE 7 — DOCUMENT MANAGEMENT (Week 12, continued)
**Goal: Build the secure document vault**

Deliverables:
- [ ] Document Center (Landlord Page 8) — drag-and-drop upload, grid view, IDOR download
- [ ] Settings & Profile Management (Landlord Page 11) — vertical tabs, bank details, toggles
- [ ] Database: documents table, folders table

Exit Criteria: Files can be uploaded, organized, and downloaded with IDOR protection

---

### 🌍 PHASE 8 — PUBLIC SHELL (Week 13)
**Goal: Build the marketing and public-facing pages**

Deliverables:
- [ ] Public Landing Page (External Page 1) — hero, features, dual CTA
- [ ] All error pages finalized and styled (403, 429, 404, 503)
- [ ] Sticky navbar scroll behavior
- [ ] Scroll reveal animations on feature cards

Exit Criteria: A new visitor can land on the platform, understand it, and register

---

### 🧪 PHASE 9 — TESTING & HARDENING (Week 14)
**Goal: Verify correctness, security, and performance across the entire system**

Deliverables:
- [ ] All 38 pages tested for functional correctness
- [ ] IDOR attack simulation — verify all resource ownership checks
- [ ] Rate limiting tested — verify 429 responses fire correctly
- [ ] SQL injection testing — verify all queries are parameterized
- [ ] XSS testing — verify all user output is escaped
- [ ] CSRF testing — verify all forms validate tokens
- [ ] Mobile responsiveness verified on 375px, 414px viewports
- [ ] Keyboard navigation tested across all forms
- [ ] All cron jobs tested with simulated dates
- [ ] Performance audit — no page load over 3 seconds

---

### 🚀 PHASE 10 — FINAL POLISH & PRESENTATION (Week 15)
**Goal: Production-ready delivery**

Deliverables:
- [ ] All animations and transitions finalized
- [ ] All empty states, loading states, and error states implemented
- [ ] Documentation reviewed and completed
- [ ] Demo walkthrough script prepared
- [ ] Final code review against AI_rules.md
- [ ] System deployed to staging environment
- [ ] Presentation prepared

---

## 📊 MILESTONE SUMMARY

| Milestone | Week | Completion Gate |
|---|---|---|
| Foundation Complete | 1 | All .md files, DB schema, folder structure |
| Authentication Live | 3 | Register → Login → Dashboard routing |
| Landlord MVP | 6 | Property, Lease, Billing complete |
| Tenant MVP | 8 | Dashboard, Payment, Profile complete |
| Maintenance Live | 9 | Kanban + ticket lifecycle complete |
| Real-Time Features | 10 | Chat + WebSocket working |
| Automation Live | 12 | Cron jobs running + analytics complete |
| Full System | 13 | All 38 pages functional |
| System Hardened | 14 | All security tests passed |
| Production Ready | 15 | Deployed, documented, presented |
```

---

# FILE 3 — `prd.md`

```md
# 📋 prd.md
# Product Requirements Document
# Rent & Lease Management System

---

## 1. PRODUCT OVERVIEW

The Rent & Lease Management System is a dual-portal SaaS web application that digitizes and
automates the complete property rental lifecycle. It serves two distinct user types with
purpose-built experiences: Landlords managing their property portfolios from desktop, and
Tenants managing their living arrangements from mobile devices.

The platform eliminates paper contracts, manual rent collection, WhatsApp-based maintenance
requests, and spreadsheet-based financial tracking — replacing them with a unified, automated,
real-time digital system.

---

## 2. THE PROBLEM BEING SOLVED

Landlords:
- Track rent payments across multiple properties manually
- Have no central record of maintenance requests
- Cannot see portfolio-wide financial performance at a glance
- Communicate with tenants through informal channels with no record
- Have no automated mechanism for applying late fees or expiry warnings

Tenants:
- Have no clear view of their current balance and payment history
- Cannot formally document maintenance issues with evidence
- Have no central location for their lease documents
- Cannot prove property condition at move-in for security deposit disputes
- Have no automated payment option to avoid late fees

---

## 3. PRODUCT VISION

A system where a Landlord can manage 50 units with the same effort it currently takes to
manage 5, and where a Tenant always knows exactly what they owe, when they owe it, and
has a formal channel for every interaction with their Landlord.

---

## 4. USERS

### 4.1 Landlord
- Uses system on desktop (optimized F-Pattern layout)
- Primary concern: portfolio health, revenue collection, maintenance resolution
- Technical comfort: moderate — expects professional CRM-like experience
- Key motivation: reduce manual work, increase visibility, protect investments

### 4.2 Tenant
- Uses system on mobile (optimized mobile-first layout)
- Primary concern: knowing what I owe, paying easily, getting repairs done
- Technical comfort: low-to-moderate — expects consumer-app simplicity
- Key motivation: avoid late fees, document issues, access lease information

---

## 5. COMPLETE FEATURE LIST

### 5.1 Authentication & Identity (All Users)
- FR-001 : Role-based registration (Landlord or Tenant) with toggle selection
- FR-002 : Email verification before account activation
- FR-003 : JWT-based session management with token expiry
- FR-004 : Forgot password with time-limited reset link (15-minute expiry)
- FR-005 : Lease invitation gateway — Tenant registers via encrypted URL from Landlord
- FR-006 : Account is automatically bound to the correct lease upon invitation acceptance

### 5.2 Property Management (Landlord)
- FR-010 : Add, edit, and delete properties with address, unit number, and base rent
- FR-011 : Delete blocked by system if active lease exists (with tooltip explanation)
- FR-012 : Occupancy status badge per property (Leased / Vacant)
- FR-013 : Multi-unit building grouping with accordion tree view
- FR-014 : Bulk financial view per parent building

### 5.3 Lease Management (Landlord)
- FR-020 : Create lease with unit, start date, end date, and rent amount
- FR-021 : Real-time overlap validation — no two active leases on same unit for same dates
- FR-022 : Invite tenant via email upon lease creation
- FR-023 : View all active and expired leases in sortable table
- FR-024 : Renew expiring leases via dashboard widget
- FR-025 : Lease expiry warning appears at 60 days (automated cron)

### 5.4 Financial Management (Landlord)
- FR-030 : Invoice ledger filtered by property, month, and status
- FR-031 : 5% late fee applied automatically to overdue invoices (automated cron)
- FR-032 : Overdue rows highlighted with Muted Red left border
- FR-033 : Export financial reports as CSV and PDF
- FR-034 : Log property expenses (repairs, taxes, maintenance costs)
- FR-035 : Net ROI calculator — revenue minus expenses per property
- FR-036 : Record offline cash payments manually

### 5.5 Rent Payment (Tenant)
- FR-040 : Hero card shows current balance with clear Safe / Due / Overdue state
- FR-041 : Payment amount is locked (readonly) — system-calculated, not user-editable
- FR-042 : Payment submission triggers gateway integration (Stripe / Paystack)
- FR-043 : Submit button disables after first tap (prevents double-charging)
- FR-044 : Payment success and payment cancelled pages with appropriate states
- FR-045 : Past invoices viewable with PDF receipt download
- FR-046 : Auto-Pay toggle — deducts exact rent on 1st of each month

### 5.6 Maintenance Helpdesk
- FR-050 : Tenant submits ticket with category, urgency, description, and photo evidence
- FR-051 : Tenant blocked from submitting if 3 active tickets already open (spam rule)
- FR-052 : Kanban board for Landlord — three columns: Pending, In Progress, Resolved
- FR-053 : Drag-and-drop ticket status update on Kanban
- FR-054 : Priority tags — Emergency (Muted Red), Low (Soft Gray)
- FR-055 : Tenant can add follow-up comments to open tickets
- FR-056 : Resolution notification sent to Tenant when Landlord closes ticket

### 5.7 Real-Time Chat
- FR-060 : WebSocket-based instant messaging between Landlord and Tenant
- FR-061 : Landlord sees all tenant contacts in left pane — selects to open thread
- FR-062 : Tenant opens directly into their single Landlord thread
- FR-063 : Photo and file attachment support
- FR-064 : Drag-and-drop file upload (Landlord desktop)
- FR-065 : Typing indicators and read receipts (blue double ticks)
- FR-066 : Online/offline presence indicators

### 5.8 Move-In/Move-Out Inspection
- FR-070 : Room-by-room accordion checklist
- FR-071 : Mandatory photo upload per room
- FR-072 : Progress-gated submission — 100% completion required
- FR-073 : Form becomes permanently readonly after submission (legal lock)

### 5.9 Document Management
- FR-080 : Drag-and-drop file upload
- FR-081 : Google Drive-style grid view organized by property folder
- FR-082 : IDOR-protected download — JWT verification before file streaming
- FR-083 : Delete with typed confirmation ("Type DELETE to confirm")

### 5.10 Analytics
- FR-090 : 12-month revenue line chart (Chart.js)
- FR-091 : Maintenance category breakdown donut chart
- FR-092 : Payment timeliness ratio donut chart
- FR-093 : At-risk tenant identification
- FR-094 : Export analytics as CSV

### 5.11 Automation Control Panel (Landlord)
- FR-100 : Toggle: 3-Day Rent Reminder Emails
- FR-101 : Toggle: Auto-Apply 5% Late Fee
- FR-102 : Toggle: Lease Expiry Warning (60 days)
- FR-103 : Real-time active/inactive status display

### 5.12 Compliance (Tenant)
- FR-110 : Upload Government ID, Proof of Income, Renter's Insurance
- FR-111 : Document verification status badges
- FR-112 : Expiry date tracking for insurance
- FR-113 : Automated warning when insurance expires within 30 days
- FR-114 : Red banner on dashboard if document is expired

### 5.13 Notifications
- FR-120 : Real-time notification push via WebSocket
- FR-121 : Chronological notification feed with unread/read states
- FR-122 : Icon-based event type identification
- FR-123 : Mark all as read function
- FR-124 : Infinite scroll pagination on history

### 5.14 Notice Board (Tenant)
- FR-130 : Landlord publishes broadcast announcements to all tenants in a building
- FR-131 : Standard notices vs urgent alerts (visual distinction)
- FR-132 : Entirely read-only for tenants

---

## 6. NON-FUNCTIONAL REQUIREMENTS

### 6.1 Performance
- NFR-001 : Dashboard loads in under 2 seconds on standard connection
- NFR-002 : Chat message delivery under 100ms (WebSocket)
- NFR-003 : Payment processing completes within 5 seconds
- NFR-004 : No page load exceeds 3 seconds on mobile
- NFR-005 : Analytics page load under 3 seconds (with caching on aggregation queries)

### 6.2 Security
- NFR-010 : All traffic over HTTPS in production
- NFR-011 : JWT tokens expire after 24 hours
- NFR-012 : Password reset links expire after 15 minutes
- NFR-013 : Invitation links expire after 24 hours
- NFR-014 : All SQL queries parameterized
- NFR-015 : IDOR protection on all resource endpoints
- NFR-016 : Rate limiting on all state-changing endpoints
- NFR-017 : Audit log for all financial and security events

### 6.3 Reliability
- NFR-020 : Cron jobs retry on failure (max 3 attempts)
- NFR-021 : Payment webhook processing is idempotent
- NFR-022 : Auto-save chat messages locally if WebSocket disconnects
- NFR-023 : System continues functioning if email service is unavailable

### 6.4 Usability
- NFR-030 : Mobile-first design for all Tenant pages
- NFR-031 : Minimum 48px touch targets on all mobile interactive elements
- NFR-032 : All forms have clear error states with specific messages
- NFR-033 : All destructive actions require confirmation
- NFR-034 : Keyboard navigation supported across all forms

### 6.5 Accessibility
- NFR-040 : All form inputs have associated labels
- NFR-041 : Color is never the only indicator of state
- NFR-042 : WCAG AA color contrast minimum

---

## 7. IN-SCOPE

- All 38 pages listed in the page specifications
- All 14 Landlord portal pages
- All 11 Tenant portal pages
- All 13 External and System pages
- Real-time chat via WebSocket
- Automated cron jobs (late fees, reminders, expiry warnings)
- Payment gateway integration (Stripe or Paystack)
- Document management with IDOR protection
- Analytics and reporting with Chart.js
- Multi-unit building management

---

## 8. OUT-OF-SCOPE

- Admin panel of any kind
- Multi-language (internationalization)
- Native mobile app (iOS or Android)
- Accounting software integration (QuickBooks, Xero)
- Property listing or marketplace features (this is management only)
- Tenant-to-tenant communication
- Third-party identity providers (Google SSO, Facebook Login)
- Video or audio calling
- AI-assisted features

---

## 9. SUCCESS CRITERIA

- A Landlord with zero technical training can add a property and invite a Tenant in under 5 minutes
- A Tenant sees their exact balance due within 2 seconds of opening the dashboard
- A rent payment completes end-to-end in under 10 seconds
- A maintenance ticket submitted by a Tenant appears on the Landlord Kanban in under 3 seconds
- The system correctly applies and prevents duplicate late fees across 100 concurrent invoices
- An IDOR attack attempt returns 403 and is logged to the audit trail
- A brute-force login attempt triggers the 429 rate limit after 10 attempts
```

---

# FILE 4 — `architecture.md`

```md
# 🏗️ architecture.md
# Rent & Lease Management System — System Architecture
# The 9-Layer Architecture | Complete Layer Definitions | Request Lifecycle

---

## 1. ARCHITECTURE PHILOSOPHY

The system is built on a strict 9-layer separation where each layer owns exactly
one concern, communicates with adjacent layers only, and never bypasses layers
to communicate directly with non-adjacent ones.

Frontend layers (1–3) live in the browser and are untrusted.
Backend layers (4–7) live on the server and are trusted.
Data layers (8–9) live in the database and are trusted.

---

## 2. THE 9 LAYERS

### LAYER 1 — STRUCTURE (HTML)
- Responsibility  : Declare what exists on each page and its semantic meaning
- Owns            : DOM elements, semantic tags, content order, accessibility attributes
- Never Does      : Style itself, execute behavior, make data decisions
- Trust Level     : Untrusted (user can modify in DevTools)

### LAYER 2 — STYLING (CSS)
- Responsibility  : Define visual appearance, spacing, animation, responsive breakpoints
- Owns            : Design tokens, layout systems, component styles, transitions, keyframes
- Never Does      : Make data decisions, communicate with server, control business logic
- Trust Level     : Untrusted (user can modify in DevTools)

### LAYER 3 — BEHAVIOR (JavaScript)
- Responsibility  : Handle user interactions, manage UI state, communicate with API
- Owns            : Event listeners, fetch calls, DOM manipulation, WebSocket client, form UX
- Never Does      : Store permanent data, enforce security, be the sole validation layer
- Trust Level     : NEVER trusted — all JS validation is for UX only, never security

### LAYER 4 — MIDDLEWARE (Python)
- Responsibility  : System-wide gatekeeping before any request reaches application logic
- Owns            : Authentication, Authorization/IDOR, Rate Limiting, CORS, Security Headers, Logging
- Execution Order : Security Headers → CORS → Request Logging → Rate Limiting → Authentication → Authorization
- Never Does      : Business logic, data operations, request routing
- Trust Level     : Fully trusted

### LAYER 5 — API (Python)
- Responsibility  : Define the official request/response contract, route requests to handlers
- Owns            : Endpoint definitions, HTTP method enforcement, input validation/sanitization, endpoint-specific rate limits, response formatting
- Never Does      : Direct database access, complex business orchestration
- Trust Level     : Fully trusted

### LAYER 6 — BUSINESS RULES (Python)
- Responsibility  : Enforce all fixed, non-negotiable system constraints
- Owns            : Constraint validation, pre-condition checks, system law enforcement
- Never Does      : Dynamic orchestration, data operations
- Trust Level     : Fully trusted
- Runs Before     : Business Logic always

### LAYER 7 — BUSINESS LOGIC (Python)
- Responsibility  : Orchestrate dynamic processes, decisions, and external service coordination
- Owns            : Multi-step workflows, external API calls (payment gateway, email), calculations, cron job logic
- Never Does      : Direct database access (calls Data Retrieval and Data Storage functions)
- Trust Level     : Fully trusted
- Runs After      : Business Rules always

### LAYER 8 — DATA RETRIEVAL (SQL)
- Responsibility  : Fetch exactly the right records with minimum queries and maximum efficiency
- Owns            : SELECT queries, JOINs, aggregations, pagination, indexes, query optimization
- Never Does      : Change data, enforce business rules
- Trust Level     : Fully trusted

### LAYER 9 — DATA STORAGE (SQL)
- Responsibility  : Permanently and safely record new and changed data
- Owns            : INSERT, UPDATE, DELETE (soft), transactions, constraints, parameterized writes
- Never Does      : Retrieve data for display, make business decisions
- Trust Level     : Fully trusted

---

## 3. COMMUNICATION RULES BETWEEN LAYERS

- Layer 3 (JS)          → communicates with → Layer 5 (API) via HTTP/WebSocket
- Layer 4 (Middleware)  → intercepts before → Layer 5 (API)
- Layer 5 (API)         → calls → Layer 6 (Business Rules)
- Layer 5 (API)         → calls → Layer 7 (Business Logic) after rules pass
- Layer 7 (Logic)       → calls → Layer 8 (Data Retrieval) when reading
- Layer 7 (Logic)       → calls → Layer 9 (Data Storage) when writing
- NO layer skips another layer
- NO layer calls a non-adjacent layer directly

---

## 4. REAL-TIME ARCHITECTURE

Chat and Notifications use WebSocket connections (not REST).
WebSocket connection bootstrapped and authenticated by Layer 5 (API).
Once authenticated, the persistent connection is managed by the WebSocket handler.
Messages are stored via Layer 9 (Data Storage) and retrieved via Layer 8 (Data Retrieval).
The Layer 7 (Business Logic) pushes events to connected WebSocket clients.

---

## 5. BACKGROUND PROCESSING ARCHITECTURE

Python Scheduler (APScheduler or Celery) runs independently of the request cycle.
Scheduler reads automation settings from the database before each job execution.
Scheduler jobs call Layer 7 (Business Logic) functions — same path as request-triggered logic.
All scheduler activity is logged to the audit_log table.

Jobs:
- nightly_late_fee_job       : Applies 5% late fee to overdue invoices
- lease_expiry_scanner       : Creates 60-day warnings for expiring leases
- rent_reminder_sender       : Sends 3-day-before-due reminder emails
- auto_pay_processor         : Processes auto-pay on 1st of month

---

## 6. REQUEST LIFECYCLE (SUMMARY)

User Action → JS (Layer 3) sends HTTP request →
Middleware Stack (Layer 4) gates the request →
API Router (Layer 5) routes and validates →
Business Rules (Layer 6) checks constraints →
Business Logic (Layer 7) orchestrates the operation →
Data Retrieval (Layer 8) or Data Storage (Layer 9) executes →
Response travels back up →
JS (Layer 3) updates the UI →
CSS (Layer 2) renders the visual state →
HTML (Layer 1) displays the result

---

## 7. DATABASE ARCHITECTURE OVERVIEW

Engine         : PostgreSQL (production) / SQLite (development)
Encoding       : UTF-8
Timestamps     : All stored in UTC
Deletes        : Soft deletes only (deleted_at column) for critical tables
Transactions   : All multi-table writes wrapped in atomic transactions
Queries        : All parameterized — no string concatenation
Indexes        : Applied to all frequently queried foreign keys and filter columns

Core Tables:
users | properties | buildings | leases | invitations |
invoices | transactions | expenses | payment_methods |
maintenance_tickets | ticket_comments | inspections |
messages | conversations | notices |
documents | folders |
notifications | audit_log |
automation_settings | cron_jobs |
compliance_documents
```

---

# FILE 5 — `design.md`

```md
# 🎨 design.md
# Rent & Lease Management System — Complete Design System
# Colors | Typography | Spacing | Components | Animations | UX Principles

---

## 1. DESIGN PHILOSOPHY

Two distinct visual identities serve two distinct user contexts:

Landlord Portal — Desktop CRM aesthetic. Professional, data-dense, trusted.
                  Inspired by Notion and Linear. Authority and clarity.

Tenant Portal   — Mobile consumer aesthetic. Warm, clear, frictionless.
                  Inspired by Monzo and Revolut. Speed and reassurance.

Both share the same design tokens and component patterns.
The difference is layout density, interaction model, and information hierarchy.

---

## 2. COLOR PALETTE

Primary (Deep Blue)       : #0F172A  — Main actions, sidebar, primary buttons, active states
Secondary (Dark Slate)    : #1E293B  — Secondary text, sub-headings
Background (Light Gray)   : #F8FAFC  — Main page canvas
Surface (Pure White)      : #FFFFFF  — Cards, modals, drawers, elevated elements
Text Primary (Dark Slate) : #1E293B  — Headings, body copy
Text Secondary            : #64748B  — Captions, helper text, placeholders, metadata
Border (Soft Gray)        : #E2E8F0  — Dividers, input outlines, subtle separators
Muted Emerald             : #10B981  — Success states, Leased badges, payment confirmed, On toggles
Muted Red                 : #EF4444  — Error states, overdue, blocked, urgent, Declined
Amber                     : #F59E0B  — Warning states, Pending tickets, caution indicators
Blue Glow (focus ring)    : rgba(15, 23, 42, 0.15) — Input focus shadow

Usage Law:
- Deep Blue   : Only for primary actions and active UI elements
- Muted Red   : Only for errors, warnings, overdue states, and urgent notices
- Muted Emerald: Only for success, completion, active paid states
- Never introduce a color not on this list

---

## 3. TYPOGRAPHY

Font Family  : System UI stack — system-ui, -apple-system, BlinkMacSystemFont, sans-serif
              (No external font dependencies — maximum performance)

Headings     : Bold weight, tight tracking (letter-spacing: -0.02em)
Body         : Regular weight, normal tracking
Labels       : Semi-bold (500), small caps optional for section labels
Captions     : Regular, #64748B color, 12–13px

Size Scale (px) : 12 | 14 | 16 | 20 | 24 | 32 | 40 | 48
Line Height     : 1.5 for body, 1.25 for headings
Base font size  : 16px (1rem)

---

## 4. SPACING SYSTEM

Base unit    : 4px
All spacing is a multiple of 4px.

Scale: 4 | 8 | 12 | 16 | 20 | 24 | 32 | 40 | 48 | 64 | 80 | 96px

Page padding         : 24px (desktop) | 16px (mobile)
Card padding         : 20–24px
Section gap          : 24–32px
Component gap        : 12–16px
Inline spacing       : 8px

No arbitrary spacing values are permitted.

---

## 5. BORDER RADIUS

Input fields, chips, small badges : 6px
Buttons                           : 6–8px
Cards                             : 10–12px
Modals, drawers, large containers : 12–16px
Avatars, pills, circular elements : 9999px (full round)

---

## 6. SHADOWS

Subtle  (cards at rest)    : 0 2px 8px rgba(15, 23, 42, 0.06)
Medium  (cards on hover)   : 0 4px 12px rgba(15, 23, 42, 0.10)
Strong  (dragged elements) : 0 8px 24px rgba(15, 23, 42, 0.15)
Focus   (input glow)       : 0 0 0 3px rgba(15, 23, 42, 0.15)

---

## 7. COMPONENT SPECIFICATIONS

### Buttons
Height          : 40px (default) | 48px (primary/mobile)
Padding         : 10px vertical / 16px horizontal (default)
Primary state   : Deep Blue background, Pure White text
Hover state     : opacity 0.9 (0.2s ease transition)
Disabled state  : Soft Gray background (#E2E8F0), not-allowed cursor
Loading state   : Replace label text with spinner, keep button disabled
Focus state     : Blue glow ring

### Input Fields
Height          : 40px (default) | 48px (mobile)
Padding         : 10px horizontal
Border          : 1px solid Soft Gray (#E2E8F0) at rest
Focus border    : Deep Blue (#0F172A) + blue glow shadow
Error border    : Muted Red (#EF4444)
Readonly style  : Light Gray background, not-allowed cursor
Label position  : Above input (not placeholder-as-label)
Transition      : 0.2s cubic-bezier(0.4, 0, 0.2, 1)

### Cards
Background      : Pure White
Border radius   : 10–12px
Shadow          : Subtle (2px 8px)
Padding         : 20–24px
Hover shadow    : Medium (4px 12px)
Transition      : 0.2s ease on shadow

### Badges
Padding         : 2px 8px
Border radius   : 4px
Font size       : 11px, font weight 600
Emerald badge   : rgba(16,185,129,0.1) background, #10B981 text
Red badge       : rgba(239,68,68,0.1) background, #EF4444 text
Amber badge     : rgba(245,158,11,0.1) background, #F59E0B text
Gray badge      : Soft Gray background, #64748B text

### Toggle Switch
Dimensions      : 44px wide × 24px tall
Track off       : Soft Gray (#E2E8F0)
Track on        : Deep Blue (#0F172A)
Thumb           : 20px × 20px Pure White circle, 2px from edge
Animation       : transform translateX(20px) over 0.2s ease
Spring physics  : cubic-bezier(0.34, 1.56, 0.64, 1) for iOS feel

### Modals
Backdrop        : rgba(0,0,0,0.4) blur(4px)
Animation in    : slide down from translateY(-20px) + fade in, 0.3s ease
Animation out   : reverse, 0.2s ease
Position        : centered, max-width 480px
Padding         : 32px
Close on        : backdrop click, ESC key, explicit close button

### Drawer (Tenant Directory, Slide-out panels)
Width           : 40% of viewport (desktop) | 100% (mobile)
Animation       : translateX(100%) → translateX(0), 0.35s cubic-bezier(0.16, 1, 0.3, 1)
Backdrop        : rgba(0,0,0,0.3)
Close on        : backdrop click, ESC key

### Toast Notifications
Position        : Bottom center (mobile) | Bottom right (desktop)
Duration        : 3 seconds auto-dismiss
Animation in    : slide up + fade, 0.3s ease
Animation out   : fade, 0.2s ease

---

## 8. LAYOUT SYSTEMS

### Landlord Portal (Desktop)
Pattern         : F-Pattern reading layout
Sidebar         : 260px fixed left, Deep Blue background
Main canvas     : flex:1, Light Gray background, 24px padding
Top metrics row : 3-column CSS Grid, equal width
Lower split     : 2-column CSS Grid, 1fr 1fr
Breakpoints     : Optimized for 1280px+ but functional at 768px+

### Tenant Portal (Mobile-first)
Max width       : 420px centered
Padding         : 16px
Hero card       : 90% screen width, centered
Action buttons  : 3-column grid, 48px minimum height
Stack layout    : Single column, top-to-bottom priority

---

## 9. ANIMATION SYSTEM

### Timing Functions
Default ease        : cubic-bezier(0.4, 0, 0.2, 1)  — Material standard
Spring/bounce       : cubic-bezier(0.34, 1.56, 0.64, 1)  — iOS toggle feel
Drawer entrance     : cubic-bezier(0.16, 1, 0.3, 1)  — Expo out

### Duration Scale
Instant feedback    : 100ms (button press, toggle)
Standard transition : 200ms (hover states, border changes)
Modal/drawer entry  : 300–350ms
Page-level          : 400–600ms

### Named Animations
countUp             : opacity 0→1, translateY 4px→0 — dashboard metrics on load
shake               : translateX oscillation — login error, blocked actions
slideInRight        : translateX(100%)→(0) — drawer open
pulseRed            : box-shadow glow expand and collapse every 3s — expired docs
drawCheck           : SVG path stroke-dashoffset 0→length — payment success
fadeUpReveal        : opacity 0→1, translateY 20px→0 — landing page scroll reveal
numberTicker        : staggered countUp for metric cards

### State Change Animations
Kanban drag         : card tilts 3deg, strong shadow, valid drop zones highlight dashed Deep Blue
Button loading      : spinner replaces label, button width preserved
Toggle activation   : thumb slides with spring physics
Progress bar fill   : width expands smoothly as checkboxes tick

---

## 10. UX PRINCIPLES

### 10.1 Affordance
Every interactive element must look like what it does.
Disabled elements must look disabled (gray, not-allowed cursor, tooltip).
Readonly fields must look uneditable (gray background, lock icon where appropriate).

### 10.2 Progressive Disclosure
Show only what the user needs at the current step.
Tenant Dashboard: 3 action buttons — not all 11 pages.
Lease creation: invite step appears only after basic details are valid.
Inspection: room details reveal only when accordion expands.

### 10.3 Optimistic UI
Update the UI immediately on user action.
Roll back with explanation if the server rejects the change.
Applied to: chat messages, Kanban drag, notification read state.

### 10.4 Error States
Every form has three states: Default, Active (focus), Error.
Error messages appear below the relevant field — never as alerts.
Error messages are specific ("Lease dates overlap with Unit 2A: Jan–Mar") not generic.
Submit button disables on error state.

### 10.5 Empty States
Every list, table, and feed has a designed empty state.
Empty state includes an icon, a message, and a primary action.
No blank white spaces — every empty UI communicates something.

### 10.6 Loading States
Every async operation has a loading state.
Skeleton screens for data-heavy pages (dashboard, invoice table).
Spinner in button for form submissions.
Never leave the user wondering if something happened.
```

---

# FILE 6 — `system_design.md`

```md
# ⚙️ system_design.md
# Rent & Lease Management System — System Design Decisions
# Patterns | Trade-offs | Data Flow | Key Design Choices

---

## 1. AUTHENTICATION DESIGN

### Decision: JWT (JSON Web Tokens)
Rationale:
- Stateless — no server-side session storage required
- Scalable — any server in a load-balanced environment can verify any token
- Self-contained — token carries user ID and role, reducing database lookups per request
- Industry standard for REST API authentication

Rules:
- Tokens expire after 24 hours
- Token payload contains: user_id, role, iat (issued at), exp (expiry)
- Token is verified on every request by Authentication Middleware
- Token is stored in memory (JavaScript variable) — never in localStorage (XSS risk)
- Token is sent via Authorization: Bearer header — never in URL parameters

### Password Reset Design
- One-time token generated using cryptographically secure random bytes
- Token hashed before storage — plain token is sent in email, hash stored in DB
- Token expires after exactly 15 minutes
- Token is invalidated immediately upon use — cannot be reused
- Old reset tokens are purged on new request generation

---

## 2. REAL-TIME DESIGN

### Decision: WebSockets for Chat and Notifications
Rationale:
- REST is request-response — unsuitable for push-based real-time delivery
- WebSockets maintain a persistent bidirectional connection
- Message latency under 100ms vs 300-500ms for polling approaches

### Chat Architecture
- One conversation record per unique Landlord-Tenant pair
- Messages reference conversation_id, sender_id, content, timestamp
- File attachments: stored in file system, message stores the file path reference
- History loaded via REST on thread open (last 50 messages, paginated)
- New messages pushed via WebSocket — no polling

### Notification Architecture
- Notifications generated by server-side events (payment processed, ticket updated)
- Pushed to connected user's WebSocket client immediately
- If user is offline, notification is stored in DB and delivered on next connection
- Real-time notification badge count updated via WebSocket push

---

## 3. PAYMENT DESIGN

### Decision: Third-party gateway integration (Stripe / Paystack)
Rationale:
- PCI compliance is the gateway's responsibility, not ours
- Card data never touches our servers
- Tokenization handles card storage securely

### Payment Flow Design
- Frontend sends: invoice_id + payment_method_token (no amount)
- Server retrieves correct amount from database (user cannot modify amount)
- Server sends to gateway: amount, currency, token, idempotency_key
- Gateway processes and returns: success/failure + transaction_id
- Webhook from gateway independently confirms the charge cleared
- Database update happens only after webhook confirmation — not on initial response
- This two-step design prevents false positives and duplicate records

### Idempotency
- Every payment request generates a unique idempotency_key
- Key composed of: user_id + invoice_id + date
- Gateway and our DB both reject duplicate submissions with the same key
- Prevents double-charging from network retries or double-tap

---

## 4. DATABASE DESIGN PATTERNS

### Soft Deletes
Applied to: users, properties, leases, tenants
Mechanism: deleted_at TIMESTAMP column, NULL when active
Queries: all standard queries include WHERE deleted_at IS NULL
Rationale: preserves historical data integrity, audit trail, financial records

### Append-Only Tables
Applied to: audit_log, transactions
Mechanism: no UPDATE or DELETE operations allowed on these tables
Rationale: immutable financial and security records

### UTC Timestamps
All created_at, updated_at, event timestamps stored in UTC
Conversion to user timezone handled at display layer (JavaScript)
Rationale: consistent across timezones, no DST corruption

### Optimistic Locking (Concurrent Updates)
Applied to: maintenance_tickets (Kanban drag)
Mechanism: version column incremented on each update
Write includes: WHERE id = ? AND version = [read version]
On mismatch: reject write, return conflict error, show user fresh data

---

## 5. CRON JOB DESIGN

### Toggleable Automation
Landlord can enable/disable each automation independently
State stored in automation_settings table per landlord
Scheduler reads state before execution — skips if disabled
State change takes effect on next scheduled run

### Retry Logic
Failed jobs retry up to 3 times with exponential backoff
Failure logged to cron_jobs table with error detail
After 3 failures, alert is logged (not emailed — email may be the failure cause)

### Late Fee Application
Runs nightly at 00:05 UTC (after midnight in most target timezones)
Selects: invoices WHERE status='Outstanding' AND due_date < TODAY AND late_fee_applied = FALSE
Applies 5% of lease.monthly_rent as new fee record
Updates invoice total
Sets late_fee_applied = TRUE flag (prevents double application)

---

## 6. DOCUMENT STORAGE DESIGN

### Decision: File system storage, database stores metadata
Rationale:
- Storing binary files in SQL databases bloats the database
- Slows all non-file queries
- Increases backup size disproportionately
- File system or object storage is designed for binary data

### IDOR Protection on Downloads
Every download request:
1. Extracts requester user_id from verified JWT
2. Queries: SELECT owner_id FROM documents WHERE id = ?
3. Compares: requester user_id == document owner_id
4. If mismatch: 403 response, event logged to audit_log
5. If match: stream file from file system with appropriate headers

---

## 7. RATE LIMITING DESIGN

Two-tier approach:

Tier 1 — Middleware (Broad protection)
Applies to: all routes
Limit: 200 requests per minute per IP
Blocked response: 429 with retry-after header

Tier 2 — API Endpoint (Precise protection)
Applies to: specific sensitive endpoints
Login: 10 attempts per 15 minutes per IP
Payment: 3 attempts per 5 minutes per authenticated user
Registration: 5 attempts per hour per IP
Document upload: 20 per hour per user
Chat: 60 messages per minute per user

---

## 8. IDOR PREVENTION DESIGN

Applied at two levels:

Level 1 — Middleware (General pattern)
Reads resource_id from request, queries owner, compares to JWT user_id
Blocks with 403 if mismatch
Logs event to audit_log

Level 2 — Query Level (Specific enforcement)
Every data retrieval query for user-owned resources includes:
WHERE resource.owner_id = [authenticated user id from JWT]
Even if Middleware is bypassed (defense in depth), the query returns no data
A resource that doesn't belong to the requester is invisible at the data level

---

## 9. ANALYTICS DESIGN

### Caching Strategy
Analytics queries are expensive (GROUP BY across large transaction tables)
Cache computed results for 5 minutes per Landlord
On cache hit: return cached JSON immediately
On cache miss: run aggregation query, store result, return to client
Cache invalidated on new payment record for that Landlord

### Chart.js Data Contract
API returns data in the exact shape Chart.js expects
Frontend passes data directly to Chart.js — no frontend transformation
This means if chart library changes, only the API response format changes
```

---

# FILE 7 — `security.md`

```md
# 🔒 security.md
# Rent & Lease Management System — Security Architecture
# All Security Rules, Policies, Protections, and Threat Mitigations

---

## 1. SECURITY PHILOSOPHY

Security is not a feature. It is an architecture decision made at the start.
Every layer enforces its own security independently (Defence in Depth).
No layer trusts the previous layer to have already handled security.
The frontend is entirely untrusted. Every validation there is for UX only.

---

## 2. AUTHENTICATION SECURITY

### JWT Token Security
- Algorithm      : HS256 minimum, RS256 preferred in production
- Secret         : Stored in environment variable — never in source code
- Expiry         : 24 hours
- Storage        : Memory (JavaScript variable) — never localStorage or sessionStorage
  Rationale      : localStorage is accessible to any JavaScript on the page (XSS attack)
- Transmission   : Authorization: Bearer header only — never URL parameters
  Rationale      : URL parameters appear in server logs and browser history
- Verification   : Signature verified cryptographically on every request by Middleware
- Tampering      : Any modification to payload or signature invalidates the token entirely

### Password Security
- Algorithm      : bcrypt with work factor 12
- Storage        : Only the hash is ever stored — plain text is never written anywhere
- Reset tokens   : Cryptographically random, hashed before storage, 15-minute TTL
- Minimum length : 8 characters enforced at API boundary
- Brute force    : Rate limiting on login endpoint (10 attempts / 15 min per IP)

---

## 3. AUTHORIZATION & IDOR PREVENTION

### The IDOR Threat
Insecure Direct Object Reference: A user guesses or obtains the ID of another user's resource
(lease, invoice, document, chat message) and accesses it by constructing the URL directly.

### Defense Layer 1 — Authorization Middleware
Every request to a resource endpoint extracts the resource ID from the request.
Middleware queries the database for the resource's owner_id.
Compares owner_id to the authenticated user's ID from the JWT.
If mismatch: returns 403, logs the event to audit_log with full details.
The API route never executes.

### Defense Layer 2 — Query-Level Scoping
Every SELECT, UPDATE, DELETE query for user-owned resources includes:
WHERE [resource].owner_id = [JWT user_id]
This means even if Middleware is bypassed (compromised or misconfigured),
the database query returns empty results for any resource not owned by the requester.
Zero data is leaked. Defense in depth at the data layer.

### Defense Layer 3 — Response Scrubbing
API responses never include fields that expose other users' identifiers.
password_hash is never included in any API response, ever.
Full tokens are never returned after creation.

---

## 4. INPUT VALIDATION & INJECTION PREVENTION

### SQL Injection Prevention
All SQL queries use parameterized statements / prepared statements.
User input is always a parameter placeholder — never concatenated into SQL strings.
This makes SQL injection categorically impossible at the query level.
Applied to: every SELECT, INSERT, UPDATE, DELETE in the system.

### XSS (Cross-Site Scripting) Prevention
All user-generated content is HTML-escaped before rendering in the browser.
Content Security Policy header restricts which scripts can execute.
Script sources are whitelisted — inline scripts from user data cannot execute.
No use of innerHTML with user content — textContent or escaped HTML only.

### CSRF Prevention
All state-changing forms include a CSRF token hidden field.
Token is generated server-side, stored in session, validated on every POST/PUT/DELETE.
Token is cryptographically random, unique per session.
On mismatch: request rejected with 403.

### File Upload Security
File type validated by extension AND MIME type AND file content (magic bytes).
Dangerous extensions rejected: .php, .py, .exe, .sh, .js (server-side)
Maximum file size enforced: configurable, default 10MB per upload.
Files stored outside the web root — cannot be directly accessed via URL.
Files served through the authenticated download endpoint only.

---

## 5. TRANSPORT SECURITY

### HTTPS
All production traffic served over HTTPS/TLS.
HTTP requests automatically redirected to HTTPS (301 permanent).
HTTP Strict Transport Security (HSTS) header enforced:
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

### Security Headers (applied by Middleware to every response)
X-Frame-Options: DENY
  Prevents embedding in iframes (clickjacking attack prevention)

X-Content-Type-Options: nosniff
  Prevents MIME type sniffing (browser cannot interpret a file as a different type)

X-XSS-Protection: 1; mode=block
  Legacy browsers XSS filter

Referrer-Policy: strict-origin-when-cross-origin
  Controls what referrer information is sent with requests

Permissions-Policy: geolocation=(), microphone=(), camera=()
  Restricts access to browser APIs the system does not use

Content-Security-Policy:
  default-src 'self';
  script-src 'self';
  style-src 'self' 'unsafe-inline';
  font-src 'self';
  img-src 'self' data:;
  connect-src 'self' wss://[websocket-domain];

---

## 6. RATE LIMITING

### Purpose
Prevents: brute force attacks, credential stuffing, payment fraud, DoS, API abuse

### Tier 1 — Middleware (Broad)
All routes: 200 requests per minute per IP
Response: 429 Too Many Requests
Headers returned: Retry-After: [seconds]

### Tier 2 — API Endpoint (Specific)
POST /api/auth/login           : 10 per 15 minutes per IP
POST /api/auth/register        : 5 per hour per IP
POST /api/auth/forgot-password : 3 per hour per email
POST /api/payments/submit      : 3 per 5 minutes per authenticated user
POST /api/documents/upload     : 20 per hour per authenticated user
POST /api/maintenance/tickets  : 10 per hour per authenticated user

---

## 7. AUDIT LOGGING

### What Is Logged
Every authentication event (login, logout, failed login, token refresh)
Every authorization failure (403 responses with resource ID and requester ID)
Every payment event (initiated, succeeded, failed, webhook received)
Every lease event (created, modified, invited, renewed)
Every document event (uploaded, downloaded, deleted)
Every admin-level toggle change (cron job settings)
Every rate limit block (IP, endpoint, timestamp)

### Audit Log Rules
Append-only: no UPDATE or DELETE operations on audit_log table
Every record is immutable after INSERT
Contains: event_type, user_id, resource_type, resource_id, ip_address, user_agent, timestamp (UTC), result
Retained: minimum 2 years
Access: server-side only — no API endpoint exposes raw audit logs to users

---

## 8. SENSITIVE DATA HANDLING

### Never Stored
- Plain text passwords (bcrypt hash only)
- Full payment card numbers (tokenized by gateway)
- CVV numbers (never)
- Full government ID content (only file path to encrypted document)

### Never Returned in API Responses
- password_hash field
- JWT secret key
- Reset token plain text (hash only in DB, plain text sent in email once)
- Other users' personal data

### Environment Variables (Never in Source Code)
- DATABASE_URL
- JWT_SECRET_KEY
- PAYMENT_GATEWAY_API_KEY
- SMTP_PASSWORD
- WEBSOCKET_SECRET

---

## 9. ERROR HANDLING SECURITY

### User-Facing Messages
Generic: "Something went wrong. Please try again."
Authentication: "Invalid email or password." (never specify which is wrong)
Rate limit: "Too many requests. Try again in [N] seconds."
Forbidden: "You do not have permission to access this resource."
Not Found: "The requested page does not exist."

### Server Logs
Full stack trace
Full error message
SQL query that failed (without user data values)
User ID and endpoint (for context)
Timestamp

### Rule: Zero stack traces in browser
Debug mode is disabled in production.
All unhandled exceptions are caught and return generic 500 response.
No framework error pages exposed to users.

---

## 10. OWASP TOP 10 COMPLIANCE STATUS

A01 Broken Access Control      : MITIGATED — IDOR middleware + query-level scoping
A02 Cryptographic Failures     : MITIGATED — HTTPS, bcrypt, hashed tokens, no plain text secrets
A03 Injection                  : MITIGATED — 100% parameterized queries, input validation
A04 Insecure Design            : MITIGATED — Security designed into architecture from start
A05 Security Misconfiguration  : MITIGATED — Security headers, debug off, secrets in env
A06 Vulnerable Components      : ONGOING — Dependencies updated regularly
A07 Auth Failures              : MITIGATED — JWT, bcrypt, rate limits, short TTL tokens
A08 Software Integrity         : MITIGATED — Dependency verification in CI/CD
A09 Logging Failures           : MITIGATED — Audit log, request logging, immutable records
A10 SSRF                       : MITIGATED — No server-side URL fetch from user input
```

---

# FILE 8 — `risk_management.md`

```md
# ⚠️ risk_management.md
# Rent & Lease Management System — Risk Management Document
# All Identified Risks | Likelihood | Impact | Mitigation | Contingency

---

## 1. RISK ASSESSMENT FRAMEWORK

Likelihood : LOW | MEDIUM | HIGH
Impact     : LOW | MEDIUM | HIGH | CRITICAL
Priority   : Likelihood × Impact (1–9 scale)

---

## 2. TECHNICAL RISKS

---

### RISK-T01 — SQL Injection Attack
Likelihood : LOW (if parameterized queries are enforced)
Impact     : CRITICAL (full database access, data destruction)
Priority   : HIGH

Description:
An attacker submits malicious SQL syntax through any input field, form, or URL parameter,
causing the database to execute arbitrary commands.

Mitigation:
- 100% parameterized queries — no string concatenation in any SQL query
- Input validation at API boundary before data reaches any query
- Database user has minimum required permissions (no DROP TABLE access)

Contingency:
- Immediate incident response: revoke database credentials, restore from backup
- Audit all data for corruption
- Notify affected users per data breach protocol

---

### RISK-T02 — JWT Token Compromise
Likelihood : LOW (if stored correctly)
Impact     : HIGH (unauthorized access to user accounts)
Priority   : MEDIUM

Description:
A JWT token is stolen from localStorage (XSS attack) or intercepted in transit (HTTPS failure),
allowing an attacker to impersonate a user.

Mitigation:
- Tokens stored in memory only — never localStorage or sessionStorage
- HTTPS enforced on all production traffic
- Short 24-hour token expiry
- Token secret stored in environment variable only

Contingency:
- Rotate JWT secret key (invalidates all active tokens, forces re-login)
- Notify affected user to change password
- Log and audit all activity under the compromised token

---

### RISK-T03 — Double Payment Processing
Likelihood : MEDIUM (network issues are common)
Impact     : HIGH (financial loss, trust damage, legal risk)
Priority   : HIGH

Description:
A user submits a payment, network drops, user resubmits, both requests reach the gateway
and result in double charges.

Mitigation:
- Idempotency keys on all payment requests
- Submit button disabled after first tap
- Gateway-level duplicate detection
- Database unique constraint on (invoice_id, gateway_transaction_id)

Contingency:
- Automatic refund of duplicate charge via gateway API
- Notification to both Landlord and Tenant
- Manual audit of all transactions within the incident window

---

### RISK-T04 — WebSocket Connection Failure (Chat Disruption)
Likelihood : MEDIUM (network conditions vary)
Impact     : MEDIUM (communication disruption, messages lost)
Priority   : MEDIUM

Description:
WebSocket connection drops, user continues typing and sending messages,
messages are lost because no reconnection or queuing exists.

Mitigation:
- Auto-reconnection logic with exponential backoff
- Unsent messages queued locally and retried on reconnect
- Online/offline indicator in chat UI so users know the connection status
- All messages persisted to database on server receipt

Contingency:
- Users can reload to re-establish connection
- Message history is always available from database on reconnect

---

### RISK-T05 — Cron Job Duplicate Late Fee Application
Likelihood : LOW (with proper flag tracking)
Impact     : HIGH (financial error, Tenant complaints, trust damage)
Priority   : MEDIUM

Description:
The nightly late fee cron job runs twice (server restart mid-execution, scheduler misconfiguration),
applying 5% late fees twice to the same invoices.

Mitigation:
- late_fee_applied BOOLEAN column on invoices table — checked before applying
- Cron job skips any invoice where late_fee_applied = TRUE
- Idempotent by design — running twice produces same result as once
- Scheduler configured with distributed lock (only one instance runs per job)

Contingency:
- Detect via analytics anomaly (double fees in same night)
- Script to identify and reverse duplicate fee applications
- Notify affected tenants

---

### RISK-T06 — File System Storage Failure (Document Vault)
Likelihood : LOW (with redundant storage)
Impact     : HIGH (Lease documents, compliance files lost)
Priority   : MEDIUM

Description:
The server file system fails or is corrupted, losing all uploaded documents while
database records still exist pointing to non-existent files.

Mitigation:
- Production file storage on cloud object storage (S3-compatible) rather than local disk
- Regular automated backups of file storage
- Database records include file hash for integrity verification

Contingency:
- Restore from backup
- Notify affected Landlords to re-upload critical documents
- Provide UI for broken file link detection and re-upload

---

## 3. BUSINESS RISKS

---

### RISK-B01 — Tenant Data Privacy Breach
Likelihood : LOW (with all security measures)
Impact     : CRITICAL (legal liability, regulatory fines, trust destruction)
Priority   : HIGH

Description:
Tenant personal data (name, address, payment history, government ID) is exposed
through a security vulnerability or data breach.

Mitigation:
- IDOR protection at all levels
- Sensitive files stored outside web root
- Minimum data exposure in API responses
- bcrypt for passwords, tokenization for payment data

Contingency:
- Incident response team activated within 1 hour
- Affected users notified within 24 hours
- Regulatory authority notified within 72 hours (GDPR requirement where applicable)
- Full security audit before service restoration

---

### RISK-B02 — Landlord Disputes Late Fee Application
Likelihood : MEDIUM (business reality)
Impact     : LOW (manageable if audit trail exists)
Priority   : LOW

Description:
A Tenant disputes a late fee, claiming it was applied incorrectly.
Without an audit trail, it becomes a "he said / she said" dispute.

Mitigation:
- Immutable audit_log records every fee application with timestamp, invoice ID, amount, calculation
- Tenant receives email notification when fee is applied (with date and calculation)
- Landlord cron job toggle provides explicit control and accountability

Contingency:
- Present audit log to resolve dispute
- Landlord can manually reverse fee via Expense & ROI Ledger

---

### RISK-B03 — Payment Gateway Downtime
Likelihood : LOW (major gateways have 99.9%+ uptime)
Impact     : HIGH (tenants cannot pay rent during downtime)
Priority   : MEDIUM

Description:
Stripe or Paystack experiences an outage, preventing all rent payments.

Mitigation:
- Graceful degradation — system remains functional, only payment fails
- Clear user message: "Payment processing temporarily unavailable. Your payment is not due now."
- Landlord offline payment recording allows manual recording of cash payments

Contingency:
- Monitor gateway status page
- Notify affected tenants proactively
- Process backlog of payments when gateway restores

---

## 4. PROJECT DELIVERY RISKS

---

### RISK-P01 — Scope Creep
Likelihood : HIGH (common in student/team projects)
Impact     : MEDIUM (delayed delivery, incomplete features)
Priority   : HIGH

Description:
New feature ideas are added during development, delaying delivery of core features.

Mitigation:
- prd.md defines the fixed scope — all new requests evaluated against out-of-scope list
- Weekly review: are we on the Phase plan from plan.md?
- Any new feature request deferred to a post-MVP backlog document

---

### RISK-P02 — Database Schema Changes Mid-Development
Likelihood : MEDIUM
Impact     : HIGH (requires refactoring multiple layers)
Priority   : HIGH

Description:
A fundamental schema change is discovered mid-build, requiring rewrites in business logic,
API responses, and frontend display.

Mitigation:
- Database schema reviewed and signed off before Phase 1 begins
- Schema changes after Phase 1 require formal decision with impact analysis
- All schema is in database.sql — single source of truth

---

### RISK-P03 — Real-Time Features Complexity Underestimated
Likelihood : MEDIUM
Impact     : MEDIUM (chat and notifications may be delayed)
Priority   : MEDIUM

Description:
WebSocket implementation is more complex than anticipated, delaying Phase 5.

Mitigation:
- Chat is scheduled in Phase 5 (Week 10) with dedicated focus
- Fallback plan: implement polling (every 3 seconds) as temporary substitute
- Core system (payments, leases, maintenance) does not depend on real-time features

Contingency:
- Deploy polling-based notifications as MVP, upgrade to WebSockets post-deadline

---

## 5. RISK REGISTER SUMMARY

| ID        | Risk                            | Likelihood | Impact   | Priority | Status  |
|---|---|---|---|---|---|
| RISK-T01  | SQL Injection                   | LOW        | CRITICAL | HIGH     | MITIGATED |
| RISK-T02  | JWT Token Compromise            | LOW        | HIGH     | MEDIUM   | MITIGATED |
| RISK-T03  | Double Payment Processing       | MEDIUM     | HIGH     | HIGH     | MITIGATED |
| RISK-T04  | WebSocket Failure               | MEDIUM     | MEDIUM   | MEDIUM   | MITIGATED |
| RISK-T05  | Duplicate Late Fee              | LOW        | HIGH     | MEDIUM   | MITIGATED |
| RISK-T06  | File Storage Failure            | LOW        | HIGH     | MEDIUM   | MONITORING |
| RISK-B01  | Tenant Data Breach              | LOW        | CRITICAL | HIGH     | MITIGATED |
| RISK-B02  | Late Fee Dispute                | MEDIUM     | LOW      | LOW      | MITIGATED |
| RISK-B03  | Payment Gateway Downtime        | LOW        | HIGH     | MEDIUM   | MONITORING |
| RISK-P01  | Scope Creep                     | HIGH       | MEDIUM   | HIGH     | ACTIVE CONTROL |
| RISK-P02  | Schema Changes Mid-Dev          | MEDIUM     | HIGH     | HIGH     | ACTIVE CONTROL |
| RISK-P03  | Real-Time Complexity            | MEDIUM     | MEDIUM   | MEDIUM   | MONITORING |
```

---

# FILE 9 — `implementation_plan.md`

```md
# 🛠️ implementation_plan.md
# Rent & Lease Management System — Implementation Plan
# Build Order | Dependencies | Integration Points | Verification Gates

---

## 1. THE GOLDEN RULE OF BUILD ORDER

Never build a feature before its foundation is in place.
The correct build order is:
Database Schema → Security Layer → Authentication → Core CRUD → Advanced Features → Real-Time → Automation

Every phase depends on everything before it being correct and tested.
A broken authentication layer makes every feature built on top of it insecure.

---

## 2. PHASE BUILD ORDER WITH DEPENDENCIES

### PHASE 0 — FOUNDATION
Build order:
1. All .md documentation files
2. Database schema (all tables, all constraints, all indexes)
3. Design system (CSS variables, base components)
4. Base HTML templates (layout_landlord, layout_tenant, layout_auth)
5. Environment configuration
6. Project folder structure
7. Git repository + .gitignore

No dependencies — this is the dependency for everything else.

---

### PHASE 1 — SECURITY PERIMETER
Build order:
1. Security Headers Middleware (runs first on every request)
2. CORS Middleware
3. Request Logging Middleware + audit_log table
4. Rate Limiting Middleware (broad)
5. Authentication Middleware (JWT verification)
6. Authorization Middleware (IDOR base check)
7. Login API endpoint + login page
8. Registration API endpoint + registration page
9. Email verification flow
10. Password reset flow (forgot + reset pages)
11. Lease Invitation Gateway

Dependencies: Phase 0 complete
Verification Gate: Can register, verify email, log in, receive JWT, hit protected route

---

### PHASE 2 — LANDLORD CORE
Build order:
1. Landlord Dashboard page + API endpoint (GET /api/landlord/dashboard)
2. Property Portfolio page + CRUD endpoints + properties table
3. Building management + buildings table
4. Leases page + lease creation + overlap validation
5. Tenant invitation within lease creation
6. Tenant Directory + slide-out drawer
7. Financials page + invoice table
8. Expense ledger + ROI calculator

Dependencies: Phase 1 complete (authenticated routes)
Verification Gate: Landlord can add property → create lease → invite tenant → view financials

---

### PHASE 3 — TENANT CORE
Build order:
1. Tenant Dashboard + hero card (reads from invoices table)
2. Rent Payment page + payment gateway integration
3. Payment webhook endpoint
4. Payment Success + Cancelled pages
5. My Lease page (reads from leases + documents tables)
6. Payment Methods + Auto-Pay toggle
7. Profile & Settings (locked email)
8. Compliance document upload

Dependencies: Phase 2 complete (leases and invoices must exist for tenants to pay)
Verification Gate: Tenant can log in → see balance → pay rent → download receipt

---

### PHASE 4 — MAINTENANCE
Build order:
1. Maintenance tickets table + ticket_comments table
2. Tenant ticket submission endpoint + page
3. Landlord Kanban board + drag-and-drop status update endpoint
4. Priority tag system
5. Follow-up comment system
6. Inspections table + Move-In/Move-Out form
7. Progress calculation logic

Dependencies: Phase 2 + Phase 3 (need active tenants with leases)
Verification Gate: Tenant submits ticket → appears on Kanban → Landlord resolves → Tenant notified

---

### PHASE 5 — REAL-TIME
Build order:
1. WebSocket server setup + authentication
2. Conversation + messages table
3. Chat history REST endpoint
4. Landlord chat UI (two-pane)
5. Tenant chat UI (single thread)
6. Typing indicators + read receipts
7. File attachment support
8. Notifications WebSocket push
9. Notification feed UI (Landlord + Tenant)
10. Notice Board (Landlord publish → Tenant read)

Dependencies: Phase 1 (WebSocket needs JWT auth)
Verification Gate: Landlord sends message → Tenant receives instantly → read receipt updates

---

### PHASE 6 — ANALYTICS + AUTOMATION
Build order:
1. Analytics aggregation queries (revenue by month)
2. Analytics API endpoints + Chart.js integration
3. Cron job infrastructure (scheduler setup)
4. automation_settings table
5. Automation Control Panel UI + toggle endpoints
6. Late fee cron job
7. Lease expiry scanner
8. Rent reminder email cron job
9. Auto-Pay processor

Dependencies: Phase 2 + Phase 3 (need financial data for analytics)
Verification Gate: Analytics charts load with real data, late fee applies correctly overnight

---

### PHASE 7 — DOCUMENTS
Build order:
1. Documents + folders tables
2. Upload endpoint (file validation + storage)
3. IDOR-protected download endpoint
4. Document grid UI
5. Delete with confirmation

Dependencies: Phase 1 (IDOR protection requires auth)
Verification Gate: Upload file → appears in grid → download works → other user cannot download

---

### PHASE 8 — PUBLIC SHELL
Build order:
1. Landing page (hero, features, CTAs)
2. Sticky navbar scroll behavior
3. Scroll reveal animations
4. All error pages (403, 429, 404, 503)

Dependencies: Design system complete
Verification Gate: Visitor lands → reads value proposition → clicks Get Started → reaches registration

---

### PHASE 9 — TESTING
Verification tests:
- Authentication: all invalid token scenarios return 401
- Authorization: all IDOR scenarios return 403 and log to audit
- Rate limiting: all limits trigger 429 at correct thresholds
- SQL: all parameterized queries verified (no string concatenation)
- XSS: all user input escaped in output
- CSRF: all form submissions validated
- Payments: idempotency tested, double-tap prevented
- Cron jobs: all automations run without duplicates
- Mobile: all Tenant pages tested at 375px viewport
- Performance: all pages under 3 seconds load time

---

### PHASE 10 — FINAL DELIVERY
Checklist:
- All 38 pages functional and tested
- All animations and transitions complete
- All empty states and loading states implemented
- All .md documentation files current and accurate
- Staging deployment verified
- Demo walkthrough prepared and rehearsed

---

## 3. INTEGRATION POINTS

| Component | Integrates With | Protocol | Authentication |
|---|---|---|---|
| Frontend | Python API | HTTP REST | JWT in Authorization header |
| Frontend | Python WebSocket | WebSocket | JWT on connect |
| Python API | Payment Gateway | HTTPS REST | API Key (env var) |
| Payment Gateway | Python API | HTTPS Webhook | Webhook signature |
| Python Scheduler | Python Business Logic | Internal call | Server-side |
| Python Backend | SMTP Email Service | SMTP | Credentials (env var) |
| Python Backend | File System / Object Storage | Local / S3 API | Credentials (env var) |

---

## 4. VERIFICATION GATES SUMMARY

| Phase | Gate Description |
|---|---|
| 0 | Project scaffolding functional, schema created |
| 1 | Register → verify → login → protected route → logout |
| 2 | Landlord full property + lease + financial workflow |
| 3 | Tenant full payment workflow with receipt |
| 4 | Full maintenance ticket lifecycle |
| 5 | Real-time chat with read receipts |
| 6 | Analytics load with data, cron job applies fee correctly |
| 7 | Document upload, display, download, IDOR block |
| 8 | Landing page to registration flow complete |
| 9 | All security tests pass |
| 10 | All 38 pages verified, staging deployed |
```

---

# FILE 10 — `file_structure.md`

```md
# 📁 file_structure.md
# Rent & Lease Management System — Project File Structure
# Every file and folder and what it owns

---

rent-lease-management/
│
├── .env                          # Environment variables (NEVER committed to git)
├── .env.example                  # Template showing required vars (committed, no values)
├── .gitignore                    # Excludes .env, __pycache__, uploads, logs
├── requirements.txt              # Python dependencies
│
├── docs/                         # All .md documentation files
│   ├── AI_rules.md
│   ├── plan.md
│   ├── prd.md
│   ├── architecture.md
│   ├── design.md
│   ├── system_design.md
│   ├── security.md
│   ├── risk_management.md
│   ├── implementation_plan.md
│   ├── file_structure.md
│   ├── naming_patterns.md
│   ├── tech_stack.md
│   └── database_schema.sql
│
├── frontend/                     # All HTML, CSS, JavaScript
│   │
│   ├── templates/                # HTML page files
│   │   ├── base/
│   │   │   ├── layout_landlord.html     # Sidebar + main content wrapper
│   │   │   ├── layout_tenant.html       # Mobile wrapper + bottom nav
│   │   │   └── layout_auth.html         # Centered card wrapper
│   │   │
│   │   ├── landlord/
│   │   │   ├── dashboard.html
│   │   │   ├── properties.html
│   │   │   ├── leases.html
│   │   │   ├── financials.html
│   │   │   ├── chat.html
│   │   │   ├── maintenance.html
│   │   │   ├── tenants.html
│   │   │   ├── documents.html
│   │   │   ├── analytics.html
│   │   │   ├── notifications.html
│   │   │   ├── settings.html
│   │   │   ├── expenses.html
│   │   │   ├── buildings.html
│   │   │   └── automations.html
│   │   │
│   │   ├── tenant/
│   │   │   ├── dashboard.html
│   │   │   ├── payments.html
│   │   │   ├── lease.html
│   │   │   ├── maintenance.html
│   │   │   ├── chat.html
│   │   │   ├── inspection.html
│   │   │   ├── payment_methods.html
│   │   │   ├── notice_board.html
│   │   │   ├── compliance.html
│   │   │   ├── profile.html
│   │   │   └── history.html
│   │   │
│   │   └── public/
│   │       ├── landing.html
│   │       ├── register.html
│   │       ├── login.html
│   │       ├── invite.html
│   │       ├── verify_email.html
│   │       ├── forgot_password.html
│   │       ├── reset_password.html
│   │       ├── payment_success.html
│   │       ├── payment_cancelled.html
│   │       ├── 403.html
│   │       ├── 429.html
│   │       ├── 404.html
│   │       └── 503.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── design_system.css         # All tokens, variables, base components
│   │   │   ├── layout_landlord.css       # Sidebar, F-pattern grid
│   │   │   ├── layout_tenant.css         # Mobile-first, single column
│   │   │   ├── animations.css            # All keyframes and transitions
│   │   │   └── components/
│   │   │       ├── buttons.css
│   │   │       ├── cards.css
│   │   │       ├── inputs.css
│   │   │       ├── badges.css
│   │   │       ├── modals.css
│   │   │       ├── drawers.css
│   │   │       ├── toggles.css
│   │   │       ├── kanban.css
│   │   │       ├── chat.css
│   │   │       └── charts.css
│   │   │
│   │   └── js/
│   │       ├── core/
│   │       │   ├── api.js               # All fetch() wrapper functions
│   │       │   ├── auth.js              # JWT token management (in memory)
│   │       │   ├── websocket.js         # WebSocket client + reconnection
│   │       │   └── utils.js             # Shared utility functions
│   │       │
│   │       ├── pages/
│   │       │   ├── landlord_dashboard.js
│   │       │   ├── landlord_properties.js
│   │       │   ├── landlord_leases.js
│   │       │   ├── landlord_financials.js
│   │       │   ├── landlord_chat.js
│   │       │   ├── landlord_maintenance.js
│   │       │   ├── landlord_analytics.js
│   │       │   ├── tenant_dashboard.js
│   │       │   ├── tenant_payments.js
│   │       │   ├── tenant_maintenance.js
│   │       │   ├── tenant_inspection.js
│   │       │   ├── tenant_chat.js
│   │       │   └── auth_forms.js
│   │       │
│   │       └── components/
│   │           ├── modal.js
│   │           ├── drawer.js
│   │           ├── kanban_drag.js
│   │           ├── toast.js
│   │           ├── file_upload.js
│   │           └── charts.js
│
├── backend/                      # All Python server code
│   │
│   ├── app.py                    # Application entry point
│   ├── config.py                 # Configuration loaded from environment variables
│   │
│   ├── middleware/               # All middleware functions
│   │   ├── security_headers.py
│   │   ├── cors.py
│   │   ├── request_logging.py
│   │   ├── rate_limiter.py
│   │   ├── authentication.py
│   │   └── authorization.py
│   │
│   ├── api/                      # All API route handlers
│   │   ├── auth_routes.py
│   │   ├── property_routes.py
│   │   ├── lease_routes.py
│   │   ├── financial_routes.py
│   │   ├── maintenance_routes.py
│   │   ├── chat_routes.py
│   │   ├── document_routes.py
│   │   ├── analytics_routes.py
│   │   ├── notification_routes.py
│   │   └── automation_routes.py
│   │
│   ├── business_rules/           # All constraint enforcement
│   │   ├── property_rules.py
│   │   ├── lease_rules.py
│   │   ├── payment_rules.py
│   │   ├── maintenance_rules.py
│   │   └── document_rules.py
│   │
│   ├── business_logic/           # All process orchestration
│   │   ├── auth_logic.py
│   │   ├── property_logic.py
│   │   ├── lease_logic.py
│   │   ├── payment_logic.py
│   │   ├── maintenance_logic.py
│   │   ├── chat_logic.py
│   │   ├── document_logic.py
│   │   ├── analytics_logic.py
│   │   └── notification_logic.py
│   │
│   ├── data/                     # All database operations
│   │   ├── connection.py         # Database connection pool
│   │   ├── retrieval/
│   │   │   ├── user_queries.py
│   │   │   ├── property_queries.py
│   │   │   ├── lease_queries.py
│   │   │   ├── financial_queries.py
│   │   │   ├── maintenance_queries.py
│   │   │   ├── chat_queries.py
│   │   │   ├── document_queries.py
│   │   │   └── analytics_queries.py
│   │   └── storage/
│   │       ├── user_writes.py
│   │       ├── property_writes.py
│   │       ├── lease_writes.py
│   │       ├── financial_writes.py
│   │       ├── maintenance_writes.py
│   │       ├── chat_writes.py
│   │       └── document_writes.py
│   │
│   ├── scheduler/                # All cron job definitions
│   │   ├── scheduler.py          # APScheduler setup
│   │   ├── late_fee_job.py
│   │   ├── lease_expiry_job.py
│   │   ├── rent_reminder_job.py
│   │   └── auto_pay_job.py
│   │
│   └── utils/                    # Shared utilities
│       ├── jwt_utils.py
│       ├── email_service.py
│       ├── password_utils.py
│       ├── file_utils.py
│       └── response_utils.py
│
├── database/
│   ├── schema.sql                # Complete database schema
│   ├── seed_data.sql             # Development test data
│   └── migrations/               # Schema change history
│
├── uploads/                      # Uploaded files (outside web root)
│   ├── documents/
│   ├── maintenance_photos/
│   └── compliance_docs/
│
└── logs/
    ├── app.log                   # Application events
    ├── audit.log                 # Security and financial audit events
    └── cron.log                  # Scheduled job execution records
```

---

# FILE 11 — `naming_patterns.md`

```md
# 🏷️ naming_patterns.md
# Rent & Lease Management System — Naming Conventions
# Every naming pattern for every file, function, variable, class, and database object

---

## 1. GENERAL NAMING PRINCIPLES

- Names must be explicit and self-documenting
- No abbreviations except universally accepted ones (id, url, api, jwt, sql, css, js)
- No single-letter variables except loop counters (i, j, k)
- No magic numbers — use named constants
- Names communicate intent — not implementation

---

## 2. PYTHON NAMING

Files             : snake_case          → payment_logic.py, auth_routes.py
Functions         : snake_case          → process_rent_payment(), validate_lease_overlap()
Variables         : snake_case          → monthly_rent, lease_start_date
Constants         : UPPER_SNAKE_CASE    → LATE_FEE_PERCENTAGE, JWT_EXPIRY_HOURS
Classes           : PascalCase          → LeaseManager, PaymentProcessor
Route prefixes    : /api/v1/[domain]    → /api/v1/payments, /api/v1/leases

Function naming pattern:
- Retrieval     : get_[thing]_by_[criteria]   → get_invoice_by_id(), get_leases_by_landlord()
- Storage       : create_[thing](), update_[thing](), delete_[thing]()
- Rules         : validate_[thing]_[constraint] → validate_lease_no_overlap()
- Logic         : process_[action]()           → process_rent_payment()
- Middleware    : check_[concern]()            → check_authentication(), check_rate_limit()

---

## 3. JAVASCRIPT NAMING

Files             : camelCase           → landlordDashboard.js, fileUpload.js
Functions         : camelCase           → submitPayment(), openDrawer(), fetchChatHistory()
Variables         : camelCase           → currentInvoice, isLoading, selectedTenantId
Constants         : UPPER_SNAKE_CASE    → MAX_FILE_SIZE_MB, API_BASE_URL
DOM references    : camelCase + El      → submitBtnEl, balanceCardEl, fileInputEl
Event handlers    : handle[Event][Target] → handleClickPayButton(), handleChangeFileInput()

---

## 4. CSS NAMING (BEM-Inspired)

Block             : [component]         → .card, .modal, .drawer, .kanban-board
Element           : [block]__[element]  → .card__title, .modal__footer, .chat__bubble
Modifier          : [block]--[state]    → .card--overdue, .badge--emerald, .btn--disabled
State classes     : is-[state]          → is-loading, is-active, is-open, is-error
JS hooks          : js-[name]           → js-submit-btn (never style these)

Color utility classes follow design token names:
.text-deep-blue | .bg-light-gray | .border-soft-gray | .text-muted-red

---

## 5. HTML NAMING

IDs               : kebab-case          → balance-card, submit-btn, file-input
Data attributes   : data-[name]         → data-invoice-id, data-tenant-id, data-ticket-status
ARIA labels       : Descriptive phrases → aria-label="Submit rent payment"
Form names        : match API field names exactly → name="first_name", name="monthly_rent"

---

## 6. DATABASE NAMING

Tables            : lowercase_plural    → users, properties, leases, invoices, maintenance_tickets
Columns           : lowercase_snake     → first_name, monthly_rent, created_at, deleted_at
Primary keys      : id (always)         → id INT PRIMARY KEY
Foreign keys      : [table_singular]_id → landlord_id, tenant_id, property_id, invoice_id
Boolean columns   : is_[state] or [verb]ed → is_verified, late_fee_applied, is_active
Timestamp columns : created_at, updated_at, deleted_at, [event]_at → paid_at, resolved_at
Status columns    : status              → status VARCHAR CHECK IN ('Active','Expired','Pending')
Indexes           : idx_[table]_[column] → idx_invoices_tenant_id, idx_leases_property_id
Constraints       : uq_[table]_[column] → uq_users_email, uq_invitations_token

---

## 7. API ENDPOINT NAMING

Pattern           : /api/v[n]/[domain]/[action if needed]
Resources         : nouns, plural        → /properties, /leases, /invoices
Methods communicate action:
  GET    /api/v1/properties             → list all landlord properties
  POST   /api/v1/properties             → create new property
  GET    /api/v1/properties/{id}        → get specific property
  PUT    /api/v1/properties/{id}        → update property
  DELETE /api/v1/properties/{id}        → delete property
  POST   /api/v1/leases/{id}/invite     → invite tenant to lease
  POST   /api/v1/payments/submit        → submit payment
  POST   /api/v1/payments/webhook       → receive gateway webhook

---

## 8. FILE UPLOAD NAMING

Uploaded files stored as: [uuid]_[original_filename_sanitized].[ext]
Example: 7f3a9c1d_lease_agreement_unit_4b.pdf
Purpose: prevents path traversal, filename collisions, and information leakage
Original filename stored in documents.original_filename for display
```

---

# FILE 12 — `tech_stack.md`

```md
# 🔧 tech_stack.md
# Rent & Lease Management System — Technology Stack
# Every technology choice, why it was chosen, and what it owns

---

## 1. FRONTEND

### HTML5
Role      : Structure layer — all 38 pages
Why       : Semantic markup for accessibility and SEO
Version   : HTML5 (semantic elements: article, section, nav, main, aside, header, footer)
Rules     : No inline styles. No inline JavaScript. Only structure and semantics.

### CSS3 (Vanilla)
Role      : Styling layer — design system, layouts, animations, responsive design
Why       : No framework overhead, full control over design system tokens,
            better performance, no dependency risk
Key CSS   : Custom Properties (design tokens), CSS Grid, Flexbox, CSS Animations,
            @keyframes, CSS Transitions, Media Queries, :focus-visible, :is(), :where()
Rules     : All values use design tokens from design.md. No arbitrary values.

### JavaScript (Vanilla ES6+)
Role      : Behavior layer — all user interaction, API communication, WebSocket client
Why       : No framework = no framework lock-in, maximum performance, full understanding
Key APIs  : fetch(), WebSocket, IntersectionObserver, FormData, DragEvent,
            localStorage (config only — never tokens), sessionStorage (never tokens),
            in-memory token storage via module-scoped variables
Rules     : No jQuery. No frameworks. Pure modern JavaScript.
            JWT token stored only in memory — never in localStorage or sessionStorage.

### Chart.js
Role      : Analytics charts (revenue line chart, donut charts)
Why       : Lightweight, well-documented, works with vanilla JS, no framework needed
Scope     : Analytics page only (Landlord Page 9)

---

## 2. BACKEND

### Python 3.11+
Role      : Middleware, API, Business Rules, Business Logic, Schedulers
Why       : Readable, large ecosystem, strong web framework support,
            excellent for data processing and scheduled jobs

### Flask (or FastAPI)
Role      : Web framework — HTTP routing, request/response handling, WebSocket support
Flask     : Simpler, more appropriate for learning context and scope of this project
FastAPI   : Higher performance, built-in async, automatic API documentation
Decision  : Flask for initial build (simpler), FastAPI upgrade path documented

### Flask-SocketIO (or FastAPI WebSockets)
Role      : WebSocket server for real-time chat and notifications
Scope     : Chat (Landlord Page 5, Tenant Page 5), Notifications

### APScheduler
Role      : Background job scheduler for all cron jobs
Scope     : Late fee job, lease expiry scanner, rent reminders, auto-pay processor
Why       : Lightweight, works within Flask process, database-backed job storage

### PyJWT
Role      : JWT token generation and verification
Scope     : Authentication Middleware, token issuance on login

### bcrypt
Role      : Password hashing
Scope     : Registration, password change, password verification on login

### Stripe Python SDK / Paystack API
Role      : Payment gateway integration
Scope     : Tenant payment processing, webhook verification

---

## 3. DATABASE

### PostgreSQL (Production) / SQLite (Development)
Role      : Persistent data store — all 9 data layer operations
PostgreSQL: ACID compliant, production-grade, handles concurrent writes correctly
SQLite    : Zero-configuration for local development and testing

### Connection Pooling
Tool      : psycopg2 with connection pooling (PostgreSQL)
Why       : Reuses database connections — avoids overhead of new connection per request

---

## 4. INFRASTRUCTURE

### SMTP (Email)
Role      : Sending verification emails, password reset, rent reminders, notifications
Provider  : SendGrid (production) / Local SMTP (development)
Scope     : All automated email events in the cron jobs and invitation flow

### File Storage
Development : Local file system (uploads/ directory outside web root)
Production  : S3-compatible object storage (AWS S3, Cloudflare R2, or similar)
Why         : Binary files do not belong in relational databases

### HTTPS / TLS
Provider    : Let's Encrypt (production)
Enforced    : All HTTP redirected to HTTPS
HSTS        : max-age=31536000; includeSubDomains; preload

---

## 5. DEVELOPMENT TOOLS

Git             : Version control (GitHub or GitLab)
.gitignore      : Excludes .env, __pycache__, uploads/, logs/, *.pyc
Postman         : API endpoint testing
Browser DevTools: Frontend debugging, performance profiling
Python venv     : Isolated dependency environment

---

## 6. TECHNOLOGY DECISION SUMMARY

| Technology | Version | Role | Layer |
|---|---|---|---|
| HTML5 | 5 | Page structure | Layer 1 |
| CSS3 | 3 | Visual design + animations | Layer 2 |
| JavaScript | ES2022 | User interaction + API calls | Layer 3 |
| Chart.js | 4.x | Analytics charts | Layer 3 |
| Python | 3.11+ | Backend engine | Layers 4–7 |
| Flask | 3.x | HTTP framework + routing | Layer 5 |
| Flask-SocketIO | 5.x | WebSocket server | Layer 5 |
| APScheduler | 3.x | Background cron jobs | Layer 7 |
| PyJWT | 2.x | JWT operations | Layer 4 |
| bcrypt | 4.x | Password hashing | Layer 7 |
| PostgreSQL | 15+ | Production database | Layers 8–9 |
| SQLite | 3.x | Development database | Layers 8–9 |
| psycopg2 | 2.x | PostgreSQL Python adapter | Layers 8–9 |
| Stripe/Paystack | Latest | Payment processing | Layer 7 |
| SendGrid/SMTP | Latest | Email delivery | Layer 7 |
| S3-compatible | Latest | File storage (production) | Layer 9 |
```

---

# FILE 13 — `database_schema.sql`

```sql
-- database_schema.sql
-- Rent & Lease Management System — Complete Database Schema
-- Every table, every column, every constraint, every index
-- Engine: PostgreSQL | Encoding: UTF-8 | All timestamps: UTC

-- ============================================================
-- USERS
-- ============================================================
CREATE TABLE users (
    id              SERIAL          PRIMARY KEY,
    email           VARCHAR(255)    NOT NULL UNIQUE,
    password_hash   VARCHAR(255)    NOT NULL,
    role            VARCHAR(20)     NOT NULL CHECK (role IN ('landlord', 'tenant')),
    first_name      VARCHAR(100)    NOT NULL,
    last_name       VARCHAR(100)    NOT NULL,
    phone_number    VARCHAR(30),
    is_verified     BOOLEAN         DEFAULT FALSE,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ     DEFAULT NULL
);

CREATE INDEX idx_users_email     ON users (email);
CREATE INDEX idx_users_role      ON users (role);
CREATE INDEX idx_users_deleted   ON users (deleted_at);

-- ============================================================
-- BUILDINGS (Parent groups for multi-unit properties)
-- ============================================================
CREATE TABLE buildings (
    id              SERIAL          PRIMARY KEY,
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    name            VARCHAR(255)    NOT NULL,
    address         TEXT            NOT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ     DEFAULT NULL
);

CREATE INDEX idx_buildings_landlord ON buildings (landlord_id);

-- ============================================================
-- PROPERTIES
-- ============================================================
CREATE TABLE properties (
    id              SERIAL          PRIMARY KEY,
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    building_id     INTEGER         REFERENCES buildings(id),
    unit_number     VARCHAR(50)     NOT NULL,
    address         TEXT            NOT NULL,
    base_rent       DECIMAL(10,2)   NOT NULL CHECK (base_rent > 0),
    status          VARCHAR(20)     DEFAULT 'Vacant' CHECK (status IN ('Vacant', 'Leased')),
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ     DEFAULT NULL
);

CREATE INDEX idx_properties_landlord ON properties (landlord_id);
CREATE INDEX idx_properties_status   ON properties (status);
CREATE INDEX idx_properties_building ON properties (building_id);

-- ============================================================
-- LEASES
-- ============================================================
CREATE TABLE leases (
    id              SERIAL          PRIMARY KEY,
    property_id     INTEGER         NOT NULL REFERENCES properties(id),
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    tenant_id       INTEGER         REFERENCES users(id),
    monthly_rent    DECIMAL(10,2)   NOT NULL CHECK (monthly_rent > 0),
    start_date      DATE            NOT NULL,
    end_date        DATE            NOT NULL,
    status          VARCHAR(20)     DEFAULT 'Pending' CHECK (status IN ('Pending','Active','Expired','Terminated')),
    signed_at       TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ     DEFAULT NULL,
    CONSTRAINT chk_lease_dates CHECK (end_date > start_date)
);

CREATE INDEX idx_leases_property  ON leases (property_id);
CREATE INDEX idx_leases_landlord  ON leases (landlord_id);
CREATE INDEX idx_leases_tenant    ON leases (tenant_id);
CREATE INDEX idx_leases_status    ON leases (status);
CREATE INDEX idx_leases_dates     ON leases (start_date, end_date);

-- ============================================================
-- INVITATIONS
-- ============================================================
CREATE TABLE invitations (
    id              SERIAL          PRIMARY KEY,
    lease_id        INTEGER         NOT NULL REFERENCES leases(id),
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    email           VARCHAR(255)    NOT NULL,
    token_hash      VARCHAR(255)    NOT NULL UNIQUE,
    expires_at      TIMESTAMPTZ     NOT NULL,
    accepted_at     TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_invitations_token   ON invitations (token_hash);
CREATE INDEX idx_invitations_lease   ON invitations (lease_id);

-- ============================================================
-- INVOICES
-- ============================================================
CREATE TABLE invoices (
    id                  SERIAL          PRIMARY KEY,
    lease_id            INTEGER         NOT NULL REFERENCES leases(id),
    tenant_id           INTEGER         NOT NULL REFERENCES users(id),
    property_id         INTEGER         NOT NULL REFERENCES properties(id),
    landlord_id         INTEGER         NOT NULL REFERENCES users(id),
    base_rent           DECIMAL(10,2)   NOT NULL,
    late_fee_amount     DECIMAL(10,2)   DEFAULT 0.00,
    total_amount        DECIMAL(10,2)   NOT NULL,
    due_date            DATE            NOT NULL,
    status              VARCHAR(20)     DEFAULT 'Outstanding' CHECK (status IN ('Outstanding','Paid','Cancelled')),
    late_fee_applied    BOOLEAN         DEFAULT FALSE,
    paid_at             TIMESTAMPTZ     DEFAULT NULL,
    created_at          TIMESTAMPTZ     DEFAULT NOW(),
    updated_at          TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_invoices_tenant    ON invoices (tenant_id);
CREATE INDEX idx_invoices_landlord  ON invoices (landlord_id);
CREATE INDEX idx_invoices_status    ON invoices (status);
CREATE INDEX idx_invoices_due_date  ON invoices (due_date);
CREATE INDEX idx_invoices_lease     ON invoices (lease_id);

-- ============================================================
-- TRANSACTIONS (Append-only — no updates or deletes)
-- ============================================================
CREATE TABLE transactions (
    id                  SERIAL          PRIMARY KEY,
    invoice_id          INTEGER         NOT NULL REFERENCES invoices(id),
    tenant_id           INTEGER         NOT NULL REFERENCES users(id),
    landlord_id         INTEGER         NOT NULL REFERENCES users(id),
    amount              DECIMAL(10,2)   NOT NULL,
    gateway_reference   VARCHAR(255)    NOT NULL UNIQUE,
    payment_method_last4 VARCHAR(4),
    idempotency_key     VARCHAR(255)    NOT NULL UNIQUE,
    created_at          TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_transactions_invoice   ON transactions (invoice_id);
CREATE INDEX idx_transactions_tenant    ON transactions (tenant_id);
CREATE INDEX idx_transactions_landlord  ON transactions (landlord_id);

-- ============================================================
-- EXPENSES
-- ============================================================
CREATE TABLE expenses (
    id              SERIAL          PRIMARY KEY,
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    property_id     INTEGER         NOT NULL REFERENCES properties(id),
    description     VARCHAR(500)    NOT NULL,
    amount          DECIMAL(10,2)   NOT NULL CHECK (amount > 0),
    expense_date    DATE            NOT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_expenses_property  ON expenses (property_id);
CREATE INDEX idx_expenses_landlord  ON expenses (landlord_id);

-- ============================================================
-- PAYMENT METHODS
-- ============================================================
CREATE TABLE payment_methods (
    id              SERIAL          PRIMARY KEY,
    tenant_id       INTEGER         NOT NULL REFERENCES users(id),
    gateway_token   VARCHAR(255)    NOT NULL,
    card_last_four  VARCHAR(4)      NOT NULL,
    card_brand      VARCHAR(50),
    is_default      BOOLEAN         DEFAULT FALSE,
    auto_pay_enabled BOOLEAN        DEFAULT FALSE,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ     DEFAULT NULL
);

CREATE INDEX idx_payment_methods_tenant ON payment_methods (tenant_id);

-- ============================================================
-- MAINTENANCE TICKETS
-- ============================================================
CREATE TABLE maintenance_tickets (
    id              SERIAL          PRIMARY KEY,
    lease_id        INTEGER         NOT NULL REFERENCES leases(id),
    tenant_id       INTEGER         NOT NULL REFERENCES users(id),
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    property_id     INTEGER         NOT NULL REFERENCES properties(id),
    category        VARCHAR(100)    NOT NULL,
    urgency         VARCHAR(20)     NOT NULL CHECK (urgency IN ('Emergency','High','Normal','Low')),
    description     TEXT            NOT NULL,
    status          VARCHAR(20)     DEFAULT 'Pending' CHECK (status IN ('Pending','In Progress','Resolved')),
    version         INTEGER         DEFAULT 1,
    resolved_at     TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_tickets_tenant   ON maintenance_tickets (tenant_id);
CREATE INDEX idx_tickets_landlord ON maintenance_tickets (landlord_id);
CREATE INDEX idx_tickets_status   ON maintenance_tickets (status);

-- ============================================================
-- TICKET COMMENTS
-- ============================================================
CREATE TABLE ticket_comments (
    id              SERIAL          PRIMARY KEY,
    ticket_id       INTEGER         NOT NULL REFERENCES maintenance_tickets(id),
    user_id         INTEGER         NOT NULL REFERENCES users(id),
    comment         TEXT            NOT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_comments_ticket ON ticket_comments (ticket_id);

-- ============================================================
-- INSPECTIONS
-- ============================================================
CREATE TABLE inspections (
    id              SERIAL          PRIMARY KEY,
    lease_id        INTEGER         NOT NULL REFERENCES leases(id),
    tenant_id       INTEGER         NOT NULL REFERENCES users(id),
    type            VARCHAR(20)     NOT NULL CHECK (type IN ('Move-In','Move-Out')),
    checklist_data  JSONB           NOT NULL,
    is_complete     BOOLEAN         DEFAULT FALSE,
    submitted_at    TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_inspections_lease  ON inspections (lease_id);
CREATE INDEX idx_inspections_tenant ON inspections (tenant_id);

-- ============================================================
-- CONVERSATIONS (Chat)
-- ============================================================
CREATE TABLE conversations (
    id              SERIAL          PRIMARY KEY,
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    tenant_id       INTEGER         NOT NULL REFERENCES users(id),
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    UNIQUE (landlord_id, tenant_id)
);

-- ============================================================
-- MESSAGES (Chat)
-- ============================================================
CREATE TABLE messages (
    id              SERIAL          PRIMARY KEY,
    conversation_id INTEGER         NOT NULL REFERENCES conversations(id),
    sender_id       INTEGER         NOT NULL REFERENCES users(id),
    content         TEXT,
    file_path       VARCHAR(500),
    is_read         BOOLEAN         DEFAULT FALSE,
    read_at         TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_messages_conversation ON messages (conversation_id);
CREATE INDEX idx_messages_sender       ON messages (sender_id);
CREATE INDEX idx_messages_created      ON messages (created_at);

-- ============================================================
-- NOTICES (Notice Board)
-- ============================================================
CREATE TABLE notices (
    id              SERIAL          PRIMARY KEY,
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    building_id     INTEGER         REFERENCES buildings(id),
    title           VARCHAR(255)    NOT NULL,
    content         TEXT            NOT NULL,
    is_urgent       BOOLEAN         DEFAULT FALSE,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ     DEFAULT NULL
);

CREATE INDEX idx_notices_landlord  ON notices (landlord_id);
CREATE INDEX idx_notices_building  ON notices (building_id);

-- ============================================================
-- DOCUMENTS
-- ============================================================
CREATE TABLE documents (
    id                  SERIAL          PRIMARY KEY,
    owner_id            INTEGER         NOT NULL REFERENCES users(id),
    property_id         INTEGER         REFERENCES properties(id),
    lease_id            INTEGER         REFERENCES leases(id),
    folder_name         VARCHAR(255),
    original_filename   VARCHAR(500)    NOT NULL,
    stored_filename     VARCHAR(500)    NOT NULL UNIQUE,
    file_path           VARCHAR(1000)   NOT NULL,
    file_type           VARCHAR(50),
    file_size_bytes     INTEGER,
    uploaded_at         TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at          TIMESTAMPTZ     DEFAULT NULL
);

CREATE INDEX idx_documents_owner    ON documents (owner_id);
CREATE INDEX idx_documents_property ON documents (property_id);
CREATE INDEX idx_documents_lease    ON documents (lease_id);

-- ============================================================
-- COMPLIANCE DOCUMENTS
-- ============================================================
CREATE TABLE compliance_documents (
    id              SERIAL          PRIMARY KEY,
    tenant_id       INTEGER         NOT NULL REFERENCES users(id),
    doc_type        VARCHAR(50)     NOT NULL CHECK (doc_type IN ('Government ID','Proof of Income','Renters Insurance')),
    document_id     INTEGER         REFERENCES documents(id),
    status          VARCHAR(20)     DEFAULT 'Pending' CHECK (status IN ('Pending','Verified','Rejected','Expired')),
    expiry_date     DATE            DEFAULT NULL,
    verified_at     TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_compliance_tenant ON compliance_documents (tenant_id);

-- ============================================================
-- NOTIFICATIONS
-- ============================================================
CREATE TABLE notifications (
    id              SERIAL          PRIMARY KEY,
    user_id         INTEGER         NOT NULL REFERENCES users(id),
    event_type      VARCHAR(50)     NOT NULL,
    title           VARCHAR(255)    NOT NULL,
    message         TEXT,
    is_read         BOOLEAN         DEFAULT FALSE,
    read_at         TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_notifications_user    ON notifications (user_id);
CREATE INDEX idx_notifications_read    ON notifications (is_read);
CREATE INDEX idx_notifications_created ON notifications (created_at);

-- ============================================================
-- AUDIT LOG (Append-only — immutable records)
-- ============================================================
CREATE TABLE audit_log (
    id              SERIAL          PRIMARY KEY,
    user_id         INTEGER         REFERENCES users(id),
    event_type      VARCHAR(100)    NOT NULL,
    resource_type   VARCHAR(100),
    resource_id     INTEGER,
    ip_address      VARCHAR(45),
    user_agent      TEXT,
    result          VARCHAR(20)     CHECK (result IN ('success','blocked','error')),
    metadata        JSONB,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_audit_user    ON audit_log (user_id);
CREATE INDEX idx_audit_event   ON audit_log (event_type);
CREATE INDEX idx_audit_created ON audit_log (created_at);

-- ============================================================
-- AUTOMATION SETTINGS
-- ============================================================
CREATE TABLE automation_settings (
    id              SERIAL          PRIMARY KEY,
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    automation_type VARCHAR(100)    NOT NULL,
    is_enabled      BOOLEAN         DEFAULT TRUE,
    updated_at      TIMESTAMPTZ     DEFAULT NOW(),
    UNIQUE (landlord_id, automation_type)
);

CREATE INDEX idx_automation_landlord ON automation_settings (landlord_id);
```

---

> ✅ **All 13 `.md` files are complete.**
> Every file is grounded in every conversation, every decision, every principle, every page specification, every architecture layer, every business rule, and every security measure discussed across this entire project.
> Copy each file into the `docs/` folder of your project structure and your system has its complete living documentation foundation.

# 🎯 The Main Purpose of the Rent & Lease Management System

---

## In One Sentence

> **To digitize, automate, and centralize the entire relationship between a Landlord and a Tenant — from the moment a lease is signed to the moment a tenant moves out — eliminating paper, manual work, and informal communication entirely.**

---

## The Core Problem It Solves

Right now, without this system, this is the reality:

**For Landlords:**
- Tracking rent payments in a notebook or spreadsheet
- Chasing tenants via WhatsApp for overdue rent
- No formal record of maintenance complaints
- No visibility into which properties are profitable
- Forgetting lease renewal dates until it is too late
- Manually calculating and communicating late fees

**For Tenants:**
- Not knowing exactly what they owe and when
- No formal way to report property damage with evidence
- No proof of property condition at move-in
- Lease documents lost or inaccessible
- No receipt or record of rent payments made

---

## What the App Actually Does

It replaces all of that chaos with **one unified platform** that handles:

| What | How |
|---|---|
| **Rent Collection** | Tenants pay online, amounts are locked and system-calculated, receipts generated automatically |
| **Lease Management** | Digital contracts, invitation system, overlap prevention, expiry warnings |
| **Maintenance** | Formal ticket system with photos, Kanban tracking, evidence trail |
| **Communication** | Real-time WhatsApp-style chat with a full message history |
| **Financial Visibility** | Revenue dashboards, expense tracking, ROI calculations, exportable reports |
| **Automation** | Late fees apply themselves, reminders send themselves, expiry warnings trigger themselves |
| **Legal Protection** | Move-in/move-out inspections locked after submission, document vault, audit trail |

---

## The Single Root Idea

> The app exists because **property management is a business** — and every business needs a system, not a collection of WhatsApp threads, notebooks, and spreadsheets.

It gives the **Landlord** a professional CRM to run their property portfolio like a business.

It gives the **Tenant** a clear, transparent, and fair experience where they always know exactly where they stand.

**Both sides win. That is the purpose.**
# 🔄 Complete Technology Stack Update
## From Flask + PostgreSQL → Django + MySQL
### Every Layer Updated | Every File Corrected | Every Decision Explained
#### Based on All Conversations in This Chat

---

## 🧠 WHY THIS CHANGE MATTERS DEEPLY

This is not a simple "swap one tool for another" update. Changing from Flask to Django and from PostgreSQL to MySQL changes **how the system thinks, how it is structured, how it communicates with the database, how middleware works, how security is implemented, and how every layer of the 9-layer architecture is built.**

Every `.md` file, every architectural decision, every database query pattern, every security mechanism must be understood through the lens of Django and MySQL specifically — not generically.

---

# 🔧 PART 1 — WHAT ACTUALLY CHANGES AND WHY

---

## CHANGE 1 — Flask → Django

### What Flask was:
Flask is a **micro-framework**. It gives you an HTTP router and almost nothing else. Every additional feature — authentication, middleware, ORM, CSRF protection, form handling, email sending — had to be chosen, installed, and configured separately. Maximum flexibility. Maximum responsibility.

### What Django is:
Django is a **batteries-included full-stack framework**. It arrives with a built-in ORM, built-in authentication system, built-in CSRF protection, built-in middleware system, built-in admin interface, built-in form validation, built-in email handling, built-in session management, and built-in security features. The philosophy is "convention over configuration" — Django has a defined, correct way to do most things, and following that way gives you enormous capability very quickly.

### What this means for the project:

**The ORM replaces raw SQL for most operations:**
In Flask with raw SQL, every database query was written by hand as a SQL string. In Django, the ORM translates Python code into SQL automatically. Instead of writing `SELECT * FROM properties WHERE landlord_id = ?`, you write `Property.objects.filter(landlord_id=user.id)`. Django generates the correct, parameterized SQL. SQL injection prevention is built into the ORM by default.

**Django's middleware system replaces custom middleware:**
In Flask, every middleware function was written from scratch. In Django, the middleware system is built in. Django provides `AuthenticationMiddleware`, `SessionMiddleware`, `SecurityMiddleware`, `CsrfViewMiddleware`, and `CommonMiddleware` out of the box. Custom middleware — rate limiting, IDOR prevention, request logging — is written as Django middleware classes that slot into the existing pipeline.

**Django's authentication replaces JWT from scratch:**
Django has a complete authentication system built in — user models, password hashing with PBKDF2 by default (bcrypt as an alternative), login, logout, and session management. For the API-based authentication needed for this project, `djangorestframework-simplejwt` provides JWT authentication that integrates cleanly with Django's existing auth system.

**Django REST Framework replaces manual API route building:**
The API layer is built using Django REST Framework (DRF). DRF provides serializers for data validation and transformation, viewsets for CRUD operations, routers for URL generation, and permission classes for authorization. The entire API layer is more structured, more consistent, and less error-prone than Flask route handlers.

---

## CHANGE 2 — PostgreSQL → MySQL

### What PostgreSQL was:
PostgreSQL is an advanced object-relational database with rich JSON support, sophisticated full-text search, window functions, and the most complete ACID implementation available in open-source databases.

### What MySQL is:
MySQL is the world's most widely deployed open-source relational database. It is fast, well-documented, widely hosted, and deeply familiar to most web developers. It fully supports ACID transactions when using the InnoDB storage engine — which is the default. It is the standard database for LAMP stack applications, which aligns perfectly with this project's deployment context.

### What this means for the project:

**InnoDB engine is mandatory:**
MySQL has multiple storage engines. Only InnoDB supports ACID transactions, foreign key constraints, and row-level locking. Every table in the system must use the InnoDB engine. This must be explicitly specified or configured as the default — `default-storage-engine = InnoDB` in MySQL configuration.

**Django's ORM handles MySQL differences transparently:**
Most of the differences between PostgreSQL and MySQL syntax are handled by Django's ORM automatically. The same Python model code generates different SQL for PostgreSQL and MySQL as needed. The developer writes Python — Django writes the correct SQL for whichever database is configured.

**MySQL-specific considerations:**
MySQL's default character set must be set to `utf8mb4` — not the older `utf8` which only supports 3-byte characters. `utf8mb4` supports the full Unicode range including emoji. This matters when Tenants send maintenance descriptions, chat messages, or inspection notes using characters outside basic ASCII.

MySQL's `DATETIME` type does not store timezone information. All timestamps must be managed at the application level as UTC. Django handles this correctly when `USE_TZ = True` is set in settings — Django stores and retrieves all datetimes in UTC and converts to the user's timezone at display time.

---

# 🏗️ PART 2 — THE UPDATED 9-LAYER ARCHITECTURE WITH DJANGO + MYSQL

---

## LAYER 1 — STRUCTURE (HTML)
**No change.** HTML is HTML. Django's template engine renders HTML. The 38 pages retain their exact structure.

The one addition: Django templates use `{% %}` template tags and `{{ }}` variable interpolation. The base templates extend Django's template inheritance system. `layout_landlord.html` becomes the base template that landlord pages extend using `{% extends "landlord/base.html" %}` and `{% block content %}`.

---

## LAYER 2 — STYLING (CSS)
**No change.** CSS is CSS. Django serves static files. The design system from `design.md` applies without modification.

The one addition: Django's `{% static %}` template tag generates correct URLs for static files. `<link rel="stylesheet" href="{% static 'css/design_system.css' %}">` replaces hardcoded paths. Django's `collectstatic` command gathers all static files for production serving.

---

## LAYER 3 — BEHAVIOR (JavaScript)
**No change in principle.** JavaScript behavior remains the same — fetch calls, WebSocket connections, DOM manipulation, form handling.

The one critical Django-specific addition: Django's CSRF protection requires the CSRF token to be included in every AJAX POST, PUT, PATCH, and DELETE request. Django provides the CSRF token in a cookie named `csrftoken`. JavaScript must read this cookie and include the value in every state-changing request header as `X-CSRFToken`. This is a non-negotiable Django security requirement.

---

## LAYER 4 — MIDDLEWARE (Django Middleware System)

### How Django Middleware Works:
Django middleware is defined as an ordered list in `settings.py` under `MIDDLEWARE`. Every request passes through this list top-to-bottom. Every response passes back through bottom-to-top. The order is the logic — exactly as established in every previous conversation.

### The Django Middleware Stack for This Project:

```
MIDDLEWARE = [
    # 1. Security Headers (built-in Django)
    'django.middleware.security.SecurityMiddleware',

    # 2. Session Management (built-in Django)
    'django.contrib.sessions.middleware.SessionMiddleware',

    # 3. CORS (django-cors-headers package)
    'corsheaders.middleware.CorsMiddleware',

    # 4. Common Middleware (URL normalization, built-in)
    'django.middleware.common.CommonMiddleware',

    # 5. CSRF Protection (built-in Django)
    'django.middleware.csrf.CsrfViewMiddleware',

    # 6. Authentication (built-in Django)
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # 7. Request Logging (custom middleware)
    'middleware.logging_middleware.RequestLoggingMiddleware',

    # 8. Rate Limiting (custom middleware)
    'middleware.rate_limit_middleware.RateLimitMiddleware',

    # 9. IDOR Authorization (custom middleware)
    'middleware.authorization_middleware.IDORAuthorizationMiddleware',

    # 10. Messages (built-in Django)
    'django.contrib.messages.middleware.MessageMiddleware',

    # 11. X-Frame-Options (built-in Django)
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### What Django's Built-in Middleware Provides for Free:
**SecurityMiddleware** sets `Strict-Transport-Security`, `X-Content-Type-Options`, redirects HTTP to HTTPS, sets referrer policy — all automatically when `SECURE_*` settings are configured.

**CsrfViewMiddleware** automatically verifies CSRF tokens on every POST/PUT/PATCH/DELETE request — the system does not need to write this check in every view.

**AuthenticationMiddleware** attaches the authenticated user to every request as `request.user`. Every view receives the authenticated user automatically.

**XFrameOptionsMiddleware** sets `X-Frame-Options: DENY` on every response automatically.

---

## LAYER 5 — API (Django REST Framework)

### How DRF Structures the API Layer:

**Serializers replace manual input validation:**
A Django REST Framework serializer defines the exact shape of data that an endpoint accepts and returns. It validates types, required fields, length limits, and custom validation rules. Invalid data is rejected with a structured 422-equivalent response before it reaches business logic. The serializer is the API boundary validator.

**ViewSets replace individual route handlers:**
A DRF ViewSet groups all CRUD operations for a resource into one class. The `PropertyViewSet` handles list, create, retrieve, update, and destroy for properties. The URL router automatically generates all the correct URL patterns from the ViewSet. This enforces the consistent URL naming convention documented in `naming_patterns.md`.

**Permission Classes replace manual authorization checks:**
DRF permission classes define who can access what. `IsAuthenticated` requires a valid JWT. `IsLandlord` is a custom permission that checks `request.user.role == 'landlord'`. `IsOwner` is a custom permission that checks the resource belongs to the requesting user. These permission classes are the DRF implementation of the authorization layer, complementing the IDOR middleware.

**JWT Integration:**
`djangorestframework-simplejwt` provides the JWT login endpoint, token refresh endpoint, and token verification. It integrates with Django's existing user model. JWT authentication is configured as the default authentication class in DRF settings.

---

## LAYERS 6 & 7 — BUSINESS RULES AND BUSINESS LOGIC

**No structural change.** Business rules and business logic remain Python functions in their dedicated modules. The only difference is that they now interact with the database through Django's ORM rather than raw SQL queries. The ORM is faster to write, safer against injection, and more maintainable — but the single responsibility and separation principles remain identical to every previous conversation.

---

## LAYERS 8 & 9 — DATA RETRIEVAL AND DATA STORAGE (Django ORM + MySQL)

### How the Django ORM Works:

Django's ORM translates Python model queries into MySQL SQL automatically. The developer never writes raw SQL for standard operations. The ORM generates parameterized queries — SQL injection is prevented by the framework's core mechanism, not by developer discipline alone.

**Data Retrieval with Django ORM:**
`Property.objects.filter(landlord=request.user).select_related('building').prefetch_related('leases')` — this single line generates an optimized JOIN query that retrieves properties with their building and lease data in two queries total (not N+1). The `select_related` and `prefetch_related` methods are the Django ORM solution to the N+1 query problem discussed in every previous conversation.

**Data Storage with Django ORM:**
`invoice.status = 'Paid'` followed by `invoice.save()` generates an `UPDATE` statement with only the changed fields. `Invoice.objects.create(...)` generates a parameterized `INSERT`. Django's `transaction.atomic()` context manager wraps multiple ORM operations in a single MySQL transaction — implementing the ACID atomicity principle discussed throughout this project.

**Raw SQL When Needed:**
For complex analytics queries — the 12-month revenue aggregation, the maintenance category breakdown — Django allows raw SQL via `Invoice.objects.raw(...)` or `connection.cursor()`. These raw queries still use parameterized values — `%s` placeholders — maintaining SQL injection prevention even for hand-written queries.

---

# 📁 PART 3 — UPDATED PROJECT FILE STRUCTURE

```
rent-lease-management/
│
├── manage.py                           # Django management command entry point
├── requirements.txt                    # All Python dependencies
├── .env                                # Environment variables (never committed)
├── .env.example                        # Template for required variables
├── .gitignore                          # Excludes .env, __pycache__, media/, staticfiles/
│
├── docs/                               # All .md documentation files
│   ├── AI_rules.md
│   ├── plan.md
│   ├── prd.md
│   ├── architecture.md
│   ├── design.md
│   ├── system_design.md
│   ├── security.md
│   ├── risk_management.md
│   ├── implementation_plan.md
│   ├── file_structure.md
│   ├── naming_patterns.md
│   └── tech_stack.md
│
├── config/                             # Django project configuration
│   ├── __init__.py
│   ├── settings/
│   │   ├── base.py                     # Shared settings for all environments
│   │   ├── development.py              # Development-specific settings
│   │   └── production.py              # Production-specific settings
│   ├── urls.py                         # Root URL configuration
│   ├── wsgi.py                         # WSGI entry point
│   └── asgi.py                         # ASGI entry point (for WebSockets)
│
├── apps/                               # All Django applications
│   │
│   ├── users/                          # User management app
│   │   ├── models.py                   # CustomUser model
│   │   ├── serializers.py              # DRF serializers
│   │   ├── views.py                    # DRF viewsets
│   │   ├── urls.py                     # URL patterns
│   │   ├── permissions.py              # Custom DRF permission classes
│   │   ├── business_rules.py           # User constraint enforcement
│   │   ├── business_logic.py           # User process orchestration
│   │   └── migrations/                 # Django database migrations
│   │
│   ├── properties/                     # Property management app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── business_rules.py
│   │   ├── business_logic.py
│   │   └── migrations/
│   │
│   ├── leases/                         # Lease management app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── business_rules.py
│   │   ├── business_logic.py
│   │   └── migrations/
│   │
│   ├── financials/                     # Financial management app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── business_rules.py
│   │   ├── business_logic.py
│   │   └── migrations/
│   │
│   ├── maintenance/                    # Maintenance helpdesk app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── business_rules.py
│   │   ├── business_logic.py
│   │   └── migrations/
│   │
│   ├── chat/                           # Real-time chat app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── consumers.py                # Django Channels WebSocket consumers
│   │   ├── routing.py                  # WebSocket URL routing
│   │   ├── business_logic.py
│   │   └── migrations/
│   │
│   ├── documents/                      # Document vault app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── business_rules.py
│   │   ├── business_logic.py
│   │   └── migrations/
│   │
│   ├── analytics/                      # Analytics and reporting app
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── queries.py                  # Complex analytics SQL queries
│   │   └── business_logic.py
│   │
│   ├── notifications/                  # Notification system app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── migrations/
│   │
│   └── automation/                     # Cron jobs and scheduling app
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── tasks.py                    # Celery task definitions
│       └── migrations/
│
├── middleware/                         # Custom Django middleware
│   ├── __init__.py
│   ├── logging_middleware.py           # Request logging
│   ├── rate_limit_middleware.py        # Rate limiting
│   └── authorization_middleware.py     # IDOR prevention
│
├── frontend/                           # All HTML, CSS, JavaScript
│   ├── templates/
│   │   ├── base/
│   │   │   ├── layout_landlord.html
│   │   │   ├── layout_tenant.html
│   │   │   └── layout_auth.html
│   │   ├── landlord/
│   │   │   └── [14 landlord page templates]
│   │   ├── tenant/
│   │   │   └── [11 tenant page templates]
│   │   └── public/
│   │       └── [13 external page templates]
│   └── static/
│       ├── css/
│       └── js/
│
├── scheduler/                          # Background job scheduling
│   ├── __init__.py
│   ├── celery.py                       # Celery configuration
│   ├── late_fee_task.py
│   ├── lease_expiry_task.py
│   ├── rent_reminder_task.py
│   └── auto_pay_task.py
│
├── media/                              # User-uploaded files (outside web root in production)
│   ├── documents/
│   ├── maintenance_photos/
│   └── compliance_docs/
│
├── staticfiles/                        # Collected static files (production)
│
└── logs/
    ├── app.log
    ├── audit.log
    └── celery.log
```

---

# 📋 PART 4 — UPDATED tech_stack.md

```md
# 🔧 tech_stack.md
# Rent & Lease Management System — Technology Stack
# Updated: Django + MySQL | Every technology, every choice, every reason

---

## 1. FRONTEND

### HTML5
Role      : Structure layer — all 38 pages
Rendered by: Django template engine
Template tags: {% %} for logic, {{ }} for variables, {% static %} for assets
Inheritance: {% extends %} and {% block %} for base layout reuse
Rules     : No inline styles. No inline JavaScript. Semantic HTML5 only.

### CSS3 (Vanilla)
Role      : Styling layer — complete design system
Served by : Django static files system (development) / CDN (production)
Loaded via: {% load static %} and {% static 'css/file.css' %} template tags
Rules     : All values reference design tokens. 4px spacing base. No arbitrary values.

### JavaScript (Vanilla ES6+)
Role      : Behavior layer — interaction, API communication, WebSocket client
Critical Django addition:
  Every AJAX POST/PUT/PATCH/DELETE must include the CSRF token:
  Header: X-CSRFToken: [value from csrftoken cookie]
  Django's CsrfViewMiddleware rejects requests missing this header.
JWT storage: Memory only — never localStorage (XSS risk)
Rules     : No frameworks. Pure modern JavaScript.

### Chart.js (4.x)
Role      : Analytics charts
Scope     : Landlord Analytics page only

---

## 2. BACKEND

### Python 3.11+
Role      : All server-side logic

### Django 4.2+ (LTS)
Role      : Complete web framework — URL routing, ORM, middleware,
            authentication, CSRF, template engine, static files,
            form validation, email, sessions
Why Django: Batteries-included. Built-in security. Mature ORM. Large community.
            LTS version means security support until April 2026+.
            Correct choice for a full-featured production system.

Key Django configurations:
  DEBUG = False (production — never True in production)
  ALLOWED_HOSTS = [production domain]
  USE_TZ = True (all datetimes stored in UTC)
  DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
  AUTH_USER_MODEL = 'users.CustomUser' (custom user model)
  PASSWORD_HASHERS = bcrypt as first hasher

### Django REST Framework (DRF) 3.14+
Role      : API layer — serializers, viewsets, routers, permissions
Why DRF   : Industry standard for Django APIs. Integrates with Django auth.
            Provides consistent patterns for all 9 resource domains.

Key DRF configurations:
  DEFAULT_AUTHENTICATION_CLASSES: JWTAuthentication
  DEFAULT_PERMISSION_CLASSES: IsAuthenticated
  DEFAULT_PAGINATION_CLASS: PageNumberPagination
  PAGE_SIZE: 20

### djangorestframework-simplejwt
Role      : JWT authentication integrated with Django's auth system
Provides  : /api/token/ (login → returns access + refresh tokens)
            /api/token/refresh/ (refresh access token)
            /api/token/verify/ (verify token validity)
Token storage: access token in memory, refresh token in httpOnly cookie

### Django Channels 4.x
Role      : WebSocket support for real-time chat and notifications
Why       : Django by default is WSGI (HTTP only). Django Channels adds
            ASGI support enabling persistent WebSocket connections.
Requires  : Redis as the channel layer backend
ASGI server: Daphne or Uvicorn

### Channels Redis
Role      : Channel layer backend for Django Channels
Why       : Multiple WebSocket server instances need a shared message broker.
            Redis is the standard, battle-tested choice.

### Celery 5.x
Role      : Background task queue for all cron jobs
Why       : Django does not have a built-in task scheduler for production.
            Celery is the industry standard for Python background tasks.
Broker    : Redis (same Redis instance as Channels, different database)
Beat      : celery-beat for scheduled (cron-style) task execution
Tasks     : Late fee application, lease expiry scan, rent reminders, auto-pay

### django-cors-headers
Role      : CORS middleware for cross-origin requests
Why       : Required when frontend and backend are on different domains.
            Integrates cleanly as Django middleware.

### Pillow
Role      : Image processing for maintenance photos and compliance documents
Why       : Validates and optionally resizes uploaded images.

---

## 3. DATABASE

### MySQL 8.0+
Role      : Primary persistent data store
Engine    : InnoDB (mandatory — the only engine supporting ACID and foreign keys)
Encoding  : utf8mb4 with utf8mb4_unicode_ci collation
            (supports full Unicode including emoji — critical for chat messages)
Timezone  : All datetimes stored as UTC via Django's USE_TZ = True

Django connection:
  DATABASE = {
    'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': env('DB_NAME'),
      'USER': env('DB_USER'),
      'PASSWORD': env('DB_PASSWORD'),
      'HOST': env('DB_HOST'),
      'PORT': '3306',
      'OPTIONS': {
        'charset': 'utf8mb4',
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
      }
    }
  }

STRICT_TRANS_TABLES: Critical setting. Without it, MySQL silently truncates
data that exceeds column length limits. With it, MySQL raises an error.
Always use STRICT_TRANS_TABLES in production.

### mysqlclient
Role      : Python MySQL adapter (recommended by Django docs)
Alternative: PyMySQL (pure Python, no C dependencies — easier to install)

### Redis 7.x
Role      : Channel layer (WebSockets) + Task broker (Celery) + Cache
Why Redis : In-memory, extremely fast, standard for both use cases.

---

## 4. DJANGO MODELS → MYSQL TABLES

Django models define the database schema in Python.
Django migrations translate model changes into MySQL ALTER/CREATE TABLE statements.
Direct SQL schema files are replaced by Django migrations.

Model → MySQL mapping:
  CharField(max_length=255)    → VARCHAR(255)
  TextField()                  → LONGTEXT
  IntegerField()               → INT
  DecimalField(max_digits, dp) → DECIMAL(max_digits, decimal_places)
  BooleanField()               → TINYINT(1)
  DateField()                  → DATE
  DateTimeField()              → DATETIME(6) with UTC storage
  ForeignKey()                 → INT with FOREIGN KEY constraint (InnoDB)
  EmailField()                 → VARCHAR(254) with email validation

---

## 5. INFRASTRUCTURE

### Redis (as described above)
Two databases within Redis:
  DB 0: Django Channels channel layer
  DB 1: Celery task broker and result backend

### SMTP / Email
Django's email backend configured via settings:
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
  All values from environment variables

### Media Files (User Uploads)
Development: MEDIA_ROOT = '/media/' served by Django
Production : MEDIA_ROOT on cloud storage (S3-compatible)
             django-storages library abstracts the storage backend
             Business logic calls the same interface regardless of backend

### Static Files
Development: Django serves static files via runserver
Production : django collectstatic gathers all static files
             Served by Nginx or CDN

### HTTPS
Django settings for production:
  SECURE_SSL_REDIRECT = True
  SECURE_HSTS_SECONDS = 31536000
  SECURE_HSTS_INCLUDE_SUBDOMAINS = True
  SECURE_HSTS_PRELOAD = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SECURE = True

---

## 6. COMPLETE TECHNOLOGY STACK TABLE

| Technology              | Version  | Role                          | Layer    |
|-------------------------|----------|-------------------------------|----------|
| HTML5                   | 5        | Page structure                | 1        |
| CSS3                    | 3        | Visual design + animations    | 2        |
| JavaScript              | ES2022   | Interaction + API calls       | 3        |
| Chart.js                | 4.x      | Analytics charts              | 3        |
| Python                  | 3.11+    | Backend engine                | 4–7      |
| Django                  | 4.2 LTS  | Full web framework            | 4–7      |
| Django REST Framework   | 3.14+    | API layer                     | 5        |
| simplejwt               | 5.x      | JWT authentication            | 4        |
| Django Channels         | 4.x      | WebSocket (ASGI)              | 5        |
| Celery                  | 5.x      | Background tasks / cron       | 7        |
| celery-beat             | 2.x      | Scheduled task execution      | 7        |
| django-cors-headers     | 4.x      | CORS middleware               | 4        |
| mysqlclient             | 2.x      | MySQL Python adapter          | 8–9      |
| MySQL                   | 8.0+     | Primary database (InnoDB)     | 8–9      |
| Redis                   | 7.x      | Channels + Celery broker      | 5, 7     |
| django-storages         | 1.14+    | Abstracted file storage       | 9        |
| Pillow                  | 10.x     | Image processing              | 9        |
| python-decouple         | 3.x      | Environment variable loading  | Config   |
| Daphne / Uvicorn        | Latest   | ASGI server for production    | Infra    |
| Nginx                   | Latest   | Reverse proxy + static files  | Infra    |
```

---

# 📋 PART 5 — UPDATED architecture.md (Django-Specific Sections)

```md
# 🏗️ architecture.md — Django + MySQL Update
# Key architectural changes from the Django and MySQL technology choices

---

## DJANGO URL ROUTING

Root URL configuration in config/urls.py:
  /api/v1/auth/         → users.urls (authentication endpoints)
  /api/v1/properties/   → properties.urls (property management)
  /api/v1/leases/       → leases.urls (lease management)
  /api/v1/financials/   → financials.urls (billing and payments)
  /api/v1/maintenance/  → maintenance.urls (helpdesk)
  /api/v1/chat/         → chat.urls (REST chat history)
  /api/v1/documents/    → documents.urls (document vault)
  /api/v1/analytics/    → analytics.urls (reporting)
  /api/v1/notifications/→ notifications.urls (notification feed)
  /api/v1/automation/   → automation.urls (cron toggle panel)
  /ws/chat/             → chat.routing (WebSocket routing via Channels)
  /ws/notifications/    → notifications.routing (WebSocket push)
  /                     → frontend HTML views (template rendering)

---

## DJANGO CUSTOM USER MODEL

The system uses a custom user model extending AbstractBaseUser.
This is a Django requirement that must be set BEFORE any migrations are run.
AUTH_USER_MODEL = 'users.CustomUser'

CustomUser fields:
  email           : EmailField(unique=True) — login identifier
  role            : CharField(choices=['landlord','tenant'])
  first_name      : CharField
  last_name       : CharField
  phone_number    : CharField
  is_verified     : BooleanField(default=False)
  is_active       : BooleanField(default=True)
  created_at      : DateTimeField(auto_now_add=True)
  updated_at      : DateTimeField(auto_now=True)
  deleted_at      : DateTimeField(null=True, blank=True)

USERNAME_FIELD = 'email' (login with email not username)
REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

---

## DJANGO MIGRATIONS (Replaces database_schema.sql)

All database schema is managed through Django migrations.
Schema changes are never applied directly to MySQL.
The migration workflow:
  1. Modify the model in models.py
  2. Run: python manage.py makemigrations [app_name]
  3. Django generates a migration file describing the change
  4. Run: python manage.py migrate
  5. Django applies the migration to MySQL

Every migration file is committed to version control.
The current database state is always reproducible by running all migrations.
Rolling back a migration: python manage.py migrate [app_name] [previous_migration]

---

## DJANGO ORM PATTERNS FOR THIS PROJECT

### N+1 Prevention (Critical)
Wrong (N+1):
  properties = Property.objects.filter(landlord=user)
  for property in properties:
      lease = property.lease_set.filter(status='Active').first()
      # This fires one query per property — N+1

Correct (2 queries total):
  properties = Property.objects.filter(
      landlord=user
  ).prefetch_related(
      Prefetch('lease_set',
               queryset=Lease.objects.filter(status='Active'),
               to_attr='active_leases')
  )

### ACID Transactions
from django.db import transaction

with transaction.atomic():
    invoice.status = 'Paid'
    invoice.paid_at = timezone.now()
    invoice.save()

    Transaction.objects.create(
        invoice=invoice,
        amount=invoice.total_amount,
        gateway_reference=gateway_ref
    )

    Notification.objects.create(
        user=invoice.tenant,
        message='Payment confirmed'
    )
# If any operation raises an exception, ALL are rolled back

### Soft Deletes via Django Manager
class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class Property(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)
    objects = SoftDeleteManager()  # default manager excludes deleted
    all_objects = models.Manager() # access all including deleted

### IDOR-Safe Queries (ownership scoping)
# Always scope to the authenticated user
Invoice.objects.filter(
    id=invoice_id,
    tenant=request.user  # IDOR protection at query level
).get()
# If the invoice belongs to another tenant, this raises DoesNotExist
# The view returns 404 — which reveals no information about
# whether the invoice exists at all

---

## DJANGO CHANNELS (WebSocket Architecture)

Django Channels replaces standard Django WSGI with ASGI.
ASGI handles both HTTP (standard requests) and WebSocket connections.

Channel Layer: Redis
  All WebSocket messages are routed through Redis.
  This allows multiple Daphne workers to share WebSocket state.
  A message sent to Landlord from Tenant arrives at any worker
  and is delivered to the correct WebSocket connection.

WebSocket Consumer (chat/consumers.py):
  Handles: connect, disconnect, receive, send
  Authentication: JWT token passed in WebSocket URL query parameter
  on connect, verified before the connection is accepted
  Group naming: chat_[conversation_id]
  Every landlord-tenant pair has a unique group
  Messages sent to the group are delivered to all connected members

WebSocket Consumer (notifications/consumers.py):
  Group naming: notifications_[user_id]
  Server-side events call async_to_sync(channel_layer.group_send)
  to push notifications to the connected user's WebSocket

---

## CELERY (Replaces APScheduler)

Celery runs as a separate process from the Django application.
Celery Beat runs as another separate process managing schedules.

Django settings integration:
  CELERY_BROKER_URL = 'redis://localhost:6379/1'
  CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
  CELERY_TIMEZONE = 'UTC'
  CELERY_BEAT_SCHEDULE defines the cron schedules

Tasks call Django ORM operations directly —
they run in a Django application context with full model access.

Automation toggle integration:
  Each task checks AutomationSetting.objects.get(
      landlord=landlord,
      automation_type='late_fee'
  ).is_enabled
  before executing its main logic.

---

## MYSQL-SPECIFIC SETTINGS

settings/base.py critical MySQL configurations:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'connect_timeout': 10,
        },
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        }
    }
}

MySQL server configuration (my.cnf):
  [mysqld]
  character-set-server = utf8mb4
  collation-server = utf8mb4_unicode_ci
  default-storage-engine = InnoDB
  innodb_strict_mode = 1
  sql_mode = STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO

These MySQL server settings ensure:
  utf8mb4: Full Unicode support
  InnoDB: ACID transactions and foreign keys on all tables
  STRICT mode: Data integrity — no silent truncation or coercion
```

---

# 📋 PART 6 — UPDATED security.md (Django-Specific Security)

```md
# 🔒 security.md — Django + MySQL Security Update

---

## DJANGO SECURITY SETTINGS (settings/production.py)

# HTTPS enforcement
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# HSTS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Cookie security
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = False  # Must be False — JS reads this cookie for AJAX
CSRF_COOKIE_SAMESITE = 'Lax'

# Security headers (SecurityMiddleware handles these)
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
     'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Password hashing — bcrypt as primary hasher
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]

---

## DJANGO CSRF PROTECTION

Django's CsrfViewMiddleware is always in the middleware stack.
All state-changing requests (POST/PUT/PATCH/DELETE) must include:
  Header: X-CSRFToken: [cookie value]

JavaScript pattern to read and send CSRF token:
  function getCsrfToken() {
      return document.cookie
          .split(';')
          .find(c => c.trim().startsWith('csrftoken='))
          ?.split('=')[1];
  }

  fetch('/api/v1/payments/submit', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`,
          'X-CSRFToken': getCsrfToken()
      },
      body: JSON.stringify(data)
  });

DRF JWT endpoints are CSRF-exempt (JWT provides equivalent protection).
Django template-rendered HTML form endpoints require CSRF tokens.
All AJAX endpoints require both JWT and CSRF.

---

## DJANGO ORM SQL INJECTION PREVENTION

Django's ORM uses parameterized queries by default.
The ORM never concatenates user input into SQL strings.
SQL injection through normal ORM usage is categorically prevented.

Raw SQL — when used — must still use parameters:
  # Safe
  Invoice.objects.raw(
      'SELECT * FROM financials_invoice WHERE tenant_id = %s',
      [tenant_id]
  )

  # NEVER DO THIS
  Invoice.objects.raw(
      f'SELECT * FROM financials_invoice WHERE tenant_id = {tenant_id}'
  )

---

## DJANGO PERMISSIONS AND IDOR

DRF permission classes (apps/users/permissions.py):
  IsLandlord: request.user.role == 'landlord'
  IsTenant: request.user.role == 'tenant'
  IsOwnerOrLandlord: request.user == obj.tenant or request.user == obj.landlord
  IsResourceOwner: request.user == obj.owner

Every ViewSet declares its permission_classes:
  class InvoiceViewSet(viewsets.ModelViewSet):
      permission_classes = [IsAuthenticated, IsTenant]

      def get_queryset(self):
          # IDOR prevention at query level
          return Invoice.objects.filter(tenant=self.request.user)

The get_queryset override is the most important IDOR protection in Django.
It scopes every query to the authenticated user automatically.
No invoice ID that belongs to another tenant will ever be returned —
regardless of what ID is in the URL.

---

## DJANGO RATE LIMITING

Custom Django middleware in middleware/rate_limit_middleware.py.
Uses Django's cache framework (Redis backend) to track request counts.
Cache key: f"rate_limit:{request.user.id}:{request.path}"
Increments on every request, checks against endpoint-specific limits.

Additionally: django-ratelimit package for per-view rate limiting.
Applied as decorators on sensitive ViewSet methods:
  @method_decorator(ratelimit(key='user', rate='3/5m', method='POST'))
  def create(self, request):  # payment submission
      ...

---

## MYSQL SECURITY

MySQL user for the application has minimum required permissions:
  GRANT SELECT, INSERT, UPDATE, DELETE ON rentlease.* TO 'app_user'@'localhost';
  -- NO DROP, NO CREATE, NO ALTER, NO GRANT
  -- Schema changes only via Django migrations run by admin user

MySQL connection from Django:
  Password stored in environment variable only
  Never in settings.py directly
  Loaded via python-decouple: env('DB_PASSWORD')

MySQL data-at-rest encryption:
  InnoDB tablespace encryption enabled for sensitive tables
  (users, invoices, transactions, messages, compliance_documents)
```

---

# 📋 PART 7 — UPDATED requirements.txt

```txt
# requirements.txt
# Rent & Lease Management System — Complete Python Dependencies
# Install: pip install -r requirements.txt

# ── Core Framework ──────────────────────────────────────────
Django==4.2.11                      # Core web framework (LTS)
djangorestframework==3.14.0         # REST API framework
djangorestframework-simplejwt==5.3.1 # JWT authentication for DRF

# ── Real-Time (WebSockets) ──────────────────────────────────
channels==4.0.0                     # Django ASGI + WebSocket support
channels-redis==4.1.0               # Redis channel layer for Channels
daphne==4.0.0                       # ASGI server for production

# ── Background Tasks ────────────────────────────────────────
celery==5.3.6                       # Background task queue
django-celery-beat==2.5.0           # Scheduled task management
django-celery-results==2.5.1        # Task result storage
redis==5.0.1                        # Redis Python client (broker + cache)

# ── Database ────────────────────────────────────────────────
mysqlclient==2.2.0                  # MySQL adapter (Django recommended)
# Alternative if mysqlclient fails to install:
# PyMySQL==1.1.0

# ── Security ────────────────────────────────────────────────
django-cors-headers==4.3.1          # CORS headers middleware
bcrypt==4.1.2                       # bcrypt password hasher
cryptography==42.0.0                # AES encryption for chat messages
django-ratelimit==4.1.0             # Per-view rate limiting decorator

# ── File Handling ────────────────────────────────────────────
Pillow==10.2.0                      # Image validation and processing
django-storages==1.14.2             # Abstracted file storage backends
boto3==1.34.0                       # S3-compatible storage (production)

# ── Email ───────────────────────────────────────────────────
# Django has built-in SMTP email — no extra package needed
# For SendGrid:
# sendgrid==6.11.0

# ── Configuration ────────────────────────────────────────────
python-decouple==3.8                # Environment variable management
django-environ==0.11.2              # Alternative: .env file loading

# ── Payments ────────────────────────────────────────────────
stripe==8.4.0                       # Stripe payment gateway SDK

# ── Utilities ────────────────────────────────────────────────
Pillow==10.2.0                      # Image processing (already listed)
python-dateutil==2.8.2              # Date arithmetic utilities

# ── Development Only ─────────────────────────────────────────
# (move to requirements-dev.txt in production)
django-debug-toolbar==4.3.0         # Development query debugging
factory-boy==3.3.0                  # Test data factories
locust==2.22.0                      # Load testing
coverage==7.4.0                     # Test coverage reporting
```

---

# 📋 PART 8 — KEY DJANGO CONCEPTS EVERY TEAM MEMBER MUST KNOW

```md
# Django Fundamentals for This Project
# What every person on the team must understand

---

## 1. DJANGO SETTINGS SPLIT

Never put everything in one settings.py.
  config/settings/base.py     → Common to all environments
  config/settings/development.py → DEBUG=True, SQLite ok, no HTTPS
  config/settings/production.py  → DEBUG=False, MySQL, HTTPS enforced

Run with specific settings:
  python manage.py runserver --settings=config.settings.development
  Production: DJANGO_SETTINGS_MODULE=config.settings.production

---

## 2. CUSTOM USER MODEL — MUST BE SET FIRST

Before running ANY migration:
  AUTH_USER_MODEL = 'users.CustomUser' must be in settings.
  If this is changed after migrations exist, the entire database
  must be rebuilt. This is not recoverable incrementally.
  Set it in base.py before python manage.py migrate is ever run.

---

## 3. DJANGO MIGRATIONS ARE THE SCHEMA

No separate database_schema.sql.
Django migrations ARE the schema.
  python manage.py makemigrations  → generates migration files
  python manage.py migrate         → applies migrations to MySQL
  python manage.py showmigrations  → shows applied/unapplied status
  python manage.py sqlmigrate app 0001 → shows the SQL a migration generates

---

## 4. DJANGO ADMIN (Available but Optional)

Django ships with a built-in admin interface.
The project scope says no admin panel.
But Django admin can serve as the minimal operations console
discussed in the solutions document — restricted to staff users,
accessible only from internal IP, used only for emergency operations.
This replaces the need to build a custom operations console from scratch.

Enable with: admin.site.register(CustomUser, CustomUserAdmin)
Protect with: AdminSiteOnlyForStaffMiddleware or IP restriction

---

## 5. DJANGO SIGNALS (For Cross-App Events)

Django signals allow decoupled communication between apps.
When an invoice is marked Paid, a signal fires.
The notifications app listens for that signal and creates a notification.
The analytics app listens and updates cached metrics.
Neither app directly calls the other.
This preserves separation of concerns across Django apps.

Key signals used:
  post_save on Invoice (status change to Paid)
  post_save on MaintenanceTicket (status change to Resolved)
  post_save on Lease (status change to Active)

---

## 6. DJANGO TESTING

Django provides a test client and test database.
Tests use a separate MySQL test database created automatically.
  python manage.py test              → runs all tests
  python manage.py test apps.users   → runs only users app tests

Test database is created fresh before each test run.
Tests are isolated — no production data is ever touched.
The test database uses the same MySQL configuration as development.
```

---

# 📊 THE COMPLETE UPDATE SUMMARY

| What Changed | From | To | Impact |
|---|---|---|---|
| Web framework | Flask (micro) | Django 4.2 LTS (full) | Architecture, ORM, middleware, auth all provided |
| API framework | Manual Flask routes | Django REST Framework | Serializers, viewsets, permissions, routers |
| Authentication | PyJWT manual | simplejwt + Django auth | Full auth system with JWT |
| Middleware | Custom from scratch | Django middleware + custom | Built-in security, CSRF, auth in pipeline |
| Database | PostgreSQL | MySQL 8.0 (InnoDB) | utf8mb4, STRICT mode, InnoDB required |
| ORM | Raw SQL (psycopg2) | Django ORM | Parameterized by default, N+1 solved by design |
| Schema management | database_schema.sql | Django migrations | Python-managed, version-controlled, reversible |
| WebSockets | Flask-SocketIO | Django Channels + Redis | ASGI, channel layer, consumer pattern |
| Background jobs | APScheduler | Celery + celery-beat | Distributed, monitored, Redis-backed |
| File storage | Local file system | django-storages abstraction | Swappable to S3 without code changes |
| CSRF | Manual tokens | Django CsrfViewMiddleware | Automatic, framework-level enforcement |
| Password hashing | Manual bcrypt | Django BCryptSHA256PasswordHasher | Framework-managed |
| Project structure | Single app | Django multi-app architecture | Clean domain separation |
| Static files | Manual paths | Django static files + collectstatic | Environment-aware serving |
| Testing | Manual pytest | Django test framework + test client | Isolated test database |

---

> **The core technology decision is clear:**
> **HTML + CSS + JavaScript on the frontend.**
> **Django + DRF + Channels on the backend.**
> **MySQL with InnoDB on the database.**
> **Redis for WebSockets and Celery.**
>
> Every principle, every security rule, every architectural decision
> from every conversation in this chat remains exactly the same.
> Only the tools implementing those decisions have been updated
> to reflect the correct, final technology stack.
please the primary languages are html, css, javascript, python(django), and mysql, please add websocket, chart.js, pptx.js, 
# 📁 Complete `.md` File Suite
## Rent & Lease Management System
### Based on Every Conversation, Decision, Architecture, and Principle Discussed

---

# FILE 1 — `AI_rules.md`

```md
# 🤖 AI_rules.md
# Rent & Lease Management System — AI Behaviour Rules
# Every AI tool, assistant, or code generator working on this project must follow these rules without exception.

---

## 🎯 PROJECT IDENTITY

- Project Name   : Rent & Lease Management System
- Type           : Full-Stack Web Application (SaaS)
- Tech Stack     : HTML + CSS + JavaScript (Frontend) | Python (Backend + Middleware + API) | SQL (Database)
- Users          : Landlords (Desktop) | Tenants (Mobile-first)
- Total Pages    : 38 (14 Landlord + 11 Tenant + 13 External/System)
- Architecture   : 9-Layer System (Structure → Styling → Behavior → Middleware → API → Business Rules → Business Logic → Data Retrieval → Data Storage)

---

## 🧠 THINKING RULES

1. Read every instruction fully before generating anything
2. Think in systems — every decision affects every layer
3. Apply Bloom's Taxonomy levels 1–6 before producing output
4. Reason from first principles — do not guess
5. If uncertain, state the uncertainty clearly and stop
6. Never produce output that violates a principle stated in this file
7. Think in the box — stay within the scope of what is asked

---

## 🏗️ ARCHITECTURE RULES

1. Every feature must be designed across all 9 layers explicitly
2. Structure (HTML) only declares existence — never style or behavior inline
3. Styling (CSS) only handles visual appearance — never business decisions
4. Behavior (JavaScript) is for UX only — never security enforcement
5. Middleware runs first — always in this order:
   Security Headers → CORS → Request Logging → Rate Limiting → Authentication → Authorization (IDOR)
6. API routes never touch the database directly — always via Business Logic
7. Business Rules are checked before Business Logic executes
8. Data Retrieval and Data Storage are always separate functions
9. Every database write uses parameterized queries — no string concatenation ever
10. Every database transaction that involves multiple writes is atomic (ACID)

---

## 📐 ENGINEERING PRINCIPLES (NON-NEGOTIABLE)

1. Single Responsibility Principle — every function does exactly one thing
2. Separation of Concerns — each layer owns only its concern
3. DRY (Don't Repeat Yourself) — every piece of logic lives in exactly one place
4. Defence in Depth — security is enforced at every layer independently
5. Principle of Least Privilege — every component accesses only what it needs
6. Fail Fast, Fail Safely — detect errors early, never expose internal details to users
7. Explicit over Implicit — never rely on hidden defaults or magic behavior
8. Optimistic UI with Safe Rollback — update UI instantly, roll back on server rejection
9. Stateless API — every request carries all information needed to process it
10. Idempotency on critical endpoints — submitting the same request twice produces the same result as once

---

## 🔐 SECURITY RULES

1. Never trust the frontend — every frontend validation must be re-enforced server-side
2. Never store passwords in plain text — bcrypt hashing only
3. Never expose stack traces, error details, or file paths to the browser
4. Never concatenate user input into SQL queries
5. Never store secrets (API keys, JWT secrets, DB passwords) in source code
6. All secrets live in environment variables only
7. JWT tokens are short-lived and verified on every request
8. IDOR protection is applied at both Middleware and query level (WHERE owner_id = authenticated_user_id)
9. Rate limiting is applied at both Middleware level (broad) and API endpoint level (specific)
10. HTTPS is enforced on all production traffic
11. CSRF tokens on all state-changing forms
12. CORS is configured to allow only known, trusted origins
13. Input is validated, sanitized, and type-checked at the API boundary before reaching business logic
14. Audit logs are append-only and immutable
15. Soft deletes only — critical data is never hard deleted

---

## 🎨 DESIGN RULES

1. Design System tokens from design.md must be used — no arbitrary values
2. 4px base spacing unit — all spacing is a multiple of 4
3. Desktop-optimized F-Pattern layout for Landlord pages
4. Mobile-first design for all Tenant pages — minimum 48px touch targets
5. Deep Blue (#0F172A) is the primary action color
6. Muted Red (#EF4444) is exclusively for errors, warnings, and overdue states
7. Muted Emerald (#10B981) is exclusively for success and active states
8. All animations use cubic-bezier easing — no linear transitions on interactive elements
9. Loading states, error states, and empty states must be designed for every component
10. Accessibility (A11Y) is required — keyboard navigation, screen reader labels, color contrast

---

## 📏 CODE QUALITY RULES

1. Every function has one job — if it does two things, split it
2. Every function can be described in one sentence without the word "and"
3. No function is longer than it needs to be
4. Error handling is explicit — no silent failures
5. All user-facing error messages are generic — all internal errors go to the log
6. Naming is explicit and descriptive — no abbreviations, no magic numbers
7. File structure follows the defined project structure in file_structure.md
8. Naming follows the conventions in naming_patterns.md

---

## 🚫 FORBIDDEN ACTIONS

- Never introduce colors outside the design system palette
- Never write business logic inside HTML templates
- Never query the database inside an API route handler directly
- Never skip the middleware order
- Never submit a form without CSRF validation
- Never return HTTP 200 for an error response
- Never store the full payment card number
- Never log sensitive user data (passwords, tokens, card numbers) to log files
- Never allow a user to access another user's resource without explicit ownership verification
- Never deploy with debug mode enabled

---

## ✅ STOPPING RULE

Stop generating when:
- The requested feature is complete across all relevant layers
- Every security rule has been applied
- Every principle has been respected
- The output is clear, correct, and self-explanatory

Do not add unrequested features.
Do not over-engineer beyond the defined scope.
Do not continue if a rule conflict is detected — flag it first.
```

---

# FILE 2 — `plan.md`

```md
# 📅 plan.md
# Rent & Lease Management System — Project Plan
# Semester Build Plan | Week-by-Week | Milestones | Deliverables

---

## 🎯 PROJECT GOAL

Build a full-stack, production-ready Rent & Lease Management System that serves two user types
(Landlords and Tenants) across 38 pages, with real-time chat, automated billing, Kanban
maintenance management, analytics, and a complete security perimeter.

---

## 👥 TEAM

- Roles              : Full-Stack Engineers
- Frontend Stack     : HTML, CSS, JavaScript
- Backend Stack      : Python (Flask or FastAPI)
- Database           : SQL (PostgreSQL or SQLite for development)
- Architecture       : 9-Layer System

---

## 📆 SEMESTER TIMELINE — 15 WEEKS

---

### 🏗️ PHASE 0 — FOUNDATION (Week 1)
**Goal: Establish all project scaffolding before writing any feature code**

Deliverables:
- [ ] All .md files created and committed (this file included)
- [ ] Project folder structure created per file_structure.md
- [ ] Design system CSS variables and base components built
- [ ] Database schema written and reviewed
- [ ] Environment variables configured
- [ ] Git repository initialized with .gitignore
- [ ] Base HTML templates (layout_landlord, layout_tenant, layout_auth) created
- [ ] Development environment verified working end-to-end

Exit Criteria: A blank-but-structured project where every layer has its home

---

### 🔐 PHASE 1 — AUTHENTICATION & SECURITY PERIMETER (Weeks 2–3)
**Goal: Build the complete identity and access layer before any feature**

Week 2 Deliverables:
- [ ] Database: users table, roles, tokens
- [ ] Registration page (External Page 2) — Role toggle, form, validation
- [ ] Login page (External Page 3) — JWT issue, role-based routing
- [ ] Email verification flow (External Page 5)
- [ ] Authentication Middleware — JWT verification
- [ ] Rate Limiting Middleware — login endpoint (10 attempts / 15 min)
- [ ] CORS Middleware configured
- [ ] Security Headers Middleware

Week 3 Deliverables:
- [ ] Forgot Password page (External Page 6)
- [ ] Reset Password page (External Page 7) — 15-minute token expiry
- [ ] Authorization Middleware — IDOR prevention base layer
- [ ] Request Logging Middleware — audit trail initiated
- [ ] Lease Invitation Gateway (External Page 4) — encrypted URL flow
- [ ] 403, 429, 404, 503 error pages (External Pages 10–13)

Exit Criteria: Complete user registration → login → dashboard routing working securely

---

### 🏠 PHASE 2 — LANDLORD CORE (Weeks 4–6)
**Goal: Build the primary Landlord management workflow**

Week 4 Deliverables:
- [ ] Landlord Dashboard (Landlord Page 1) — metrics, transactions, expiring leases
- [ ] Property Portfolio (Landlord Page 2) — grid, add/edit/delete with active lease block
- [ ] Database: properties table, status constraints

Week 5 Deliverables:
- [ ] Leases & Tenant Onboarding (Landlord Page 3) — table, create modal, overlap validation
- [ ] Tenant Directory CRM (Landlord Page 7) — slide-out drawer
- [ ] Database: leases table, invitations table, enrollments

Week 6 Deliverables:
- [ ] Financials & Billing (Landlord Page 4) — invoice ledger, late fee rows, export
- [ ] Expense & ROI Ledger (Landlord Page 12) — expense log, net income calculator
- [ ] Database: invoices table, transactions table, expenses table

Exit Criteria: A Landlord can register, add properties, create leases, invite tenants, and view financials

---

### 📱 PHASE 3 — TENANT CORE (Weeks 7–8)
**Goal: Build the complete Tenant living experience**

Week 7 Deliverables:
- [ ] Tenant Dashboard (Tenant Page 1) — hero card, balance states, quick actions
- [ ] Rent Payment & Invoices (Tenant Page 2) — locked amount, payment submission
- [ ] Payment Success page (External Page 8)
- [ ] Payment Cancelled page (External Page 9)
- [ ] My Lease & Property Details (Tenant Page 3) — progress bar, document view

Week 8 Deliverables:
- [ ] Payment Methods & Auto-Pay (Tenant Page 7) — card management, toggle
- [ ] Profile & Settings (Tenant Page 10) — locked email, emergency contact
- [ ] Compliance & Insurance (Tenant Page 9) — upload blocks, expiry tracking
- [ ] Database: payment_methods table, automation_settings table, compliance_documents table

Exit Criteria: A Tenant can log in, see their balance, pay rent, and manage their account

---

### 🔧 PHASE 4 — MAINTENANCE & OPERATIONS (Week 9)
**Goal: Build the maintenance helpdesk workflow for both users**

Deliverables:
- [ ] Maintenance Helpdesk Kanban (Landlord Page 6) — drag-and-drop, priority tags
- [ ] Maintenance Helpdesk Tenant (Tenant Page 4) — ticket submission, spam limit, status tracker
- [ ] Move-In/Move-Out Inspection (Tenant Page 6) — accordion checklist, progress-gated submit
- [ ] Multi-Unit & Building Management (Landlord Page 13) — tree view, bulk operations
- [ ] Database: maintenance_tickets table, ticket_comments table, inspections table, buildings table

Exit Criteria: Complete ticket lifecycle from Tenant submission to Landlord resolution

---

### 💬 PHASE 5 — REAL-TIME FEATURES (Week 10)
**Goal: Build all WebSocket-driven real-time communication**

Deliverables:
- [ ] Real-Time Chat Landlord (Landlord Page 5) — two-pane, contact list, read receipts
- [ ] Real-Time Chat Tenant (Tenant Page 5) — single thread, typing indicator
- [ ] Notice Board Tenant (Tenant Page 8) — read-only broadcast feed
- [ ] WebSocket connection management, authentication, reconnection logic
- [ ] Database: messages table, conversations table, notices table

Exit Criteria: Landlord and Tenant can exchange real-time messages with read receipts

---

### 📊 PHASE 6 — INTELLIGENCE & AUTOMATION (Weeks 11–12)
**Goal: Build analytics, reporting, and all automated background processes**

Week 11 Deliverables:
- [ ] Advanced Analytics (Landlord Page 9) — revenue chart, donut charts, Chart.js integration
- [ ] System Notifications (Landlord Page 10) — chronological feed, icon states
- [ ] Notification & History Center Tenant (Tenant Page 11) — audit log, infinite scroll
- [ ] Database: notifications table, audit_log table

Week 12 Deliverables:
- [ ] Automated Reminders Control Panel (Landlord Page 14) — cron toggle switches
- [ ] Python Scheduler — nightly late fee application
- [ ] Python Scheduler — lease expiry warning (60-day scan)
- [ ] Python Scheduler — rent reminder emails (3-day)
- [ ] Auto-Pay cron job — 1st of month deduction
- [ ] Database: cron_jobs table, automation_settings table

Exit Criteria: System runs automated processes without human intervention

---

### 🗂️ PHASE 7 — DOCUMENT MANAGEMENT (Week 12, continued)
**Goal: Build the secure document vault**

Deliverables:
- [ ] Document Center (Landlord Page 8) — drag-and-drop upload, grid view, IDOR download
- [ ] Settings & Profile Management (Landlord Page 11) — vertical tabs, bank details, toggles
- [ ] Database: documents table, folders table

Exit Criteria: Files can be uploaded, organized, and downloaded with IDOR protection

---

### 🌍 PHASE 8 — PUBLIC SHELL (Week 13)
**Goal: Build the marketing and public-facing pages**

Deliverables:
- [ ] Public Landing Page (External Page 1) — hero, features, dual CTA
- [ ] All error pages finalized and styled (403, 429, 404, 503)
- [ ] Sticky navbar scroll behavior
- [ ] Scroll reveal animations on feature cards

Exit Criteria: A new visitor can land on the platform, understand it, and register

---

### 🧪 PHASE 9 — TESTING & HARDENING (Week 14)
**Goal: Verify correctness, security, and performance across the entire system**

Deliverables:
- [ ] All 38 pages tested for functional correctness
- [ ] IDOR attack simulation — verify all resource ownership checks
- [ ] Rate limiting tested — verify 429 responses fire correctly
- [ ] SQL injection testing — verify all queries are parameterized
- [ ] XSS testing — verify all user output is escaped
- [ ] CSRF testing — verify all forms validate tokens
- [ ] Mobile responsiveness verified on 375px, 414px viewports
- [ ] Keyboard navigation tested across all forms
- [ ] All cron jobs tested with simulated dates
- [ ] Performance audit — no page load over 3 seconds

---

### 🚀 PHASE 10 — FINAL POLISH & PRESENTATION (Week 15)
**Goal: Production-ready delivery**

Deliverables:
- [ ] All animations and transitions finalized
- [ ] All empty states, loading states, and error states implemented
- [ ] Documentation reviewed and completed
- [ ] Demo walkthrough script prepared
- [ ] Final code review against AI_rules.md
- [ ] System deployed to staging environment
- [ ] Presentation prepared

---

## 📊 MILESTONE SUMMARY

| Milestone | Week | Completion Gate |
|---|---|---|
| Foundation Complete | 1 | All .md files, DB schema, folder structure |
| Authentication Live | 3 | Register → Login → Dashboard routing |
| Landlord MVP | 6 | Property, Lease, Billing complete |
| Tenant MVP | 8 | Dashboard, Payment, Profile complete |
| Maintenance Live | 9 | Kanban + ticket lifecycle complete |
| Real-Time Features | 10 | Chat + WebSocket working |
| Automation Live | 12 | Cron jobs running + analytics complete |
| Full System | 13 | All 38 pages functional |
| System Hardened | 14 | All security tests passed |
| Production Ready | 15 | Deployed, documented, presented |
```

---

# FILE 3 — `prd.md`

```md
# 📋 prd.md
# Product Requirements Document
# Rent & Lease Management System

---

## 1. PRODUCT OVERVIEW

The Rent & Lease Management System is a dual-portal SaaS web application that digitizes and
automates the complete property rental lifecycle. It serves two distinct user types with
purpose-built experiences: Landlords managing their property portfolios from desktop, and
Tenants managing their living arrangements from mobile devices.

The platform eliminates paper contracts, manual rent collection, WhatsApp-based maintenance
requests, and spreadsheet-based financial tracking — replacing them with a unified, automated,
real-time digital system.

---

## 2. THE PROBLEM BEING SOLVED

Landlords:
- Track rent payments across multiple properties manually
- Have no central record of maintenance requests
- Cannot see portfolio-wide financial performance at a glance
- Communicate with tenants through informal channels with no record
- Have no automated mechanism for applying late fees or expiry warnings

Tenants:
- Have no clear view of their current balance and payment history
- Cannot formally document maintenance issues with evidence
- Have no central location for their lease documents
- Cannot prove property condition at move-in for security deposit disputes
- Have no automated payment option to avoid late fees

---

## 3. PRODUCT VISION

A system where a Landlord can manage 50 units with the same effort it currently takes to
manage 5, and where a Tenant always knows exactly what they owe, when they owe it, and
has a formal channel for every interaction with their Landlord.

---

## 4. USERS

### 4.1 Landlord
- Uses system on desktop (optimized F-Pattern layout)
- Primary concern: portfolio health, revenue collection, maintenance resolution
- Technical comfort: moderate — expects professional CRM-like experience
- Key motivation: reduce manual work, increase visibility, protect investments

### 4.2 Tenant
- Uses system on mobile (optimized mobile-first layout)
- Primary concern: knowing what I owe, paying easily, getting repairs done
- Technical comfort: low-to-moderate — expects consumer-app simplicity
- Key motivation: avoid late fees, document issues, access lease information

---

## 5. COMPLETE FEATURE LIST

### 5.1 Authentication & Identity (All Users)
- FR-001 : Role-based registration (Landlord or Tenant) with toggle selection
- FR-002 : Email verification before account activation
- FR-003 : JWT-based session management with token expiry
- FR-004 : Forgot password with time-limited reset link (15-minute expiry)
- FR-005 : Lease invitation gateway — Tenant registers via encrypted URL from Landlord
- FR-006 : Account is automatically bound to the correct lease upon invitation acceptance

### 5.2 Property Management (Landlord)
- FR-010 : Add, edit, and delete properties with address, unit number, and base rent
- FR-011 : Delete blocked by system if active lease exists (with tooltip explanation)
- FR-012 : Occupancy status badge per property (Leased / Vacant)
- FR-013 : Multi-unit building grouping with accordion tree view
- FR-014 : Bulk financial view per parent building

### 5.3 Lease Management (Landlord)
- FR-020 : Create lease with unit, start date, end date, and rent amount
- FR-021 : Real-time overlap validation — no two active leases on same unit for same dates
- FR-022 : Invite tenant via email upon lease creation
- FR-023 : View all active and expired leases in sortable table
- FR-024 : Renew expiring leases via dashboard widget
- FR-025 : Lease expiry warning appears at 60 days (automated cron)

### 5.4 Financial Management (Landlord)
- FR-030 : Invoice ledger filtered by property, month, and status
- FR-031 : 5% late fee applied automatically to overdue invoices (automated cron)
- FR-032 : Overdue rows highlighted with Muted Red left border
- FR-033 : Export financial reports as CSV and PDF
- FR-034 : Log property expenses (repairs, taxes, maintenance costs)
- FR-035 : Net ROI calculator — revenue minus expenses per property
- FR-036 : Record offline cash payments manually

### 5.5 Rent Payment (Tenant)
- FR-040 : Hero card shows current balance with clear Safe / Due / Overdue state
- FR-041 : Payment amount is locked (readonly) — system-calculated, not user-editable
- FR-042 : Payment submission triggers gateway integration (Stripe / Paystack)
- FR-043 : Submit button disables after first tap (prevents double-charging)
- FR-044 : Payment success and payment cancelled pages with appropriate states
- FR-045 : Past invoices viewable with PDF receipt download
- FR-046 : Auto-Pay toggle — deducts exact rent on 1st of each month

### 5.6 Maintenance Helpdesk
- FR-050 : Tenant submits ticket with category, urgency, description, and photo evidence
- FR-051 : Tenant blocked from submitting if 3 active tickets already open (spam rule)
- FR-052 : Kanban board for Landlord — three columns: Pending, In Progress, Resolved
- FR-053 : Drag-and-drop ticket status update on Kanban
- FR-054 : Priority tags — Emergency (Muted Red), Low (Soft Gray)
- FR-055 : Tenant can add follow-up comments to open tickets
- FR-056 : Resolution notification sent to Tenant when Landlord closes ticket

### 5.7 Real-Time Chat
- FR-060 : WebSocket-based instant messaging between Landlord and Tenant
- FR-061 : Landlord sees all tenant contacts in left pane — selects to open thread
- FR-062 : Tenant opens directly into their single Landlord thread
- FR-063 : Photo and file attachment support
- FR-064 : Drag-and-drop file upload (Landlord desktop)
- FR-065 : Typing indicators and read receipts (blue double ticks)
- FR-066 : Online/offline presence indicators

### 5.8 Move-In/Move-Out Inspection
- FR-070 : Room-by-room accordion checklist
- FR-071 : Mandatory photo upload per room
- FR-072 : Progress-gated submission — 100% completion required
- FR-073 : Form becomes permanently readonly after submission (legal lock)

### 5.9 Document Management
- FR-080 : Drag-and-drop file upload
- FR-081 : Google Drive-style grid view organized by property folder
- FR-082 : IDOR-protected download — JWT verification before file streaming
- FR-083 : Delete with typed confirmation ("Type DELETE to confirm")

### 5.10 Analytics
- FR-090 : 12-month revenue line chart (Chart.js)
- FR-091 : Maintenance category breakdown donut chart
- FR-092 : Payment timeliness ratio donut chart
- FR-093 : At-risk tenant identification
- FR-094 : Export analytics as CSV

### 5.11 Automation Control Panel (Landlord)
- FR-100 : Toggle: 3-Day Rent Reminder Emails
- FR-101 : Toggle: Auto-Apply 5% Late Fee
- FR-102 : Toggle: Lease Expiry Warning (60 days)
- FR-103 : Real-time active/inactive status display

### 5.12 Compliance (Tenant)
- FR-110 : Upload Government ID, Proof of Income, Renter's Insurance
- FR-111 : Document verification status badges
- FR-112 : Expiry date tracking for insurance
- FR-113 : Automated warning when insurance expires within 30 days
- FR-114 : Red banner on dashboard if document is expired

### 5.13 Notifications
- FR-120 : Real-time notification push via WebSocket
- FR-121 : Chronological notification feed with unread/read states
- FR-122 : Icon-based event type identification
- FR-123 : Mark all as read function
- FR-124 : Infinite scroll pagination on history

### 5.14 Notice Board (Tenant)
- FR-130 : Landlord publishes broadcast announcements to all tenants in a building
- FR-131 : Standard notices vs urgent alerts (visual distinction)
- FR-132 : Entirely read-only for tenants

---

## 6. NON-FUNCTIONAL REQUIREMENTS

### 6.1 Performance
- NFR-001 : Dashboard loads in under 2 seconds on standard connection
- NFR-002 : Chat message delivery under 100ms (WebSocket)
- NFR-003 : Payment processing completes within 5 seconds
- NFR-004 : No page load exceeds 3 seconds on mobile
- NFR-005 : Analytics page load under 3 seconds (with caching on aggregation queries)

### 6.2 Security
- NFR-010 : All traffic over HTTPS in production
- NFR-011 : JWT tokens expire after 24 hours
- NFR-012 : Password reset links expire after 15 minutes
- NFR-013 : Invitation links expire after 24 hours
- NFR-014 : All SQL queries parameterized
- NFR-015 : IDOR protection on all resource endpoints
- NFR-016 : Rate limiting on all state-changing endpoints
- NFR-017 : Audit log for all financial and security events

### 6.3 Reliability
- NFR-020 : Cron jobs retry on failure (max 3 attempts)
- NFR-021 : Payment webhook processing is idempotent
- NFR-022 : Auto-save chat messages locally if WebSocket disconnects
- NFR-023 : System continues functioning if email service is unavailable

### 6.4 Usability
- NFR-030 : Mobile-first design for all Tenant pages
- NFR-031 : Minimum 48px touch targets on all mobile interactive elements
- NFR-032 : All forms have clear error states with specific messages
- NFR-033 : All destructive actions require confirmation
- NFR-034 : Keyboard navigation supported across all forms

### 6.5 Accessibility
- NFR-040 : All form inputs have associated labels
- NFR-041 : Color is never the only indicator of state
- NFR-042 : WCAG AA color contrast minimum

---

## 7. IN-SCOPE

- All 38 pages listed in the page specifications
- All 14 Landlord portal pages
- All 11 Tenant portal pages
- All 13 External and System pages
- Real-time chat via WebSocket
- Automated cron jobs (late fees, reminders, expiry warnings)
- Payment gateway integration (Stripe or Paystack)
- Document management with IDOR protection
- Analytics and reporting with Chart.js
- Multi-unit building management

---

## 8. OUT-OF-SCOPE

- Admin panel of any kind
- Multi-language (internationalization)
- Native mobile app (iOS or Android)
- Accounting software integration (QuickBooks, Xero)
- Property listing or marketplace features (this is management only)
- Tenant-to-tenant communication
- Third-party identity providers (Google SSO, Facebook Login)
- Video or audio calling
- AI-assisted features

---

## 9. SUCCESS CRITERIA

- A Landlord with zero technical training can add a property and invite a Tenant in under 5 minutes
- A Tenant sees their exact balance due within 2 seconds of opening the dashboard
- A rent payment completes end-to-end in under 10 seconds
- A maintenance ticket submitted by a Tenant appears on the Landlord Kanban in under 3 seconds
- The system correctly applies and prevents duplicate late fees across 100 concurrent invoices
- An IDOR attack attempt returns 403 and is logged to the audit trail
- A brute-force login attempt triggers the 429 rate limit after 10 attempts
```

---

# FILE 4 — `architecture.md`

```md
# 🏗️ architecture.md
# Rent & Lease Management System — System Architecture
# The 9-Layer Architecture | Complete Layer Definitions | Request Lifecycle

---

## 1. ARCHITECTURE PHILOSOPHY

The system is built on a strict 9-layer separation where each layer owns exactly
one concern, communicates with adjacent layers only, and never bypasses layers
to communicate directly with non-adjacent ones.

Frontend layers (1–3) live in the browser and are untrusted.
Backend layers (4–7) live on the server and are trusted.
Data layers (8–9) live in the database and are trusted.

---

## 2. THE 9 LAYERS

### LAYER 1 — STRUCTURE (HTML)
- Responsibility  : Declare what exists on each page and its semantic meaning
- Owns            : DOM elements, semantic tags, content order, accessibility attributes
- Never Does      : Style itself, execute behavior, make data decisions
- Trust Level     : Untrusted (user can modify in DevTools)

### LAYER 2 — STYLING (CSS)
- Responsibility  : Define visual appearance, spacing, animation, responsive breakpoints
- Owns            : Design tokens, layout systems, component styles, transitions, keyframes
- Never Does      : Make data decisions, communicate with server, control business logic
- Trust Level     : Untrusted (user can modify in DevTools)

### LAYER 3 — BEHAVIOR (JavaScript)
- Responsibility  : Handle user interactions, manage UI state, communicate with API
- Owns            : Event listeners, fetch calls, DOM manipulation, WebSocket client, form UX
- Never Does      : Store permanent data, enforce security, be the sole validation layer
- Trust Level     : NEVER trusted — all JS validation is for UX only, never security

### LAYER 4 — MIDDLEWARE (Python)
- Responsibility  : System-wide gatekeeping before any request reaches application logic
- Owns            : Authentication, Authorization/IDOR, Rate Limiting, CORS, Security Headers, Logging
- Execution Order : Security Headers → CORS → Request Logging → Rate Limiting → Authentication → Authorization
- Never Does      : Business logic, data operations, request routing
- Trust Level     : Fully trusted

### LAYER 5 — API (Python)
- Responsibility  : Define the official request/response contract, route requests to handlers
- Owns            : Endpoint definitions, HTTP method enforcement, input validation/sanitization, endpoint-specific rate limits, response formatting
- Never Does      : Direct database access, complex business orchestration
- Trust Level     : Fully trusted

### LAYER 6 — BUSINESS RULES (Python)
- Responsibility  : Enforce all fixed, non-negotiable system constraints
- Owns            : Constraint validation, pre-condition checks, system law enforcement
- Never Does      : Dynamic orchestration, data operations
- Trust Level     : Fully trusted
- Runs Before     : Business Logic always

### LAYER 7 — BUSINESS LOGIC (Python)
- Responsibility  : Orchestrate dynamic processes, decisions, and external service coordination
- Owns            : Multi-step workflows, external API calls (payment gateway, email), calculations, cron job logic
- Never Does      : Direct database access (calls Data Retrieval and Data Storage functions)
- Trust Level     : Fully trusted
- Runs After      : Business Rules always

### LAYER 8 — DATA RETRIEVAL (SQL)
- Responsibility  : Fetch exactly the right records with minimum queries and maximum efficiency
- Owns            : SELECT queries, JOINs, aggregations, pagination, indexes, query optimization
- Never Does      : Change data, enforce business rules
- Trust Level     : Fully trusted

### LAYER 9 — DATA STORAGE (SQL)
- Responsibility  : Permanently and safely record new and changed data
- Owns            : INSERT, UPDATE, DELETE (soft), transactions, constraints, parameterized writes
- Never Does      : Retrieve data for display, make business decisions
- Trust Level     : Fully trusted

---

## 3. COMMUNICATION RULES BETWEEN LAYERS

- Layer 3 (JS)          → communicates with → Layer 5 (API) via HTTP/WebSocket
- Layer 4 (Middleware)  → intercepts before → Layer 5 (API)
- Layer 5 (API)         → calls → Layer 6 (Business Rules)
- Layer 5 (API)         → calls → Layer 7 (Business Logic) after rules pass
- Layer 7 (Logic)       → calls → Layer 8 (Data Retrieval) when reading
- Layer 7 (Logic)       → calls → Layer 9 (Data Storage) when writing
- NO layer skips another layer
- NO layer calls a non-adjacent layer directly

---

## 4. REAL-TIME ARCHITECTURE

Chat and Notifications use WebSocket connections (not REST).
WebSocket connection bootstrapped and authenticated by Layer 5 (API).
Once authenticated, the persistent connection is managed by the WebSocket handler.
Messages are stored via Layer 9 (Data Storage) and retrieved via Layer 8 (Data Retrieval).
The Layer 7 (Business Logic) pushes events to connected WebSocket clients.

---

## 5. BACKGROUND PROCESSING ARCHITECTURE

Python Scheduler (APScheduler or Celery) runs independently of the request cycle.
Scheduler reads automation settings from the database before each job execution.
Scheduler jobs call Layer 7 (Business Logic) functions — same path as request-triggered logic.
All scheduler activity is logged to the audit_log table.

Jobs:
- nightly_late_fee_job       : Applies 5% late fee to overdue invoices
- lease_expiry_scanner       : Creates 60-day warnings for expiring leases
- rent_reminder_sender       : Sends 3-day-before-due reminder emails
- auto_pay_processor         : Processes auto-pay on 1st of month

---

## 6. REQUEST LIFECYCLE (SUMMARY)

User Action → JS (Layer 3) sends HTTP request →
Middleware Stack (Layer 4) gates the request →
API Router (Layer 5) routes and validates →
Business Rules (Layer 6) checks constraints →
Business Logic (Layer 7) orchestrates the operation →
Data Retrieval (Layer 8) or Data Storage (Layer 9) executes →
Response travels back up →
JS (Layer 3) updates the UI →
CSS (Layer 2) renders the visual state →
HTML (Layer 1) displays the result

---

## 7. DATABASE ARCHITECTURE OVERVIEW

Engine         : PostgreSQL (production) / SQLite (development)
Encoding       : UTF-8
Timestamps     : All stored in UTC
Deletes        : Soft deletes only (deleted_at column) for critical tables
Transactions   : All multi-table writes wrapped in atomic transactions
Queries        : All parameterized — no string concatenation
Indexes        : Applied to all frequently queried foreign keys and filter columns

Core Tables:
users | properties | buildings | leases | invitations |
invoices | transactions | expenses | payment_methods |
maintenance_tickets | ticket_comments | inspections |
messages | conversations | notices |
documents | folders |
notifications | audit_log |
automation_settings | cron_jobs |
compliance_documents
```

---

# FILE 5 — `design.md`

```md
# 🎨 design.md
# Rent & Lease Management System — Complete Design System
# Colors | Typography | Spacing | Components | Animations | UX Principles

---

## 1. DESIGN PHILOSOPHY

Two distinct visual identities serve two distinct user contexts:

Landlord Portal — Desktop CRM aesthetic. Professional, data-dense, trusted.
                  Inspired by Notion and Linear. Authority and clarity.

Tenant Portal   — Mobile consumer aesthetic. Warm, clear, frictionless.
                  Inspired by Monzo and Revolut. Speed and reassurance.

Both share the same design tokens and component patterns.
The difference is layout density, interaction model, and information hierarchy.

---

## 2. COLOR PALETTE

Primary (Deep Blue)       : #0F172A  — Main actions, sidebar, primary buttons, active states
Secondary (Dark Slate)    : #1E293B  — Secondary text, sub-headings
Background (Light Gray)   : #F8FAFC  — Main page canvas
Surface (Pure White)      : #FFFFFF  — Cards, modals, drawers, elevated elements
Text Primary (Dark Slate) : #1E293B  — Headings, body copy
Text Secondary            : #64748B  — Captions, helper text, placeholders, metadata
Border (Soft Gray)        : #E2E8F0  — Dividers, input outlines, subtle separators
Muted Emerald             : #10B981  — Success states, Leased badges, payment confirmed, On toggles
Muted Red                 : #EF4444  — Error states, overdue, blocked, urgent, Declined
Amber                     : #F59E0B  — Warning states, Pending tickets, caution indicators
Blue Glow (focus ring)    : rgba(15, 23, 42, 0.15) — Input focus shadow

Usage Law:
- Deep Blue   : Only for primary actions and active UI elements
- Muted Red   : Only for errors, warnings, overdue states, and urgent notices
- Muted Emerald: Only for success, completion, active paid states
- Never introduce a color not on this list

---

## 3. TYPOGRAPHY

Font Family  : System UI stack — system-ui, -apple-system, BlinkMacSystemFont, sans-serif
              (No external font dependencies — maximum performance)

Headings     : Bold weight, tight tracking (letter-spacing: -0.02em)
Body         : Regular weight, normal tracking
Labels       : Semi-bold (500), small caps optional for section labels
Captions     : Regular, #64748B color, 12–13px

Size Scale (px) : 12 | 14 | 16 | 20 | 24 | 32 | 40 | 48
Line Height     : 1.5 for body, 1.25 for headings
Base font size  : 16px (1rem)

---

## 4. SPACING SYSTEM

Base unit    : 4px
All spacing is a multiple of 4px.

Scale: 4 | 8 | 12 | 16 | 20 | 24 | 32 | 40 | 48 | 64 | 80 | 96px

Page padding         : 24px (desktop) | 16px (mobile)
Card padding         : 20–24px
Section gap          : 24–32px
Component gap        : 12–16px
Inline spacing       : 8px

No arbitrary spacing values are permitted.

---

## 5. BORDER RADIUS

Input fields, chips, small badges : 6px
Buttons                           : 6–8px
Cards                             : 10–12px
Modals, drawers, large containers : 12–16px
Avatars, pills, circular elements : 9999px (full round)

---

## 6. SHADOWS

Subtle  (cards at rest)    : 0 2px 8px rgba(15, 23, 42, 0.06)
Medium  (cards on hover)   : 0 4px 12px rgba(15, 23, 42, 0.10)
Strong  (dragged elements) : 0 8px 24px rgba(15, 23, 42, 0.15)
Focus   (input glow)       : 0 0 0 3px rgba(15, 23, 42, 0.15)

---

## 7. COMPONENT SPECIFICATIONS

### Buttons
Height          : 40px (default) | 48px (primary/mobile)
Padding         : 10px vertical / 16px horizontal (default)
Primary state   : Deep Blue background, Pure White text
Hover state     : opacity 0.9 (0.2s ease transition)
Disabled state  : Soft Gray background (#E2E8F0), not-allowed cursor
Loading state   : Replace label text with spinner, keep button disabled
Focus state     : Blue glow ring

### Input Fields
Height          : 40px (default) | 48px (mobile)
Padding         : 10px horizontal
Border          : 1px solid Soft Gray (#E2E8F0) at rest
Focus border    : Deep Blue (#0F172A) + blue glow shadow
Error border    : Muted Red (#EF4444)
Readonly style  : Light Gray background, not-allowed cursor
Label position  : Above input (not placeholder-as-label)
Transition      : 0.2s cubic-bezier(0.4, 0, 0.2, 1)

### Cards
Background      : Pure White
Border radius   : 10–12px
Shadow          : Subtle (2px 8px)
Padding         : 20–24px
Hover shadow    : Medium (4px 12px)
Transition      : 0.2s ease on shadow

### Badges
Padding         : 2px 8px
Border radius   : 4px
Font size       : 11px, font weight 600
Emerald badge   : rgba(16,185,129,0.1) background, #10B981 text
Red badge       : rgba(239,68,68,0.1) background, #EF4444 text
Amber badge     : rgba(245,158,11,0.1) background, #F59E0B text
Gray badge      : Soft Gray background, #64748B text

### Toggle Switch
Dimensions      : 44px wide × 24px tall
Track off       : Soft Gray (#E2E8F0)
Track on        : Deep Blue (#0F172A)
Thumb           : 20px × 20px Pure White circle, 2px from edge
Animation       : transform translateX(20px) over 0.2s ease
Spring physics  : cubic-bezier(0.34, 1.56, 0.64, 1) for iOS feel

### Modals
Backdrop        : rgba(0,0,0,0.4) blur(4px)
Animation in    : slide down from translateY(-20px) + fade in, 0.3s ease
Animation out   : reverse, 0.2s ease
Position        : centered, max-width 480px
Padding         : 32px
Close on        : backdrop click, ESC key, explicit close button

### Drawer (Tenant Directory, Slide-out panels)
Width           : 40% of viewport (desktop) | 100% (mobile)
Animation       : translateX(100%) → translateX(0), 0.35s cubic-bezier(0.16, 1, 0.3, 1)
Backdrop        : rgba(0,0,0,0.3)
Close on        : backdrop click, ESC key

### Toast Notifications
Position        : Bottom center (mobile) | Bottom right (desktop)
Duration        : 3 seconds auto-dismiss
Animation in    : slide up + fade, 0.3s ease
Animation out   : fade, 0.2s ease

---

## 8. LAYOUT SYSTEMS

### Landlord Portal (Desktop)
Pattern         : F-Pattern reading layout
Sidebar         : 260px fixed left, Deep Blue background
Main canvas     : flex:1, Light Gray background, 24px padding
Top metrics row : 3-column CSS Grid, equal width
Lower split     : 2-column CSS Grid, 1fr 1fr
Breakpoints     : Optimized for 1280px+ but functional at 768px+

### Tenant Portal (Mobile-first)
Max width       : 420px centered
Padding         : 16px
Hero card       : 90% screen width, centered
Action buttons  : 3-column grid, 48px minimum height
Stack layout    : Single column, top-to-bottom priority

---

## 9. ANIMATION SYSTEM

### Timing Functions
Default ease        : cubic-bezier(0.4, 0, 0.2, 1)  — Material standard
Spring/bounce       : cubic-bezier(0.34, 1.56, 0.64, 1)  — iOS toggle feel
Drawer entrance     : cubic-bezier(0.16, 1, 0.3, 1)  — Expo out

### Duration Scale
Instant feedback    : 100ms (button press, toggle)
Standard transition : 200ms (hover states, border changes)
Modal/drawer entry  : 300–350ms
Page-level          : 400–600ms

### Named Animations
countUp             : opacity 0→1, translateY 4px→0 — dashboard metrics on load
shake               : translateX oscillation — login error, blocked actions
slideInRight        : translateX(100%)→(0) — drawer open
pulseRed            : box-shadow glow expand and collapse every 3s — expired docs
drawCheck           : SVG path stroke-dashoffset 0→length — payment success
fadeUpReveal        : opacity 0→1, translateY 20px→0 — landing page scroll reveal
numberTicker        : staggered countUp for metric cards

### State Change Animations
Kanban drag         : card tilts 3deg, strong shadow, valid drop zones highlight dashed Deep Blue
Button loading      : spinner replaces label, button width preserved
Toggle activation   : thumb slides with spring physics
Progress bar fill   : width expands smoothly as checkboxes tick

---

## 10. UX PRINCIPLES

### 10.1 Affordance
Every interactive element must look like what it does.
Disabled elements must look disabled (gray, not-allowed cursor, tooltip).
Readonly fields must look uneditable (gray background, lock icon where appropriate).

### 10.2 Progressive Disclosure
Show only what the user needs at the current step.
Tenant Dashboard: 3 action buttons — not all 11 pages.
Lease creation: invite step appears only after basic details are valid.
Inspection: room details reveal only when accordion expands.

### 10.3 Optimistic UI
Update the UI immediately on user action.
Roll back with explanation if the server rejects the change.
Applied to: chat messages, Kanban drag, notification read state.

### 10.4 Error States
Every form has three states: Default, Active (focus), Error.
Error messages appear below the relevant field — never as alerts.
Error messages are specific ("Lease dates overlap with Unit 2A: Jan–Mar") not generic.
Submit button disables on error state.

### 10.5 Empty States
Every list, table, and feed has a designed empty state.
Empty state includes an icon, a message, and a primary action.
No blank white spaces — every empty UI communicates something.

### 10.6 Loading States
Every async operation has a loading state.
Skeleton screens for data-heavy pages (dashboard, invoice table).
Spinner in button for form submissions.
Never leave the user wondering if something happened.
```

---

# FILE 6 — `system_design.md`

```md
# ⚙️ system_design.md
# Rent & Lease Management System — System Design Decisions
# Patterns | Trade-offs | Data Flow | Key Design Choices

---

## 1. AUTHENTICATION DESIGN

### Decision: JWT (JSON Web Tokens)
Rationale:
- Stateless — no server-side session storage required
- Scalable — any server in a load-balanced environment can verify any token
- Self-contained — token carries user ID and role, reducing database lookups per request
- Industry standard for REST API authentication

Rules:
- Tokens expire after 24 hours
- Token payload contains: user_id, role, iat (issued at), exp (expiry)
- Token is verified on every request by Authentication Middleware
- Token is stored in memory (JavaScript variable) — never in localStorage (XSS risk)
- Token is sent via Authorization: Bearer header — never in URL parameters

### Password Reset Design
- One-time token generated using cryptographically secure random bytes
- Token hashed before storage — plain token is sent in email, hash stored in DB
- Token expires after exactly 15 minutes
- Token is invalidated immediately upon use — cannot be reused
- Old reset tokens are purged on new request generation

---

## 2. REAL-TIME DESIGN

### Decision: WebSockets for Chat and Notifications
Rationale:
- REST is request-response — unsuitable for push-based real-time delivery
- WebSockets maintain a persistent bidirectional connection
- Message latency under 100ms vs 300-500ms for polling approaches

### Chat Architecture
- One conversation record per unique Landlord-Tenant pair
- Messages reference conversation_id, sender_id, content, timestamp
- File attachments: stored in file system, message stores the file path reference
- History loaded via REST on thread open (last 50 messages, paginated)
- New messages pushed via WebSocket — no polling

### Notification Architecture
- Notifications generated by server-side events (payment processed, ticket updated)
- Pushed to connected user's WebSocket client immediately
- If user is offline, notification is stored in DB and delivered on next connection
- Real-time notification badge count updated via WebSocket push

---

## 3. PAYMENT DESIGN

### Decision: Third-party gateway integration (Stripe / Paystack)
Rationale:
- PCI compliance is the gateway's responsibility, not ours
- Card data never touches our servers
- Tokenization handles card storage securely

### Payment Flow Design
- Frontend sends: invoice_id + payment_method_token (no amount)
- Server retrieves correct amount from database (user cannot modify amount)
- Server sends to gateway: amount, currency, token, idempotency_key
- Gateway processes and returns: success/failure + transaction_id
- Webhook from gateway independently confirms the charge cleared
- Database update happens only after webhook confirmation — not on initial response
- This two-step design prevents false positives and duplicate records

### Idempotency
- Every payment request generates a unique idempotency_key
- Key composed of: user_id + invoice_id + date
- Gateway and our DB both reject duplicate submissions with the same key
- Prevents double-charging from network retries or double-tap

---

## 4. DATABASE DESIGN PATTERNS

### Soft Deletes
Applied to: users, properties, leases, tenants
Mechanism: deleted_at TIMESTAMP column, NULL when active
Queries: all standard queries include WHERE deleted_at IS NULL
Rationale: preserves historical data integrity, audit trail, financial records

### Append-Only Tables
Applied to: audit_log, transactions
Mechanism: no UPDATE or DELETE operations allowed on these tables
Rationale: immutable financial and security records

### UTC Timestamps
All created_at, updated_at, event timestamps stored in UTC
Conversion to user timezone handled at display layer (JavaScript)
Rationale: consistent across timezones, no DST corruption

### Optimistic Locking (Concurrent Updates)
Applied to: maintenance_tickets (Kanban drag)
Mechanism: version column incremented on each update
Write includes: WHERE id = ? AND version = [read version]
On mismatch: reject write, return conflict error, show user fresh data

---

## 5. CRON JOB DESIGN

### Toggleable Automation
Landlord can enable/disable each automation independently
State stored in automation_settings table per landlord
Scheduler reads state before execution — skips if disabled
State change takes effect on next scheduled run

### Retry Logic
Failed jobs retry up to 3 times with exponential backoff
Failure logged to cron_jobs table with error detail
After 3 failures, alert is logged (not emailed — email may be the failure cause)

### Late Fee Application
Runs nightly at 00:05 UTC (after midnight in most target timezones)
Selects: invoices WHERE status='Outstanding' AND due_date < TODAY AND late_fee_applied = FALSE
Applies 5% of lease.monthly_rent as new fee record
Updates invoice total
Sets late_fee_applied = TRUE flag (prevents double application)

---

## 6. DOCUMENT STORAGE DESIGN

### Decision: File system storage, database stores metadata
Rationale:
- Storing binary files in SQL databases bloats the database
- Slows all non-file queries
- Increases backup size disproportionately
- File system or object storage is designed for binary data

### IDOR Protection on Downloads
Every download request:
1. Extracts requester user_id from verified JWT
2. Queries: SELECT owner_id FROM documents WHERE id = ?
3. Compares: requester user_id == document owner_id
4. If mismatch: 403 response, event logged to audit_log
5. If match: stream file from file system with appropriate headers

---

## 7. RATE LIMITING DESIGN

Two-tier approach:

Tier 1 — Middleware (Broad protection)
Applies to: all routes
Limit: 200 requests per minute per IP
Blocked response: 429 with retry-after header

Tier 2 — API Endpoint (Precise protection)
Applies to: specific sensitive endpoints
Login: 10 attempts per 15 minutes per IP
Payment: 3 attempts per 5 minutes per authenticated user
Registration: 5 attempts per hour per IP
Document upload: 20 per hour per user
Chat: 60 messages per minute per user

---

## 8. IDOR PREVENTION DESIGN

Applied at two levels:

Level 1 — Middleware (General pattern)
Reads resource_id from request, queries owner, compares to JWT user_id
Blocks with 403 if mismatch
Logs event to audit_log

Level 2 — Query Level (Specific enforcement)
Every data retrieval query for user-owned resources includes:
WHERE resource.owner_id = [authenticated user id from JWT]
Even if Middleware is bypassed (defense in depth), the query returns no data
A resource that doesn't belong to the requester is invisible at the data level

---

## 9. ANALYTICS DESIGN

### Caching Strategy
Analytics queries are expensive (GROUP BY across large transaction tables)
Cache computed results for 5 minutes per Landlord
On cache hit: return cached JSON immediately
On cache miss: run aggregation query, store result, return to client
Cache invalidated on new payment record for that Landlord

### Chart.js Data Contract
API returns data in the exact shape Chart.js expects
Frontend passes data directly to Chart.js — no frontend transformation
This means if chart library changes, only the API response format changes
```

---

# FILE 7 — `security.md`

```md
# 🔒 security.md
# Rent & Lease Management System — Security Architecture
# All Security Rules, Policies, Protections, and Threat Mitigations

---

## 1. SECURITY PHILOSOPHY

Security is not a feature. It is an architecture decision made at the start.
Every layer enforces its own security independently (Defence in Depth).
No layer trusts the previous layer to have already handled security.
The frontend is entirely untrusted. Every validation there is for UX only.

---

## 2. AUTHENTICATION SECURITY

### JWT Token Security
- Algorithm      : HS256 minimum, RS256 preferred in production
- Secret         : Stored in environment variable — never in source code
- Expiry         : 24 hours
- Storage        : Memory (JavaScript variable) — never localStorage or sessionStorage
  Rationale      : localStorage is accessible to any JavaScript on the page (XSS attack)
- Transmission   : Authorization: Bearer header only — never URL parameters
  Rationale      : URL parameters appear in server logs and browser history
- Verification   : Signature verified cryptographically on every request by Middleware
- Tampering      : Any modification to payload or signature invalidates the token entirely

### Password Security
- Algorithm      : bcrypt with work factor 12
- Storage        : Only the hash is ever stored — plain text is never written anywhere
- Reset tokens   : Cryptographically random, hashed before storage, 15-minute TTL
- Minimum length : 8 characters enforced at API boundary
- Brute force    : Rate limiting on login endpoint (10 attempts / 15 min per IP)

---

## 3. AUTHORIZATION & IDOR PREVENTION

### The IDOR Threat
Insecure Direct Object Reference: A user guesses or obtains the ID of another user's resource
(lease, invoice, document, chat message) and accesses it by constructing the URL directly.

### Defense Layer 1 — Authorization Middleware
Every request to a resource endpoint extracts the resource ID from the request.
Middleware queries the database for the resource's owner_id.
Compares owner_id to the authenticated user's ID from the JWT.
If mismatch: returns 403, logs the event to audit_log with full details.
The API route never executes.

### Defense Layer 2 — Query-Level Scoping
Every SELECT, UPDATE, DELETE query for user-owned resources includes:
WHERE [resource].owner_id = [JWT user_id]
This means even if Middleware is bypassed (compromised or misconfigured),
the database query returns empty results for any resource not owned by the requester.
Zero data is leaked. Defense in depth at the data layer.

### Defense Layer 3 — Response Scrubbing
API responses never include fields that expose other users' identifiers.
password_hash is never included in any API response, ever.
Full tokens are never returned after creation.

---

## 4. INPUT VALIDATION & INJECTION PREVENTION

### SQL Injection Prevention
All SQL queries use parameterized statements / prepared statements.
User input is always a parameter placeholder — never concatenated into SQL strings.
This makes SQL injection categorically impossible at the query level.
Applied to: every SELECT, INSERT, UPDATE, DELETE in the system.

### XSS (Cross-Site Scripting) Prevention
All user-generated content is HTML-escaped before rendering in the browser.
Content Security Policy header restricts which scripts can execute.
Script sources are whitelisted — inline scripts from user data cannot execute.
No use of innerHTML with user content — textContent or escaped HTML only.

### CSRF Prevention
All state-changing forms include a CSRF token hidden field.
Token is generated server-side, stored in session, validated on every POST/PUT/DELETE.
Token is cryptographically random, unique per session.
On mismatch: request rejected with 403.

### File Upload Security
File type validated by extension AND MIME type AND file content (magic bytes).
Dangerous extensions rejected: .php, .py, .exe, .sh, .js (server-side)
Maximum file size enforced: configurable, default 10MB per upload.
Files stored outside the web root — cannot be directly accessed via URL.
Files served through the authenticated download endpoint only.

---

## 5. TRANSPORT SECURITY

### HTTPS
All production traffic served over HTTPS/TLS.
HTTP requests automatically redirected to HTTPS (301 permanent).
HTTP Strict Transport Security (HSTS) header enforced:
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

### Security Headers (applied by Middleware to every response)
X-Frame-Options: DENY
  Prevents embedding in iframes (clickjacking attack prevention)

X-Content-Type-Options: nosniff
  Prevents MIME type sniffing (browser cannot interpret a file as a different type)

X-XSS-Protection: 1; mode=block
  Legacy browsers XSS filter

Referrer-Policy: strict-origin-when-cross-origin
  Controls what referrer information is sent with requests

Permissions-Policy: geolocation=(), microphone=(), camera=()
  Restricts access to browser APIs the system does not use

Content-Security-Policy:
  default-src 'self';
  script-src 'self';
  style-src 'self' 'unsafe-inline';
  font-src 'self';
  img-src 'self' data:;
  connect-src 'self' wss://[websocket-domain];

---

## 6. RATE LIMITING

### Purpose
Prevents: brute force attacks, credential stuffing, payment fraud, DoS, API abuse

### Tier 1 — Middleware (Broad)
All routes: 200 requests per minute per IP
Response: 429 Too Many Requests
Headers returned: Retry-After: [seconds]

### Tier 2 — API Endpoint (Specific)
POST /api/auth/login           : 10 per 15 minutes per IP
POST /api/auth/register        : 5 per hour per IP
POST /api/auth/forgot-password : 3 per hour per email
POST /api/payments/submit      : 3 per 5 minutes per authenticated user
POST /api/documents/upload     : 20 per hour per authenticated user
POST /api/maintenance/tickets  : 10 per hour per authenticated user

---

## 7. AUDIT LOGGING

### What Is Logged
Every authentication event (login, logout, failed login, token refresh)
Every authorization failure (403 responses with resource ID and requester ID)
Every payment event (initiated, succeeded, failed, webhook received)
Every lease event (created, modified, invited, renewed)
Every document event (uploaded, downloaded, deleted)
Every admin-level toggle change (cron job settings)
Every rate limit block (IP, endpoint, timestamp)

### Audit Log Rules
Append-only: no UPDATE or DELETE operations on audit_log table
Every record is immutable after INSERT
Contains: event_type, user_id, resource_type, resource_id, ip_address, user_agent, timestamp (UTC), result
Retained: minimum 2 years
Access: server-side only — no API endpoint exposes raw audit logs to users

---

## 8. SENSITIVE DATA HANDLING

### Never Stored
- Plain text passwords (bcrypt hash only)
- Full payment card numbers (tokenized by gateway)
- CVV numbers (never)
- Full government ID content (only file path to encrypted document)

### Never Returned in API Responses
- password_hash field
- JWT secret key
- Reset token plain text (hash only in DB, plain text sent in email once)
- Other users' personal data

### Environment Variables (Never in Source Code)
- DATABASE_URL
- JWT_SECRET_KEY
- PAYMENT_GATEWAY_API_KEY
- SMTP_PASSWORD
- WEBSOCKET_SECRET

---

## 9. ERROR HANDLING SECURITY

### User-Facing Messages
Generic: "Something went wrong. Please try again."
Authentication: "Invalid email or password." (never specify which is wrong)
Rate limit: "Too many requests. Try again in [N] seconds."
Forbidden: "You do not have permission to access this resource."
Not Found: "The requested page does not exist."

### Server Logs
Full stack trace
Full error message
SQL query that failed (without user data values)
User ID and endpoint (for context)
Timestamp

### Rule: Zero stack traces in browser
Debug mode is disabled in production.
All unhandled exceptions are caught and return generic 500 response.
No framework error pages exposed to users.

---

## 10. OWASP TOP 10 COMPLIANCE STATUS

A01 Broken Access Control      : MITIGATED — IDOR middleware + query-level scoping
A02 Cryptographic Failures     : MITIGATED — HTTPS, bcrypt, hashed tokens, no plain text secrets
A03 Injection                  : MITIGATED — 100% parameterized queries, input validation
A04 Insecure Design            : MITIGATED — Security designed into architecture from start
A05 Security Misconfiguration  : MITIGATED — Security headers, debug off, secrets in env
A06 Vulnerable Components      : ONGOING — Dependencies updated regularly
A07 Auth Failures              : MITIGATED — JWT, bcrypt, rate limits, short TTL tokens
A08 Software Integrity         : MITIGATED — Dependency verification in CI/CD
A09 Logging Failures           : MITIGATED — Audit log, request logging, immutable records
A10 SSRF                       : MITIGATED — No server-side URL fetch from user input
```

---

# FILE 8 — `risk_management.md`

```md
# ⚠️ risk_management.md
# Rent & Lease Management System — Risk Management Document
# All Identified Risks | Likelihood | Impact | Mitigation | Contingency

---

## 1. RISK ASSESSMENT FRAMEWORK

Likelihood : LOW | MEDIUM | HIGH
Impact     : LOW | MEDIUM | HIGH | CRITICAL
Priority   : Likelihood × Impact (1–9 scale)

---

## 2. TECHNICAL RISKS

---

### RISK-T01 — SQL Injection Attack
Likelihood : LOW (if parameterized queries are enforced)
Impact     : CRITICAL (full database access, data destruction)
Priority   : HIGH

Description:
An attacker submits malicious SQL syntax through any input field, form, or URL parameter,
causing the database to execute arbitrary commands.

Mitigation:
- 100% parameterized queries — no string concatenation in any SQL query
- Input validation at API boundary before data reaches any query
- Database user has minimum required permissions (no DROP TABLE access)

Contingency:
- Immediate incident response: revoke database credentials, restore from backup
- Audit all data for corruption
- Notify affected users per data breach protocol

---

### RISK-T02 — JWT Token Compromise
Likelihood : LOW (if stored correctly)
Impact     : HIGH (unauthorized access to user accounts)
Priority   : MEDIUM

Description:
A JWT token is stolen from localStorage (XSS attack) or intercepted in transit (HTTPS failure),
allowing an attacker to impersonate a user.

Mitigation:
- Tokens stored in memory only — never localStorage or sessionStorage
- HTTPS enforced on all production traffic
- Short 24-hour token expiry
- Token secret stored in environment variable only

Contingency:
- Rotate JWT secret key (invalidates all active tokens, forces re-login)
- Notify affected user to change password
- Log and audit all activity under the compromised token

---

### RISK-T03 — Double Payment Processing
Likelihood : MEDIUM (network issues are common)
Impact     : HIGH (financial loss, trust damage, legal risk)
Priority   : HIGH

Description:
A user submits a payment, network drops, user resubmits, both requests reach the gateway
and result in double charges.

Mitigation:
- Idempotency keys on all payment requests
- Submit button disabled after first tap
- Gateway-level duplicate detection
- Database unique constraint on (invoice_id, gateway_transaction_id)

Contingency:
- Automatic refund of duplicate charge via gateway API
- Notification to both Landlord and Tenant
- Manual audit of all transactions within the incident window

---

### RISK-T04 — WebSocket Connection Failure (Chat Disruption)
Likelihood : MEDIUM (network conditions vary)
Impact     : MEDIUM (communication disruption, messages lost)
Priority   : MEDIUM

Description:
WebSocket connection drops, user continues typing and sending messages,
messages are lost because no reconnection or queuing exists.

Mitigation:
- Auto-reconnection logic with exponential backoff
- Unsent messages queued locally and retried on reconnect
- Online/offline indicator in chat UI so users know the connection status
- All messages persisted to database on server receipt

Contingency:
- Users can reload to re-establish connection
- Message history is always available from database on reconnect

---

### RISK-T05 — Cron Job Duplicate Late Fee Application
Likelihood : LOW (with proper flag tracking)
Impact     : HIGH (financial error, Tenant complaints, trust damage)
Priority   : MEDIUM

Description:
The nightly late fee cron job runs twice (server restart mid-execution, scheduler misconfiguration),
applying 5% late fees twice to the same invoices.

Mitigation:
- late_fee_applied BOOLEAN column on invoices table — checked before applying
- Cron job skips any invoice where late_fee_applied = TRUE
- Idempotent by design — running twice produces same result as once
- Scheduler configured with distributed lock (only one instance runs per job)

Contingency:
- Detect via analytics anomaly (double fees in same night)
- Script to identify and reverse duplicate fee applications
- Notify affected tenants

---

### RISK-T06 — File System Storage Failure (Document Vault)
Likelihood : LOW (with redundant storage)
Impact     : HIGH (Lease documents, compliance files lost)
Priority   : MEDIUM

Description:
The server file system fails or is corrupted, losing all uploaded documents while
database records still exist pointing to non-existent files.

Mitigation:
- Production file storage on cloud object storage (S3-compatible) rather than local disk
- Regular automated backups of file storage
- Database records include file hash for integrity verification

Contingency:
- Restore from backup
- Notify affected Landlords to re-upload critical documents
- Provide UI for broken file link detection and re-upload

---

## 3. BUSINESS RISKS

---

### RISK-B01 — Tenant Data Privacy Breach
Likelihood : LOW (with all security measures)
Impact     : CRITICAL (legal liability, regulatory fines, trust destruction)
Priority   : HIGH

Description:
Tenant personal data (name, address, payment history, government ID) is exposed
through a security vulnerability or data breach.

Mitigation:
- IDOR protection at all levels
- Sensitive files stored outside web root
- Minimum data exposure in API responses
- bcrypt for passwords, tokenization for payment data

Contingency:
- Incident response team activated within 1 hour
- Affected users notified within 24 hours
- Regulatory authority notified within 72 hours (GDPR requirement where applicable)
- Full security audit before service restoration

---

### RISK-B02 — Landlord Disputes Late Fee Application
Likelihood : MEDIUM (business reality)
Impact     : LOW (manageable if audit trail exists)
Priority   : LOW

Description:
A Tenant disputes a late fee, claiming it was applied incorrectly.
Without an audit trail, it becomes a "he said / she said" dispute.

Mitigation:
- Immutable audit_log records every fee application with timestamp, invoice ID, amount, calculation
- Tenant receives email notification when fee is applied (with date and calculation)
- Landlord cron job toggle provides explicit control and accountability

Contingency:
- Present audit log to resolve dispute
- Landlord can manually reverse fee via Expense & ROI Ledger

---

### RISK-B03 — Payment Gateway Downtime
Likelihood : LOW (major gateways have 99.9%+ uptime)
Impact     : HIGH (tenants cannot pay rent during downtime)
Priority   : MEDIUM

Description:
Stripe or Paystack experiences an outage, preventing all rent payments.

Mitigation:
- Graceful degradation — system remains functional, only payment fails
- Clear user message: "Payment processing temporarily unavailable. Your payment is not due now."
- Landlord offline payment recording allows manual recording of cash payments

Contingency:
- Monitor gateway status page
- Notify affected tenants proactively
- Process backlog of payments when gateway restores

---

## 4. PROJECT DELIVERY RISKS

---

### RISK-P01 — Scope Creep
Likelihood : HIGH (common in student/team projects)
Impact     : MEDIUM (delayed delivery, incomplete features)
Priority   : HIGH

Description:
New feature ideas are added during development, delaying delivery of core features.

Mitigation:
- prd.md defines the fixed scope — all new requests evaluated against out-of-scope list
- Weekly review: are we on the Phase plan from plan.md?
- Any new feature request deferred to a post-MVP backlog document

---

### RISK-P02 — Database Schema Changes Mid-Development
Likelihood : MEDIUM
Impact     : HIGH (requires refactoring multiple layers)
Priority   : HIGH

Description:
A fundamental schema change is discovered mid-build, requiring rewrites in business logic,
API responses, and frontend display.

Mitigation:
- Database schema reviewed and signed off before Phase 1 begins
- Schema changes after Phase 1 require formal decision with impact analysis
- All schema is in database.sql — single source of truth

---

### RISK-P03 — Real-Time Features Complexity Underestimated
Likelihood : MEDIUM
Impact     : MEDIUM (chat and notifications may be delayed)
Priority   : MEDIUM

Description:
WebSocket implementation is more complex than anticipated, delaying Phase 5.

Mitigation:
- Chat is scheduled in Phase 5 (Week 10) with dedicated focus
- Fallback plan: implement polling (every 3 seconds) as temporary substitute
- Core system (payments, leases, maintenance) does not depend on real-time features

Contingency:
- Deploy polling-based notifications as MVP, upgrade to WebSockets post-deadline

---

## 5. RISK REGISTER SUMMARY

| ID        | Risk                            | Likelihood | Impact   | Priority | Status  |
|---|---|---|---|---|---|
| RISK-T01  | SQL Injection                   | LOW        | CRITICAL | HIGH     | MITIGATED |
| RISK-T02  | JWT Token Compromise            | LOW        | HIGH     | MEDIUM   | MITIGATED |
| RISK-T03  | Double Payment Processing       | MEDIUM     | HIGH     | HIGH     | MITIGATED |
| RISK-T04  | WebSocket Failure               | MEDIUM     | MEDIUM   | MEDIUM   | MITIGATED |
| RISK-T05  | Duplicate Late Fee              | LOW        | HIGH     | MEDIUM   | MITIGATED |
| RISK-T06  | File Storage Failure            | LOW        | HIGH     | MEDIUM   | MONITORING |
| RISK-B01  | Tenant Data Breach              | LOW        | CRITICAL | HIGH     | MITIGATED |
| RISK-B02  | Late Fee Dispute                | MEDIUM     | LOW      | LOW      | MITIGATED |
| RISK-B03  | Payment Gateway Downtime        | LOW        | HIGH     | MEDIUM   | MONITORING |
| RISK-P01  | Scope Creep                     | HIGH       | MEDIUM   | HIGH     | ACTIVE CONTROL |
| RISK-P02  | Schema Changes Mid-Dev          | MEDIUM     | HIGH     | HIGH     | ACTIVE CONTROL |
| RISK-P03  | Real-Time Complexity            | MEDIUM     | MEDIUM   | MEDIUM   | MONITORING |
```

---

# FILE 9 — `implementation_plan.md`

```md
# 🛠️ implementation_plan.md
# Rent & Lease Management System — Implementation Plan
# Build Order | Dependencies | Integration Points | Verification Gates

---

## 1. THE GOLDEN RULE OF BUILD ORDER

Never build a feature before its foundation is in place.
The correct build order is:
Database Schema → Security Layer → Authentication → Core CRUD → Advanced Features → Real-Time → Automation

Every phase depends on everything before it being correct and tested.
A broken authentication layer makes every feature built on top of it insecure.

---

## 2. PHASE BUILD ORDER WITH DEPENDENCIES

### PHASE 0 — FOUNDATION
Build order:
1. All .md documentation files
2. Database schema (all tables, all constraints, all indexes)
3. Design system (CSS variables, base components)
4. Base HTML templates (layout_landlord, layout_tenant, layout_auth)
5. Environment configuration
6. Project folder structure
7. Git repository + .gitignore

No dependencies — this is the dependency for everything else.

---

### PHASE 1 — SECURITY PERIMETER
Build order:
1. Security Headers Middleware (runs first on every request)
2. CORS Middleware
3. Request Logging Middleware + audit_log table
4. Rate Limiting Middleware (broad)
5. Authentication Middleware (JWT verification)
6. Authorization Middleware (IDOR base check)
7. Login API endpoint + login page
8. Registration API endpoint + registration page
9. Email verification flow
10. Password reset flow (forgot + reset pages)
11. Lease Invitation Gateway

Dependencies: Phase 0 complete
Verification Gate: Can register, verify email, log in, receive JWT, hit protected route

---

### PHASE 2 — LANDLORD CORE
Build order:
1. Landlord Dashboard page + API endpoint (GET /api/landlord/dashboard)
2. Property Portfolio page + CRUD endpoints + properties table
3. Building management + buildings table
4. Leases page + lease creation + overlap validation
5. Tenant invitation within lease creation
6. Tenant Directory + slide-out drawer
7. Financials page + invoice table
8. Expense ledger + ROI calculator

Dependencies: Phase 1 complete (authenticated routes)
Verification Gate: Landlord can add property → create lease → invite tenant → view financials

---

### PHASE 3 — TENANT CORE
Build order:
1. Tenant Dashboard + hero card (reads from invoices table)
2. Rent Payment page + payment gateway integration
3. Payment webhook endpoint
4. Payment Success + Cancelled pages
5. My Lease page (reads from leases + documents tables)
6. Payment Methods + Auto-Pay toggle
7. Profile & Settings (locked email)
8. Compliance document upload

Dependencies: Phase 2 complete (leases and invoices must exist for tenants to pay)
Verification Gate: Tenant can log in → see balance → pay rent → download receipt

---

### PHASE 4 — MAINTENANCE
Build order:
1. Maintenance tickets table + ticket_comments table
2. Tenant ticket submission endpoint + page
3. Landlord Kanban board + drag-and-drop status update endpoint
4. Priority tag system
5. Follow-up comment system
6. Inspections table + Move-In/Move-Out form
7. Progress calculation logic

Dependencies: Phase 2 + Phase 3 (need active tenants with leases)
Verification Gate: Tenant submits ticket → appears on Kanban → Landlord resolves → Tenant notified

---

### PHASE 5 — REAL-TIME
Build order:
1. WebSocket server setup + authentication
2. Conversation + messages table
3. Chat history REST endpoint
4. Landlord chat UI (two-pane)
5. Tenant chat UI (single thread)
6. Typing indicators + read receipts
7. File attachment support
8. Notifications WebSocket push
9. Notification feed UI (Landlord + Tenant)
10. Notice Board (Landlord publish → Tenant read)

Dependencies: Phase 1 (WebSocket needs JWT auth)
Verification Gate: Landlord sends message → Tenant receives instantly → read receipt updates

---

### PHASE 6 — ANALYTICS + AUTOMATION
Build order:
1. Analytics aggregation queries (revenue by month)
2. Analytics API endpoints + Chart.js integration
3. Cron job infrastructure (scheduler setup)
4. automation_settings table
5. Automation Control Panel UI + toggle endpoints
6. Late fee cron job
7. Lease expiry scanner
8. Rent reminder email cron job
9. Auto-Pay processor

Dependencies: Phase 2 + Phase 3 (need financial data for analytics)
Verification Gate: Analytics charts load with real data, late fee applies correctly overnight

---

### PHASE 7 — DOCUMENTS
Build order:
1. Documents + folders tables
2. Upload endpoint (file validation + storage)
3. IDOR-protected download endpoint
4. Document grid UI
5. Delete with confirmation

Dependencies: Phase 1 (IDOR protection requires auth)
Verification Gate: Upload file → appears in grid → download works → other user cannot download

---

### PHASE 8 — PUBLIC SHELL
Build order:
1. Landing page (hero, features, CTAs)
2. Sticky navbar scroll behavior
3. Scroll reveal animations
4. All error pages (403, 429, 404, 503)

Dependencies: Design system complete
Verification Gate: Visitor lands → reads value proposition → clicks Get Started → reaches registration

---

### PHASE 9 — TESTING
Verification tests:
- Authentication: all invalid token scenarios return 401
- Authorization: all IDOR scenarios return 403 and log to audit
- Rate limiting: all limits trigger 429 at correct thresholds
- SQL: all parameterized queries verified (no string concatenation)
- XSS: all user input escaped in output
- CSRF: all form submissions validated
- Payments: idempotency tested, double-tap prevented
- Cron jobs: all automations run without duplicates
- Mobile: all Tenant pages tested at 375px viewport
- Performance: all pages under 3 seconds load time

---

### PHASE 10 — FINAL DELIVERY
Checklist:
- All 38 pages functional and tested
- All animations and transitions complete
- All empty states and loading states implemented
- All .md documentation files current and accurate
- Staging deployment verified
- Demo walkthrough prepared and rehearsed

---

## 3. INTEGRATION POINTS

| Component | Integrates With | Protocol | Authentication |
|---|---|---|---|
| Frontend | Python API | HTTP REST | JWT in Authorization header |
| Frontend | Python WebSocket | WebSocket | JWT on connect |
| Python API | Payment Gateway | HTTPS REST | API Key (env var) |
| Payment Gateway | Python API | HTTPS Webhook | Webhook signature |
| Python Scheduler | Python Business Logic | Internal call | Server-side |
| Python Backend | SMTP Email Service | SMTP | Credentials (env var) |
| Python Backend | File System / Object Storage | Local / S3 API | Credentials (env var) |

---

## 4. VERIFICATION GATES SUMMARY

| Phase | Gate Description |
|---|---|
| 0 | Project scaffolding functional, schema created |
| 1 | Register → verify → login → protected route → logout |
| 2 | Landlord full property + lease + financial workflow |
| 3 | Tenant full payment workflow with receipt |
| 4 | Full maintenance ticket lifecycle |
| 5 | Real-time chat with read receipts |
| 6 | Analytics load with data, cron job applies fee correctly |
| 7 | Document upload, display, download, IDOR block |
| 8 | Landing page to registration flow complete |
| 9 | All security tests pass |
| 10 | All 38 pages verified, staging deployed |
```

---

# FILE 10 — `file_structure.md`

```md
# 📁 file_structure.md
# Rent & Lease Management System — Project File Structure
# Every file and folder and what it owns

---

rent-lease-management/
│
├── .env                          # Environment variables (NEVER committed to git)
├── .env.example                  # Template showing required vars (committed, no values)
├── .gitignore                    # Excludes .env, __pycache__, uploads, logs
├── requirements.txt              # Python dependencies
│
├── docs/                         # All .md documentation files
│   ├── AI_rules.md
│   ├── plan.md
│   ├── prd.md
│   ├── architecture.md
│   ├── design.md
│   ├── system_design.md
│   ├── security.md
│   ├── risk_management.md
│   ├── implementation_plan.md
│   ├── file_structure.md
│   ├── naming_patterns.md
│   ├── tech_stack.md
│   └── database_schema.sql
│
├── frontend/                     # All HTML, CSS, JavaScript
│   │
│   ├── templates/                # HTML page files
│   │   ├── base/
│   │   │   ├── layout_landlord.html     # Sidebar + main content wrapper
│   │   │   ├── layout_tenant.html       # Mobile wrapper + bottom nav
│   │   │   └── layout_auth.html         # Centered card wrapper
│   │   │
│   │   ├── landlord/
│   │   │   ├── dashboard.html
│   │   │   ├── properties.html
│   │   │   ├── leases.html
│   │   │   ├── financials.html
│   │   │   ├── chat.html
│   │   │   ├── maintenance.html
│   │   │   ├── tenants.html
│   │   │   ├── documents.html
│   │   │   ├── analytics.html
│   │   │   ├── notifications.html
│   │   │   ├── settings.html
│   │   │   ├── expenses.html
│   │   │   ├── buildings.html
│   │   │   └── automations.html
│   │   │
│   │   ├── tenant/
│   │   │   ├── dashboard.html
│   │   │   ├── payments.html
│   │   │   ├── lease.html
│   │   │   ├── maintenance.html
│   │   │   ├── chat.html
│   │   │   ├── inspection.html
│   │   │   ├── payment_methods.html
│   │   │   ├── notice_board.html
│   │   │   ├── compliance.html
│   │   │   ├── profile.html
│   │   │   └── history.html
│   │   │
│   │   └── public/
│   │       ├── landing.html
│   │       ├── register.html
│   │       ├── login.html
│   │       ├── invite.html
│   │       ├── verify_email.html
│   │       ├── forgot_password.html
│   │       ├── reset_password.html
│   │       ├── payment_success.html
│   │       ├── payment_cancelled.html
│   │       ├── 403.html
│   │       ├── 429.html
│   │       ├── 404.html
│   │       └── 503.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── design_system.css         # All tokens, variables, base components
│   │   │   ├── layout_landlord.css       # Sidebar, F-pattern grid
│   │   │   ├── layout_tenant.css         # Mobile-first, single column
│   │   │   ├── animations.css            # All keyframes and transitions
│   │   │   └── components/
│   │   │       ├── buttons.css
│   │   │       ├── cards.css
│   │   │       ├── inputs.css
│   │   │       ├── badges.css
│   │   │       ├── modals.css
│   │   │       ├── drawers.css
│   │   │       ├── toggles.css
│   │   │       ├── kanban.css
│   │   │       ├── chat.css
│   │   │       └── charts.css
│   │   │
│   │   └── js/
│   │       ├── core/
│   │       │   ├── api.js               # All fetch() wrapper functions
│   │       │   ├── auth.js              # JWT token management (in memory)
│   │       │   ├── websocket.js         # WebSocket client + reconnection
│   │       │   └── utils.js             # Shared utility functions
│   │       │
│   │       ├── pages/
│   │       │   ├── landlord_dashboard.js
│   │       │   ├── landlord_properties.js
│   │       │   ├── landlord_leases.js
│   │       │   ├── landlord_financials.js
│   │       │   ├── landlord_chat.js
│   │       │   ├── landlord_maintenance.js
│   │       │   ├── landlord_analytics.js
│   │       │   ├── tenant_dashboard.js
│   │       │   ├── tenant_payments.js
│   │       │   ├── tenant_maintenance.js
│   │       │   ├── tenant_inspection.js
│   │       │   ├── tenant_chat.js
│   │       │   └── auth_forms.js
│   │       │
│   │       └── components/
│   │           ├── modal.js
│   │           ├── drawer.js
│   │           ├── kanban_drag.js
│   │           ├── toast.js
│   │           ├── file_upload.js
│   │           └── charts.js
│
├── backend/                      # All Python server code
│   │
│   ├── app.py                    # Application entry point
│   ├── config.py                 # Configuration loaded from environment variables
│   │
│   ├── middleware/               # All middleware functions
│   │   ├── security_headers.py
│   │   ├── cors.py
│   │   ├── request_logging.py
│   │   ├── rate_limiter.py
│   │   ├── authentication.py
│   │   └── authorization.py
│   │
│   ├── api/                      # All API route handlers
│   │   ├── auth_routes.py
│   │   ├── property_routes.py
│   │   ├── lease_routes.py
│   │   ├── financial_routes.py
│   │   ├── maintenance_routes.py
│   │   ├── chat_routes.py
│   │   ├── document_routes.py
│   │   ├── analytics_routes.py
│   │   ├── notification_routes.py
│   │   └── automation_routes.py
│   │
│   ├── business_rules/           # All constraint enforcement
│   │   ├── property_rules.py
│   │   ├── lease_rules.py
│   │   ├── payment_rules.py
│   │   ├── maintenance_rules.py
│   │   └── document_rules.py
│   │
│   ├── business_logic/           # All process orchestration
│   │   ├── auth_logic.py
│   │   ├── property_logic.py
│   │   ├── lease_logic.py
│   │   ├── payment_logic.py
│   │   ├── maintenance_logic.py
│   │   ├── chat_logic.py
│   │   ├── document_logic.py
│   │   ├── analytics_logic.py
│   │   └── notification_logic.py
│   │
│   ├── data/                     # All database operations
│   │   ├── connection.py         # Database connection pool
│   │   ├── retrieval/
│   │   │   ├── user_queries.py
│   │   │   ├── property_queries.py
│   │   │   ├── lease_queries.py
│   │   │   ├── financial_queries.py
│   │   │   ├── maintenance_queries.py
│   │   │   ├── chat_queries.py
│   │   │   ├── document_queries.py
│   │   │   └── analytics_queries.py
│   │   └── storage/
│   │       ├── user_writes.py
│   │       ├── property_writes.py
│   │       ├── lease_writes.py
│   │       ├── financial_writes.py
│   │       ├── maintenance_writes.py
│   │       ├── chat_writes.py
│   │       └── document_writes.py
│   │
│   ├── scheduler/                # All cron job definitions
│   │   ├── scheduler.py          # APScheduler setup
│   │   ├── late_fee_job.py
│   │   ├── lease_expiry_job.py
│   │   ├── rent_reminder_job.py
│   │   └── auto_pay_job.py
│   │
│   └── utils/                    # Shared utilities
│       ├── jwt_utils.py
│       ├── email_service.py
│       ├── password_utils.py
│       ├── file_utils.py
│       └── response_utils.py
│
├── database/
│   ├── schema.sql                # Complete database schema
│   ├── seed_data.sql             # Development test data
│   └── migrations/               # Schema change history
│
├── uploads/                      # Uploaded files (outside web root)
│   ├── documents/
│   ├── maintenance_photos/
│   └── compliance_docs/
│
└── logs/
    ├── app.log                   # Application events
    ├── audit.log                 # Security and financial audit events
    └── cron.log                  # Scheduled job execution records
```

---

# FILE 11 — `naming_patterns.md`

```md
# 🏷️ naming_patterns.md
# Rent & Lease Management System — Naming Conventions
# Every naming pattern for every file, function, variable, class, and database object

---

## 1. GENERAL NAMING PRINCIPLES

- Names must be explicit and self-documenting
- No abbreviations except universally accepted ones (id, url, api, jwt, sql, css, js)
- No single-letter variables except loop counters (i, j, k)
- No magic numbers — use named constants
- Names communicate intent — not implementation

---

## 2. PYTHON NAMING

Files             : snake_case          → payment_logic.py, auth_routes.py
Functions         : snake_case          → process_rent_payment(), validate_lease_overlap()
Variables         : snake_case          → monthly_rent, lease_start_date
Constants         : UPPER_SNAKE_CASE    → LATE_FEE_PERCENTAGE, JWT_EXPIRY_HOURS
Classes           : PascalCase          → LeaseManager, PaymentProcessor
Route prefixes    : /api/v1/[domain]    → /api/v1/payments, /api/v1/leases

Function naming pattern:
- Retrieval     : get_[thing]_by_[criteria]   → get_invoice_by_id(), get_leases_by_landlord()
- Storage       : create_[thing](), update_[thing](), delete_[thing]()
- Rules         : validate_[thing]_[constraint] → validate_lease_no_overlap()
- Logic         : process_[action]()           → process_rent_payment()
- Middleware    : check_[concern]()            → check_authentication(), check_rate_limit()

---

## 3. JAVASCRIPT NAMING

Files             : camelCase           → landlordDashboard.js, fileUpload.js
Functions         : camelCase           → submitPayment(), openDrawer(), fetchChatHistory()
Variables         : camelCase           → currentInvoice, isLoading, selectedTenantId
Constants         : UPPER_SNAKE_CASE    → MAX_FILE_SIZE_MB, API_BASE_URL
DOM references    : camelCase + El      → submitBtnEl, balanceCardEl, fileInputEl
Event handlers    : handle[Event][Target] → handleClickPayButton(), handleChangeFileInput()

---

## 4. CSS NAMING (BEM-Inspired)

Block             : [component]         → .card, .modal, .drawer, .kanban-board
Element           : [block]__[element]  → .card__title, .modal__footer, .chat__bubble
Modifier          : [block]--[state]    → .card--overdue, .badge--emerald, .btn--disabled
State classes     : is-[state]          → is-loading, is-active, is-open, is-error
JS hooks          : js-[name]           → js-submit-btn (never style these)

Color utility classes follow design token names:
.text-deep-blue | .bg-light-gray | .border-soft-gray | .text-muted-red

---

## 5. HTML NAMING

IDs               : kebab-case          → balance-card, submit-btn, file-input
Data attributes   : data-[name]         → data-invoice-id, data-tenant-id, data-ticket-status
ARIA labels       : Descriptive phrases → aria-label="Submit rent payment"
Form names        : match API field names exactly → name="first_name", name="monthly_rent"

---

## 6. DATABASE NAMING

Tables            : lowercase_plural    → users, properties, leases, invoices, maintenance_tickets
Columns           : lowercase_snake     → first_name, monthly_rent, created_at, deleted_at
Primary keys      : id (always)         → id INT PRIMARY KEY
Foreign keys      : [table_singular]_id → landlord_id, tenant_id, property_id, invoice_id
Boolean columns   : is_[state] or [verb]ed → is_verified, late_fee_applied, is_active
Timestamp columns : created_at, updated_at, deleted_at, [event]_at → paid_at, resolved_at
Status columns    : status              → status VARCHAR CHECK IN ('Active','Expired','Pending')
Indexes           : idx_[table]_[column] → idx_invoices_tenant_id, idx_leases_property_id
Constraints       : uq_[table]_[column] → uq_users_email, uq_invitations_token

---

## 7. API ENDPOINT NAMING

Pattern           : /api/v[n]/[domain]/[action if needed]
Resources         : nouns, plural        → /properties, /leases, /invoices
Methods communicate action:
  GET    /api/v1/properties             → list all landlord properties
  POST   /api/v1/properties             → create new property
  GET    /api/v1/properties/{id}        → get specific property
  PUT    /api/v1/properties/{id}        → update property
  DELETE /api/v1/properties/{id}        → delete property
  POST   /api/v1/leases/{id}/invite     → invite tenant to lease
  POST   /api/v1/payments/submit        → submit payment
  POST   /api/v1/payments/webhook       → receive gateway webhook

---

## 8. FILE UPLOAD NAMING

Uploaded files stored as: [uuid]_[original_filename_sanitized].[ext]
Example: 7f3a9c1d_lease_agreement_unit_4b.pdf
Purpose: prevents path traversal, filename collisions, and information leakage
Original filename stored in documents.original_filename for display
```

---

# FILE 12 — `tech_stack.md`

```md
# 🔧 tech_stack.md
# Rent & Lease Management System — Technology Stack
# Every technology choice, why it was chosen, and what it owns

---

## 1. FRONTEND

### HTML5
Role      : Structure layer — all 38 pages
Why       : Semantic markup for accessibility and SEO
Version   : HTML5 (semantic elements: article, section, nav, main, aside, header, footer)
Rules     : No inline styles. No inline JavaScript. Only structure and semantics.

### CSS3 (Vanilla)
Role      : Styling layer — design system, layouts, animations, responsive design
Why       : No framework overhead, full control over design system tokens,
            better performance, no dependency risk
Key CSS   : Custom Properties (design tokens), CSS Grid, Flexbox, CSS Animations,
            @keyframes, CSS Transitions, Media Queries, :focus-visible, :is(), :where()
Rules     : All values use design tokens from design.md. No arbitrary values.

### JavaScript (Vanilla ES6+)
Role      : Behavior layer — all user interaction, API communication, WebSocket client
Why       : No framework = no framework lock-in, maximum performance, full understanding
Key APIs  : fetch(), WebSocket, IntersectionObserver, FormData, DragEvent,
            localStorage (config only — never tokens), sessionStorage (never tokens),
            in-memory token storage via module-scoped variables
Rules     : No jQuery. No frameworks. Pure modern JavaScript.
            JWT token stored only in memory — never in localStorage or sessionStorage.

### Chart.js
Role      : Analytics charts (revenue line chart, donut charts)
Why       : Lightweight, well-documented, works with vanilla JS, no framework needed
Scope     : Analytics page only (Landlord Page 9)

---

## 2. BACKEND

### Python 3.11+
Role      : Middleware, API, Business Rules, Business Logic, Schedulers
Why       : Readable, large ecosystem, strong web framework support,
            excellent for data processing and scheduled jobs

### Flask (or FastAPI)
Role      : Web framework — HTTP routing, request/response handling, WebSocket support
Flask     : Simpler, more appropriate for learning context and scope of this project
FastAPI   : Higher performance, built-in async, automatic API documentation
Decision  : Flask for initial build (simpler), FastAPI upgrade path documented

### Flask-SocketIO (or FastAPI WebSockets)
Role      : WebSocket server for real-time chat and notifications
Scope     : Chat (Landlord Page 5, Tenant Page 5), Notifications

### APScheduler
Role      : Background job scheduler for all cron jobs
Scope     : Late fee job, lease expiry scanner, rent reminders, auto-pay processor
Why       : Lightweight, works within Flask process, database-backed job storage

### PyJWT
Role      : JWT token generation and verification
Scope     : Authentication Middleware, token issuance on login

### bcrypt
Role      : Password hashing
Scope     : Registration, password change, password verification on login

### Stripe Python SDK / Paystack API
Role      : Payment gateway integration
Scope     : Tenant payment processing, webhook verification

---

## 3. DATABASE

### PostgreSQL (Production) / SQLite (Development)
Role      : Persistent data store — all 9 data layer operations
PostgreSQL: ACID compliant, production-grade, handles concurrent writes correctly
SQLite    : Zero-configuration for local development and testing

### Connection Pooling
Tool      : psycopg2 with connection pooling (PostgreSQL)
Why       : Reuses database connections — avoids overhead of new connection per request

---

## 4. INFRASTRUCTURE

### SMTP (Email)
Role      : Sending verification emails, password reset, rent reminders, notifications
Provider  : SendGrid (production) / Local SMTP (development)
Scope     : All automated email events in the cron jobs and invitation flow

### File Storage
Development : Local file system (uploads/ directory outside web root)
Production  : S3-compatible object storage (AWS S3, Cloudflare R2, or similar)
Why         : Binary files do not belong in relational databases

### HTTPS / TLS
Provider    : Let's Encrypt (production)
Enforced    : All HTTP redirected to HTTPS
HSTS        : max-age=31536000; includeSubDomains; preload

---

## 5. DEVELOPMENT TOOLS

Git             : Version control (GitHub or GitLab)
.gitignore      : Excludes .env, __pycache__, uploads/, logs/, *.pyc
Postman         : API endpoint testing
Browser DevTools: Frontend debugging, performance profiling
Python venv     : Isolated dependency environment

---

## 6. TECHNOLOGY DECISION SUMMARY

| Technology | Version | Role | Layer |
|---|---|---|---|
| HTML5 | 5 | Page structure | Layer 1 |
| CSS3 | 3 | Visual design + animations | Layer 2 |
| JavaScript | ES2022 | User interaction + API calls | Layer 3 |
| Chart.js | 4.x | Analytics charts | Layer 3 |
| Python | 3.11+ | Backend engine | Layers 4–7 |
| Flask | 3.x | HTTP framework + routing | Layer 5 |
| Flask-SocketIO | 5.x | WebSocket server | Layer 5 |
| APScheduler | 3.x | Background cron jobs | Layer 7 |
| PyJWT | 2.x | JWT operations | Layer 4 |
| bcrypt | 4.x | Password hashing | Layer 7 |
| PostgreSQL | 15+ | Production database | Layers 8–9 |
| SQLite | 3.x | Development database | Layers 8–9 |
| psycopg2 | 2.x | PostgreSQL Python adapter | Layers 8–9 |
| Stripe/Paystack | Latest | Payment processing | Layer 7 |
| SendGrid/SMTP | Latest | Email delivery | Layer 7 |
| S3-compatible | Latest | File storage (production) | Layer 9 |
```

---

# FILE 13 — `database_schema.sql`

```sql
-- database_schema.sql
-- Rent & Lease Management System — Complete Database Schema
-- Every table, every column, every constraint, every index
-- Engine: PostgreSQL | Encoding: UTF-8 | All timestamps: UTC

-- ============================================================
-- USERS
-- ============================================================
CREATE TABLE users (
    id              SERIAL          PRIMARY KEY,
    email           VARCHAR(255)    NOT NULL UNIQUE,
    password_hash   VARCHAR(255)    NOT NULL,
    role            VARCHAR(20)     NOT NULL CHECK (role IN ('landlord', 'tenant')),
    first_name      VARCHAR(100)    NOT NULL,
    last_name       VARCHAR(100)    NOT NULL,
    phone_number    VARCHAR(30),
    is_verified     BOOLEAN         DEFAULT FALSE,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ     DEFAULT NULL
);

CREATE INDEX idx_users_email     ON users (email);
CREATE INDEX idx_users_role      ON users (role);
CREATE INDEX idx_users_deleted   ON users (deleted_at);

-- ============================================================
-- BUILDINGS (Parent groups for multi-unit properties)
-- ============================================================
CREATE TABLE buildings (
    id              SERIAL          PRIMARY KEY,
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    name            VARCHAR(255)    NOT NULL,
    address         TEXT            NOT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ     DEFAULT NULL
);

CREATE INDEX idx_buildings_landlord ON buildings (landlord_id);

-- ============================================================
-- PROPERTIES
-- ============================================================
CREATE TABLE properties (
    id              SERIAL          PRIMARY KEY,
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    building_id     INTEGER         REFERENCES buildings(id),
    unit_number     VARCHAR(50)     NOT NULL,
    address         TEXT            NOT NULL,
    base_rent       DECIMAL(10,2)   NOT NULL CHECK (base_rent > 0),
    status          VARCHAR(20)     DEFAULT 'Vacant' CHECK (status IN ('Vacant', 'Leased')),
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ     DEFAULT NULL
);

CREATE INDEX idx_properties_landlord ON properties (landlord_id);
CREATE INDEX idx_properties_status   ON properties (status);
CREATE INDEX idx_properties_building ON properties (building_id);

-- ============================================================
-- LEASES
-- ============================================================
CREATE TABLE leases (
    id              SERIAL          PRIMARY KEY,
    property_id     INTEGER         NOT NULL REFERENCES properties(id),
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    tenant_id       INTEGER         REFERENCES users(id),
    monthly_rent    DECIMAL(10,2)   NOT NULL CHECK (monthly_rent > 0),
    start_date      DATE            NOT NULL,
    end_date        DATE            NOT NULL,
    status          VARCHAR(20)     DEFAULT 'Pending' CHECK (status IN ('Pending','Active','Expired','Terminated')),
    signed_at       TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ     DEFAULT NULL,
    CONSTRAINT chk_lease_dates CHECK (end_date > start_date)
);

CREATE INDEX idx_leases_property  ON leases (property_id);
CREATE INDEX idx_leases_landlord  ON leases (landlord_id);
CREATE INDEX idx_leases_tenant    ON leases (tenant_id);
CREATE INDEX idx_leases_status    ON leases (status);
CREATE INDEX idx_leases_dates     ON leases (start_date, end_date);

-- ============================================================
-- INVITATIONS
-- ============================================================
CREATE TABLE invitations (
    id              SERIAL          PRIMARY KEY,
    lease_id        INTEGER         NOT NULL REFERENCES leases(id),
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    email           VARCHAR(255)    NOT NULL,
    token_hash      VARCHAR(255)    NOT NULL UNIQUE,
    expires_at      TIMESTAMPTZ     NOT NULL,
    accepted_at     TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_invitations_token   ON invitations (token_hash);
CREATE INDEX idx_invitations_lease   ON invitations (lease_id);

-- ============================================================
-- INVOICES
-- ============================================================
CREATE TABLE invoices (
    id                  SERIAL          PRIMARY KEY,
    lease_id            INTEGER         NOT NULL REFERENCES leases(id),
    tenant_id           INTEGER         NOT NULL REFERENCES users(id),
    property_id         INTEGER         NOT NULL REFERENCES properties(id),
    landlord_id         INTEGER         NOT NULL REFERENCES users(id),
    base_rent           DECIMAL(10,2)   NOT NULL,
    late_fee_amount     DECIMAL(10,2)   DEFAULT 0.00,
    total_amount        DECIMAL(10,2)   NOT NULL,
    due_date            DATE            NOT NULL,
    status              VARCHAR(20)     DEFAULT 'Outstanding' CHECK (status IN ('Outstanding','Paid','Cancelled')),
    late_fee_applied    BOOLEAN         DEFAULT FALSE,
    paid_at             TIMESTAMPTZ     DEFAULT NULL,
    created_at          TIMESTAMPTZ     DEFAULT NOW(),
    updated_at          TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_invoices_tenant    ON invoices (tenant_id);
CREATE INDEX idx_invoices_landlord  ON invoices (landlord_id);
CREATE INDEX idx_invoices_status    ON invoices (status);
CREATE INDEX idx_invoices_due_date  ON invoices (due_date);
CREATE INDEX idx_invoices_lease     ON invoices (lease_id);

-- ============================================================
-- TRANSACTIONS (Append-only — no updates or deletes)
-- ============================================================
CREATE TABLE transactions (
    id                  SERIAL          PRIMARY KEY,
    invoice_id          INTEGER         NOT NULL REFERENCES invoices(id),
    tenant_id           INTEGER         NOT NULL REFERENCES users(id),
    landlord_id         INTEGER         NOT NULL REFERENCES users(id),
    amount              DECIMAL(10,2)   NOT NULL,
    gateway_reference   VARCHAR(255)    NOT NULL UNIQUE,
    payment_method_last4 VARCHAR(4),
    idempotency_key     VARCHAR(255)    NOT NULL UNIQUE,
    created_at          TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_transactions_invoice   ON transactions (invoice_id);
CREATE INDEX idx_transactions_tenant    ON transactions (tenant_id);
CREATE INDEX idx_transactions_landlord  ON transactions (landlord_id);

-- ============================================================
-- EXPENSES
-- ============================================================
CREATE TABLE expenses (
    id              SERIAL          PRIMARY KEY,
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    property_id     INTEGER         NOT NULL REFERENCES properties(id),
    description     VARCHAR(500)    NOT NULL,
    amount          DECIMAL(10,2)   NOT NULL CHECK (amount > 0),
    expense_date    DATE            NOT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_expenses_property  ON expenses (property_id);
CREATE INDEX idx_expenses_landlord  ON expenses (landlord_id);

-- ============================================================
-- PAYMENT METHODS
-- ============================================================
CREATE TABLE payment_methods (
    id              SERIAL          PRIMARY KEY,
    tenant_id       INTEGER         NOT NULL REFERENCES users(id),
    gateway_token   VARCHAR(255)    NOT NULL,
    card_last_four  VARCHAR(4)      NOT NULL,
    card_brand      VARCHAR(50),
    is_default      BOOLEAN         DEFAULT FALSE,
    auto_pay_enabled BOOLEAN        DEFAULT FALSE,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ     DEFAULT NULL
);

CREATE INDEX idx_payment_methods_tenant ON payment_methods (tenant_id);

-- ============================================================
-- MAINTENANCE TICKETS
-- ============================================================
CREATE TABLE maintenance_tickets (
    id              SERIAL          PRIMARY KEY,
    lease_id        INTEGER         NOT NULL REFERENCES leases(id),
    tenant_id       INTEGER         NOT NULL REFERENCES users(id),
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    property_id     INTEGER         NOT NULL REFERENCES properties(id),
    category        VARCHAR(100)    NOT NULL,
    urgency         VARCHAR(20)     NOT NULL CHECK (urgency IN ('Emergency','High','Normal','Low')),
    description     TEXT            NOT NULL,
    status          VARCHAR(20)     DEFAULT 'Pending' CHECK (status IN ('Pending','In Progress','Resolved')),
    version         INTEGER         DEFAULT 1,
    resolved_at     TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_tickets_tenant   ON maintenance_tickets (tenant_id);
CREATE INDEX idx_tickets_landlord ON maintenance_tickets (landlord_id);
CREATE INDEX idx_tickets_status   ON maintenance_tickets (status);

-- ============================================================
-- TICKET COMMENTS
-- ============================================================
CREATE TABLE ticket_comments (
    id              SERIAL          PRIMARY KEY,
    ticket_id       INTEGER         NOT NULL REFERENCES maintenance_tickets(id),
    user_id         INTEGER         NOT NULL REFERENCES users(id),
    comment         TEXT            NOT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_comments_ticket ON ticket_comments (ticket_id);

-- ============================================================
-- INSPECTIONS
-- ============================================================
CREATE TABLE inspections (
    id              SERIAL          PRIMARY KEY,
    lease_id        INTEGER         NOT NULL REFERENCES leases(id),
    tenant_id       INTEGER         NOT NULL REFERENCES users(id),
    type            VARCHAR(20)     NOT NULL CHECK (type IN ('Move-In','Move-Out')),
    checklist_data  JSONB           NOT NULL,
    is_complete     BOOLEAN         DEFAULT FALSE,
    submitted_at    TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_inspections_lease  ON inspections (lease_id);
CREATE INDEX idx_inspections_tenant ON inspections (tenant_id);

-- ============================================================
-- CONVERSATIONS (Chat)
-- ============================================================
CREATE TABLE conversations (
    id              SERIAL          PRIMARY KEY,
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    tenant_id       INTEGER         NOT NULL REFERENCES users(id),
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    UNIQUE (landlord_id, tenant_id)
);

-- ============================================================
-- MESSAGES (Chat)
-- ============================================================
CREATE TABLE messages (
    id              SERIAL          PRIMARY KEY,
    conversation_id INTEGER         NOT NULL REFERENCES conversations(id),
    sender_id       INTEGER         NOT NULL REFERENCES users(id),
    content         TEXT,
    file_path       VARCHAR(500),
    is_read         BOOLEAN         DEFAULT FALSE,
    read_at         TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_messages_conversation ON messages (conversation_id);
CREATE INDEX idx_messages_sender       ON messages (sender_id);
CREATE INDEX idx_messages_created      ON messages (created_at);

-- ============================================================
-- NOTICES (Notice Board)
-- ============================================================
CREATE TABLE notices (
    id              SERIAL          PRIMARY KEY,
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    building_id     INTEGER         REFERENCES buildings(id),
    title           VARCHAR(255)    NOT NULL,
    content         TEXT            NOT NULL,
    is_urgent       BOOLEAN         DEFAULT FALSE,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ     DEFAULT NULL
);

CREATE INDEX idx_notices_landlord  ON notices (landlord_id);
CREATE INDEX idx_notices_building  ON notices (building_id);

-- ============================================================
-- DOCUMENTS
-- ============================================================
CREATE TABLE documents (
    id                  SERIAL          PRIMARY KEY,
    owner_id            INTEGER         NOT NULL REFERENCES users(id),
    property_id         INTEGER         REFERENCES properties(id),
    lease_id            INTEGER         REFERENCES leases(id),
    folder_name         VARCHAR(255),
    original_filename   VARCHAR(500)    NOT NULL,
    stored_filename     VARCHAR(500)    NOT NULL UNIQUE,
    file_path           VARCHAR(1000)   NOT NULL,
    file_type           VARCHAR(50),
    file_size_bytes     INTEGER,
    uploaded_at         TIMESTAMPTZ     DEFAULT NOW(),
    deleted_at          TIMESTAMPTZ     DEFAULT NULL
);

CREATE INDEX idx_documents_owner    ON documents (owner_id);
CREATE INDEX idx_documents_property ON documents (property_id);
CREATE INDEX idx_documents_lease    ON documents (lease_id);

-- ============================================================
-- COMPLIANCE DOCUMENTS
-- ============================================================
CREATE TABLE compliance_documents (
    id              SERIAL          PRIMARY KEY,
    tenant_id       INTEGER         NOT NULL REFERENCES users(id),
    doc_type        VARCHAR(50)     NOT NULL CHECK (doc_type IN ('Government ID','Proof of Income','Renters Insurance')),
    document_id     INTEGER         REFERENCES documents(id),
    status          VARCHAR(20)     DEFAULT 'Pending' CHECK (status IN ('Pending','Verified','Rejected','Expired')),
    expiry_date     DATE            DEFAULT NULL,
    verified_at     TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_compliance_tenant ON compliance_documents (tenant_id);

-- ============================================================
-- NOTIFICATIONS
-- ============================================================
CREATE TABLE notifications (
    id              SERIAL          PRIMARY KEY,
    user_id         INTEGER         NOT NULL REFERENCES users(id),
    event_type      VARCHAR(50)     NOT NULL,
    title           VARCHAR(255)    NOT NULL,
    message         TEXT,
    is_read         BOOLEAN         DEFAULT FALSE,
    read_at         TIMESTAMPTZ     DEFAULT NULL,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_notifications_user    ON notifications (user_id);
CREATE INDEX idx_notifications_read    ON notifications (is_read);
CREATE INDEX idx_notifications_created ON notifications (created_at);

-- ============================================================
-- AUDIT LOG (Append-only — immutable records)
-- ============================================================
CREATE TABLE audit_log (
    id              SERIAL          PRIMARY KEY,
    user_id         INTEGER         REFERENCES users(id),
    event_type      VARCHAR(100)    NOT NULL,
    resource_type   VARCHAR(100),
    resource_id     INTEGER,
    ip_address      VARCHAR(45),
    user_agent      TEXT,
    result          VARCHAR(20)     CHECK (result IN ('success','blocked','error')),
    metadata        JSONB,
    created_at      TIMESTAMPTZ     DEFAULT NOW()
);

CREATE INDEX idx_audit_user    ON audit_log (user_id);
CREATE INDEX idx_audit_event   ON audit_log (event_type);
CREATE INDEX idx_audit_created ON audit_log (created_at);

-- ============================================================
-- AUTOMATION SETTINGS
-- ============================================================
CREATE TABLE automation_settings (
    id              SERIAL          PRIMARY KEY,
    landlord_id     INTEGER         NOT NULL REFERENCES users(id),
    automation_type VARCHAR(100)    NOT NULL,
    is_enabled      BOOLEAN         DEFAULT TRUE,
    updated_at      TIMESTAMPTZ     DEFAULT NOW(),
    UNIQUE (landlord_id, automation_type)
);

CREATE INDEX idx_automation_landlord ON automation_settings (landlord_id);
```

---

> ✅ **All 13 `.md` files are complete.**
> Every file is grounded in every conversation, every decision, every principle, every page specification, every architecture layer, every business rule, and every security measure discussed across this entire project.
> Copy each file into the `docs/` folder of your project structure and your system has its complete living documentation foundation.
# 🎯 The Main Purpose of the Rent & Lease Management System

---

## In One Sentence

> **To digitize, automate, and centralize the entire relationship between a Landlord and a Tenant — from the moment a lease is signed to the moment a tenant moves out — eliminating paper, manual work, and informal communication entirely.**

---

## The Core Problem It Solves

Right now, without this system, this is the reality:

**For Landlords:**
- Tracking rent payments in a notebook or spreadsheet
- Chasing tenants via WhatsApp for overdue rent
- No formal record of maintenance complaints
- No visibility into which properties are profitable
- Forgetting lease renewal dates until it is too late
- Manually calculating and communicating late fees

**For Tenants:**
- Not knowing exactly what they owe and when
- No formal way to report property damage with evidence
- No proof of property condition at move-in
- Lease documents lost or inaccessible
- No receipt or record of rent payments made

---

## What the App Actually Does

It replaces all of that chaos with **one unified platform** that handles:

| What | How |
|---|---|
| **Rent Collection** | Tenants pay online, amounts are locked and system-calculated, receipts generated automatically |
| **Lease Management** | Digital contracts, invitation system, overlap prevention, expiry warnings |
| **Maintenance** | Formal ticket system with photos, Kanban tracking, evidence trail |
| **Communication** | Real-time WhatsApp-style chat with a full message history |
| **Financial Visibility** | Revenue dashboards, expense tracking, ROI calculations, exportable reports |
| **Automation** | Late fees apply themselves, reminders send themselves, expiry warnings trigger themselves |
| **Legal Protection** | Move-in/move-out inspections locked after submission, document vault, audit trail |

---

## The Single Root Idea

> The app exists because **property management is a business** — and every business needs a system, not a collection of WhatsApp threads, notebooks, and spreadsheets.

It gives the **Landlord** a professional CRM to run their property portfolio like a business.

It gives the **Tenant** a clear, transparent, and fair experience where they always know exactly where they stand.

**Both sides win. That is the purpose.**
# 🎯 Core Features, Functionalities, Pages, Purpose, Scope, Margin & Strength
## Rent & Lease Management System — The Complete Project Profile

---

## 🧭 1. PURPOSE — Why This System Exists

### The Root Problem
In traditional property management, data is documented manually using notepads, Microsoft Excel, or other spreadsheets. This makes the process slow, inefficient, and more likely to have errors. Landlords either had to manage everything themselves or hire third-party managers, requiring more time and labor. Property management systems were formed to evade human errors and streamline work through automation.

### The Primary Purpose — In Three Levels

**Level 1 — The Human Purpose:**
> To give Landlords their time back and give Tenants clarity and peace of mind.

**Level 2 — The Business Purpose:**
> To replace every spreadsheet, every WhatsApp thread, every paper lease, and every manual bank transfer with a single, automated, intelligent platform that runs the property rental lifecycle from end to end.

**Level 3 — The Technical Purpose:**
> To build a dual-portal SaaS web application that digitizes, automates, and centralizes the complete relationship between a Landlord and a Tenant — covering leases, rent, maintenance, communication, documents, compliance, and financial reporting — in one unified system.

---

## 📊 2. MARKET — Where This System Sits

The global property management software market was valued at USD 24.18 billion in 2024 and is projected to grow from USD 26.55 billion in 2025 to USD 52.21 billion by 2032, exhibiting a CAGR of 10.1%.

The increasing demand for SaaS-based property management software is one of the key drivers of market growth.

Online portals for tenants that facilitate rent payments, maintenance requests, and document access foster transparent communication and improve the overall tenant experience. This integration contributes to higher tenant retention rates and increased real-estate profitability.

This system is built directly at the intersection of those two growing demands — **SaaS delivery** and **tenant-centered experience**.

---

## 🏗️ 3. CORE FEATURES — The 12 Pillars

These are the 12 fundamental capabilities the system is built around. Each one solves a specific real-world problem.

---

### PILLAR 1 — Identity & Access Management
**The Problem it Solves:** Anyone can claim to be a Landlord or Tenant without verification.

**What it does:**
- Role-based registration — Landlord or Tenant selected at signup
- Email verification before any access is granted
- JWT-based secure sessions that expire automatically
- Lease Invitation Gateway — Tenants are invited via encrypted URL, binding their account to a specific lease
- Password reset with 15-minute expiry tokens
- Every session is authenticated and every resource access is authorized

**Why it matters:**
Without this, the entire system has no identity. Every other feature depends on knowing who the user is and what they are allowed to access.

---

### PILLAR 2 — Property Portfolio Management
**The Problem it Solves:** Landlords manage properties across notebooks, phone photos, and memory.

**What it does:**
- Add, edit, and view all properties with address, unit number, and base rent
- Delete properties — blocked automatically if an active lease exists
- Occupancy status badge per property — Leased or Vacant
- Multi-unit building grouping with accordion tree view
- Parent building containing multiple child units
- Bulk financial view per building

**Why it matters:**
A Landlord with 20 units across 4 buildings needs a central catalog. This is that catalog.

---

### PILLAR 3 — Lease & Contract Management
**The Problem it Solves:** Paper leases get lost, dates get confused, tenants get informally invited.

**What it does:**
- Create digital leases with unit, start date, end date, and monthly rent
- Real-time overlap validation — system prevents two active leases on the same unit for the same dates
- Email invitation system — Tenant receives a unique encrypted link to accept and register
- Sortable lease table showing all active and expired leases
- 60-day automated expiry warning
- One-click lease renewal from the dashboard

**Why it matters:**
Every financial and operational event in the system traces back to a lease. The lease is the contract that makes everything else valid.

---

### PILLAR 4 — Rent Collection & Financial Management
**The Problem it Solves:** Rent is tracked in spreadsheets, late fees are forgotten, and receipts do not exist.

**What it does:**
- Invoice generation tied directly to the lease contract
- Tenant payment amount is system-locked — cannot be modified
- Payment gateway integration — online card payments
- 5% late fee applied automatically by cron job on overdue invoices
- Overdue invoices highlighted visually in the Landlord ledger
- PDF receipt generated for every payment
- Financial report export as CSV and PDF
- Expense logging — plumbing, taxes, repairs
- Net ROI calculator — revenue minus expenses per property
- Offline cash payment recording for manual transactions

**Why it matters:**
Automated property management tools reduce human errors and help property managers assign tasks more efficiently, preventing service delays. They help reduce the time taken to respond to complaints and grievances of tenants. They streamline property management procedures by facilitating rent collection processes, reducing communication gaps, tracking finances, and storing and leasing documents and contracts.

---

### PILLAR 5 — Real-Time Chat (WhatsApp-Style)
**The Problem it Solves:** Landlord-Tenant communication happens over personal WhatsApp with no professional record.

**What it does:**
- WebSocket-driven instant messaging between Landlord and each Tenant
- Landlord sees all tenants in a contact list — clicks to open a dedicated thread
- Tenant opens directly into their single Landlord thread
- Photo and file attachments
- Typing indicators — see when the other party is writing
- Read receipts — blue double ticks confirm message was seen
- Online/offline presence indicator — green dot for live status
- Floating "New Message" pill when scrolled up in history
- Full message history persisted in database

**Why it matters:**
Every conversation is now formal, searchable, time-stamped, and owned by the system. No more "I never received that message" disputes.

---

### PILLAR 6 — Maintenance Helpdesk
**The Problem it Solves:** Repair requests are sent via WhatsApp, forgotten, and undocumented.

**What it does:**
- Tenant submits ticket with category, urgency level, description, and photo evidence
- System enforces a 3-ticket active limit per Tenant (spam prevention)
- Landlord manages all tickets on a Kanban board — Pending → In Progress → Resolved
- Drag-and-drop status updates between columns
- Priority tags — Emergency (red), Low (gray)
- Tenant can add follow-up comments to open tickets
- Tenant notified immediately when Landlord resolves the ticket
- Resolution time tracked for analytics

**Why it matters:**
Maintenance becomes a formal, evidence-backed, trackable workflow — not a forgotten WhatsApp voice note.

---

### PILLAR 7 — Move-In / Move-Out Inspection
**The Problem it Solves:** Security deposit disputes with no documented proof of property condition.

**What it does:**
- Room-by-room accordion checklist — Kitchen, Bathroom, Bedroom, Living Area
- Mandatory photo upload per room
- Progress bar — 0% to 100% completion
- Submit button locked until 100% complete
- Form becomes permanently readonly after submission — legal protection
- Both Landlord and Tenant have access to the submitted report
- Timestamp-locked for legal validity

**Why it matters:**
This is the legal protection layer. A tenant who documented pre-existing damage cannot be charged for it. A Landlord with a documented inspection cannot be disputed without evidence. Both parties are protected.

---

### PILLAR 8 — Document Management (The Vault)
**The Problem it Solves:** Lease agreements, insurance documents, and property records are scattered across email inboxes and physical folders.

**What it does:**
- Drag-and-drop file upload
- Google Drive-style grid view organized by property folder
- IDOR-protected download — JWT verified before any file is streamed
- Delete with typed confirmation ("Type DELETE to confirm")
- Secure file storage outside the web root
- Compliance documents — Government ID, Proof of Income, Renter's Insurance
- Expiry date tracking on insurance documents
- Automated warnings 30 days before insurance expires

**Why it matters:**
Every legal document in the entire landlord-tenant relationship lives in one secure, organized, always-accessible vault.

---

### PILLAR 9 — Analytics & Reporting
**The Problem it Solves:** Landlords have no data-driven view of whether their properties are actually profitable.

**What it does:**
- 12-month revenue trend line chart
- Maintenance category breakdown donut chart
- Payment timeliness ratio donut chart
- At-risk tenant identification — tenants with consistent late payment history
- Best and worst performing properties
- Average ticket resolution time
- Collection rate calculation
- CSV export of full analytics data

**Why it matters:**
These solutions automate tenant screening, lease management, rent collection, maintenance tracking, and tenant communication, fostering operational efficiency, tenant satisfaction, and data-driven decision-making. They offer centralized data management and real-time insights, allowing real-estate managers to optimize rental performance.

---

### PILLAR 10 — Automation Engine
**The Problem it Solves:** Manual reminders, manual fee applications, and manual expiry checks are forgotten or inconsistent.

**What it does:**
- 3-Day Rent Reminder Emails — sent automatically before due date
- 5% Late Fee Auto-Application — applied by cron job at midnight on overdue invoices
- 60-Day Lease Expiry Warning — alerts Landlord and Tenant automatically
- Auto-Pay — deducts exact rent on the 1st of each month when Tenant enables it
- Insurance Expiry Warning — alerts Tenant 30 days before insurance expires
- All automations are toggle-controlled by the Landlord from the Control Panel
- Every automated event is logged to the audit trail

**Why it matters:**
The system works while the Landlord sleeps. No manual intervention needed for routine financial and administrative operations.

---

### PILLAR 11 — Notice Board
**The Problem it Solves:** Community announcements get buried in group chats.

**What it does:**
- Landlord publishes broadcast announcements to all tenants in a building
- Standard notices and urgent alerts visually distinguished
- Urgent notices have a thick Muted Red border and URGENT badge
- Entirely read-only for tenants — no replies
- Chronological feed

**Why it matters:**
A formal, centralized announcement channel that all tenants in a building receive simultaneously — no one can claim they did not see it.

---

### PILLAR 12 — Notification System & Audit Trail
**The Problem it Solves:** Users have no single place to see everything that has happened.

**What it does:**
- Real-time push notifications via WebSocket
- Chronological notification feed per user
- Color-coded icons by event type — payments, late fees, tickets, chat
- Mark all as read in one click
- Infinite scroll pagination
- Complete audit log of all financial and security events
- Immutable records — audit log is append-only, never editable

**Why it matters:**
Every event in the system is visible, traceable, and permanent. Disputes are resolved by checking the log.

---

## 📄 4. PAGES — All 38 At a Glance

### 🖥️ Landlord Portal — 14 Pages (Desktop-Optimized)

| # | Page | Core Job |
|---|---|---|
| 1 | Dashboard | Command center — portfolio health at a glance |
| 2 | Property Portfolio | Manage all physical property assets |
| 3 | Leases & Onboarding | Create and manage lease contracts |
| 4 | Financials & Billing | Invoice ledger, late fees, revenue export |
| 5 | Real-Time Chat | Instant messaging with all tenants |
| 6 | Maintenance Kanban | Visual ticket workflow management |
| 7 | Tenant Directory (CRM) | Search, filter, and manage all tenant profiles |
| 8 | Document Center | Secure file vault for all legal documents |
| 9 | Analytics & Reports | Data intelligence and performance insights |
| 10 | Notifications | Chronological system event feed |
| 11 | Settings & Profile | Credentials, bank details, notification preferences |
| 12 | Expense & ROI Ledger | Expense logging and net income tracking |
| 13 | Multi-Unit Buildings | Hierarchical building and unit management |
| 14 | Automation Control Panel | Toggle switches for all cron job automations |

### 📱 Tenant Portal — 11 Pages (Mobile-First)

| # | Page | Core Job |
|---|---|---|
| 1 | Dashboard | Balance status and quick actions |
| 2 | Rent Payment & Invoices | Secure checkout and receipt history |
| 3 | My Lease & Property | Read-only lease details and documents |
| 4 | Maintenance Helpdesk | Submit and track repair tickets |
| 5 | Real-Time Chat | Direct messaging with Landlord |
| 6 | Move-In/Move-Out Inspection | Progress-gated legal inspection form |
| 7 | Payment Methods & Auto-Pay | Card management and auto-deduction setup |
| 8 | Notice Board | Read-only Landlord announcements |
| 9 | Compliance & Insurance | Mandatory document uploads and expiry tracking |
| 10 | Profile & Settings | Personal account and notification management |
| 11 | Notification & History | Complete event audit log |

### 🌍 External & System Pages — 13 Pages

| # | Page | Core Job |
|---|---|---|
| 1 | Landing Page | Marketing front door and conversion |
| 2 | Registration | Role-based new user onboarding |
| 3 | Login | Secure authentication entry point |
| 4 | Lease Invitation Gateway | Encrypted URL tenant registration |
| 5 | Email Verification | Holding page for account verification |
| 6 | Forgot Password | Reset request trigger |
| 7 | Reset Password | Secure two-stage password recovery |
| 8 | Payment Success | Financial reassurance callback page |
| 9 | Payment Cancelled | Decline notification with retry action |
| 10 | 403 Forbidden | IDOR security block with audit log |
| 11 | 429 Too Many Requests | Rate limit block with live countdown |
| 12 | 404 Not Found | Broken URL friendly page |
| 13 | 503 Maintenance / Error | Server down — zero JavaScript, zero animations |

---

## 🗺️ 5. SCOPE — What Is and Is Not This System

### ✅ IN SCOPE — What the System Covers

```
IDENTITY          → Registration, login, roles, verification, password reset
PROPERTIES        → Add, edit, delete, organize, multi-unit buildings
LEASES            → Create, invite, overlap-validate, renew, expire
RENT              → Invoice, pay, receipt, export, late fee, auto-pay, offline
MAINTENANCE       → Submit, track, Kanban, photo evidence, spam limit
INSPECTION        → Move-in, move-out, progress-gated, legally locked
CHAT              → Real-time, WebSocket, read receipts, file attachment
DOCUMENTS         → Upload, organize, IDOR-protected download, compliance
ANALYTICS         → Revenue charts, maintenance charts, at-risk tenants
AUTOMATION        → Late fees, reminders, expiry warnings, auto-pay cron jobs
NOTIFICATIONS     → Real-time push, audit log, event history
NOTICES           → Landlord broadcast to building tenants
SECURITY          → JWT, bcrypt, IDOR, rate limiting, CSRF, audit trail
COMPLIANCE        → Government ID, income proof, insurance with expiry tracking
ERROR HANDLING    → 403, 429, 404, 503 branded pages
```

### ❌ OUT OF SCOPE — What the System Does Not Cover

```
Admin panel of any kind
Property listing or marketplace (finding tenants)
Multi-language / internationalization
Native mobile app (iOS or Android)
Accounting software integration (QuickBooks, Xero)
Tenant-to-tenant communication
Third-party SSO (Google Login, Facebook Login)
Video or audio calling
AI-assisted features
Utility billing management
Property valuation tools
```

---

## 💰 6. MARGIN — The Value This System Creates

### For the Landlord

| Without the System | With the System | Value Created |
|---|---|---|
| Chasing tenants via WhatsApp for rent | Automatic reminders sent 3 days before due date | Time saved, stress eliminated |
| Manually calculating 5% late fees | Cron job applies fees at midnight automatically | Zero human error, consistent enforcement |
| Forgetting lease renewal dates | 60-day automated expiry warning | Never lose a tenant from administrative oversight |
| Spreadsheet financial tracking | Real-time dashboard + CSV/PDF export | Business intelligence, not guesswork |
| Paper receipts or no receipts | Automatically generated digital receipts per payment | Legal protection, professional image |
| No visibility into ROI | Revenue minus expenses = net ROI per property | Informed investment decisions |
| Informal WhatsApp maintenance requests | Formal Kanban with photo evidence and timestamps | Accountability, resolution tracking |
| Paper move-in/move-out forms | Digital, legally locked, timestamped inspections | Deposit dispute protection |

### For the Tenant

| Without the System | With the System | Value Created |
|---|---|---|
| Not knowing what they owe | Hero card shows exact balance in 2 seconds | Clarity, no anxiety |
| No formal way to report damage | Structured ticket system with photo evidence | Protection, accountability |
| No proof of property condition at move-in | Legally locked inspection report | Security deposit protection |
| Lease documents lost or inaccessible | Always-accessible digital document vault | Peace of mind |
| No payment history or receipts | Complete transaction history with PDF receipts | Financial record |
| Forgetting rent due dates | Automatic email reminders before due date | Late fee prevention |
| Having to remember to pay every month | Auto-Pay handles it on the 1st | Zero effort, zero late fees |

### The Market Margin
The increasing demand for property management software to address consumers' real estate preferences and the growing need for improved consumer handling and support are driving the market expansion.

Cost-effective SaaS offerings are opening the market to small and medium-sized enterprises.

This system specifically targets the **underserved small-to-mid Landlord** — someone with 2 to 50 units who cannot afford enterprise solutions like Yardi or AppFolio but is currently managing everything manually. That is the largest unserved segment in the entire market.

---

## 💪 7. STRENGTH — What Makes This System Genuinely Powerful

### STRENGTH 1 — It Serves Two Users Simultaneously With One System
Every feature is designed for both the Landlord's perspective and the Tenant's perspective. The Kanban board is the Landlord's management view. The ticket status tracker is the Tenant's visibility view. The same data. Two different, purpose-built interfaces. One system.

### STRENGTH 2 — Real-Time at Its Core
The chat and notification systems are built on WebSockets — not polling, not page refreshes. When a Tenant sends a message, the Landlord sees it instantly. When a payment is made, the Landlord's dashboard updates in real time. The system feels alive.

### STRENGTH 3 — Automation That Works While Nobody Is Watching
The cron job engine means the system performs work — applying fees, sending reminders, scanning for expiring leases, processing auto-pay — without any human being at a computer. Automated property management tools reduce human errors and help property managers assign tasks more efficiently, preventing service delays.

### STRENGTH 4 — Security Designed In, Not Bolted On
IDOR prevention at both middleware and query level. JWT authentication. bcrypt password hashing. Rate limiting at two tiers. CSRF protection. Parameterized queries. Append-only audit logs. These are not afterthoughts — they are designed into the architecture from the first line.

### STRENGTH 5 — Legal Protection for Both Parties
The Move-In/Move-Out inspection form is progress-gated and permanently locked after submission. The audit trail is immutable. Invoices and receipts are system-generated and tamper-proof. Every event is timestamped in UTC. When a dispute happens — and in property rental, disputes always happen — the system is the evidence.

### STRENGTH 6 — A Purpose-Built Experience for Each User
The Landlord portal is desktop-optimized with an F-Pattern layout, dense data tables, analytics charts, and a Kanban board — a professional CRM. The Tenant portal is mobile-first with large 48px touch targets, a single hero card showing their balance, and three focused action buttons — a consumer app. The same system. Two completely different interaction models designed for how each user actually works.

### STRENGTH 7 — Complete Financial Lifecycle Coverage
From lease creation to invoice generation to payment processing to receipt download to expense logging to ROI calculation to CSV export — every financial event in the landlord-tenant relationship is covered in one system. No spreadsheet required. No manual reconciliation. No guesswork.

### STRENGTH 8 — Built on Industry Standards
The SaaS model has gained popularity due to its value proposition of lower initial investments and regular updates without much IT burden. This model gives businesses the flexibility to scale their lease management implementation based on requirements, adapting easily to changing needs from the leasing market without the limitations of traditional software solutions.

The 9-layer architecture, SOLID principles, ACID transactions, JWT authentication, WebSocket real-time, and the complete OWASP Top 10 mitigation — these are not academic exercises. They are the same patterns used by Stripe, Linear, Notion, and every other respected SaaS platform.

---

## 📊 THE COMPLETE SUMMARY TABLE

| Dimension | Detail |
|---|---|
| **Purpose** | Digitize and automate the complete landlord-tenant relationship lifecycle |
| **Users** | Landlords (desktop CRM) + Tenants (mobile consumer app) |
| **Total Pages** | 38 (14 Landlord + 11 Tenant + 13 External/System) |
| **Core Pillars** | 12 (Identity, Properties, Leases, Rent, Chat, Maintenance, Inspection, Documents, Analytics, Automation, Notices, Notifications) |
| **Architecture** | 9-Layer System — HTML → CSS → JS → Middleware → API → Business Rules → Business Logic → Data Retrieval → Data Storage |
| **Tech Stack** | HTML + CSS + JavaScript (Frontend) | Python (Backend) | SQL (Database) |
| **Real-Time** | WebSocket chat + WebSocket push notifications |
| **Automation** | 4 cron jobs — late fees, reminders, expiry warnings, auto-pay |
| **Security** | JWT, bcrypt, IDOR x2, rate limit x2, CSRF, parameterized queries, audit log |
| **In-Scope** | Full rental lifecycle — lease to move-out |
| **Out-of-Scope** | Admin panel, marketplace, native app, third-party SSO |
| **Market** | $24.18B property management software market growing at 10.1% CAGR |
| **Target Segment** | Small-to-mid landlords (2–50 units) currently managing manually |
| **Core Strength** | Dual-portal real-time system with automation, security, and legal protection built in |

---

> This is not a project. It is a **product**.
> It solves a real problem that millions of Landlords and Tenants face every single day.
> It is built with the architecture, security, and design standards of a system that is meant to last — not just to be submitted.
# ⚠️ Core Failures, Risks, Ups & Downs, Hard Times & Weaknesses
## Rent & Lease Management System — The Honest, Unfiltered Project Truth
### Because Every Great System Has a Shadow Side

---

## 🧠 THE FOUNDATIONAL TRUTH BEFORE EVERYTHING

> **A system that only knows its strengths is a system waiting to fail.**
> The engineers who built the Titanic knew every strength.
> They did not take the weaknesses seriously enough.
> That is the lesson.

Understanding where a project can break, bleed, and collapse is not pessimism. It is the most important form of engineering intelligence. Every weakness identified before production is a crisis prevented. Every weakness ignored before production becomes a story told after the disaster.

This document is the honest mirror the project must look into.

---

# 🔴 PART 1 — CORE TECHNICAL FAILURES
### *The places where the code itself can break the system*

---

## FAILURE 1 — The WebSocket Complexity Trap

### What it is:
WebSockets sound simple in theory. In practice, they are one of the most technically demanding features in web development, and this project has them at the core of two critical features — real-time chat and live notifications.

### Where it breaks:
A WebSocket connection is a persistent, stateful, bidirectional connection. Unlike REST which is stateless and self-healing, a WebSocket that drops is gone. The user is offline. Messages sent during disconnection are lost unless a queuing and re-delivery system is built. That queuing and re-delivery system is an entire additional engineering problem that is easy to underestimate.

When a user's mobile network switches from WiFi to cellular — which happens constantly on mobile devices — the WebSocket connection drops silently. The Tenant's chat page shows they are still connected when they are not. They send a message. It disappears. No error. No feedback. Just silence.

### The hard truth:
Building WebSockets correctly requires handling connection state, reconnection with exponential backoff, message acknowledgement, duplicate message prevention on reconnect, offline message queuing, and presence state synchronization. Most first implementations handle the happy path — connection established, messages flow. They do not handle the broken path — what happens when the network is unreliable, the server restarts, or the client goes offline mid-conversation.

### The real-world consequence:
A Tenant sends an urgent maintenance photo through chat. The connection silently dropped 3 seconds earlier. The message never arrives. The Tenant thinks it was sent. The Landlord never sees it. The plumbing leak gets worse. This is a trust-destroying failure.

---

## FAILURE 2 — The Payment Webhook Vulnerability Window

### What it is:
The payment flow has a dangerous gap between the moment the Tenant's browser submits the payment and the moment the payment gateway's webhook confirms the charge cleared.

### Where it breaks:
The system is designed correctly — the database only updates after the webhook confirms. But webhooks are not instant. A webhook from Stripe or Paystack can arrive anywhere between 1 second and 30 seconds after the payment. During that window, the Tenant's UI is showing a spinner. If the Tenant closes the browser, navigates away, or loses connection during that window, the payment may have cleared at the gateway but the system never received the webhook confirmation.

The result is a Tenant who was charged but whose invoice still shows Outstanding. They have a bank deduction. The system says they have not paid. The Landlord sees an overdue invoice. The Tenant receives a late fee reminder for money they already paid.

### The second failure:
Webhook endpoints must be publicly accessible to receive callbacks from the gateway. This makes them a potential attack surface. A malicious actor who discovers the webhook URL can send fake webhook payloads pretending to confirm payments that never happened — marking invoices as paid without any money moving. Without webhook signature verification, the system processes these fake confirmations.

### The hard truth:
Webhook signature verification is not optional. Idempotency on webhook processing is not optional. A reconciliation job that checks gateway records against database records is not optional. These are three additional engineering problems that emerge from the simple feature description of "accept online payments."

---

## FAILURE 3 — The Cron Job Silent Failure Problem

### What it is:
Four background cron jobs run automatically — late fees, reminders, expiry warnings, and auto-pay. They run at night when no developer is watching. They fail silently.

### Where it breaks:
A cron job that encounters a database connection timeout at 00:05 AM does not alert anyone. It logs an error to a file that no one is reading. The late fees that should have been applied to 47 overdue invoices that night are not applied. The next morning, 47 Tenants who should have received late fee notifications did not. The Landlord's financial reports are wrong. The automated enforcement that the entire billing automation depends on silently did not happen.

The opposite failure is equally dangerous. A cron job that runs twice — because a server restart triggered a duplicate execution — applies late fees twice to every overdue invoice. 47 Tenants get charged 10% instead of 5%. The system created a financial error at scale in the middle of the night with no human present to catch it.

### The third cron failure:
Auto-Pay processes real money. A bug in the auto-pay cron job that causes it to process payments for the wrong amount, or to process payments for tenants who have already paid manually, is a financial disaster. Real money is moved incorrectly at scale. Reversals require manual intervention, customer service, and destroy Tenant trust completely.

### The hard truth:
Background jobs require monitoring infrastructure, alerting systems, distributed locking, idempotency protection, retry logic, and audit logging. Without all of these, automation becomes a liability rather than an asset.

---

## FAILURE 4 — The Database N+1 Query Death Spiral

### What it is:
As the system grows in data volume, poorly written data retrieval code that seems fast during development becomes catastrophically slow in production.

### Where it breaks:
The Landlord Dashboard loads data for all their properties. If the dashboard makes one query to get 20 properties, then for each property makes another query to get its active lease, then another to get the tenant name, then another to get the invoice status — that is 1 + 20 + 20 + 20 = 61 database queries to load one page. With 50 properties it becomes 151 queries. With 200 properties it becomes 601 queries. Each query adds latency. A dashboard that loads in 80ms during development loads in 4 seconds in production with real data.

### The real-world consequence:
A Landlord with a growing portfolio opens their dashboard every morning. It takes 6 seconds to load. They conclude the system is broken. They stop using it. They go back to their spreadsheet. The product fails not because the features are wrong but because the performance is wrong.

### The hard truth:
N+1 queries are invisible during development because the database has 10 rows. They are catastrophic in production with 10,000 rows. Every data retrieval function must be written with JOINs and proper query planning from the start — not optimized later when users are already frustrated.

---

## FAILURE 5 — The IDOR Implementation Gap

### What it is:
IDOR (Insecure Direct Object Reference) protection is designed at two levels — middleware and query level. But there is a gap that is easy to miss.

### Where it breaks:
Middleware checks resource ownership broadly. But some resources have complex ownership chains. A maintenance ticket belongs to a Tenant, but it also belongs to a Landlord. A document belongs to a Landlord, but it is associated with a Tenant's lease. A chat message belongs to a conversation that involves two users.

If the middleware ownership check only verifies the primary owner and misses the secondary relationship, a Tenant could potentially access a document uploaded by another Tenant for the same property — because both share the same property_id and the check verified property ownership rather than document ownership.

These are subtle, logic-level IDOR vulnerabilities that automated security scans will not catch. They require deliberate security review of every resource relationship in the system.

### The hard truth:
IDOR is not a single check. It is a mindset applied to every single resource in the system. Missing one resource — one endpoint, one download route, one analytics query — creates a data breach waiting to be discovered.

---

# 🟠 PART 2 — CORE PROJECT RISKS
### *The threats that can derail the entire project before it ships*

---

## RISK 1 — Scope Creep: The Silent Project Killer

### What it is:
The project has 38 pages, 12 feature pillars, 4 cron jobs, WebSocket real-time, payment integration, and a complete security perimeter. It is already large. The temptation to add more is constant and dangerous.

### How it manifests:
Mid-development, a team member suggests adding a maintenance vendor management system. Another suggests a property listing page for finding new tenants. Another wants to add a rent negotiation feature. Each one sounds reasonable in isolation. Together, they push the delivery date from Week 15 to Week 25 — while the core features remain incomplete.

### The worst version of this risk:
The project is presented with a beautifully designed landing page, a partially working dashboard, and 6 incomplete features — because the team spent 3 weeks building a feature that was not in scope instead of completing the core. The system looks impressive until anyone tries to actually use it.

### The hard truth:
Every feature added to scope is a feature removed from quality. A project with 38 pages completed correctly is infinitely more valuable than a project with 60 pages half-finished.

---

## RISK 2 — The Integration Dependency Chain

### What it is:
This system has multiple external dependencies — payment gateway, SMTP email service, WebSocket server, file storage. Each one is a point of failure outside the team's control.

### How it breaks:
Stripe changes their API. The webhook signature format is updated. The existing integration breaks silently — payments appear to succeed in the browser but are never confirmed. Or Stripe requires additional compliance verification for a student project and the account is restricted during the final presentation week.

The SMTP service hits its free tier limit. Invitation emails, password reset emails, and rent reminder emails stop sending. Tenants cannot verify their accounts. The entire onboarding flow breaks.

### The academic context risk:
Student developer accounts on free tiers have strict limits. A payment gateway that works perfectly during development with 5 test transactions may refuse to process when 20 people try to use the demo simultaneously during presentation.

---

## RISK 3 — The Single Point of Knowledge Problem

### What it is:
In a team project, if only one person understands the WebSocket implementation, and only one person understands the payment gateway integration, and only one person understands the database schema — the project has single points of failure in its human architecture.

### How it breaks:
The team member who built the WebSocket server becomes unavailable during the final week. No one else can debug it. The chat feature breaks during the presentation. The team cannot fix it.

Or worse — one person wrote everything. The code works. But no one else understands it well enough to explain it during the presentation defense. The evaluator asks "why did you choose WebSockets over polling?" and the answer is silence.

### The hard truth:
A project that cannot be explained by the team that built it is a project that was not built by the team. It was built by one person who dragged the rest along. Evaluators know how to find this.

---

## RISK 4 — The "It Works on My Machine" Deployment Risk

### What it is:
The system works perfectly on the developer's local machine. It uses SQLite for the database, a local file system for uploads, localhost for the WebSocket, and test credentials for payments. Moving to a real server breaks all four of these simultaneously.

### How it breaks:
SQLite does not handle concurrent writes correctly under production load. The local file upload path `/uploads/documents/` does not exist on the production server. The WebSocket connection that uses `localhost` fails because the production server is a different machine. The payment gateway test credentials work only in sandbox mode.

### The hard truth:
A system that has never been deployed is not a production system. It is a local prototype. Deployment is a separate engineering problem that takes time, and discovering it the week before presentation is too late.

---

# 🟡 PART 3 — UPS AND DOWNS THROUGHOUT THE BUILD
### *The emotional and technical journey of a project this size*

---

## THE UPS

### Up 1 — When the Authentication Flow First Works
The moment a user registers, receives a verification email, clicks the link, logs in, receives a JWT, and lands on the correct dashboard for their role — this is the first complete end-to-end moment. It proves the entire architecture is connected. Everything before this is setup. Everything after this is building on a foundation that works. This moment feels like the project has a heartbeat for the first time.

### Up 2 — When the Kanban Drag-and-Drop Clicks Into Place
The visual magic of dragging a card from Pending to Resolved, watching it tilt 3 degrees with a strong shadow, landing it in the correct column, and having the database update silently in the background — this is the moment the project stops feeling like a school assignment and starts feeling like a real product. Non-technical people who see this moment immediately understand what the system is capable of.

### Up 3 — When the First Real Payment Processes
Entering a test card number, tapping pay, watching the spinner, and seeing the success page with a receipt ID — and then checking the database and seeing the invoice marked Paid, the transaction record created, and the notification in the feed. This is the moment the financial backbone of the entire system proves itself. The most complex technical flow in the project completed successfully.

### Up 4 — When Chat Works in Real Time Across Two Browser Windows
Opening the Landlord chat on one browser and the Tenant chat on another, sending a message from one, watching it appear on the other in under 100 milliseconds — with the typing indicator showing while composing, and the blue double tick appearing on delivery. This is the moment the system feels alive. No page refresh. No polling delay. Pure real-time.

### Up 5 — When the Cron Job Runs for the First Time at Midnight
Setting a test invoice to overdue, watching the clock tick past midnight, refreshing the database — and seeing the late fee applied, the invoice total updated, and the notification record created. Without anyone pressing a button. Without anyone being awake. The automation working exactly as designed. This is when the system stops being code and becomes a machine.

---

## THE DOWNS

### Down 1 — The Database Schema Crisis at Week 5
At some point during the build, a fundamental problem with the database schema is discovered. The invoices table was designed without properly accounting for the late fee as a separate tracked record. Now 3 tables have been built on top of it, 2 API endpoints reference it, and the business logic for payment processing depends on it. Changing the schema means touching everything built on top of it.

This is the moment the team learns why the database schema must be reviewed and signed off before writing a single line of application code. The lesson is learned the hard way.

### Down 2 — The First Security Failure Discovery
During testing, a team member discovers that entering another user's invoice ID in the payment URL accesses that invoice. The IDOR protection was implemented for documents and leases but missed the invoice endpoint. The system has been running for two weeks with this vulnerability.

The response requires auditing every single endpoint for the same class of vulnerability. Two days of work reviewing code instead of building new features. It feels like going backwards. But it is actually the most important two days of the entire project.

### Down 3 — The Week Before Presentation: Nothing Works Together
Individual features work in isolation. The Kanban board works. The payment flow works. The chat works. But when a complete user journey is tested end-to-end — register as Landlord, add property, create lease, invite Tenant, Tenant pays rent, Landlord receives notification, Landlord views analytics — something breaks at every step.

Session handling breaks the invitation flow. The WebSocket disconnects after 10 minutes of inactivity. The analytics chart loads empty because the aggregation query returns zero when it should not. The cron job does not fire because the scheduler was not started with the correct timezone setting.

This is the hardest moment of the project. Three weeks of work and the integrated system does not hold together. The temptation to give up is real. The correct response is to work through it systematically, layer by layer, starting from the database and working up.

### Down 4 — The Mobile Responsiveness Reckoning
The Tenant portal was built mobile-first in principle. But it was tested on a desktop browser with responsive mode enabled. When opened on an actual iPhone 12, three issues appear simultaneously — the hero balance card overflows the screen, the "Pay Rent" button is partially hidden behind the browser navigation bar, and the chat input field is pushed off screen when the keyboard opens.

Real device testing should have happened at the end of every feature, not at the end of the project.

### Down 5 — The Moment the Team Realizes the Project Is Too Big
There is a week — usually around Week 8 or 9 — when the team looks at what has been built (roughly half the features), looks at what remains (roughly the other half), and realizes the timeline does not add up. The chat, the analytics, the cron jobs, the document vault, the compliance system, the inspection form, the building management, the automation panel — all still need to be built.

This is the down that separates good teams from great ones. Great teams reprioritize ruthlessly, cut scope to in-scope MVP, and deliver what they promised. Average teams try to build everything and deliver nothing complete.

---

# 🔵 PART 4 — PROJECT WEAKNESSES
### *The honest limitations and gaps in what has been designed*

---

## WEAKNESS 1 — No Offline Support

### What it is:
The entire system requires a live internet connection to function. There is no offline mode, no service worker caching, no local data persistence.

### Why it is a weakness:
The Tenant portal targets mobile users. Mobile users lose connectivity regularly — underground, in basements, in rural areas, traveling. When connectivity drops, the Tenant portal shows a blank screen or an error. The Tenant cannot view their balance, cannot check their lease, cannot see their payment history.

For a system that holds a Tenant's most important financial information — their rent status — this is a significant usability limitation. A Tenant who cannot check if they paid their rent because the app requires internet has a worse experience than looking at a bank statement.

---

## WEAKNESS 2 — Single Language, No Internationalization

### What it is:
The system is built in English only. All labels, error messages, notifications, and UI copy are hardcoded in English.

### Why it is a weakness:
Property management is a global need. Landlords and Tenants in Ghana, Nigeria, Kenya, India, and Brazil — all major real estate markets — may not have English as their primary language. A system targeting "all schools" or a broad market that operates only in English immediately excludes a significant portion of its potential users.

Internationalization is out of scope — but that does not make it a strength. It is a deliberate limitation with a real market cost.

---

## WEAKNESS 3 — No Admin Override Mechanism

### What it is:
The system deliberately has no admin panel. There are exactly two user types — Landlord and Tenant.

### Why it is a weakness:
This is clean in design but creates operational problems in reality.

When a Tenant is locked out because their email verification link expired and they cannot receive emails, there is no administrator who can manually verify the account.

When a payment is processed by the gateway but the webhook fails to arrive and the invoice remains Outstanding, there is no administrator who can manually mark the invoice as paid.

When a lease has a data error that prevents the Tenant from accessing their account, there is no administrator who can correct the record.

Every one of these scenarios — all of which will happen in production — requires either a database administrator with direct SQL access or a developer to manually fix the record. This means operational problems require engineering-level intervention. That is not sustainable.

---

## WEAKNESS 4 — The File Storage Scaling Problem

### What it is:
Documents, maintenance photos, compliance files, and inspection photos are all stored in the file system. In development this works perfectly. In production with many Landlords and Tenants, it becomes a serious problem.

### Why it is a weakness:
The server's file system has finite disk space. When it fills up, uploads fail silently or with cryptic errors. There is no automatic cleanup of deleted files — the soft delete system marks the database record as deleted but the actual file remains on disk consuming space.

If the server is ever migrated, scaled horizontally, or replaced — all uploaded files are gone unless a separate file migration process was built. This is frequently discovered too late.

The recommended solution is cloud object storage — but that adds a paid external dependency, adds configuration complexity, and requires the team to understand S3-compatible APIs on top of everything else the system already demands.

---

## WEAKNESS 5 — The Tenant Is Entirely Dependent on the Landlord

### What it is:
A Tenant cannot join the system independently. They can only enter the system through a Landlord's invitation. They cannot self-register and search for their property. They cannot register and request to be connected to a Landlord.

### Why it is a weakness:
In reality, Tenants move in before some Landlords adopt new software. If a Landlord is slow to create the lease and send the invitation, the Tenant has a rent payment due but no way to access the system.

A Tenant cannot use the system to manage their side of the relationship unless the Landlord has already completed their setup. This creates a chicken-and-egg adoption problem — the Tenant experience is entirely blocked by the Landlord's speed and technical willingness.

---

## WEAKNESS 6 — No Dispute Resolution Mechanism

### What it is:
When a Landlord and Tenant disagree — about a charge, about a maintenance resolution, about a lease condition — the system has no formal dispute workflow.

### Why it is a weakness:
The chat system allows communication. The audit log provides evidence. But there is no structured dispute flow — no way for a Tenant to formally contest a late fee, no way for a Landlord to formally respond to a contested charge, no escalation path, no resolution recording.

The system provides the communication tools but not the workflow. Real property disputes require documentation, formal responses, and timestamped resolution records. The system provides none of this structure. It provides only the raw evidence that a dispute would use.

---

## WEAKNESS 7 — Performance Under Load Is Untested

### What it is:
The system has been designed for performance — pagination, indexed queries, caching on analytics, WebSocket efficiency. But it has never been load-tested. No one knows how it actually performs with 100 concurrent users.

### Why it is a weakness:
The WebSocket server, in particular, has a connection limit that depends on the server configuration. A default Flask-SocketIO setup on a modest server may handle 50 concurrent connections comfortably and collapse at 51. The payment webhook endpoint, which must process quickly and respond to the gateway within a timeout window, may queue up under concurrent load and begin timing out — causing the gateway to retry the webhook, causing duplicate processing attempts, causing the idempotency system to be stress-tested in ways it was never tested.

Performance under load is not a feature that can be verified by reading the code. It requires running tests. Those tests are not in the project scope. This is an honest gap.

---

## WEAKNESS 8 — The Chat is Not End-to-End Encrypted

### What it is:
Messages are transmitted over HTTPS/WebSocket TLS — encrypted in transit. But they are stored in the database as plain text. The messages table contains every message ever sent between every Landlord and every Tenant in plain, readable text.

### Why it is a weakness:
A database breach exposes every private conversation ever had on the platform. A maintenance technician who needs access to the database for a performance issue can read every message between every user.

For a system that handles sensitive financial discussions — "I cannot pay this month", "your security deposit will not be returned in full", "I am reporting you for illegal entry" — plain text message storage is a serious privacy weakness.

True end-to-end encryption where messages are encrypted on the sender's device and decrypted only on the receiver's device would solve this. But it is architecturally complex and far beyond the current scope. The weakness exists and is not resolved.

---

# 📊 THE COMPLETE WEAKNESS & RISK REGISTER

| # | Issue | Type | Severity | Currently Mitigated? |
|---|---|---|---|---|
| 1 | WebSocket silent disconnection | Technical Failure | HIGH | Partially |
| 2 | Payment webhook vulnerability window | Technical Failure | CRITICAL | Partially |
| 3 | Cron job silent failure | Technical Failure | HIGH | Partially |
| 4 | N+1 database query performance | Technical Failure | HIGH | Requires discipline |
| 5 | IDOR implementation gaps | Security Failure | CRITICAL | Requires full audit |
| 6 | Scope creep | Project Risk | HIGH | Controlled by prd.md |
| 7 | External dependency failures | Project Risk | MEDIUM | Graceful degradation |
| 8 | Single point of knowledge | Project Risk | HIGH | Team practice required |
| 9 | Deployment environment differences | Project Risk | HIGH | Requires staging env |
| 10 | No offline support | Weakness | MEDIUM | Out of scope |
| 11 | English only | Weakness | LOW | Deliberate limitation |
| 12 | No admin panel | Weakness | HIGH | Operational gap |
| 13 | File storage scaling | Weakness | MEDIUM | Cloud storage needed |
| 14 | Tenant dependent on Landlord | Weakness | MEDIUM | Design limitation |
| 15 | No dispute resolution workflow | Weakness | MEDIUM | Not in scope |
| 16 | Performance under load untested | Weakness | HIGH | Requires load testing |
| 17 | Chat stored as plain text | Weakness | MEDIUM | Encryption out of scope |

---

## 🎯 THE FINAL HONEST TRUTH

> Every weakness listed here is not a reason to abandon the project.
> It is a **map of where to grow next.**

The system as designed is genuinely powerful — 38 pages, real-time communication, automated billing, legal protection, security architecture, and analytics intelligence. That is real. That is significant.

But the weaknesses are also real. The cron jobs can fail silently. The WebSocket can disconnect without recovery. The lack of an admin panel will cause operational pain. The plain text message storage is a privacy gap. The dependency on Landlord adoption blocks Tenant access.

> **A senior engineer is not someone who builds systems with no weaknesses.**
> **A senior engineer is someone who knows exactly where every weakness is**
> **— and has a plan for every one of them.**

That is what this document gives you.
# 🛡️ Complete Solutions to Every Weakness, Problem, Struggle & Insecurity
## Rent & Lease Management System — The Full Resolution Document
### Every Problem Has a Solution. Every Weakness Has a Fix. Every Risk Has a Counter.

---

## 🧠 THE MINDSET BEFORE THE SOLUTIONS

> **A problem identified without a solution is just a complaint.**
> **A problem identified with a solution is engineering.**

Every weakness, every failure, every risk, every hard time documented in the previous analysis exists for one reason — so that this document can close every open loop. This is not a list of workarounds. These are permanent, architectural, production-grade solutions built into the system from this point forward.

---

# 🔴 SECTION 1 — SOLUTIONS TO CORE TECHNICAL FAILURES

---

## FAILURE 1 SOLUTION — WebSocket Silent Disconnection

### The Problem Restated:
WebSocket connections drop silently. Users think they are connected when they are not. Messages sent during disconnection are lost. The Tenant sends an urgent maintenance photo. It disappears. Trust is destroyed.

### The Complete Solution:

**Solution Layer 1 — Heartbeat Ping System:**
The server sends a ping signal to every connected client every 25 seconds. The client must respond with a pong within 10 seconds. If the pong does not arrive, the server marks the connection as dead and cleans up the session. The client simultaneously sends its own ping every 20 seconds. If no response arrives, the client knows the connection is dead before the user does. This is called a heartbeat system — the connection has a measurable pulse, and when the pulse stops, both sides know immediately.

**Solution Layer 2 — Automatic Reconnection with Exponential Backoff:**
The moment the client detects a lost connection, it does not immediately flood the server with reconnection attempts. It waits 1 second and tries. If that fails, it waits 2 seconds. Then 4. Then 8. Then 16. Then it caps at 30 seconds and tries every 30 seconds indefinitely. This exponential backoff prevents a situation where 500 clients all lose connection simultaneously and all hammer the server with reconnection attempts at the same moment — which would crash the server. The reconnection is automatic, invisible to the user, and smart about not making the problem worse.

**Solution Layer 3 — Connection Status Indicator in the UI:**
The chat interface has a visible connection status indicator. When connected, the header shows a green dot. When reconnecting, it shows an amber dot with the text "Reconnecting..." When offline, it shows a red dot with "Connection lost — messages will be sent when connection is restored." The user always knows the state of their connection. They are never in the dark.

**Solution Layer 4 — Outbox Queue for Unsent Messages:**
When a user sends a message and the connection is down, the message is not lost. It goes into a local outbox queue — stored in memory. When the connection is restored, the outbox is flushed automatically — all queued messages are sent in order. The user sees their message in a "pending" visual state (slightly grayed out with a clock icon) until confirmation arrives from the server. On confirmation, it becomes fully visible with the standard timestamp. The message is never lost.

**Solution Layer 5 — Server-Side Message Persistence Before Delivery:**
Every message is written to the database the moment the server receives it — before it is pushed to the recipient. This means if the recipient is offline, the message is not lost. When they reconnect, the server detects the reconnection, queries all undelivered messages, and pushes them in order. The database is the source of truth for every message ever sent. The WebSocket is the delivery mechanism — fast when available, but never the only copy.

---

## FAILURE 2 SOLUTION — Payment Webhook Vulnerability Window

### The Problem Restated:
There is a dangerous gap between payment submission and webhook confirmation. Tenants can be charged without their invoice updating. Fake webhooks can mark invoices as paid without money moving.

### The Complete Solution:

**Solution Layer 1 — Webhook Signature Verification:**
Every payment gateway — Stripe, Paystack — signs their webhook payloads with a secret key. When a webhook arrives at the system's webhook endpoint, the first thing the backend does — before reading any data from the payload — is verify the cryptographic signature. The gateway provides the signature in a request header. The backend re-computes the expected signature using the raw request body and the webhook secret stored in the environment variable. If the computed signature does not match the header signature, the webhook is rejected with a 403 response and logged to the audit trail as a security event. A fake webhook cannot replicate this signature without knowing the secret. This makes fake webhook attacks categorically impossible.

**Solution Layer 2 — Idempotent Webhook Processing:**
The gateway may send the same webhook multiple times — particularly if the first delivery times out or receives a slow response. The system must process each unique payment event exactly once. Every webhook payload contains a unique event ID from the gateway. Before processing any webhook, the system checks the database for a record of that event ID. If it already exists, the webhook is acknowledged with a 200 response and processing stops immediately. Nothing changes in the database. The second webhook is swallowed safely. This prevents double-payment recording from webhook retries.

**Solution Layer 3 — Pending State During the Confirmation Window:**
When a Tenant submits a payment, the invoice is not marked as Outstanding and it is not marked as Paid. It is marked as Pending. The Tenant's UI shows a clear "Payment Processing" state — not a success state and not a failure state. The automatic late fee cron job skips invoices in Pending state. The Landlord's overdue alerts skip Pending invoices. The Tenant sees a clear "Your payment is being confirmed. This usually takes a few seconds." message. When the webhook arrives and confirms the charge, the status moves from Pending to Paid. If the webhook signals failure, it moves back to Outstanding with a failure notification. The system never makes a financial decision based on the browser submission alone.

**Solution Layer 4 — Daily Reconciliation Job:**
Every morning at 6 AM, a lightweight reconciliation cron job runs. It queries the payment gateway's API for all transactions in the last 24 hours. It compares each transaction against the database records. Any transaction that the gateway shows as successful but the database shows as Outstanding or Pending is investigated and flagged in the audit log for manual review. This catches the rare case where the webhook arrived but was silently dropped. The reconciliation job is the safety net beneath the webhook system.

**Solution Layer 5 — Webhook Endpoint Protection:**
The webhook endpoint is rate limited separately from all other endpoints. It is not authenticated with JWT — the gateway cannot provide a JWT. But it is protected by webhook signature verification (Layer 1) and an IP allowlist — only requests from the gateway's documented IP ranges are accepted. All other IPs receive a 403 response immediately.

---

## FAILURE 3 SOLUTION — Cron Job Silent Failure

### The Problem Restated:
Cron jobs fail silently at midnight. Late fees are not applied. Or they run twice and double-charge tenants. No one is watching.

### The Complete Solution:

**Solution Layer 1 — Job Execution Logging Table:**
Every cron job execution — successful or failed — writes a record to a dedicated cron_log table. The record includes the job name, the start time, the end time, the number of records processed, the number of records skipped, the number of errors encountered, and the final status. Every morning, this table is the first place to look to verify that the previous night's jobs ran correctly. If a job failed, the record shows exactly what failed and at what point.

**Solution Layer 2 — Idempotency Flag on Every Automated Action:**
The late fee job checks the `late_fee_applied` boolean column before applying any fee. If it is already TRUE, the job skips that invoice entirely. This means running the job twice produces identical results to running it once. No invoice ever gets a double late fee regardless of how many times the job runs. This is the idempotency principle applied directly to financial automation.

**Solution Layer 3 — Distributed Lock on Job Execution:**
Before any cron job begins executing its main logic, it acquires a database-level lock for that specific job type. The lock record is written to a `job_locks` table with the job name and the acquiring timestamp. If a second instance of the same job starts — because of a server restart mid-execution or a scheduler misconfiguration — it checks the lock table, finds the lock already held, and exits immediately without executing. The lock is released when the job completes or after a maximum lock duration (for example, 10 minutes) to prevent deadlocks from crashed jobs.

**Solution Layer 4 — Retry Logic with Maximum Attempts:**
If a cron job encounters an error — a database timeout, a network failure, an unexpected exception — it does not silently stop. It logs the error, waits a configured backoff period, and retries up to 3 times. If all 3 attempts fail, the job writes a FAILED status to the cron_log table and creates a high-priority notification in the audit log. This notification is visible the next time any user with system access logs in — providing visibility into the failure even without a dedicated monitoring system.

**Solution Layer 5 — Pre-Job Validation:**
Before the late fee job processes any invoices, it runs a quick validation query to verify the database is responsive and the data looks sane — for example, checking that the count of overdue invoices is within a reasonable range. If the query returns 0 overdue invoices on the 15th of the month when there are normally dozens, this is anomalous. The job logs a warning and exits rather than proceeding with potentially corrupt data.

---

## FAILURE 4 SOLUTION — N+1 Database Query Performance

### The Problem Restated:
The Landlord Dashboard makes 61+ separate database queries to load data for 20 properties. In production it loads in 6 seconds. Users abandon it.

### The Complete Solution:

**Solution Layer 1 — Consolidated JOIN Queries:**
The dashboard never makes one query per property. It makes one query total that joins properties, leases, invoices, and tenants simultaneously and returns all required data in a single database round trip. The query uses LEFT JOINs so that properties with no active lease still appear. It uses GROUP BY and COUNT to aggregate maintenance tickets per property. The result is a single structured response containing everything the dashboard needs. One network round trip to the database instead of sixty.

**Solution Layer 2 — Select Only Required Fields:**
Every query explicitly names every column it needs. Never `SELECT *`. If the dashboard needs property address, unit number, occupancy status, and monthly rent — the query requests exactly those four columns. The password_hash, the created_at, the updated_at, and every other column the dashboard does not use are never fetched, never transmitted, never processed. This reduces data transfer volume and processing time proportionally.

**Solution Layer 3 — Database Indexes on Every Frequently Queried Column:**
Every column that appears in a WHERE clause, a JOIN condition, or an ORDER BY clause in a frequently executed query has an index. The landlord_id column on the properties table is indexed. The tenant_id column on the invoices table is indexed. The status column on the leases table is indexed. The due_date column on the invoices table is indexed. These indexes mean the database does not scan every row — it jumps directly to the matching rows. A query that scans 50,000 rows without an index runs in 800ms. The same query with an index runs in 2ms.

**Solution Layer 4 — Analytics Query Caching:**
The analytics page runs the most expensive queries in the system — 12-month revenue aggregations, maintenance category counts, payment timeliness calculations. These queries run against potentially large datasets. But the underlying data does not change every second. A 5-minute cache on analytics query results means the expensive aggregation runs once every 5 minutes — not once every time the page loads. The cache key is the landlord's user ID plus the query type. Cache invalidation happens when a new payment is recorded for that landlord. The analytics are current within 5 minutes — more than accurate enough for a monthly revenue overview.

**Solution Layer 5 — Pagination Enforced at the Query Level:**
Every query that returns a list — invoices, properties, notifications, chat history, maintenance tickets — has a mandatory LIMIT clause enforced at the data retrieval layer. The API never accepts a request to return all records with no limit. The default page size is 20. The maximum page size is 100. Infinite scroll and "Load More" buttons on the frontend request the next page. The database never returns more rows than required for the current view.

---

## FAILURE 5 SOLUTION — IDOR Implementation Gaps

### The Problem Restated:
IDOR protection missed complex ownership chains. A Tenant could potentially access another Tenant's document through a shared property_id relationship.

### The Complete Solution:

**Solution Layer 1 — Ownership Matrix Documentation:**
Before writing a single IDOR check, every resource in the system is mapped in an ownership matrix. The matrix defines for every resource type — invoice, lease, document, maintenance ticket, message, inspection, compliance document — who the primary owner is, who the secondary owner is, what relationship makes access legitimate, and what access should be denied. This matrix is documented in security.md and reviewed before every new endpoint is written.

**Solution Layer 2 — Resource-Specific Ownership Verification Functions:**
Each resource type has a dedicated ownership verification function. `verify_invoice_access(user_id, invoice_id)` checks that the user is either the tenant on the invoice OR the landlord on the invoice. `verify_document_access(user_id, document_id)` checks that the user is the direct owner of the document record — not just associated with the property. These functions are the single source of truth for access decisions on their resource type. They are called everywhere that resource is accessed.

**Solution Layer 3 — Query-Level Ownership Scoping:**
Every SELECT, UPDATE, and DELETE query for user-owned resources includes the ownership condition directly in the WHERE clause. `WHERE invoice.tenant_id = :authenticated_user_id OR invoice.landlord_id = :authenticated_user_id`. This means even if the middleware check is bypassed, the database query returns no data for unauthorized requests. The data is invisible at the storage level. This is defence in depth applied directly to the data layer.

**Solution Layer 4 — Regular Security Review Checklist:**
Every time a new API endpoint is added, a security checklist is completed before the endpoint is considered done. The checklist includes: Does this endpoint expose a resource? Has ownership been verified? Has the verification been tested with a user who should be denied? Has the denial been confirmed to return 403 and log to audit? No endpoint ships without this checklist signed off.

**Solution Layer 5 — Automated IDOR Testing:**
A set of security test cases is written that specifically test IDOR scenarios. Test Case 1: Tenant A tries to access Tenant B's invoice. Expected result: 403. Test Case 2: Tenant A tries to download Tenant B's document. Expected result: 403. Test Case 3: Tenant A tries to view Tenant B's maintenance ticket. Expected result: 403. These tests run automatically every time new code is deployed. If any test fails, the deployment is blocked.

---

# 🟠 SECTION 2 — SOLUTIONS TO CORE PROJECT RISKS

---

## RISK 1 SOLUTION — Scope Creep

### The Complete Solution:

**Solution 1 — The Frozen PRD Rule:**
The `prd.md` file is the absolute authority on what is in scope. Once Phase 0 is complete and the PRD is signed off, no new feature can be added to the current build without removing an existing feature of equal complexity. Every suggested new feature goes into a `backlog.md` file — acknowledged, documented, and deferred. It is not rejected. It is deferred. This respects the idea while protecting the timeline.

**Solution 2 — Weekly Scope Audit:**
Every week during the plan review, the team answers one question: "Did we build anything this week that is not in prd.md?" If yes — why? Was it necessary? Does it replace something in scope or add to it? This question, asked weekly, catches scope drift before it becomes scope explosion.

**Solution 3 — The MVP Gate:**
Before Phase 9 testing begins, every in-scope feature must be functional at MVP level. Incomplete features are more damaging than missing features. A half-working payment system is worse than no payment system — it suggests the system was not engineered, it was rushed. If time is short, complete fewer features completely rather than more features partially.

---

## RISK 2 SOLUTION — External Integration Dependency Failures

### The Complete Solution:

**Solution 1 — Graceful Degradation Design:**
Every external dependency — payment gateway, SMTP service, file storage — is wrapped in a try-catch with a defined fallback behavior. If the payment gateway is unavailable, the Tenant sees: "Payment processing is temporarily unavailable. Your payment is not due at this moment. Please try again shortly." The system continues operating. Only the payment feature is degraded — not the entire platform.

**Solution 2 — Mock/Stub Interfaces for Development:**
During development and testing, all external services use mock implementations. A mock email service logs emails to a file instead of sending them. A mock payment gateway accepts any test card and returns a success response. This means the system can be fully demonstrated and tested without any live external accounts. The presentation works even if Stripe's sandbox is down.

**Solution 3 — Environment-Specific Configuration:**
All external service credentials are stored in environment variables and are swappable between environments without code changes. Development uses sandbox credentials. Staging uses sandbox credentials. Production uses live credentials. Switching environments never requires touching code — only configuration.

---

## RISK 3 SOLUTION — Single Point of Knowledge

### The Complete Solution:

**Solution 1 — Mandatory Code Documentation:**
Every function in the system has a clear comment block explaining what it does, what it receives, what it returns, and why it exists. Not how — the code shows how. The comment explains the why and the what. Any team member reading the comment can understand the function's purpose without needing to understand its implementation details.

**Solution 2 — Knowledge Transfer Sessions:**
After each major feature is completed, the person who built it spends 30 minutes walking the rest of the team through it. Not a code review — a conceptual walkthrough. "Here is what this feature does. Here is why it was built this way. Here is where it lives in the folder structure. Here is what would break if this function failed." Every person on the team can explain every major feature — even if they did not build it.

**Solution 3 — Pair Building on Critical Features:**
The WebSocket implementation and the payment integration — the two most complex and most fragile features — are built by two people together, not one person alone. Two people understand the implementation. Two people can debug it. Two people can explain it during a presentation defense.

---

## RISK 4 SOLUTION — The Deployment Environment Difference

### The Complete Solution:

**Solution 1 — Staging Environment from Week 1:**
A staging server that mirrors the production environment is set up in Phase 0 — not Phase 10. Every feature is deployed to staging as it is completed. Problems are discovered incrementally over 15 weeks instead of all at once in Week 15.

**Solution 2 — Environment Parity Checklist:**
A deployment checklist documents every difference between development and production. SQLite vs PostgreSQL. Local file system vs cloud storage. localhost WebSocket vs production WebSocket domain. HTTP vs HTTPS. Each difference on the list has a specific migration task associated with it that is completed before the final deployment.

**Solution 3 — Docker Containerization:**
The entire application — Python backend, database, scheduler — runs inside Docker containers. A container is identical on the developer's laptop and on the production server. "It works on my machine" becomes "the container works, and the container is the same everywhere." This eliminates the class of environment difference problems entirely.

---

# 🔵 SECTION 3 — SOLUTIONS TO ALL PROJECT WEAKNESSES

---

## WEAKNESS 1 SOLUTION — No Offline Support

### The Complete Solution:

**Solution 1 — Service Worker Caching for Static Assets:**
A service worker is registered for the Tenant portal. It caches all static assets — HTML, CSS, JavaScript, fonts, icons — on first load. When the user is offline, the app shell loads from the service worker cache. The user sees the application structure, not a blank screen or a browser error page.

**Solution 2 — Cached Data for Critical Read-Only Views:**
The Tenant's current balance, lease details, and most recent payment history are cached in the browser using the Cache API on every successful load. When offline, these cached values are displayed with a clear banner: "You are currently offline. Showing the last updated information from [timestamp]." The Tenant can still see their balance, check their lease, and view payment history — even without connectivity.

**Solution 3 — Offline Action Queue:**
Actions taken while offline — a chat message typed, a maintenance ticket drafted — are stored in a local queue. When connectivity returns, the queue is automatically flushed. The user is informed: "You were offline. 1 message has been sent now that your connection is restored."

---

## WEAKNESS 2 SOLUTION — English Only / No Internationalization

### The Complete Solution:

**Solution 1 — Externalized String Architecture:**
All user-facing text — every label, every error message, every button, every notification — is moved out of the HTML and JavaScript files into a dedicated strings file. Instead of hardcoding "Pay Rent" in the button, the button references a string key: `strings.tenant.payRent`. The strings file currently contains only English values. But the architecture is ready for a second language to be added by creating a second strings file with the same keys and different values. Internationalization is not implemented, but the system is architected to accept it with minimal rework.

**Solution 2 — Date and Currency Formatting via Browser APIs:**
All date formatting and currency formatting uses the browser's built-in Internationalization API (`Intl.DateTimeFormat` and `Intl.NumberFormat`) rather than hardcoded formats. Dates display in the format appropriate for the user's browser locale. Currency displays with the correct symbol and decimal convention. This is locale-awareness without full internationalization — a meaningful improvement that costs very little to implement.

---

## WEAKNESS 3 SOLUTION — No Admin Panel

### The Complete Solution:

**Solution 1 — A Minimal System Operations Interface:**
A protected, internal-only system operations page is created — not an admin panel for users, but an operations console for the development team and system maintainers. It is accessible only from a specific IP address (the developer's server access) or via a separate authentication mechanism. It provides exactly four capabilities: manually verify a user account, manually mark a payment as reconciled, manually correct a lease data error, and view the live audit log. Nothing more. This solves every operational emergency identified without creating a full admin portal.

**Solution 2 — Self-Service Recovery Flows:**
Rather than requiring admin intervention for common problems, self-service flows are built for the most frequent scenarios. Expired verification email? The verification page has a "Resend Verification Email" button that works indefinitely. Invitation link expired? The Landlord can resend the invitation from the lease management page. Locked out of account? The forgot password flow works independently of verification status. Every scenario that would require admin intervention is given a self-service solution first.

**Solution 3 — Database Script Library:**
For the scenarios that truly require direct database intervention, a library of safe, tested, documented SQL scripts is maintained. `manually_verify_user.sql`, `reconcile_payment.sql`, `correct_lease_dates.sql`. Each script has comments explaining when to use it, what it changes, and what to verify after running it. The operations team runs these scripts directly — but safely, with documentation, not by guessing at SQL commands under pressure.

---

## WEAKNESS 4 SOLUTION — File Storage Scaling

### The Complete Solution:

**Solution 1 — Abstract the Storage Interface from Day One:**
The file storage system is designed behind an interface from the very first upload. The business logic calls `storage_service.upload(file)` and `storage_service.download(file_path)`. In development, the storage service writes to the local file system. In production, the storage service writes to cloud object storage. The business logic never changes. Only the storage service implementation changes. Switching from local to cloud storage requires changing one file — not rewriting the upload system.

**Solution 2 — Soft Delete with Scheduled Cleanup:**
When a document is deleted, the database record is soft-deleted (deleted_at populated). The actual file is not deleted immediately. Instead, a weekly cleanup job runs that identifies all soft-deleted document records older than 30 days and physically removes the files from storage. This gives a 30-day grace period to recover accidentally deleted files while still freeing storage space consistently.

**Solution 3 — File Size Limits and Type Restrictions:**
Every upload endpoint enforces a maximum file size — 10MB for documents, 5MB for maintenance photos, 2MB for compliance documents. Oversized uploads are rejected at the API boundary before they reach storage. Allowed file types are restricted by both extension and MIME type. These limits prevent storage from being consumed by accidental or malicious large uploads.

---

## WEAKNESS 5 SOLUTION — Tenant Dependent on Landlord

### The Complete Solution:

**Solution 1 — Tenant Pre-Registration with Lease Linking:**
A Tenant can visit the platform and begin registration independently, entering their name, email, and password. Their account is created in a `pending_lease_link` status. They see a holding screen: "Your account is ready. Please ask your Landlord to send you a lease invitation to complete setup." When the Landlord sends the invitation to that email address, the invitation is automatically linked to the existing account rather than requiring a fresh registration. The Tenant's waiting period is reduced because their account already exists.

**Solution 2 — Tenant Registration Code System:**
When a Landlord creates a lease, the system generates a short alphanumeric code — for example, `RENT-4B92`. The Landlord gives this code to the Tenant in person, by text, or verbally. The Tenant visits the registration page, enters the code, and their account is automatically linked to the correct lease without needing a clickable invitation link in an email. This solves the problem of Tenants who did not receive the email — the code works independently of email delivery.

---

## WEAKNESS 6 SOLUTION — No Dispute Resolution Mechanism

### The Complete Solution:

**Solution 1 — Formal Dispute Flow on Financial Events:**
Every invoice and every late fee has a "Dispute This Charge" button for the Tenant. Tapping it opens a structured form — not a free-text chat message — that requires the Tenant to select a dispute reason from a defined list, provide a brief description, and submit. The dispute creates a formal dispute record linked to the invoice. The Landlord receives a notification of the dispute. The Landlord can either accept it (reversing the charge), reject it (with a mandatory written reason), or respond with additional information. Every action in the dispute is timestamped and appended to the dispute record. The dispute record is immutable after resolution.

**Solution 2 — Audit Evidence Attachment:**
When a dispute is raised, the system automatically attaches all relevant evidence to the dispute record — the payment history for that invoice, the lease terms showing the late fee clause, the relevant audit log entries, and any maintenance tickets that may be related. Both parties see the same evidence. Disputes are resolved with facts, not with memory.

---

## WEAKNESS 7 SOLUTION — Performance Under Load Is Untested

### The Complete Solution:

**Solution 1 — Load Testing with Locust:**
A load testing script using Python's Locust library simulates concurrent users against the most critical endpoints — login, dashboard load, payment submission, WebSocket connection. The test defines three user scenarios: 10 concurrent users (expected normal load), 50 concurrent users (expected peak load), and 100 concurrent users (stress test). The tests are run against the staging environment before any production deployment. Response time targets — dashboard under 2 seconds, payment under 5 seconds — must be met at 50 concurrent users before the system is considered production-ready.

**Solution 2 — Database Query Performance Profiling:**
Every query that runs more than 5 times per minute is profiled using the database's query execution plan. Any query with a full table scan on a table with more than 1,000 rows is flagged for index optimization. This profiling is run after inserting realistic seed data — 100 users, 50 properties, 200 invoices, 500 notifications — to simulate real production data volumes. Performance problems discovered with 10 rows of test data are not real. Performance problems discovered with 50,000 rows are real.

**Solution 3 — WebSocket Connection Limit Configuration:**
The Flask-SocketIO server is configured with an explicit maximum connection limit set below the server's actual capacity — for example, 80% of maximum. When the limit is reached, new connection attempts receive a 503 response with a "Server at capacity, please try again shortly" message rather than crashing the server. The system degrades gracefully under extreme load.

---

## WEAKNESS 8 SOLUTION — Chat Stored as Plain Text

### The Complete Solution:

**Solution 1 — Application-Level Encryption for Message Content:**
Message content is encrypted before being written to the database using AES-256 encryption. The encryption key is stored in an environment variable — never in the database. The message text column stores ciphertext, not plain text. When messages are retrieved, the business logic layer decrypts them before returning them to the API. A database breach exposes ciphertext — unreadable without the encryption key. A database administrator querying the messages table directly sees encrypted data, not conversations.

**Solution 2 — Key Rotation Strategy:**
The encryption key can be rotated periodically. A key rotation job re-encrypts all stored messages with the new key. The old key is retired. This means even if an old key is compromised, messages encrypted with the rotated key remain protected.

**Solution 3 — Minimum Data Retention Policy:**
Messages older than 12 months are automatically archived — moved from the active messages table to a compressed archive and removed from the standard message history view. This limits the volume of readable message data in the active database at any time. The archive retains legal records. The active table retains recent, operationally relevant conversations.

---

# 🟡 SECTION 4 — SOLUTIONS TO THE UPS AND DOWNS

---

## THE DOWNS — How to Survive and Solve Each One

---

## DOWN 1 SOLUTION — The Database Schema Crisis

### The Complete Solution:

**Prevention — Schema Review Gate Before Phase 1:**
The database schema is treated as the most important document in the project. Before writing a single line of application code, the complete schema — every table, every column, every constraint, every relationship — is reviewed against every feature in the PRD. Every scenario is walked through: "When a Tenant pays rent, which tables are written to? In what order? Are all necessary columns present? Are all necessary constraints defined?" This review happens in Phase 0 and is a hard gate before Phase 1 begins.

**Recovery — Schema Migration System:**
If a schema change is unavoidable after development has started, a migration system tracks the change. Every schema modification is a numbered migration file — `002_add_late_fee_applied_column.sql`. Migrations run in order. The current schema state is always the result of running all migrations in sequence. Rollback migrations are written alongside forward migrations — every change can be undone. This makes schema evolution manageable rather than catastrophic.

---

## DOWN 2 SOLUTION — The Security Failure Discovery

### The Complete Solution:

**Prevention — Security-First Endpoint Review:**
Every new API endpoint is reviewed against the IDOR checklist before being merged into the codebase. The checklist is a required step — not an optional review. It cannot be skipped.

**Recovery — Security Audit Sprint:**
When a vulnerability is discovered, a dedicated security audit sprint is triggered immediately. Every endpoint in the system is reviewed in sequence against the ownership matrix. The audit takes priority over all feature development. It is not a distraction — it is the most important work happening in the project at that moment. The audit is documented in the audit log so that the remediation is traceable.

---

## DOWN 3 SOLUTION — The Week Before Presentation: Nothing Works Together

### The Complete Solution:

**Prevention — End-to-End Journey Testing After Every Phase:**
After every phase is complete, one complete user journey is tested end-to-end. After Phase 2, test: Landlord registers → verifies email → logs in → adds a property → creates a lease. After Phase 3, test: Tenant accepts invitation → logs in → sees balance → submits payment → receives receipt. These journey tests catch integration failures early — when they are cheap to fix — not in Week 14 when they are expensive.

**Recovery — Systematic Layer-by-Layer Debugging:**
When the integrated system fails, the debugging process starts at Layer 9 (database) and works upward. Is the data correct in the database? Yes — move to Layer 8. Is the query returning the right data? Yes — move to Layer 7. Is the business logic processing it correctly? This systematic approach finds the broken layer faster than randomly looking at code. Every layer is interrogated in sequence until the failure is located.

---

## DOWN 4 SOLUTION — The Mobile Responsiveness Reckoning

### The Complete Solution:

**Prevention — Real Device Testing After Every Tenant Page:**
Every Tenant page is tested on a real mobile device — not a browser simulator — before it is considered complete. The specific devices tested are iPhone SE (smallest common iPhone), iPhone 12 (standard), and a mid-range Android device. The specific scenarios tested include the keyboard opening over input fields, the browser navigation bar overlapping action buttons, and horizontal scrolling triggering on narrow screens.

**Recovery — The Safe Area Inset Fix:**
The browser navigation bar issue on mobile is solved with CSS environment variables — `padding-bottom: env(safe-area-inset-bottom)` — which automatically accounts for the bottom navigation bar on iPhones and Android devices. This is a one-line CSS fix that prevents the most common mobile layout failure permanently.

---

## DOWN 5 SOLUTION — The Moment the Team Realizes the Project Is Too Big

### The Complete Solution:

**Prevention — The MVP Priority Stack:**
At the start of the project, every feature is categorized into three tiers. Tier 1 — must exist for the system to be usable at all (authentication, rent payment, lease management). Tier 2 — significantly improves the system but is not required for a working demonstration (real-time chat, analytics, cron jobs). Tier 3 — enhances the experience but can be deferred (dispute resolution, compliance documents, building management).

If the project falls behind schedule, Tier 3 features are cut first. Then Tier 2. Tier 1 is never cut. A demonstration of a complete, working Tier 1 system is more impressive than a demonstration of 38 half-finished pages.

**Recovery — Scope Reduction Decision Protocol:**
When the team realizes they are behind, a structured decision is made: what is removed from scope, and what is elevated to ensure what remains is excellent. The removed features go into `backlog.md` with notes explaining why they were deferred and how they would be built. This demonstrates engineering maturity — knowing what to cut and why is as important as knowing what to build.

---

# 📊 THE COMPLETE SOLUTIONS REGISTER

| # | Problem | Solution | Status After Solution |
|---|---|---|---|
| 1 | WebSocket silent disconnection | Heartbeat + reconnection + outbox queue + server persistence | Fully Resolved |
| 2 | Payment webhook vulnerability | Signature verification + idempotency + pending state + reconciliation | Fully Resolved |
| 3 | Cron job silent failure | Execution logging + idempotency flags + distributed lock + retry logic | Fully Resolved |
| 4 | N+1 query performance | JOIN queries + field selection + indexes + caching + pagination | Fully Resolved |
| 5 | IDOR implementation gaps | Ownership matrix + resource functions + query scoping + automated tests | Fully Resolved |
| 6 | Scope creep | Frozen PRD + weekly audit + MVP gate | Controlled |
| 7 | External dependency failures | Graceful degradation + mock interfaces + env configuration | Fully Resolved |
| 8 | Single point of knowledge | Documentation + knowledge transfer + pair building | Fully Resolved |
| 9 | Deployment environment difference | Staging from Week 1 + parity checklist + Docker | Fully Resolved |
| 10 | No offline support | Service worker + cached data + offline queue | Substantially Resolved |
| 11 | English only | Externalized strings + Intl API + architecture ready | Architecture Ready |
| 12 | No admin panel | Operations console + self-service flows + script library | Operationally Resolved |
| 13 | File storage scaling | Storage interface abstraction + cleanup job + size limits | Fully Resolved |
| 14 | Tenant dependent on Landlord | Pre-registration flow + registration code system | Fully Resolved |
| 15 | No dispute resolution | Formal dispute flow + audit evidence attachment | Fully Resolved |
| 16 | Performance under load untested | Locust load testing + query profiling + connection limits | Fully Resolved |
| 17 | Chat stored as plain text | AES-256 encryption + key rotation + retention policy | Fully Resolved |
| 18 | Database schema crisis | Schema review gate + migration system | Prevented and Recoverable |
| 19 | Security failure discovery | Security-first checklist + audit sprint protocol | Prevented and Recoverable |
| 20 | Integration failure before presentation | Phase-end journey testing + layer-by-layer debugging | Prevented and Recoverable |
| 21 | Mobile responsiveness failure | Real device testing + safe area CSS + per-page testing | Fully Resolved |
| 22 | Project too big realization | MVP priority stack + scope reduction protocol | Controlled |

---

## 🎯 THE FINAL TRUTH ABOUT SOLUTIONS

> Solutions do not eliminate problems.
> They transform **catastrophic failures** into **manageable events**.

A WebSocket that drops is still a problem. But with heartbeat detection, automatic reconnection, an outbox queue, and server-side message persistence — it is a problem that the system recovers from in under 3 seconds, invisibly, with no data loss. The user never knows it happened.

A cron job that fails is still a problem. But with execution logging, idempotency flags, retry logic, and a distributed lock — it is a problem that surfaces in a log file the next morning, can be re-run safely, and never charges a Tenant twice.

> **The measure of a great system is not that nothing goes wrong.**
> **The measure of a great system is that when something goes wrong,**
> **the system already knew what to do about it.**

That is what every solution in this document achieves.
# 🔧 Complete Software Engineering Maintenance Guide
## Rent & Lease Management System — The Full Maintenance Bible
### Every Layer | Every System | Every Schedule | Every Protocol

---

## 🧠 THE ENGINEERING TRUTH ABOUT MAINTENANCE

> **Building the system is the beginning, not the end.**
> Every professional software engineer knows that a system launched without a maintenance plan is a system with a planned expiry date.

Software maintenance is not fixing bugs. That is one part of it. Software maintenance is the complete, ongoing discipline of keeping a living system correct, secure, performant, observable, and aligned with the needs of its users — permanently.

There are four types of software maintenance recognized in software engineering:

**Corrective Maintenance** — Fixing defects and failures discovered after deployment.
**Adaptive Maintenance** — Updating the system when its environment changes — new browser versions, Python updates, payment gateway API changes.
**Perfective Maintenance** — Improving the system based on user feedback and performance data — faster queries, better UX, cleaner code.
**Preventive Maintenance** — Proactively improving the system to prevent future failures — refactoring fragile code, adding monitoring, strengthening security.

This document covers all four across every layer of the 9-layer architecture, every feature pillar, and every known weakness of the Rent & Lease Management System.

---

# 🗓️ PART 1 — MAINTENANCE SCHEDULES
### *When maintenance happens, what is checked, and why*

---

## SCHEDULE 1 — DAILY MAINTENANCE (Every Day, No Exceptions)

### Daily Task 1 — Cron Job Execution Verification
Every morning, the first engineering task is checking that the previous night's automated jobs ran correctly.

What is checked:
The `cron_log` table is queried for the previous night's executions. Every scheduled job — the late fee application, the lease expiry scanner, the rent reminder sender, and the auto-pay processor — must have a record showing status SUCCESS. Any record showing FAILED or PARTIAL triggers an immediate investigation before the business day begins.

Why this matters:
A late fee cron job that silently failed means dozens of Tenants were not charged correctly. The Landlord's financial records are wrong. The automated enforcement that the entire billing system depends on did not happen. Discovering this at 9 AM is recoverable. Discovering it at 5 PM after the Landlord has already seen wrong data is a trust problem.

What the check looks like:
The cron_log query returns the job name, start time, end time, records processed, errors encountered, and final status. A clean morning report shows all four jobs with SUCCESS status, zero errors, and a processing count that matches the expected volume based on the current number of active leases and invoices.

---

### Daily Task 2 — Error Log Review
The application error log — `logs/app.log` — is reviewed every morning for any exceptions, unexpected errors, or warning patterns from the previous 24 hours.

What is looked for:
Any unhandled exception is a bug waiting to become a user complaint. Any database connection timeout is a performance signal. Any repeated authentication failure from the same IP is a potential brute force attempt. Any file upload failure is a Tenant who could not submit compliance documents. These signals in the log are invisible to users but visible to engineers. The log is read every morning because that is when these signals are cheapest to act on.

What action is taken:
Critical errors — payment processing failures, database write failures, authentication system errors — trigger immediate investigation. Warning-level patterns — repeated 404 errors on the same URL, elevated response times on specific endpoints — are logged in the issue tracker for resolution within the week.

---

### Daily Task 3 — Audit Log Security Review
The `audit_log` table is scanned daily for security events. Specifically:

All 403 Forbidden responses — these indicate IDOR attempts. A single 403 from an unfamiliar user is curiosity. Ten 403 responses from the same user in five minutes is a probing attack. A hundred 403 responses from the same IP in one hour is an automated attack.

All 429 Too Many Requests responses — these indicate rate limiting is working. But a sustained pattern of 429 responses from many different IPs simultaneously may indicate a distributed attack that the per-IP rate limit is not designed to stop.

Failed login attempts — more than 5 failed logins for any single account within 15 minutes is a credential stuffing attempt targeting that specific account. The account is reviewed and the user is notified.

---

### Daily Task 4 — Payment Reconciliation Check
The payment reconciliation job — which runs automatically at 6 AM — produces a report. The report is reviewed for any discrepancies between the payment gateway's transaction records and the system's invoice records.

Any invoice showing Outstanding status for a gateway transaction that the payment gateway shows as Successful is an immediate priority. This means money was collected but the invoice was not updated. The Tenant was charged. The system disagrees. This must be resolved the same day it is discovered, before the Tenant receives a late fee reminder for a payment they already made.

---

## SCHEDULE 2 — WEEKLY MAINTENANCE (Every Week)

### Weekly Task 1 — Database Performance Review
Every week, the database slow query log is reviewed. Any query that took more than 500 milliseconds to execute is examined. The execution plan is analyzed. If the query is performing a sequential scan on a table with more than 10,000 rows, an index optimization is planned.

Database growth is also tracked weekly. The size of each table is recorded. When a table grows beyond expected projections, the pagination settings and archiving schedule are reviewed. A notifications table that is growing 20% faster than expected means more system events are being generated than anticipated — which may indicate a loop or a configuration problem in the notification logic.

---

### Weekly Task 2 — Dependency Vulnerability Scan
Every Python package in `requirements.txt` and every JavaScript library used in the frontend is scanned against the National Vulnerability Database.

For Python: `pip audit` is run. Any package with a known security vulnerability is flagged for update.

For JavaScript: Any CDN-loaded library — Chart.js — is checked against its current published version. If the CDN URL references a specific version and that version has a security advisory, the URL is updated to the patched version.

Why this matters:
The system was built with specific library versions. Vulnerabilities are discovered in those versions after the system ships. A vulnerability in a version of Flask or PyJWT that the system uses can be exploited by an attacker who knows the version. Staying current with security patches is the single most effective preventive maintenance action available.

---

### Weekly Task 3 — WebSocket Connection Health Review
The WebSocket server metrics are reviewed weekly. Specifically:

Average number of concurrent connections throughout the week. If this number is approaching the configured maximum connection limit, the limit needs to be raised or the infrastructure needs to be scaled.

Connection drop rate — what percentage of connections dropped and reconnected during the week. A healthy system has a reconnection rate below 5%. A rate above 15% suggests network instability, server memory pressure, or a bug in the heartbeat system.

Average message delivery latency — the time between a message being sent and the server acknowledgement being returned. This should be consistently under 100 milliseconds. Spikes above 300 milliseconds indicate server processing delays that will be perceived by users as chat lag.

---

### Weekly Task 4 — Storage Usage Review
File storage usage is checked weekly. The total storage consumed by documents, maintenance photos, compliance files, and inspection photos is measured. The growth rate from the previous week is calculated. This growth rate is projected forward to estimate when storage capacity will be reached.

The cleanup job log is verified — confirming that soft-deleted files older than 30 days were physically removed during the weekly cleanup execution.

If storage growth is accelerating beyond projections, the file size limits are reviewed. An unexpectedly large number of very large files may indicate that Tenants are uploading raw, uncompressed photos — which can be 8-15 MB each — instead of compressed ones.

---

### Weekly Task 5 — Scope and Feature Backlog Review
Every week, the `backlog.md` file is reviewed as a team. No new items are moved into the current build scope without a formal trade-off decision. Deferred items are re-evaluated — are any of them becoming urgent based on user feedback? Are any of them no longer relevant? The backlog is a living document, not a graveyard.

---

## SCHEDULE 3 — MONTHLY MAINTENANCE

### Monthly Task 1 — Full Security Audit
Every month, a structured security audit walks through every API endpoint in the system against the IDOR checklist, the input validation checklist, and the authentication checklist. This is not a code review — it is a security-specific review with documented findings.

The audit follows this sequence:
Every endpoint is tested with an unauthenticated request — the correct response is 401. Every endpoint is tested with a valid token for the wrong user role — the correct response is 403. Every endpoint that accepts a resource ID is tested with an ID belonging to a different user — the correct response is 403 and an audit log entry. Every form submission endpoint is tested without a CSRF token — the correct response is 403.

Any endpoint that fails any of these tests is a security vulnerability. It is fixed before any other development work continues.

---

### Monthly Task 2 — Database Integrity Verification
Every month, a set of database integrity queries is run to verify that the data relationships are correct and that no orphaned records exist.

Specific checks:
Every lease record has a valid property_id that exists in the properties table. Every invoice has a valid lease_id and tenant_id. Every maintenance ticket has a valid lease_id and property_id. Every message has a valid conversation_id and sender_id. Every transaction has a corresponding invoice that is now marked Paid.

If any orphaned records are found — records with foreign keys pointing to non-existent parents — they are investigated. Orphaned records indicate either a bug in the delete logic or a race condition in the creation logic. The root cause is identified and fixed before the data inconsistency spreads.

---

### Monthly Task 3 — Performance Baseline Comparison
Every month, a standard set of performance benchmarks is run against the staging environment with the current production data volume replicated. The results are compared to the previous month's benchmarks and to the baseline established in Phase 9 testing.

Benchmarks tested:
Landlord Dashboard load time. Tenant Dashboard load time. Payment submission to confirmation time. Analytics page load time. Chat message delivery latency at 50 concurrent connections. WebSocket connection establishment time.

If any benchmark has degraded by more than 20% from the previous month, it is investigated. Performance degradation that compounds monthly becomes a critical user experience problem within 6 months.

---

### Monthly Task 4 — Backup Verification
Every month, the backup system is tested by performing a full restoration to a clean test environment. The restoration is not considered successful until the test environment is running the application correctly — not just until the backup files exist.

Backups that have never been tested are not real backups. They are hopes. The monthly restoration test converts hope into verified capability.

What is backed up:
The complete database is backed up daily with a 30-day retention. The encrypted file storage is backed up weekly with a 90-day retention. The application configuration and environment variable structure (not values) is backed up with every deployment.

---

### Monthly Task 5 — User Experience Review
Every month, the actual usage patterns from the past month are reviewed against the intended UX design.

Specific questions:
Which pages have the highest bounce rate — users leaving immediately? This indicates a page that is confusing or broken. Which API endpoints have the highest error rates? This indicates features that are failing users silently. Which features are never used — zero API calls in 30 days? This may indicate features that are not discoverable or not valuable. What is the average time from landing page visit to completed registration? A long time indicates friction in the onboarding flow.

These insights drive perfective maintenance — improvements that are not about fixing bugs but about making the system genuinely better to use.

---

## SCHEDULE 4 — QUARTERLY MAINTENANCE

### Quarterly Task 1 — Dependency Major Version Updates
Every quarter, all dependencies are evaluated for major version updates. Major version updates are not applied automatically — they are evaluated. A major version update to Flask, to PyJWT, or to the payment gateway SDK may include breaking changes that require code modifications.

The update process:
The update is applied in a dedicated feature branch. The test suite is run. Any failures are investigated — are they caused by breaking changes in the updated library? If yes, the code is updated to use the new API. The updated branch is deployed to staging and tested against the full feature set before being merged to production.

---

### Quarterly Task 2 — Architecture Review
Every quarter, the architecture is reviewed against the current state of the system and the upcoming requirements. Specifically:

Are any layers beginning to violate their Single Responsibility? Has business logic started leaking into API route handlers? Has data retrieval logic started appearing in business logic files? These violations start small and compound over time. The quarterly review catches them while they are still easy to correct.

Is the database schema still normalized? Have new columns been added that should be separate tables? Has data started being duplicated across tables? These normalization violations also start small and compound into corruption and inconsistency.

---

### Quarterly Task 3 — Load Testing
Every quarter, a full load test is run using the Locust load testing scripts. The test simulates the current expected peak concurrent user count plus 50% headroom. The results are compared to the previous quarter's results.

If the system handles 50 concurrent users comfortably in Q1 but only 40 in Q2 — without the user count actually increasing — something in the system has regressed in performance. This regression is identified and fixed before it affects real users.

---

### Quarterly Task 4 — Security Penetration Review
Every quarter, a structured penetration review is conducted against the OWASP Top 10. Each of the ten categories is tested systematically with documented findings and remediation status.

This is distinct from the monthly security audit. The monthly audit verifies that existing protections are working correctly. The quarterly penetration review attempts to find new vulnerabilities that the existing protections may not cover.

---

## SCHEDULE 5 — ANNUAL MAINTENANCE

### Annual Task 1 — Full System Architecture Review
Once a year, the entire system is reviewed from the ground up. Every architectural decision made during the original build is re-evaluated against what was actually built, how it actually performed, and what the users actually need.

Questions asked:
Is the 9-layer architecture still being respected in practice? Has technical debt accumulated in specific layers? Is the database schema still the right schema for the features being delivered? Are there features that should be redesigned rather than maintained in their current form?

---

### Annual Task 2 — Disaster Recovery Drill
Once a year, a full disaster recovery scenario is simulated. The production database is considered lost. The file storage is considered unavailable. The server is considered destroyed. The team has 4 hours to restore the system to full operation using only the backup infrastructure and the documented recovery procedures.

The drill measures: How long does full restoration actually take? Does the documentation match reality? Are there gaps in the backup coverage that the drill reveals? Every gap found in the drill is a gap that would have been catastrophic in a real disaster.

---

# 🖥️ PART 2 — FRONTEND MAINTENANCE
### *Keeping the 38-page interface correct, fast, and accessible*

---

## Frontend Maintenance Area 1 — HTML Structure Integrity

### What degrades over time:
HTML files accumulate small inconsistencies as features are added. A button added without the correct ARIA label. A form field added without an associated label element. A new section added without the correct semantic element. Individually small. Collectively, they degrade accessibility and semantic correctness.

### Maintenance action:
Every new HTML element added to any of the 38 pages is reviewed against the structural rules in `AI_rules.md` before being merged. Quarterly, an automated HTML validation pass is run against all 38 page templates. Any validation error is treated as a bug — not a style preference.

### Specific checks:
Every `<input>` has an associated `<label>`. Every interactive element has an `aria-label` or visible label text. Every image has meaningful `alt` text. Every form has a `novalidate` attribute with corresponding JavaScript validation. Page structure follows the correct landmark hierarchy — one `<main>`, correct heading levels, navigation in `<nav>`, footer in `<footer>`.

---

## Frontend Maintenance Area 2 — CSS Design System Consistency

### What degrades over time:
As features are added, developers introduce spacing values that are not on the 4px scale. Colors are introduced that are not in the defined palette. Border radius values are used inconsistently. The design system defined in `design.md` begins to diverge from what is actually rendered.

### Maintenance action:
A CSS custom properties audit is run quarterly. Every color value, every spacing value, and every border radius value used across all CSS files is compared against the design system tokens. Any value that does not match a defined token is replaced with the correct token or escalated as a design decision.

Specific forbidden patterns:
Hardcoded color values like `#0F172A` written directly in CSS rules instead of `var(--deep-blue)`. Arbitrary spacing values like `margin: 17px` instead of `margin: 16px` (the nearest 4px multiple). Inline styles on HTML elements except where absolutely unavoidable and explicitly documented.

---

## Frontend Maintenance Area 3 — JavaScript Quality and Security

### What degrades over time:
JavaScript files grow as features are added. Functions that were originally focused begin taking on additional responsibilities. Event listeners accumulate without corresponding removal when components are destroyed. Memory leaks develop. Console errors appear that no one investigates because the feature "seems to work."

### Maintenance action:
Monthly review of the browser console output across all 38 pages for any errors or warnings. Every console error is a bug. Zero tolerance.

Quarterly review of JavaScript function sizes and responsibilities. Any function that has grown beyond its original single responsibility is refactored. The Single Responsibility Principle applies to JavaScript functions exactly as it does to Python functions.

Security-specific JavaScript review:
Every `innerHTML` usage is audited — is the content being set from user-provided data? If yes, it must be replaced with `textContent` or properly escaped HTML. Every `eval()` call is an automatic security failure. Every `localStorage` access is reviewed — is sensitive data being stored? JWT tokens in localStorage are a critical vulnerability that must be removed immediately if discovered.

---

## Frontend Maintenance Area 4 — Animation and Performance

### What degrades over time:
Animations added to new features may conflict with or degrade existing animations. Performance-intensive animations — large canvas animations, continuous transforms, unoptimized keyframes — accumulate and reduce the frame rate on lower-powered mobile devices.

### Maintenance action:
Quarterly, the Tenant portal is tested on a mid-range Android device — specifically a device from 2021 or 2022 with modest GPU capability. Every animation is checked to run at 60 frames per second. Any animation that drops below 30 FPS is either optimized or removed.

The `will-change` CSS property is used on elements that animate frequently — transforming elements, fading elements — to give the browser a performance hint. But `will-change` applied to too many elements consumes memory. Quarterly, `will-change` usage is audited and limited to elements that genuinely need it.

---

## Frontend Maintenance Area 5 — Cross-Browser and Cross-Device Compatibility

### What degrades over time:
Browser engines update. CSS features that were progressive enhancements become standard — and sometimes the syntax changes. JavaScript APIs that were experimental become deprecated. A feature that worked perfectly in Chrome 120 may have a rendering quirk in Chrome 130.

### Maintenance action:
After every browser major version release — Chrome, Safari, Firefox — the 38 pages are tested in that browser version for visual and functional regressions. The most critical pages tested first: Login, Tenant Dashboard, Rent Payment, Landlord Kanban.

Mobile Safari on iOS receives special attention. iOS Safari has historically lagged behind Chrome in CSS support and has unique behaviors with fixed positioning, keyboard display, and touch events. Every Tenant portal page is tested on iOS Safari after every iOS major version release.

---

# ⚙️ PART 3 — BACKEND MAINTENANCE
### *Keeping the Python server correct, secure, and efficient*

---

## Backend Maintenance Area 1 — API Endpoint Health

### What degrades over time:
API endpoints that were correct when written may become incorrect as the database schema evolves, as business rules change, or as new features create unexpected interactions with existing endpoints.

### Maintenance action:
A comprehensive API test suite is maintained — one test per endpoint, per scenario. Tests cover the happy path (correct request, expected response), the authentication failure path (no token — expect 401), the authorization failure path (wrong user's resource — expect 403), and the validation failure path (missing required field — expect 422).

After every code change that touches an API endpoint, the full test suite for that endpoint and all related endpoints runs automatically. A failing test blocks the change from being merged.

---

## Backend Maintenance Area 2 — Middleware Stack Integrity

### What degrades over time:
Middleware is the most critical layer in the system's security architecture. As new routes are added, they may accidentally be exempted from middleware. A new route added to handle a specific feature may inadvertently bypass the authentication check because it was added to the wrong route group.

### Maintenance action:
After every new API endpoint is added, it is explicitly tested for middleware coverage. The test submits a request to the new endpoint without a JWT token. The expected response is 401. If the response is anything else, the endpoint is not protected by authentication middleware and this is a critical security bug.

The middleware execution order — Security Headers → CORS → Request Logging → Rate Limiting → Authentication → Authorization — is documented in `architecture.md` and verified in the application startup sequence after every deployment. If the order has changed, the deployment is rolled back.

---

## Backend Maintenance Area 3 — Business Logic Correctness

### What degrades over time:
Business logic is the most complex Python code in the system. As features evolve and edge cases are discovered, business logic functions are modified. These modifications can introduce subtle bugs — particularly in financial calculations, date arithmetic, and multi-step orchestrations.

### Maintenance action:
Every business logic function that performs a financial calculation — the 5% late fee formula, the invoice total calculation, the ROI calculation — has a dedicated set of unit tests with specific numerical inputs and expected outputs. These tests are never modified to match wrong outputs. If a test fails, the business logic is wrong and must be fixed.

The late fee calculation specifically is tested monthly with edge cases. What happens when the monthly rent is $0? What happens when the invoice already has a late fee applied? What happens when the Landlord has disabled late fees but the cron job still runs? These edge cases represent real scenarios that will occur in production.

---

## Backend Maintenance Area 4 — Cron Job Maintenance

### What degrades over time:
Cron jobs run on a schedule. The data they process grows. A cron job that runs in 30 seconds on 100 invoices may run in 8 minutes on 10,000 invoices. If the cron job window overlaps with the next scheduled execution, two instances run simultaneously, triggering the distributed lock system, and one instance does nothing for that night.

### Maintenance action:
Quarterly, cron job execution times are reviewed against data volume growth. If any cron job is taking more than 50% of its scheduled window, the job logic is optimized — better queries, batch processing instead of row-by-row processing, pre-filtering to reduce the working set.

Every cron job is reviewed against the idempotency principle quarterly. Can this job run twice and produce the same result as running once? If any path through the job logic can cause a duplicate action on the second run, that path is fixed.

---

## Backend Maintenance Area 5 — WebSocket Server Maintenance

### What degrades over time:
WebSocket connections are stateful. Unlike HTTP, a connection that is not properly cleaned up remains in the server's connection registry, consuming memory. Over time, ghost connections — connections that dropped without a clean disconnect — accumulate. The server's memory grows. Performance degrades.

### Maintenance action:
The heartbeat system that detects dead connections is verified monthly. The test is simple — a client connection is established, the network is simulated as dropped, and the server's connection registry is checked to confirm the ghost connection is removed within the heartbeat timeout period (25 seconds + 10 seconds = 35 seconds maximum).

The total memory consumed by the WebSocket server process is monitored weekly. Linear memory growth without a corresponding linear growth in active users indicates a memory leak. The source is identified — typically accumulating message buffers or unreleased event listeners — and fixed.

---

# 🗄️ PART 4 — DATABASE MAINTENANCE
### *Keeping the permanent memory of the system trustworthy and fast*

---

## Database Maintenance Area 1 — Query Performance

### What degrades over time:
Database tables grow. Indexes that perform well with 10,000 rows begin to degrade with 1,000,000 rows — not because the index is wrong but because the statistics the database uses to plan queries become stale.

### Maintenance action:
Database statistics are updated monthly using `ANALYZE` (PostgreSQL). This refreshes the query planner's understanding of data distribution and allows it to choose optimal execution plans based on current data volumes.

The slow query log threshold is set at 200 milliseconds. Any query appearing in this log is analyzed using `EXPLAIN ANALYZE` to understand its execution plan. Queries performing sequential scans on large tables are candidates for additional indexing or query restructuring.

---

## Database Maintenance Area 2 — Index Maintenance

### What degrades over time:
Database indexes become fragmented over time as rows are inserted, updated, and deleted. A fragmented index is less efficient than a fresh index. High-write tables — messages, notifications, audit_log, transactions — are particularly prone to index fragmentation.

### Maintenance action:
Monthly, index fragmentation is checked using PostgreSQL's built-in index statistics. Any index with fragmentation above 30% is rebuilt using `REINDEX CONCURRENTLY` — the CONCURRENTLY option allows the rebuild to proceed without locking the table, meaning the application continues operating normally during the maintenance operation.

Unused indexes — indexes that have not been used in any query over the past 30 days — are reviewed quarterly. An unused index still consumes storage and slows write operations. Indexes that are genuinely never used are removed.

---

## Database Maintenance Area 3 — Data Archiving

### What degrades over time:
Append-only tables — audit_log, transactions, notifications, messages — grow indefinitely. After 2 years, the notifications table may contain millions of rows that are never queried. Every query against this table — even with good indexes — is slower than it needs to be because the planner considers the full table size.

### Maintenance action:
Quarterly, data archiving is performed on high-volume tables. Records older than 12 months in the notifications table are moved to a dedicated archive table and removed from the active table. The archive table has the same schema but is never queried by the application — it exists only for legal record-keeping.

The messages table follows the same pattern — messages older than 12 months are archived. Active chat history remains fast. Historical records are preserved.

The audit_log and transactions tables are never archived — they are the legal and financial record. They are indexed to maintain query performance as they grow.

---

## Database Maintenance Area 4 — ACID Transaction Verification

### What degrades over time:
As new features are added, new multi-step database operations are introduced. If these operations are not wrapped in transactions, partial write failures can leave the database in an inconsistent state.

### Maintenance action:
Quarterly, every multi-step write operation in the codebase is reviewed. Any operation that writes to more than one table must be wrapped in a transaction. Any operation that writes to one table and then calls an external service (email, payment gateway) must have a clear strategy for what happens if the external call fails after the database write — is the write rolled back? Is the external call retried?

---

## Database Maintenance Area 5 — Backup Integrity

### What degrades over time:
The backup system continues running, creating backup files. But backup files can become corrupted. The backup process itself can fail silently — creating a backup file with incomplete data. The assumption that backups are working is not the same as verifying that they work.

### Maintenance action:
Monthly, one full database backup is restored to a completely clean test environment and the application is started against it. If the application starts correctly, connects to the restored database, and can serve the login page — the backup is verified. If anything fails, the backup system is broken and this is treated as a critical maintenance issue.

---

# 🔐 PART 5 — SECURITY MAINTENANCE
### *Keeping the system's defenses current and effective*

---

## Security Maintenance Area 1 — JWT Secret Rotation

### What it is:
The JWT secret key is used to sign every authentication token in the system. If this key is compromised — through a code repository leak, a server breach, or an environment variable exposure — every token in the system can be forged.

### Maintenance action:
The JWT secret key is rotated every 90 days as a preventive measure — not only when a breach is suspected. Rotating the key invalidates all existing tokens. All currently logged-in users are logged out and must re-authenticate. This is a small inconvenience compared to the alternative of not rotating and having a compromised key sign valid tokens indefinitely.

The rotation process is documented and rehearsed. The new key is generated, stored in the environment configuration, and deployed. The deployment triggers a graceful restart of the application server. Active WebSocket connections are gracefully disconnected with a "Session renewed, please log in again" message.

---

## Security Maintenance Area 2 — Rate Limit Tuning

### What degrades over time:
Rate limits set during development were calibrated against expected usage patterns. Actual usage patterns differ. A rate limit that was appropriate at launch may be too strict — blocking legitimate users during legitimate peak activity — or too lenient — failing to stop increasingly sophisticated attack patterns.

### Maintenance action:
Monthly, the rate limiting logs are reviewed. The frequency and pattern of 429 responses are analyzed. If legitimate users are consistently hitting rate limits during normal usage — for example, the chat rate limit of 60 messages per minute is being hit by users having normal conversations — the limit is increased. If the login endpoint's rate limit is being hit almost exclusively by the same small set of IPs with failed authentication attempts, the limit may need to be tightened or the IP ban duration extended.

---

## Security Maintenance Area 3 — OWASP Top 10 Reassessment

### What degrades over time:
The OWASP Top 10 list is updated periodically to reflect the current threat landscape. A vulnerability category that was not in the top 10 when the system was built may enter the top 10 as attackers shift focus. A mitigation that was state-of-the-art in 2024 may have known bypass techniques in 2026.

### Maintenance action:
Annually, the OWASP Top 10 current list is compared against the system's security posture. Any new category in the current top 10 that was not in the version the system was designed against is assessed and mitigated.

---

## Security Maintenance Area 4 — Dependency Security Patches

### What degrades over time:
Every library in the system — Flask, PyJWT, bcrypt, the payment gateway SDK — has vulnerabilities discovered after the system ships. These vulnerabilities are published in the National Vulnerability Database with severity scores. A critical vulnerability in PyJWT, for example, could allow an attacker to forge JWT tokens, bypassing authentication entirely.

### Maintenance action:
A weekly automated scan using `pip audit` and `safety check` runs against the current `requirements.txt`. Any dependency with a known vulnerability of HIGH or CRITICAL severity triggers an immediate patch. The patch is applied, tested in staging, and deployed to production within 24 hours for CRITICAL vulnerabilities and within 7 days for HIGH vulnerabilities.

MEDIUM and LOW vulnerabilities are scheduled for resolution in the next regular maintenance window.

---

## Security Maintenance Area 5 — Audit Log Review for Anomalies

### What degrades over time:
The audit log grows continuously. As it grows, finding meaningful security signals in it becomes harder. A manual daily review that worked when the system had 50 users becomes impractical with 5,000 users.

### Maintenance action:
Automated anomaly detection queries run nightly against the audit log. These queries flag:
Any user account that has more than 20 403 responses in a single day. Any IP address that has successfully authenticated as more than 3 different user accounts in one day. Any download event for more than 50 documents by a single user in one hour. Any payment webhook received from an IP not on the gateway's documented IP range.

Each flagged event generates a notification in the cron_log for review the following morning.

---

# 📊 PART 6 — MONITORING AND OBSERVABILITY MAINTENANCE
### *Knowing what the system is doing at all times*

---

## Monitoring Maintenance Area 1 — Application Uptime Monitoring

### What is monitored:
An external uptime monitoring service — independent of the application server — sends an HTTP request to the system's health check endpoint every 60 seconds. If the endpoint does not respond within 5 seconds, or responds with a non-200 status, an alert is triggered immediately.

The health check endpoint verifies three things: the application server is running, the database connection is healthy, and the WebSocket server is responsive. A health check that passes all three confirms the entire stack is operational.

### Maintenance action:
The uptime monitoring configuration is verified monthly. Alert routing — where the alert goes when the system is down — is tested by temporarily taking the staging environment offline and confirming the alert arrives at the correct destination.

---

## Monitoring Maintenance Area 2 — Response Time Monitoring

### What is monitored:
The response time of every API endpoint is measured on every request and recorded. A statistical summary — average, 95th percentile, 99th percentile — is reviewed weekly.

The 95th percentile response time is the most meaningful metric. It tells you what 95% of your users experience. If the 95th percentile for the Landlord Dashboard endpoint is 2.1 seconds, 5% of Landlord Dashboard loads take longer than 2.1 seconds. If this metric increases week over week, something is degrading — more data, a slower query, server resource pressure.

### Maintenance action:
Response time alerts are configured. If the 95th percentile response time for any endpoint exceeds twice its established baseline — a dashboard that normally loads in 800ms taking over 1,600ms — an alert is triggered for investigation.

---

## Monitoring Maintenance Area 3 — Error Rate Monitoring

### What is monitored:
The percentage of all API requests that result in a 5xx (server error) response is monitored continuously. A healthy system maintains a 5xx rate below 0.1%. A spike above 1% indicates a systemic problem — a database failure, an unhandled exception in business logic, a configuration error after a deployment.

### Maintenance action:
An error rate alert fires if the 5xx rate exceeds 0.5% over any 5-minute window. When this alert fires, the error log is immediately consulted to identify the source. If the source is a deployment — a recently deployed code change — the deployment is rolled back immediately while the bug is investigated.

---

# 📝 PART 7 — DOCUMENTATION MAINTENANCE
### *Keeping the knowledge as current as the system*

---

## Documentation Maintenance Area 1 — .md File Currency

### What degrades over time:
The 13 `.md` files created in Phase 0 document the system as designed. The system as built evolves. A database column added in Week 7 that is not reflected in `database_schema.sql`. A new API endpoint added in Week 11 that is not documented in `architecture.md`. A new business rule enforced in Week 9 that is not in `prd.md`.

After 6 months, the documentation describes a system that no longer exists. A new developer joins and reads the documentation — and builds against a ghost.

### Maintenance action:
Documentation is updated in the same pull request that changes the code. A code change that adds a new database table without updating `database_schema.sql` is not a complete change. The pull request is not merged until the documentation matches the implementation.

Quarterly, a documentation audit compares the actual codebase against the documented architecture, schema, and API contracts. Any divergence is corrected.

---

## Documentation Maintenance Area 2 — API Documentation Currency

### What degrades over time:
API endpoints evolve. A field is added to a response. A validation rule is tightened. A new optional parameter is added. If the API documentation does not reflect these changes, frontend developers — and the future AI tools using these documents — work against wrong contracts.

### Maintenance action:
Every API endpoint change includes a corresponding update to the API contract documentation. The request shape, the response shape, the error responses, and the rate limit are all documented and kept current.

---

# 🚀 PART 8 — DEPLOYMENT MAINTENANCE
### *Keeping the process of releasing changes safe and reliable*

---

## Deployment Maintenance Area 1 — The Deployment Checklist

Every deployment — regardless of size — runs through a standard checklist before the deployment begins and another checklist after it completes.

### Pre-deployment checklist:
All automated tests pass on the staging environment. The database migration scripts for this deployment have been tested on a copy of the production database. The environment variables for any new configuration values have been added to the production server. The deployment window has been communicated to users if it involves downtime. A rollback plan is documented and reviewed.

### Post-deployment checklist:
The health check endpoint returns 200. The login flow works end-to-end. The payment flow works in sandbox mode. The cron jobs are scheduled and will run at their next scheduled time. The WebSocket server is accepting connections. The error rate is at baseline levels within 5 minutes of deployment.

If any post-deployment check fails, the rollback plan is executed immediately.

---

## Deployment Maintenance Area 2 — Database Migration Safety

### What can go wrong:
A database migration that adds a NOT NULL column to a table with existing rows fails if no default value is provided. A migration that renames a column causes every query using the old column name to fail immediately. A migration that drops a table or column is irreversible.

### Maintenance action:
Every database migration follows a two-phase approach for destructive changes. Phase 1: Add the new column or table, make it optional (nullable), deploy the application code that uses it. Phase 2: After the application is using the new column, make it NOT NULL if required. Never rename a column in one step — add the new column, migrate data to it, update the application code, then drop the old column in a separate subsequent deployment.

No migration that drops a column, drops a table, or renames a table is deployed without a verified backup taken within the last 2 hours.

---

# 📊 THE COMPLETE MAINTENANCE CALENDAR

| Task | Frequency | Owner | Critical? |
|---|---|---|---|
| Cron job execution verification | Daily | Engineer on rotation | YES |
| Error log review | Daily | Engineer on rotation | YES |
| Audit log security review | Daily | Engineer on rotation | YES |
| Payment reconciliation review | Daily | Engineer on rotation | YES |
| Database performance review | Weekly | Database engineer | YES |
| Dependency vulnerability scan | Weekly | Security engineer | YES |
| WebSocket connection health | Weekly | Backend engineer | YES |
| Storage usage review | Weekly | Infrastructure engineer | NO |
| Scope and backlog review | Weekly | Full team | NO |
| Full security audit | Monthly | Security engineer | YES |
| Database integrity verification | Monthly | Database engineer | YES |
| Performance benchmark comparison | Monthly | Backend engineer | YES |
| Backup verification (restore test) | Monthly | Infrastructure engineer | YES |
| User experience review | Monthly | Full team | NO |
| JWT secret rotation | Quarterly | Security engineer | YES |
| Rate limit tuning | Monthly | Security engineer | NO |
| Index maintenance and rebuild | Monthly | Database engineer | YES |
| Data archiving | Quarterly | Database engineer | NO |
| Dependency major updates | Quarterly | Backend engineer | YES |
| Architecture review | Quarterly | Full team | YES |
| Load testing | Quarterly | Backend engineer | YES |
| Security penetration review | Quarterly | Security engineer | YES |
| Full system architecture review | Annually | Full team | YES |
| Disaster recovery drill | Annually | Full team | YES |
| OWASP Top 10 reassessment | Annually | Security engineer | YES |
| Documentation comprehensive audit | Quarterly | Full team | YES |

---

## 🎯 THE MAINTENANCE PHILOSOPHY FOR THIS PROJECT

> **Maintenance is not what you do when something breaks.**
> **Maintenance is what you do so that things break less, break smaller, and break recoverable.**

Every daily check, every weekly scan, every monthly audit, every quarterly review, every annual drill exists for one reason — to keep the Landlord's financial data correct, keep the Tenant's payment history trustworthy, keep the chat messages private, keep the documents secure, and keep the entire 9-layer system performing at the standard it was designed to deliver.

A system without maintenance is a system with a countdown timer. The maintenance schedule is what resets that timer — permanently.

> **The best software engineers do not just build systems.**
> **They maintain them.**
> **Because they know that building is the easy part.**
> **Keeping it correct, secure, and trusted — forever — that is the craft.**
# 🔄 Complete Technology Stack Update
## From Flask + PostgreSQL → Django + MySQL
### Every Layer Updated | Every File Corrected | Every Decision Explained
#### Based on All Conversations in This Chat

---

## 🧠 WHY THIS CHANGE MATTERS DEEPLY

This is not a simple "swap one tool for another" update. Changing from Flask to Django and from PostgreSQL to MySQL changes **how the system thinks, how it is structured, how it communicates with the database, how middleware works, how security is implemented, and how every layer of the 9-layer architecture is built.**

Every `.md` file, every architectural decision, every database query pattern, every security mechanism must be understood through the lens of Django and MySQL specifically — not generically.

---

# 🔧 PART 1 — WHAT ACTUALLY CHANGES AND WHY

---

## CHANGE 1 — Flask → Django

### What Flask was:
Flask is a **micro-framework**. It gives you an HTTP router and almost nothing else. Every additional feature — authentication, middleware, ORM, CSRF protection, form handling, email sending — had to be chosen, installed, and configured separately. Maximum flexibility. Maximum responsibility.

### What Django is:
Django is a **batteries-included full-stack framework**. It arrives with a built-in ORM, built-in authentication system, built-in CSRF protection, built-in middleware system, built-in admin interface, built-in form validation, built-in email handling, built-in session management, and built-in security features. The philosophy is "convention over configuration" — Django has a defined, correct way to do most things, and following that way gives you enormous capability very quickly.

### What this means for the project:

**The ORM replaces raw SQL for most operations:**
In Flask with raw SQL, every database query was written by hand as a SQL string. In Django, the ORM translates Python code into SQL automatically. Instead of writing `SELECT * FROM properties WHERE landlord_id = ?`, you write `Property.objects.filter(landlord_id=user.id)`. Django generates the correct, parameterized SQL. SQL injection prevention is built into the ORM by default.

**Django's middleware system replaces custom middleware:**
In Flask, every middleware function was written from scratch. In Django, the middleware system is built in. Django provides `AuthenticationMiddleware`, `SessionMiddleware`, `SecurityMiddleware`, `CsrfViewMiddleware`, and `CommonMiddleware` out of the box. Custom middleware — rate limiting, IDOR prevention, request logging — is written as Django middleware classes that slot into the existing pipeline.

**Django's authentication replaces JWT from scratch:**
Django has a complete authentication system built in — user models, password hashing with PBKDF2 by default (bcrypt as an alternative), login, logout, and session management. For the API-based authentication needed for this project, `djangorestframework-simplejwt` provides JWT authentication that integrates cleanly with Django's existing auth system.

**Django REST Framework replaces manual API route building:**
The API layer is built using Django REST Framework (DRF). DRF provides serializers for data validation and transformation, viewsets for CRUD operations, routers for URL generation, and permission classes for authorization. The entire API layer is more structured, more consistent, and less error-prone than Flask route handlers.

---

## CHANGE 2 — PostgreSQL → MySQL

### What PostgreSQL was:
PostgreSQL is an advanced object-relational database with rich JSON support, sophisticated full-text search, window functions, and the most complete ACID implementation available in open-source databases.

### What MySQL is:
MySQL is the world's most widely deployed open-source relational database. It is fast, well-documented, widely hosted, and deeply familiar to most web developers. It fully supports ACID transactions when using the InnoDB storage engine — which is the default. It is the standard database for LAMP stack applications, which aligns perfectly with this project's deployment context.

### What this means for the project:

**InnoDB engine is mandatory:**
MySQL has multiple storage engines. Only InnoDB supports ACID transactions, foreign key constraints, and row-level locking. Every table in the system must use the InnoDB engine. This must be explicitly specified or configured as the default — `default-storage-engine = InnoDB` in MySQL configuration.

**Django's ORM handles MySQL differences transparently:**
Most of the differences between PostgreSQL and MySQL syntax are handled by Django's ORM automatically. The same Python model code generates different SQL for PostgreSQL and MySQL as needed. The developer writes Python — Django writes the correct SQL for whichever database is configured.

**MySQL-specific considerations:**
MySQL's default character set must be set to `utf8mb4` — not the older `utf8` which only supports 3-byte characters. `utf8mb4` supports the full Unicode range including emoji. This matters when Tenants send maintenance descriptions, chat messages, or inspection notes using characters outside basic ASCII.

MySQL's `DATETIME` type does not store timezone information. All timestamps must be managed at the application level as UTC. Django handles this correctly when `USE_TZ = True` is set in settings — Django stores and retrieves all datetimes in UTC and converts to the user's timezone at display time.

---

# 🏗️ PART 2 — THE UPDATED 9-LAYER ARCHITECTURE WITH DJANGO + MYSQL

---

## LAYER 1 — STRUCTURE (HTML)
**No change.** HTML is HTML. Django's template engine renders HTML. The 38 pages retain their exact structure.

The one addition: Django templates use `{% %}` template tags and `{{ }}` variable interpolation. The base templates extend Django's template inheritance system. `layout_landlord.html` becomes the base template that landlord pages extend using `{% extends "landlord/base.html" %}` and `{% block content %}`.

---

## LAYER 2 — STYLING (CSS)
**No change.** CSS is CSS. Django serves static files. The design system from `design.md` applies without modification.

The one addition: Django's `{% static %}` template tag generates correct URLs for static files. `<link rel="stylesheet" href="{% static 'css/design_system.css' %}">` replaces hardcoded paths. Django's `collectstatic` command gathers all static files for production serving.

---

## LAYER 3 — BEHAVIOR (JavaScript)
**No change in principle.** JavaScript behavior remains the same — fetch calls, WebSocket connections, DOM manipulation, form handling.

The one critical Django-specific addition: Django's CSRF protection requires the CSRF token to be included in every AJAX POST, PUT, PATCH, and DELETE request. Django provides the CSRF token in a cookie named `csrftoken`. JavaScript must read this cookie and include the value in every state-changing request header as `X-CSRFToken`. This is a non-negotiable Django security requirement.

---

## LAYER 4 — MIDDLEWARE (Django Middleware System)

### How Django Middleware Works:
Django middleware is defined as an ordered list in `settings.py` under `MIDDLEWARE`. Every request passes through this list top-to-bottom. Every response passes back through bottom-to-top. The order is the logic — exactly as established in every previous conversation.

### The Django Middleware Stack for This Project:

```
MIDDLEWARE = [
    # 1. Security Headers (built-in Django)
    'django.middleware.security.SecurityMiddleware',

    # 2. Session Management (built-in Django)
    'django.contrib.sessions.middleware.SessionMiddleware',

    # 3. CORS (django-cors-headers package)
    'corsheaders.middleware.CorsMiddleware',

    # 4. Common Middleware (URL normalization, built-in)
    'django.middleware.common.CommonMiddleware',

    # 5. CSRF Protection (built-in Django)
    'django.middleware.csrf.CsrfViewMiddleware',

    # 6. Authentication (built-in Django)
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # 7. Request Logging (custom middleware)
    'middleware.logging_middleware.RequestLoggingMiddleware',

    # 8. Rate Limiting (custom middleware)
    'middleware.rate_limit_middleware.RateLimitMiddleware',

    # 9. IDOR Authorization (custom middleware)
    'middleware.authorization_middleware.IDORAuthorizationMiddleware',

    # 10. Messages (built-in Django)
    'django.contrib.messages.middleware.MessageMiddleware',

    # 11. X-Frame-Options (built-in Django)
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### What Django's Built-in Middleware Provides for Free:
**SecurityMiddleware** sets `Strict-Transport-Security`, `X-Content-Type-Options`, redirects HTTP to HTTPS, sets referrer policy — all automatically when `SECURE_*` settings are configured.

**CsrfViewMiddleware** automatically verifies CSRF tokens on every POST/PUT/PATCH/DELETE request — the system does not need to write this check in every view.

**AuthenticationMiddleware** attaches the authenticated user to every request as `request.user`. Every view receives the authenticated user automatically.

**XFrameOptionsMiddleware** sets `X-Frame-Options: DENY` on every response automatically.

---

## LAYER 5 — API (Django REST Framework)

### How DRF Structures the API Layer:

**Serializers replace manual input validation:**
A Django REST Framework serializer defines the exact shape of data that an endpoint accepts and returns. It validates types, required fields, length limits, and custom validation rules. Invalid data is rejected with a structured 422-equivalent response before it reaches business logic. The serializer is the API boundary validator.

**ViewSets replace individual route handlers:**
A DRF ViewSet groups all CRUD operations for a resource into one class. The `PropertyViewSet` handles list, create, retrieve, update, and destroy for properties. The URL router automatically generates all the correct URL patterns from the ViewSet. This enforces the consistent URL naming convention documented in `naming_patterns.md`.

**Permission Classes replace manual authorization checks:**
DRF permission classes define who can access what. `IsAuthenticated` requires a valid JWT. `IsLandlord` is a custom permission that checks `request.user.role == 'landlord'`. `IsOwner` is a custom permission that checks the resource belongs to the requesting user. These permission classes are the DRF implementation of the authorization layer, complementing the IDOR middleware.

**JWT Integration:**
`djangorestframework-simplejwt` provides the JWT login endpoint, token refresh endpoint, and token verification. It integrates with Django's existing user model. JWT authentication is configured as the default authentication class in DRF settings.

---

## LAYERS 6 & 7 — BUSINESS RULES AND BUSINESS LOGIC

**No structural change.** Business rules and business logic remain Python functions in their dedicated modules. The only difference is that they now interact with the database through Django's ORM rather than raw SQL queries. The ORM is faster to write, safer against injection, and more maintainable — but the single responsibility and separation principles remain identical to every previous conversation.

---

## LAYERS 8 & 9 — DATA RETRIEVAL AND DATA STORAGE (Django ORM + MySQL)

### How the Django ORM Works:

Django's ORM translates Python model queries into MySQL SQL automatically. The developer never writes raw SQL for standard operations. The ORM generates parameterized queries — SQL injection is prevented by the framework's core mechanism, not by developer discipline alone.

**Data Retrieval with Django ORM:**
`Property.objects.filter(landlord=request.user).select_related('building').prefetch_related('leases')` — this single line generates an optimized JOIN query that retrieves properties with their building and lease data in two queries total (not N+1). The `select_related` and `prefetch_related` methods are the Django ORM solution to the N+1 query problem discussed in every previous conversation.

**Data Storage with Django ORM:**
`invoice.status = 'Paid'` followed by `invoice.save()` generates an `UPDATE` statement with only the changed fields. `Invoice.objects.create(...)` generates a parameterized `INSERT`. Django's `transaction.atomic()` context manager wraps multiple ORM operations in a single MySQL transaction — implementing the ACID atomicity principle discussed throughout this project.

**Raw SQL When Needed:**
For complex analytics queries — the 12-month revenue aggregation, the maintenance category breakdown — Django allows raw SQL via `Invoice.objects.raw(...)` or `connection.cursor()`. These raw queries still use parameterized values — `%s` placeholders — maintaining SQL injection prevention even for hand-written queries.

---

# 📁 PART 3 — UPDATED PROJECT FILE STRUCTURE

```
rent-lease-management/
│
├── manage.py                           # Django management command entry point
├── requirements.txt                    # All Python dependencies
├── .env                                # Environment variables (never committed)
├── .env.example                        # Template for required variables
├── .gitignore                          # Excludes .env, __pycache__, media/, staticfiles/
│
├── docs/                               # All .md documentation files
│   ├── AI_rules.md
│   ├── plan.md
│   ├── prd.md
│   ├── architecture.md
│   ├── design.md
│   ├── system_design.md
│   ├── security.md
│   ├── risk_management.md
│   ├── implementation_plan.md
│   ├── file_structure.md
│   ├── naming_patterns.md
│   └── tech_stack.md
│
├── config/                             # Django project configuration
│   ├── __init__.py
│   ├── settings/
│   │   ├── base.py                     # Shared settings for all environments
│   │   ├── development.py              # Development-specific settings
│   │   └── production.py              # Production-specific settings
│   ├── urls.py                         # Root URL configuration
│   ├── wsgi.py                         # WSGI entry point
│   └── asgi.py                         # ASGI entry point (for WebSockets)
│
├── apps/                               # All Django applications
│   │
│   ├── users/                          # User management app
│   │   ├── models.py                   # CustomUser model
│   │   ├── serializers.py              # DRF serializers
│   │   ├── views.py                    # DRF viewsets
│   │   ├── urls.py                     # URL patterns
│   │   ├── permissions.py              # Custom DRF permission classes
│   │   ├── business_rules.py           # User constraint enforcement
│   │   ├── business_logic.py           # User process orchestration
│   │   └── migrations/                 # Django database migrations
│   │
│   ├── properties/                     # Property management app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── business_rules.py
│   │   ├── business_logic.py
│   │   └── migrations/
│   │
│   ├── leases/                         # Lease management app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── business_rules.py
│   │   ├── business_logic.py
│   │   └── migrations/
│   │
│   ├── financials/                     # Financial management app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── business_rules.py
│   │   ├── business_logic.py
│   │   └── migrations/
│   │
│   ├── maintenance/                    # Maintenance helpdesk app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── business_rules.py
│   │   ├── business_logic.py
│   │   └── migrations/
│   │
│   ├── chat/                           # Real-time chat app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── consumers.py                # Django Channels WebSocket consumers
│   │   ├── routing.py                  # WebSocket URL routing
│   │   ├── business_logic.py
│   │   └── migrations/
│   │
│   ├── documents/                      # Document vault app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── business_rules.py
│   │   ├── business_logic.py
│   │   └── migrations/
│   │
│   ├── analytics/                      # Analytics and reporting app
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── queries.py                  # Complex analytics SQL queries
│   │   └── business_logic.py
│   │
│   ├── notifications/                  # Notification system app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── migrations/
│   │
│   └── automation/                     # Cron jobs and scheduling app
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── tasks.py                    # Celery task definitions
│       └── migrations/
│
├── middleware/                         # Custom Django middleware
│   ├── __init__.py
│   ├── logging_middleware.py           # Request logging
│   ├── rate_limit_middleware.py        # Rate limiting
│   └── authorization_middleware.py     # IDOR prevention
│
├── frontend/                           # All HTML, CSS, JavaScript
│   ├── templates/
│   │   ├── base/
│   │   │   ├── layout_landlord.html
│   │   │   ├── layout_tenant.html
│   │   │   └── layout_auth.html
│   │   ├── landlord/
│   │   │   └── [14 landlord page templates]
│   │   ├── tenant/
│   │   │   └── [11 tenant page templates]
│   │   └── public/
│   │       └── [13 external page templates]
│   └── static/
│       ├── css/
│       └── js/
│
├── scheduler/                          # Background job scheduling
│   ├── __init__.py
│   ├── celery.py                       # Celery configuration
│   ├── late_fee_task.py
│   ├── lease_expiry_task.py
│   ├── rent_reminder_task.py
│   └── auto_pay_task.py
│
├── media/                              # User-uploaded files (outside web root in production)
│   ├── documents/
│   ├── maintenance_photos/
│   └── compliance_docs/
│
├── staticfiles/                        # Collected static files (production)
│
└── logs/
    ├── app.log
    ├── audit.log
    └── celery.log
```

---

# 📋 PART 4 — UPDATED tech_stack.md

```md
# 🔧 tech_stack.md
# Rent & Lease Management System — Technology Stack
# Updated: Django + MySQL | Every technology, every choice, every reason

---

## 1. FRONTEND

### HTML5
Role      : Structure layer — all 38 pages
Rendered by: Django template engine
Template tags: {% %} for logic, {{ }} for variables, {% static %} for assets
Inheritance: {% extends %} and {% block %} for base layout reuse
Rules     : No inline styles. No inline JavaScript. Semantic HTML5 only.

### CSS3 (Vanilla)
Role      : Styling layer — complete design system
Served by : Django static files system (development) / CDN (production)
Loaded via: {% load static %} and {% static 'css/file.css' %} template tags
Rules     : All values reference design tokens. 4px spacing base. No arbitrary values.

### JavaScript (Vanilla ES6+)
Role      : Behavior layer — interaction, API communication, WebSocket client
Critical Django addition:
  Every AJAX POST/PUT/PATCH/DELETE must include the CSRF token:
  Header: X-CSRFToken: [value from csrftoken cookie]
  Django's CsrfViewMiddleware rejects requests missing this header.
JWT storage: Memory only — never localStorage (XSS risk)
Rules     : No frameworks. Pure modern JavaScript.

### Chart.js (4.x)
Role      : Analytics charts
Scope     : Landlord Analytics page only

---

## 2. BACKEND

### Python 3.11+
Role      : All server-side logic

### Django 4.2+ (LTS)
Role      : Complete web framework — URL routing, ORM, middleware,
            authentication, CSRF, template engine, static files,
            form validation, email, sessions
Why Django: Batteries-included. Built-in security. Mature ORM. Large community.
            LTS version means security support until April 2026+.
            Correct choice for a full-featured production system.

Key Django configurations:
  DEBUG = False (production — never True in production)
  ALLOWED_HOSTS = [production domain]
  USE_TZ = True (all datetimes stored in UTC)
  DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
  AUTH_USER_MODEL = 'users.CustomUser' (custom user model)
  PASSWORD_HASHERS = bcrypt as first hasher

### Django REST Framework (DRF) 3.14+
Role      : API layer — serializers, viewsets, routers, permissions
Why DRF   : Industry standard for Django APIs. Integrates with Django auth.
            Provides consistent patterns for all 9 resource domains.

Key DRF configurations:
  DEFAULT_AUTHENTICATION_CLASSES: JWTAuthentication
  DEFAULT_PERMISSION_CLASSES: IsAuthenticated
  DEFAULT_PAGINATION_CLASS: PageNumberPagination
  PAGE_SIZE: 20

### djangorestframework-simplejwt
Role      : JWT authentication integrated with Django's auth system
Provides  : /api/token/ (login → returns access + refresh tokens)
            /api/token/refresh/ (refresh access token)
            /api/token/verify/ (verify token validity)
Token storage: access token in memory, refresh token in httpOnly cookie

### Django Channels 4.x
Role      : WebSocket support for real-time chat and notifications
Why       : Django by default is WSGI (HTTP only). Django Channels adds
            ASGI support enabling persistent WebSocket connections.
Requires  : Redis as the channel layer backend
ASGI server: Daphne or Uvicorn

### Channels Redis
Role      : Channel layer backend for Django Channels
Why       : Multiple WebSocket server instances need a shared message broker.
            Redis is the standard, battle-tested choice.

### Celery 5.x
Role      : Background task queue for all cron jobs
Why       : Django does not have a built-in task scheduler for production.
            Celery is the industry standard for Python background tasks.
Broker    : Redis (same Redis instance as Channels, different database)
Beat      : celery-beat for scheduled (cron-style) task execution
Tasks     : Late fee application, lease expiry scan, rent reminders, auto-pay

### django-cors-headers
Role      : CORS middleware for cross-origin requests
Why       : Required when frontend and backend are on different domains.
            Integrates cleanly as Django middleware.

### Pillow
Role      : Image processing for maintenance photos and compliance documents
Why       : Validates and optionally resizes uploaded images.

---

## 3. DATABASE

### MySQL 8.0+
Role      : Primary persistent data store
Engine    : InnoDB (mandatory — the only engine supporting ACID and foreign keys)
Encoding  : utf8mb4 with utf8mb4_unicode_ci collation
            (supports full Unicode including emoji — critical for chat messages)
Timezone  : All datetimes stored as UTC via Django's USE_TZ = True

Django connection:
  DATABASE = {
    'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': env('DB_NAME'),
      'USER': env('DB_USER'),
      'PASSWORD': env('DB_PASSWORD'),
      'HOST': env('DB_HOST'),
      'PORT': '3306',
      'OPTIONS': {
        'charset': 'utf8mb4',
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
      }
    }
  }

STRICT_TRANS_TABLES: Critical setting. Without it, MySQL silently truncates
data that exceeds column length limits. With it, MySQL raises an error.
Always use STRICT_TRANS_TABLES in production.

### mysqlclient
Role      : Python MySQL adapter (recommended by Django docs)
Alternative: PyMySQL (pure Python, no C dependencies — easier to install)

### Redis 7.x
Role      : Channel layer (WebSockets) + Task broker (Celery) + Cache
Why Redis : In-memory, extremely fast, standard for both use cases.

---

## 4. DJANGO MODELS → MYSQL TABLES

Django models define the database schema in Python.
Django migrations translate model changes into MySQL ALTER/CREATE TABLE statements.
Direct SQL schema files are replaced by Django migrations.

Model → MySQL mapping:
  CharField(max_length=255)    → VARCHAR(255)
  TextField()                  → LONGTEXT
  IntegerField()               → INT
  DecimalField(max_digits, dp) → DECIMAL(max_digits, decimal_places)
  BooleanField()               → TINYINT(1)
  DateField()                  → DATE
  DateTimeField()              → DATETIME(6) with UTC storage
  ForeignKey()                 → INT with FOREIGN KEY constraint (InnoDB)
  EmailField()                 → VARCHAR(254) with email validation

---

## 5. INFRASTRUCTURE

### Redis (as described above)
Two databases within Redis:
  DB 0: Django Channels channel layer
  DB 1: Celery task broker and result backend

### SMTP / Email
Django's email backend configured via settings:
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
  All values from environment variables

### Media Files (User Uploads)
Development: MEDIA_ROOT = '/media/' served by Django
Production : MEDIA_ROOT on cloud storage (S3-compatible)
             django-storages library abstracts the storage backend
             Business logic calls the same interface regardless of backend

### Static Files
Development: Django serves static files via runserver
Production : django collectstatic gathers all static files
             Served by Nginx or CDN

### HTTPS
Django settings for production:
  SECURE_SSL_REDIRECT = True
  SECURE_HSTS_SECONDS = 31536000
  SECURE_HSTS_INCLUDE_SUBDOMAINS = True
  SECURE_HSTS_PRELOAD = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SECURE = True

---

## 6. COMPLETE TECHNOLOGY STACK TABLE

| Technology              | Version  | Role                          | Layer    |
|-------------------------|----------|-------------------------------|----------|
| HTML5                   | 5        | Page structure                | 1        |
| CSS3                    | 3        | Visual design + animations    | 2        |
| JavaScript              | ES2022   | Interaction + API calls       | 3        |
| Chart.js                | 4.x      | Analytics charts              | 3        |
| Python                  | 3.11+    | Backend engine                | 4–7      |
| Django                  | 4.2 LTS  | Full web framework            | 4–7      |
| Django REST Framework   | 3.14+    | API layer                     | 5        |
| simplejwt               | 5.x      | JWT authentication            | 4        |
| Django Channels         | 4.x      | WebSocket (ASGI)              | 5        |
| Celery                  | 5.x      | Background tasks / cron       | 7        |
| celery-beat             | 2.x      | Scheduled task execution      | 7        |
| django-cors-headers     | 4.x      | CORS middleware               | 4        |
| mysqlclient             | 2.x      | MySQL Python adapter          | 8–9      |
| MySQL                   | 8.0+     | Primary database (InnoDB)     | 8–9      |
| Redis                   | 7.x      | Channels + Celery broker      | 5, 7     |
| django-storages         | 1.14+    | Abstracted file storage       | 9        |
| Pillow                  | 10.x     | Image processing              | 9        |
| python-decouple         | 3.x      | Environment variable loading  | Config   |
| Daphne / Uvicorn        | Latest   | ASGI server for production    | Infra    |
| Nginx                   | Latest   | Reverse proxy + static files  | Infra    |
```

---

# 📋 PART 5 — UPDATED architecture.md (Django-Specific Sections)

```md
# 🏗️ architecture.md — Django + MySQL Update
# Key architectural changes from the Django and MySQL technology choices

---

## DJANGO URL ROUTING

Root URL configuration in config/urls.py:
  /api/v1/auth/         → users.urls (authentication endpoints)
  /api/v1/properties/   → properties.urls (property management)
  /api/v1/leases/       → leases.urls (lease management)
  /api/v1/financials/   → financials.urls (billing and payments)
  /api/v1/maintenance/  → maintenance.urls (helpdesk)
  /api/v1/chat/         → chat.urls (REST chat history)
  /api/v1/documents/    → documents.urls (document vault)
  /api/v1/analytics/    → analytics.urls (reporting)
  /api/v1/notifications/→ notifications.urls (notification feed)
  /api/v1/automation/   → automation.urls (cron toggle panel)
  /ws/chat/             → chat.routing (WebSocket routing via Channels)
  /ws/notifications/    → notifications.routing (WebSocket push)
  /                     → frontend HTML views (template rendering)

---

## DJANGO CUSTOM USER MODEL

The system uses a custom user model extending AbstractBaseUser.
This is a Django requirement that must be set BEFORE any migrations are run.
AUTH_USER_MODEL = 'users.CustomUser'

CustomUser fields:
  email           : EmailField(unique=True) — login identifier
  role            : CharField(choices=['landlord','tenant'])
  first_name      : CharField
  last_name       : CharField
  phone_number    : CharField
  is_verified     : BooleanField(default=False)
  is_active       : BooleanField(default=True)
  created_at      : DateTimeField(auto_now_add=True)
  updated_at      : DateTimeField(auto_now=True)
  deleted_at      : DateTimeField(null=True, blank=True)

USERNAME_FIELD = 'email' (login with email not username)
REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

---

## DJANGO MIGRATIONS (Replaces database_schema.sql)

All database schema is managed through Django migrations.
Schema changes are never applied directly to MySQL.
The migration workflow:
  1. Modify the model in models.py
  2. Run: python manage.py makemigrations [app_name]
  3. Django generates a migration file describing the change
  4. Run: python manage.py migrate
  5. Django applies the migration to MySQL

Every migration file is committed to version control.
The current database state is always reproducible by running all migrations.
Rolling back a migration: python manage.py migrate [app_name] [previous_migration]

---

## DJANGO ORM PATTERNS FOR THIS PROJECT

### N+1 Prevention (Critical)
Wrong (N+1):
  properties = Property.objects.filter(landlord=user)
  for property in properties:
      lease = property.lease_set.filter(status='Active').first()
      # This fires one query per property — N+1

Correct (2 queries total):
  properties = Property.objects.filter(
      landlord=user
  ).prefetch_related(
      Prefetch('lease_set',
               queryset=Lease.objects.filter(status='Active'),
               to_attr='active_leases')
  )

### ACID Transactions
from django.db import transaction

with transaction.atomic():
    invoice.status = 'Paid'
    invoice.paid_at = timezone.now()
    invoice.save()

    Transaction.objects.create(
        invoice=invoice,
        amount=invoice.total_amount,
        gateway_reference=gateway_ref
    )

    Notification.objects.create(
        user=invoice.tenant,
        message='Payment confirmed'
    )
# If any operation raises an exception, ALL are rolled back

### Soft Deletes via Django Manager
class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class Property(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)
    objects = SoftDeleteManager()  # default manager excludes deleted
    all_objects = models.Manager() # access all including deleted

### IDOR-Safe Queries (ownership scoping)
# Always scope to the authenticated user
Invoice.objects.filter(
    id=invoice_id,
    tenant=request.user  # IDOR protection at query level
).get()
# If the invoice belongs to another tenant, this raises DoesNotExist
# The view returns 404 — which reveals no information about
# whether the invoice exists at all

---

## DJANGO CHANNELS (WebSocket Architecture)

Django Channels replaces standard Django WSGI with ASGI.
ASGI handles both HTTP (standard requests) and WebSocket connections.

Channel Layer: Redis
  All WebSocket messages are routed through Redis.
  This allows multiple Daphne workers to share WebSocket state.
  A message sent to Landlord from Tenant arrives at any worker
  and is delivered to the correct WebSocket connection.

WebSocket Consumer (chat/consumers.py):
  Handles: connect, disconnect, receive, send
  Authentication: JWT token passed in WebSocket URL query parameter
  on connect, verified before the connection is accepted
  Group naming: chat_[conversation_id]
  Every landlord-tenant pair has a unique group
  Messages sent to the group are delivered to all connected members

WebSocket Consumer (notifications/consumers.py):
  Group naming: notifications_[user_id]
  Server-side events call async_to_sync(channel_layer.group_send)
  to push notifications to the connected user's WebSocket

---

## CELERY (Replaces APScheduler)

Celery runs as a separate process from the Django application.
Celery Beat runs as another separate process managing schedules.

Django settings integration:
  CELERY_BROKER_URL = 'redis://localhost:6379/1'
  CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
  CELERY_TIMEZONE = 'UTC'
  CELERY_BEAT_SCHEDULE defines the cron schedules

Tasks call Django ORM operations directly —
they run in a Django application context with full model access.

Automation toggle integration:
  Each task checks AutomationSetting.objects.get(
      landlord=landlord,
      automation_type='late_fee'
  ).is_enabled
  before executing its main logic.

---

## MYSQL-SPECIFIC SETTINGS

settings/base.py critical MySQL configurations:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'connect_timeout': 10,
        },
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        }
    }
}

MySQL server configuration (my.cnf):
  [mysqld]
  character-set-server = utf8mb4
  collation-server = utf8mb4_unicode_ci
  default-storage-engine = InnoDB
  innodb_strict_mode = 1
  sql_mode = STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO

These MySQL server settings ensure:
  utf8mb4: Full Unicode support
  InnoDB: ACID transactions and foreign keys on all tables
  STRICT mode: Data integrity — no silent truncation or coercion
```

---

# 📋 PART 6 — UPDATED security.md (Django-Specific Security)

```md
# 🔒 security.md — Django + MySQL Security Update

---

## DJANGO SECURITY SETTINGS (settings/production.py)

# HTTPS enforcement
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# HSTS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Cookie security
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = False  # Must be False — JS reads this cookie for AJAX
CSRF_COOKIE_SAMESITE = 'Lax'

# Security headers (SecurityMiddleware handles these)
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
     'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Password hashing — bcrypt as primary hasher
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]

---

## DJANGO CSRF PROTECTION

Django's CsrfViewMiddleware is always in the middleware stack.
All state-changing requests (POST/PUT/PATCH/DELETE) must include:
  Header: X-CSRFToken: [cookie value]

JavaScript pattern to read and send CSRF token:
  function getCsrfToken() {
      return document.cookie
          .split(';')
          .find(c => c.trim().startsWith('csrftoken='))
          ?.split('=')[1];
  }

  fetch('/api/v1/payments/submit', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`,
          'X-CSRFToken': getCsrfToken()
      },
      body: JSON.stringify(data)
  });

DRF JWT endpoints are CSRF-exempt (JWT provides equivalent protection).
Django template-rendered HTML form endpoints require CSRF tokens.
All AJAX endpoints require both JWT and CSRF.

---

## DJANGO ORM SQL INJECTION PREVENTION

Django's ORM uses parameterized queries by default.
The ORM never concatenates user input into SQL strings.
SQL injection through normal ORM usage is categorically prevented.

Raw SQL — when used — must still use parameters:
  # Safe
  Invoice.objects.raw(
      'SELECT * FROM financials_invoice WHERE tenant_id = %s',
      [tenant_id]
  )

  # NEVER DO THIS
  Invoice.objects.raw(
      f'SELECT * FROM financials_invoice WHERE tenant_id = {tenant_id}'
  )

---

## DJANGO PERMISSIONS AND IDOR

DRF permission classes (apps/users/permissions.py):
  IsLandlord: request.user.role == 'landlord'
  IsTenant: request.user.role == 'tenant'
  IsOwnerOrLandlord: request.user == obj.tenant or request.user == obj.landlord
  IsResourceOwner: request.user == obj.owner

Every ViewSet declares its permission_classes:
  class InvoiceViewSet(viewsets.ModelViewSet):
      permission_classes = [IsAuthenticated, IsTenant]

      def get_queryset(self):
          # IDOR prevention at query level
          return Invoice.objects.filter(tenant=self.request.user)

The get_queryset override is the most important IDOR protection in Django.
It scopes every query to the authenticated user automatically.
No invoice ID that belongs to another tenant will ever be returned —
regardless of what ID is in the URL.

---

## DJANGO RATE LIMITING

Custom Django middleware in middleware/rate_limit_middleware.py.
Uses Django's cache framework (Redis backend) to track request counts.
Cache key: f"rate_limit:{request.user.id}:{request.path}"
Increments on every request, checks against endpoint-specific limits.

Additionally: django-ratelimit package for per-view rate limiting.
Applied as decorators on sensitive ViewSet methods:
  @method_decorator(ratelimit(key='user', rate='3/5m', method='POST'))
  def create(self, request):  # payment submission
      ...

---

## MYSQL SECURITY

MySQL user for the application has minimum required permissions:
  GRANT SELECT, INSERT, UPDATE, DELETE ON rentlease.* TO 'app_user'@'localhost';
  -- NO DROP, NO CREATE, NO ALTER, NO GRANT
  -- Schema changes only via Django migrations run by admin user

MySQL connection from Django:
  Password stored in environment variable only
  Never in settings.py directly
  Loaded via python-decouple: env('DB_PASSWORD')

MySQL data-at-rest encryption:
  InnoDB tablespace encryption enabled for sensitive tables
  (users, invoices, transactions, messages, compliance_documents)
```

---

# 📋 PART 7 — UPDATED requirements.txt

```txt
# requirements.txt
# Rent & Lease Management System — Complete Python Dependencies
# Install: pip install -r requirements.txt

# ── Core Framework ──────────────────────────────────────────
Django==4.2.11                      # Core web framework (LTS)
djangorestframework==3.14.0         # REST API framework
djangorestframework-simplejwt==5.3.1 # JWT authentication for DRF

# ── Real-Time (WebSockets) ──────────────────────────────────
channels==4.0.0                     # Django ASGI + WebSocket support
channels-redis==4.1.0               # Redis channel layer for Channels
daphne==4.0.0                       # ASGI server for production

# ── Background Tasks ────────────────────────────────────────
celery==5.3.6                       # Background task queue
django-celery-beat==2.5.0           # Scheduled task management
django-celery-results==2.5.1        # Task result storage
redis==5.0.1                        # Redis Python client (broker + cache)

# ── Database ────────────────────────────────────────────────
mysqlclient==2.2.0                  # MySQL adapter (Django recommended)
# Alternative if mysqlclient fails to install:
# PyMySQL==1.1.0

# ── Security ────────────────────────────────────────────────
django-cors-headers==4.3.1          # CORS headers middleware
bcrypt==4.1.2                       # bcrypt password hasher
cryptography==42.0.0                # AES encryption for chat messages
django-ratelimit==4.1.0             # Per-view rate limiting decorator

# ── File Handling ────────────────────────────────────────────
Pillow==10.2.0                      # Image validation and processing
django-storages==1.14.2             # Abstracted file storage backends
boto3==1.34.0                       # S3-compatible storage (production)

# ── Email ───────────────────────────────────────────────────
# Django has built-in SMTP email — no extra package needed
# For SendGrid:
# sendgrid==6.11.0

# ── Configuration ────────────────────────────────────────────
python-decouple==3.8                # Environment variable management
django-environ==0.11.2              # Alternative: .env file loading

# ── Payments ────────────────────────────────────────────────
stripe==8.4.0                       # Stripe payment gateway SDK

# ── Utilities ────────────────────────────────────────────────
Pillow==10.2.0                      # Image processing (already listed)
python-dateutil==2.8.2              # Date arithmetic utilities

# ── Development Only ─────────────────────────────────────────
# (move to requirements-dev.txt in production)
django-debug-toolbar==4.3.0         # Development query debugging
factory-boy==3.3.0                  # Test data factories
locust==2.22.0                      # Load testing
coverage==7.4.0                     # Test coverage reporting
```

---

# 📋 PART 8 — KEY DJANGO CONCEPTS EVERY TEAM MEMBER MUST KNOW

```md
# Django Fundamentals for This Project
# What every person on the team must understand

---

## 1. DJANGO SETTINGS SPLIT

Never put everything in one settings.py.
  config/settings/base.py     → Common to all environments
  config/settings/development.py → DEBUG=True, SQLite ok, no HTTPS
  config/settings/production.py  → DEBUG=False, MySQL, HTTPS enforced

Run with specific settings:
  python manage.py runserver --settings=config.settings.development
  Production: DJANGO_SETTINGS_MODULE=config.settings.production

---

## 2. CUSTOM USER MODEL — MUST BE SET FIRST

Before running ANY migration:
  AUTH_USER_MODEL = 'users.CustomUser' must be in settings.
  If this is changed after migrations exist, the entire database
  must be rebuilt. This is not recoverable incrementally.
  Set it in base.py before python manage.py migrate is ever run.

---

## 3. DJANGO MIGRATIONS ARE THE SCHEMA

No separate database_schema.sql.
Django migrations ARE the schema.
  python manage.py makemigrations  → generates migration files
  python manage.py migrate         → applies migrations to MySQL
  python manage.py showmigrations  → shows applied/unapplied status
  python manage.py sqlmigrate app 0001 → shows the SQL a migration generates

---

## 4. DJANGO ADMIN (Available but Optional)

Django ships with a built-in admin interface.
The project scope says no admin panel.
But Django admin can serve as the minimal operations console
discussed in the solutions document — restricted to staff users,
accessible only from internal IP, used only for emergency operations.
This replaces the need to build a custom operations console from scratch.

Enable with: admin.site.register(CustomUser, CustomUserAdmin)
Protect with: AdminSiteOnlyForStaffMiddleware or IP restriction

---

## 5. DJANGO SIGNALS (For Cross-App Events)

Django signals allow decoupled communication between apps.
When an invoice is marked Paid, a signal fires.
The notifications app listens for that signal and creates a notification.
The analytics app listens and updates cached metrics.
Neither app directly calls the other.
This preserves separation of concerns across Django apps.

Key signals used:
  post_save on Invoice (status change to Paid)
  post_save on MaintenanceTicket (status change to Resolved)
  post_save on Lease (status change to Active)

---

## 6. DJANGO TESTING

Django provides a test client and test database.
Tests use a separate MySQL test database created automatically.
  python manage.py test              → runs all tests
  python manage.py test apps.users   → runs only users app tests

Test database is created fresh before each test run.
Tests are isolated — no production data is ever touched.
The test database uses the same MySQL configuration as development.
```

---

# 📊 THE COMPLETE UPDATE SUMMARY

| What Changed | From | To | Impact |
|---|---|---|---|
| Web framework | Flask (micro) | Django 4.2 LTS (full) | Architecture, ORM, middleware, auth all provided |
| API framework | Manual Flask routes | Django REST Framework | Serializers, viewsets, permissions, routers |
| Authentication | PyJWT manual | simplejwt + Django auth | Full auth system with JWT |
| Middleware | Custom from scratch | Django middleware + custom | Built-in security, CSRF, auth in pipeline |
| Database | PostgreSQL | MySQL 8.0 (InnoDB) | utf8mb4, STRICT mode, InnoDB required |
| ORM | Raw SQL (psycopg2) | Django ORM | Parameterized by default, N+1 solved by design |
| Schema management | database_schema.sql | Django migrations | Python-managed, version-controlled, reversible |
| WebSockets | Flask-SocketIO | Django Channels + Redis | ASGI, channel layer, consumer pattern |
| Background jobs | APScheduler | Celery + celery-beat | Distributed, monitored, Redis-backed |
| File storage | Local file system | django-storages abstraction | Swappable to S3 without code changes |
| CSRF | Manual tokens | Django CsrfViewMiddleware | Automatic, framework-level enforcement |
| Password hashing | Manual bcrypt | Django BCryptSHA256PasswordHasher | Framework-managed |
| Project structure | Single app | Django multi-app architecture | Clean domain separation |
| Static files | Manual paths | Django static files + collectstatic | Environment-aware serving |
| Testing | Manual pytest | Django test framework + test client | Isolated test database |

---

> **The core technology decision is clear:**
> **HTML + CSS + JavaScript on the frontend.**
> **Django + DRF + Channels on the backend.**
> **MySQL with InnoDB on the database.**
> **Redis for WebSockets and Celery.**
>
> Every principle, every security rule, every architectural decision
> from every conversation in this chat remains exactly the same.
> Only the tools implementing those decisions have been updated
> to reflect the correct, final technology stack.
