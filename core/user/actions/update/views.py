from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, UpdateView
from django.urls import reverse

from user.actions.update import forms
from user.models import User


class SettingsView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("update_username")


class UpdateUsernameView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = forms.UsernameForm
    template_name = "user/update/username.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("update_username")


class UpdatePasswordView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = forms.PasswordForm
    template_name = "user/update/password.html"

    def form_valid(self, form):
        user = form.save()
        if user is not None:  # update current session credentials
            update_session_auth_hash(self.request, user)

        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("update_password")


class UpdateAvatarView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = forms.AvatarForm
    template_name = "user/update/avatar.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("update_avatar")


class UpdateNameView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = forms.NameForm
    template_name = "user/update/name.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("update_name")


class UpdateHeaderView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = forms.HeaderForm
    template_name = "user/update/header.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("update_header")


class UpdateBioView(LoginRequiredMixin, UpdateView):
    model = User
    pass
