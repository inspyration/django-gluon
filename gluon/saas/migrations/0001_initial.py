# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import base.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('util', '0002_auto_20141205_2217'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAccount',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(editable=False, null=True, verbose_name='deleted on', blank=True)),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255)),
                ('created_by', base.fields.UserField(editable=False, related_name='created_saas_accessaccount_set', null=True, verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_saas_accessaccount_set', null=True, verbose_name='deleted by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccessRole',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(editable=False, null=True, verbose_name='deleted on', blank=True)),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255)),
                ('created_by', base.fields.UserField(editable=False, related_name='created_saas_accessrole_set', null=True, verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_saas_accessrole_set', null=True, verbose_name='deleted by', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(to='auth.Group', verbose_name='groups')),
                ('last_modified_by', base.fields.UserField(editable=False, related_name='last_modified_saas_accessrole_set', null=True, verbose_name='last modified by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(editable=False, null=True, verbose_name='deleted on', blank=True)),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255)),
                ('opened', models.BooleanField(default=True, verbose_name='opened')),
                ('buyer', models.CharField(verbose_name='buyer', max_length=127)),
                ('address1', models.CharField(verbose_name='address 1', max_length=255)),
                ('address2', models.CharField(verbose_name='address 2', max_length=255)),
                ('zip', models.CharField(verbose_name='zip', max_length=16)),
                ('city', models.CharField(verbose_name='city', max_length=255)),
                ('website', models.CharField(verbose_name='website', max_length=64)),
                ('phone', models.CharField(verbose_name='phone', max_length=16)),
                ('fax', models.CharField(verbose_name='fax', max_length=16)),
                ('tin', models.CharField(verbose_name='tin', max_length=16)),
                ('logo_height', models.PositiveSmallIntegerField(verbose_name='logo height')),
                ('logo_width', models.PositiveSmallIntegerField(verbose_name='logo width')),
                ('logo', models.ImageField(upload_to='saas/logos/%Y/%m/%d', height_field=models.PositiveSmallIntegerField(verbose_name='logo height'), width_field=models.PositiveSmallIntegerField(verbose_name='logo width'), verbose_name='logo', max_length=64)),
                ('country', models.ForeignKey(verbose_name='country', related_name='saas_instance_set', to='util.Country')),
                ('created_by', base.fields.UserField(editable=False, related_name='created_saas_instance_set', null=True, verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_saas_instance_set', null=True, verbose_name='deleted by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', base.fields.UserField(editable=False, related_name='last_modified_saas_instance_set', null=True, verbose_name='last modified by', to=settings.AUTH_USER_MODEL)),
                ('locale', models.ForeignKey(verbose_name='locale', related_name='saas_instance_set', to='util.Locale')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(editable=False, null=True, verbose_name='deleted on', blank=True)),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255)),
                ('application', models.BooleanField(default=True, verbose_name='Is this module a main application ?')),
                ('price', models.DecimalField(max_digits=5, decimal_places=2, verbose_name='price')),
                ('created_by', base.fields.UserField(editable=False, related_name='created_saas_module_set', null=True, verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_saas_module_set', null=True, verbose_name='deleted by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', base.fields.UserField(editable=False, related_name='last_modified_saas_module_set', null=True, verbose_name='last modified by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(editable=False, null=True, verbose_name='deleted on', blank=True)),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, unique=True, verbose_name='name', max_length=255)),
                ('first_name', models.CharField(verbose_name='first name', max_length=32)),
                ('last_name', models.CharField(verbose_name='last name', max_length=32)),
                ('avatar_height', models.PositiveSmallIntegerField(verbose_name='avatar height')),
                ('avatar_width', models.PositiveSmallIntegerField(verbose_name='avatar width')),
                ('avatar', models.ImageField(upload_to='saas/avatars/%Y/%m/%d', height_field=models.PositiveSmallIntegerField(verbose_name='avatar height'), width_field=models.PositiveSmallIntegerField(verbose_name='avatar width'), verbose_name='avatar', max_length=64)),
                ('created_by', base.fields.UserField(editable=False, related_name='created_saas_profile_set', null=True, verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', base.fields.UserField(editable=False, related_name='deleted_saas_profile_set', null=True, verbose_name='deleted by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', base.fields.UserField(editable=False, related_name='last_modified_saas_profile_set', null=True, verbose_name='last modified by', to=settings.AUTH_USER_MODEL)),
                ('locale', models.ForeignKey(verbose_name='locale', related_name='user_set', to='util.Locale')),
                ('timezone', models.ForeignKey(verbose_name='timezone', related_name='user_set', to='util.TimeZone')),
                ('user', models.OneToOneField(related_name='profile', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='instance',
            name='modules',
            field=models.ManyToManyField(to='saas.Module', verbose_name='modules'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='state',
            field=models.ForeignKey(verbose_name='state', related_name='saas_instance_set', to='util.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='timezone',
            field=models.ForeignKey(verbose_name='timezone', related_name='saas_instance_set', to='util.TimeZone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='instance',
            field=models.ForeignKey(verbose_name='instances', to='saas.Instance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='last_modified_by',
            field=base.fields.UserField(editable=False, related_name='last_modified_saas_accessaccount_set', null=True, verbose_name='last modified by', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='role',
            field=models.ForeignKey(verbose_name='role', related_name='saas_access_account_set', to='saas.AccessRole'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='user',
            field=models.ForeignKey(verbose_name='user', related_name='saas_access_account_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
