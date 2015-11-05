# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pago', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_id', models.CharField(max_length=30)),
                ('lugar_entrega', models.CharField(max_length=30)),
                ('precio_total', models.IntegerField()),
                ('tipo', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(to='usuarios.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servicio', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('edad', models.CharField(max_length=2)),
                ('imagen', models.ImageField(upload_to=b'')),
                ('password', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=10)),
                ('celular', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='restaurante',
            name='usuario_restaurant',
            field=models.ForeignKey(to='usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario_cliente',
            field=models.ForeignKey(to='usuarios.Usuario'),
        ),
    ]
