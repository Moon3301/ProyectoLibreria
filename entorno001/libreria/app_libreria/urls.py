from django import contrib
from django import urls
from django.urls import path 
from django.contrib import admin
from django.urls.conf import include
from .views import *


urlpatterns = [

    path('inicio',inicio ,name = "inicio"),
    path('libros',libros, name = "libros"),
    path('listarLibros',listarLibros, name = "listarLibros"),

]