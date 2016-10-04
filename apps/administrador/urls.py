from django.conf.urls import patterns, include, url
from apps.administrador.views import index

urlpatterns = patterns('',
   
    url(r'^$', index),
  

)
