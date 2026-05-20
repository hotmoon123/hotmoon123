# MASTER REBUILD PROMPT — RentFlow CRM v1.0
## Complete System Specification & Implementation Blueprint

**Institution:** Regional Maritime University, Accra, Ghana  
**Team IDs:** BCE0000725 | BIT00021427 | BIT3105227  
**Project:** RentFlow CRM — Rent & Lease Management System  
**Date:** 2026-05-20  
**Status:** ✅ PRODUCTION-READY SPECIFICATION

---

## ROLE & EXECUTION FRAMEWORK

Act as an elite Senior Full-Stack Engineering Team encompassing:
- Principal Systems Architect
- Backend Django Engineer  
- UI/UX Designer
- Database Administrator
- Frontend Motion Engineer
- QA Security Engineer
- DevSecOps Engineer
- Product Manager

Apply Bloom's Revised Taxonomy Levels 1–6:
- L1 Remember → L2 Understand → L3 Apply → L4 Analyse → L5 Evaluate → L6 Create

Answer every structural decision using:
- **WHAT** it is | **WHY** it exists | **WHEN** to use it | **HOW** it works | **WHERE** it fits | **WHICH** pattern is cleanest

Govern all output using eight prompt frameworks simultaneously:
- RTF + SOLVE + TAG + RACE + DREAM + PACT + CARE + RISE

---

## TECHNOLOGY STACK — NON-NEGOTIABLE

### Backend
- Python 3.13
- Django 4.2.30
- Function-based views ONLY (no class-based views)
- Django session-based authentication
- Django ORM (no raw SQL in views)
- python-decouple for .env config
- mysqlclient for MySQL connection
- Pillow for image/file uploads

### Database
- MySQL via XAMPP (MariaDB 10.4.28)
- Host: 127.0.0.1 | Port: 3306 | User: root | Password: (empty)
- Database name: rent_lease_db
- Primary keys: BIGINT AUTO_INCREMENT (NOT UUID)
- Schema: docs/rent_lease_db_new_schema.sql

### Frontend
- HTML5 (Django template language)
- CSS3 (custom design system)
- Vanilla JavaScript ES6+ (fetch API, no jQuery, no React)
- CDN libraries (see below)

### ABSOLUTELY FORBIDDEN
❌ Django REST Framework (DRF)  
❌ JWT tokens (SimpleJWT, PyJWT)  
❌ Celery or Redis  
❌ Django Channels or WebSockets  
❌ Daphne or ASGI servers  
❌ Custom middleware folder  
❌ Any /api/ URL prefix  
❌ UUID primary keys  
❌ SQLite database  
❌ Class-based views  
❌ Bootstrap or Tailwind  

---

## SECURITY ARCHITECTURE — INLINE VIEW-LEVEL ONLY

ALL security checks happen INSIDE view functions only.  
Zero custom middleware. Pure Python if/else logic.

### Role Check Pattern (Landlord)
```python
if request.session.get('user_role') != 'landlord':
    return redirect('/login/')
```

### Role Check Pattern (Tenant)
```python
if request.session.get('user_role') != 'tenant':
    return redirect('/login/')
```

### Session Variables Set on Login
```python
request.session['user_role'] = 'landlord'  # or 'tenant'
request.session['user_id'] = str(user.id)
request.session['user_email'] = user.email
request.session['user_name'] = user.first_name
```

### OWASP Top 10 Implementation
- **A01 Broken Access Control** → view-level role checks
- **A02 Cryptographic Failures** → Django password hashing (PBKDF2)
- **A03 Injection** → Django ORM (no raw SQL)
- **A04 Insecure Design** → session isolation per role
- **A05 Security Misconfiguration** → DEBUG=False in production
- **A07 Auth Failures** → EmailBackend + session management
- **A08 Data Integrity** → CSRF tokens on all POST forms
- **XSS Prevention** → Django template auto-escaping
- **SQL Injection** → ORM prepared statements only
- **CSRF Protection** → {% csrf_token %} on all forms
- **Input Validation** → server-side in every view
- **Data Sanitization** → .strip() + type checking
- **Rate Limiting** → view-level request counters using Django cache

---

## DESIGN SYSTEM — Janus Tiu Standard

### Color Palette
```
Primary:         #003366 — Deep Navy Blue (main actions, nav, buttons, headers)
Primary Light:   #0052A3 — Medium Blue (hover states, secondary buttons)
Primary Dark:    #001F3F — Dark Navy (sidebar, footer)
Secondary:       #00A86B — Emerald Green (success, paid badges, active)
Accent:          #F0A500 — Amber Gold (warnings, pending, MoMo highlights)
Danger:          #DC3545 — Red (overdue, errors, delete)
Background:      #F4F6F9 — Light Grey (page canvas)
Surface:         #FFFFFF — Pure White (cards, modals, forms)
Surface Alt:     #F8F9FA — Off White (table rows, alternating BGs)
Text Primary:    #1A1A2E — Near Black (headings, body)
Text Secondary:  #6C757D — Medium Grey (captions, labels, placeholders)
Text Muted:      #ADB5BD — Light Grey (disabled, hints)
Border:          #DEE2E6 — Light border (dividers, inputs)
Border Focus:    #003366 — Navy (focused input borders)
Success:         #00A86B — Green
Warning:         #F0A500 — Amber
Error:           #DC3545 — Red
Info:            #17A2B8 — Teal
```

### Typography (Google Fonts via CDN)
- **Primary Font:** 'Inter' — headings, navigation, buttons
- **Secondary Font:** 'DM Sans' — body text, labels, captions
- **Mono Font:** 'JetBrains Mono' — code, IDs, references
- **Headings:** bold, tracking tight (-0.02em)
- **Body:** regular weight (400), line-height 1.6
- **Size Scale:** 12 / 14 / 16 / 18 / 20 / 24 / 32 / 40 / 48px

### Spacing Scale (4px base unit)
Values: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96px

### Border Radius
- **Small:** 6px (inputs, chips, badges, tags)
- **Medium:** 12px (cards, buttons, dropdowns)
- **Large:** 20px (modals, large containers, hero sections)
- **Full:** 9999px (avatars, pills, toggle switches)

### Shadows
```
Subtle:  0 1px 3px rgba(0, 51, 102, 0.08)
Medium:  0 4px 12px rgba(0, 51, 102, 0.12)
Strong:  0 8px 24px rgba(0, 51, 102, 0.18)
Card:    0 2px 8px rgba(0, 0, 0, 0.08)
```

### Component Patterns

**Buttons:**
- Primary: bg #003366, white text, 44px height, 12px/24px padding, 12px radius
- Hover: bg #0052A3, transform scale(1.02), transition 0.2s ease
- Secondary: border #003366, blue text, same dimensions
- Danger: bg #DC3545, white text
- Disabled: opacity 0.5, cursor not-allowed

**Inputs/Forms:**
- Height: 44px, padding: 12px 16px
- Border: 1.5px solid #DEE2E6
- Focus: border-color #003366, box-shadow 0 0 0 3px rgba(0,51,102,0.1)
- Border radius: 6px
- Font size: 14px

**Cards:**
- Padding: 24px
- Background: #FFFFFF
- Border: 1px solid #DEE2E6
- Border radius: 12px
- Shadow: card shadow
- Hover: shadow increases to medium

**Data Tables:**
- Header: bg #F8F9FA, text #003366, font-weight 600
- Row hover: bg #F0F4FF (light blue tint)
- Border: 1px solid #DEE2E6
- Padding: 12px 16px per cell

**Stat Cards (Dashboard Metrics):**
- Large number: 32px, bold, color Primary
- Label: 14px, Text Secondary
- Icon: 40px circle, Primary Light bg
- Trend chip: green/red with arrow icon
- Shadow: card shadow

**Status Badges:**
- Active/Paid/Available: bg #E6F7F0, text #00A86B
- Pending/Warning: bg #FFF8E6, text #F0A500
- Overdue/Danger: bg #FDE8EA, text #DC3545
- Inactive/Muted: bg #F8F9FA, text #6C757D
- In Progress: bg #E8F0FE, text #003366
- Cancelled: bg #FEF3F0, text #DC3545
- Maintenance: bg #FFF3CD, text #856404

**Sidebar Navigation:**
- Width: 260px, bg #001F3F (dark navy)
- Active item: bg #003366, left border 3px #F0A500
- Hover: bg rgba(255,255,255,0.08)
- Text: white, icon: #ADB5BD
- Logo area: 72px height, bg #001F3F

### Design Rules
1. Never introduce colors outside this palette
2. Always use the spacing scale — no arbitrary values
3. Maintain consistent border radius per element type
4. When in doubt, add more whitespace
5. Every interactive element gets a hover transition (0.2s ease)
6. Every form field gets focus state feedback
7. Every data state (empty, loading, error) gets a visual
8. Status always shown with color + icon + text (never color alone)

---

## CDN LIBRARIES — Load in Base Templates

Load ALL of these in base_landlord.html and base_tenant.html:

```html
<!-- ── FONTS ── -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

<!-- ── ICONS ── -->
<script src="https://unpkg.com/@phosphor-icons/web@2.1.1"></script>

<!-- ── CHARTS ── -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>

<!-- ── ANIMATIONS ── -->
<link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
<script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">

<!-- ── NOTIFICATIONS ── -->
<link rel="stylesheet" type="text/css" 
  href="https://cdn.jsdelivr.net/npm/toastify-js/src/toastify.min.css">
<script type="text/javascript" 
  src="https://cdn.jsdelivr.net/npm/toastify-js"></script>

<!-- ── DATE PICKER ── -->
<link rel="stylesheet" 
  href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>

<!-- ── PARTICLES (landing page only) ── -->
<script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>

<!-- ── COUNTERS ── -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/countup.js/2.8.0/countUp.umd.min.js"></script>
```

Initialize AOS in every page's script block:
```javascript
AOS.init({ duration: 600, easing: 'ease-out-cubic', once: true });
```

---

## DATABASE ARCHITECTURE

Import SQL schema first:
```bash
/opt/lampp/bin/mysql -u root -e \
  "DROP DATABASE IF EXISTS rent_lease_db; 
   CREATE DATABASE rent_lease_db 
   CHARACTER SET utf8mb4 
   COLLATE utf8mb4_unicode_ci;"
/opt/lampp/bin/mysql -u root rent_lease_db \
  < docs/rent_lease_db_new_schema.sql
```

### 20 Business Tables

**USER TABLES (no shared users table):**
1. landlord_accounts — ALL landlord data + login credentials
2. tenant_accounts — ALL tenant data + login credentials
3. password_reset_tokens

**PROPERTY:**
4. buildings
5. properties (field: property_type, default: 'available')

**LEASE:**
6. leases (has: deposit_amount, contract_pdf)
7. invitations

**FINANCIAL:**
8. invoices (FK: rental_property_id, has: invoice_type)
9. transactions (has: idempotency_key, momo fields)
10. expenses (FK: rental_property_id, has: receipt)
11. payment_methods (has: method_type, exp_month, exp_year, gateway_customer_id, momo_provider, momo_number)

**MAINTENANCE:**
12. maintenance_tickets (has: photo, estimated_cost)

**COMMUNICATIONS:**
13. notifications
14. activity_log
15. messages
16. notices

**DOCUMENTS:**
17. documents
18. compliance_documents

**OPERATIONS:**
19. inspections
20. automation_rules

---

## IMPLEMENTATION ORDER — Execute in EXACT Sequence

1. Drop old database → import rent_lease_db_new_schema.sql
2. Delete all old migration files (keep __init__.py)
3. Delete db.sqlite3 if it exists
4. Rewrite core/settings.py (MySQL, no AUTH_USER_MODEL, no custom middleware, Africa/Accra timezone)
5. Create .env file
6. Install: pip install mysqlclient python-decouple Pillow
7. Rewrite apps/users/models.py with Landlord and Tenant (BIGINT PKs)
8. Rewrite apps/users/auth_backend.py (EmailBackend checks both)
9. Rewrite apps/users/views.py (register, login, logout, forgot/reset)
10. Update apps/users/business_logic.py (PasswordResetToken)
11. Rewrite all app models (match SQL field names exactly)
12. Register all models in admin.py files
13. Rewrite core/views.py (all page views, role checks, inline session validation)
14. Rewrite core/urls.py (all routes)
15. Create/update frontend/static/css/main.css (design system)
16. Create/update frontend/static/js/main.js (utilities)
17. Create/update base_landlord.html and base_tenant.html (include all CDN libraries)
18. Build ALL 30 HTML templates (5 public + 15 landlord + 10 tenant)
19. Add page-specific JS files for dashboard charts
20. Run: python manage.py makemigrations (all apps)
21. Run: python manage.py migrate --fake-initial
22. Run: python manage.py check → must be 0 issues
23. Test user creation in shell
24. Run: python manage.py runserver
25. Test full flow: register → login → dashboard

---

## VERIFICATION CHECKLIST

```bash
# 1. System check
python manage.py check

# 2. Verify MySQL tables
/opt/lampp/bin/mysql -u root rent_lease_db \
  -e "SHOW TABLES;"

# 3. Test user creation
python manage.py shell -c "
from apps.users.models import Landlord, Tenant

l = Landlord.objects.create_user(
    email='landlord@rentflow.com',
    password='Demo123!',
    first_name='Kwame',
    last_name='Mensah',
)
t = Tenant.objects.create_user(
    email='tenant@rentflow.com',
    password='Demo123!',
    first_name='Ama',
    last_name='Boateng',
)
print('Landlord id (int):', l.id, type(l.id))
print('Tenant id (int):', t.id, type(t.id))
"

# 4. Start server
python manage.py runserver
```

### EXPECTED FINAL STATE
✅ python manage.py check → 0 issues  
✅ Database: MySQL via XAMPP (NOT SQLite)  
✅ PKs: integers 1, 2, 3... (NOT UUID)  
✅ All 20+ tables in MySQL  
✅ Register landlord → row in landlord_accounts only  
✅ Register tenant → row in tenant_accounts only  
✅ Login → session['user_role'] set correctly  
✅ All 30 HTML templates render correctly  
✅ CDN libraries loaded  
✅ Design system: Navy + White + Green + Amber palette  
✅ All forms have CSRF tokens  
✅ All views have inline role session checks  
✅ GHS currency displayed throughout  
✅ MoMo payment fields in payment_methods  

---

**Use this document as the authoritative specification for rebuilding or extending RentFlow CRM.**
