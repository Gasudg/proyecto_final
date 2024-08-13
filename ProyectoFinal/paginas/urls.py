from django.urls import path
from .views import PaginaListaVista, PaginaDetalleVista, PaginaCrearVista, PaginaActualizarVista, PaginaEliminarVista

urlpatterns = [
    path('', PaginaListaVista.as_view(), name='lista-paginas'),
    path('<int:pk>/', PaginaDetalleVista.as_view(), name='detalle-pagina'),
    path('crear/', PaginaCrearVista.as_view(), name='crear-pagina'),
    path('<int:pk>/editar/', PaginaActualizarVista.as_view(), name='editar-pagina'),
    path('<int:pk>/eliminar/', PaginaEliminarVista.as_view(), name='eliminar-pagina'),
]
