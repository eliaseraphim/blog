from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


# Create your models here.
class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _('email address'),
        max_length=64,
        blank=False,
        help_text=_('Required. Please enter a valid email.'),
    )
    avatar = models.ImageField(blank=True, null=True, upload_to=f'users/{username}/%Y/%m/%d')
    bio = models.CharField(null=True, blank=True, max_length=255)
    website = models.CharField(null=True, blank=True, max_length=255)

    objects = UserManager()

    def __str__(self):
        return f'{self.username} - <{self.email}>'

