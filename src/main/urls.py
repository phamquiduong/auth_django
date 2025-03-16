from django.urls import include, path

urlpatterns = [
    path('',  include('common.urls')),
    path('auth/',  include('_auth.urls')),
    path('user/',  include('_user.urls')),
]
