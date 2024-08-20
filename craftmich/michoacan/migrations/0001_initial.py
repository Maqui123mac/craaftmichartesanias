# Generated by Django 5.0.6 on 2024-07-13 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrearEvento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Evento')),
                ('nombre', models.TextField(verbose_name='Nombre del Evento')),
                ('fecha', models.DateField(verbose_name='Fecha del Evento')),
                ('hora', models.TimeField(verbose_name='Hora del Evento')),
                ('lugar', models.TextField(verbose_name='Lugar del Evento')),
                ('tipo', models.TextField(verbose_name='Tipo de Evento')),
                ('descripcion', models.TextField(verbose_name='Descripcion del Evento')),
                ('image', models.ImageField(blank=True, null=True, upload_to='evento_imagenes')),
            ],
            options={
                'verbose_name': 'Crear Evento',
                'verbose_name_plural': 'Crear Eventos',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('imagen', models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía')),
                ('evento', models.TextField(default='Eventos')),
                ('precio', models.PositiveIntegerField(default=0)),
                ('descripcion', models.TextField(default='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
                'ordering': ['-created'],
            },
        ),
    ]