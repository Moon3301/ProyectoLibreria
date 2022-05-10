from django.contrib import admin
from .models import Cliente, Libro, Tienda, CategoriaLibro
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Libro)
admin.site.register(Tienda)
admin.site.register(CategoriaLibro)