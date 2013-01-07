from principal.models import Producto, Proveedor, Cliente, Personal, Proveedor_Producto,Factura, Detalle 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404

def detalle_factura(request):
	detalle = Detalle.objects.all()	
	facturas = Factura.objects.all()
	dato_=1
	return render_to_response('reporte.html',{'detalle':detalle,'facturas':facturas})
