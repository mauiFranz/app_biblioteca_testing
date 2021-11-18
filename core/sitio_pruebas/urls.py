from django.urls import path
from core.sitio_pruebas import views

app_name = 'sitio_pruebas'

urlpatterns = [
    path('', views.LibrosListView.as_view(), name='home'),
    path('libro_add/', views.LibroCreateView.as_view(), name='libro_add'),
]
