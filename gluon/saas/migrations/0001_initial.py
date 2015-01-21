# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import base.fields
import django.utils.timezone
import util.fields


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0002_imports'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date of creation', default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, help_text='Date of last modification', default=django.utils.timezone.now, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(editable=False, default=True, help_text='Is the data usable ?', verbose_name='active')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(editable=False, max_length=255, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True)),
                ('created_by', base.fields.UserField(related_name='created_saas_accessaccount_set', help_text='The user who created this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(related_name='deleted_saas_accessaccount_set', help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='deleted by')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date of creation', default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, help_text='Date of last modification', default=django.utils.timezone.now, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(editable=False, default=True, help_text='Is the data usable ?', verbose_name='active')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(editable=False, max_length=255, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True)),
                ('created_by', base.fields.UserField(related_name='created_saas_accessrole_set', help_text='The user who created this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(related_name='deleted_saas_accessrole_set', help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='deleted by')),
                ('groups', models.ManyToManyField(to='auth.Group', help_text='List of groups used by the role', verbose_name='groups')),
                ('last_modified_by', base.fields.UserField(related_name='last_modified_saas_accessrole_set', help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='last modified by')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date of creation', default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, help_text='Date of last modification', default=django.utils.timezone.now, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(editable=False, default=True, help_text='Is the data usable ?', verbose_name='active')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(editable=False, max_length=255, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True)),
                ('address1', models.CharField(max_length=255, help_text='first line of the address', verbose_name='address 1')),
                ('address2', models.CharField(blank=True, max_length=255, verbose_name='address 2', help_text='second line of the address', null=True)),
                ('zip', models.CharField(max_length=16, help_text='Zip code', verbose_name='zip')),
                ('city', models.CharField(max_length=255, help_text='City', verbose_name='city')),
                ('website', models.CharField(blank=True, max_length=64, verbose_name='website', help_text='Website URI', null=True)),
                ('phone', models.CharField(max_length=16, help_text='Phone number', verbose_name='phone')),
                ('fax', models.CharField(blank=True, max_length=16, verbose_name='fax', help_text='Fax number', null=True)),
                ('tin', models.CharField(blank=True, max_length=16, verbose_name='tin', help_text='Tax intra. number', null=True)),
                ('logo_height', models.PositiveSmallIntegerField(blank=True, verbose_name='logo height')),
                ('logo_width', models.PositiveSmallIntegerField(blank=True, verbose_name='logo width')),
                ('logo', models.ImageField(upload_to='media/%(app_label)s/%(class)s/logos/%Y/%m/%d', max_length=64, help_text='Logo of the instance owner', height_field=models.PositiveSmallIntegerField(blank=True, verbose_name='logo height'), blank=True, width_field=models.PositiveSmallIntegerField(blank=True, verbose_name='logo width'), null=True, verbose_name='logo')),
                ('opened', models.BooleanField(default=True, help_text='Is the instance is open ?', verbose_name='opened')),
                ('owner', models.CharField(max_length=127, help_text='Owner', verbose_name='owner')),
                ('country', models.ForeignKey(related_name='saas_instance_set', help_text='Country', to='util.Country', verbose_name='country')),
                ('created_by', base.fields.UserField(related_name='created_saas_instance_set', help_text='The user who created this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(related_name='deleted_saas_instance_set', help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(related_name='last_modified_saas_instance_set', help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='last modified by')),
                ('locale', models.ForeignKey(related_name='saas_instance_set', help_text='Locale', to='util.Locale', verbose_name='locale')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date of creation', default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, help_text='Date of last modification', default=django.utils.timezone.now, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(editable=False, default=True, help_text='Is the data usable ?', verbose_name='active')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(editable=False, max_length=255, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True)),
                ('application', models.BooleanField(default=True, help_text='Is this module an application ?', verbose_name='Is this module a main application ?')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, help_text='Module price', verbose_name='price')),
                ('created_by', base.fields.UserField(related_name='created_saas_module_set', help_text='The user who created this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(related_name='deleted_saas_module_set', help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='deleted by')),
                ('dependencies', models.ManyToManyField(related_name='dependencies_rel_set', to='saas.Module', help_text='List of modules required to make this one work', verbose_name='Dependencies')),
                ('last_modified_by', base.fields.UserField(related_name='last_modified_saas_module_set', help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='last modified by')),
                ('status', util.fields.StatusField(related_name='status_saas_module_set', default=util.fields.get_default_status, to='util.Status', verbose_name='status')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date of creation', default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, help_text='Date of last modification', default=django.utils.timezone.now, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(editable=False, default=True, help_text='Is the data usable ?', verbose_name='active')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(editable=False, max_length=255, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True)),
                ('first_name', models.CharField(max_length=32, help_text='First name', verbose_name='first name')),
                ('last_name', models.CharField(max_length=32, help_text='Last name', verbose_name='last name')),
                ('avatar_height', models.PositiveSmallIntegerField(verbose_name='avatar height')),
                ('avatar_width', models.PositiveSmallIntegerField(verbose_name='avatar width')),
                ('avatar', models.ImageField(upload_to='media/saas/avatars/%Y/%m/%d', max_length=64, help_text='Avatar', height_field=models.PositiveSmallIntegerField(verbose_name='avatar height'), width_field=models.PositiveSmallIntegerField(verbose_name='avatar width'), verbose_name='avatar')),
                ('created_by', base.fields.UserField(related_name='created_saas_profile_set', help_text='The user who created this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(related_name='deleted_saas_profile_set', help_text='The user who deleted this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(related_name='last_modified_saas_profile_set', help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='last modified by')),
                ('locale', models.ForeignKey(related_name='user_set', help_text='Locale', to='util.Locale', verbose_name='locale')),
                ('timezone', models.ForeignKey(related_name='user_set', help_text='Timezone', to='util.TimeZone', verbose_name='timezone')),
                ('user', models.OneToOneField(related_name='profile', help_text='User linked to this profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
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
            field=models.ManyToManyField(to='saas.Module', help_text='List of module installed on the instance', verbose_name='modules'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='state',
            field=models.ForeignKey(related_name='saas_instance_set', help_text='State', to='util.State', blank=True, null=True, verbose_name='state'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='status',
            field=util.fields.StatusField(related_name='status_saas_instance_set', default=util.fields.get_default_status, to='util.Status', verbose_name='status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='timezone',
            field=models.ForeignKey(related_name='saas_instance_set', help_text='Timezone', to='util.TimeZone', verbose_name='timezone'),
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
            field=base.fields.UserField(related_name='last_modified_saas_accessaccount_set', help_text='The user who last modified this data', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='last modified by'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='role',
            field=models.ForeignKey(related_name='saas_access_account_set', help_text='Role linked to this account', to='saas.AccessRole', verbose_name='role'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='status',
            field=util.fields.StatusField(related_name='status_saas_accessaccount_set', default=util.fields.get_default_status, to='util.Status', verbose_name='status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='user',
            field=models.ForeignKey(related_name='saas_access_account_set', help_text='user who owns this account', to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=True,
        ),
    ]
