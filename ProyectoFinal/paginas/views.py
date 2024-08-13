from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pagina

class PaginaListaVista(ListView):
    model = Pagina
    template_name = 'paginas/lista_paginas.html'

class PaginaDetalleVista(DetailView):
    model = Pagina
    template_name = 'paginas/detalle_pagina.html'

class PaginaCrearVista(CreateView):
    model = Pagina
    template_name = 'paginas/formulario_pagina.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'fecha_publicacion']

class PaginaActualizarVista(UpdateView):
    model = Pagina
    template_name = 'paginas/formulario_pagina.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'fecha_publicacion']

class PaginaEliminarVista(DeleteView):
    model = Pagina
    template_name = 'paginas/confirmar_eliminar_pagina.html'
    success_url = '/'
