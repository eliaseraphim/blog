from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', views.UserView.as_view(), name='user'),
    path('login/', TemplateView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', TemplateView.as_view(template_name='user/logged_out.html'), name='logout'),
]
