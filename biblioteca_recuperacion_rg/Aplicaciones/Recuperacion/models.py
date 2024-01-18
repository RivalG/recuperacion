from django.db import models

class Genero(models.Model):
    id_rg = models.AutoField(primary_key=True)
    nombre_rg = models.CharField(max_length=255)
    descripcion_rg = models.TextField()
    fotografia = models.FileField(upload_to='generos', null=True, blank=True)

    def __str__(self):
        return self.nombre_rg

class Libro(models.Model):
    id_rg = models.AutoField(primary_key=True)
    titulo_rg = models.CharField(max_length=255)
    editorial_rg = models.CharField(max_length=255)
    fecha_rg = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='libros')
    fotografia = models.FileField(upload_to='libros', null=True, blank=True)

    def __str__(self):
        return self.titulo_rg

class Autor(models.Model):
    id_rg = models.AutoField(primary_key=True)
    apellido_rg = models.CharField(max_length=255)
    nombre_rg = models.CharField(max_length=255)
    edad_rg = models.IntegerField()
    libros = models.ManyToManyField(Libro, related_name='autores')
    pdf_documento = models.FileField(upload_to='autores_pdfs', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_rg} {self.apellido_rg}"

class Profesion(models.Model):
    id_rg = models.AutoField(primary_key=True)
    nombre_rg = models.CharField(max_length=255)
    descripcion_rg = models.TextField()
    autores = models.ManyToManyField(Autor, related_name='profesiones')

    def __str__(self):
        return self.nombre_rg
