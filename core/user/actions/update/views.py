from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView

from user.actions.update import forms
from user.models import User


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = "user/settings.html"


class UpdateUsernameView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = forms.UsernameForm
    template_name = "user/update/username.html"

    def get_object(self, queryset=None):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, UpdateView):
    pass


class UpdateAvatarView(LoginRequiredMixin, UpdateView):
    pass


class UpdatePersonalInformationView(LoginRequiredMixin, UpdateView):
    pass


class UpdateHeaderView(LoginRequiredMixin, UpdateView):
    pass


class UpdateBioView(LoginRequiredMixin, UpdateView):
    pass
