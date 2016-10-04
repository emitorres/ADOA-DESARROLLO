from django import forms
from apps.usuario.models import Usuario

class RegistroForm(forms.ModelForm):
	class Meta:
			model = Usuario

			fields = [
				'nombre',
				'apellido',
				'dni',
				'carrera',
				'email',
			]

			labels = {
				'nombre':'Nombre',
				'apellido':'Apellido',
				'dni':'DNI',
				'carrera':'Carrera',
				'email':'Email',
			}

			widgets = {
				'nombre':forms.TextInput(),
				'apellido':forms.TextInput(),
				'dni':forms.TextInput(),
				'carrera':forms.TextInput(),
				'email':forms.TextInput(),



			}

class IngresoForm(forms.Form):
	usuario = forms.CharField(error_messages = {'required': 'Debe ingresar un usuario'})
	clave   = forms.CharField(widget = forms.PasswordInput(),
							  error_messages = {'required': 'Debe ingresar una clave'})
	
class CambioPwdForm(forms.Form):
	actual = forms.CharField(widget = forms.PasswordInput(),
							 error_messages = {'required': 'Debe ingresar la clave actual'})
	nueva = forms.CharField(widget = forms.PasswordInput(),
							error_messages = {'required': 'Debe ingresar la clave nueva'})
	repetida = forms.CharField(widget = forms.PasswordInput(),
							   error_messages = {'required': 'Debe ingresar la clave repetida'})

	# Las validaciones para campos son clean_<nombre_campo>
	# Si el metodo se llama clean es para todos los campos juntos
	#validaciones propias
	def clean_repetida(self):
		nueva = self.cleaned_data.get('nueva')
		repetida = self.cleaned_data.get('repetida')
		if nueva != repetida:
			raise forms.ValidationError('Clave nueva y repetida deben ser iguales')
		return repetida			

class PerfilForm(forms.ModelForm):
	class Meta:
			model = Usuario

			fields = [
				'nombre',
				'apellido',
				'dni',
				'carrera',
			]

			labels = {
				'nombre':'Nombre',
				'apellido':'Apellido',
				'dni':'DNI',
				'carrera':'Carrera',
			}

			widgets = {
				'nombre':forms.TextInput(),
				'apellido':forms.TextInput(),
				'dni':forms.TextInput(),
				'carrera':forms.TextInput(),
			}

class PerfilIndexForm(forms.ModelForm):
	class Meta:
			model = Usuario

