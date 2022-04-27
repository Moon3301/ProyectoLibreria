from tkinter import Widget
from django import forms
from django.db import models
from .models import *

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'
        
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre', 'style':'margin-bottom:20px;'}))
    rut = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Rut', 'style':'margin-bottom:20px;'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion', 'style':'margin-bottom:20px;'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Correo', 'style':'margin-bottom:20px;'}))
    telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Telefono', 'style':'margin-bottom:20px;'}))

    # borrar nombre de los campos
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = ""
        self.fields['rut'].label = ""
        self.fields['direccion'].label = ""
        self.fields['correo'].label = ""
        self.fields['telefono'].label = ""

    # hacer un salto de linea en los campos

    