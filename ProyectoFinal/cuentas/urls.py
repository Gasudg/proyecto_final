from django.urls import path
from django.contrib.auth import views as auth_views
from .views import EditarPerfilVista, PerfilVista, VistaRegistro, cerrar_sesion, CambiarPasswordVista

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registro/login.html'), name='login'),
    path('logout/', cerrar_sesion, name='logout'),  # Usa la vista personalizada
    path('registro/', VistaRegistro.as_view(), name='registro'),
    path('perfil/', PerfilVista.as_view(), name='perfil'),
    path('perfil/editar/', EditarPerfilVista.as_view(), name='editar_perfil'),
    path('perfil/cambiar_password/', CambiarPasswordVista.as_view(), name='cambiar_password'),

]
