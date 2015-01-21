# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import base.fields
import util.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('util', '0002_imports'),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(help_text='Date of creation', verbose_name='created on', auto_now_add=True, default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', auto_now=True, default=django.utils.timezone.now)),
                ('deleted_on', models.DateTimeField(null=True, help_text='Date of deletion', editable=False, verbose_name='deleted on', blank=True)),
                ('active', models.BooleanField(default=True, help_text='Is the data usable ?', editable=False, verbose_name='active')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(max_length=255, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True, editable=False)),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_saas_accessaccount_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_saas_accessaccount_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='deleted by')),
            ],
            options={
                'verbose_name_plural': 'access accounts',
                'verbose_name': 'access account',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccessRole',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(help_text='Date of creation', verbose_name='created on', auto_now_add=True, default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', auto_now=True, default=django.utils.timezone.now)),
                ('deleted_on', models.DateTimeField(null=True, help_text='Date of deletion', editable=False, verbose_name='deleted on', blank=True)),
                ('active', models.BooleanField(default=True, help_text='Is the data usable ?', editable=False, verbose_name='active')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(max_length=255, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True, editable=False)),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_saas_accessrole_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_saas_accessrole_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='deleted by')),
                ('groups', models.ManyToManyField(help_text='List of groups used by the role', to='auth.Group', verbose_name='groups')),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_saas_accessrole_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='last modified by')),
            ],
            options={
                'verbose_name_plural': 'access roles',
                'verbose_name': 'access role',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(help_text='Date of creation', verbose_name='created on', auto_now_add=True, default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', auto_now=True, default=django.utils.timezone.now)),
                ('deleted_on', models.DateTimeField(null=True, help_text='Date of deletion', editable=False, verbose_name='deleted on', blank=True)),
                ('active', models.BooleanField(default=True, help_text='Is the data usable ?', editable=False, verbose_name='active')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(max_length=255, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True, editable=False)),
                ('address1', models.CharField(help_text='first line of the address', max_length=255, verbose_name='address 1')),
                ('address2', models.CharField(help_text='second line of the address', max_length=255, verbose_name='address 2')),
                ('zip', models.CharField(help_text='Zip code', max_length=16, verbose_name='zip')),
                ('city', models.CharField(help_text='City', max_length=255, verbose_name='city')),
                ('website', models.CharField(help_text='Website URI', max_length=64, verbose_name='website')),
                ('phone', models.CharField(help_text='Phone number', max_length=16, verbose_name='phone')),
                ('fax', models.CharField(help_text='Fax number', max_length=16, verbose_name='fax')),
                ('tin', models.CharField(help_text='Tax intra. number', max_length=16, verbose_name='tin')),
                ('logo_height', models.PositiveSmallIntegerField(verbose_name='logo height')),
                ('logo_width', models.PositiveSmallIntegerField(verbose_name='logo width')),
                ('logo', models.ImageField(help_text='Logo of the instance owner', verbose_name='logo', height_field=models.PositiveSmallIntegerField(verbose_name='logo height'), width_field=models.PositiveSmallIntegerField(verbose_name='logo width'), max_length=64, upload_to='media/%(app_label)s/%(class)s/logos/%Y/%m/%d')),
                ('opened', models.BooleanField(help_text='Is the instance is open ?', default=True, verbose_name='opened')),
                ('owner', models.CharField(help_text='Owner', max_length=127, verbose_name='owner')),
                ('country', models.ForeignKey(help_text='Country', related_name='saas_instance_set', to='util.Country', verbose_name='country')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_saas_instance_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_saas_instance_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_saas_instance_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='last modified by')),
                ('locale', models.ForeignKey(help_text='Locale', related_name='saas_instance_set', to='util.Locale', verbose_name='locale')),
            ],
            options={
                'verbose_name_plural': 'instances',
                'verbose_name': 'instance',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(help_text='Date of creation', verbose_name='created on', auto_now_add=True, default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', auto_now=True, default=django.utils.timezone.now)),
                ('deleted_on', models.DateTimeField(null=True, help_text='Date of deletion', editable=False, verbose_name='deleted on', blank=True)),
                ('active', models.BooleanField(default=True, help_text='Is the data usable ?', editable=False, verbose_name='active')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(max_length=255, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True, editable=False)),
                ('application', models.BooleanField(help_text='Is this module an application ?', default=True, verbose_name='Is this module a main application ?')),
                ('price', models.DecimalField(decimal_places=2, help_text='Module price', max_digits=5, verbose_name='price')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_saas_module_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_saas_module_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='deleted by')),
                ('dependencies', models.ManyToManyField(help_text='List of modules required to make this one work', related_name='dependencies_rel_set', to='saas.Module', verbose_name='Dependencies')),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_saas_module_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='last modified by')),
                ('status', util.fields.StatusField(related_name='status_saas_module_set', to='util.Status', default=util.fields.get_default_status, verbose_name='status')),
            ],
            options={
                'verbose_name_plural': 'modules',
                'verbose_name': 'module',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(help_text='Date of creation', verbose_name='created on', auto_now_add=True, default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', verbose_name='last modified on', auto_now=True, default=django.utils.timezone.now)),
                ('deleted_on', models.DateTimeField(null=True, help_text='Date of deletion', editable=False, verbose_name='deleted on', blank=True)),
                ('active', models.BooleanField(default=True, help_text='Is the data usable ?', editable=False, verbose_name='active')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(max_length=255, help_text='Unique name, used in imports/exports features', verbose_name='name', unique=True, editable=False)),
                ('first_name', models.CharField(help_text='First name', max_length=32, verbose_name='first name')),
                ('last_name', models.CharField(help_text='Last name', max_length=32, verbose_name='last name')),
                ('avatar_height', models.PositiveSmallIntegerField(verbose_name='avatar height')),
                ('avatar_width', models.PositiveSmallIntegerField(verbose_name='avatar width')),
                ('avatar', models.ImageField(help_text='Avatar', verbose_name='avatar', height_field=models.PositiveSmallIntegerField(verbose_name='avatar height'), width_field=models.PositiveSmallIntegerField(verbose_name='avatar width'), max_length=64, upload_to='media/saas/avatars/%Y/%m/%d')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_saas_profile_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_saas_profile_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_saas_profile_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='last modified by')),
                ('locale', models.ForeignKey(help_text='Locale', related_name='user_set', to='util.Locale', verbose_name='locale')),
                ('timezone', models.ForeignKey(help_text='Timezone', related_name='user_set', to='util.TimeZone', verbose_name='timezone')),
                ('user', models.OneToOneField(help_text='User linked to this profile', related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name_plural': 'profiles',
                'verbose_name': 'profile',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='instance',
            name='modules',
            field=models.ManyToManyField(help_text='List of module installed on the instance', to='saas.Module', verbose_name='modules'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='state',
            field=models.ForeignKey(help_text='State', related_name='saas_instance_set', to='util.State', verbose_name='state'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='status',
            field=util.fields.StatusField(related_name='status_saas_instance_set', to='util.Status', default=util.fields.get_default_status, verbose_name='status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='timezone',
            field=models.ForeignKey(help_text='Timezone', related_name='saas_instance_set', to='util.TimeZone', verbose_name='timezone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='instance',
            field=models.ForeignKey(help_text='Role linked to this account', to='saas.Instance', verbose_name='instance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='last_modified_by',
            field=base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_saas_accessaccount_set', to=settings.AUTH_USER_MODEL, null=True, editable=False, verbose_name='last modified by'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='role',
            field=models.ForeignKey(help_text='Role linked to this account', related_name='saas_access_account_set', to='saas.AccessRole', verbose_name='role'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='status',
            field=util.fields.StatusField(related_name='status_saas_accessaccount_set', to='util.Status', default=util.fields.get_default_status, verbose_name='status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='user',
            field=models.ForeignKey(help_text='user who owns this account', related_name='saas_access_account_set', to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=True,
        ),
    ]
