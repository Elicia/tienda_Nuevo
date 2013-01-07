# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Proveedor.direccion'
        db.add_column('principal_proveedor', 'direccion',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Proveedor.direccion'
        db.delete_column('principal_proveedor', 'direccion')


    models = {
        'principal.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'principal.detalle': {
            'Meta': {'object_name': 'Detalle'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Cliente']"}),
            'factura': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Factura']"}),
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'personal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Personal']"}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Producto']"})
        },
        'principal.factura': {
            'Meta': {'object_name': 'Factura'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'principal.personal': {
            'Meta': {'object_name': 'Personal'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'principal.producto': {
            'Meta': {'object_name': 'Producto'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precio': ('django.db.models.fields.FloatField', [], {})
        },
        'principal.proveedor': {
            'Meta': {'object_name': 'Proveedor'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ruc': ('django.db.models.fields.CharField', [], {'max_length': '11'})
        },
        'principal.proveedor_producto': {
            'Meta': {'object_name': 'Proveedor_Producto'},
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Producto']"}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Proveedor']"})
        }
    }

    complete_apps = ['principal']