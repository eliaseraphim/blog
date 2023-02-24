from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


def user_avatar_path(instance, filename):
    now = timezone.now()
    return (
        f"users/{instance.get_username()}/{now.year}/{now.month}/{now.day}/{filename}"
    )


class User(AbstractUser):
    email = models.EmailField(
        _("email address"),
        blank=False,
        help_text=_("Required. Please enter a valid email."),
        max_length=254,
    )
    avatar = models.ImageField(
        blank=True,
        help_text="Your user avatar.",
        null=True,
        upload_to=user_avatar_path,
        verbose_name="User Avatar",
    )
    bio = models.CharField(
        blank=True,
        help_text="Say a little something about yourself.",
        null=True,
        max_length=255,
        verbose_name="User Bio",
    )
    website = models.CharField(
        blank=True,
        help_text="Your personal website.",
        null=True,
        max_length=255,
        verbose_name="User Website",
    )

    objects = UserManager()

    def __str__(self):
        return f"{self.username} - <{self.email}>"
