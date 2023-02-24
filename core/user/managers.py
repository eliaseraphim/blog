from django.contrib.auth import models
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _


class UserManager(models.UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.

        :param username:
        """
        if not username:
            raise ValueError(_("The given username must be set."))
        if not email:
            raise ValueError(_("The given email must be set."))

        username = self.model.normalize_username(username)
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
