from django.shortcuts import render
from django.views.generic import TemplateView

class HomeVista(TemplateView):
    template_name = 'home.html'

class AboutVista(TemplateView):
    template_name = 'about.html'