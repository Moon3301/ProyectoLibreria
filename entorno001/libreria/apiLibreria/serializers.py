from rest_framework import serializers
from libreria.models import *


class LibroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TiendaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = '__all__'

class CategoriaLibroSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriaLibro
        fields = '__all__'