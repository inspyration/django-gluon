# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import base.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Browser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, verbose_name='created on', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, help_text='Date of deletion', verbose_name='deleted on', null=True, blank=True)),
                ('active', models.BooleanField(editable=False, help_text='Is the data usable ?', verbose_name='active', default=True)),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True)),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False, null=True, verbose_name='created by', related_name='created_util_browser_set')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False, null=True, verbose_name='deleted by', related_name='deleted_util_browser_set')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False, null=True, verbose_name='last modified by', related_name='last_modified_util_browser_set')),
            ],
            options={
                'verbose_name': 'Browser',
                'verbose_name_plural': 'Browsers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, verbose_name='created on', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, help_text='Date of deletion', verbose_name='deleted on', null=True, blank=True)),
                ('active', models.BooleanField(editable=False, help_text='Is the data usable ?', verbose_name='active', default=True)),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True)),
                ('alpha2', models.CharField(max_length=2, help_text='Two letters code', verbose_name='alpha2', unique=True)),
                ('alpha3', models.CharField(max_length=3, help_text='Three letters code', verbose_name='alpha3', unique=True)),
                ('number', models.PositiveSmallIntegerField(help_text='Three digits number code', verbose_name='number', unique=True)),
                ('name_fr', models.CharField(max_length=2, help_text='French common name of the country', verbose_name='french name', unique=True)),
                ('name_en', models.CharField(max_length=3, help_text='English common name of the country', verbose_name='english name', unique=True)),
                ('usage', models.CharField(max_length=3, help_text='Usage name (localised)', verbose_name='usage name', unique=True)),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False, null=True, verbose_name='created by', related_name='created_util_country_set')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False, null=True, verbose_name='deleted by', related_name='deleted_util_country_set')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False, null=True, verbose_name='last modified by', related_name='last_modified_util_country_set')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HtmlTag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, verbose_name='created on', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, help_text='Date of deletion', verbose_name='deleted on', null=True, blank=True)),
                ('active', models.BooleanField(editable=False, help_text='Is the data usable ?', verbose_name='active', default=True)),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True)),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False, null=True, verbose_name='created by', related_name='created_util_htmltag_set')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False, null=True, verbose_name='deleted by', related_name='deleted_util_htmltag_set')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False, null=True, verbose_name='last modified by', related_name='last_modified_util_htmltag_set')),
            ],
            options={
                'verbose_name': 'Html tag',
                'verbose_name_plural': 'Html tags',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HttpResource',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, verbose_name='created on', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, help_text='Date of deletion', verbose_name='deleted on', null=True, blank=True)),
                ('active', models.BooleanField(editable=False, help_text='Is the data usable ?', verbose_name='active', default=True)),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True)),
                ('path', models.CharField(max_length=127, blank=True, help_text='Path to the (hosted) resource', verbose_name='path')),
                ('browser', models.ForeignKey(to='util.Browser', help_text='Specific Browser (potentially with version number)', verbose_name='browser', related_name='browser_httpresource_set')),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False, null=True, verbose_name='created by', related_name='created_util_httpresource_set')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False, null=True, verbose_name='deleted by', related_name='deleted_util_httpresource_set')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False, null=True, verbose_name='last modified by', related_name='last_modified_util_httpresource_set')),
                ('tag', models.ForeignKey(to='util.HtmlTag', help_text='HTML Tag used to call this resource', verbose_name='tag', related_name='tag_httpresource_set')),
            ],
            options={
                'verbose_name': 'Http resource',
                'verbose_name_plural': 'Http resources',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HttpResourcesConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', auto_now_add=True, help_text='Date of creation', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', help_text='Date of last modification', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', null=True, help_text='Date of deletion', editable=False)),
                ('active', models.BooleanField(verbose_name='active', help_text='Is the data usable ?', default=True, editable=False)),
                ('label', models.CharField(verbose_name='label', help_text='The way the data will be see from foreign objects', max_length=32)),
                ('name', models.CharField(verbose_name='name', unique=True, help_text='Unique name, used in imports/exports features', max_length=255, editable=False)),
                ('created_by', base.fields.UserField(verbose_name='created by', to=settings.AUTH_USER_MODEL, related_name='created_util_httpresourcesconfig_set', editable=False, null=True, help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(verbose_name='deleted by', to=settings.AUTH_USER_MODEL, related_name='deleted_util_httpresourcesconfig_set', editable=False, null=True, help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(verbose_name='last modified by', to=settings.AUTH_USER_MODEL, related_name='last_modified_util_httpresourcesconfig_set', editable=False, null=True, help_text='The user who last modified this data')),
                ('resources', models.ManyToManyField(blank=True, verbose_name='HTTP resources', help_text='List of resources used by this view (CSS, JS, Meta, ...)', to='util.HttpResource', related_name='view_set')),
            ],
            options={
                'verbose_name': 'Http resources configuration',
                'verbose_name_plural': 'Http resources configurations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, verbose_name='created on', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, help_text='Date of deletion', verbose_name='deleted on', null=True, blank=True)),
                ('active', models.BooleanField(editable=False, help_text='Is the data usable ?', verbose_name='active', default=True)),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True)),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False, null=True, verbose_name='created by', related_name='created_util_keyword_set')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False, null=True, verbose_name='deleted by', related_name='deleted_util_keyword_set')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False, null=True, verbose_name='last modified by', related_name='last_modified_util_keyword_set')),
            ],
            options={
                'verbose_name': 'keyword',
                'verbose_name_plural': 'keywords',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locale',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, verbose_name='created on', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, help_text='Date of deletion', verbose_name='deleted on', null=True, blank=True)),
                ('active', models.BooleanField(editable=False, help_text='Is the data usable ?', verbose_name='active', default=True)),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True)),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False, null=True, verbose_name='created by', related_name='created_util_locale_set')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False, null=True, verbose_name='deleted by', related_name='deleted_util_locale_set')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False, null=True, verbose_name='last modified by', related_name='last_modified_util_locale_set')),
            ],
            options={
                'verbose_name': 'locale',
                'verbose_name_plural': 'locales',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mime',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, verbose_name='created on', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, help_text='Date of deletion', verbose_name='deleted on', null=True, blank=True)),
                ('active', models.BooleanField(editable=False, help_text='Is the data usable ?', verbose_name='active', default=True)),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True)),
                ('reference', models.CharField(max_length=127, blank=True, help_text='Mime type reference', verbose_name='reference')),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False, null=True, verbose_name='created by', related_name='created_util_mime_set')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False, null=True, verbose_name='deleted by', related_name='deleted_util_mime_set')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False, null=True, verbose_name='last modified by', related_name='last_modified_util_mime_set')),
            ],
            options={
                'verbose_name': 'MIME type',
                'verbose_name_plural': 'MIME types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MimeRegistry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, verbose_name='created on', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, help_text='Date of deletion', verbose_name='deleted on', null=True, blank=True)),
                ('active', models.BooleanField(editable=False, help_text='Is the data usable ?', verbose_name='active', default=True)),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True)),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False, null=True, verbose_name='created by', related_name='created_util_mimeregistry_set')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False, null=True, verbose_name='deleted by', related_name='deleted_util_mimeregistry_set')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False, null=True, verbose_name='last modified by', related_name='last_modified_util_mimeregistry_set')),
            ],
            options={
                'verbose_name': 'MIME registry',
                'verbose_name_plural': 'MIME registries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, verbose_name='created on', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, help_text='Date of deletion', verbose_name='deleted on', null=True, blank=True)),
                ('active', models.BooleanField(editable=False, help_text='Is the data usable ?', verbose_name='active', default=True)),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True)),
                ('code', models.CharField(max_length=2, help_text='Two letters code', verbose_name='code', unique=True)),
                ('country', models.ForeignKey(to='util.Country', help_text='Related country', verbose_name='country')),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False, null=True, verbose_name='created by', related_name='created_util_state_set')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False, null=True, verbose_name='deleted by', related_name='deleted_util_state_set')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False, null=True, verbose_name='last modified by', related_name='last_modified_util_state_set')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, verbose_name='created on', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, help_text='Date of deletion', verbose_name='deleted on', null=True, blank=True)),
                ('active', models.BooleanField(editable=False, help_text='Is the data usable ?', verbose_name='active', default=True)),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True)),
                ('model', models.CharField(max_length=32, help_text='Model related to the status', verbose_name='model')),
                ('is_default', models.BooleanField(help_text='Is the status is the default one for the model ?', verbose_name='status name', default=False)),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False, null=True, verbose_name='created by', related_name='created_util_status_set')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False, null=True, verbose_name='deleted by', related_name='deleted_util_status_set')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False, null=True, verbose_name='last modified by', related_name='last_modified_util_status_set')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, verbose_name='created on', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, help_text='Date of deletion', verbose_name='deleted on', null=True, blank=True)),
                ('active', models.BooleanField(editable=False, help_text='Is the data usable ?', verbose_name='active', default=True)),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True)),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who created this data', editable=False, null=True, verbose_name='created by', related_name='created_util_timezone_set')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data', editable=False, null=True, verbose_name='deleted by', related_name='deleted_util_timezone_set')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data', editable=False, null=True, verbose_name='last modified by', related_name='last_modified_util_timezone_set')),
            ],
            options={
                'verbose_name': 'timezone',
                'verbose_name_plural': 'timezones',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mime',
            name='registry',
            field=models.ForeignKey(to='util.MimeRegistry', help_text='Mime type registry', verbose_name='registry', related_name='registry_mime_set'),
            preserve_default=True,
        ),
    ]
