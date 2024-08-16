from django.contrib import admin
from django.urls import path, include
from .views import HomeVista, AboutVista
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeVista.as_view(), name='home'),
    path('about/', AboutVista.as_view(), name='about'),
    path('paginas/', include('paginas.urls')),
    path('cuentas/', include('cuentas.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
