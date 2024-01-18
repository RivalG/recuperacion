from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarGeneros, name='listarGeneros'),
    path('listarGeneros/', views.listarGeneros, name='listarGeneros'),
    path('guardarGenero/', views.guardarGenero, name='guardarGenero'),
    path('editarGenero/<int:id_rg>/', views.editarGenero, name='editarGenero'),
    path('eliminarGenero/<int:id_rg>/', views.eliminarGenero, name='eliminarGenero'),
    path('actualizarGenero/<int:id_rg>/', views.actualizarGenero, name='actualizarGenero'),

    path('libros/', views.listarLibros, name='listarLibros'),
    path('guardarLibro/', views.guardarLibro, name='guardarLibro'),
    path('editarLibro/<int:id_rg>/', views.editarLibro, name='editarLibro'),
    path('eliminarLibro/<int:id_rg>/', views.eliminarLibro, name='eliminarLibro'),
    path('actualizarLibro/<int:id_rg>/', views.actualizarLibro, name='actualizarLibro'),


    path('listadoAutores/', views.listadoAutores, name='listadoAutores'),
    path('guardarAutor/', views.guardarAutor, name='guardarAutor'),
    path('editarAutor/<int:id_rg>/', views.editarAutor, name='editarAutor'),
    path('actualizarAutor/<int:id_rg>/', views.actualizarAutor, name='actualizarAutor'),
    path('eliminarAutor/<int:id_rg>/', views.eliminarAutor, name='eliminarAutor'),


    path('listadoProfesiones/', views.listadoProfesiones, name='listadoProfesiones'),
    path('guardarProfesion/', views.guardarProfesion, name='guardarProfesion'),
    path('editarProfesion/<int:id_rg>/', views.editarProfesion, name='editarProfesion'),
    path('eliminarProfesion/<int:id_rg>/', views.eliminarProfesion, name='eliminarProfesion'),
    path('actualizarProfesion/<int:id_rg>/', views.actualizarProfesion, name='actualizarProfesion'),  # Agrega esta línea
]
