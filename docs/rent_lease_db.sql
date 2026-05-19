-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 13, 2026 at 04:08 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rent_lease_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add crontab', 6, 'add_crontabschedule'),
(22, 'Can change crontab', 6, 'change_crontabschedule'),
(23, 'Can delete crontab', 6, 'delete_crontabschedule'),
(24, 'Can view crontab', 6, 'view_crontabschedule'),
(25, 'Can add interval', 7, 'add_intervalschedule'),
(26, 'Can change interval', 7, 'change_intervalschedule'),
(27, 'Can delete interval', 7, 'delete_intervalschedule'),
(28, 'Can view interval', 7, 'view_intervalschedule'),
(29, 'Can add periodic task', 8, 'add_periodictask'),
(30, 'Can change periodic task', 8, 'change_periodictask'),
(31, 'Can delete periodic task', 8, 'delete_periodictask'),
(32, 'Can view periodic task', 8, 'view_periodictask'),
(33, 'Can add periodic task track', 9, 'add_periodictasks'),
(34, 'Can change periodic task track', 9, 'change_periodictasks'),
(35, 'Can delete periodic task track', 9, 'delete_periodictasks'),
(36, 'Can view periodic task track', 9, 'view_periodictasks'),
(37, 'Can add solar event', 10, 'add_solarschedule'),
(38, 'Can change solar event', 10, 'change_solarschedule'),
(39, 'Can delete solar event', 10, 'delete_solarschedule'),
(40, 'Can view solar event', 10, 'view_solarschedule'),
(41, 'Can add clocked', 11, 'add_clockedschedule'),
(42, 'Can change clocked', 11, 'change_clockedschedule'),
(43, 'Can delete clocked', 11, 'delete_clockedschedule'),
(44, 'Can view clocked', 11, 'view_clockedschedule'),
(45, 'Can add task result', 12, 'add_taskresult'),
(46, 'Can change task result', 12, 'change_taskresult'),
(47, 'Can delete task result', 12, 'delete_taskresult'),
(48, 'Can view task result', 12, 'view_taskresult'),
(49, 'Can add chord counter', 13, 'add_chordcounter'),
(50, 'Can change chord counter', 13, 'change_chordcounter'),
(51, 'Can delete chord counter', 13, 'delete_chordcounter'),
(52, 'Can view chord counter', 13, 'view_chordcounter'),
(53, 'Can add group result', 14, 'add_groupresult'),
(54, 'Can change group result', 14, 'change_groupresult'),
(55, 'Can delete group result', 14, 'delete_groupresult'),
(56, 'Can view group result', 14, 'view_groupresult'),
(57, 'Can add custom user', 15, 'add_customuser'),
(58, 'Can change custom user', 15, 'change_customuser'),
(59, 'Can delete custom user', 15, 'delete_customuser'),
(60, 'Can view custom user', 15, 'view_customuser'),
(61, 'Can add landlord profile', 16, 'add_landlordprofile'),
(62, 'Can change landlord profile', 16, 'change_landlordprofile'),
(63, 'Can delete landlord profile', 16, 'delete_landlordprofile'),
(64, 'Can view landlord profile', 16, 'view_landlordprofile'),
(65, 'Can add tenant profile', 17, 'add_tenantprofile'),
(66, 'Can change tenant profile', 17, 'change_tenantprofile'),
(67, 'Can delete tenant profile', 17, 'delete_tenantprofile'),
(68, 'Can view tenant profile', 17, 'view_tenantprofile'),
(69, 'Can add building', 18, 'add_building'),
(70, 'Can change building', 18, 'change_building'),
(71, 'Can delete building', 18, 'delete_building'),
(72, 'Can view building', 18, 'view_building'),
(73, 'Can add property', 19, 'add_property'),
(74, 'Can change property', 19, 'change_property'),
(75, 'Can delete property', 19, 'delete_property'),
(76, 'Can view property', 19, 'view_property'),
(77, 'Can add lease', 20, 'add_lease'),
(78, 'Can change lease', 20, 'change_lease'),
(79, 'Can delete lease', 20, 'delete_lease'),
(80, 'Can view lease', 20, 'view_lease'),
(81, 'Can add invitation', 21, 'add_invitation'),
(82, 'Can change invitation', 21, 'change_invitation'),
(83, 'Can delete invitation', 21, 'delete_invitation'),
(84, 'Can view invitation', 21, 'view_invitation'),
(85, 'Can add invoice', 22, 'add_invoice'),
(86, 'Can change invoice', 22, 'change_invoice'),
(87, 'Can delete invoice', 22, 'delete_invoice'),
(88, 'Can view invoice', 22, 'view_invoice'),
(89, 'Can add payment method', 23, 'add_paymentmethod'),
(90, 'Can change payment method', 23, 'change_paymentmethod'),
(91, 'Can delete payment method', 23, 'delete_paymentmethod'),
(92, 'Can view payment method', 23, 'view_paymentmethod'),
(93, 'Can add transaction', 24, 'add_transaction'),
(94, 'Can change transaction', 24, 'change_transaction'),
(95, 'Can delete transaction', 24, 'delete_transaction'),
(96, 'Can view transaction', 24, 'view_transaction'),
(97, 'Can add expense', 25, 'add_expense'),
(98, 'Can change expense', 25, 'change_expense'),
(99, 'Can delete expense', 25, 'delete_expense'),
(100, 'Can view expense', 25, 'view_expense'),
(101, 'Can add maintenance ticket', 26, 'add_maintenanceticket'),
(102, 'Can change maintenance ticket', 26, 'change_maintenanceticket'),
(103, 'Can delete maintenance ticket', 26, 'delete_maintenanceticket'),
(104, 'Can view maintenance ticket', 26, 'view_maintenanceticket'),
(105, 'Can add landlord', 27, 'add_landlord'),
(106, 'Can change landlord', 27, 'change_landlord'),
(107, 'Can delete landlord', 27, 'delete_landlord'),
(108, 'Can view landlord', 27, 'view_landlord'),
(109, 'Can add tenant', 28, 'add_tenant'),
(110, 'Can change tenant', 28, 'change_tenant'),
(111, 'Can delete tenant', 28, 'delete_tenant'),
(112, 'Can view tenant', 28, 'view_tenant');

-- --------------------------------------------------------

--
-- Table structure for table `buildings`
--

CREATE TABLE `buildings` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `landlord_id` bigint(20) NOT NULL,
  `description` longtext DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_beat_clockedschedule`
--

CREATE TABLE `django_celery_beat_clockedschedule` (
  `id` int(11) NOT NULL,
  `clocked_time` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_beat_crontabschedule`
--

CREATE TABLE `django_celery_beat_crontabschedule` (
  `id` int(11) NOT NULL,
  `minute` varchar(240) NOT NULL,
  `hour` varchar(96) NOT NULL,
  `day_of_week` varchar(64) NOT NULL,
  `day_of_month` varchar(124) NOT NULL,
  `month_of_year` varchar(64) NOT NULL,
  `timezone` varchar(63) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_beat_intervalschedule`
--

CREATE TABLE `django_celery_beat_intervalschedule` (
  `id` int(11) NOT NULL,
  `every` int(11) NOT NULL,
  `period` varchar(24) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_beat_periodictask`
--

CREATE TABLE `django_celery_beat_periodictask` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `task` varchar(200) NOT NULL,
  `args` longtext NOT NULL,
  `kwargs` longtext NOT NULL,
  `queue` varchar(200) DEFAULT NULL,
  `exchange` varchar(200) DEFAULT NULL,
  `routing_key` varchar(200) DEFAULT NULL,
  `expires` datetime(6) DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime(6) DEFAULT NULL,
  `total_run_count` int(10) UNSIGNED NOT NULL CHECK (`total_run_count` >= 0),
  `date_changed` datetime(6) NOT NULL,
  `description` longtext NOT NULL,
  `crontab_id` int(11) DEFAULT NULL,
  `interval_id` int(11) DEFAULT NULL,
  `solar_id` int(11) DEFAULT NULL,
  `one_off` tinyint(1) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `priority` int(10) UNSIGNED DEFAULT NULL CHECK (`priority` >= 0),
  `headers` longtext NOT NULL,
  `clocked_id` int(11) DEFAULT NULL,
  `expire_seconds` int(10) UNSIGNED DEFAULT NULL CHECK (`expire_seconds` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_beat_periodictasks`
--

CREATE TABLE `django_celery_beat_periodictasks` (
  `ident` smallint(6) NOT NULL,
  `last_update` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_beat_solarschedule`
--

CREATE TABLE `django_celery_beat_solarschedule` (
  `id` int(11) NOT NULL,
  `event` varchar(24) NOT NULL,
  `latitude` decimal(9,6) NOT NULL,
  `longitude` decimal(9,6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_results_chordcounter`
--

CREATE TABLE `django_celery_results_chordcounter` (
  `id` int(11) NOT NULL,
  `group_id` varchar(255) NOT NULL,
  `sub_tasks` longtext NOT NULL,
  `count` int(10) UNSIGNED NOT NULL CHECK (`count` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_results_groupresult`
--

CREATE TABLE `django_celery_results_groupresult` (
  `id` int(11) NOT NULL,
  `group_id` varchar(255) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `date_done` datetime(6) NOT NULL,
  `content_type` varchar(128) NOT NULL,
  `content_encoding` varchar(64) NOT NULL,
  `result` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_results_taskresult`
--

CREATE TABLE `django_celery_results_taskresult` (
  `id` int(11) NOT NULL,
  `task_id` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `content_type` varchar(128) NOT NULL,
  `content_encoding` varchar(64) NOT NULL,
  `result` longtext DEFAULT NULL,
  `date_done` datetime(6) NOT NULL,
  `traceback` longtext DEFAULT NULL,
  `meta` longtext DEFAULT NULL,
  `task_args` longtext DEFAULT NULL,
  `task_kwargs` longtext DEFAULT NULL,
  `task_name` varchar(255) DEFAULT NULL,
  `worker` varchar(100) DEFAULT NULL,
  `date_created` datetime(6) NOT NULL,
  `periodic_task_name` varchar(255) DEFAULT NULL,
  `date_started` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(11, 'django_celery_beat', 'clockedschedule'),
(6, 'django_celery_beat', 'crontabschedule'),
(7, 'django_celery_beat', 'intervalschedule'),
(8, 'django_celery_beat', 'periodictask'),
(9, 'django_celery_beat', 'periodictasks'),
(10, 'django_celery_beat', 'solarschedule'),
(13, 'django_celery_results', 'chordcounter'),
(14, 'django_celery_results', 'groupresult'),
(12, 'django_celery_results', 'taskresult'),
(25, 'financials', 'expense'),
(22, 'financials', 'invoice'),
(23, 'financials', 'paymentmethod'),
(24, 'financials', 'transaction'),
(21, 'leases', 'invitation'),
(20, 'leases', 'lease'),
(26, 'maintenance', 'maintenanceticket'),
(18, 'properties', 'building'),
(19, 'properties', 'property'),
(5, 'sessions', 'session'),
(15, 'users', 'customuser'),
(27, 'users', 'landlord'),
(16, 'users', 'landlordprofile'),
(28, 'users', 'tenant'),
(17, 'users', 'tenantprofile');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-05-13 01:41:32.564491'),
(2, 'contenttypes', '0002_remove_content_type_name', '2026-05-13 01:41:32.731507'),
(3, 'auth', '0001_initial', '2026-05-13 01:41:33.982564'),
(4, 'auth', '0002_alter_permission_name_max_length', '2026-05-13 01:41:34.302012'),
(5, 'auth', '0003_alter_user_email_max_length', '2026-05-13 01:41:34.322790'),
(6, 'auth', '0004_alter_user_username_opts', '2026-05-13 01:41:34.349055'),
(7, 'auth', '0005_alter_user_last_login_null', '2026-05-13 01:41:34.370717'),
(8, 'auth', '0006_require_contenttypes_0002', '2026-05-13 01:41:34.387598'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2026-05-13 01:41:34.408002'),
(10, 'auth', '0008_alter_user_username_max_length', '2026-05-13 01:41:34.429068'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2026-05-13 01:41:34.458458'),
(12, 'auth', '0010_alter_group_name_max_length', '2026-05-13 01:41:34.512714'),
(13, 'auth', '0011_update_proxy_permissions', '2026-05-13 01:41:34.535623'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2026-05-13 01:41:34.557554'),
(15, 'users', '0001_initial', '2026-05-13 01:41:37.153554'),
(16, 'admin', '0001_initial', '2026-05-13 01:41:37.933859'),
(17, 'admin', '0002_logentry_remove_auto_add', '2026-05-13 01:41:37.957831'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2026-05-13 01:41:37.980403'),
(19, 'django_celery_beat', '0001_initial', '2026-05-13 01:41:39.093919'),
(20, 'django_celery_beat', '0002_auto_20161118_0346', '2026-05-13 01:41:40.759984'),
(21, 'django_celery_beat', '0003_auto_20161209_0049', '2026-05-13 01:41:40.876131'),
(22, 'django_celery_beat', '0004_auto_20170221_0000', '2026-05-13 01:41:40.894552'),
(23, 'django_celery_beat', '0005_add_solarschedule_events_choices', '2026-05-13 01:41:40.912934'),
(24, 'django_celery_beat', '0006_auto_20180322_0932', '2026-05-13 01:41:41.115108'),
(25, 'django_celery_beat', '0007_auto_20180521_0826', '2026-05-13 01:41:41.259431'),
(26, 'django_celery_beat', '0008_auto_20180914_1922', '2026-05-13 01:41:41.307545'),
(27, 'django_celery_beat', '0006_auto_20180210_1226', '2026-05-13 01:41:41.348040'),
(28, 'django_celery_beat', '0006_periodictask_priority', '2026-05-13 01:41:41.405776'),
(29, 'django_celery_beat', '0009_periodictask_headers', '2026-05-13 01:41:41.492933'),
(30, 'django_celery_beat', '0010_auto_20190429_0326', '2026-05-13 01:41:41.716066'),
(31, 'django_celery_beat', '0011_auto_20190508_0153', '2026-05-13 01:41:42.261873'),
(32, 'django_celery_beat', '0012_periodictask_expire_seconds', '2026-05-13 01:41:42.322899'),
(33, 'django_celery_beat', '0013_auto_20200609_0727', '2026-05-13 01:41:42.400269'),
(34, 'django_celery_beat', '0014_remove_clockedschedule_enabled', '2026-05-13 01:41:42.472981'),
(35, 'django_celery_beat', '0015_edit_solarschedule_events_choices', '2026-05-13 01:41:42.492089'),
(36, 'django_celery_beat', '0016_alter_crontabschedule_timezone', '2026-05-13 01:41:42.517849'),
(37, 'django_celery_beat', '0017_alter_crontabschedule_month_of_year', '2026-05-13 01:41:42.543568'),
(38, 'django_celery_beat', '0018_improve_crontab_helptext', '2026-05-13 01:41:42.566345'),
(39, 'django_celery_beat', '0019_alter_periodictasks_options', '2026-05-13 01:41:42.585028'),
(40, 'django_celery_results', '0001_initial', '2026-05-13 01:41:43.504958'),
(41, 'django_celery_results', '0002_add_task_name_args_kwargs', '2026-05-13 01:41:43.858911'),
(42, 'django_celery_results', '0003_auto_20181106_1101', '2026-05-13 01:41:43.905880'),
(43, 'django_celery_results', '0004_auto_20190516_0412', '2026-05-13 01:41:44.460505'),
(44, 'django_celery_results', '0005_taskresult_worker', '2026-05-13 01:41:44.604441'),
(45, 'django_celery_results', '0006_taskresult_date_created', '2026-05-13 01:41:44.783270'),
(46, 'django_celery_results', '0007_remove_taskresult_hidden', '2026-05-13 01:41:44.882211'),
(47, 'django_celery_results', '0008_chordcounter', '2026-05-13 01:41:44.993106'),
(48, 'django_celery_results', '0009_groupresult', '2026-05-13 01:41:47.557750'),
(49, 'django_celery_results', '0010_remove_duplicate_indices', '2026-05-13 01:41:47.573856'),
(50, 'django_celery_results', '0011_taskresult_periodic_task_name', '2026-05-13 01:41:47.613487'),
(51, 'django_celery_results', '0012_taskresult_date_started', '2026-05-13 01:41:47.643640'),
(52, 'django_celery_results', '0013_taskresult_django_cele_periodi_1993cf_idx', '2026-05-13 01:41:47.701354'),
(53, 'django_celery_results', '0014_alter_taskresult_status', '2026-05-13 01:41:47.713330'),
(54, 'properties', '0001_initial', '2026-05-13 01:41:48.783855'),
(55, 'properties', '0002_alter_property_options_and_more', '2026-05-13 01:41:49.547930'),
(56, 'properties', '0003_alter_building_description_and_more', '2026-05-13 01:41:49.579994'),
(57, 'leases', '0001_initial', '2026-05-13 01:41:51.384456'),
(58, 'financials', '0001_initial', '2026-05-13 01:41:55.940412'),
(59, 'financials', '0002_remove_expense_idx_expenses_property_and_more', '2026-05-13 01:42:05.425979'),
(60, 'leases', '0002_remove_invitation_idx_invitations_token_and_more', '2026-05-13 01:42:07.816700'),
(61, 'maintenance', '0001_initial', '2026-05-13 01:42:08.471922'),
(62, 'sessions', '0001_initial', '2026-05-13 01:42:08.644976'),
(63, 'users', '0002_landlordprofile_tenantprofile', '2026-05-13 01:42:09.161450'),
(64, 'users', '0003_landlord_tenant_mti', '2026-05-13 02:00:14.822407');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `expenses`
--

CREATE TABLE `expenses` (
  `id` bigint(20) NOT NULL,
  `category` varchar(20) NOT NULL,
  `description` longtext NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `expense_date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `landlord_id` bigint(20) NOT NULL,
  `rental_property_id` bigint(20) DEFAULT NULL,
  `receipt` varchar(100) DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `invitations`
--

CREATE TABLE `invitations` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `token_hash` varchar(255) NOT NULL,
  `expires_at` datetime(6) NOT NULL,
  `accepted_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `landlord_id` bigint(20) NOT NULL,
  `lease_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `invoices`
--

CREATE TABLE `invoices` (
  `id` bigint(20) NOT NULL,
  `due_date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `paid_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `landlord_id` bigint(20) NOT NULL,
  `lease_id` bigint(20) NOT NULL,
  `rental_property_id` bigint(20) DEFAULT NULL,
  `tenant_id` bigint(20) NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `amount_paid` decimal(12,2) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `invoice_type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `landlord_accounts`
--

CREATE TABLE `landlord_accounts` (
  `customuser_ptr_id` bigint(20) NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `business_reg_no` varchar(100) NOT NULL,
  `tax_id` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `postal_code` varchar(20) NOT NULL,
  `profile_photo` varchar(500) NOT NULL,
  `bio` longtext NOT NULL,
  `bank_name` varchar(100) NOT NULL,
  `bank_account_no` varchar(100) NOT NULL,
  `bank_routing_no` varchar(100) NOT NULL,
  `profile_created_at` datetime(6) NOT NULL,
  `profile_updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `leases`
--

CREATE TABLE `leases` (
  `id` bigint(20) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `signed_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `deleted_at` datetime(6) DEFAULT NULL,
  `landlord_id` bigint(20) NOT NULL,
  `tenant_id` bigint(20) DEFAULT NULL,
  `contract_pdf` varchar(100) DEFAULT NULL,
  `deposit_amount` decimal(12,2) NOT NULL,
  `rent_amount` decimal(12,2) NOT NULL,
  `property_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `maintenance_tickets`
--

CREATE TABLE `maintenance_tickets` (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `priority` varchar(15) NOT NULL,
  `status` varchar(20) NOT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `estimated_cost` decimal(12,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `landlord_id` bigint(20) NOT NULL,
  `property_id` bigint(20) NOT NULL,
  `tenant_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `payment_methods`
--

CREATE TABLE `payment_methods` (
  `id` bigint(20) NOT NULL,
  `is_default` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `tenant_id` bigint(20) NOT NULL,
  `exp_month` int(11) DEFAULT NULL,
  `exp_year` int(11) DEFAULT NULL,
  `gateway_customer_id` varchar(255) NOT NULL,
  `last_four` varchar(4) NOT NULL,
  `method_type` varchar(20) NOT NULL,
  `provider` varchar(100) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `properties`
--

CREATE TABLE `properties` (
  `id` bigint(20) NOT NULL,
  `unit_number` varchar(50) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `building_id` bigint(20) DEFAULT NULL,
  `landlord_id` bigint(20) NOT NULL,
  `description` longtext DEFAULT NULL,
  `property_type` varchar(20) NOT NULL,
  `rent_amount` decimal(12,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tenant_accounts`
--

CREATE TABLE `tenant_accounts` (
  `customuser_ptr_id` bigint(20) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `national_id_number` varchar(100) NOT NULL,
  `id_document` varchar(500) NOT NULL,
  `profile_photo` varchar(500) NOT NULL,
  `employer_name` varchar(255) NOT NULL,
  `monthly_income` decimal(10,2) DEFAULT NULL,
  `emergency_contact_name` varchar(100) NOT NULL,
  `emergency_contact_phone` varchar(30) NOT NULL,
  `emergency_contact_relation` varchar(50) NOT NULL,
  `previous_address` longtext NOT NULL,
  `previous_landlord_name` varchar(100) NOT NULL,
  `previous_landlord_phone` varchar(30) NOT NULL,
  `profile_created_at` datetime(6) NOT NULL,
  `profile_updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `tenant_accounts`
--

INSERT INTO `tenant_accounts` (`customuser_ptr_id`, `date_of_birth`, `national_id_number`, `id_document`, `profile_photo`, `employer_name`, `monthly_income`, `emergency_contact_name`, `emergency_contact_phone`, `emergency_contact_relation`, `previous_address`, `previous_landlord_name`, `previous_landlord_phone`, `profile_created_at`, `profile_updated_at`) VALUES
(1, NULL, '', '', '', '', NULL, '', '', '', '', '', '', '2026-05-13 02:05:32.409981', '2026-05-13 02:05:32.410008');

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `id` bigint(20) NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `gateway_reference` varchar(255) NOT NULL,
  `idempotency_key` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `invoice_id` bigint(20) NOT NULL,
  `landlord_id` bigint(20) NOT NULL,
  `tenant_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(254) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `phone_number` varchar(30) NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `deleted_at` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `password`, `last_login`, `is_superuser`, `email`, `first_name`, `last_name`, `phone_number`, `is_verified`, `is_active`, `is_staff`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'bcrypt_sha256$$2b$12$7YWcMcqg6STNZOcTizO25eliWtCjteRn2nHUNiLmENppGk42yrL/2', NULL, 0, 'kofiban@gmail.com', 'Kofi', 'Ban', '', 0, 1, 0, '2026-05-13 02:05:32.399534', '2026-05-13 02:05:32.399571', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users_groups`
--

CREATE TABLE `users_groups` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_user_permissions`
--

CREATE TABLE `users_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `buildings`
--
ALTER TABLE `buildings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `buildings_landlord_id_c3a2efcb` (`landlord_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_users_id` (`user_id`);

--
-- Indexes for table `django_celery_beat_clockedschedule`
--
ALTER TABLE `django_celery_beat_clockedschedule`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_celery_beat_crontabschedule`
--
ALTER TABLE `django_celery_beat_crontabschedule`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_celery_beat_intervalschedule`
--
ALTER TABLE `django_celery_beat_intervalschedule`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_celery_beat_periodictask`
--
ALTER TABLE `django_celery_beat_periodictask`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` (`crontab_id`),
  ADD KEY `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` (`interval_id`),
  ADD KEY `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` (`solar_id`),
  ADD KEY `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` (`clocked_id`);

--
-- Indexes for table `django_celery_beat_periodictasks`
--
ALTER TABLE `django_celery_beat_periodictasks`
  ADD PRIMARY KEY (`ident`);

--
-- Indexes for table `django_celery_beat_solarschedule`
--
ALTER TABLE `django_celery_beat_solarschedule`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_celery_beat_solar_event_latitude_longitude_ba64999a_uniq` (`event`,`latitude`,`longitude`);

--
-- Indexes for table `django_celery_results_chordcounter`
--
ALTER TABLE `django_celery_results_chordcounter`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `group_id` (`group_id`);

--
-- Indexes for table `django_celery_results_groupresult`
--
ALTER TABLE `django_celery_results_groupresult`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `group_id` (`group_id`),
  ADD KEY `django_cele_date_cr_bd6c1d_idx` (`date_created`),
  ADD KEY `django_cele_date_do_caae0e_idx` (`date_done`);

--
-- Indexes for table `django_celery_results_taskresult`
--
ALTER TABLE `django_celery_results_taskresult`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `task_id` (`task_id`),
  ADD KEY `django_cele_task_na_08aec9_idx` (`task_name`),
  ADD KEY `django_cele_status_9b6201_idx` (`status`),
  ADD KEY `django_cele_worker_d54dd8_idx` (`worker`),
  ADD KEY `django_cele_date_cr_f04a50_idx` (`date_created`),
  ADD KEY `django_cele_date_do_f59aad_idx` (`date_done`),
  ADD KEY `django_cele_periodi_1993cf_idx` (`periodic_task_name`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `expenses`
--
ALTER TABLE `expenses`
  ADD PRIMARY KEY (`id`),
  ADD KEY `expenses_property_id_95dbed3f` (`rental_property_id`),
  ADD KEY `expenses_landlord_id_58a6c892` (`landlord_id`);

--
-- Indexes for table `invitations`
--
ALTER TABLE `invitations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `invitations_landlord_id_e6185590_fk_users_id` (`landlord_id`),
  ADD KEY `invitations_lease_id_75ee530c` (`lease_id`);

--
-- Indexes for table `invoices`
--
ALTER TABLE `invoices`
  ADD PRIMARY KEY (`id`),
  ADD KEY `invoices_tenant_id_87941761` (`tenant_id`),
  ADD KEY `invoices_landlord_id_6c80bce0` (`landlord_id`),
  ADD KEY `invoices_lease_id_fcdd800b` (`lease_id`),
  ADD KEY `invoices_rental_property_id_cbdca392_fk_properties_id` (`rental_property_id`);

--
-- Indexes for table `landlord_accounts`
--
ALTER TABLE `landlord_accounts`
  ADD PRIMARY KEY (`customuser_ptr_id`);

--
-- Indexes for table `leases`
--
ALTER TABLE `leases`
  ADD PRIMARY KEY (`id`),
  ADD KEY `leases_landlord_id_1351940e` (`landlord_id`),
  ADD KEY `leases_tenant_id_9b3f9a65` (`tenant_id`),
  ADD KEY `leases_property_id_a153b4b9_fk_properties_id` (`property_id`);

--
-- Indexes for table `maintenance_tickets`
--
ALTER TABLE `maintenance_tickets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `maintenance_tickets_landlord_id_af6cb07f_fk_users_id` (`landlord_id`),
  ADD KEY `maintenance_tickets_property_id_cac825ac_fk_properties_id` (`property_id`),
  ADD KEY `maintenance_tickets_tenant_id_67ef2c50_fk_users_id` (`tenant_id`);

--
-- Indexes for table `payment_methods`
--
ALTER TABLE `payment_methods`
  ADD PRIMARY KEY (`id`),
  ADD KEY `payment_methods_tenant_id_be63116b` (`tenant_id`);

--
-- Indexes for table `properties`
--
ALTER TABLE `properties`
  ADD PRIMARY KEY (`id`),
  ADD KEY `properties_landlord_id_9cbfae9b` (`landlord_id`),
  ADD KEY `properties_building_id_50240b65` (`building_id`);

--
-- Indexes for table `tenant_accounts`
--
ALTER TABLE `tenant_accounts`
  ADD PRIMARY KEY (`customuser_ptr_id`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `idempotency_key` (`idempotency_key`),
  ADD KEY `transactions_landlord_id_3a901b5c_fk_users_id` (`landlord_id`),
  ADD KEY `transactions_invoice_id_b2e2bb58` (`invoice_id`),
  ADD KEY `transactions_tenant_id_36e35a29` (`tenant_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `idx_users_email` (`email`),
  ADD KEY `idx_users_deleted` (`deleted_at`);

--
-- Indexes for table `users_groups`
--
ALTER TABLE `users_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_groups_customuser_id_group_id_927de924_uniq` (`customuser_id`,`group_id`),
  ADD KEY `users_groups_group_id_2f3517aa_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `users_user_permissions`
--
ALTER TABLE `users_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_user_permissions_customuser_id_permission_id_2b4e4e39_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `users_user_permissio_permission_id_6d08dcd2_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=113;

--
-- AUTO_INCREMENT for table `buildings`
--
ALTER TABLE `buildings`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_beat_clockedschedule`
--
ALTER TABLE `django_celery_beat_clockedschedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_beat_crontabschedule`
--
ALTER TABLE `django_celery_beat_crontabschedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_beat_intervalschedule`
--
ALTER TABLE `django_celery_beat_intervalschedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_beat_periodictask`
--
ALTER TABLE `django_celery_beat_periodictask`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_beat_solarschedule`
--
ALTER TABLE `django_celery_beat_solarschedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_results_chordcounter`
--
ALTER TABLE `django_celery_results_chordcounter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_results_groupresult`
--
ALTER TABLE `django_celery_results_groupresult`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_results_taskresult`
--
ALTER TABLE `django_celery_results_taskresult`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `expenses`
--
ALTER TABLE `expenses`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `invitations`
--
ALTER TABLE `invitations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `invoices`
--
ALTER TABLE `invoices`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `leases`
--
ALTER TABLE `leases`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `maintenance_tickets`
--
ALTER TABLE `maintenance_tickets`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `payment_methods`
--
ALTER TABLE `payment_methods`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `properties`
--
ALTER TABLE `properties`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transactions`
--
ALTER TABLE `transactions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users_groups`
--
ALTER TABLE `users_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_user_permissions`
--
ALTER TABLE `users_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `buildings`
--
ALTER TABLE `buildings`
  ADD CONSTRAINT `buildings_landlord_id_c3a2efcb_fk_users_id` FOREIGN KEY (`landlord_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `django_celery_beat_periodictask`
--
ALTER TABLE `django_celery_beat_periodictask`
  ADD CONSTRAINT `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` FOREIGN KEY (`clocked_id`) REFERENCES `django_celery_beat_clockedschedule` (`id`),
  ADD CONSTRAINT `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` FOREIGN KEY (`crontab_id`) REFERENCES `django_celery_beat_crontabschedule` (`id`),
  ADD CONSTRAINT `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` FOREIGN KEY (`interval_id`) REFERENCES `django_celery_beat_intervalschedule` (`id`),
  ADD CONSTRAINT `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` FOREIGN KEY (`solar_id`) REFERENCES `django_celery_beat_solarschedule` (`id`);

--
-- Constraints for table `expenses`
--
ALTER TABLE `expenses`
  ADD CONSTRAINT `expenses_landlord_id_58a6c892_fk_users_id` FOREIGN KEY (`landlord_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `expenses_rental_property_id_60c2e5d8_fk_properties_id` FOREIGN KEY (`rental_property_id`) REFERENCES `properties` (`id`);

--
-- Constraints for table `invitations`
--
ALTER TABLE `invitations`
  ADD CONSTRAINT `invitations_landlord_id_e6185590_fk_users_id` FOREIGN KEY (`landlord_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `invitations_lease_id_75ee530c_fk_leases_id` FOREIGN KEY (`lease_id`) REFERENCES `leases` (`id`);

--
-- Constraints for table `invoices`
--
ALTER TABLE `invoices`
  ADD CONSTRAINT `invoices_landlord_id_6c80bce0_fk_users_id` FOREIGN KEY (`landlord_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `invoices_lease_id_fcdd800b_fk_leases_id` FOREIGN KEY (`lease_id`) REFERENCES `leases` (`id`),
  ADD CONSTRAINT `invoices_rental_property_id_cbdca392_fk_properties_id` FOREIGN KEY (`rental_property_id`) REFERENCES `properties` (`id`),
  ADD CONSTRAINT `invoices_tenant_id_87941761_fk_users_id` FOREIGN KEY (`tenant_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `landlord_accounts`
--
ALTER TABLE `landlord_accounts`
  ADD CONSTRAINT `landlord_accounts_customuser_ptr_id_bf775cb0_fk_users_id` FOREIGN KEY (`customuser_ptr_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `leases`
--
ALTER TABLE `leases`
  ADD CONSTRAINT `leases_landlord_id_1351940e_fk_users_id` FOREIGN KEY (`landlord_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `leases_property_id_a153b4b9_fk_properties_id` FOREIGN KEY (`property_id`) REFERENCES `properties` (`id`),
  ADD CONSTRAINT `leases_tenant_id_9b3f9a65_fk_users_id` FOREIGN KEY (`tenant_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `maintenance_tickets`
--
ALTER TABLE `maintenance_tickets`
  ADD CONSTRAINT `maintenance_tickets_landlord_id_af6cb07f_fk_users_id` FOREIGN KEY (`landlord_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `maintenance_tickets_property_id_cac825ac_fk_properties_id` FOREIGN KEY (`property_id`) REFERENCES `properties` (`id`),
  ADD CONSTRAINT `maintenance_tickets_tenant_id_67ef2c50_fk_users_id` FOREIGN KEY (`tenant_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `payment_methods`
--
ALTER TABLE `payment_methods`
  ADD CONSTRAINT `payment_methods_tenant_id_be63116b_fk_users_id` FOREIGN KEY (`tenant_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `properties`
--
ALTER TABLE `properties`
  ADD CONSTRAINT `properties_building_id_50240b65_fk_buildings_id` FOREIGN KEY (`building_id`) REFERENCES `buildings` (`id`),
  ADD CONSTRAINT `properties_landlord_id_9cbfae9b_fk_users_id` FOREIGN KEY (`landlord_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `tenant_accounts`
--
ALTER TABLE `tenant_accounts`
  ADD CONSTRAINT `tenant_accounts_customuser_ptr_id_12a3b985_fk_users_id` FOREIGN KEY (`customuser_ptr_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `transactions`
--
ALTER TABLE `transactions`
  ADD CONSTRAINT `transactions_invoice_id_b2e2bb58_fk_invoices_id` FOREIGN KEY (`invoice_id`) REFERENCES `invoices` (`id`),
  ADD CONSTRAINT `transactions_landlord_id_3a901b5c_fk_users_id` FOREIGN KEY (`landlord_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `transactions_tenant_id_36e35a29_fk_users_id` FOREIGN KEY (`tenant_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `users_groups`
--
ALTER TABLE `users_groups`
  ADD CONSTRAINT `users_groups_customuser_id_4bd991a9_fk_users_id` FOREIGN KEY (`customuser_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `users_groups_group_id_2f3517aa_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `users_user_permissions`
--
ALTER TABLE `users_user_permissions`
  ADD CONSTRAINT `users_user_permissio_permission_id_6d08dcd2_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `users_user_permissions_customuser_id_efdb305c_fk_users_id` FOREIGN KEY (`customuser_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
