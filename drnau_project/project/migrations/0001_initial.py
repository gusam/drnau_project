# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('project_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proj_name', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('proj_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('proj_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='project_user')),
            ('proj_description', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
        ))
        db.send_create_signal('project', ['Project'])

        # Adding model 'ShowTv'
        db.create_table('project_showtv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('st_channel', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('st_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('st_live', self.gf('django.db.models.fields.CharField')(default='2', max_length=1)),
        ))
        db.send_create_signal('project', ['ShowTv'])

        # Adding model 'Prototype'
        db.create_table('project_prototype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pro_proj_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'], related_name='prototype_project')),
            ('pro_version', self.gf('django.db.models.fields.IntegerField')()),
            ('pro_link_content', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('pro_sho_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.ShowTv'], related_name='prototype_showtv')),
            ('pro_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('pro_date_update', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('pro_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('pro_description', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
        ))
        db.send_create_signal('project', ['Prototype'])

        # Adding model 'Schedule'
        db.create_table('project_schedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sch_st_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.ShowTv'], related_name='schedule_showtv')),
            ('sch_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('project', ['Schedule'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('project_project')

        # Deleting model 'ShowTv'
        db.delete_table('project_showtv')

        # Deleting model 'Prototype'
        db.delete_table('project_prototype')

        # Deleting model 'Schedule'
        db.delete_table('project_schedule')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'project.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proj_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'proj_description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'proj_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'proj_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'project_user'"})
        },
        'project.prototype': {
            'Meta': {'object_name': 'Prototype'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pro_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'pro_date_update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pro_description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'pro_link_content': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pro_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pro_proj_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Project']", 'related_name': "'prototype_project'"}),
            'pro_sho_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.ShowTv']", 'related_name': "'prototype_showtv'"}),
            'pro_version': ('django.db.models.fields.IntegerField', [], {})
        },
        'project.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sch_st_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.ShowTv']", 'related_name': "'schedule_showtv'"}),
            'sch_time': ('django.db.models.fields.TimeField', [], {})
        },
        'project.showtv': {
            'Meta': {'object_name': 'ShowTv'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'st_channel': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'st_live': ('django.db.models.fields.CharField', [], {'default': "'2'", 'max_length': '1'}),
            'st_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['project']