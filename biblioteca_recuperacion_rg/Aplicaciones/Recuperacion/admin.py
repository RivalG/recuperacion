from django.contrib import admin
from .models import Genero, Libro, Autor, Profesion

admin.site.register(Genero)
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Profesion)
