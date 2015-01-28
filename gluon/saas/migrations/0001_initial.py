# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import base.fields
import util.mixins
import django.utils.timezone
import util.fields
from django.conf import settings


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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation', auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of last modification', verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, blank=True, help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, unique=True, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='created by', related_name='created_saas_accessaccount_set')),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='deleted by', related_name='deleted_saas_accessaccount_set')),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='last modified by', related_name='last_modified_saas_accessaccount_set')),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation', auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of last modification', verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, blank=True, help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, unique=True, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='created by', related_name='created_saas_accessrole_set')),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='deleted by', related_name='deleted_saas_accessrole_set')),
                ('groups', models.ManyToManyField(verbose_name='groups', to='auth.Group', help_text='List of groups used by the role')),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='last modified by', related_name='last_modified_saas_accessrole_set')),
            ],
            options={
                'verbose_name': 'access role',
                'verbose_name_plural': 'access roles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation', auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of last modification', verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, blank=True, help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, unique=True, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name')),
                ('default', models.BooleanField(default=False, verbose_name='default', help_text='Is this menu item is always displayed ?')),
                ('path', models.CharField(max_length=127, help_text='Menu item link', verbose_name='path')),
                ('icon', models.CharField(max_length=31, help_text='Icon (font-awesome)', verbose_name='icon')),
            ],
            options={
                'verbose_name': 'menu item',
                'verbose_name_plural': 'menu items',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation', auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of last modification', verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, blank=True, help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, unique=True, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name')),
                ('application', models.BooleanField(default=True, verbose_name='Is this module a main application ?', help_text='Is this module an application ?')),
                ('monthly_price', models.DecimalField(verbose_name='price', max_digits=5, decimal_places=2, help_text='Module price')),
                ('yearly_price', models.DecimalField(verbose_name='price', max_digits=5, decimal_places=2, help_text='Module price')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='created by', related_name='created_saas_module_set')),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='deleted by', related_name='deleted_saas_module_set')),
                ('dependencies', models.ManyToManyField(verbose_name='Dependencies', to='saas.Module', related_name='dependencies_rel_set', help_text='List of modules required to make this one work')),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='last modified by', related_name='last_modified_saas_module_set')),
                ('status', util.fields.StatusField(to='util.Status', verbose_name='status', related_name='status_saas_module_set')),
            ],
            options={
                'verbose_name': 'module',
                'verbose_name_plural': 'modules',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation', auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of last modification', verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, blank=True, help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, unique=True, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name')),
                ('message', models.TextField(verbose_name='message', help_text='Message')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='created by', related_name='created_saas_notification_set')),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='deleted by', related_name='deleted_saas_notification_set')),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='last modified by', related_name='last_modified_saas_notification_set')),
                ('status', util.fields.StatusField(to='util.Status', verbose_name='status', related_name='status_saas_notification_set')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation', auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of last modification', verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, blank=True, help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, unique=True, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name')),
                ('avatar_height', models.PositiveSmallIntegerField(verbose_name='avatar height', null=True, blank=True, editable=False)),
                ('avatar_width', models.PositiveSmallIntegerField(verbose_name='avatar width', null=True, blank=True, editable=False)),
                ('avatar', models.ImageField(max_length=64, null=True, upload_to=util.mixins.AvatarMixin.compute_upload_path, help_text='Avatar', verbose_name='avatar', blank=True, height_field='avatar_height', width_field='avatar_width')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='created by', related_name='created_saas_profile_set')),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='deleted by', related_name='deleted_saas_profile_set')),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='last modified by', related_name='last_modified_saas_profile_set')),
                ('locale', models.ForeignKey(help_text='Locale', to='util.Locale', verbose_name='locale', related_name='saas_profile_set')),
                ('notifications', models.ManyToManyField(verbose_name='notifications', blank=True, to='saas.Notification', help_text='Notifications')),
                ('timezone', models.ForeignKey(help_text='Timezone', to='util.TimeZone', verbose_name='timezone', related_name='saas_profile_set')),
                ('user', models.OneToOneField(help_text='User linked to this profile', to=settings.AUTH_USER_MODEL, verbose_name='user', related_name='profile')),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation', auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of last modification', verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, blank=True, help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, unique=True, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name')),
                ('referrer', models.EmailField(max_length=75, blank=True, help_text='Email of the person who recommended this site', verbose_name='referrer')),
                ('company_name', models.CharField(max_length=127, blank=True, help_text='Company name if the subscription is on behalf a company', verbose_name='company name')),
            ],
            options={
                'verbose_name': 'subscription',
                'verbose_name_plural': 'subscriptions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubscriptionCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation', auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of last modification', verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, blank=True, help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, unique=True, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='created by', related_name='created_saas_subscriptioncategory_set')),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='deleted by', related_name='deleted_saas_subscriptioncategory_set')),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='last modified by', related_name='last_modified_saas_subscriptioncategory_set')),
                ('status', util.fields.StatusField(to='util.Status', verbose_name='status', related_name='status_saas_subscriptioncategory_set')),
            ],
            options={
                'verbose_name': 'subscription category',
                'verbose_name_plural': 'subscription categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation', auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of last modification', verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, blank=True, help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, unique=True, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name')),
                ('page_title', models.CharField(max_length=127, help_text='Title of the page', verbose_name='page title')),
                ('page_description', models.CharField(max_length=250, help_text='Description of the page (250 characters max, 200 ideally)', verbose_name='page description')),
            ],
            options={
                'verbose_name': 'view',
                'verbose_name_plural': 'views',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ViewContext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation', auto_now_add=True, verbose_name='created on')),
                ('last_modified_on', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of last modification', verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, editable=False, blank=True, help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(max_length=32, help_text='The way the data will be see from foreign objects', verbose_name='label')),
                ('name', models.CharField(max_length=255, unique=True, editable=False, help_text='Unique name, used in imports/exports features', verbose_name='name')),
                ('created_by', base.fields.UserField(help_text='The user who created this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='created by', related_name='created_saas_viewcontext_set')),
                ('deleted_by', base.fields.UserField(help_text='The user who deleted this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='deleted by', related_name='deleted_saas_viewcontext_set')),
                ('last_modified_by', base.fields.UserField(help_text='The user who last modified this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='last modified by', related_name='last_modified_saas_viewcontext_set')),
            ],
            options={
                'verbose_name': 'view context',
                'verbose_name_plural': 'view contexts',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='view',
            name='context',
            field=models.ForeignKey(help_text='Context of the menu Item', to='saas.ViewContext', verbose_name='context', related_name='view_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='view',
            name='created_by',
            field=base.fields.UserField(help_text='The user who created this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='created by', related_name='created_saas_view_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='view',
            name='deleted_by',
            field=base.fields.UserField(help_text='The user who deleted this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='deleted by', related_name='deleted_saas_view_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='view',
            name='last_modified_by',
            field=base.fields.UserField(help_text='The user who last modified this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='last modified by', related_name='last_modified_saas_view_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='view',
            name='module',
            field=models.ForeignKey(help_text='Module of the view', to='saas.Module', verbose_name='module', related_name='view_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='view',
            name='page_keywords',
            field=models.ManyToManyField(verbose_name='page keywords', blank=True, to='util.Keyword', related_name='view_set', help_text='List of keywords used by the page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='view',
            name='resources_config',
            field=models.ForeignKey(help_text='List of resources used by this view (CSS, JS, Meta, ...)', to='util.HttpResourcesConfig', verbose_name='HTTP resources configuration', blank=True, related_name='view_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscription',
            name='category',
            field=models.ForeignKey(help_text='Subscription category', to='saas.SubscriptionCategory', verbose_name='category', related_name='saas_subscription_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscription',
            name='created_by',
            field=base.fields.UserField(help_text='The user who created this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='created by', related_name='created_saas_subscription_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscription',
            name='deleted_by',
            field=base.fields.UserField(help_text='The user who deleted this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='deleted by', related_name='deleted_saas_subscription_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscription',
            name='last_modified_by',
            field=base.fields.UserField(help_text='The user who last modified this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='last modified by', related_name='last_modified_saas_subscription_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscription',
            name='modules',
            field=models.ManyToManyField(verbose_name='modules', to='saas.Module', help_text='List of module installed on the subscription'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscription',
            name='owner',
            field=models.ForeignKey(help_text='Subscription owner', to=settings.AUTH_USER_MODEL, verbose_name='owner', related_name='saas_subscription_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscription',
            name='status',
            field=util.fields.StatusField(to='util.Status', verbose_name='status', related_name='status_saas_subscription_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='context',
            field=models.ForeignKey(help_text='Context of the menu Item', to='saas.ViewContext', verbose_name='context', related_name='menu_item_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='created_by',
            field=base.fields.UserField(help_text='The user who created this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='created by', related_name='created_saas_menuitem_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='deleted_by',
            field=base.fields.UserField(help_text='The user who deleted this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='deleted by', related_name='deleted_saas_menuitem_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='last_modified_by',
            field=base.fields.UserField(help_text='The user who last modified this data', null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='last modified by', related_name='last_modified_saas_menuitem_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(help_text='Parent directory', null=True, to='saas.MenuItem', verbose_name='parent', blank=True, related_name='directory_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='views',
            field=models.ManyToManyField(verbose_name='views', blank=True, to='saas.View', related_name='menu_item_set', help_text='Views related to this menu item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='role',
            field=models.ForeignKey(help_text='Role linked to this account', to='saas.AccessRole', verbose_name='role', related_name='saas_access_account_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='status',
            field=util.fields.StatusField(to='util.Status', verbose_name='status', related_name='status_saas_accessaccount_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='subscription',
            field=models.ForeignKey(help_text='Role linked to this account', to='saas.Subscription', verbose_name='subscription', related_name='saas_access_account_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessaccount',
            name='user',
            field=models.ForeignKey(help_text='user who owns this account', to=settings.AUTH_USER_MODEL, verbose_name='user', related_name='saas_access_account_set'),
            preserve_default=True,
        ),
    ]
