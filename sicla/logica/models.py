#enconding: utf-8
from django.db import models

class Autor(models.Model):
 nombre = models.TextField(max_length=45)
 sexo = models.CharField(max_length=2) 
 
 def __unicode__(self):
   return self.nombre	

class Articulo(models.Model):
 autor = models.ForeignKey(Autor)
 titulo = models.TextField(max_length=100)
 articulo = models.TextField(max_length=10000)

 def __unicode__(self):
  return self.titulo
