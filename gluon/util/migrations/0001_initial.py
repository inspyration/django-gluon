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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(null=True, editable=False, blank=True, verbose_name='deleted on')),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255)),
                ('alpha2', models.CharField(unique=True, verbose_name='alpha2', max_length=2)),
                ('alpha3', models.CharField(unique=True, verbose_name='alpha3', max_length=3)),
                ('number', models.PositiveSmallIntegerField(unique=True, verbose_name='number')),
                ('name_fr', models.CharField(unique=True, verbose_name='french name', max_length=2)),
                ('name_en', models.CharField(unique=True, verbose_name='english name', max_length=3)),
                ('usage', models.CharField(unique=True, verbose_name='usage name', max_length=3)),
                ('created_by', base.fields.UserField(related_name='created_util_country_set', to=settings.AUTH_USER_MODEL, verbose_name='created by', null=True, editable=False)),
                ('deleted_by', base.fields.UserField(related_name='deleted_util_country_set', to=settings.AUTH_USER_MODEL, verbose_name='deleted by', null=True, editable=False)),
                ('last_modified_by', base.fields.UserField(related_name='last_modified_util_country_set', to=settings.AUTH_USER_MODEL, verbose_name='last modified by', null=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(null=True, editable=False, blank=True, verbose_name='deleted on')),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255)),
                ('created_by', base.fields.UserField(related_name='created_util_locale_set', to=settings.AUTH_USER_MODEL, verbose_name='created by', null=True, editable=False)),
                ('deleted_by', base.fields.UserField(related_name='deleted_util_locale_set', to=settings.AUTH_USER_MODEL, verbose_name='deleted by', null=True, editable=False)),
                ('last_modified_by', base.fields.UserField(related_name='last_modified_util_locale_set', to=settings.AUTH_USER_MODEL, verbose_name='last modified by', null=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(null=True, editable=False, blank=True, verbose_name='deleted on')),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255)),
                ('code', models.CharField(unique=True, verbose_name='code', max_length=2)),
                ('country', models.ForeignKey(to='util.Country', verbose_name='country')),
                ('created_by', base.fields.UserField(related_name='created_util_state_set', to=settings.AUTH_USER_MODEL, verbose_name='created by', null=True, editable=False)),
                ('deleted_by', base.fields.UserField(related_name='deleted_util_state_set', to=settings.AUTH_USER_MODEL, verbose_name='deleted by', null=True, editable=False)),
                ('last_modified_by', base.fields.UserField(related_name='last_modified_util_state_set', to=settings.AUTH_USER_MODEL, verbose_name='last modified by', null=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('model', models.CharField(verbose_name='model', max_length=16)),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('deleted', models.BooleanField(default=False, verbose_name='active')),
                ('name', models.CharField(verbose_name='status name', max_length=16)),
                ('is_default', models.BooleanField(default=False, verbose_name='status name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeZone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(null=True, editable=False, blank=True, verbose_name='deleted on')),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255)),
                ('created_by', base.fields.UserField(related_name='created_util_timezone_set', to=settings.AUTH_USER_MODEL, verbose_name='created by', null=True, editable=False)),
                ('deleted_by', base.fields.UserField(related_name='deleted_util_timezone_set', to=settings.AUTH_USER_MODEL, verbose_name='deleted by', null=True, editable=False)),
                ('last_modified_by', base.fields.UserField(related_name='last_modified_util_timezone_set', to=settings.AUTH_USER_MODEL, verbose_name='last modified by', null=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
