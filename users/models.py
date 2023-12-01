from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    @property
    def is_vendedor(self):
        return self.groups.filter(name="vendedor").exists()
