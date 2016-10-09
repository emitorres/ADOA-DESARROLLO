from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from apps.usuario.access import my_login_required

def index(request):
	return render(request, 'inicio/index.html')
@my_login_required

def index_adoa(request):

	return render_to_response('adoa/AdoaBase.html', locals(), context_instance = RequestContext(request))