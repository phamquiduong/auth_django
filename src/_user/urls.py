from django.urls import path

from _user import views

urlpatterns = [
    path('profile/',  views.profile_view, name='user-profile'),
    path('change-avatar/',  views.change_avatar_view, name='user-change_avatar'),

    # Change password
    path('change-password/',  views.change_password_view, name='user-change_password'),

    # Verify email
    path('send-verify-email/',  views.send_verify_email_view, name='user-send_verify_email'),
    path('verify-email/',  views.verify_email_view, name='user-verify_email'),
]
