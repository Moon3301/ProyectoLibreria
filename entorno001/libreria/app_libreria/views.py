from django.shortcuts import render, redirect
from .models import *
from .forms import *

def inicio (request):
    return render (request, 'index.html')

def libros (request):
    return render (request, 'libros.html')

def libros1 (request):
    return render (request, 'detalle_libros.html')



def listarLibros (request):
    listado = Libro.objects.all()

    contexto = {'listado' : listado}
    return render (request, 'libros.html', contexto)


def detalleLibros (request, id):
    
    libro = Libro.objects.get(id = id)
    
    contexto = {'Libro' : LibroForm(instance=libro)}
    
    
    return render (request, 'detalle_libros.html')
    


# Create your views here.
