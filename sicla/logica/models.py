#enconding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Autor(models.Model):
	nombre = models.TextField(max_length=45)
	sexo = models.CharField(max_length=2) 

def __unicode__(self):
   	return self.nombre

class Articulo(models.Model):
  autor = models.ForeignKey(Autor)
  articulo = models.TextField(max_length=10000)

def __unicode__(self):
     return self.articulo
