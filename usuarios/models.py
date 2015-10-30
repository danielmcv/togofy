from django.db import models

# Create your models here.

class Cliente(models.Model):
	"""datos de los clientes"""
		first_name = models.CharField(max_length=30)
		last_name = models.CharField(max_length=30)
		email = models.EmailField(max_length=30)
		edad = models.CharField(max_length=2)
		imagen= models.ImageField()


class Restaurante(models.Model):
	"""datos de usuario restaurant """
		name = models.CharField(max_length=30)
		

	
		
		

