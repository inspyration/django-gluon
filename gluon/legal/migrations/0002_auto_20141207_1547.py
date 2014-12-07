# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import saas.fields
from django.conf import settings
import base.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('legal', '0001_initial'),
        ('saas', '0001_initial'),
        ('util', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='instance',
            field=saas.fields.InstanceField(related_name='instance_legal_profile_set', verbose_name='instance', editable=False, to='saas.Instance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_modified_by',
            field=base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_legal_profile_set', editable=False, verbose_name='last modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='locale',
            field=models.ForeignKey(help_text='Profile Locale', verbose_name='locale', to='util.Locale'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='timezone',
            field=models.ForeignKey(help_text='Timezone', verbose_name='Profile timezone', to='util.TimeZone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(help_text='Address country', verbose_name='country', to='util.Country'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='created_by',
            field=base.fields.UserField(help_text='The user who created this data', related_name='created_legal_address_set', editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='deleted_by',
            field=base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_legal_address_set', editable=False, verbose_name='deleted by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='instance',
            field=saas.fields.InstanceField(related_name='instance_legal_address_set', verbose_name='instance', editable=False, to='saas.Instance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='last_modified_by',
            field=base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_legal_address_set', editable=False, verbose_name='last modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(help_text='Address state', verbose_name='state', to='util.State'),
            preserve_default=True,
        ),
    ]
