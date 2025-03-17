from django.contrib.auth import views as dj_auth_views
from django.urls import path

from _auth import views

urlpatterns = [
    path('login', views.login_view, name='auth-login'),
    path('logout', dj_auth_views.LogoutView.as_view(next_page='home'), name='auth-logout'),
]
