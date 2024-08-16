from django.urls import path
from django.contrib.auth import views as auth_views
from .views import VistaRegistro, cerrar_sesion

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registro/login.html'), name='login'),
    path('logout/', cerrar_sesion, name='logout'),  # Usa la vista personalizada
    path('registro/', VistaRegistro.as_view(), name='registro'),
]
