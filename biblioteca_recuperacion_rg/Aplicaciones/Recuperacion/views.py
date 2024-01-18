from django.shortcuts import render, redirect
from .models import Genero, Libro, Autor, Profesion
from django.contrib import messages



def listarGeneros(request):
    generos = Genero.objects.all()
    return render(request, 'generos.html', {'generos': generos})

def guardarGenero(request):
    if request.method == 'POST':
        nombre_rg = request.POST.get('nombre_rg')
        descripcion_rg = request.POST.get('descripcion_rg')
        fotografia = request.FILES.get('fotografia')

        # Realiza la validación que consideres necesaria antes de guardar
        if nombre_rg and descripcion_rg:
            genero = Genero(nombre_rg=nombre_rg,
            descripcion_rg=descripcion_rg,
            fotografia=fotografia)
            genero.save()
            messages.success(request, 'Género guardado exitosamente.')
        else:
            messages.error(request, 'Error al guardar el género. Por favor, complete los campos obligatorios.')

        return redirect('listarGeneros')  # Ajusta el nombre de la URL según tus necesidades

    generos = Genero.objects.all()
    return render(request, 'generos.html', {'generos': generos})


def editarGenero(request, id_rg):
    try:
        genero = Genero.objects.get(id_rg=id_rg)
    except Genero.DoesNotExist:
        # Manejar el caso en el que el genero no existe
        messages.error(request, 'El género no existe.')
        return redirect('listarGeneros')

    if request.method == 'POST':
        # Procesar los datos del formulario directamente
        nombre_rg = request.POST.get('nombre_rg')
        descripcion_rg = request.POST.get('descripcion_rg')
        # Puedes agregar aquí la lógica de validación necesaria

        # Actualizar el objeto Genero con los nuevos datos
        genero.nombre_rg = nombre_rg
        genero.descripcion_rg = descripcion_rg
        genero.save()

        messages.success(request, 'Género editado exitosamente.')
        return redirect('listarGeneros')

    return render(request, 'editarGenero.html', {'genero': genero})



def eliminarGenero(request, id_rg):
    try:
        genero = Genero.objects.get(id_rg=id_rg)
        genero.delete()
        messages.success(request, 'Género eliminado exitosamente.')
    except Genero.DoesNotExist:
        messages.error(request, 'El género que intenta eliminar no existe.')

    return redirect('listarGeneros')  # Ajusta el nombre de la URL según tus necesidades


def actualizarGenero(request, id_rg):
    try:
        # Intenta obtener la instancia del Genero
        genero = Genero.objects.get(id_rg=id_rg)
    except Genero.DoesNotExist:
        # Si no se encuentra el Genero, redirige o maneja la situación según tus necesidades
        messages.error(request, 'El género no existe.')
        return redirect('listarGeneros')

    if request.method == 'POST':
        # Actualiza los campos directamente
        genero.nombre_rg = request.POST.get('nombre_rg')
        genero.descripcion_rg = request.POST.get('descripcion_rg')
        genero.fotografia = request.FILES.get('fotografia')

        # Guarda los cambios
        genero.save()

        messages.success(request, 'Género actualizado exitosamente.')
        return redirect('listarGeneros')

    return render(request, 'editarGenero.html', {'genero': genero})


def listarLibros(request):
    libros = Libro.objects.all()
    generos = Genero.objects.all()
    return render(request, 'libros.html', {'libros': libros, 'generos': generos})

def guardarLibro(request):
    if request.method == 'POST':
        titulo_rg = request.POST.get('titulo_rg')
        editorial_rg = request.POST.get('editorial_rg')
        fecha_rg = request.POST.get('fecha_rg')
        genero_id = request.POST.get('genero_id')
        fotografia = request.FILES.get('fotografia')

        # Realiza la validación que consideres necesaria antes de guardar
        if titulo_rg and editorial_rg and fecha_rg and genero_id:
            libro = Libro(
                titulo_rg=titulo_rg,
                editorial_rg=editorial_rg,
                fecha_rg=fecha_rg,
                genero_id=genero_id,
                fotografia=fotografia
            )
            libro.save()
            messages.success(request, 'Libro guardado exitosamente.')
        else:
            messages.error(request, 'Error al guardar el libro. Por favor, complete los campos obligatorios.')

        return redirect('listarLibros')  # Ajusta el nombre de la URL según tus necesidades

    libros = Libro.objects.all()
    return render(request, 'libros.html', {'libros': libros})


def editarLibro(request, id_rg):
    try:
        libro = Libro.objects.get(id_rg=id_rg)
    except Libro.DoesNotExist:
        messages.error(request, 'El libro no existe.')
        return redirect('listarLibros')

    if request.method == 'POST':
        # Procesar los datos del formulario directamente
        titulo_rg = request.POST.get('titulo_rg')
        editorial_rg = request.POST.get('editorial_rg')
        fecha_rg = request.POST.get('fecha_rg')
        genero_id = request.POST.get('genero_id')  # Asegúrate de usar 'genero_id' aquí
        fotografia = request.FILES.get('fotografia')

        # Puedes agregar aquí la lógica de validación necesaria

        # Actualizar el objeto Libro con los nuevos datos
        libro.titulo_rg = titulo_rg
        libro.editorial_rg = editorial_rg
        libro.fecha_rg = fecha_rg
        libro.genero_id = genero_id
        libro.fotografia = fotografia
        libro.save()

        messages.success(request, 'Libro editado exitosamente.')
        return redirect('listarLibros')

    generos = Genero.objects.all()
    return render(request, 'editarLibro.html', {'libro': libro, 'generos': generos})



def actualizarLibro(request, id_rg):
    try:
        # Intenta obtener la instancia del Libro
        libro = Libro.objects.get(id_rg=id_rg)
    except Libro.DoesNotExist:
        # Si no se encuentra el Libro, redirige o maneja la situación según tus necesidades
        messages.error(request, 'El libro no existe.')
        return redirect('listarLibros')

    if request.method == 'POST':
        # Actualiza los campos directamente
        libro.titulo_rg = request.POST.get('titulo_rg')
        libro.editorial_rg = request.POST.get('editorial_rg')
        libro.fecha_rg = request.POST.get('fecha_rg')

        # Actualiza el genero solo si se proporciona un ID válido
        genero_id = request.POST.get('genero')
        if genero_id:
            try:
                genero = Genero.objects.get(id_rg=genero_id)
                libro.genero = genero
            except Genero.DoesNotExist:
                # Manejar la situación en la que el genero no existe
                messages.error(request, 'El género no existe.')
                return redirect('listarLibros')

        libro.fotografia = request.FILES.get('fotografia')

        # Guarda los cambios
        libro.save()

        messages.success(request, 'Libro actualizado exitosamente.')
        return redirect('listarLibros')

    # Obtén la lista de géneros para pasarla al formulario
    generos = Genero.objects.all()
    return render(request, 'editarLibro.html', {'libro': libro, 'generos': generos})




def eliminarLibro(request, id_rg):
    try:
        libro = Libro.objects.get(id_rg=id_rg)
        libro.delete()
        messages.success(request, 'Libro eliminado exitosamente.')
    except Libro.DoesNotExist:
        messages.error(request, 'El libro que intenta eliminar no existe.')

    return redirect('listarLibros')  # Ajusta el nombre de la URL según tus necesidades





def listadoAutores(request):
    libros = Libro.objects.all()
    autores = Autor.objects.all()
    return render(request, 'autores.html', {'autores': autores, 'libros': libros})


def guardarAutor(request):
    if request.method == 'POST':
        apellido_rg = request.POST.get('apellido_rg')
        nombre_rg = request.POST.get('nombre_rg')
        edad_rg = request.POST.get('edad_rg')
        libros_ids = request.POST.getlist('libros_autor')  # Actualiza aquí al nombre correcto
        pdf_documento = request.FILES.get('pdf_documento')

        # Realiza la validación que consideres necesaria antes de guardar
        if apellido_rg and nombre_rg and edad_rg and libros_ids:
            autor = Autor(
                apellido_rg=apellido_rg,
                nombre_rg=nombre_rg,
                edad_rg=edad_rg,
                pdf_documento=pdf_documento
            )
            autor.save()
            autor.libros.set(libros_ids)  # Asigna los libros al autor
            messages.success(request, 'Autor guardado exitosamente.')
        else:
            messages.error(request, 'Error al guardar el autor. Por favor, complete los campos obligatorios.')

        return redirect('listadoAutores')  # Ajusta el nombre de la URL según tus necesidades

    autores = Autor.objects.all()
    return render(request, 'autores.html', {'autores': autores})

def editarAutor(request, id_rg):
    try:
        autor = Autor.objects.get(id_rg=id_rg)
    except Autor.DoesNotExist:
        messages.error(request, 'El autor no existe.')
        return redirect('listadoAutores')

    if request.method == 'POST':
        # Procesar los datos del formulario directamente
        apellido_rg = request.POST.get('apellido_rg')
        nombre_rg = request.POST.get('nombre_rg')
        edad_rg = request.POST.get('edad_rg')
        libros_ids = request.POST.getlist('libros_ids[]')
        pdf_documento = request.FILES.get('pdf_documento')

        # Puedes agregar aquí la lógica de validación necesaria

        # Actualizar el objeto Autor con los nuevos datos
        autor.apellido_rg = apellido_rg
        autor.nombre_rg = nombre_rg
        autor.edad_rg = edad_rg
        autor.pdf_documento = pdf_documento
        autor.save()
        autor.libros.set(libros_ids)  # Actualiza los libros del autor

        messages.success(request, 'Autor editado exitosamente.')
        return redirect('listadoAutores')

    # Obtén la lista de libros para pasarla al formulario
    libros = Libro.objects.all()
    return render(request, 'editarAutor.html', {'autor': autor, 'libros': libros})

def actualizarAutor(request, id_rg):
    try:
        # Intenta obtener la instancia del Autor
        autor = Autor.objects.get(id_rg=id_rg)
    except Autor.DoesNotExist:
        # Si no se encuentra el Autor, redirige o maneja la situación según tus necesidades
        messages.error(request, 'El autor no existe.')
        return redirect('listadoAutores')

    if request.method == 'POST':
        # Actualiza los campos directamente
        autor.apellido_rg = request.POST.get('apellido_rg')
        autor.nombre_rg = request.POST.get('nombre_rg')
        autor.edad_rg = request.POST.get('edad_rg')
        autor.pdf_documento = request.FILES.get('pdf_documento')

        # Guarda los cambios
        autor.save()

        # Puedes agregar la lógica de actualización de libros si es necesario
        libros_ids = request.POST.getlist('libros_ids[]')
        autor.libros.set(libros_ids)  # Actualiza los libros del autor

        messages.success(request, 'Autor actualizado exitosamente.')
        return redirect('listadoAutores')

    # Obtén la lista de libros para pasarla al formulario
    libros = Libro.objects.all()
    return render(request, 'editarAutor.html', {'autor': autor, 'libros': libros})

def eliminarAutor(request, id_rg):
    try:
        autor = Autor.objects.get(id_rg=id_rg)
        autor.delete()
        messages.success(request, 'Autor eliminado exitosamente.')
    except Autor.DoesNotExist:
        messages.error(request, 'El autor que intenta eliminar no existe.')

    return redirect('listadoAutores')  # Ajusta el nombre de la URL según tus necesidades



def listadoProfesiones(request):
    profesiones = Profesion.objects.all()
    autores_disponibles = Autor.objects.all()   # Agrega esta línea para obtener la lista de autores
    return render(request, 'profesiones.html', {'profesiones': profesiones, 'autores_disponibles': autores_disponibles})


def guardarProfesion(request):
    if request.method == 'POST':
        nombre_rg = request.POST.get('nombre_rg')
        descripcion_rg = request.POST.get('descripcion_rg')
        autores_ids = request.POST.getlist('autores_ids[]')

        # Realiza la validación que consideres necesaria antes de guardar
        if nombre_rg and descripcion_rg and autores_ids:
            profesion = Profesion(
                nombre_rg=nombre_rg,
                descripcion_rg=descripcion_rg
            )
            profesion.save()
            profesion.autores.set(autores_ids)  # Asigna los autores a la profesión
            messages.success(request, 'Profesión guardada exitosamente.')
        else:
            messages.error(request, 'Error al guardar la profesión. Por favor, complete los campos obligatorios.')

        return redirect('listadoProfesiones')  # Ajusta el nombre de la URL según tus necesidades

    profesiones = Profesion.objects.all()
    return render(request, 'profesiones.html', {'profesiones': profesiones})


def editarProfesion(request, id_rg):
    try:
        profesion = Profesion.objects.get(id_rg=id_rg)
    except Profesion.DoesNotExist:
        messages.error(request, 'La profesión no existe.')
        return redirect('listadoProfesiones')

    if request.method == 'POST':
        # Procesar los datos del formulario directamente
        nombre_rg = request.POST.get('nombre_rg')
        descripcion_rg = request.POST.get('descripcion_rg')
        autores_ids = request.POST.getlist('autores_ids[]')

        # Puedes agregar aquí la lógica de validación necesaria

        # Actualizar el objeto Profesion con los nuevos datos
        profesion.nombre_rg = nombre_rg
        profesion.descripcion_rg = descripcion_rg
        profesion.save()
        profesion.autores.set(autores_ids)  # Actualiza los autores de la profesión

        messages.success(request, 'Profesión editada exitosamente.')
        return redirect('listadoProfesiones')

    # Obtén la lista de autores para pasarla al formulario
    autores_disponibles = Autor.objects.all()
    return render(request, 'editarProfesion.html', {'profesion': profesion, 'autores_disponibles': autores_disponibles})



def actualizarProfesion(request, id_rg):
    try:
        # Intenta obtener la instancia de la Profesion
        profesion = Profesion.objects.get(id_rg=id_rg)
    except Profesion.DoesNotExist:
        # Si no se encuentra la Profesion, redirige o maneja la situación según tus necesidades
        messages.error(request, 'La profesión no existe.')
        return redirect('listadoProfesiones')

    if request.method == 'POST':
        # Actualiza los campos directamente
        nombre_rg = request.POST.get('nombre_rg')
        descripcion_rg = request.POST.get('descripcion_rg')
        autores_ids = request.POST.getlist('autores_ids[]')

        # Actualiza los datos de la Profesion
        profesion.nombre_rg = nombre_rg
        profesion.descripcion_rg = descripcion_rg
        profesion.save()
        profesion.autores.set(autores_ids)  # Actualiza los autores de la profesión

        messages.success(request, 'Profesión actualizada exitosamente.')
        return redirect('listadoProfesiones')

    # Obtén la lista de autores para pasarla al formulario
    autores_disponibles = Autor.objects.all()
    return render(request, 'editarProfesion.html', {'profesion': profesion, 'autores_disponibles': autores_disponibles})


def eliminarProfesion(request, id_rg):
    try:
        profesion = Profesion.objects.get(id_rg=id_rg)
        profesion.delete()
        messages.success(request, 'Profesión eliminada exitosamente.')
    except Profesion.DoesNotExist:
        messages.error(request, 'La profesión que intenta eliminar no existe.')

    return redirect('listadoProfesiones')  # Ajusta el nombre de la URL según tus necesidades
