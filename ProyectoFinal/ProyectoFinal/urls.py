from django.contrib import admin
from django.urls import path, include
from .views import InicioVista, AcercaDeMiVista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioVista.as_view(), name='inicio'),
    path('acerca-de-mi/', AcercaDeMiVista.as_view(), name='acerca_de_mi'),
    path('paginas/', include('paginas.urls')),
    path('cuentas/', include('cuentas.urls')),
]
