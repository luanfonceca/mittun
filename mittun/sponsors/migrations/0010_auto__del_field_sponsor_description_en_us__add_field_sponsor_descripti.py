# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Sponsor.description_en'
        db.delete_column('sponsors_sponsor', 'description_en')

        # Adding field 'Sponsor.description_en'
        db.add_column('sponsors_sponsor', 'description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Changing field 'Sponsor.description_pt_br'
        db.alter_column('sponsors_sponsor', 'description_pt_br', self.gf('django.db.models.fields.TextField')(default=''))

        # Deleting field 'Category.name_en'
        db.delete_column('sponsors_category', 'name_en')

        # Adding field 'Category.name_en'
        db.add_column('sponsors_category', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True), keep_default=False)

        # Adding field 'Category.priority'
        db.add_column('sponsors_category', 'priority', self.gf('django.db.models.fields.IntegerField')(default=''), keep_default=False)

        # Changing field 'Category.name_pt_br'
        db.alter_column('sponsors_category', 'name_pt_br', self.gf('django.db.models.fields.CharField')(default='', max_length=120))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Sponsor.description_en'
        raise RuntimeError("Cannot reverse this migration. 'Sponsor.description_en' and its values cannot be restored.")

        # Deleting field 'Sponsor.description_en'
        db.delete_column('sponsors_sponsor', 'description_en')

        # Changing field 'Sponsor.description_pt_br'
        db.alter_column('sponsors_sponsor', 'description_pt_br', self.gf('django.db.models.fields.TextField')(null=True))

        # User chose to not deal with backwards NULL issues for 'Category.name_en'
        raise RuntimeError("Cannot reverse this migration. 'Category.name_en' and its values cannot be restored.")

        # Deleting field 'Category.name_en'
        db.delete_column('sponsors_category', 'name_en')

        # Deleting field 'Category.priority'
        db.delete_column('sponsors_category', 'priority')

        # Changing field 'Category.name_pt_br'
        db.alter_column('sponsors_category', 'name_pt_br', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 11, 6, 33, 4, 21526)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 11, 6, 33, 4, 21400)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sponsors.bonus': {
            'Meta': {'object_name': 'Bonus'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sponsors.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'name_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'priority': ('django.db.models.fields.IntegerField', [], {})
        },
        'sponsors.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Sponsor']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sponsors.job': {
            'Meta': {'object_name': 'Job'},
            'bonuses': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Bonus']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Sponsor']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'requirements': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Requirement']"}),
            'responsabilities': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Responsibility']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'web_site': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'sponsors.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sponsors.responsibility': {
            'Meta': {'object_name': 'Responsibility'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sponsors.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Category']"}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_pt_br': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sponsors']
