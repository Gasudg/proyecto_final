from django.urls import reverse_lazy
from django.views import generic
from .forms import FormularioRegistroUsuario, EditarPerfilForm
from django.contrib.auth.views import LogoutView , PasswordChangeView
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from .models import Perfil

class VistaRegistro(generic.CreateView):
    form_class = FormularioRegistroUsuario
    template_name = 'registro/registro.html'
    success_url = reverse_lazy('login')


class LogoutVista(LogoutView):
    next_page = reverse_lazy('login')


class PerfilVista(LoginRequiredMixin, DetailView):
    model = Perfil
    template_name = 'registro/perfil.html'
    
    def get_object(self):
        return self.request.user.perfil
    

class EditarPerfilVista(LoginRequiredMixin, UpdateView):
    model = Perfil
    form_class = EditarPerfilForm
    template_name = 'registro/editar_perfil.html'
    success_url = reverse_lazy('perfil')

    def get_object(self):
        return self.request.user.perfil

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    

class CambiarPasswordVista(PasswordChangeView):
    template_name = 'registro/cambiar_password.html'
    success_url = reverse_lazy('perfil')


def cerrar_sesion(request):
    logout(request)
    return redirect('/')
