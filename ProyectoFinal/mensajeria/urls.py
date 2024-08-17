from django.urls import path
from .views import agregar_comentario

urlpatterns = [
    path('comentario/<int:pagina_id>/', agregar_comentario, name='agregar_comentario'),
]
