# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import base.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('util', '0002_auto_20141205_2217'),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', null=True)),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', max_length=255, unique=True)),
                ('created_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by', related_name='created_saas_accessaccount_set')),
                ('deleted_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='deleted by', related_name='deleted_saas_accessaccount_set')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccessRole',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', null=True)),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', max_length=255, unique=True)),
                ('created_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by', related_name='created_saas_accessrole_set')),
                ('deleted_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='deleted by', related_name='deleted_saas_accessrole_set')),
                ('groups', models.ManyToManyField(verbose_name='groups', to='auth.Group')),
                ('last_modified_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='last modified by', related_name='last_modified_saas_accessrole_set')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', null=True)),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', max_length=255, unique=True)),
                ('opened', models.BooleanField(verbose_name='opened', default=True)),
                ('buyer', models.CharField(verbose_name='buyer', max_length=127)),
                ('address1', models.CharField(verbose_name='address 1', max_length=255)),
                ('address2', models.CharField(verbose_name='address 2', max_length=255)),
                ('zip', models.CharField(verbose_name='zip', max_length=16)),
                ('website', models.CharField(verbose_name='website', max_length=64)),
                ('phone', models.CharField(verbose_name='phone', max_length=16)),
                ('fax', models.CharField(verbose_name='fax', max_length=16)),
                ('tin', models.CharField(verbose_name='tin', max_length=16)),
                ('logo_height', models.PositiveSmallIntegerField(verbose_name='logo height')),
                ('logo_width', models.PositiveSmallIntegerField(verbose_name='logo width')),
                ('logo', models.ImageField(verbose_name='logo', upload_to='saas/logos/%Y/%m/%d', max_length=64, height_field=models.PositiveSmallIntegerField(verbose_name='logo height'), width_field=models.PositiveSmallIntegerField(verbose_name='logo width'))),
                ('country', models.ForeignKey(verbose_name='country', to='util.Country')),
                ('created_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by', related_name='created_saas_instance_set')),
                ('deleted_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='deleted by', related_name='deleted_saas_instance_set')),
                ('last_modified_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='last modified by', related_name='last_modified_saas_instance_set')),
                ('locale', models.ForeignKey(verbose_name='locale', to='util.Locale')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', null=True)),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', max_length=255, unique=True)),
                ('application', models.BooleanField(verbose_name='Is this module a main application ?', default=True)),
                ('price', models.DecimalField(verbose_name='price', decimal_places=2, max_digits=5)),
                ('created_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by', related_name='created_saas_module_set')),
                ('deleted_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='deleted by', related_name='deleted_saas_module_set')),
                ('last_modified_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='last modified by', related_name='last_modified_saas_module_set')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', null=True)),
                ('active', models.BooleanField(editable=False, default=True, verbose_name='active')),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(editable=False, verbose_name='name', max_length=255, unique=True)),
                ('first_name', models.CharField(verbose_name='first name', max_length=32)),
                ('last_name', models.CharField(verbose_name='last name', max_length=32)),
                ('avatar_height', models.PositiveSmallIntegerField(verbose_name='avatar height')),
                ('avatar_width', models.PositiveSmallIntegerField(verbose_name='avatar width')),
                ('avatar', models.ImageField(verbose_name='avatar', upload_to='saas/avatars/%Y/%m/%d', max_length=64, height_field=models.PositiveSmallIntegerField(verbose_name='avatar height'), width_field=models.PositiveSmallIntegerField(verbose_name='avatar width'))),
                ('created_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by', related_name='created_saas_profile_set')),
                ('deleted_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='deleted by', related_name='deleted_saas_profile_set')),
                ('last_modified_by', base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='last modified by', related_name='last_modified_saas_profile_set')),
                ('locale', models.ForeignKey(verbose_name='locale', to='util.Locale')),
                ('timezone', models.ForeignKey(verbose_name='timezone', to='util.TimeZone')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='user', related_name='profile')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='instance',
            name='modules',
            field=models.ManyToManyField(verbose_name='modules', to='saas.Module'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='state',
            field=models.ForeignKey(verbose_name='state', to='util.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='timezone',
            field=models.ForeignKey(verbose_name='timezone', to='util.TimeZone'),
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
            field=base.fields.UserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='last modified by', related_name='last_modified_saas_accessaccount_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='role',
            field=models.ForeignKey(to='saas.AccessRole', related_name='account_set', verbose_name='role'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='access_account_set', verbose_name='user'),
            preserve_default=True,
        ),
    ]
