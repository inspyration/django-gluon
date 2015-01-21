# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import util.fields
import base.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('util', '0002_imports'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAccount',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', help_text='Date of creation', default=django.utils.timezone.now, auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', help_text='Date of last modification', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, blank=True, verbose_name='deleted on', null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('created_by', base.fields.UserField(editable=False, related_name='created_saas_accessaccount_set', verbose_name='created by', help_text='The user who created this data', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_saas_accessaccount_set', verbose_name='deleted by', help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'access account',
                'verbose_name_plural': 'access accounts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccessRole',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', help_text='Date of creation', default=django.utils.timezone.now, auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', help_text='Date of last modification', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, blank=True, verbose_name='deleted on', null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('created_by', base.fields.UserField(editable=False, related_name='created_saas_accessrole_set', verbose_name='created by', help_text='The user who created this data', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_saas_accessrole_set', verbose_name='deleted by', help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, null=True)),
                ('groups', models.ManyToManyField(to='auth.Group', verbose_name='groups', help_text='List of groups used by the role')),
                ('last_modified_by', base.fields.UserField(editable=False, related_name='last_modified_saas_accessrole_set', verbose_name='last modified by', help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'access role',
                'verbose_name_plural': 'access roles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', help_text='Date of creation', default=django.utils.timezone.now, auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', help_text='Date of last modification', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, blank=True, verbose_name='deleted on', null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('application', models.BooleanField(verbose_name='Is this module a main application ?', default=True, help_text='Is this module an application ?')),
                ('price', models.DecimalField(decimal_places=2, verbose_name='price', max_digits=5, help_text='Module price')),
                ('created_by', base.fields.UserField(editable=False, related_name='created_saas_module_set', verbose_name='created by', help_text='The user who created this data', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_saas_module_set', verbose_name='deleted by', help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, null=True)),
                ('dependencies', models.ManyToManyField(related_name='dependencies_rel_set', verbose_name='Dependencies', to='saas.Module', help_text='List of modules required to make this one work')),
                ('last_modified_by', base.fields.UserField(editable=False, related_name='last_modified_saas_module_set', verbose_name='last modified by', help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, null=True)),
                ('status', util.fields.StatusField(related_name='status_saas_module_set', verbose_name='status', default=util.fields.get_default_status, to='util.Status')),
            ],
            options={
                'verbose_name': 'module',
                'verbose_name_plural': 'modules',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', help_text='Date of creation', default=django.utils.timezone.now, auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', help_text='Date of last modification', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, blank=True, verbose_name='deleted on', null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('avatar_height', models.PositiveSmallIntegerField(blank=True, verbose_name='avatar height', null=True)),
                ('avatar_width', models.PositiveSmallIntegerField(blank=True, verbose_name='avatar width', null=True)),
                ('avatar', models.ImageField(height_field='avatar_height', width_field='avatar_width', blank=True, verbose_name='avatar', help_text='Avatar', upload_to='media/%(app_label)s/%(class)s/avatars/%Y/%m/%d', null=True, max_length=64)),
                ('first_name', models.CharField(verbose_name='first_name', max_length=127, help_text='Person first name')),
                ('last_name', models.CharField(verbose_name='last name', max_length=127, help_text='Person last name')),
                ('created_by', base.fields.UserField(editable=False, related_name='created_saas_profile_set', verbose_name='created by', help_text='The user who created this data', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_saas_profile_set', verbose_name='deleted by', help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, null=True)),
                ('last_modified_by', base.fields.UserField(editable=False, related_name='last_modified_saas_profile_set', verbose_name='last modified by', help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, null=True)),
                ('locale', models.ForeignKey(related_name='saas_profile_set', verbose_name='locale', help_text='Locale', to='util.Locale')),
                ('timezone', models.ForeignKey(related_name='saas_profile_set', verbose_name='timezone', help_text='Timezone', to='util.TimeZone')),
                ('user', models.OneToOneField(related_name='profile', verbose_name='user', help_text='User linked to this profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', help_text='Date of creation', default=django.utils.timezone.now, auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', help_text='Date of last modification', default=django.utils.timezone.now, auto_now=True)),
                ('deleted_on', models.DateTimeField(editable=False, blank=True, verbose_name='deleted on', null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(editable=False, verbose_name='active', default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255, help_text='Unique name, used in imports/exports features')),
                ('address1', models.CharField(verbose_name='address 1', max_length=255, help_text='first line of the address')),
                ('address2', models.CharField(blank=True, verbose_name='address 2', null=True, help_text='second line of the address', max_length=255)),
                ('zip', models.CharField(verbose_name='zip', max_length=16, help_text='Zip code')),
                ('city', models.CharField(verbose_name='city', max_length=255, help_text='City')),
                ('website', models.CharField(blank=True, verbose_name='website', null=True, help_text='Website URI', max_length=64)),
                ('phone', models.CharField(verbose_name='phone', max_length=16, help_text='Phone number')),
                ('fax', models.CharField(blank=True, verbose_name='fax', null=True, help_text='Fax number', max_length=16)),
                ('tin', models.CharField(verbose_name='tin', max_length=16, help_text='Tax intra. number')),
                ('logo_height', models.PositiveSmallIntegerField(blank=True, verbose_name='logo height', null=True)),
                ('logo_width', models.PositiveSmallIntegerField(blank=True, verbose_name='logo width', null=True)),
                ('logo', models.ImageField(height_field='logo_height', width_field='logo_width', blank=True, verbose_name='logo', help_text='Logo of the instance owner', upload_to='media/%(app_label)s/%(class)s/logos/%Y/%m/%d', null=True, max_length=64)),
                ('opened', models.BooleanField(verbose_name='opened', default=True, help_text='Is the instance is open ?')),
                ('owner', models.CharField(verbose_name='owner', max_length=127, help_text='Owner')),
                ('country', models.ForeignKey(related_name='saas_subscription_set', verbose_name='country', help_text='Country', to='util.Country')),
                ('created_by', base.fields.UserField(editable=False, related_name='created_saas_subscription_set', verbose_name='created by', help_text='The user who created this data', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_saas_subscription_set', verbose_name='deleted by', help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, null=True)),
                ('last_modified_by', base.fields.UserField(editable=False, related_name='last_modified_saas_subscription_set', verbose_name='last modified by', help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, null=True)),
                ('locale', models.ForeignKey(related_name='saas_subscription_set', verbose_name='locale', help_text='Locale', to='util.Locale')),
                ('modules', models.ManyToManyField(to='saas.Module', verbose_name='modules', help_text='List of module installed on the instance')),
                ('state', models.ForeignKey(blank=True, related_name='saas_subscription_set', verbose_name='state', help_text='State', to='util.State', null=True)),
                ('status', util.fields.StatusField(related_name='status_saas_subscription_set', verbose_name='status', default=util.fields.get_default_status, to='util.Status')),
                ('timezone', models.ForeignKey(related_name='saas_subscription_set', verbose_name='timezone', help_text='Timezone', to='util.TimeZone')),
            ],
            options={
                'verbose_name': 'instance',
                'verbose_name_plural': 'instances',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='instance',
            field=models.ForeignKey(to='saas.Subscription', verbose_name='instance', help_text='Role linked to this account'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='last_modified_by',
            field=base.fields.UserField(editable=False, related_name='last_modified_saas_accessaccount_set', verbose_name='last modified by', help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='role',
            field=models.ForeignKey(related_name='saas_access_account_set', verbose_name='role', help_text='Role linked to this account', to='saas.AccessRole'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='status',
            field=util.fields.StatusField(related_name='status_saas_accessaccount_set', verbose_name='status', default=util.fields.get_default_status, to='util.Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='user',
            field=models.ForeignKey(related_name='saas_access_account_set', verbose_name='user', help_text='user who owns this account', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
