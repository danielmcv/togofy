from django.db import models

# Create your models here.

tipos_usuarios = (
	(CLIENTE, "cliente"),
	(RESTAURANT, "restaurant"),
)

class Usuario(models.Model):
	"""datos de los usuarios"""
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	email = models.EmailField(max_length=30, )
	edad = models.CharField(max_length=2)
	imagen = models.ImageField()
	password = models.CharField(max_length=15)
	telefono = models.CharField(max_length=10)
	celular = models.CharField(max_length=10)
	tipo = models.ChoiceField(opcion_chida1)

class Cliente(models.Model):
	"""datos de usuario cliente """
	usuario_cliente = models.ForeignKey(Usuario)
	pago = models.BooleanField(default=False)


class Restaurante(models.Model):
	"""datos de usuario restaurant """
	usuario_restaurant = models.ForeignKey(Usuario)
	servicio = models.BooleanField(default=False)

class Orden(models.Model):
	"""datos de  orden"""
	_id = models.CharField(max_length=30)
	cliente = models.ForeignKey(Cliente)
	lugar_entrega = models.CharField(max_length=30)
	precio_total = models.IntegerField()
	tipo = models.BooleanField(default=False)
