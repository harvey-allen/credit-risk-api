import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteModel
from helpers.base_model import BaseModel


class Title(models.TextChoices):
    MR = "Mr", _("Mr")
    MRS = "Mrs", _("Mrs")
    MS = "Ms", _("Ms")
    DR = "Dr", _("Dr")
    PROF = "Prof", _("Prof")
    OTHER = "Other", _("Other")


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser, BaseModel, SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    username = None
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=50, verbose_name="first name")
    middle_name = models.CharField(
        max_length=50, verbose_name="middle name", null=True, blank=True
    )
    last_name = models.CharField(max_length=50, verbose_name="last name")
    title = models.CharField(
        max_length=10,
        choices=Title.choices,
        verbose_name="Title",
        null=True,
        blank=True,
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(verbose_name="Phone Number", max_length=11)

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        return super().save(*args, **kwargs)
