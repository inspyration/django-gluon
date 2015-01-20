# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import util.fields
import base.fields

from django.utils.timezone import now


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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(verbose_name='created on', default=now, auto_now_add=True, help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', default=now, auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', blank=True, editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(verbose_name='active', editable=False, default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(verbose_name='name', max_length=255, editable=False, help_text='Unique name, used in imports/exports features', unique=True)),
                ('created_by', base.fields.UserField(verbose_name='created by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='created_saas_accessaccount_set', help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(verbose_name='deleted by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='deleted_saas_accessaccount_set', help_text='The user who deleted this data')),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(verbose_name='created on', default=now, auto_now_add=True, help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', default=now, auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', blank=True, editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(verbose_name='active', editable=False, default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(verbose_name='name', max_length=255, editable=False, help_text='Unique name, used in imports/exports features', unique=True)),
                ('created_by', base.fields.UserField(verbose_name='created by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='created_saas_accessrole_set', help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(verbose_name='deleted by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='deleted_saas_accessrole_set', help_text='The user who deleted this data')),
                ('groups', models.ManyToManyField(verbose_name='groups', to='auth.Group', help_text='List of groups used by the role')),
                ('last_modified_by', base.fields.UserField(verbose_name='last modified by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='last_modified_saas_accessrole_set', help_text='The user who last modified this data')),
            ],
            options={
                'verbose_name': 'access role',
                'verbose_name_plural': 'access roles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(verbose_name='created on', default=now, auto_now_add=True, help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', default=now, auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', blank=True, editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(verbose_name='active', editable=False, default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(verbose_name='name', max_length=255, editable=False, help_text='Unique name, used in imports/exports features', unique=True)),
                ('opened', models.BooleanField(verbose_name='opened', default=True, help_text='Is the instance is open ?')),
                ('owner', models.CharField(verbose_name='owner', max_length=127, help_text='Owner')),
                ('address1', models.CharField(verbose_name='address 1', max_length=255, help_text='Address 1 of the instance owner')),
                ('address2', models.CharField(verbose_name='address 2', max_length=255, help_text='Address 2 of the instance owner')),
                ('zip', models.CharField(verbose_name='zip', max_length=16, help_text='Zip of the instance owner')),
                ('city', models.CharField(verbose_name='city', max_length=255, help_text='City of the instance owner')),
                ('website', models.CharField(verbose_name='website', max_length=64, help_text='Website URI')),
                ('phone', models.CharField(verbose_name='phone', max_length=16, help_text='Phone number')),
                ('fax', models.CharField(verbose_name='fax', max_length=16, help_text='Fax number')),
                ('tin', models.CharField(verbose_name='tin', max_length=16, help_text='Tax intra. number')),
                ('logo_height', models.PositiveSmallIntegerField(verbose_name='logo height')),
                ('logo_width', models.PositiveSmallIntegerField(verbose_name='logo width')),
                ('logo', models.ImageField(verbose_name='logo', max_length=64, upload_to='media/saas/logos/%Y/%m/%d', width_field=models.PositiveSmallIntegerField(verbose_name='logo width'), height_field=models.PositiveSmallIntegerField(verbose_name='logo height'), help_text='Logo of the instance owner')),
                ('country', models.ForeignKey(verbose_name='country', to='util.Country', help_text='Country of the instance owner', related_name='saas_instance_set')),
                ('created_by', base.fields.UserField(verbose_name='created by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='created_saas_instance_set', help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(verbose_name='deleted by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='deleted_saas_instance_set', help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(verbose_name='last modified by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='last_modified_saas_instance_set', help_text='The user who last modified this data')),
                ('locale', models.ForeignKey(verbose_name='locale', to='util.Locale', help_text='Locale', related_name='saas_instance_set')),
            ],
            options={
                'verbose_name': 'instance',
                'verbose_name_plural': 'instances',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(verbose_name='created on', default=now, auto_now_add=True, help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', default=now, auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', blank=True, editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(verbose_name='active', editable=False, default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(verbose_name='name', max_length=255, editable=False, help_text='Unique name, used in imports/exports features', unique=True)),
                ('application', models.BooleanField(verbose_name='Is this module a main application ?', default=True, help_text='Is this module an application ?')),
                ('price', models.DecimalField(verbose_name='price', max_digits=5, help_text='Module price', decimal_places=2)),
                ('created_by', base.fields.UserField(verbose_name='created by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='created_saas_module_set', help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(verbose_name='deleted by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='deleted_saas_module_set', help_text='The user who deleted this data')),
                ('dependencies', models.ManyToManyField(verbose_name='Dependencies', related_name='dependencies_rel_set', to='saas.Module', help_text='List of modules required to make this one work')),
                ('last_modified_by', base.fields.UserField(verbose_name='last modified by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='last_modified_saas_module_set', help_text='The user who last modified this data')),
                ('status', util.fields.StatusField(verbose_name='status', default=None, to='util.Status', related_name='status_saas_module_set')),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(verbose_name='created on', default=now, auto_now_add=True, help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', default=now, auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', blank=True, editable=False, null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(verbose_name='active', editable=False, default=True, help_text='Is the data usable ?')),
                ('label', models.CharField(verbose_name='label', max_length=32, help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(verbose_name='name', max_length=255, editable=False, help_text='Unique name, used in imports/exports features', unique=True)),
                ('first_name', models.CharField(verbose_name='first name', max_length=32, help_text='First name')),
                ('last_name', models.CharField(verbose_name='last name', max_length=32, help_text='Last name')),
                ('avatar_height', models.PositiveSmallIntegerField(verbose_name='avatar height')),
                ('avatar_width', models.PositiveSmallIntegerField(verbose_name='avatar width')),
                ('avatar', models.ImageField(verbose_name='avatar', max_length=64, upload_to='media/saas/avatars/%Y/%m/%d', width_field=models.PositiveSmallIntegerField(verbose_name='avatar width'), height_field=models.PositiveSmallIntegerField(verbose_name='avatar height'), help_text='Avatar')),
                ('created_by', base.fields.UserField(verbose_name='created by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='created_saas_profile_set', help_text='The user who created this data')),
                ('deleted_by', base.fields.UserField(verbose_name='deleted by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='deleted_saas_profile_set', help_text='The user who deleted this data')),
                ('last_modified_by', base.fields.UserField(verbose_name='last modified by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='last_modified_saas_profile_set', help_text='The user who last modified this data')),
                ('locale', models.ForeignKey(verbose_name='locale', to='util.Locale', help_text='Locale', related_name='user_set')),
                ('timezone', models.ForeignKey(verbose_name='timezone', to='util.TimeZone', help_text='Timezone', related_name='user_set')),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL, help_text='User linked to this profile', related_name='profile')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='instance',
            name='modules',
            field=models.ManyToManyField(verbose_name='modules', to='saas.Module', help_text='List of module installed on the instance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='state',
            field=models.ForeignKey(verbose_name='state', to='util.State', help_text='State of the instance owner', related_name='saas_instance_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='status',
            field=util.fields.StatusField(verbose_name='status', default=None, to='util.Status', related_name='status_saas_instance_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='timezone',
            field=models.ForeignKey(verbose_name='timezone', to='util.TimeZone', help_text='Timezone', related_name='saas_instance_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='instance',
            field=models.ForeignKey(verbose_name='instance', to='saas.Instance', help_text='Role linked to this account'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='last_modified_by',
            field=base.fields.UserField(verbose_name='last modified by', null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='last_modified_saas_accessaccount_set', help_text='The user who last modified this data'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='role',
            field=models.ForeignKey(verbose_name='role', to='saas.AccessRole', help_text='Role linked to this account', related_name='saas_access_account_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='status',
            field=util.fields.StatusField(verbose_name='status', default=None, to='util.Status', related_name='status_saas_accessaccount_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='user',
            field=models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL, help_text='user who owns this account', related_name='saas_access_account_set'),
            preserve_default=True,
        ),
    ]
