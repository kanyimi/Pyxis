from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

