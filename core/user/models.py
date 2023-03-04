from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


def get_avatar_path(instance, filename):
    now = timezone.now()
    return f"user/{instance.get_username()}/avatar/{now.year}/{now.month}/{now.day}/{now.hour}:{now.month}:{now.second} - {filename}"


def get_header_path(instance, filename):
    now = timezone.now()
    return f"user/{instance.get_username()}/header/{now.year}/{now.month}/{now.day}/{now.hour}:{now.month}:{now.second} - {filename}"


class User(AbstractUser):
    # user information
    email = models.EmailField(
        _("email address"),
        blank=False,
        help_text=_("Required. Please enter a valid email."),
        max_length=254,
    )
    avatar = models.ImageField(
        blank=True,
        help_text="User Avatar. Displayed on posts, and in user page.",
        null=True,
        upload_to=get_avatar_path,
        verbose_name="User Avatar",
    )
    header = models.ImageField(
        blank=True,
        help_text=_("Header Image. Displayed above the user biography."),
        null=True,
        upload_to=get_header_path,
        verbose_name="Header Image",
    )
    bio = models.TextField(
        blank=True,
        help_text=_("Introduce yourself."),
        verbose_name="User Bio",
    )
    website = models.CharField(
        blank=True,
        help_text="Your personal website.",
        max_length=255,
        verbose_name="User Website",
    )

    # privacy
    show_email = models.BooleanField(
        default=False,
        help_text=_("Show email on personal page?"),
        verbose_name=_("Show Email"),
    )
    show_first_name = models.BooleanField(
        default=False,
        help_text=_("Show first name on personal page?"),
        verbose_name=_("Show First Name"),
    )
    show_last_name = models.BooleanField(
        default=False,
        help_text=_("Show last name on personal page?"),
        verbose_name=_("Show Last Name"),
    )
    show_website = models.BooleanField(
        default=False,
        help_text=_("Show website on personal page?"),
        verbose_name=_("Show Website"),
    )

    objects = UserManager()

    def __str__(self):
        return f"{self.username} - <{self.email}>"
