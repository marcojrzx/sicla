from django.db import models

# Create your models here.

class Autor(model.Model):
	  nombre = models.TextField(max_length=45)
	  sexo = models.TextField(max_length=3) 
