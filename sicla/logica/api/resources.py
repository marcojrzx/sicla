from tastypie.resources import ModelResource
from logica.models import Autor, Articulo

class AutorResource(ModelResource):
 class Meta:
  queryset = Autor.objects.all()
  allowed_methods = ['get']
                                                                                                                                      

class ArticuloResource(ModelResource):
 class  Meta:
  queryset = Articulo.objects.all()
  allowed_methods = ['get']	
  		  
	