# Migration Guide: Apps → Features Structure

## Overview

This guide documents the migration from the legacy `apps/` structure to the new `features/` structure following Agile methodology and Single Responsibility Principle.

## What Changed

### Old Structure (apps/)
```
apps/
├── users/
│   ├── models.py
│   ├── views.py (273 lines - multiple responsibilities)
│   ├── serializers.py
│   ├── business_logic.py
│   ├── business_rules.py
│   ├── permissions.py
│   └── urls.py
└── ... (other apps)
```

### New Structure (features/)
```
features/
└── authentication/
    ├── backend/
    │   ├── models.py
    │   ├── views/
    │   │   ├── register_view.py (single responsibility)
    │   │   ├── login_view.py (single responsibility)
    │   │   ├── verify_email_view.py
    │   │   ├── forgot_password_view.py
    │   │   └── reset_password_view.py
    │   ├── serializers.py
    │   ├── business_logic/
    │   │   ├── create_user.py
    │   │   ├── generate_tokens.py
    │   │   └── send_emails.py
    │   ├── business_rules/
    │   │   ├── validate_password.py
    │   │   └── validate_role.py
    │   ├── permissions.py
    │   ├── urls.py
    │   └── tests/
    └── frontend/
        ├── templates/
        └── js/
```

## Migration Steps Completed

### ✅ Phase 1: Foundation (COMPLETED)

1. **Created new directory structure**
   - `features/` folder with all feature subdirectories
   - `shared/` folder for utilities and constants
   - `core/middleware/` for middleware files

2. **Fixed critical bugs**
   - Removed duplicate URL patterns in `core/urls.py` (lines 31-34 duplicated 41-94)
   - Removed duplicate function definitions in `core/views.py` 
     - `landlord_dashboard` was defined twice (lines 33, 49)
     - `tenant_dashboard` was defined twice (lines 42)
   - Standardized all URLs to use trailing slashes consistently

3. **Created shared utilities**
   - `shared/constants.py` - Application-wide constants
   - `shared/exceptions/` - Custom exception classes
   - `shared/utils/email_service.py` - Centralized email service

4. **Moved middleware**
   - Copied from `middleware/` to `core/middleware/`
   - Old location preserved for backward compatibility

## Next Steps (To Be Completed)

### Phase 2: Authentication Migration (IN PROGRESS)

#### Backend Migration

**Step 1: Move Models** ✅ COMPLETED
- Moved `CustomUser` model to `features/authentication/backend/models.py`
- Model remains in `apps.users` for now (Django migrations dependency)
- Will switch AUTH_USER_MODEL after full migration

**Step 2: Split Views (TODO)**

Current: `apps/users/views.py` (273 lines)
```python
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    # Handles: validation, user creation, email sending
    pass
```

New: `features/authentication/backend/views/register_view.py`
```python
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from features.authentication.backend.serializers import RegisterSerializer
from features.authentication.backend.business_logic.create_user import create_user
from features.authentication.backend.business_logic.send_emails import send_verification_email_async

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """
    POST /api/v1/auth/register/
    
    Creates a new user account and queues verification email.
    Single responsibility: Handle HTTP request/response only.
    """
    serializer = RegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    
    # Delegate to business logic
    user = create_user(
        email=data['email'],
        password=data['password'],
        role=data['role'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        phone_number=data.get('phone_number', ''),
    )
    
    # Async email sending (non-blocking)
    send_verification_email_async.delay(user.id)
    
    return Response({
        'message': 'Account created. Please check your email to verify your account.',
        'user': UserProfileSerializer(user).data,
    }, status=status.HTTP_201_CREATED)
```

**Step 3: Split Business Logic (TODO)**

Current: `apps/users/business_logic.py` (172 lines)
- `create_user()`
- `generate_verification_token()`
- `send_verification_email()`
- `verify_email_token()`
- `generate_password_reset_token()`
- `send_password_reset_email()`
- `reset_password_with_token()`

New: Each function becomes its own file in `features/authentication/backend/business_logic/`
- `create_user.py`
- `generate_tokens.py` 
- `send_emails.py`

**Step 4: Split Business Rules (TODO)**

Current: `apps/users/business_rules.py`
New: `features/authentication/backend/business_rules/`
- `validate_password.py`
- `validate_role.py`
- `validate_name.py`

**Step 5: Create URL Configuration (TODO)**

File: `features/authentication/backend/urls.py`
```python
from django.urls import path
from features.authentication.backend.views import (
    register_view,
    login_view,
    verify_email_view,
    forgot_password_view,
    reset_password_view,
    me_view,
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('verify-email/', verify_email_view, name='verify_email'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('reset-password/', reset_password_view, name='reset_password'),
    path('me/', me_view, name='me'),
]
```

#### Frontend Migration (TODO)

**Step 1: Move Templates**
```
OLD:
frontend/templates/public/login.html
frontend/templates/public/register.html

NEW:
features/authentication/frontend/templates/login.html
features/authentication/frontend/templates/register.html
```

**Step 2: Create Feature-Specific JavaScript**
```
OLD:
frontend/static/js/api.js (monolithic)

NEW:
features/authentication/frontend/js/login.js
features/authentication/frontend/js/register.js
shared/js/api.js (shared API client)
```

### Phase 3: Update Django Settings (TODO)

**Update `core/settings.py`:**

```python
# OLD
INSTALLED_APPS = [
    # ...
    'apps.users',
    'apps.properties',
    # ...
]

# NEW (after full migration)
INSTALLED_APPS = [
    # ...
    'features.authentication',
    'features.properties',
    'features.leases',
    # ...
]

# Keep AUTH_USER_MODEL pointing to old location until migration complete
AUTH_USER_MODEL = 'users.CustomUser'  # Temporary
# AUTH_USER_MODEL = 'authentication.CustomUser'  # After migration
```

**Update `core/urls.py`:**

```python
# OLD
path('api/v1/auth/', include('apps.users.urls')),

# NEW (after migration)
path('api/v1/auth/', include('features.authentication.backend.urls')),
```

### Phase 4: Testing (TODO)

**Create comprehensive tests:**
```python
# features/authentication/backend/tests/test_registration.py
from django.test import TestCase
from rest_framework.test import APIClient
from features.authentication.backend.models import CustomUser

class RegistrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_register_success(self):
        response = self.client.post('/api/v1/auth/register/', {
            'email': 'test@example.com',
            'password': 'StrongP@ss123',
            'role': 'tenant',
            'first_name': 'Test',
            'last_name': 'User',
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(CustomUser.objects.filter(email='test@example.com').exists())
    
    def test_register_weak_password(self):
        response = self.client.post('/api/v1/auth/register/', {
            'email': 'test@example.com',
            'password': 'weak',
            'role': 'tenant',
            'first_name': 'Test',
            'last_name': 'User',
        })
        self.assertEqual(response.status_code, 400)
```

### Phase 5: Database Migration (TODO)

**Important:** Django migrations are tied to app labels. The migration strategy:

1. **Keep old apps** until all features migrated
2. **Create new feature apps** alongside old apps
3. **Test thoroughly** with both structures
4. **Switch AUTH_USER_MODEL** only after full migration
5. **Remove old apps** in final cleanup

**DO NOT delete `apps/` until:**
- All features migrated to `features/`
- All tests passing with new structure
- `AUTH_USER_MODEL` updated and migrations run
- Production deployment verified

## Benefits of New Structure

### 1. Single Responsibility Principle
- Each function handles ONE task
- Each file has ONE purpose
- Easy to understand, test, and maintain

### 2. Agile Alignment
- Each feature folder = one epic/story
- Independent development and deployment
- Sprint planning maps directly to structure

### 3. Separation of Concerns
- Frontend and backend separated but linked
- Clear boundaries between layers
- No circular dependencies

### 4. Scalability
- Easy to add new features
- Easy to refactor existing features
- Team can work on features in parallel

### 5. Testability
- Each function can be tested in isolation
- Mock dependencies easily
- High test coverage achievable

## Rollback Plan

If issues arise during migration:

1. **Old structure preserved** - `apps/` not deleted
2. **Git branches** - Each feature migration on separate branch
3. **Feature flags** - Can switch between old/new structure
4. **Database unchanged** - No destructive migrations

To rollback:
```bash
git checkout main  # Before migration
# Old structure intact, no data loss
```

## Developer Onboarding

**New developers should:**
1. Read this migration guide
2. Understand feature-based structure
3. Follow Single Responsibility Principle
4. Write tests for all new code
5. Keep frontend/backend separated but linked

**Code Review Checklist:**
- [ ] Function does ONE thing only
- [ ] File has clear, single purpose
- [ ] Frontend/backend properly separated
- [ ] Tests included
- [ ] Error handling present
- [ ] No hardcoded values
- [ ] Uses shared utilities where applicable

## Timeline

- **Sprint 1 (Week 1-2):** Foundation & Authentication ← YOU ARE HERE
- **Sprint 2 (Week 3-4):** Dashboard & Properties
- **Sprint 3 (Week 5-6):** Leases & Financials
- **Sprint 4 (Week 7-8):** Maintenance & Chat
- **Sprint 5 (Week 9-10):** Analytics, Notifications & Automation
- **Sprint 6 (Week 11-12):** Polish & Deployment

## Questions?

Refer to:
- Plan document: `Codebase_Analysis_&_Reorganization_*.md`
- Architecture docs: `docs/`
- Shared constants: `shared/constants.py`
- Shared exceptions: `shared/exceptions/__init__.py`
