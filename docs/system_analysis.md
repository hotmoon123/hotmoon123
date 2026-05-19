# 🏗️ RentFlow CRM — Complete System Analysis
### As of April 22, 2026

---

## 1. 🗄️ DATABASE — What Are We Using?

**Right now (Development):** `SQLite` — stored in `db.sqlite3` at the project root.

**In Production (when you switch):** `MySQL` — configured through the `.env` file.

> The database engine is controlled by a single line in your `.env`:
> ```
> DB_ENGINE=django.db.backends.sqlite3   ← currently SQLite
> # DB_ENGINE=django.db.backends.mysql   ← uncomment to switch to MySQL
> ```
> The `core/settings.py` reads that variable and automatically picks the right database config. You do NOT need to change any Python code to switch databases — only the `.env` file.

---

## 2. 🔗 HOW HTML, CSS, JS, PYTHON & DJANGO CONNECT — The Full Request Lifecycle

This is the most important thing to understand. Here is a plain-English walkthrough of exactly what happens when a user visits a page:

### Step-by-Step: User visits `/login/`

```
BROWSER
  │
  │  1. User types http://localhost:8000/login/ and presses Enter
  ▼
DJANGO (Python) — core/urls.py
  │  2. Django reads its URL table and finds the match:
  │     path("login/", frontend_views.login_page, name="login_page")
  │  3. Django calls the Python function `login_page` in core/views.py
  ▼
PYTHON FUNCTION — core/views.py
  │  4. def login_page(request):
  │         return render(request, "public/login.html")
  │  5. Django's `render()` function finds the HTML file at:
  │     frontend/templates/public/login.html
  ▼
DJANGO TEMPLATE ENGINE
  │  6. Django reads login.html which starts with:
  │     {% extends "base/layout_auth.html" %}
  │  7. Django assembles the final HTML by:
  │     - Taking base/layout_auth.html as the outer shell
  │     - Injecting login.html's content into {% block auth_content %}
  │     - Also pulling in base/base.html (the outer-outer shell)
  │  8. The {{ variable }} and {% tag %} syntax is filled in with real data
  ▼
BROWSER RECEIVES HTML
  │  9. The browser loads the assembled HTML page
  │  10. It finds <link rel="stylesheet" href="/static/css/design_system.css">
  │      → Django serves this from frontend/static/css/design_system.css
  │  11. It finds <script src="/static/js/api.js">
  │      → Django serves this from frontend/static/js/api.js
  ▼
JAVASCRIPT RUNS
  │  12. User fills in email + password and clicks "Sign In"
  │  13. JavaScript intercepts the form submit (e.preventDefault())
  │  14. JS calls: api.post('/auth/login/', { email, password })
  │  15. This sends an HTTP POST request to:
  │      http://localhost:8000/api/v1/auth/login/
  ▼
DJANGO REST FRAMEWORK (DRF) — API Layer
  │  16. core/urls.py matches: path('api/v1/auth/', include('apps.users.urls'))
  │  17. apps/users/urls.py matches: path('login/', views.login_view)
  │  18. The Python function login_view() in apps/users/views.py runs:
  │      a. Validates input with LoginSerializer (serializers.py)
  │      b. Checks business rules (business_rules.py)
  │      c. Calls business logic (business_logic.py)
  │      d. Queries the database for the user
  │      e. Verifies password
  │      f. Generates JWT tokens
  │      g. Returns JSON: { access, refresh, user, redirect }
  ▼
JAVASCRIPT RECEIVES JSON RESPONSE
  │  19. JS stores the token: sessionStorage.setItem('accessToken', data.access)
  │  20. JS reads data.redirect → '/landlord/dashboard/'
  │  21. JS redirects: window.location.href = data.redirect
  ▼
USER IS NOW ON THE DASHBOARD (the cycle repeats from Step 1)
```

### The Template Inheritance Chain (How HTML files connect)

```
base/base.html              ← The outermost shell. Has Bootstrap, CSS, JS links.
    └── base/layout_auth.html      ← Auth pages shell (centered card)
    │       └── public/login.html  ← The actual login content
    │       └── public/register.html
    │       └── public/forgot_password.html
    │
    └── base/layout_landlord.html  ← Landlord shell (sidebar + main area)
    │       └── landlord/dashboard.html
    │       └── landlord/properties.html  
    │       └── etc.
    │
    └── base/layout_tenant.html    ← Tenant shell
            └── tenant/dashboard.html
            └── etc.
```

### The CSS Connection

There is **one CSS file**: `frontend/static/css/design_system.css`
- It defines all CSS variables (colors, fonts, spacing)
- All templates load it via `base/base.html`
- Pages use Bootstrap 5 classes (`col-md-4`, `d-flex`, etc.) PLUS custom design system classes (`card`, `btn-primary`, `nav-link`, etc.)

### The JavaScript Connection (Two Types)

**Type 1 — Shared JS (loaded on every page):**
- `frontend/static/js/api.js` — The `APIClient` class that handles all HTTP calls to the backend API. Creates a global `api` object.

**Type 2 — Page-specific JS (inline in `{% block extra_js %}`):**
- Written inside `<script>` tags at the bottom of each HTML template
- Uses the global `api` object to call the backend
- Uses the `showToast()` function defined in `base.html`
- Uses `lucide.createIcons()` for SVG icons

---

## 3. ✅ PAGES THAT ARE BUILT & WORKING

### Public Pages
| URL | HTML Template | Status |
|-----|--------------|--------|
| `/` | `public/landing.html` | ✅ Built |
| `/login/` | `public/login.html` | ✅ Built + JS Logic |
| `/register/` | `public/register.html` | ✅ Built + JS Logic |
| `/forgot-password/` | `public/forgot_password.html` | ✅ Built |
| `/reset-password/` | `public/reset_password.html` | ✅ Built |
| `/verify-email/` | `public/verify_email.html` | ✅ Built |
| `/payment/success/` | `public/payment_success.html` | ✅ Built |
| `/payment/cancelled/` | `public/payment_cancelled.html` | ✅ Built |
| `403 / 404 / 429 / 500` | `public/error_generic.html` | ✅ Built |

### Landlord Pages
| URL | HTML Template | Status |
|-----|--------------|--------|
| `/landlord/dashboard/` | `landlord/dashboard.html` | ✅ Built (with real DB data) |
| `/landlord/properties/` | `landlord/properties.html` | ✅ Built |
| `/landlord/leases/` | `landlord/leases.html` | ✅ Built |
| `/landlord/financials/` | `landlord/financials.html` | ✅ Built |
| `/landlord/analytics/` | `landlord/analytics.html` | ✅ Built |

### Tenant Pages
| URL | HTML Template | Status |
|-----|--------------|--------|
| `/tenant/dashboard/` | `tenant/dashboard.html` | ✅ Built (with real DB data) |

---

## 4. ❌ PAGES NOT YET CREATED (Templates Missing)

### Landlord Pages — Template Files Are MISSING
| URL | Expected Template | Status |
|-----|-----------------|--------|
| `/landlord/tenants/` | `landlord/tenants.html` | ❌ NOT CREATED |
| `/landlord/maintenance/` | `landlord/maintenance.html` | ❌ NOT CREATED |
| `/landlord/chat/` | `landlord/chat.html` | ❌ NOT CREATED |
| `/landlord/documents/` | `landlord/documents.html` | ❌ NOT CREATED |
| `/landlord/notifications/` | `landlord/notifications.html` | ❌ NOT CREATED |
| `/landlord/settings/` | `landlord/settings.html` | ❌ NOT CREATED |
| `/landlord/automations/` | `landlord/automations.html` | ❌ NOT CREATED |
| `/landlord/buildings/` | `landlord/buildings.html` | ❌ NOT CREATED |
| `/landlord/expenses/` | `landlord/expenses.html` | ❌ NOT CREATED |

### Tenant Pages — Template Files Are MISSING
| URL | Expected Template | Status |
|-----|-----------------|--------|
| `/tenant/payments/` | `tenant/payments.html` | ❌ NOT CREATED |
| `/tenant/lease/` | `tenant/lease.html` | ❌ NOT CREATED |
| `/tenant/maintenance/` | `tenant/maintenance.html` | ❌ NOT CREATED |
| `/tenant/chat/` | `tenant/chat.html` | ❌ NOT CREATED |
| `/tenant/inspection/` | `tenant/inspection.html` | ❌ NOT CREATED |
| `/tenant/payment-methods/` | `tenant/payment_methods.html` | ❌ NOT CREATED |
| `/tenant/notice-board/` | `tenant/notice_board.html` | ❌ NOT CREATED |
| `/tenant/compliance/` | `tenant/compliance.html` | ❌ NOT CREATED |
| `/tenant/profile/` | `tenant/profile.html` | ❌ NOT CREATED |
| `/tenant/history/` | `tenant/history.html` | ❌ NOT CREATED |

> ⚠️ **Important:** The Python views for ALL of these pages exist in `core/views.py` and the URL routes exist in `core/urls.py`. The only missing piece is the HTML template file. If a user visits any of these URLs right now, Django will throw a `TemplateDoesNotExist` error.

---

## 5. 🔌 BACKEND API ENDPOINTS — Status

### Active API Endpoints (fully wired)
| Method | Endpoint | What it does | Status |
|--------|----------|-------------|--------|
| POST | `/api/v1/auth/register/` | Create new user account | ✅ Active |
| POST | `/api/v1/auth/login/` | Login + get JWT tokens | ✅ Active |
| POST | `/api/v1/auth/token/refresh/` | Refresh access token | ✅ Active |
| POST | `/api/v1/auth/verify-email/` | Verify email with token | ✅ Active |
| POST | `/api/v1/auth/forgot-password/` | Request password reset email | ✅ Active |
| POST | `/api/v1/auth/reset-password/` | Reset password with token | ✅ Active |
| GET | `/api/v1/auth/me/` | Get current user profile | ✅ Active |
| GET/POST | `/api/v1/properties/buildings/` | List/create buildings | ✅ Active |
| GET/PUT/DELETE | `/api/v1/properties/buildings/{id}/` | Building detail | ✅ Active |
| GET/POST | `/api/v1/properties/units/` | List/create property units | ✅ Active |
| GET/PUT/DELETE | `/api/v1/properties/units/{id}/` | Unit detail | ✅ Active |
| GET/POST | `/api/v1/leases/` | List/create leases | ✅ Active |
| GET/PUT/DELETE | `/api/v1/leases/{id}/` | Lease detail | ✅ Active |
| GET/POST | `/api/v1/financials/` | Invoices, transactions, expenses | ✅ Active |

### Commented-Out API Endpoints (Not Yet Active)
| Endpoint prefix | Status |
|----------------|--------|
| `/api/v1/maintenance/` | ⏸️ Commented out in urls.py |
| `/api/v1/chat/` | ⏸️ Commented out in urls.py |
| `/api/v1/documents/` | ⏸️ Commented out in urls.py |
| `/api/v1/analytics/` | ⏸️ Commented out in urls.py |
| `/api/v1/notifications/` | ⏸️ Commented out in urls.py |
| `/api/v1/automation/` | ⏸️ Commented out in urls.py |

---

## 6. 🐍 DJANGO APPS STATUS — All 10 Apps

| App | Models Built | API Views | Serializers | URLs | Status |
|-----|-------------|-----------|-------------|------|--------|
| `apps.users` | ✅ CustomUser, LandlordProfile, TenantProfile | ✅ Full auth | ✅ Full | ✅ | ✅ Phase 1 Complete |
| `apps.properties` | ✅ Building, Property | ✅ ViewSets | ✅ | ✅ | ✅ Phase 2 Complete |
| `apps.leases` | ✅ Lease, Invitation | ✅ ViewSets | ✅ | ✅ | ✅ Phase 2 Complete |
| `apps.financials` | ✅ Invoice, Transaction, Expense, PaymentMethod | ✅ Views | ✅ | ✅ | ✅ Phase 2 Complete |
| `apps.maintenance` | ✅ MaintenanceTicket | ❌ No views | ❌ | ❌ | ⚠️ Model only |
| `apps.chat` | ❌ Empty | ❌ | ❌ | ❌ | ❌ Stub only |
| `apps.documents` | ❌ Empty | ❌ | ❌ | ❌ | ❌ Stub only |
| `apps.analytics` | ❌ Empty | ❌ | ❌ | ❌ | ❌ Stub only |
| `apps.notifications` | ❌ Empty | ❌ | ❌ | ❌ | ❌ Stub only |
| `apps.automation` | ❌ Empty | ❌ | ❌ | ❌ | ❌ Stub only |

---

## 7. 🏛️ DATABASE TABLES THAT EXIST (via migrations)

| Table Name | Django Model | App |
|-----------|-------------|-----|
| `users` | `CustomUser` | users |
| `landlords` | `LandlordProfile` | users |
| `tenants` | `TenantProfile` | users |
| `buildings` | `Building` | properties |
| `properties` | `Property` | properties |
| `leases` | `Lease` | leases |
| `invitations` | `Invitation` | leases |
| `invoices` | `Invoice` | financials |
| `transactions` | `Transaction` | financials |
| `expenses` | `Expense` | financials |
| `payment_methods` | `PaymentMethod` | financials |
| `maintenance_tickets` | `MaintenanceTicket` | maintenance |

> Tables for `chat`, `documents`, `analytics`, `notifications`, `automation` do NOT exist yet because those app models are empty.

---

## 8. 🔐 SECURITY LAYER — What's Built

| Security Feature | Implementation | Status |
|-----------------|---------------|--------|
| JWT Authentication | `rest_framework_simplejwt` | ✅ Active |
| Password Hashing | BCrypt (bcrypt + PBKDF2 fallback) | ✅ Active |
| CSRF Protection | Django middleware | ✅ Active |
| Rate Limiting | Custom `RateLimitMiddleware` | ✅ Active |
| Request Logging | Custom `RequestLoggingMiddleware` | ✅ Active |
| IDOR Prevention | Custom `IDORAuthorizationMiddleware` | ✅ Active |
| Email Verification | Token-based, required before login | ✅ Active |
| Soft Delete | `deleted_at` field on User | ✅ Active |
| CORS | `corsheaders` package | ✅ Active |
| Security Headers | HSTS, X-Frame-Options, etc. | ✅ (in production mode) |

---

## 9. 📋 DEVELOPMENT PHASE SUMMARY

| Phase | Title | Status |
|-------|-------|--------|
| Phase 1 | Authentication & Security Perimeter | ✅ COMPLETE |
| Phase 2 | Landlord Core (Properties, Leases, Financials) | 🏗️ IN PROGRESS |
| Phase 3 | Tenant Experience (Payments, Maintenance, Chat) | 📅 PLANNED |
| Phase 4 | Real-time Features (WebSocket Chat, Notifications) | 📅 PLANNED |
| Phase 5 | Automation & Analytics | 📅 PLANNED |

---

## 10. 🗺️ WHAT TO BUILD NEXT (Priority Order)

1. **Missing HTML Templates** — 19 pages need their `.html` files created (highest priority — currently causes `TemplateDoesNotExist` crashes)
2. **Maintenance App** — Model exists, but no serializers, views, or URL routes
3. **Notifications App** — Model needed, then API
4. **Chat App** — Requires Django Channels + WebSocket consumer
5. **Documents App** — File upload/download management
6. **Analytics App** — Read-only aggregation queries
7. **Automation App** — Celery tasks (scheduled rent invoicing, etc.)
