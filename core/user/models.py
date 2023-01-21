from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        max_length=64,
        blank=False,
        help_text=_('Required. Please enter a valid email.'),
    )

    objects = UserManager()

    def __str__(self):
        return f'{self.username} - <{self.email}>'

