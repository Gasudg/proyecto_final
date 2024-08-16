from django.urls import path
from .views import PaginaListaVista, PaginaDetalleVista, PaginaCrearVista, PaginaEditarVista, PaginaEliminarVista

urlpatterns = [
    path('', PaginaListaVista.as_view(), name='pagina_lista'),
    path('<int:pk>/', PaginaDetalleVista.as_view(), name='pagina_detalle'),
    path('crear/', PaginaCrearVista.as_view(), name='pagina_crear'),
    path('<int:pk>/editar/', PaginaEditarVista.as_view(), name='pagina_editar'),
    path('<int:pk>/eliminar/', PaginaEliminarVista.as_view(), name='pagina_eliminar'),
]
