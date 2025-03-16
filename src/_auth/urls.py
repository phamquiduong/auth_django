from django.urls import path

from _auth import views

urlpatterns = [
    path('login', views.login_view, name='auth_login'),
]
