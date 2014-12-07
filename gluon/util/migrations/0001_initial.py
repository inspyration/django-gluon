# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import base.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the data usable ?', editable=False)),
                ('label', models.CharField(verbose_name='label', help_text='The way the data will be see from foreign objects', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True, max_length=255)),
                ('alpha2', models.CharField(verbose_name='alpha2', help_text='Two letters code', unique=True, max_length=2)),
                ('alpha3', models.CharField(verbose_name='alpha3', help_text='Three letters code', unique=True, max_length=3)),
                ('number', models.PositiveSmallIntegerField(verbose_name='number', help_text='Three digits number code', unique=True)),
                ('name_fr', models.CharField(verbose_name='french name', help_text='French common name of the country', unique=True, max_length=2)),
                ('name_en', models.CharField(verbose_name='english name', help_text='English common name of the country', unique=True, max_length=3)),
                ('usage', models.CharField(verbose_name='usage name', help_text='Usage name (localised)', unique=True, max_length=3)),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_util_country_set', editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_util_country_set', editable=False, verbose_name='deleted by', to=settings.AUTH_USER_MODEL, null=True)),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_util_country_set', editable=False, verbose_name='last modified by', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locale',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the data usable ?', editable=False)),
                ('label', models.CharField(verbose_name='label', help_text='The way the data will be see from foreign objects', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True, max_length=255)),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_util_locale_set', editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_util_locale_set', editable=False, verbose_name='deleted by', to=settings.AUTH_USER_MODEL, null=True)),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_util_locale_set', editable=False, verbose_name='last modified by', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'locale',
                'verbose_name_plural': 'locales',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the data usable ?', editable=False)),
                ('label', models.CharField(verbose_name='label', help_text='The way the data will be see from foreign objects', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True, max_length=255)),
                ('code', models.CharField(verbose_name='code', help_text='Two letters code', unique=True, max_length=2)),
                ('country', models.ForeignKey(help_text='Related country', verbose_name='country', to='util.Country')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_util_state_set', editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_util_state_set', editable=False, verbose_name='deleted by', to=settings.AUTH_USER_MODEL, null=True)),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_util_state_set', editable=False, verbose_name='last modified by', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'state',
                'verbose_name_plural': 'states',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('model', models.CharField(verbose_name='model', help_text='Model related to the status', max_length=16)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the status usable ?')),
                ('deleted', models.BooleanField(default=False, verbose_name='deleted', help_text='Is the status deleted')),
                ('name', models.CharField(verbose_name='status name', help_text='Name of the status', max_length=16)),
                ('is_default', models.BooleanField(default=False, verbose_name='status name', help_text='Is the status is the default one for the model ?')),
            ],
            options={
                'verbose_name': 'status',
                'verbose_name_plural': 'statuses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeZone',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the data usable ?', editable=False)),
                ('label', models.CharField(verbose_name='label', help_text='The way the data will be see from foreign objects', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True, max_length=255)),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_util_timezone_set', editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_util_timezone_set', editable=False, verbose_name='deleted by', to=settings.AUTH_USER_MODEL, null=True)),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_util_timezone_set', editable=False, verbose_name='last modified by', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'timezone',
                'verbose_name_plural': 'timezones',
            },
            bases=(models.Model,),
        ),
    ]
