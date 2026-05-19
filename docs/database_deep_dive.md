# 🗄️ RentFlow Database — Complete Deep Dive
### Tables · Columns · Rows · Relationships · Live Data

---

## 📖 TERMINOLOGY FIRST — Plain English

| Technical Word | Plain English Meaning | Example |
|---------------|----------------------|---------|
| **Database** | The entire file that stores ALL your data | `db.sqlite3` (the file in your project) |
| **Table** | Like a spreadsheet — one topic per table | `users`, `properties`, `leases` |
| **Column** | A field — one specific piece of info | `email`, `rent_amount`, `status` |
| **Row / Tuple** | One complete record in a table | One user, one property, one lease |
| **Primary Key (PK)** | The unique ID number for each row | `id = 1`, `id = 2`, etc. |
| **Foreign Key (FK)** | A column that points to another table's PK | `landlord_id` points to `users.id` |
| **NULL** | Empty / no value stored | A phone number field left blank |
| **NOT NULL** | This column MUST have a value | `email` is always required |

---

## 🗂️ ALL TABLES IN YOUR DATABASE

There are **27 tables total**, but only **9 are yours** (your business data).
The rest are Django's own internal tables.

### Your 9 Business Tables
```
users              → All accounts (landlords + tenants)
buildings          → Groups of units (e.g. "Ocean View Apartments")
properties         → Individual rental units (Apt 101, Studio, etc.)
leases             → Rental contracts between landlord & tenant
invitations        → Email invites landlords send to tenants
invoices           → Monthly rent bills sent to tenants
transactions       → Actual payments made by tenants
expenses           → Costs a landlord tracks (repairs, tax, etc.)
payment_methods    → Tenant's saved card/bank details
```

### Django's Internal Tables (you don't touch these)
```
auth_group, auth_permission                → Django's permission system
django_migrations                          → Tracks which DB changes have run
django_session                             → Stores login session data
django_admin_log                           → Admin panel activity log
django_celery_beat_*                       → Scheduled task schedules
django_celery_results_*                    → Background task results
django_content_type                        → Internal model registry
```

---

## 📋 TABLE 1: `users` — 4 Rows Currently

**What it stores:** Every person who has an account — both landlords and tenants live in this one table. The `role` column tells them apart.

| Column | Data Type | Required? | What It Stores |
|--------|-----------|-----------|----------------|
| `id` | INTEGER | ✅ PK | Auto-generated unique number (1, 2, 3…) |
| `email` | varchar(254) | ✅ UNIQUE | Login identifier — must be unique |
| `password` | varchar(128) | ✅ | Hashed password (bcrypt — never plain text) |
| `role` | varchar(20) | ✅ | `'landlord'` or `'tenant'` only |
| `first_name` | varchar(100) | ✅ | User's first name |
| `last_name` | varchar(100) | ✅ | User's last name |
| `phone_number` | varchar(30) | ✅ | Phone (can be blank string `''`) |
| `is_verified` | bool | ✅ | `True` = email verified → can log in |
| `is_active` | bool | ✅ | `False` = soft-deleted / banned |
| `is_staff` | bool | ✅ | `True` = can access Django Admin panel |
| `is_superuser` | bool | ✅ | `True` = full Django admin powers |
| `last_login` | datetime | ❌ | Timestamp of last login (NULL if never) |
| `created_at` | datetime | ✅ | Account creation timestamp |
| `updated_at` | datetime | ✅ | Last profile update timestamp |
| `deleted_at` | datetime | ❌ | NULL = active; set = soft-deleted |

### 📊 Actual Live Data (4 rows / 4 tuples)

```
id | email                  | role     | first_name | last_name | is_verified | is_staff
---+------------------------+----------+------------+-----------+-------------+---------
1  | kojocbentum@gmail.com  | landlord | Caleb      | Bentum    | True ✅      | False
2  | goodben@gmail.com      | tenant   | Caleb      | Bentum    | False ⛔     | False
3  | landlord@test.com      | landlord | Test       | Landlord  | True ✅      | False
4  | tenant@test.com        | tenant   | Test       | Tenant    | True ✅      | False
```

> 🔍 Notice: User `id=2` (`goodben@gmail.com`) has `is_verified = False` — this person **cannot log in** until they verify their email.

---

## 📋 TABLE 2: `buildings` — 1 Row Currently

**What it stores:** A "parent group" for properties. One building can contain many units.

| Column | Data Type | Required? | What It Stores |
|--------|-----------|-----------|----------------|
| `id` | INTEGER | ✅ PK | Unique building ID |
| `name` | varchar(255) | ✅ | e.g. "Ocean View Apartments" |
| `address` | TEXT | ✅ | Full street address |
| `description` | TEXT | ❌ | Optional description |
| `landlord_id` | bigint | ✅ **FK** | → Points to `users.id` (who owns it) |
| `created_at` | datetime | ✅ | When record was created |
| `updated_at` | datetime | ✅ | Last update timestamp |

### 📊 Actual Live Data (1 row)

```
id | name                      | address               | landlord_id
---+---------------------------+-----------------------+------------
1  | Ocean View Apartments     | 123 Beachfront Way    | 1  (= Caleb Bentum)
```

---

## 📋 TABLE 3: `properties` — 3 Rows Currently

**What it stores:** Individual rental units. Can belong to a building or be standalone.

| Column | Data Type | Required? | What It Stores |
|--------|-----------|-----------|----------------|
| `id` | INTEGER | ✅ PK | Unique unit ID |
| `unit_number` | varchar(50) | ✅ | e.g. "Apt 101", "Studio A" |
| `property_type` | varchar(20) | ✅ | `apartment`, `house`, `office`, `studio` |
| `rent_amount` | decimal | ✅ | Monthly rent in dollars |
| `status` | varchar(20) | ✅ | `available`, `occupied`, `maintenance` |
| `description` | TEXT | ❌ | Optional unit description |
| `building_id` | bigint | ❌ **FK** | → `buildings.id` (NULL if standalone) |
| `landlord_id` | bigint | ✅ **FK** | → `users.id` (the owner) |
| `created_at` | datetime | ✅ | Creation timestamp |
| `updated_at` | datetime | ✅ | Last update timestamp |

### 📊 Actual Live Data (3 rows)

```
id | unit_number      | type      | rent    | status    | building_id | landlord_id
---+------------------+-----------+---------+-----------+-------------+------------
1  | Apt 101          | apartment | $1500   | occupied  | 1           | 1
2  | Apt 102          | apartment | $1200   | available | 1           | 1
3  | Downtown Studio  | studio    | $800    | available | NULL        | 1
```

> 🔍 Apt 101 and Apt 102 belong to building `id=1` (Ocean View Apartments).
> Downtown Studio has `building_id = NULL` — it's a standalone unit with no parent building.

---

## 📋 TABLE 4: `leases` — 0 Rows (empty)

**What it stores:** The rental contract — who rents what unit, for how long, at what price.

| Column | Data Type | Required? | What It Stores |
|--------|-----------|-----------|----------------|
| `id` | INTEGER | ✅ PK | Unique lease ID |
| `start_date` | date | ✅ | When lease begins |
| `end_date` | date | ✅ | When lease expires |
| `monthly_rent` | decimal | ✅ | Agreed rent amount |
| `status` | varchar(20) | ✅ | `active`, `pending`, `terminated`, `expired` |
| `contract_pdf` | — | ❌ | File path to the PDF contract |
| `signed_at` | datetime | ❌ | When tenant signed (NULL = not signed yet) |
| `deleted_at` | datetime | ❌ | Soft delete timestamp |
| `landlord_id` | bigint | ✅ **FK** | → `users.id` (the landlord) |
| `tenant_id` | bigint | ❌ **FK** | → `users.id` (the tenant — NULL until invited) |
| `property_id` | bigint | ✅ **FK** | → `properties.id` (which unit) |
| `created_at` | datetime | ✅ | When lease was created |
| `updated_at` | datetime | ✅ | Last update |

---

## 📋 TABLE 5: `invitations` — 0 Rows (empty)

**What it stores:** When a landlord invites a tenant by email to join a lease. The tenant gets a link with a secret `token_hash` to accept.

| Column | Data Type | Required? | What It Stores |
|--------|-----------|-----------|----------------|
| `id` | INTEGER | ✅ PK | Unique invitation ID |
| `email` | varchar(254) | ✅ | Tenant's email address |
| `token_hash` | varchar(255) | ✅ | Hashed secret token (sent in email link) |
| `expires_at` | datetime | ✅ | Link expiry time |
| `accepted_at` | datetime | ❌ | When tenant clicked the link (NULL = not yet) |
| `landlord_id` | bigint | ✅ **FK** | → `users.id` |
| `lease_id` | bigint | ✅ **FK** | → `leases.id` (which lease they're invited to) |
| `created_at` | datetime | ✅ | When invite was sent |

---

## 📋 TABLE 6: `invoices` — 0 Rows (empty)

**What it stores:** Monthly rent bills. The landlord generates one invoice per month per tenant.

| Column | Data Type | Required? | What It Stores |
|--------|-----------|-----------|----------------|
| `id` | INTEGER | ✅ PK | Unique invoice ID |
| `base_rent` | decimal | ✅ | Base rent amount |
| `late_fee_amount` | decimal | ✅ | Late fee charged (0.00 if none) |
| `total_amount` | decimal | ✅ | `base_rent + late_fee_amount` |
| `due_date` | date | ✅ | Payment deadline |
| `status` | varchar(20) | ✅ | `unpaid`, `partial`, `paid`, `overdue` |
| `late_fee_applied` | bool | ✅ | Whether a late fee was added |
| `paid_at` | datetime | ❌ | When fully paid (NULL = not paid yet) |
| `landlord_id` | bigint | ✅ **FK** | → `users.id` |
| `tenant_id` | bigint | ✅ **FK** | → `users.id` |
| `lease_id` | bigint | ✅ **FK** | → `leases.id` |
| `property_id` | bigint | ✅ **FK** | → `properties.id` |
| `created_at` | datetime | ✅ | Creation timestamp |
| `updated_at` | datetime | ✅ | Last update |

---

## 📋 TABLE 7: `transactions` — 0 Rows (empty)

**What it stores:** Every payment a tenant makes. One invoice can have multiple partial transactions.

| Column | Data Type | Required? | What It Stores |
|--------|-----------|-----------|----------------|
| `id` | INTEGER | ✅ PK | Unique transaction ID |
| `amount` | decimal | ✅ | How much was paid |
| `gateway_reference` | varchar(255) | ✅ | Stripe/Paystack payment ID |
| `payment_method_last4` | varchar(4) | ✅ | Last 4 digits of card used |
| `idempotency_key` | varchar(255) | ✅ UNIQUE | Prevents duplicate charges |
| `invoice_id` | bigint | ✅ **FK** | → `invoices.id` |
| `tenant_id` | bigint | ✅ **FK** | → `users.id` |
| `landlord_id` | bigint | ✅ **FK** | → `users.id` |
| `created_at` | datetime | ✅ | When payment was processed |

---

## 📋 TABLE 8: `expenses` — 0 Rows (empty)

**What it stores:** Landlord's operating costs — repairs, insurance, tax, etc. Used for ROI tracking.

| Column | Data Type | Required? | What It Stores |
|--------|-----------|-----------|----------------|
| `id` | INTEGER | ✅ PK | Unique expense ID |
| `category` | varchar(20) | ✅ | `maintenance`, `repair`, `utility`, `tax`, `insurance`, `other` |
| `description` | TEXT | ✅ | What the expense was for |
| `amount` | decimal | ✅ | Cost in dollars |
| `expense_date` | date | ✅ | When it was paid |
| `landlord_id` | bigint | ✅ **FK** | → `users.id` |
| `property_id` | bigint | ✅ **FK** | → `properties.id` |
| `created_at` | datetime | ✅ | Record creation timestamp |

---

## 📋 TABLE 9: `payment_methods` — 0 Rows (empty)

**What it stores:** A tenant's saved payment cards. The actual card number is NEVER stored — only the last 4 digits and a token from Stripe/Paystack.

| Column | Data Type | Required? | What It Stores |
|--------|-----------|-----------|----------------|
| `id` | INTEGER | ✅ PK | Unique method ID |
| `gateway_token` | varchar(255) | ✅ | Stripe's `pm_xxxxx` token |
| `last4` | varchar(4) | ✅ | e.g. `"4242"` |
| `card_brand` | varchar(20) | ✅ | `"Visa"`, `"Mastercard"`, etc. |
| `expiry_month` | INTEGER | ✅ | e.g. `12` |
| `expiry_year` | INTEGER | ✅ | e.g. `2027` |
| `is_default` | bool | ✅ | `True` = use this card by default |
| `is_active` | bool | ✅ | `False` = card was deleted |
| `tenant_id` | bigint | ✅ **FK** | → `users.id` |
| `created_at` | datetime | ✅ | When card was saved |

---

## 🔗 HOW THE TABLES LINK TOGETHER (Relationships / Foreign Keys)

```
users (id)
  │
  ├── [as landlord] ──────────────────────────────────────────────────┐
  │                                                                    │
  │   ┌── buildings (landlord_id → users.id)                          │
  │   │       └── properties (building_id → buildings.id)            │
  │   │                   ↑                                           │
  │   └── properties (landlord_id → users.id) ──────────────────────►│
  │                   │                                               │
  │                   └── leases (property_id → properties.id) ◄─────┤
  │                           │                                       │
  │                   leases (landlord_id → users.id) ───────────────►│
  │                           │                                       │
  │                   invitations (lease_id → leases.id)             │
  │                   invitations (landlord_id → users.id) ─────────►│
  │                           │                                       │
  │                   invoices (lease_id → leases.id)                │
  │                   invoices (property_id → properties.id)         │
  │                   invoices (landlord_id → users.id) ────────────►│
  │                           │                                       │
  │                   transactions (invoice_id → invoices.id)        │
  │                   transactions (landlord_id → users.id) ────────►│
  │                           │                                       │
  │                   expenses (property_id → properties.id)         │
  │                   expenses (landlord_id → users.id) ────────────►│
  │
  └── [as tenant] ──────────────────────────────────────────────────┐
                                                                     │
      leases (tenant_id → users.id) ─────────────────────────────►  │
      invoices (tenant_id → users.id) ────────────────────────────►  │
      transactions (tenant_id → users.id) ────────────────────────►  │
      payment_methods (tenant_id → users.id) ─────────────────────►  │
```

### In Plain English:
- **One landlord → Many buildings** (`buildings.landlord_id`)
- **One building → Many properties** (`properties.building_id`)
- **One landlord → Many properties** (`properties.landlord_id`)
- **One property → Many leases** (over time, different tenants)
- **One lease → One tenant + One landlord + One property**
- **One lease → Many invoices** (one per month)
- **One invoice → Many transactions** (partial payments)
- **One tenant → Many payment methods** (multiple cards)
- **One landlord → Many expenses** (per property)

---

## 📏 CURRENT DATABASE SIZE SUMMARY

| Table | Rows (Tuples) | Columns | Has Data? |
|-------|--------------|---------|-----------|
| `users` | **4** | 15 | ✅ Yes |
| `buildings` | **1** | 7 | ✅ Yes |
| `properties` | **3** | 10 | ✅ Yes |
| `leases` | 0 | 12 | ❌ Empty |
| `invitations` | 0 | 8 | ❌ Empty |
| `invoices` | 0 | 14 | ❌ Empty |
| `transactions` | 0 | 9 | ❌ Empty |
| `expenses` | 0 | 8 | ❌ Empty |
| `payment_methods` | 0 | 10 | ❌ Empty |

> The empty tables are expected — leases haven't been created yet (that's Phase 3 of the roadmap).
> Once you create leases, invoices and transactions will auto-populate through the app.

---

## 🧠 Quick Mental Model

Think of your database like this physical office:

```
🗄️ Filing Cabinet = the database (db.sqlite3)

   📁 Folder "users"        = spreadsheet with 4 people (rows)
   📁 Folder "buildings"    = spreadsheet with 1 building (row)
   📁 Folder "properties"   = spreadsheet with 3 units (rows)
   📁 Folder "leases"       = spreadsheet, currently empty
   📁 Folder "invoices"     = spreadsheet, currently empty
   ...etc.

Each folder has columns (headers at the top of the spreadsheet):
   users: [id | email | role | first_name | last_name | ...]
   
Each row is one complete record:
   [1 | kojocbentum@gmail.com | landlord | Caleb | Bentum | ...]
   [2 | goodben@gmail.com     | tenant   | Caleb | Bentum | ...]
```
