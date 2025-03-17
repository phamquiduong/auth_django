from django.urls import path

from _user import views

urlpatterns = [
    path('profile/',  views.profile_view, name='user-profile'),
    path('avatar/',  views.avatar_view, name='user-avatar'),
    path('password/',  views.password_view, name='user-password'),
]
