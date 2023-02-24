from django.contrib.auth import get_user_model, views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .forms import LoginForm, PasswordResetForm, SetPasswordForm

_User = get_user_model()


class UserView(LoginRequiredMixin, TemplateView):
    template_name = "user/user.html"


class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = "user/login.html"


class LogoutView(views.LogoutView):
    template_name = "user/logged_out.html"


class PasswordResetView(views.PasswordResetView):
    form_class = PasswordResetForm
    email_template_name = "user/password_reset_email.html"
    template_name = "user/password_reset_form.html"
    subject_template_name = "user/password_reset_subject.txt"


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = "user/password_reset_done.html"


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    form_class = SetPasswordForm
    template_name = "user/password_reset_confirm.html"


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    pass
