# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date of creation', default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', auto_now=True, default=django.utils.timezone.now, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(help_text='Date of deletion', blank=True, editable=False, verbose_name='deleted on', null=True)),
                ('active', models.BooleanField(help_text='Is the data usable ?', editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, help_text='Unique name, used in imports/exports features', editable=False, verbose_name='name', unique=True)),
                ('alpha2', models.CharField(max_length=2, help_text='Two letters code', verbose_name='alpha2', unique=True)),
                ('alpha3', models.CharField(max_length=3, help_text='Three letters code', verbose_name='alpha3', unique=True)),
                ('number', models.PositiveSmallIntegerField(help_text='Three digits number code', verbose_name='number', unique=True)),
                ('name_fr', models.CharField(max_length=2, help_text='French common name of the country', verbose_name='french name', unique=True)),
                ('name_en', models.CharField(max_length=3, help_text='English common name of the country', verbose_name='english name', unique=True)),
                ('usage', models.CharField(max_length=3, help_text='Usage name (localised)', verbose_name='usage name', unique=True)),
                ('created_by', base.fields.UserField(editable=False, related_name='created_util_country_set', null=True, help_text='The user who created this data', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_util_country_set', null=True, help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(editable=False, related_name='last_modified_util_country_set', null=True, help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, verbose_name='last modified by')),
            ],
            options={
                'verbose_name_plural': 'countries',
                'verbose_name': 'country',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locale',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date of creation', default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', auto_now=True, default=django.utils.timezone.now, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(help_text='Date of deletion', blank=True, editable=False, verbose_name='deleted on', null=True)),
                ('active', models.BooleanField(help_text='Is the data usable ?', editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, help_text='Unique name, used in imports/exports features', editable=False, verbose_name='name', unique=True)),
                ('created_by', base.fields.UserField(editable=False, related_name='created_util_locale_set', null=True, help_text='The user who created this data', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_util_locale_set', null=True, help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(editable=False, related_name='last_modified_util_locale_set', null=True, help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, verbose_name='last modified by')),
            ],
            options={
                'verbose_name_plural': 'locales',
                'verbose_name': 'locale',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date of creation', default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', auto_now=True, default=django.utils.timezone.now, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(help_text='Date of deletion', blank=True, editable=False, verbose_name='deleted on', null=True)),
                ('active', models.BooleanField(help_text='Is the data usable ?', editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, help_text='Unique name, used in imports/exports features', editable=False, verbose_name='name', unique=True)),
                ('code', models.CharField(max_length=2, help_text='Two letters code', verbose_name='code', unique=True)),
                ('country', models.ForeignKey(help_text='Related country', to='util.Country', verbose_name='country')),
                ('created_by', base.fields.UserField(editable=False, related_name='created_util_state_set', null=True, help_text='The user who created this data', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_util_state_set', null=True, help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(editable=False, related_name='last_modified_util_state_set', null=True, help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, verbose_name='last modified by')),
            ],
            options={
                'verbose_name_plural': 'states',
                'verbose_name': 'state',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date of creation', default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', auto_now=True, default=django.utils.timezone.now, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(help_text='Date of deletion', blank=True, editable=False, verbose_name='deleted on', null=True)),
                ('active', models.BooleanField(help_text='Is the data usable ?', editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, help_text='Unique name, used in imports/exports features', editable=False, verbose_name='name', unique=True)),
                ('model', models.CharField(max_length=16, help_text='Model related to the status', verbose_name='model')),
                ('is_default', models.BooleanField(help_text='Is the status is the default one for the model ?', default=False, verbose_name='status name')),
                ('created_by', base.fields.UserField(editable=False, related_name='created_util_status_set', null=True, help_text='The user who created this data', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_util_status_set', null=True, help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(editable=False, related_name='last_modified_util_status_set', null=True, help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, verbose_name='last modified by')),
            ],
            options={
                'verbose_name_plural': 'statuses',
                'verbose_name': 'status',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeZone',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date of creation', default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', auto_now=True, default=django.utils.timezone.now, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(help_text='Date of deletion', blank=True, editable=False, verbose_name='deleted on', null=True)),
                ('active', models.BooleanField(help_text='Is the data usable ?', editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, help_text='Unique name, used in imports/exports features', editable=False, verbose_name='name', unique=True)),
                ('created_by', base.fields.UserField(editable=False, related_name='created_util_timezone_set', null=True, help_text='The user who created this data', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_util_timezone_set', null=True, help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(editable=False, related_name='last_modified_util_timezone_set', null=True, help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, verbose_name='last modified by')),
            ],
            options={
                'verbose_name_plural': 'timezones',
                'verbose_name': 'timezone',
            },
            bases=(models.Model,),
        ),
    ]
