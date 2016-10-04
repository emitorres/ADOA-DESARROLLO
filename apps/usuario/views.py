from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from apps.usuario.forms import RegistroForm, IngresoForm,PerfilForm,PerfilIndexForm
from apps.usuario.models import Usuario
from django.http import HttpResponseRedirect

from apps.usuario.access import my_login_required


def usuario_index(request):
	return render_to_response('usuario/InicioSesion.html', locals(), context_instance = RequestContext(request))

def registro(request):
	valido = False
	ver_error = False
	msg_ok = 'Operacion Exitosa'
	msg_no = 'No se pudo realizar la operacion'
	lista_err = []

	try:
		usuario = Usuario.objects.get(id = registro)
	except:
		usuario = Usuario()

	if request.method == 'POST':
		formulario = RegistroForm(request.POST, instance = usuario)
		valido = formulario.is_valid()
		if valido:
			formulario.save()
			#return redirect('usuario:usuario_index')
			nombre = formulario.cleaned_data['nombre']
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append(field.label + ': ' + error)
	else:
		formulario = RegistroForm(instance = usuario)
	# locals() es un diccionario con todas las variables locales y sus valores
	return render_to_response('usuario/Registro.html', locals(), context_instance = RequestContext(request))

def iniciarSesion(request):
	valido = False
	ver_error = False
	msg_no  = 'Ingreso no valido'
	lista_err = []
	if request.method == 'POST':
		formulario = IngresoForm(request.POST)
		valido = formulario.is_valid()
		if valido:
			usuario = formulario.cleaned_data['usuario']
			clave = formulario.cleaned_data['clave']
			usrLog = Usuario.objects.login_ok(usuario, clave)
			if usrLog != None:
				request.session['usuario'] = usrLog
				return redirect('principal:index_adoa')
			else:
				ver_error = True
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append(field.label + ': ' + error)
	else:
		formulario = IngresoForm()

	return render_to_response('usuario/InicioSesion.html', locals(), context_instance = RequestContext(request))
@my_login_required
def perfil_index(request):

	id = request.session['usuario'].id
	usuario = Usuario.objects.get(id= id)

	
	return render_to_response('usuario/Perfil.html', locals(), context_instance = RequestContext(request))	
	
@my_login_required
def perfil_editar(request,registro):
	valido = False
	ver_error = False
	msg_ok = 'Operacion Exitosa'
	msg_no = 'No se pudo realizar la operacion'
	lista_err = []

	try:
		usuario = Usuario.objects.get(id = registro)
	except:
		usuario = Usuario()

	if request.method == 'POST':
		formulario = PerfilForm(request.POST, instance = usuario)
		valido = formulario.is_valid()
		if valido:
			formulario.save()
			#return redirect('usuario:usuario_index')
			#nombre = formulario.cleaned_data['nombre']
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append(field.label + ': ' + error)
	else:
		formulario = PerfilForm(instance = usuario)
	# locals() es un diccionario con todas las variables locales y sus valores
	return render_to_response('usuario/EditarPerfil.html', locals(), context_instance = RequestContext(request))
@my_login_required
def usuario_salir(request):
	del request.session['usuario']
	return HttpResponseRedirect('/')

def usuario_acceso_denegado(request):
	return render_to_response('usuario/acceso_denegado.html', locals(), context_instance = RequestContext(request))

