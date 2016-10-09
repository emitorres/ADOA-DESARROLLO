from django.db import models

#--------------------------------------------------------------------------

class TipoUsuarioManager(models.Manager):
# Al heredar de Manager, en model se tiene al modelo actual

	def todos(self):
		return self.model.objects.all()

#---------------------------------------------------------------------------

class UsuarioManager(models.Manager):

	def todos(self):
		return self.model.objects.all()

	def login_ok(self, usuario, clave):
		try:
			existe = self.model.objects.get(email = usuario, clave = clave)
		except self.model.DoesNotExist:
			return None
		else:
			return existe

	def cambiar_clave(self, id, actual, nueva):
		usuario = self.model.objects.get(id = id)
		if usuario.clave != actual: return False
		usuario.clave = nueva
		usuario.save()
		return True
		
	def email_ok(self,email):
		try:
			existe = self.model.objects.get(email = email)
		except self.model.DoesNotExist:
			return None
		else:
			return existe


#--------------------------------------------------------------------------

class MenuManager(models.Manager):
# Al heredar de Manager, en model se tiene al modelo actual

	def todos(self):
		return self.model.objects.all()

#---------------------------------------------------------------------------

class MenuTipoUsuarioManager(models.Manager):
# Al heredar de Manager, en model se tiene al modelo actual

	def todos(self):
		return self.model.objects.all()

	def emi(self, idmenu, idtipo):
		try:
			existe = self.model.objects.get(menu_id = idmenu.id, tipousuario_id = idtipo.id)
		except self.model.DoesNotExist:
			return None
		else:
			return existe

#---------------------------------------------------------------------------