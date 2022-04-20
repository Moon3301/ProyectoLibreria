from django.shortcuts import render, redirect
from .models import *
from .forms import *

def inicio (request):
    return render (request, 'index.html')


# Create your views here.
