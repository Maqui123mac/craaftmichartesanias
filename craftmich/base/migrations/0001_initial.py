# Generated by Django 5.0.6 on 2024-07-13 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('imagen', models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía')),
                ('producto', models.TextField(default='producto')),
                ('precio', models.PositiveIntegerField(default=0)),
                ('descripcion', models.TextField(default='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=25)),
                ('fecha', models.DateTimeField()),
                ('roles', models.CharField(choices=[('usuario', 'Usuario normal'), ('admin', 'Administrador')], default='usuario', max_length=7)),
            ],
        ),
    ]