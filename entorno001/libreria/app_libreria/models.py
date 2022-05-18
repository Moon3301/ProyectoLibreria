from operator import mod
from statistics import mode
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
        return self.rut


class CategoriaLibro(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id       = models.IntegerField(primary_key=True)
    nombre   = models.CharField(max_length=50)
    autor    = models.CharField(max_length=50)
    imagen   = models.CharField(max_length=50)
    editorial= models.CharField(max_length=50)
    stock    = models.IntegerField()
    precio = models.IntegerField()
    categoria = models.ForeignKey(CategoriaLibro, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Tienda(models.Model):
    id        = models.IntegerField(primary_key=True)
    ubicacion = models.CharField(max_length=50)
    def __str__(self):
        return self.ubicacion

class Carrito(models.Model):
    id    = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    listaLibros = models.ManyToManyField(Libro)
    
    

    def __str__(self):
        return str(self.id)
    # rut_cliente = models.ForeignKey(Cliente)
