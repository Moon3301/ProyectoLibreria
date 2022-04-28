from django import contrib
from django import urls
from django.urls import path 
from django.contrib import admin
from django.urls.conf import include
from .views import *


urlpatterns = [

    path('inicio',inicio ,name = "inicio"),
    path('listarLibros',listarLibros, name = "listarLibros"),
    path('detalleLibros/<id>', detalleLibros, name="detalleLibros"),
    path('formCompra', formCompra, name="formCompra"),

]