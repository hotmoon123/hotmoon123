"""
Management command to create test users for development.

Usage:
    python manage.py create_test_users
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create test users for development'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating test users...')

        # Create test landlord
        landlord_email = 'landlord@test.com'
        if not User.objects.filter(email=landlord_email).exists():
            landlord = User.objects.create_user(
                email=landlord_email,
                password='testpass123',
                role='landlord',
                first_name='Test',
                last_name='Landlord',
                phone_number='+1234567890',
            )
            # Mark as verified so they can log in
            landlord.is_verified = True
            landlord.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f'✓ Created landlord: {landlord_email} / testpass123'
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Landlord {landlord_email} already exists')
            )

        # Create test tenant
        tenant_email = 'tenant@test.com'
        if not User.objects.filter(email=tenant_email).exists():
            tenant = User.objects.create_user(
                email=tenant_email,
                password='testpass123',
                role='tenant',
                first_name='Test',
                last_name='Tenant',
                phone_number='+0987654321',
            )
            # Mark as verified so they can log in
            tenant.is_verified = True
            tenant.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f'✓ Created tenant: {tenant_email} / testpass123'
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Tenant {tenant_email} already exists')
            )

        self.stdout.write(self.style.SUCCESS('\n✅ Test users created successfully!'))
        self.stdout.write(self.style.WARNING('\n⚠️  DO NOT use these credentials in production!\n'))
