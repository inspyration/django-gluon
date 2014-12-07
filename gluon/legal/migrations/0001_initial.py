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
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the data usable ?', editable=False)),
                ('label', models.CharField(verbose_name='label', help_text='The way the data will be see from foreign objects', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True, max_length=255)),
                ('address1', models.CharField(verbose_name='address 1', help_text='Address line 1', max_length=255)),
                ('address2', models.CharField(verbose_name='address 2', help_text='Address line 2', max_length=255)),
                ('zip', models.CharField(verbose_name='zip', help_text='Address zip code', max_length=16)),
                ('city', models.CharField(verbose_name='city', help_text='Address city', max_length=255)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the data usable ?', editable=False)),
                ('label', models.CharField(verbose_name='label', help_text='The way the data will be see from foreign objects', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True, max_length=255)),
                ('website', models.CharField(verbose_name='website', help_text='Profile main website', max_length=64)),
                ('phone', models.CharField(verbose_name='phone', help_text='Profile phone', max_length=16)),
                ('fax', models.CharField(verbose_name='fax', help_text='Profile Fax', max_length=16)),
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
                ('profile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='legal.Profile')),
                ('first_name', models.CharField(verbose_name='first_name', help_text='Person first name', max_length=127)),
                ('last_name', models.CharField(verbose_name='last name', help_text='Person last name', max_length=127)),
                ('avatar_height', models.PositiveSmallIntegerField(verbose_name='avatar height')),
                ('avatar_width', models.PositiveSmallIntegerField(verbose_name='avatar width')),
                ('avatar', models.ImageField(upload_to='legal/persons/avatars/%Y/%m/%d', help_text='Avatar', max_length=64, width_field=models.PositiveSmallIntegerField(verbose_name='avatar width'), height_field=models.PositiveSmallIntegerField(verbose_name='avatar height'), verbose_name='avatar')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
            bases=('legal.profile',),
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('profile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='legal.Profile')),
                ('tin', models.CharField(verbose_name='tin', help_text='Tax intra. number', max_length=16)),
                ('logo_height', models.PositiveSmallIntegerField(verbose_name='logo height')),
                ('logo_width', models.PositiveSmallIntegerField(verbose_name='logo width')),
                ('logo', models.ImageField(upload_to='legal/entities/logos/%Y/%m/%d', help_text='Entity logo', max_length=64, width_field=models.PositiveSmallIntegerField(verbose_name='logo width'), height_field=models.PositiveSmallIntegerField(verbose_name='logo height'), verbose_name='logo')),
            ],
            options={
                'verbose_name': 'entity',
                'verbose_name_plural': 'entities',
            },
            bases=('legal.profile',),
        ),
        migrations.AddField(
            model_name='profile',
            name='addresses',
            field=models.ManyToManyField(blank=True, verbose_name='addresses', to='legal.Address', help_text='Profile addresses', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='created_by',
            field=base.fields.UserField(help_text='The user who created this data', related_name='created_legal_profile_set', editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='deleted_by',
            field=base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_legal_profile_set', editable=False, verbose_name='deleted by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
