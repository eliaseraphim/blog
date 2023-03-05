from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from user.forms import LoginForm


class UserView(LoginRequiredMixin, TemplateView):
    template_name = "user/user.html"


class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = "user/login.html"


class LogoutView(views.LogoutView):
    template_name = "user/logged_out.html"
