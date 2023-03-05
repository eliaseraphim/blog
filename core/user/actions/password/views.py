from django.contrib.auth import views

from user.actions.password import forms


class PasswordResetView(views.PasswordResetView):
    form_class = forms.PasswordResetForm
    email_template_name = "user/password/reset_email.html"
    template_name = "user/password/reset_form.html"
    subject_template_name = "user/password/reset_subject.txt"


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = "user/password/reset_done.html"


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    form_class = forms.SetPasswordForm
    template_name = "user/password/reset_confirm.html"


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = "user/password/reset_complete.html"


class PasswordChangeView(views.PasswordChangeView):
    form_class = forms.PasswordChangeForm
    template_name = "user/password/change_form.html"


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = "user/password/change_done.html"
