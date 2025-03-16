from django.urls import path

from common import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('heath-check', views.heath_check_view, name='heath_check'),
]
