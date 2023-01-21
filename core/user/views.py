from django.contrib.auth import get_user_model, views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .forms import LoginForm


_User = get_user_model()


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'user/user.html'


class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'


class LogoutView(views.LogoutView):
    template_name = 'user/logged_out.html'


class PasswordResetView(views.PasswordResetView):
    pass


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    pass


class PasswordResetDoneView(views.PasswordResetDoneView):
    pass


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    pass
