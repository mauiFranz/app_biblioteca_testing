from django import forms
from core.sitio_pruebas.models import Materia, Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'isbn',
            'nombre_libro',
            'materia_libro'
        ]
        labels = {
            'isbn': 'ISBN',
            'nombre_libro': 'Nombre',
            'materia_libro': 'Materia',
        }
        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el número ISBN', 'required': 'true'}),
            'nombre_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Título del Libro', 'required': 'true'}),
            'materia_libro': forms.Select(attrs={'class': 'form-select', 'required': 'true'}),
        }