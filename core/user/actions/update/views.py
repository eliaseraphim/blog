from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from user.models import User
from user.forms import PasswordChangeForm, UsernameForm


class UpdateUsernameView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UsernameForm
    template_name = "user/update/username.html"


class UpdatePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    pass


class UpdateAvatarView(LoginRequiredMixin, UpdateView):
    pass


class UpdatePersonalInformationView(LoginRequiredMixin, UpdateView):
    pass


class UpdateHeaderView(LoginRequiredMixin, UpdateView):
    pass


class UpdateBioView(LoginRequiredMixin, UpdateView):
    pass
