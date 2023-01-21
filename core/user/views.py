from django.contrib.auth import get_user_model
from django.views.generic import DetailView, TemplateView


_User = get_user_model()


class UserView(TemplateView):
    template_name = 'user/user.html'
