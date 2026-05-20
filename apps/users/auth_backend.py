from django.contrib.auth.backends import ModelBackend
from .models import Landlord, Tenant


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            landlord = Landlord.objects.get(email=email)
            if landlord.check_password(password) and self.user_can_authenticate(landlord):
                return landlord
        except Landlord.DoesNotExist:
            pass

        try:
            tenant = Tenant.objects.get(email=email)
            if tenant.check_password(password) and self.user_can_authenticate(tenant):
                return tenant
        except Tenant.DoesNotExist:
            pass

        return None

    def get_user(self, user_id):
        try:
            return Landlord.objects.get(pk=user_id)
        except Landlord.DoesNotExist:
            try:
                return Tenant.objects.get(pk=user_id)
            except Tenant.DoesNotExist:
                return None
