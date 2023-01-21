from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


def user_avatar_path(instance, filename):
    now = timezone.now()
    return f'users/{instance.get_username()}/{now.year}/{now.month}/{now.day}/{filename}'


class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        max_length=64,
        blank=False,
        help_text=_('Required. Please enter a valid email.'),
    )
    avatar = models.ImageField(blank=True, null=True, upload_to=user_avatar_path)
    bio = models.CharField(null=True, blank=True, max_length=255)
    website = models.CharField(null=True, blank=True, max_length=255)

    objects = UserManager()

    def __str__(self):
        return f'{self.username} - <{self.email}>'
