# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Edition'
        db.create_table('website_showroom_edition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site_title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('html_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('site_subtitle', self.gf('django.db.models.fields.CharField')(max_length=125)),
            ('rss_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('rss_description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('facebook_url', self.gf('django.db.models.fields.CharField')(max_length=90, null=True, blank=True)),
            ('home_menu_title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('home_menu_color', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('home_menu_active_color', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('home_num_websites', self.gf('django.db.models.fields.IntegerField')()),
            ('footer_left', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('footer_right', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contact_title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('contact_html', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('website_showroom', ['Edition'])

        # Adding model 'Category'
        db.create_table('website_showroom_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('url_name', self.gf('django.db.models.fields.SlugField')(max_length=40)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('active_color', self.gf('django.db.models.fields.CharField')(max_length=7)),
        ))
        db.send_create_signal('website_showroom', ['Category'])

        # Adding model 'EditionCategory'
        db.create_table('website_showroom_editioncategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('edition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website_showroom.Edition'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website_showroom.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('url_name', self.gf('django.db.models.fields.SlugField')(max_length=40)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('website_showroom', ['EditionCategory'])

        # Adding model 'Website'
        db.create_table('website_showroom_website', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website_showroom.Category'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('screenshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('website_showroom', ['Website'])

        # Adding model 'EditionWebsite'
        db.create_table('website_showroom_editionwebsite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('edition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website_showroom.Edition'])),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website_showroom.Website'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('website_showroom', ['EditionWebsite'])


    def backwards(self, orm):
        # Deleting model 'Edition'
        db.delete_table('website_showroom_edition')

        # Deleting model 'Category'
        db.delete_table('website_showroom_category')

        # Deleting model 'EditionCategory'
        db.delete_table('website_showroom_editioncategory')

        # Deleting model 'Website'
        db.delete_table('website_showroom_website')

        # Deleting model 'EditionWebsite'
        db.delete_table('website_showroom_editionwebsite')


    models = {
        'website_showroom.category': {
            'Meta': {'object_name': 'Category'},
            'active_color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'url_name': ('django.db.models.fields.SlugField', [], {'max_length': '40'})
        },
        'website_showroom.edition': {
            'Meta': {'object_name': 'Edition'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact_html': ('django.db.models.fields.TextField', [], {}),
            'contact_title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'facebook_url': ('django.db.models.fields.CharField', [], {'max_length': '90', 'null': 'True', 'blank': 'True'}),
            'footer_left': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'footer_right': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'home_menu_active_color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'home_menu_color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'home_menu_title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'home_num_websites': ('django.db.models.fields.IntegerField', [], {}),
            'html_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'rss_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rss_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'site_subtitle': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'site_title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'website_showroom.editioncategory': {
            'Meta': {'object_name': 'EditionCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website_showroom.Category']"}),
            'edition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website_showroom.Edition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'url_name': ('django.db.models.fields.SlugField', [], {'max_length': '40'})
        },
        'website_showroom.editionwebsite': {
            'Meta': {'object_name': 'EditionWebsite'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'edition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website_showroom.Edition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website_showroom.Website']"})
        },
        'website_showroom.website': {
            'Meta': {'object_name': 'Website'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website_showroom.Category']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'screenshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        }
    }

    complete_apps = ['website_showroom']