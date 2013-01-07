from principal.models import Producto
from principal.models import Proveedor
from principal.models import Cliente
from principal.models import Personal
from principal.models import Proveedor_Producto
from principal.models import Factura
from principal.models import Detalle


from django.contrib import admin

admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Personal)
admin.site.register(Proveedor_Producto)
admin.site.register(Factura)
admin.site.register(Detalle)