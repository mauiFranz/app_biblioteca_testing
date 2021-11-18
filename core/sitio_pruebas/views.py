from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, CreateView
from core.sitio_pruebas.models import Libro
from core.sitio_pruebas.forms import LibroForm


# Create your views here.
@method_decorator(login_required, name='get')
class LibrosListView(ListView):
    queryset = Libro.objects.all()
    context_object_name = 'libros'
    template_name = 'core/sitio_pruebas/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Biblioteca Test'
        context['subtitulo'] = 'Listado de Libros'
        return context


@method_decorator(login_required, name='dispatch')
class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'core/sitio_pruebas/libro_create.html'
    success_url = reverse_lazy('sitio_pruebas:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Biblioteca Test'
        context['subtitulo'] = 'Registro de Libros'
        return context