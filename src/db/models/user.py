from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

from user.constants import DEFAULT_FULL_NAME, Role
from user.helpers import normalize_email


###################################################
# Manager
###################################################
class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str, **extra_fields):
        if not email:
            raise ValueError("Email is required.")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("role", Role.ADMIN)

        return self.create_user(email=email, password=password, **extra_fields)


###################################################
# Mixin
###################################################
class RoleMixin(models.Model):
    role = models.CharField(max_length=10, default=Role.GUEST)

    class Meta:
        abstract = True


class InfoMixin(models.Model):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        abstract = True

    def get_full_name(self, default=DEFAULT_FULL_NAME):
        return f"{self.last_name} {self.first_name}" if self.first_name and self.last_name else default


class TimestampMixin(models.Model):
    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class StatusMixin(models.Model):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    is_email_verified = models.BooleanField(default=False)

    class Meta:
        abstract = True


###################################################
# Model
###################################################
class User(AbstractBaseUser, RoleMixin, InfoMixin, TimestampMixin, StatusMixin):
    username = None

    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    def clean(self):
        super().clean()
        if self.email:
            self.email = normalize_email(email=self.email)

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    class Meta:
        db_table = "users"
