from _user.views.avatar import change_avatar_view
from _user.views.email import send_verify_email_view, verify_email_view
from _user.views.password import change_password_view
from _user.views.profile import profile_view

__all__ = [
    'profile_view',
    'change_avatar_view',
    'change_password_view',
    'send_verify_email_view', 'verify_email_view',
]
