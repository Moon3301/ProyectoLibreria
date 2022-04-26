from django import forms
from django.db import models
from .models import *

class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = '__all__'