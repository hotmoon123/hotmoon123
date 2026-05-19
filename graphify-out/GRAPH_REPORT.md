# Graph Report - .  (2026-05-19)

## Corpus Check
- Large corpus: 281 files · ~581,279 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 1119 nodes · 3064 edges · 44 communities detected
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 378 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `zs` - 71 edges
2. `_i()` - 62 edges
3. `Landlord` - 59 edges
4. `Tenant` - 58 edges
5. `Lease` - 54 edges
6. `os()` - 54 edges
7. `Property` - 51 edges
8. `Invoice` - 46 edges
9. `Transaction` - 46 edges
10. `MaintenanceTicket` - 43 edges

## Surprising Connections (you probably didn't know these)
- `Canonical user models live in apps.users.models — import from there.` --uses--> `CustomUserManager`  [INFERRED]
  features/authentication/backend/models.py → apps/users/models.py
- `RoleAuthorizationMiddleware` --uses--> `Landlord`  [INFERRED]
  middleware/authorization_middleware.py → apps/users/models.py
- `RoleAuthorizationMiddleware` --uses--> `Tenant`  [INFERRED]
  middleware/authorization_middleware.py → apps/users/models.py
- `IDOR Authorization Middleware  Prevents Insecure Direct Object Reference attacks` --uses--> `Landlord`  [INFERRED]
  core/middleware/authorization_middleware.py → apps/users/models.py
- `IDOR Authorization Middleware  Prevents Insecure Direct Object Reference attacks` --uses--> `Tenant`  [INFERRED]
  core/middleware/authorization_middleware.py → apps/users/models.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.03
Nodes (157): AbstractBaseUser, ConcreteUserBackend, get_concrete_user(), Session auth must return Landlord / Tenant instances, not only CustomUser.  With, Resolve an MTI parent row to Landlord or Tenant when a child row exists., Same as ModelBackend, but request.user is the concrete MTI subclass., IDORAuthorizationMiddleware, IDOR Authorization Middleware  Prevents Insecure Direct Object Reference attacks (+149 more)

### Community 1 - "Community 1"
Cohesion: 0.02
Nodes (117): A(), Aa(), add(), addControllers(), addElements(), addPlugins(), addScales(), ae (+109 more)

### Community 2 - "Community 2"
Cohesion: 0.03
Nodes (51): apply(), as(), at(), Ba(), buildLookupTable(), buildTicks(), _calculateBarValuePixels(), constructor() (+43 more)

### Community 3 - "Community 3"
Cohesion: 0.04
Nodes (31): addBox(), be(), Ce(), cs(), de(), describe(), ea(), _exec() (+23 more)

### Community 4 - "Community 4"
Cohesion: 0.04
Nodes (24): beforeUpdate(), configure(), ds(), fa(), ga(), generateLabels(), getLabelAndValue(), getLabelForValue() (+16 more)

### Community 5 - "Community 5"
Cohesion: 0.07
Nodes (26): afterDraw(), afterEvent(), afterUpdate(), beforeDatasetDraw(), beforeDatasetsDraw(), beforeLayout(), bn(), ci() (+18 more)

### Community 6 - "Community 6"
Cohesion: 0.2
Nodes (46): A(), B(), Bt(), c(), Ct(), d(), Dt(), E() (+38 more)

### Community 7 - "Community 7"
Cohesion: 0.16
Nodes (31): a(), b(), Be(), Ct(), d(), De(), Dt(), e() (+23 more)

### Community 8 - "Community 8"
Cohesion: 0.14
Nodes (2): ma, pa

### Community 9 - "Community 9"
Cohesion: 0.16
Nodes (4): qa, ua(), xa(), ya()

### Community 10 - "Community 10"
Cohesion: 0.18
Nodes (5): bs, getPlugin(), removeBox(), stop(), vs()

### Community 11 - "Community 11"
Cohesion: 0.16
Nodes (14): Exception, AuthorizationError, BusinessRuleError, EmailServiceError, PaymentError, Custom exceptions for the Rent & Lease Management System., Raised when email sending fails., Raised when payment processing fails. (+6 more)

### Community 12 - "Community 12"
Cohesion: 0.12
Nodes (15): create_user(), generate_password_reset_token(), generate_verification_token(), Users App — Business Logic (Layer 7)  Dynamic process orchestration for user ope, Generate a password reset token with 15-minute expiry.     Returns the raw token, Send password reset link to the user., Reset password using a valid token.     Returns the user if successful, None if, Create a new user account.     Password is hashed automatically by Django's set_ (+7 more)

### Community 13 - "Community 13"
Cohesion: 0.38
Nodes (1): APIClient

### Community 14 - "Community 14"
Cohesion: 0.33
Nodes (9): Ba(), Eu(), fa(), Gu(), Iu(), ka(), Pa(), Wu() (+1 more)

### Community 15 - "Community 15"
Cohesion: 0.2
Nodes (9): Users App — Business Rules (Layer 6)  Fixed, non-negotiable system constraints f, Validate email format using regex pattern., Password must be at least 8 characters with:     - At least one uppercase letter, Role must be exactly 'landlord' or 'tenant'., First and last name are required and must not be blank., validate_email_format(), validate_name_not_empty(), validate_password_strength() (+1 more)

### Community 16 - "Community 16"
Cohesion: 0.22
Nodes (1): Ji

### Community 17 - "Community 17"
Cohesion: 0.29
Nodes (4): RateLimitMiddleware, Rate Limiting Middleware  Two-tier rate limiting as defined in the security arch, Per-IP rate limiting with endpoint-specific overrides., Extract client IP, accounting for reverse proxy headers.

### Community 18 - "Community 18"
Cohesion: 0.48
Nodes (6): AppConfig, FinancialsConfig, LeasesConfig, MaintenanceConfig, PropertiesConfig, UsersConfig

### Community 19 - "Community 19"
Cohesion: 0.33
Nodes (7): Authentication System, Database Layer (MySQL), Django Core Framework, Frontend (Templates + JS), Landlord Features, REST API Layer (DRF), Tenant Features

### Community 20 - "Community 20"
Cohesion: 0.33
Nodes (3): Request Logging Middleware  Logs every request to the console with timing inform, Logs method, path, user, status code, and response time for every request., RequestLoggingMiddleware

### Community 21 - "Community 21"
Cohesion: 0.4
Nodes (5): Shared email service for the Rent & Lease Management System. Handles all email s, Send an email with HTML and text fallback.          Args:         subject: Email, Convenience method for sending templated emails.          Args:         subject:, send_email(), send_templated_email()

### Community 22 - "Community 22"
Cohesion: 0.5
Nodes (3): BaseUserManager, CustomUserManager, Manager for creating users with email as the identifier.

### Community 23 - "Community 23"
Cohesion: 0.4
Nodes (3): forwards_migrate_profiles(), Migration, Copy old `landlords` / `tenants` profile rows into MTI child tables.

### Community 24 - "Community 24"
Cohesion: 0.4
Nodes (3): BaseCommand, Command, Management command to create test users for development.  Usage:     python mana

### Community 25 - "Community 25"
Cohesion: 0.5
Nodes (3): Registration View — Single Responsibility Handles HTTP request/response for user, POST /api/v1/auth/register/          Creates a new user account and queues verif, register_view()

### Community 26 - "Community 26"
Cohesion: 0.67
Nodes (2): main(), Run administrative tasks.

### Community 27 - "Community 27"
Cohesion: 0.67
Nodes (0): 

### Community 28 - "Community 28"
Cohesion: 1.0
Nodes (1): Application-wide constants for the Rent & Lease Management System.

### Community 29 - "Community 29"
Cohesion: 1.0
Nodes (1): Root URL Configuration — Rent & Lease Management System Frontend HTML pages + JS

### Community 30 - "Community 30"
Cohesion: 1.0
Nodes (1): Migration

### Community 31 - "Community 31"
Cohesion: 1.0
Nodes (1): Migration

### Community 32 - "Community 32"
Cohesion: 1.0
Nodes (1): Migration

### Community 33 - "Community 33"
Cohesion: 1.0
Nodes (1): Migration

### Community 34 - "Community 34"
Cohesion: 1.0
Nodes (1): Migration

### Community 35 - "Community 35"
Cohesion: 1.0
Nodes (1): Migration

### Community 36 - "Community 36"
Cohesion: 1.0
Nodes (1): Django Settings — Rent & Lease Management System

### Community 37 - "Community 37"
Cohesion: 1.0
Nodes (1): WSGI config for core project.  It exposes the WSGI callable as a module-level va

### Community 38 - "Community 38"
Cohesion: 1.0
Nodes (1): ASGI config for Rent & Lease Management System.  Supports both HTTP and WebSocke

### Community 39 - "Community 39"
Cohesion: 1.0
Nodes (0): 

### Community 40 - "Community 40"
Cohesion: 1.0
Nodes (0): 

### Community 41 - "Community 41"
Cohesion: 1.0
Nodes (0): 

### Community 42 - "Community 42"
Cohesion: 1.0
Nodes (0): 

### Community 43 - "Community 43"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **54 isolated node(s):** `Run administrative tasks.`, `Request Logging Middleware  Logs every request to the console with timing inform`, `Logs method, path, user, status code, and response time for every request.`, `Rate Limiting Middleware  Two-tier rate limiting as defined in the security arch`, `Application-wide constants for the Rent & Lease Management System.` (+49 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 28`** (2 nodes): `constants.py`, `Application-wide constants for the Rent & Lease Management System.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (2 nodes): `urls.py`, `Root URL Configuration — Rent & Lease Management System Frontend HTML pages + JS`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (2 nodes): `0002_remove_expense_idx_expenses_property_and_more.py`, `Migration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (2 nodes): `0001_initial.py`, `Migration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (2 nodes): `0002_alter_property_options_and_more.py`, `Migration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (2 nodes): `0003_alter_building_description_and_more.py`, `Migration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (2 nodes): `0004_property_address.py`, `Migration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (2 nodes): `0002_landlordprofile_tenantprofile.py`, `Migration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (2 nodes): `settings.py`, `Django Settings — Rent & Lease Management System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (2 nodes): `wsgi.py`, `WSGI config for core project.  It exposes the WSGI callable as a module-level va`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (2 nodes): `asgi.py`, `ASGI config for Rent & Lease Management System.  Supports both HTTP and WebSocke`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (2 nodes): `xlsx.full.min.js`, `make_xlsx_lib()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (1 nodes): `admin.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (1 nodes): `serializers.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (1 nodes): `tests.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (1 nodes): `docx.umd.min.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `zs` connect `Community 2` to `Community 1`, `Community 4`, `Community 5`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **Why does `_i()` connect `Community 3` to `Community 1`, `Community 2`, `Community 4`, `Community 5`, `Community 8`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Why does `os()` connect `Community 4` to `Community 1`, `Community 2`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Are the 56 inferred relationships involving `Landlord` (e.g. with `RoleAuthorizationMiddleware` and `IDOR Authorization Middleware  Prevents Insecure Direct Object Reference attacks`) actually correct?**
  _`Landlord` has 56 INFERRED edges - model-reasoned connections that need verification._
- **Are the 55 inferred relationships involving `Tenant` (e.g. with `RoleAuthorizationMiddleware` and `IDOR Authorization Middleware  Prevents Insecure Direct Object Reference attacks`) actually correct?**
  _`Tenant` has 55 INFERRED edges - model-reasoned connections that need verification._
- **Are the 51 inferred relationships involving `Lease` (e.g. with `Domain helpers for invoices, payments, and landlord reporting.` and `Sum ``Transaction.amount`` per calendar month for the trailing ``num_months```) actually correct?**
  _`Lease` has 51 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Run administrative tasks.`, `Request Logging Middleware  Logs every request to the console with timing inform`, `Logs method, path, user, status code, and response time for every request.` to the rest of the system?**
  _54 weakly-connected nodes found - possible documentation gaps or missing edges._