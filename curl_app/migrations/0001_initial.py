# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'urls'
        db.create_table('curl_app_urls', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('curl_app', ['urls'])

        # Adding model 'count'
        db.create_table('curl_app_count', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('counter', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('curl_app', ['count'])


    def backwards(self, orm):
        # Deleting model 'urls'
        db.delete_table('curl_app_urls')

        # Deleting model 'count'
        db.delete_table('curl_app_count')


    models = {
        'curl_app.count': {
            'Meta': {'object_name': 'count'},
            'counter': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'curl_app.urls': {
            'Meta': {'object_name': 'urls'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['curl_app']