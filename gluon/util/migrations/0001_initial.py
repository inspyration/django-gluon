# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import base.fields
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', auto_now_add=True, default=django.utils.timezone.now, help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, help_text='Date of deletion', blank=True)),
                ('active', models.BooleanField(verbose_name='active', default=True, editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(verbose_name='name', max_length=255, unique=True, help_text='Unique name, used in imports/exports features', editable=False)),
                ('alpha2', models.CharField(verbose_name='alpha2', max_length=2, unique=True, help_text='Two letters code')),
                ('alpha3', models.CharField(verbose_name='alpha3', max_length=3, unique=True, help_text='Three letters code')),
                ('number', models.PositiveSmallIntegerField(verbose_name='number', unique=True, help_text='Three digits number code')),
                ('name_fr', models.CharField(verbose_name='french name', max_length=2, unique=True, help_text='French common name of the country')),
                ('name_en', models.CharField(verbose_name='english name', max_length=3, unique=True, help_text='English common name of the country')),
                ('usage', models.CharField(verbose_name='usage name', max_length=3, unique=True, help_text='Usage name (localised)')),
                ('created_by', base.fields.UserField(verbose_name='created by', related_name='created_util_country_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False)),
                ('deleted_by', base.fields.UserField(verbose_name='deleted by', related_name='deleted_util_country_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False)),
                ('last_modified_by', base.fields.UserField(verbose_name='last modified by', related_name='last_modified_util_country_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', auto_now_add=True, default=django.utils.timezone.now, help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, help_text='Date of deletion', blank=True)),
                ('active', models.BooleanField(verbose_name='active', default=True, editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(verbose_name='name', max_length=255, unique=True, help_text='Unique name, used in imports/exports features', editable=False)),
                ('created_by', base.fields.UserField(verbose_name='created by', related_name='created_util_locale_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False)),
                ('deleted_by', base.fields.UserField(verbose_name='deleted by', related_name='deleted_util_locale_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False)),
                ('last_modified_by', base.fields.UserField(verbose_name='last modified by', related_name='last_modified_util_locale_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', auto_now_add=True, default=django.utils.timezone.now, help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, help_text='Date of deletion', blank=True)),
                ('active', models.BooleanField(verbose_name='active', default=True, editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(verbose_name='name', max_length=255, unique=True, help_text='Unique name, used in imports/exports features', editable=False)),
                ('code', models.CharField(verbose_name='code', max_length=2, unique=True, help_text='Two letters code')),
                ('country', models.ForeignKey(verbose_name='country', to='util.Country', help_text='Related country')),
                ('created_by', base.fields.UserField(verbose_name='created by', related_name='created_util_state_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False)),
                ('deleted_by', base.fields.UserField(verbose_name='deleted by', related_name='deleted_util_state_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False)),
                ('last_modified_by', base.fields.UserField(verbose_name='last modified by', related_name='last_modified_util_state_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', auto_now_add=True, default=django.utils.timezone.now, help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, help_text='Date of deletion', blank=True)),
                ('active', models.BooleanField(verbose_name='active', default=True, editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(verbose_name='name', max_length=255, unique=True, help_text='Unique name, used in imports/exports features', editable=False)),
                ('model', models.CharField(verbose_name='model', max_length=16, help_text='Model related to the status')),
                ('is_default', models.BooleanField(verbose_name='status name', default=False, help_text='Is the status is the default one for the model ?')),
                ('created_by', base.fields.UserField(verbose_name='created by', related_name='created_util_status_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False)),
                ('deleted_by', base.fields.UserField(verbose_name='deleted by', related_name='deleted_util_status_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False)),
                ('last_modified_by', base.fields.UserField(verbose_name='last modified by', related_name='last_modified_util_status_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', auto_now_add=True, default=django.utils.timezone.now, help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, help_text='Date of deletion', blank=True)),
                ('active', models.BooleanField(verbose_name='active', default=True, editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(verbose_name='name', max_length=255, unique=True, help_text='Unique name, used in imports/exports features', editable=False)),
                ('created_by', base.fields.UserField(verbose_name='created by', related_name='created_util_timezone_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False)),
                ('deleted_by', base.fields.UserField(verbose_name='deleted by', related_name='deleted_util_timezone_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False)),
                ('last_modified_by', base.fields.UserField(verbose_name='last modified by', related_name='last_modified_util_timezone_set', null=True, to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False)),
            ],
            options={
                'verbose_name': 'timezone',
                'verbose_name_plural': 'timezones',
            },
            bases=(models.Model,),
        ),
    ]
