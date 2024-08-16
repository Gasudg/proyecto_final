# paginas/views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pagina
from django.urls import reverse_lazy

class PaginaListaVista(ListView):
    model = Pagina
    template_name = 'paginas/lista.html'
    context_object_name = 'paginas'

class PaginaDetalleVista(DetailView):
    model = Pagina
    template_name = 'paginas/detalle.html'
    context_object_name = 'pagina'

class PaginaCrearVista(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Pagina
    template_name = 'paginas/crear.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_message = "Página creada con éxito."
    success_url = reverse_lazy('pagina_lista')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PaginaEditarVista(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Pagina
    template_name = 'paginas/editar.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_message = "Página actualizada con éxito."

class PaginaEliminarVista(LoginRequiredMixin, DeleteView):
    model = Pagina
    template_name = 'paginas/eliminar.html'
    success_url = '/paginas/'
    success_message = "Página eliminada con éxito."
