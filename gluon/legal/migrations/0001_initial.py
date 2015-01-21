# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import base.fields
import saas.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('util', '0002_imports'),
        ('saas', '0002_imports'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', default=django.utils.timezone.now, help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on', default=django.utils.timezone.now, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(null=True, blank=True, verbose_name='deleted on', help_text='Date of deletion', editable=False)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the data usable ?', editable=False)),
                ('label', models.CharField(max_length=32, verbose_name='label', help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name', help_text='Unique name, used in imports/exports features', editable=False)),
                ('address1', models.CharField(max_length=255, verbose_name='address 1', help_text='first line of the address')),
                ('address2', models.CharField(max_length=255, blank=True, verbose_name='address 2', help_text='second line of the address', null=True)),
                ('zip', models.CharField(max_length=16, verbose_name='zip', help_text='Zip code')),
                ('city', models.CharField(max_length=255, verbose_name='city', help_text='City')),
                ('country', models.ForeignKey(verbose_name='country', help_text='Country', to='util.Country', related_name='legal_address_set')),
                ('created_by', base.fields.UserField(null=True, verbose_name='created by', help_text='The user who created this data', editable=False, related_name='created_legal_address_set', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', base.fields.UserField(null=True, verbose_name='deleted by', help_text='The user who deleted this data', editable=False, related_name='deleted_legal_address_set', to=settings.AUTH_USER_MODEL)),
                ('instance', saas.fields.InstanceField(verbose_name='instance', to='saas.Instance', editable=False, related_name='instance_legal_address_set')),
                ('last_modified_by', base.fields.UserField(null=True, verbose_name='last modified by', help_text='The user who last modified this data', editable=False, related_name='last_modified_legal_address_set', to=settings.AUTH_USER_MODEL)),
                ('state', models.ForeignKey(null=True, verbose_name='state', blank=True, help_text='State', related_name='legal_address_set', to='util.State')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', default=django.utils.timezone.now, help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on', default=django.utils.timezone.now, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(null=True, blank=True, verbose_name='deleted on', help_text='Date of deletion', editable=False)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the data usable ?', editable=False)),
                ('label', models.CharField(max_length=32, verbose_name='label', help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name', help_text='Unique name, used in imports/exports features', editable=False)),
                ('website', models.CharField(max_length=64, blank=True, verbose_name='website', help_text='Website URI', null=True)),
                ('phone', models.CharField(max_length=16, verbose_name='phone', help_text='Phone number')),
                ('fax', models.CharField(max_length=16, blank=True, verbose_name='fax', help_text='Fax number', null=True)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('profile_ptr', models.OneToOneField(serialize=False, primary_key=True, to='legal.Profile', auto_created=True, parent_link=True)),
                ('avatar_height', models.PositiveSmallIntegerField(verbose_name='avatar height', blank=True)),
                ('avatar_width', models.PositiveSmallIntegerField(verbose_name='avatar width', blank=True)),
                ('avatar', models.ImageField(width_field=models.PositiveSmallIntegerField(verbose_name='avatar width', blank=True), max_length=64, verbose_name='avatar', blank=True, null=True, help_text='Avatar', upload_to='media/%(app_label)s/%(class)s/avatars/%Y/%m/%d', height_field=models.PositiveSmallIntegerField(verbose_name='avatar height', blank=True))),
                ('first_name', models.CharField(max_length=127, verbose_name='first_name', help_text='Person first name')),
                ('last_name', models.CharField(max_length=127, verbose_name='last name', help_text='Person last name')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
            bases=('legal.profile', models.Model),
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('profile_ptr', models.OneToOneField(serialize=False, primary_key=True, to='legal.Profile', auto_created=True, parent_link=True)),
                ('tin', models.CharField(max_length=16, blank=True, verbose_name='tin', help_text='Tax intra. number', null=True)),
                ('logo_height', models.PositiveSmallIntegerField(verbose_name='logo height', blank=True)),
                ('logo_width', models.PositiveSmallIntegerField(verbose_name='logo width', blank=True)),
                ('logo', models.ImageField(width_field=models.PositiveSmallIntegerField(verbose_name='logo width', blank=True), max_length=64, verbose_name='logo', blank=True, null=True, help_text='Logo of the instance owner', upload_to='media/%(app_label)s/%(class)s/logos/%Y/%m/%d', height_field=models.PositiveSmallIntegerField(verbose_name='logo height', blank=True))),
            ],
            options={
                'verbose_name': 'entity',
                'verbose_name_plural': 'entities',
            },
            bases=('legal.profile', models.Model),
        ),
        migrations.AddField(
            model_name='profile',
            name='addresses',
            field=models.ManyToManyField(null=True, blank=True, verbose_name='addresses', help_text='Profile addresses', to='legal.Address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='created_by',
            field=base.fields.UserField(null=True, verbose_name='created by', help_text='The user who created this data', editable=False, related_name='created_legal_profile_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='deleted_by',
            field=base.fields.UserField(null=True, verbose_name='deleted by', help_text='The user who deleted this data', editable=False, related_name='deleted_legal_profile_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='instance',
            field=saas.fields.InstanceField(verbose_name='instance', to='saas.Instance', editable=False, related_name='instance_legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_modified_by',
            field=base.fields.UserField(null=True, verbose_name='last modified by', help_text='The user who last modified this data', editable=False, related_name='last_modified_legal_profile_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='locale',
            field=models.ForeignKey(verbose_name='locale', help_text='Locale', to='util.Locale', related_name='legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='timezone',
            field=models.ForeignKey(verbose_name='timezone', help_text='Timezone', to='util.TimeZone', related_name='legal_profile_set'),
            preserve_default=True,
        ),
    ]
