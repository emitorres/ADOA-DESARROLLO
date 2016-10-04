from django.conf.urls import patterns, include, url
from apps.principal.views import index, index_adoa

urlpatterns = patterns('',
   
   url(r'^$', index, name = 'index'),

   url(r'^adoa/', index_adoa, name = 'index_adoa'),
  

)
