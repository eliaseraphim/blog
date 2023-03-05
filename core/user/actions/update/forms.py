from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

from user.models import User
from django.utils.translation import gettext_lazy as _


class UsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }


class PasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["new_password1", "new_password2"]

    error_messages = {
        "password_mismatch": _("The two password fields didn't match."),
        "password_incorrect": _(
            "Your old password was entered incorrectly. Please enter it again."
        ),
    }
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
    new_password1 = forms.CharField(
        label=_("New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control",
                "placeholder": _("Enter your new password here..."),
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Confirm New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control",
                "placeholder": _("Re-enter your new password here..."),
            }
        ),
        help_text=_("Enter the same password as before, for verification."),
    )

    field_order = ["old_password", "new_password1", "new_password2"]

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.instance.check_password(old_password):
            raise ValidationError(
                self.error_messages["password_incorrect"],
                code="password_incorrect",
            )
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    self.error_messages["password_mismatch"],
                    code="password_mismatch",
                )
        password_validation.validate_password(password2, self.instance)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.instance.set_password(password)
        if commit:
            self.instance.save()
        return self.instance


class AvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["avatar"]
        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"})
        }


class NameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["show_first_name", "first_name", "show_last_name", "last_name"]
        widgets = {
            "show_first_name": forms.CheckboxInput(),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "show_last_name": forms.CheckboxInput(),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }


class HeaderForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["header"]
        widgets = {
            "header": forms.ClearableFileInput(attrs={"class": "form-control"})
        }
