from django.urls import path

from user.actions.update import views

urlpatterns = [
    path("", views.SettingsView.as_view(), name="settings"),
    path("username/", views.UpdateUsernameView.as_view(), name="update_username"),
    path("password/", views.UpdatePasswordView.as_view(), name="update_password"),
    path("avatar/", views.UpdateAvatarView.as_view(), name="update_avatar"),
    path("name/", views.UpdateNameView.as_view(), name="update_name"),
    path("header/", views.UpdateHeaderView.as_view(), name="update_header")
]
