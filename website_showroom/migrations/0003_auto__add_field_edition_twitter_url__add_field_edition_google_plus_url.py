# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Edition.twitter_url'
        db.add_column('website_showroom_edition', 'twitter_url',
                      self.gf('django.db.models.fields.CharField')(max_length=90, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Edition.google_plus_url'
        db.add_column('website_showroom_edition', 'google_plus_url',
                      self.gf('django.db.models.fields.CharField')(max_length=90, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Edition.twitter_url'
        db.delete_column('website_showroom_edition', 'twitter_url')

        # Deleting field 'Edition.google_plus_url'
        db.delete_column('website_showroom_edition', 'google_plus_url')


    models = {
        'website_showroom.category': {
            'Meta': {'object_name': 'Category'},
            'active_color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
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
            'google_plus_url': ('django.db.models.fields.CharField', [], {'max_length': '90', 'null': 'True', 'blank': 'True'}),
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
            'site_title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'twitter_url': ('django.db.models.fields.CharField', [], {'max_length': '90', 'null': 'True', 'blank': 'True'})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'screenshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        }
    }

    complete_apps = ['website_showroom']