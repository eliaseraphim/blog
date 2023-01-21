from django.urls import path

from . import views


urlpatterns = [
    path('', views.UserView.as_view(), name='user'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
