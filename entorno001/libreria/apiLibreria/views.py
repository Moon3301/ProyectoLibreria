from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.serializers import Serializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework.authtoken.models import Token

from .serializers import *
from libreria.models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated

@csrf_exempt
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

# Create your views here.
