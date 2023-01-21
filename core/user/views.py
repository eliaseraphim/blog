from django.views.generic import TemplateView

from .models import User


class UserView(TemplateView):
    template_name = 'user/user.html'
