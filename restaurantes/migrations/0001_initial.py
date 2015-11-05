# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cosas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('_id', models.ForeignKey(to='usuarios.Orden')),
            ],
        ),
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('imagen', models.ImageField(upload_to=b'')),
                ('telefono', models.CharField(max_length=10)),
                ('calificacion', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=10)),
                ('dueno', models.ForeignKey(to='usuarios.Restaurante')),
            ],
        ),
        migrations.CreateModel(
            name='Platillos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('imagen', models.ImageField(upload_to=b'')),
                ('calificacion', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=10)),
                ('precio', models.IntegerField()),
                ('restaurante', models.ForeignKey(to='restaurantes.Datos')),
            ],
        ),
        migrations.AddField(
            model_name='cosas',
            name='platillo',
            field=models.ForeignKey(related_name='platillos', to='restaurantes.Platillos'),
        ),
        migrations.AddField(
            model_name='cosas',
            name='precio',
            field=models.ForeignKey(related_name='precios', to='restaurantes.Platillos'),
        ),
    ]
