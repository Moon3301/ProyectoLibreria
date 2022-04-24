from tkinter import image_names
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Cliente(models.Model):
    rut       = models.IntegerField(primary_key=True)
    nombre    = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    correo    = models.EmailField( max_length=50)
    telefono  = models.IntegerField()
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id       = models.IntegerField(primary_key=True)
    nombre   = models.CharField(max_length=50)
    autor    = models.CharField(max_length=50)
    imagen   = models.ImageField()
    editorial= models.CharField(max_length=50)
    stock    = models.IntegerField()
    def __str__(self):
        return self.nombre
    
class Tienda(models.Model):
    id        = models.IntegerField(primary_key=True)
    ubicacion = models.CharField(max_length=50)
    def __str__(self):
        return self.ubicacion