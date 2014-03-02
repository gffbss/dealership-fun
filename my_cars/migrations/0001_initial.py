# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Car'
        db.create_table(u'my_cars_car', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('horsepower', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('transmission', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'my_cars', ['Car'])


    def backwards(self, orm):
        # Deleting model 'Car'
        db.delete_table(u'my_cars_car')


    models = {
        u'my_cars.car': {
            'Meta': {'object_name': 'Car'},
            'horsepower': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'transmission': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['my_cars']