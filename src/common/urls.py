from django.urls import path

from common import views

urlpatterns = [
    path('heath-check', views.heath_check_view, name='heath_check'),
]
