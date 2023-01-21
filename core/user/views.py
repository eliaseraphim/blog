from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, TemplateView


_User = get_user_model()


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'user/user.html'

class UserLoginView():
    pass
