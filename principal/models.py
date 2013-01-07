from django.db import models

class Proveedor(models.Model):

	nombre = models.CharField(max_length=50)
	ruc = models.CharField(max_length=11)
	direccion = models.CharField(max_length=40, null=True, blank=True)

	def __unicode__(self):
		return self.nombre

class Personal(models.Model):	
	
	nombre = models.CharField(max_length=50)
	dni = models.CharField(max_length=8)
	categoria = models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre

class Cliente(models.Model):
	
	nombre	= models.CharField(max_length=50)
	direccion = models.CharField(max_length=40)
	dni = models.CharField(max_length=8)

	def __unicode__(self):
		return self.nombre

class Producto(models.Model):
	
	nombre	= models.CharField(max_length=50)
	descripcion = models.CharField(max_length=70)
	precio = models.FloatField()
	cantidad = models.IntegerField()

	def __unicode__(self):
		return self.nombre

class Proveedor_Producto(models.Model):
	
	fecha = models.DateField(auto_now=True)

	proveedor = models.ForeignKey(Proveedor)
	producto = models.ForeignKey(Producto)

	def __unicode__(self):
		return '%s con %s'%(self.proveedor, self.producto) 


class Factura(models.Model):
	numero = models.CharField(max_length=10)
	
	def __unicode__(self):
		return self.numero			

class Detalle(models.Model):

	precio = models.FloatField()
	cantidad = models.IntegerField()
	fecha = models.DateField(auto_now=True)
	producto = models.ForeignKey(Producto)
	cliente = models.ForeignKey(Cliente)
	personal = models.ForeignKey(Personal)
	factura = models.ForeignKey(Factura)

	def __unicode__(self):
		return '%s de %s'%(self.cliente, self.personal)