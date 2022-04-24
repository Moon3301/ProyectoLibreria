from django.shortcuts import render, redirect
from .models import *
from .forms import *

def inicio (request):
    return render (request, 'index.html')

def libros (request):
    return render (request, 'libros.html')


def listarLibros (request):
    listado = Libro.objects.all()

    contexto = {'listado' : listado}
    return render (request, 'libros.html', contexto)
    


# Create your views here.
