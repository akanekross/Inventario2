from django.db import models

class Productos(models.Model):
    Nserie = models.CharField(max_length=100)
    NomProducto=models.CharField(max_length=100)
    Descripcion=models.CharField(max_length=100)
    Cantidad=models.CharField(max_length=100)
    Categoria=models.CharField(max_length=100)
    Precio=models.CharField(max_length=100)

# Create your models here.
