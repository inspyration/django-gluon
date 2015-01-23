# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import base.fields
import util.fields
import django.utils.timezone
import util.mixins
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('util', '0002_imports'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAccount',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, editable=False, blank=True, verbose_name='deleted on', help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, help_text='Is the data usable ?', editable=False, verbose_name='active')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(help_text='Unique name, used in imports/exports features', max_length=255, editable=False, verbose_name='name', unique=True)),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='created_saas_accessaccount_set', help_text='The user who created this data', editable=False, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='deleted_saas_accessaccount_set', help_text='The user who deleted this data', editable=False, verbose_name='deleted by')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, editable=False, blank=True, verbose_name='deleted on', help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, help_text='Is the data usable ?', editable=False, verbose_name='active')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(help_text='Unique name, used in imports/exports features', max_length=255, editable=False, verbose_name='name', unique=True)),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='created_saas_accessrole_set', help_text='The user who created this data', editable=False, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='deleted_saas_accessrole_set', help_text='The user who deleted this data', editable=False, verbose_name='deleted by')),
                ('groups', models.ManyToManyField(help_text='List of groups used by the role', verbose_name='groups', to='auth.Group')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='last_modified_saas_accessrole_set', help_text='The user who last modified this data', editable=False, verbose_name='last modified by')),
            ],
            options={
                'verbose_name_plural': 'access roles',
                'verbose_name': 'access role',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, editable=False, blank=True, verbose_name='deleted on', help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, help_text='Is the data usable ?', editable=False, verbose_name='active')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(help_text='Unique name, used in imports/exports features', max_length=255, editable=False, verbose_name='name', unique=True)),
                ('path', models.CharField(help_text='Menu item link', max_length=127, verbose_name='path')),
                ('icon', models.CharField(help_text='Icon (font-awesome)', max_length=31, verbose_name='icon')),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='created_saas_menuitem_set', help_text='The user who created this data', editable=False, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='deleted_saas_menuitem_set', help_text='The user who deleted this data', editable=False, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='last_modified_saas_menuitem_set', help_text='The user who last modified this data', editable=False, verbose_name='last modified by')),
                ('parent', models.ForeignKey(to='saas.MenuItem', null=True, help_text='Parent directory', blank=True, related_name='directory_set', verbose_name='parent')),
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
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, editable=False, blank=True, verbose_name='deleted on', help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, help_text='Is the data usable ?', editable=False, verbose_name='active')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(help_text='Unique name, used in imports/exports features', max_length=255, editable=False, verbose_name='name', unique=True)),
                ('application', models.BooleanField(help_text='Is this module an application ?', default=True, verbose_name='Is this module a main application ?')),
                ('price', models.DecimalField(max_digits=5, help_text='Module price', verbose_name='price', decimal_places=2)),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='created_saas_module_set', help_text='The user who created this data', editable=False, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='deleted_saas_module_set', help_text='The user who deleted this data', editable=False, verbose_name='deleted by')),
                ('dependencies', models.ManyToManyField(to='saas.Module', help_text='List of modules required to make this one work', verbose_name='Dependencies', related_name='dependencies_rel_set')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='last_modified_saas_module_set', help_text='The user who last modified this data', editable=False, verbose_name='last modified by')),
                ('status', util.fields.StatusField(related_name='status_saas_module_set', to='util.Status', default=util.fields.get_default_status, verbose_name='status')),
            ],
            options={
                'verbose_name_plural': 'modules',
                'verbose_name': 'module',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, editable=False, blank=True, verbose_name='deleted on', help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, help_text='Is the data usable ?', editable=False, verbose_name='active')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(help_text='Unique name, used in imports/exports features', max_length=255, editable=False, verbose_name='name', unique=True)),
                ('message', models.TextField(help_text='Message', verbose_name='message')),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='created_saas_notification_set', help_text='The user who created this data', editable=False, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='deleted_saas_notification_set', help_text='The user who deleted this data', editable=False, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='last_modified_saas_notification_set', help_text='The user who last modified this data', editable=False, verbose_name='last modified by')),
                ('status', util.fields.StatusField(related_name='status_saas_notification_set', to='util.Status', default=util.fields.get_default_status, verbose_name='status')),
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
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, editable=False, blank=True, verbose_name='deleted on', help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, help_text='Is the data usable ?', editable=False, verbose_name='active')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(help_text='Unique name, used in imports/exports features', max_length=255, editable=False, verbose_name='name', unique=True)),
                ('avatar_height', models.PositiveSmallIntegerField(null=True, editable=False, blank=True, verbose_name='avatar height')),
                ('avatar_width', models.PositiveSmallIntegerField(null=True, editable=False, blank=True, verbose_name='avatar width')),
                ('avatar', models.ImageField(max_length=64, null=True, upload_to=util.mixins.AvatarMixin.compute_upload_path, help_text='Avatar', blank=True, height_field='avatar_height', width_field='avatar_width', verbose_name='avatar')),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='created_saas_profile_set', help_text='The user who created this data', editable=False, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='deleted_saas_profile_set', help_text='The user who deleted this data', editable=False, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='last_modified_saas_profile_set', help_text='The user who last modified this data', editable=False, verbose_name='last modified by')),
                ('locale', models.ForeignKey(to='util.Locale', related_name='saas_profile_set', help_text='Locale', verbose_name='locale')),
                ('notifications', models.ManyToManyField(help_text='Notifications', blank=True, verbose_name='notifications', to='saas.Notification')),
                ('timezone', models.ForeignKey(to='util.TimeZone', related_name='saas_profile_set', help_text='Timezone', verbose_name='timezone')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, help_text='User linked to this profile', related_name='profile', verbose_name='user')),
            ],
            options={
                'verbose_name_plural': 'profiles',
                'verbose_name': 'profile',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, editable=False, blank=True, verbose_name='deleted on', help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, help_text='Is the data usable ?', editable=False, verbose_name='active')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(help_text='Unique name, used in imports/exports features', max_length=255, editable=False, verbose_name='name', unique=True)),
                ('address1', models.CharField(help_text='first line of the address', max_length=255, verbose_name='address 1')),
                ('address2', models.CharField(null=True, max_length=255, blank=True, verbose_name='address 2', help_text='second line of the address')),
                ('zip', models.CharField(help_text='Zip code', max_length=16, verbose_name='zip')),
                ('city', models.CharField(help_text='City', max_length=255, verbose_name='city')),
                ('website', models.CharField(null=True, max_length=64, blank=True, verbose_name='website', help_text='Website URI')),
                ('phone', models.CharField(help_text='Phone number', max_length=16, verbose_name='phone')),
                ('fax', models.CharField(null=True, max_length=16, blank=True, verbose_name='fax', help_text='Fax number')),
                ('tin', models.CharField(help_text='Tax intra. number', max_length=16, verbose_name='tin')),
                ('logo_height', models.PositiveSmallIntegerField(null=True, editable=False, blank=True, verbose_name='logo height')),
                ('logo_width', models.PositiveSmallIntegerField(null=True, editable=False, blank=True, verbose_name='logo width')),
                ('logo', models.ImageField(max_length=64, null=True, upload_to=util.mixins.LogoMixin.compute_upload_path, help_text='Logo of the instance owner', blank=True, height_field='logo_height', width_field='logo_width', verbose_name='logo')),
                ('opened', models.BooleanField(help_text='Is the instance is open ?', default=True, verbose_name='opened')),
                ('owner', models.CharField(help_text='Owner', max_length=127, verbose_name='owner')),
                ('country', models.ForeignKey(to='util.Country', related_name='saas_subscription_set', help_text='Country', verbose_name='country')),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='created_saas_subscription_set', help_text='The user who created this data', editable=False, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='deleted_saas_subscription_set', help_text='The user who deleted this data', editable=False, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='last_modified_saas_subscription_set', help_text='The user who last modified this data', editable=False, verbose_name='last modified by')),
                ('locale', models.ForeignKey(to='util.Locale', related_name='saas_subscription_set', help_text='Locale', verbose_name='locale')),
                ('modules', models.ManyToManyField(help_text='List of module installed on the instance', verbose_name='modules', to='saas.Module')),
                ('state', models.ForeignKey(to='util.State', null=True, help_text='State', blank=True, related_name='saas_subscription_set', verbose_name='state')),
                ('status', util.fields.StatusField(related_name='status_saas_subscription_set', to='util.Status', default=util.fields.get_default_status, verbose_name='status')),
                ('timezone', models.ForeignKey(to='util.TimeZone', related_name='saas_subscription_set', help_text='Timezone', verbose_name='timezone')),
            ],
            options={
                'verbose_name_plural': 'instances',
                'verbose_name': 'instance',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_on', models.DateTimeField(help_text='Date of creation', auto_now_add=True, default=django.utils.timezone.now, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', default=django.utils.timezone.now, verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, editable=False, blank=True, verbose_name='deleted on', help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, help_text='Is the data usable ?', editable=False, verbose_name='active')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', max_length=32, verbose_name='label')),
                ('name', models.CharField(help_text='Unique name, used in imports/exports features', max_length=255, editable=False, verbose_name='name', unique=True)),
                ('page_title', models.CharField(help_text='Title of the page', max_length=127, verbose_name='page title')),
                ('page_description', models.CharField(help_text='Description of the page (250 characters max, 200 ideally)', max_length=250, verbose_name='page description')),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='created_saas_view_set', help_text='The user who created this data', editable=False, verbose_name='created by')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='deleted_saas_view_set', help_text='The user who deleted this data', editable=False, verbose_name='deleted by')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='last_modified_saas_view_set', help_text='The user who last modified this data', editable=False, verbose_name='last modified by')),
                ('module', models.ForeignKey(to='saas.Module', related_name='view_set', help_text='Module of the view', verbose_name='module')),
                ('page_keywords', models.ManyToManyField(to='util.Keyword', help_text='List of keywords used by the page', blank=True, verbose_name='page keywords', related_name='view_set')),
                ('resources_config', models.ForeignKey(to='util.HttpResourcesConfig', blank=True, related_name='view_set', help_text='List of resources used by this view (CSS, JS, Meta, ...)', verbose_name='HTTP resources configuration')),
            ],
            options={
                'verbose_name_plural': 'views',
                'verbose_name': 'view',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='views',
            field=models.ManyToManyField(to='saas.View', help_text='Views related to this menu item', blank=True, verbose_name='views', related_name='menu_item_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='instance',
            field=models.ForeignKey(to='saas.Subscription', help_text='Role linked to this account', verbose_name='instance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='last_modified_by',
            field=base.fields.UserField(to=settings.AUTH_USER_MODEL, null=True, related_name='last_modified_saas_accessaccount_set', help_text='The user who last modified this data', editable=False, verbose_name='last modified by'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='role',
            field=models.ForeignKey(to='saas.AccessRole', related_name='saas_access_account_set', help_text='Role linked to this account', verbose_name='role'),
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
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='saas_access_account_set', help_text='user who owns this account', verbose_name='user'),
            preserve_default=True,
        ),
    ]
