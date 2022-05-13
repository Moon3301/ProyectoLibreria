from django.conf.urls import include
from django.urls import path
from django.contrib import admin

from .views import *

urlpatterns = [
    path('listarLibro/',listarLibro, name= "listarLibro"),
    
]