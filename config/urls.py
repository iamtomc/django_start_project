
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from filebrowser.sites import site

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', include('apps.core.urls', namespace="core")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
