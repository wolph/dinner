# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dinner'
        db.create_table('dinner_dinner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('price', self.gf('django.db.models.fields.DecimalField')(default='4', max_digits=8, decimal_places=2)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(default='2.3', max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'dinner', ['Dinner'])

        # Adding unique constraint on 'Dinner', fields ['date']
        db.create_unique('dinner_dinner', ['date'])

        # Adding M2M table for field cooks on 'Dinner'
        m2m_table_name = db.shorten_name('dinner_dinner_cooks')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dinner', models.ForeignKey(orm[u'dinner.dinner'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dinner_id', 'user_id'])

        # Adding M2M table for field courses on 'Dinner'
        m2m_table_name = db.shorten_name('dinner_dinner_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dinner', models.ForeignKey(orm[u'dinner.dinner'], null=False)),
            ('course', models.ForeignKey(orm[u'dinner.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dinner_id', 'course_id'])

        # Adding model 'Course'
        db.create_table('dinner_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('default', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'dinner', ['Course'])

        # Adding unique constraint on 'Course', fields ['name']
        db.create_unique('dinner_course', ['name'])

        # Adding model 'Reservation'
        db.create_table('dinner_reservation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('allergies', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('dinner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dinner.Dinner'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dinner.Course'])),
            ('paid', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=8, decimal_places=2)),
            ('discount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'dinner', ['Reservation'])


    def backwards(self, orm):
        # Removing unique constraint on 'Course', fields ['name']
        db.delete_unique('dinner_course', ['name'])

        # Removing unique constraint on 'Dinner', fields ['date']
        db.delete_unique('dinner_dinner', ['date'])

        # Deleting model 'Dinner'
        db.delete_table('dinner_dinner')

        # Removing M2M table for field cooks on 'Dinner'
        db.delete_table(db.shorten_name('dinner_dinner_cooks'))

        # Removing M2M table for field courses on 'Dinner'
        db.delete_table(db.shorten_name('dinner_dinner_courses'))

        # Deleting model 'Course'
        db.delete_table('dinner_course')

        # Deleting model 'Reservation'
        db.delete_table('dinner_reservation')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dinner.course': {
            'Meta': {'unique_together': "(('name',),)", 'object_name': 'Course'},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dinner.dinner': {
            'Meta': {'ordering': "['date']", 'unique_together': "(('date',),)", 'object_name': 'Dinner'},
            'cooks': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'default': "'2.3'", 'max_digits': '8', 'decimal_places': '2'}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dinner'", 'symmetrical': 'False', 'to': u"orm['dinner.Course']"}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': "'4'", 'max_digits': '8', 'decimal_places': '2'})
        },
        u'dinner.reservation': {
            'Meta': {'ordering': "['dinner__date']", 'object_name': 'Reservation'},
            'allergies': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dinner.Course']"}),
            'dinner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dinner.Dinner']"}),
            'discount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'paid': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dinner']