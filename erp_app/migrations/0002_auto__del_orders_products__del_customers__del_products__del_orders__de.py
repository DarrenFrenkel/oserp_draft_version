# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Orders_Products'
        db.delete_table(u'erp_app_orders_products')

        # Deleting model 'Customers'
        db.delete_table(u'erp_app_customers')

        # Deleting model 'Products'
        db.delete_table(u'erp_app_products')

        # Deleting model 'Orders'
        db.delete_table(u'erp_app_orders')

        # Deleting model 'General_Settings'
        db.delete_table(u'erp_app_general_settings')

        # Adding model 'Customer'
        db.create_table(u'erp_app_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('print_on_check_as', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('billing_street', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('billing_city', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('billing_state', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('billing_zip', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('billing_country', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('shipping_street', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('shipping_city', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('shipping_state', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('shipping_zip', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('shipping_country', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('other_details', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
        ))
        db.send_create_signal(u'erp_app', ['Customer'])

        # Adding model 'Orders_Product'
        db.create_table(u'erp_app_orders_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp_app.Order'])),
            ('product_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp_app.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'erp_app', ['Orders_Product'])

        # Adding model 'General_Setting'
        db.create_table(u'erp_app_general_setting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'erp_app', ['General_Setting'])

        # Adding model 'Order'
        db.create_table(u'erp_app_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cust_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp_app.Customer'])),
            ('invoice_creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('delivery_due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('payment_due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('custom_message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'erp_app', ['Order'])

        # Adding model 'Product'
        db.create_table(u'erp_app_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
        ))
        db.send_create_signal(u'erp_app', ['Product'])


    def backwards(self, orm):
        # Adding model 'Orders_Products'
        db.create_table(u'erp_app_orders_products', (
            ('order_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp_app.Orders'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('product_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp_app.Products'])),
        ))
        db.send_create_signal(u'erp_app', ['Orders_Products'])

        # Adding model 'Customers'
        db.create_table(u'erp_app_customers', (
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('shipping_street', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('other_details', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('billing_street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('print_on_check_as', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('billing_country', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('shipping_city', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('shipping_state', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('billing_city', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('shipping_zip', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('billing_zip', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('shipping_country', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('billing_state', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'erp_app', ['Customers'])

        # Adding model 'Products'
        db.create_table(u'erp_app_products', (
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'erp_app', ['Products'])

        # Adding model 'Orders'
        db.create_table(u'erp_app_orders', (
            ('payment_due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('invoice_creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('cust_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp_app.Customers'])),
            ('custom_message', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('delivery_due_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'erp_app', ['Orders'])

        # Adding model 'General_Settings'
        db.create_table(u'erp_app_general_settings', (
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'erp_app', ['General_Settings'])

        # Deleting model 'Customer'
        db.delete_table(u'erp_app_customer')

        # Deleting model 'Orders_Product'
        db.delete_table(u'erp_app_orders_product')

        # Deleting model 'General_Setting'
        db.delete_table(u'erp_app_general_setting')

        # Deleting model 'Order'
        db.delete_table(u'erp_app_order')

        # Deleting model 'Product'
        db.delete_table(u'erp_app_product')


    models = {
        u'erp_app.customer': {
            'Meta': {'object_name': 'Customer'},
            'billing_city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'billing_country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'billing_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'billing_street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'billing_zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'other_details': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'print_on_check_as': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'shipping_city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'shipping_country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'shipping_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'shipping_street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'shipping_zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'erp_app.general_setting': {
            'Meta': {'object_name': 'General_Setting'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'erp_app.order': {
            'Meta': {'object_name': 'Order'},
            'cust_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp_app.Customer']"}),
            'custom_message': ('django.db.models.fields.TextField', [], {}),
            'delivery_due_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'payment_due_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'erp_app.orders_product': {
            'Meta': {'object_name': 'Orders_Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp_app.Order']"}),
            'product_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp_app.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'erp_app.product': {
            'Meta': {'object_name': 'Product'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'})
        }
    }

    complete_apps = ['erp_app']