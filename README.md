# Rent & Lease Management System

A comprehensive property management platform built with Django, featuring landlord and tenant portals with real-time capabilities.

## 🏗️ Architecture

### Feature-Based Structure (NEW)

This project uses a **feature-based architecture** following Agile methodology and Single Responsibility Principle:

```
features/
├── authentication/     # User registration, login, password management
├── dashboard/          # Landlord & tenant dashboards
├── properties/         # Property & building management
├── leases/             # Lease creation & management
├── financials/         # Payments, invoices, financial reports
├── maintenance/        # Maintenance ticket system
├── chat/               # Real-time messaging (WebSocket)
├── documents/          # Document management
├── analytics/          # Analytics & reporting
├── notifications/      # Notification system
└── automation/         # Automated workflows

shared/                 # Shared utilities, constants, exceptions
core/                   # Django core configuration & middleware
```

### Each Feature Contains:

```
feature_name/
├── backend/
│   ├── models.py              # Data models
│   ├── views/                 # HTTP handlers (single responsibility)
│   │   ├── list_view.py
│   │   ├── create_view.py
│   │   └── update_view.py
│   ├── serializers.py         # Data serialization
│   ├── business_logic/        # Business processes
│   ├── business_rules/        # Validation rules
│   ├── services/              # Service layer
│   ├── urls.py                # Feature URL routing
│   └── tests/                 # Feature tests
└── frontend/
    ├── templates/             # HTML templates
    └── js/                    # Feature-specific JavaScript
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- MySQL 8.0+ (or SQLite for development)
- Redis 6.0+

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd rent-lease-management
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

8. **Start Redis** (for caching & WebSockets)
   ```bash
   redis-server
   ```

9. **Start Celery** (for background tasks)
   ```bash
   celery -A core worker -l info
   ```

## 📁 Project Structure

### Core Directories

| Directory | Purpose |
|-----------|---------|
| `features/` | All feature modules (frontend + backend) |
| `shared/` | Shared utilities, constants, exceptions |
| `core/` | Django configuration, middleware, settings |
| `media/` | User-uploaded files |
| `logs/` | Application logs |
| `docs/` | Architecture & design documentation |

### Key Files

| File | Purpose |
|------|---------|
| `core/settings.py` | Django configuration |
| `core/urls.py` | Root URL routing |
| `shared/constants.py` | Application-wide constants |
| `shared/exceptions/` | Custom exception classes |
| `shared/utils/email_service.py` | Email sending service |
| `.env` | Environment variables (not committed) |
| `requirements.txt` | Python dependencies |
| `manage.py` | Django management script |

## 🎯 Development Guidelines

### Single Responsibility Principle

**Each function should do ONE thing only:**

✅ **Good:**
```python
# features/authentication/backend/views/register_view.py
def register_view(request):
    """Handle HTTP request/response for registration."""
    # Validate, delegate, return response
```

❌ **Bad:**
```python
# apps/users/views.py (273 lines, 5+ responsibilities)
def register_view(request):
    # Validate, create user, send email, log, format response...
```

### Feature Organization

**Keep frontend and backend together:**

```
features/authentication/
├── backend/          # All backend code
└── frontend/         # All frontend code
```

### Error Handling

**Always log errors and handle gracefully:**

```python
import logging

logger = logging.getLogger(__name__)

try:
    send_verification_email(user)
except EmailServiceError as e:
    logger.error(f"Email failed for user {user.id}: {e}")
    # Handle gracefully
except Exception as e:
    logger.critical(f"Unexpected error: {e}")
    raise
```

### Testing

**Write tests for all new code:**

```python
# features/authentication/backend/tests/test_registration.py
class RegistrationTests(TestCase):
    def test_register_success(self):
        # Test happy path
        pass
    
    def test_register_weak_password(self):
        # Test validation
        pass
```

## 🔄 Migration Status

This project is undergoing a major reorganization from `apps/` to `features/` structure.

**Current Status:** Sprint 1 of 6 (35% complete)

- ✅ Foundation complete
- 🔄 Authentication migration in progress
- ⏳ Other features pending

See `MIGRATION_GUIDE.md` and `IMPLEMENTATION_SUMMARY.md` for details.

## 🛠️ Technology Stack

### Backend
- **Django 6.0+** - Web framework
- **Django REST Framework** - API development
- **JWT** - Authentication
- **Django Channels** - WebSockets
- **Celery** - Background tasks
- **MySQL** - Primary database
- **Redis** - Caching & message broker

### Frontend
- **Django Templates** - Server-side rendering
- **Vanilla JavaScript (ES6+)** - Client-side logic
- **Custom Design System** - CSS with design tokens
- **Chart.js** - Data visualization
- **Lucide Icons** - Icon library

### Security
- **BCrypt** - Password hashing
- **JWT with rotation** - Token management
- **IDOR protection** - Authorization middleware
- **Rate limiting** - Request throttling
- **CORS** - Cross-origin protection
- **CSRF** - Cross-site request forgery protection

## 📊 API Documentation

### Authentication Endpoints

```
POST   /api/v1/auth/register/        # Create account
POST   /api/v1/auth/login/           # Authenticate
POST   /api/v1/auth/verify-email/    # Verify email
POST   /api/v1/auth/forgot-password/ # Request reset
POST   /api/v1/auth/reset-password/  # Reset password
GET    /api/v1/auth/me/              # Get current user
```

### Properties Endpoints

```
GET    /api/v1/properties/           # List properties
POST   /api/v1/properties/           # Create property
GET    /api/v1/properties/{id}/      # Get property
PUT    /api/v1/properties/{id}/      # Update property
DELETE /api/v1/properties/{id}/      # Delete property
```

See individual feature documentation for complete API specs.

## 🧪 Testing

### Run Tests

```bash
# All tests
python manage.py test

# Specific feature
python manage.py test features.authentication

# With coverage
coverage run manage.py test
coverage report
coverage html
```

### Test Structure

```
features/{feature}/backend/tests/
├── test_models.py
├── test_views.py
├── test_serializers.py
├── test_business_logic.py
└── test_business_rules.py
```

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG=False` in `.env`
- [ ] Configure MySQL database
- [ ] Set up Redis server
- [ ] Configure email backend (SendGrid, SES, etc.)
- [ ] Set up SSL certificates
- [ ] Configure static files (WhiteNoise or CDN)
- [ ] Set up Celery workers
- [ ] Configure logging
- [ ] Run security checks (`python manage.py check --deploy`)
- [ ] Enable monitoring (Sentry, New Relic, etc.)

### Deployment Commands

```bash
# Collect static files
python manage.py collectstatic

# Run migrations
python manage.py migrate

# Restart services
sudo systemctl restart gunicorn
sudo systemctl restart celery
sudo systemctl restart nginx
```

## 📚 Documentation

- **Migration Guide:** `MIGRATION_GUIDE.md`
- **Implementation Summary:** `IMPLEMENTATION_SUMMARY.md`
- **System Architecture:** `docs/system architecture`
- **Technical Architecture:** `docs/technical architecture`
- **API Documentation:** (Coming soon)

## 🤝 Contributing

### Development Workflow

1. Create feature branch from `develop`
2. Implement feature in `features/{feature_name}/`
3. Write tests
4. Submit pull request
5. Code review
6. Merge to `develop`

### Code Review Checklist

- [ ] Single Responsibility Principle followed
- [ ] Frontend/backend properly separated
- [ ] Tests included and passing
- [ ] Error handling present
- [ ] No hardcoded values
- [ ] Uses shared utilities
- [ ] Documentation updated

## 📝 License

[Your License Here]

## 👥 Team

- **Developer:** [Your Name]
- **Role:** Full-Stack Engineer
- **Contact:** [Your Email]

---

**Last Updated:** 2026-04-21

**Status:** Under active development (Sprint 1 of 6)
