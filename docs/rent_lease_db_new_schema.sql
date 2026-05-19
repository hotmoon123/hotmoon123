-- New Rent & Lease Management Database Schema
-- Two-Table Architecture (No MTI)
-- Generated: 2026-05-20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

SET NAMES utf8mb4;

-- =====================================================================
-- BLOCK 1: USER TABLES (Independent, No MTI)
-- =====================================================================

CREATE TABLE `landlord_accounts` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `password` varchar(255) NOT NULL,
  `last_login` datetime(6) NULL,
  `email` varchar(255) NOT NULL UNIQUE,
  `first_name` varchar(150) NOT NULL DEFAULT '',
  `last_name` varchar(150) NOT NULL DEFAULT '',
  `phone_number` varchar(30) NOT NULL DEFAULT '',
  `company_name` varchar(255) NOT NULL DEFAULT '',
  `business_reg_no` varchar(100) NOT NULL DEFAULT '',
  `tax_id` varchar(100) NOT NULL DEFAULT '',
  `address` varchar(500) NOT NULL DEFAULT '',
  `city` varchar(100) NOT NULL DEFAULT '',
  `state` varchar(100) NOT NULL DEFAULT '',
  `country` varchar(100) NOT NULL DEFAULT '',
  `postal_code` varchar(20) NOT NULL DEFAULT '',
  `profile_photo` varchar(255) NULL,
  `bio` longtext NOT NULL DEFAULT '',
  `bank_name` varchar(255) NOT NULL DEFAULT '',
  `bank_account_no` varchar(100) NOT NULL DEFAULT '',
  `bank_routing_no` varchar(100) NOT NULL DEFAULT '',
  `is_verified` tinyint(1) NOT NULL DEFAULT 0,
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `is_staff` tinyint(1) NOT NULL DEFAULT 0,
  `is_superuser` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `tenant_accounts` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `password` varchar(255) NOT NULL,
  `last_login` datetime(6) NULL,
  `email` varchar(255) NOT NULL UNIQUE,
  `first_name` varchar(150) NOT NULL DEFAULT '',
  `last_name` varchar(150) NOT NULL DEFAULT '',
  `phone_number` varchar(30) NOT NULL DEFAULT '',
  `date_of_birth` date NULL,
  `national_id_number` varchar(100) NOT NULL DEFAULT '',
  `id_document` varchar(255) NULL,
  `employer_name` varchar(255) NOT NULL DEFAULT '',
  `monthly_income` decimal(12,2) NULL,
  `emergency_contact_name` varchar(255) NOT NULL DEFAULT '',
  `emergency_contact_phone` varchar(30) NOT NULL DEFAULT '',
  `emergency_contact_relation` varchar(100) NOT NULL DEFAULT '',
  `profile_photo` varchar(255) NULL,
  `previous_address` varchar(500) NOT NULL DEFAULT '',
  `previous_landlord_name` varchar(255) NOT NULL DEFAULT '',
  `previous_landlord_phone` varchar(30) NOT NULL DEFAULT '',
  `is_verified` tinyint(1) NOT NULL DEFAULT 0,
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `is_staff` tinyint(1) NOT NULL DEFAULT 0,
  `is_superuser` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `password_reset_tokens` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `user_type` varchar(10) NOT NULL,
  `user_id` bigint UNSIGNED NOT NULL,
  `token_hash` varchar(255) NOT NULL UNIQUE,
  `expires_at` datetime(6) NOT NULL,
  `used_at` datetime(6) NULL,
  `created_at` datetime(6) NOT NULL,
  KEY `user_type_user_id` (`user_type`, `user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================================
-- BLOCK 2: PROPERTY TABLES
-- =====================================================================

CREATE TABLE `buildings` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` longtext NOT NULL,
  `description` longtext NOT NULL DEFAULT '',
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  CONSTRAINT `buildings_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `properties` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `building_id` bigint UNSIGNED NULL,
  `unit_number` varchar(50) NOT NULL,
  `address` longtext NOT NULL DEFAULT '',
  `property_type` varchar(20) NOT NULL DEFAULT 'apartment',
  `rent_amount` decimal(12,2) NOT NULL DEFAULT 0.00,
  `status` varchar(20) NOT NULL DEFAULT 'available',
  `description` longtext NOT NULL DEFAULT '',
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  KEY `status` (`status`),
  KEY `building_id` (`building_id`),
  CONSTRAINT `properties_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `properties_building_fk` FOREIGN KEY (`building_id`)
    REFERENCES `buildings` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================================
-- BLOCK 3: LEASE TABLES
-- =====================================================================

CREATE TABLE `leases` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `tenant_id` bigint UNSIGNED NULL,
  `property_id` bigint UNSIGNED NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `rent_amount` decimal(12,2) NOT NULL,
  `deposit_amount` decimal(12,2) NOT NULL DEFAULT 0.00,
  `status` varchar(20) NOT NULL DEFAULT 'pending',
  `contract_pdf` varchar(255) NULL,
  `signed_at` datetime(6) NULL,
  `deleted_at` datetime(6) NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  KEY `tenant_id` (`tenant_id`),
  KEY `property_id` (`property_id`),
  KEY `status` (`status`),
  KEY `deleted_at` (`deleted_at`),
  KEY `end_date` (`end_date`),
  CONSTRAINT `leases_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `leases_tenant_fk` FOREIGN KEY (`tenant_id`)
    REFERENCES `tenant_accounts` (`id`) ON DELETE SET NULL,
  CONSTRAINT `leases_property_fk` FOREIGN KEY (`property_id`)
    REFERENCES `properties` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `invitations` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `lease_id` bigint UNSIGNED NOT NULL,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `email` varchar(255) NOT NULL,
  `token_hash` varchar(255) NOT NULL,
  `expires_at` datetime(6) NOT NULL,
  `accepted_at` datetime(6) NULL,
  `created_at` datetime(6) NOT NULL,
  KEY `token_hash` (`token_hash`),
  KEY `email` (`email`),
  KEY `lease_id` (`lease_id`),
  CONSTRAINT `invitations_lease_fk` FOREIGN KEY (`lease_id`)
    REFERENCES `leases` (`id`) ON DELETE CASCADE,
  CONSTRAINT `invitations_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================================
-- BLOCK 4: FINANCIAL TABLES
-- =====================================================================

CREATE TABLE `invoices` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `tenant_id` bigint UNSIGNED NOT NULL,
  `lease_id` bigint UNSIGNED NOT NULL,
  `rental_property_id` bigint UNSIGNED NULL,
  `amount` decimal(12,2) NOT NULL DEFAULT 0.00,
  `amount_paid` decimal(12,2) NOT NULL DEFAULT 0.00,
  `due_date` date NOT NULL,
  `paid_at` datetime(6) NULL,
  `invoice_type` varchar(20) NOT NULL DEFAULT 'rent',
  `status` varchar(20) NOT NULL DEFAULT 'unpaid',
  `description` varchar(255) NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  KEY `tenant_id` (`tenant_id`),
  KEY `status` (`status`),
  KEY `due_date` (`due_date`),
  KEY `paid_at` (`paid_at`),
  KEY `lease_id` (`lease_id`),
  KEY `rental_property_id` (`rental_property_id`),
  CONSTRAINT `invoices_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `invoices_tenant_fk` FOREIGN KEY (`tenant_id`)
    REFERENCES `tenant_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `invoices_lease_fk` FOREIGN KEY (`lease_id`)
    REFERENCES `leases` (`id`) ON DELETE CASCADE,
  CONSTRAINT `invoices_property_fk` FOREIGN KEY (`rental_property_id`)
    REFERENCES `properties` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `transactions` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `invoice_id` bigint UNSIGNED NOT NULL,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `tenant_id` bigint UNSIGNED NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `gateway_reference` varchar(255) NOT NULL DEFAULT '',
  `idempotency_key` varchar(255) NOT NULL UNIQUE,
  `created_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  KEY `tenant_id` (`tenant_id`),
  KEY `invoice_id` (`invoice_id`),
  CONSTRAINT `transactions_invoice_fk` FOREIGN KEY (`invoice_id`)
    REFERENCES `invoices` (`id`) ON DELETE CASCADE,
  CONSTRAINT `transactions_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `transactions_tenant_fk` FOREIGN KEY (`tenant_id`)
    REFERENCES `tenant_accounts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `expenses` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `rental_property_id` bigint UNSIGNED NULL,
  `category` varchar(100) NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `description` longtext NOT NULL,
  `expense_date` date NOT NULL,
  `receipt` varchar(255) NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  KEY `expense_date` (`expense_date`),
  KEY `category` (`category`),
  CONSTRAINT `expenses_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `expenses_property_fk` FOREIGN KEY (`rental_property_id`)
    REFERENCES `properties` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `payment_methods` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `tenant_id` bigint UNSIGNED NOT NULL,
  `method_type` varchar(20) NOT NULL DEFAULT 'card',
  `provider` varchar(100) NOT NULL DEFAULT 'stripe',
  `last_four` varchar(4) NOT NULL DEFAULT '0000',
  `exp_month` int NULL,
  `exp_year` int NULL,
  `is_default` tinyint(1) NOT NULL DEFAULT 0,
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `gateway_customer_id` varchar(255) NOT NULL DEFAULT '',
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  KEY `tenant_id` (`tenant_id`),
  CONSTRAINT `payment_methods_tenant_fk` FOREIGN KEY (`tenant_id`)
    REFERENCES `tenant_accounts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================================
-- BLOCK 5: MAINTENANCE TABLE
-- =====================================================================

CREATE TABLE `maintenance_tickets` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `tenant_id` bigint UNSIGNED NULL,
  `property_id` bigint UNSIGNED NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `priority` varchar(15) NOT NULL DEFAULT 'medium',
  `status` varchar(20) NOT NULL DEFAULT 'todo',
  `photo` varchar(255) NULL,
  `estimated_cost` decimal(12,2) NOT NULL DEFAULT 0.00,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  KEY `tenant_id` (`tenant_id`),
  KEY `status` (`status`),
  KEY `priority` (`priority`),
  CONSTRAINT `maintenance_tickets_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `maintenance_tickets_tenant_fk` FOREIGN KEY (`tenant_id`)
    REFERENCES `tenant_accounts` (`id`) ON DELETE SET NULL,
  CONSTRAINT `maintenance_tickets_property_fk` FOREIGN KEY (`property_id`)
    REFERENCES `properties` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================================
-- BLOCK 6: NOTIFICATION & ACTIVITY TABLES
-- =====================================================================

CREATE TABLE `notifications` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `recipient_type` varchar(10) NOT NULL,
  `landlord_id` bigint UNSIGNED NULL,
  `tenant_id` bigint UNSIGNED NULL,
  `type` varchar(50) NOT NULL,
  `title` varchar(255) NOT NULL,
  `message` longtext NOT NULL DEFAULT '',
  `is_read` tinyint(1) NOT NULL DEFAULT 0,
  `related_url` varchar(500) NOT NULL DEFAULT '',
  `created_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  KEY `tenant_id` (`tenant_id`),
  KEY `is_read` (`is_read`),
  KEY `created_at` (`created_at`),
  CONSTRAINT `notifications_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `notifications_tenant_fk` FOREIGN KEY (`tenant_id`)
    REFERENCES `tenant_accounts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `activity_log` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `actor_type` varchar(10) NOT NULL,
  `landlord_id` bigint UNSIGNED NULL,
  `tenant_id` bigint UNSIGNED NULL,
  `action` varchar(100) NOT NULL,
  `description` longtext NOT NULL DEFAULT '',
  `related_table` varchar(100) NOT NULL DEFAULT '',
  `related_id` bigint UNSIGNED NULL,
  `created_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  KEY `created_at` (`created_at`),
  KEY `action` (`action`),
  CONSTRAINT `activity_log_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `activity_log_tenant_fk` FOREIGN KEY (`tenant_id`)
    REFERENCES `tenant_accounts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================================
-- BLOCK 7: DOCUMENT TABLE
-- =====================================================================

CREATE TABLE `documents` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `tenant_id` bigint UNSIGNED NULL,
  `lease_id` bigint UNSIGNED NULL,
  `property_id` bigint UNSIGNED NULL,
  `title` varchar(255) NOT NULL,
  `file_path` varchar(500) NOT NULL,
  `file_type` varchar(50) NOT NULL DEFAULT '',
  `file_size` int UNSIGNED NOT NULL DEFAULT 0,
  `uploaded_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  KEY `lease_id` (`lease_id`),
  CONSTRAINT `documents_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `documents_tenant_fk` FOREIGN KEY (`tenant_id`)
    REFERENCES `tenant_accounts` (`id`) ON DELETE SET NULL,
  CONSTRAINT `documents_lease_fk` FOREIGN KEY (`lease_id`)
    REFERENCES `leases` (`id`) ON DELETE SET NULL,
  CONSTRAINT `documents_property_fk` FOREIGN KEY (`property_id`)
    REFERENCES `properties` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================================
-- BLOCK 8: CHAT TABLE
-- =====================================================================

CREATE TABLE `messages` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `tenant_id` bigint UNSIGNED NOT NULL,
  `sender_type` varchar(10) NOT NULL,
  `body` longtext NOT NULL,
  `is_read` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  KEY `tenant_id` (`tenant_id`),
  KEY `created_at` (`created_at`),
  KEY `is_read` (`is_read`),
  CONSTRAINT `messages_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `messages_tenant_fk` FOREIGN KEY (`tenant_id`)
    REFERENCES `tenant_accounts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================================
-- BLOCK 9: NOTICE BOARD TABLE
-- =====================================================================

CREATE TABLE `notices` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `title` varchar(255) NOT NULL,
  `body` longtext NOT NULL,
  `is_pinned` tinyint(1) NOT NULL DEFAULT 0,
  `expires_at` datetime(6) NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  KEY `is_pinned` (`is_pinned`),
  KEY `expires_at` (`expires_at`),
  CONSTRAINT `notices_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================================
-- BLOCK 10: INSPECTION TABLE
-- =====================================================================

CREATE TABLE `inspections` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `lease_id` bigint UNSIGNED NOT NULL,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `tenant_id` bigint UNSIGNED NOT NULL,
  `property_id` bigint UNSIGNED NOT NULL,
  `type` varchar(20) NOT NULL,
  `condition` varchar(20) NOT NULL DEFAULT 'good',
  `notes` longtext NOT NULL DEFAULT '',
  `photos` longtext NOT NULL DEFAULT '',
  `conducted_at` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  KEY `lease_id` (`lease_id`),
  KEY `landlord_id` (`landlord_id`),
  CONSTRAINT `inspections_lease_fk` FOREIGN KEY (`lease_id`)
    REFERENCES `leases` (`id`) ON DELETE CASCADE,
  CONSTRAINT `inspections_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `inspections_tenant_fk` FOREIGN KEY (`tenant_id`)
    REFERENCES `tenant_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `inspections_property_fk` FOREIGN KEY (`property_id`)
    REFERENCES `properties` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================================
-- BLOCK 11: COMPLIANCE TABLE
-- =====================================================================

CREATE TABLE `compliance_documents` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL DEFAULT '',
  `file_path` varchar(500) NOT NULL,
  `category` varchar(100) NOT NULL DEFAULT '',
  `is_mandatory` tinyint(1) NOT NULL DEFAULT 0,
  `valid_until` date NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  KEY `category` (`category`),
  CONSTRAINT `compliance_documents_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================================
-- BLOCK 12: AUTOMATION TABLE
-- =====================================================================

CREATE TABLE `automation_rules` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `trigger_event` varchar(100) NOT NULL,
  `action` varchar(100) NOT NULL,
  `conditions` longtext NOT NULL DEFAULT '',
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `last_run_at` datetime(6) NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  KEY `landlord_id` (`landlord_id`),
  KEY `is_active` (`is_active`),
  CONSTRAINT `automation_rules_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================================
-- DJANGO PERMISSION TABLES (Landlord model only — AUTH_USER_MODEL)
-- =====================================================================

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` varchar(150) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `landlord_accounts_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `group_id` int(11) NOT NULL,
  UNIQUE KEY `unique_landlord_group` (`landlord_id`, `group_id`),
  CONSTRAINT `landlord_accounts_groups_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `landlord_accounts_groups_group_fk` FOREIGN KEY (`group_id`)
    REFERENCES `auth_group` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `landlord_accounts_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `landlord_id` bigint UNSIGNED NOT NULL,
  `permission_id` int(11) NOT NULL,
  UNIQUE KEY `unique_landlord_perm` (`landlord_id`, `permission_id`),
  CONSTRAINT `landlord_accounts_user_permissions_landlord_fk` FOREIGN KEY (`landlord_id`)
    REFERENCES `landlord_accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `landlord_accounts_user_permissions_perm_fk` FOREIGN KEY (`permission_id`)
    REFERENCES `auth_permission` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

COMMIT;
