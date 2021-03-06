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
            name='Browser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(unique=True, editable=False, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('created_by', base.fields.UserField(null=True, editable=False, verbose_name='created by', related_name='created_util_browser_set', to=settings.AUTH_USER_MODEL, help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(null=True, editable=False, verbose_name='deleted by', related_name='deleted_util_browser_set', to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(null=True, editable=False, verbose_name='last modified by', related_name='last_modified_util_browser_set', to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(unique=True, editable=False, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('alpha2', models.CharField(unique=True, verbose_name='alpha2', max_length=2, help_text='Two letters code')),
                ('alpha3', models.CharField(unique=True, verbose_name='alpha3', max_length=3, help_text='Three letters code')),
                ('number', models.PositiveSmallIntegerField(unique=True, verbose_name='number', help_text='Three digits number code')),
                ('name_fr', models.CharField(unique=True, verbose_name='french name', max_length=2, help_text='French common name of the country')),
                ('name_en', models.CharField(unique=True, verbose_name='english name', max_length=3, help_text='English common name of the country')),
                ('usage', models.CharField(unique=True, verbose_name='usage name', max_length=3, help_text='Usage name (localised)')),
                ('created_by', base.fields.UserField(null=True, editable=False, verbose_name='created by', related_name='created_util_country_set', to=settings.AUTH_USER_MODEL, help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(null=True, editable=False, verbose_name='deleted by', related_name='deleted_util_country_set', to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(null=True, editable=False, verbose_name='last modified by', related_name='last_modified_util_country_set', to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(unique=True, editable=False, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('created_by', base.fields.UserField(null=True, editable=False, verbose_name='created by', related_name='created_util_htmltag_set', to=settings.AUTH_USER_MODEL, help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(null=True, editable=False, verbose_name='deleted by', related_name='deleted_util_htmltag_set', to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(null=True, editable=False, verbose_name='last modified by', related_name='last_modified_util_htmltag_set', to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(unique=True, editable=False, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('path', models.CharField(verbose_name='path', blank=True, max_length=127, help_text='Path to the (hosted) resource')),
                ('browser', models.ForeignKey(verbose_name='browser', related_name='browser_httpresource_set', to='util.Browser', help_text='Specific Browser (potentially with version number)')),
                ('created_by', base.fields.UserField(null=True, editable=False, verbose_name='created by', related_name='created_util_httpresource_set', to=settings.AUTH_USER_MODEL, help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(null=True, editable=False, verbose_name='deleted by', related_name='deleted_util_httpresource_set', to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(null=True, editable=False, verbose_name='last modified by', related_name='last_modified_util_httpresource_set', to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data')),
                ('tag', models.ForeignKey(verbose_name='tag', related_name='tag_httpresource_set', to='util.HtmlTag', help_text='HTML Tag used to call this resource')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(unique=True, editable=False, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('created_by', base.fields.UserField(null=True, editable=False, verbose_name='created by', related_name='created_util_httpresourcesconfig_set', to=settings.AUTH_USER_MODEL, help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(null=True, editable=False, verbose_name='deleted by', related_name='deleted_util_httpresourcesconfig_set', to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(null=True, editable=False, verbose_name='last modified by', related_name='last_modified_util_httpresourcesconfig_set', to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data')),
                ('resources', models.ManyToManyField(verbose_name='HTTP resources', to='util.HttpResource', related_name='view_set', blank=True, help_text='List of resources used by this view (CSS, JS, Meta, ...)')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(unique=True, editable=False, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('created_by', base.fields.UserField(null=True, editable=False, verbose_name='created by', related_name='created_util_keyword_set', to=settings.AUTH_USER_MODEL, help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(null=True, editable=False, verbose_name='deleted by', related_name='deleted_util_keyword_set', to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(null=True, editable=False, verbose_name='last modified by', related_name='last_modified_util_keyword_set', to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(unique=True, editable=False, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('created_by', base.fields.UserField(null=True, editable=False, verbose_name='created by', related_name='created_util_locale_set', to=settings.AUTH_USER_MODEL, help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(null=True, editable=False, verbose_name='deleted by', related_name='deleted_util_locale_set', to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(null=True, editable=False, verbose_name='last modified by', related_name='last_modified_util_locale_set', to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(unique=True, editable=False, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('reference', models.CharField(verbose_name='reference', blank=True, max_length=127, help_text='Mime type reference')),
                ('created_by', base.fields.UserField(null=True, editable=False, verbose_name='created by', related_name='created_util_mime_set', to=settings.AUTH_USER_MODEL, help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(null=True, editable=False, verbose_name='deleted by', related_name='deleted_util_mime_set', to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(null=True, editable=False, verbose_name='last modified by', related_name='last_modified_util_mime_set', to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(unique=True, editable=False, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('created_by', base.fields.UserField(null=True, editable=False, verbose_name='created by', related_name='created_util_mimeregistry_set', to=settings.AUTH_USER_MODEL, help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(null=True, editable=False, verbose_name='deleted by', related_name='deleted_util_mimeregistry_set', to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(null=True, editable=False, verbose_name='last modified by', related_name='last_modified_util_mimeregistry_set', to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(unique=True, editable=False, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('code', models.CharField(unique=True, verbose_name='code', max_length=5, help_text='Two letters code')),
            ],
            options={
                'verbose_name': 'state',
                'verbose_name_plural': 'states',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StateCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(unique=True, editable=False, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('plural', models.CharField(verbose_name='plural', max_length=127, help_text='Plural label')),
                ('created_by', base.fields.UserField(null=True, editable=False, verbose_name='created by', related_name='created_util_statecategory_set', to=settings.AUTH_USER_MODEL, help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(null=True, editable=False, verbose_name='deleted by', related_name='deleted_util_statecategory_set', to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(null=True, editable=False, verbose_name='last modified by', related_name='last_modified_util_statecategory_set', to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data')),
            ],
            options={
                'verbose_name': 'state category',
                'verbose_name_plural': 'state categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(unique=True, editable=False, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('model', models.CharField(verbose_name='model', max_length=32, help_text='Model related to the status')),
                ('is_default', models.BooleanField(verbose_name='status name', default=False, help_text='Is the status is the default one for the model ?')),
                ('created_by', base.fields.UserField(null=True, editable=False, verbose_name='created by', related_name='created_util_status_set', to=settings.AUTH_USER_MODEL, help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(null=True, editable=False, verbose_name='deleted by', related_name='deleted_util_status_set', to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(null=True, editable=False, verbose_name='last modified by', related_name='last_modified_util_status_set', to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, verbose_name='deleted on', editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(unique=True, editable=False, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('created_by', base.fields.UserField(null=True, editable=False, verbose_name='created by', related_name='created_util_timezone_set', to=settings.AUTH_USER_MODEL, help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(null=True, editable=False, verbose_name='deleted by', related_name='deleted_util_timezone_set', to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(null=True, editable=False, verbose_name='last modified by', related_name='last_modified_util_timezone_set', to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data')),
            ],
            options={
                'verbose_name': 'timezone',
                'verbose_name_plural': 'timezones',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='state',
            name='category',
            field=models.ForeignKey(verbose_name='category', related_name='registry_state_set', to='util.StateCategory', help_text='State, Province or District'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='state',
            name='country',
            field=models.ForeignKey(verbose_name='country', related_name='state_set', to='util.Country', help_text='Related country'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='state',
            name='created_by',
            field=base.fields.UserField(null=True, editable=False, verbose_name='created by', related_name='created_util_state_set', to=settings.AUTH_USER_MODEL, help_text='The user who created this data'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='state',
            name='deleted_by',
            field=base.fields.UserField(null=True, editable=False, verbose_name='deleted by', related_name='deleted_util_state_set', to=settings.AUTH_USER_MODEL, help_text='The user who deleted this data'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='state',
            name='last_modified_by',
            field=base.fields.UserField(null=True, editable=False, verbose_name='last modified by', related_name='last_modified_util_state_set', to=settings.AUTH_USER_MODEL, help_text='The user who last modified this data'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mime',
            name='registry',
            field=models.ForeignKey(verbose_name='registry', related_name='registry_mime_set', to='util.MimeRegistry', help_text='Mime type registry'),
            preserve_default=True,
        ),
    ]
