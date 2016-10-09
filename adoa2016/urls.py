from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adoa2016.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^administrador/',   include('apps.administrador.urls',  namespace = 'administrador')),
    url(r'^usuario/',         include('apps.usuario.urls',        namespace = 'usuario')),
    url(r'^',                 include('apps.principal.urls',      namespace = 'principal')),
 	url(r'^adoa/',                 include('apps.principal.urls',      namespace = 'principal_adoa')),












)
