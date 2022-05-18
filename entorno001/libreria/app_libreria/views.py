from django import views
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def inicio (request):
    return render (request, 'index.html')

def listarLibros (request):
    listado = Libro.objects.all()

    contexto = {'listado' : listado}
    return render (request, 'libros.html', contexto)


def detalleLibros (request, id):
    
    libro = Libro.objects.get(id = id)
    
    contexto = {'Libro' : libro}
    
    return render (request, 'detalle_libros.html',contexto)

def formCompra(request):

    contexto = {'formulario' : ClienteForm}

    if request.method == 'POST':

        cliente = ClienteForm(request.POST)
        cliente.save()
        contexto['mensaje'] = 'Datos Guardados'

    return render (request, 'formCompra.html', contexto)
    


# Create your views here.
