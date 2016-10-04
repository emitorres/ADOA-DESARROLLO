from django.conf.urls import patterns, include, url
from apps.usuario.views import usuario_index,registro, iniciarSesion,perfil_index, perfil_editar,usuario_salir,usuario_acceso_denegado

urlpatterns = patterns('',
    url(r'^index/$', usuario_index, name = 'usuario_index'),
    url(r'^registrarse/$', registro, name = 'usuario_registro'),
    url(r'^iniciar_sesion/$', iniciarSesion, name = 'usuario_iniciarSesion'),
	url(r'^perfil/$', perfil_index, name = 'perfil_index'),
	url(r'^perfil/editar/(\d+)/', perfil_editar, name = 'perfil_editar'),
	url(r'^salir/', usuario_salir, name = 'usuario_salir'),
	url(r'^acceso_denegado/$', usuario_acceso_denegado, name = 'usuario_acceso_denegado'),

)
