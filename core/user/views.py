from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from blog.models import Post

from .forms import LoginForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm


class UserView(LoginRequiredMixin, TemplateView):
    template_name = "user/user.html"


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = "user/settings.html"
    post_model = Post

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update(
            {
                'posts': self.post_model.get_authors_posts(self.request.user)
            }
        )

        return context_data


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
    template_name = "user/password_reset_complete.html"


class PasswordChangeView(views.PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "user/password_change_form.html"


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = "user/password_change_done.html"
