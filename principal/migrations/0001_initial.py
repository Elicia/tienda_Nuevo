# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Proveedor'
        db.create_table('principal_proveedor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ruc', self.gf('django.db.models.fields.CharField')(max_length=11)),
        ))
        db.send_create_signal('principal', ['Proveedor'])

        # Adding model 'Personal'
        db.create_table('principal_personal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('principal', ['Personal'])

        # Adding model 'Cliente'
        db.create_table('principal_cliente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('principal', ['Cliente'])

        # Adding model 'Producto'
        db.create_table('principal_producto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('principal', ['Producto'])

        # Adding model 'Proveedor_Producto'
        db.create_table('principal_proveedor_producto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Proveedor'])),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Producto'])),
        ))
        db.send_create_signal('principal', ['Proveedor_Producto'])

        # Adding model 'Factura'
        db.create_table('principal_factura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('principal', ['Factura'])

        # Adding model 'Detalle'
        db.create_table('principal_detalle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Producto'])),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Cliente'])),
            ('personal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Personal'])),
            ('factura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Factura'])),
        ))
        db.send_create_signal('principal', ['Detalle'])


    def backwards(self, orm):
        # Deleting model 'Proveedor'
        db.delete_table('principal_proveedor')

        # Deleting model 'Personal'
        db.delete_table('principal_personal')

        # Deleting model 'Cliente'
        db.delete_table('principal_cliente')

        # Deleting model 'Producto'
        db.delete_table('principal_producto')

        # Deleting model 'Proveedor_Producto'
        db.delete_table('principal_proveedor_producto')

        # Deleting model 'Factura'
        db.delete_table('principal_factura')

        # Deleting model 'Detalle'
        db.delete_table('principal_detalle')


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