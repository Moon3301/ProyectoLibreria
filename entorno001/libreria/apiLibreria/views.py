from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.serializers import Serializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework.authtoken.models import Token

from .serializers import *
from app_libreria.models import *
from app_libreria.models import Libro

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated


@api_view(['GET','POST'])
def listarLibro(request):
    if request.method == 'GET':
        listado = Libro.objects.all()
        Serializer = LibroSerializers(listado, many=True)
        return Response(Serializer.data)

    elif request.method == 'POST':
        Serializer = LibroSerializers(data= request.data)

    if Serializer.is_valid():
        Serializer.save()
        return Response(Serializer.data, status= status.HTTP_201_CREATED)
    
    return Response(Serializer.errors, status= status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def libroLista(request, id):
    libro = Libro.objects.get(id=id)
    try:
        objeto = Libro.objects.get(id = id)
    except Libro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': #leer
        serializer = LibroSerializers(objeto)
        return Response(serializer.data)

    elif request.method == 'DELETE': # eliminar
        objeto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT': # modificar
        serializer = LibroSerializers(objeto, data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

        


    
    

    
    
# Create your views here.
