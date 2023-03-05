from django.urls import path

from user.actions.update import views

urlpatterns = [
    path("", views.SettingsView.as_view(), name="settings"),
    path("username/", views.UpdateUsernameView.as_view(), name="update_username"),
]
