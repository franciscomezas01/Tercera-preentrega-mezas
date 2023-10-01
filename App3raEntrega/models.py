from django.db import models

# Create your models here.
class TipoDeCafe(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    sabor = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.sabor}"

class Origen(models.Model):
    nombre = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nombre} - {self.pais} - {self.region}"

class Preparacion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    def __str__(self):
        return f"{self.nombre}- {self.descripcion}"

    