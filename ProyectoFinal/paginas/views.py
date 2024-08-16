from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pagina
from django.urls import reverse_lazy

class PaginaListaVista(ListView):
    model = Pagina
    template_name = 'paginas/lista.html'

class PaginaDetalleVista(DetailView):
    model = Pagina
    template_name = 'paginas/detalle.html'

class PaginaCrearVista(CreateView):
    model = Pagina
    template_name = 'paginas/crear.html'
    fields = ['titulo', 'contenido']

class PaginaEditarVista(UpdateView):
    model = Pagina
    template_name = 'paginas/editar.html'
    fields = ['titulo', 'contenido']

class PaginaEliminarVista(DeleteView):
    model = Pagina
    template_name = 'paginas/eliminar.html'
    success_url = reverse_lazy('pagina_lista')
