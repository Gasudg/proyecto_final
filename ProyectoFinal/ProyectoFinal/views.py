from django.shortcuts import render
from django.views.generic import TemplateView

class InicioVista(TemplateView):
    template_name = 'inicio.html'

class AcercaDeMiVista(TemplateView):
    template_name = 'acerca_de_mi.html'
