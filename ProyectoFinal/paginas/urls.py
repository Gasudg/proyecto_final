from django.urls import path
from .views import PaginaListaVista, PaginaDetalleVista, PaginaCrearVista, PaginaEditarVista, PaginaEliminarVista

urlpatterns = [
    path('', PaginaListaVista.as_view(), name='pagina_lista'),
    path('<int:pk>/', PaginaDetalleVista.as_view(), name='pagina_detalle'),
    path('crear/', PaginaCrearVista.as_view(), name='pagina_crear'),
    path('editar/<int:pk>/', PaginaEditarVista.as_view(), name='pagina_editar'),
    path('eliminar/<int:pk>/', PaginaEliminarVista.as_view(), name='pagina_eliminar'),
]
