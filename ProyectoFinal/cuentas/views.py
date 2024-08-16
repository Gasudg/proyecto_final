from django.urls import reverse_lazy
from django.views import generic
from .forms import FormularioRegistroUsuario
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.contrib.auth import logout


class VistaRegistro(generic.CreateView):
    form_class = FormularioRegistroUsuario
    template_name = 'registro/registro.html'
    success_url = reverse_lazy('login')


class LogoutVista(LogoutView):
    next_page = reverse_lazy('login')


def cerrar_sesion(request):
    logout(request)
    return redirect('/')
