from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class AccessType(models.Model):
    access_type = models.CharField(null=False, blank=False, max_length=30)


class ToorinUserManager(UserManager):
    def create(self, username, email=None, password=None, **extra_fields):
        return super().create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        user = super().create_superuser(username, email, password, **extra_fields)
        user.access_type = AccessType.objects.get(id=1)
        user.save()
        return user


class User(AbstractUser):
    access_type = models.ForeignKey(AccessType, on_delete=models.PROTECT, default=3)
    email = models.EmailField(_('email address'), unique=True)
    objects = ToorinUserManager()
