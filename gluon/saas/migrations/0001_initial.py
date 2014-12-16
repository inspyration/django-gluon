# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import base.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0001_initial'),
        ('util', '0002_auto_20141205_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the data usable ?', editable=False)),
                ('label', models.CharField(verbose_name='label', help_text='The way the data will be see from foreign objects', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True, max_length=255)),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_saas_accessaccount_set', editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_saas_accessaccount_set', editable=False, verbose_name='deleted by', to=settings.AUTH_USER_MODEL, null=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the data usable ?', editable=False)),
                ('label', models.CharField(verbose_name='label', help_text='The way the data will be see from foreign objects', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True, max_length=255)),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_saas_accessrole_set', editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_saas_accessrole_set', editable=False, verbose_name='deleted by', to=settings.AUTH_USER_MODEL, null=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', to='auth.Group', help_text='List of groups used by the role')),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_saas_accessrole_set', editable=False, verbose_name='last modified by', to=settings.AUTH_USER_MODEL, null=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the data usable ?', editable=False)),
                ('label', models.CharField(verbose_name='label', help_text='The way the data will be see from foreign objects', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True, max_length=255)),
                ('opened', models.BooleanField(default=True, verbose_name='opened', help_text='Is the instance is open ?')),
                ('owner', models.CharField(verbose_name='owner', help_text='Owner', max_length=127)),
                ('address1', models.CharField(verbose_name='address 1', help_text='Address 1 of the instance owner', max_length=255)),
                ('address2', models.CharField(verbose_name='address 2', help_text='Address 2 of the instance owner', max_length=255)),
                ('zip', models.CharField(verbose_name='zip', help_text='Zip of the instance owner', max_length=16)),
                ('city', models.CharField(verbose_name='city', help_text='City of the instance owner', max_length=255)),
                ('website', models.CharField(verbose_name='website', help_text='Website URI', max_length=64)),
                ('phone', models.CharField(verbose_name='phone', help_text='Phone number', max_length=16)),
                ('fax', models.CharField(verbose_name='fax', help_text='Fax number', max_length=16)),
                ('tin', models.CharField(verbose_name='tin', help_text='Tax intra. number', max_length=16)),
                ('logo_height', models.PositiveSmallIntegerField(verbose_name='logo height')),
                ('logo_width', models.PositiveSmallIntegerField(verbose_name='logo width')),
                ('logo', models.ImageField(upload_to='media/saas/logos/%Y/%m/%d', help_text='Logo of the instance owner', max_length=64, width_field=models.PositiveSmallIntegerField(verbose_name='logo width'), height_field=models.PositiveSmallIntegerField(verbose_name='logo height'), verbose_name='logo')),
                ('country', models.ForeignKey(help_text='Country of the instance owner', related_name='saas_instance_set', verbose_name='country', to='util.Country')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_saas_instance_set', editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_saas_instance_set', editable=False, verbose_name='deleted by', to=settings.AUTH_USER_MODEL, null=True)),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_saas_instance_set', editable=False, verbose_name='last modified by', to=settings.AUTH_USER_MODEL, null=True)),
                ('locale', models.ForeignKey(help_text='Locale', related_name='saas_instance_set', verbose_name='locale', to='util.Locale')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the data usable ?', editable=False)),
                ('label', models.CharField(verbose_name='label', help_text='The way the data will be see from foreign objects', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True, max_length=255)),
                ('application', models.BooleanField(default=True, verbose_name='Is this module a main application ?', help_text='Is this module an application ?')),
                ('price', models.DecimalField(max_digits=5, decimal_places=2, verbose_name='price', help_text='Module price')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_saas_module_set', editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_saas_module_set', editable=False, verbose_name='deleted by', to=settings.AUTH_USER_MODEL, null=True)),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_saas_module_set', editable=False, verbose_name='last modified by', to=settings.AUTH_USER_MODEL, null=True)),
                ('dependencies', models.ManyToManyField(help_text='List of modules required to make this one work', related_name='dependencies_rel_+', verbose_name='Dependencies', to='saas.Module')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', help_text='Date of creation')),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', auto_now=True, help_text='Date of last modification')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', help_text='Date of deletion', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='active', help_text='Is the data usable ?', editable=False)),
                ('label', models.CharField(verbose_name='label', help_text='The way the data will be see from foreign objects', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', help_text='Unique name, used in imports/exports features', unique=True, max_length=255)),
                ('first_name', models.CharField(verbose_name='first name', help_text='First name', max_length=32)),
                ('last_name', models.CharField(verbose_name='last name', help_text='Last name', max_length=32)),
                ('avatar_height', models.PositiveSmallIntegerField(verbose_name='avatar height')),
                ('avatar_width', models.PositiveSmallIntegerField(verbose_name='avatar width')),
                ('avatar', models.ImageField(upload_to='media/saas/avatars/%Y/%m/%d', help_text='Avatar', max_length=64, width_field=models.PositiveSmallIntegerField(verbose_name='avatar width'), height_field=models.PositiveSmallIntegerField(verbose_name='avatar height'), verbose_name='avatar')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', related_name='created_saas_profile_set', editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL, null=True)),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', related_name='deleted_saas_profile_set', editable=False, verbose_name='deleted by', to=settings.AUTH_USER_MODEL, null=True)),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_saas_profile_set', editable=False, verbose_name='last modified by', to=settings.AUTH_USER_MODEL, null=True)),
                ('locale', models.ForeignKey(help_text='Locale', related_name='user_set', verbose_name='locale', to='util.Locale')),
                ('timezone', models.ForeignKey(help_text='Timezone', related_name='user_set', verbose_name='timezone', to='util.TimeZone')),
                ('user', models.OneToOneField(help_text='User linked to this profile', related_name='profile', verbose_name='user', to=settings.AUTH_USER_MODEL)),
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
            field=models.ForeignKey(help_text='State of the instance owner', related_name='saas_instance_set', verbose_name='state', to='util.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='timezone',
            field=models.ForeignKey(help_text='Timezone', related_name='saas_instance_set', verbose_name='timezone', to='util.TimeZone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='instance',
            field=models.ForeignKey(help_text='Role linked to this account', verbose_name='instance', to='saas.Instance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='last_modified_by',
            field=base.fields.UserField(help_text='The user who last modified this data', related_name='last_modified_saas_accessaccount_set', editable=False, verbose_name='last modified by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='role',
            field=models.ForeignKey(help_text='Role linked to this account', related_name='saas_access_account_set', verbose_name='role', to='saas.AccessRole'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='user',
            field=models.ForeignKey(help_text='user who owns this account', related_name='saas_access_account_set', verbose_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
