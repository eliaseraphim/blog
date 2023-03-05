from django.urls import include, path

from user import views

urlpatterns = [
    path("", views.UserView.as_view(), name="user"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("settings/", include("user.actions.update.urls")),
    path("password", include("user.actions.password.urls")),
]
