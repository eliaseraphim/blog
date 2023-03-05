from django.urls import path

from user.actions.password import views

urlpatterns = [
    path("change/", views.PasswordChangeView.as_view(), name="password_change"),
    path(
        "change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
