from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('',  include('common.urls')),
    path('auth/',  include('_auth.urls')),
    path('user/',  include('_user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
