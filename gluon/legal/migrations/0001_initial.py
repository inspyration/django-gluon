# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import saas.fields
import base.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saas', '0002_imports'),
        ('util', '0002_imports'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', auto_now=True, default=django.utils.timezone.now, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(help_text='Date of deletion', null=True, blank=True, verbose_name='deleted on', editable=False)),
                ('active', models.BooleanField(help_text='Is the data usable ?', default=True, verbose_name='active', editable=False)),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(help_text='Unique name, used in imports/exports features', max_length=255, unique=True, verbose_name='name', editable=False)),
                ('address1', models.CharField(help_text='first line of the address', max_length=255, verbose_name='address 1')),
                ('address2', models.CharField(help_text='second line of the address', max_length=255, verbose_name='address 2')),
                ('zip', models.CharField(help_text='Zip code', max_length=16, verbose_name='zip')),
                ('city', models.CharField(help_text='City', max_length=255, verbose_name='city')),
                ('country', models.ForeignKey(help_text='Country', related_name='legal_address_set', to='util.Country', verbose_name='country')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_legal_address_set', to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by', editable=False)),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_legal_address_set', to=settings.AUTH_USER_MODEL, null=True, verbose_name='deleted by', editable=False)),
                ('instance', saas.fields.InstanceField(related_name='instance_legal_address_set', to='saas.Instance', verbose_name='instance', editable=False)),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_legal_address_set', to=settings.AUTH_USER_MODEL, null=True, verbose_name='last modified by', editable=False)),
                ('state', models.ForeignKey(help_text='State', related_name='legal_address_set', to='util.State', verbose_name='state')),
            ],
            options={
                'verbose_name_plural': 'addresses',
                'verbose_name': 'address',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', auto_now=True, default=django.utils.timezone.now, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(help_text='Date of deletion', null=True, blank=True, verbose_name='deleted on', editable=False)),
                ('active', models.BooleanField(help_text='Is the data usable ?', default=True, verbose_name='active', editable=False)),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(help_text='Unique name, used in imports/exports features', max_length=255, unique=True, verbose_name='name', editable=False)),
                ('website', models.CharField(help_text='Website URI', max_length=64, verbose_name='website')),
                ('phone', models.CharField(help_text='Phone number', max_length=16, verbose_name='phone')),
                ('fax', models.CharField(help_text='Fax number', max_length=16, verbose_name='fax')),
            ],
            options={
                'verbose_name_plural': 'profiles',
                'verbose_name': 'profile',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='legal.Profile')),
                ('avatar_height', models.PositiveSmallIntegerField(verbose_name='avatar height')),
                ('avatar_width', models.PositiveSmallIntegerField(verbose_name='avatar width')),
                ('avatar', models.ImageField(help_text='Avatar', width_field=models.PositiveSmallIntegerField(verbose_name='avatar width'), height_field=models.PositiveSmallIntegerField(verbose_name='avatar height'), upload_to='media/%(app_label)s/%(class)s/avatars/%Y/%m/%d', max_length=64, verbose_name='avatar')),
                ('first_name', models.CharField(help_text='Person first name', max_length=127, verbose_name='first_name')),
                ('last_name', models.CharField(help_text='Person last name', max_length=127, verbose_name='last name')),
            ],
            options={
                'verbose_name_plural': 'persons',
                'verbose_name': 'person',
            },
            bases=('legal.profile', models.Model),
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='legal.Profile')),
                ('tin', models.CharField(help_text='Tax intra. number', max_length=16, verbose_name='tin')),
                ('logo_height', models.PositiveSmallIntegerField(verbose_name='logo height')),
                ('logo_width', models.PositiveSmallIntegerField(verbose_name='logo width')),
                ('logo', models.ImageField(help_text='Logo of the instance owner', width_field=models.PositiveSmallIntegerField(verbose_name='logo width'), height_field=models.PositiveSmallIntegerField(verbose_name='logo height'), upload_to='media/%(app_label)s/%(class)s/logos/%Y/%m/%d', max_length=64, verbose_name='logo')),
            ],
            options={
                'verbose_name_plural': 'entities',
                'verbose_name': 'entity',
            },
            bases=('legal.profile', models.Model),
        ),
        migrations.AddField(
            model_name='profile',
            name='addresses',
            field=models.ManyToManyField(help_text='Profile addresses', to='legal.Address', null=True, blank=True, verbose_name='addresses'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='created_by',
            field=base.fields.UserField(help_text='The user who created this data', related_name='created_legal_profile_set', to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='deleted_by',
            field=base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_legal_profile_set', to=settings.AUTH_USER_MODEL, null=True, verbose_name='deleted by', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='instance',
            field=saas.fields.InstanceField(related_name='instance_legal_profile_set', to='saas.Instance', verbose_name='instance', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_modified_by',
            field=base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_legal_profile_set', to=settings.AUTH_USER_MODEL, null=True, verbose_name='last modified by', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='locale',
            field=models.ForeignKey(help_text='Locale', related_name='legal_profile_set', to='util.Locale', verbose_name='locale'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='timezone',
            field=models.ForeignKey(help_text='Timezone', related_name='legal_profile_set', to='util.TimeZone', verbose_name='timezone'),
            preserve_default=True,
        ),
    ]
