from django.db import models

# Create your models here.

class Datos(models.Model):
	"""datos del restaurant"""
	dueno = models.ForeignKey('usuarios.Restaurante')
	nombre = models.CharField(max_length=30)
	direccion = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	imagen = models.ImageField()
	telefono = models.CharField(max_length=10)
	calificacion = models.CharField(max_length=10)
	tipo = models.CharField(max_length=10)


class Platillos(models.Model):
	"""datos de platillos"""
	restaurante = models.ForeignKey(Datos)
	nombre = models.CharField(max_length=30)
	imagen = models.ImageField()
	calificacion = models.CharField(max_length=10)
	tipo = models.CharField(max_length=10)
	precio = models.IntegerField()

class Cosas(models.Model):
	"""datos de cosas"""
	_id = models.ForeignKey('usuarios.Orden')
	platillo = models.ForeignKey(Platillos, related_name='platillos')
	precio = models.ForeignKey(Platillos, related_name='precios')
	cantidad = models.IntegerField()
