from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('official_kkn_bot/', admin.site.urls),
    path('', include('chat.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

