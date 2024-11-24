from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_company_admin = models.BooleanField(default=False)
    is_super_admin = models.BooleanField(default=False)

    @property
    def societe_associee(self):
        return getattr(self, 'societe', None)