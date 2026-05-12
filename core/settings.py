"""
Django Settings — Rent & Lease Management System

Configured per docs/documents file.md architecture:
- Custom User Model (AUTH_USER_MODEL)
- Django REST Framework with JWT authentication
- Django Channels for WebSockets
- Celery for background tasks
- CORS headers for cross-origin requests
- Security headers and CSRF protection
- Environment variables via python-decouple
"""
from pathlib import Path
from datetime import timedelta
from decouple import config, Csv

# ─── BASE DIRECTORY ──────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ─── SECURITY ────────────────────────────────────────────────
# Secret key loaded from environment — never hardcoded in production
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

# ─── APPLICATIONS ────────────────────────────────────────────
INSTALLED_APPS = [
    # Django Channels ASGI server (must be first)
    'daphne',

    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party packages
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'channels',
    'django_celery_beat',
    'django_celery_results',

    # Project apps (10 domain apps)
    'apps.users',
    'apps.properties',
    'apps.leases',
    'apps.financials',
    'apps.maintenance',
    'apps.chat',
    'apps.documents',
    'apps.analytics',
    'apps.notifications',
    'apps.automation',
]

# ─── MIDDLEWARE ───────────────────────────────────────────────
# Order matters — matches the 9-layer architecture middleware stack
MIDDLEWARE = [
    # 1. Security headers (HSTS, X-Content-Type-Options, etc.)
    'django.middleware.security.SecurityMiddleware',

    # 2. Session management
    'django.contrib.sessions.middleware.SessionMiddleware',

    # 3. CORS (must be before CommonMiddleware)
    'corsheaders.middleware.CorsMiddleware',

    # 4. URL normalization
    'django.middleware.common.CommonMiddleware',

    # 5. CSRF protection on all state-changing requests
    'django.middleware.csrf.CsrfViewMiddleware',

    # 6. Authentication (attaches request.user)
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # 7. Messages framework
    'django.contrib.messages.middleware.MessageMiddleware',

    # 8. Clickjacking protection (X-Frame-Options: DENY)
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Custom middleware (Phase 1)
    'middleware.logging_middleware.RequestLoggingMiddleware',
    'middleware.rate_limit_middleware.RateLimitMiddleware',
    'middleware.authorization_middleware.IDORAuthorizationMiddleware',
]

# ─── CACHE (used by rate limiting middleware) ────────────────
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'rate-limit-cache',
    }
}

# ─── CUSTOM USER MODEL ──────────────────────────────────────
# CRITICAL: This must be set BEFORE running any migrations.
# Changing this after migrations exist requires a full database rebuild.
AUTH_USER_MODEL = 'users.CustomUser'

# ─── URL CONFIGURATION ──────────────────────────────────────
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'

# ─── AUTHENTICATION URLS ───────────────────────────────────
# These settings define where Django redirects for auth flows
LOGIN_URL = '/login/'  # Redirect unauthenticated users here
LOGIN_REDIRECT_URL = '/landlord/dashboard/'  # Redirect after successful login
LOGOUT_REDIRECT_URL = '/login/'  # Redirect after logout

# ─── TEMPLATES ───────────────────────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'frontend' / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ─── DATABASE ────────────────────────────────────────────────
# SQLite for development, MySQL for production
# Switch by changing DB_ENGINE in .env
_db_engine = config('DB_ENGINE', default='django.db.backends.sqlite3')

if _db_engine == 'django.db.backends.sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / config('DB_NAME', default='db.sqlite3'),
        }
    }
else:
    _mysql_options = {
        'charset': 'utf8mb4',
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    }
    # LAMPP/XAMPP on Linux often uses a Unix socket instead of TCP (optional)
    _db_socket = config('DB_SOCKET', default='').strip()
    if _db_socket:
        _mysql_options['unix_socket'] = _db_socket

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            # XAMPP/LAMPP default user is often root with an empty password
            'PASSWORD': config('DB_PASSWORD', default=''),
            'HOST': config('DB_HOST', default='127.0.0.1'),
            'PORT': config('DB_PORT', default='3306'),
            'OPTIONS': _mysql_options,
        }
    }

# ─── PASSWORD VALIDATION ────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
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

# ─── INTERNATIONALIZATION ────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ─── STATIC FILES ───────────────────────────────────────────
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'frontend' / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ─── MEDIA FILES (User Uploads) ─────────────────────────────
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ─── DEFAULT PRIMARY KEY ────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ─── DJANGO REST FRAMEWORK ──────────────────────────────────
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

# ─── JWT CONFIGURATION ──────────────────────────────────────
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(
        hours=config('JWT_ACCESS_TOKEN_LIFETIME_HOURS', default=24, cast=int)
    ),
    'REFRESH_TOKEN_LIFETIME': timedelta(
        days=config('JWT_REFRESH_TOKEN_LIFETIME_DAYS', default=7, cast=int)
    ),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

# ─── CORS ────────────────────────────────────────────────────
CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    default='http://localhost:8000',
    cast=Csv()
)
CORS_ALLOW_CREDENTIALS = True

# ─── DJANGO CHANNELS ────────────────────────────────────────
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [config('REDIS_URL', default='redis://127.0.0.1:6379/0')],
        },
    },
}

# ─── CELERY ──────────────────────────────────────────────────
CELERY_BROKER_URL = config('CELERY_BROKER_URL', default='redis://127.0.0.1:6379/1')
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# ─── EMAIL ───────────────────────────────────────────────────
EMAIL_BACKEND = config(
    'EMAIL_BACKEND',
    default='django.core.mail.backends.console.EmailBackend'
)

# ─── SECURITY HEADERS ───────────────────────────────────────
# Applied in production (when DEBUG=False)
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
else:
    # Development: allow HTTP cookies
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_HTTPONLY = False  # Must be False — JS reads this for AJAX requests

# ─── LOGGING ─────────────────────────────────────────────────
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname} {name} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
