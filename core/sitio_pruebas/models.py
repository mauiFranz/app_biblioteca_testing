from django.db import models
from django.db.models.base import Model



# Create your models here.
class Materia(models.Model):
    nombre_materia = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre_materia


class Libro(models.Model):
    isbn = models.CharField(primary_key=True, max_length=25)
    nombre_libro = models.CharField(max_length=50)
    materia_libro = models.ForeignKey(Materia, on_delete=models.CASCADE)