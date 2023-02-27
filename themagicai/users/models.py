from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from themagicai.users.manager import CustomUserManager


class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=70)
    email = models.EmailField(_("Email of User"), unique=True)
    username = None
    first_name = None
    last_name = None

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"email": self.email})
