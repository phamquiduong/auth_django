from django.urls import path

from _user import views

urlpatterns = [
    path('profile/',  views.profile_view, name='user-profile'),
]
