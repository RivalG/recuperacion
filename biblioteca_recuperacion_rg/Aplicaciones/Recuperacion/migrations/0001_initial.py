# Generated by Django 4.2.7 on 2024-01-18 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_rg', models.AutoField(primary_key=True, serialize=False)),
                ('apellido_rg', models.CharField(max_length=255)),
                ('nombre_rg', models.CharField(max_length=255)),
                ('edad_rg', models.IntegerField()),
                ('pdf_documento', models.FileField(blank=True, null=True, upload_to='autores_pdfs')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_rg', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rg', models.CharField(max_length=255)),
                ('descripcion_rg', models.TextField()),
                ('fotografia', models.FileField(blank=True, null=True, upload_to='generos')),
            ],
        ),
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id_rg', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rg', models.CharField(max_length=255)),
                ('descripcion_rg', models.TextField()),
                ('autores', models.ManyToManyField(related_name='profesiones', to='Recuperacion.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_rg', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_rg', models.CharField(max_length=255)),
                ('editorial_rg', models.CharField(max_length=255)),
                ('fecha_rg', models.DateField()),
                ('fotografia', models.FileField(blank=True, null=True, upload_to='libros')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='Recuperacion.genero')),
            ],
        ),
        migrations.AddField(
            model_name='autor',
            name='libros',
            field=models.ManyToManyField(related_name='autores', to='Recuperacion.libro'),
        ),
    ]
