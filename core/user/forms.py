from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _

from user.models import User


class LoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        label=_("Username"),
        required=True,
        strip=True,
        widget=forms.TextInput(
            attrs={
                "autocomplete": "username",
                "autofocus": True,
                "class": "form-control",
                "placeholder": "Enter your username here...",
            }
        ),
    )
    password = forms.CharField(
        label=_("Password"),
        required=True,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control",
                "placeholder": "Enter your password here...",
            }
        ),
    )

    field_order = ["username", "password"]


class PasswordResetForm(auth_forms.PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "email",
                "class": "form-control",
                "placeholder": "Enter your email here...",
            }
        ),
    )


class SetPasswordForm(auth_forms.SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control",
                "placeholder": "Enter your new password here...",
            }
        ),
    )
    new_password2 = forms.CharField(
        label=_("Confirm New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control",
                "placeholder": "Enter your new password here...",
            }
        ),
    )

    field_order = ["new_password1", "new_password2"]


class PasswordChangeForm(SetPasswordForm):
    old_password = forms.CharField(
        label=_("Old Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "autofocus": True,
                "class": "form-control",
                "placeholder": "Enter your old password here...",
            }
        ),
    )

    field_order = ["old_password", "new_password1", "new_password2"]


class UsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }
