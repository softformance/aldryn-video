# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from ..utils import rename_tables_old_to_new, rename_tables_new_to_old

class Migration(SchemaMigration):

    def forwards(self, orm):
        rename_tables_old_to_new(db)
        # Adding field 'OEmbedVideoPlugin.use_lightbox'
        db.add_column('aldryn_video_oembedvideoplugin', 'use_lightbox',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        rename_tables_new_to_old(db)
        # Deleting field 'OEmbedVideoPlugin.use_lightbox'
        db.delete_column('cmsplugin_oembedvideoplugin', 'use_lightbox')


    models = {
        'aldryn_video.oembedvideoplugin': {
            'Meta': {'object_name': 'OEmbedVideoPlugin', 'db_table': "u'cmsplugin_oembedvideoplugin'", '_ormbases': ['cms.CMSPlugin']},
            'auto_play': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'loop_video': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '100'}),
            'use_lightbox': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        # XXX intellectronica 2015-11-02 The CMSPlugin fields level, lft,
        # rght and tree_id have been commented-out in order to allow this
        # migration to run in later versions of the CMS where they do not exist.
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            # 'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            # 'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            # 'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            # 'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['aldryn_video']
