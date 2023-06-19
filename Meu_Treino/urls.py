from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('apps.core.urls')),
    path("acounts/",include('apps.acounts.urls')),
    path("",include('apps.dietas.urls')),
    path("",include('apps.treinos.urls')),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)