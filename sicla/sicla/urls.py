from django.conf.urls import patterns, include, url

from django.contrib import admin
from tastypie.api import Api
from logica.api.resources import AutorResource

admin.autodiscover()

autor_resource = AutorResource()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'sicla.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(autor_resource.urls)),

)
