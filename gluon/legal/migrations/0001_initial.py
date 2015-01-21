# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import base.fields
import django.utils.timezone
from django.conf import settings
import saas.fields


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0002_imports'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saas', '0002_imports'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date of creation', verbose_name='created on', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', auto_now=True, verbose_name='last modified on', default=django.utils.timezone.now)),
                ('deleted_on', models.DateTimeField(blank=True, null=True, help_text='Date of deletion', verbose_name='deleted on', editable=False)),
                ('active', models.BooleanField(help_text='Is the data usable ?', verbose_name='active', editable=False, default=True)),
                ('label', models.CharField(max_length=32, verbose_name='label', help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(max_length=255, verbose_name='name', help_text='Unique name, used in imports/exports features', editable=False, unique=True)),
                ('address1', models.CharField(max_length=255, verbose_name='address 1', help_text='first line of the address')),
                ('address2', models.CharField(blank=True, null=True, max_length=255, verbose_name='address 2', help_text='second line of the address')),
                ('zip', models.CharField(max_length=16, verbose_name='zip', help_text='Zip code')),
                ('city', models.CharField(max_length=255, verbose_name='city', help_text='City')),
                ('country', models.ForeignKey(help_text='Country', verbose_name='country', to='util.Country', related_name='legal_address_set')),
                ('created_by', base.fields.UserField(null=True, editable=False, help_text='The user who created this data', verbose_name='created by', to=settings.AUTH_USER_MODEL, related_name='created_legal_address_set')),
                ('deleted_by', base.fields.UserField(null=True, editable=False, help_text='The user who deleted this data', verbose_name='deleted by', to=settings.AUTH_USER_MODEL, related_name='deleted_legal_address_set')),
                ('last_modified_by', base.fields.UserField(null=True, editable=False, help_text='The user who last modified this data', verbose_name='last modified by', to=settings.AUTH_USER_MODEL, related_name='last_modified_legal_address_set')),
                ('state', models.ForeignKey(blank=True, null=True, help_text='State', verbose_name='state', to='util.State', related_name='legal_address_set')),
                ('subscription', saas.fields.SubscriptionField(editable=False, verbose_name='instance', to='saas.Subscription', related_name='instance_legal_address_set')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Date of creation', verbose_name='created on', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(help_text='Date of last modification', auto_now=True, verbose_name='last modified on', default=django.utils.timezone.now)),
                ('deleted_on', models.DateTimeField(blank=True, null=True, help_text='Date of deletion', verbose_name='deleted on', editable=False)),
                ('active', models.BooleanField(help_text='Is the data usable ?', verbose_name='active', editable=False, default=True)),
                ('label', models.CharField(max_length=32, verbose_name='label', help_text='The way the data will be see from foreign objects')),
                ('name', models.CharField(max_length=255, verbose_name='name', help_text='Unique name, used in imports/exports features', editable=False, unique=True)),
                ('website', models.CharField(blank=True, null=True, max_length=64, verbose_name='website', help_text='Website URI')),
                ('phone', models.CharField(max_length=16, verbose_name='phone', help_text='Phone number')),
                ('fax', models.CharField(blank=True, null=True, max_length=16, verbose_name='fax', help_text='Fax number')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('profile_ptr', models.OneToOneField(serialize=False, to='legal.Profile', auto_created=True, primary_key=True, parent_link=True)),
                ('avatar_height', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='avatar height')),
                ('avatar_width', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='avatar width')),
                ('avatar', models.ImageField(blank=True, null=True, max_length=64, upload_to='media/%(app_label)s/%(class)s/avatars/%Y/%m/%d', width_field='avatar_width', height_field='avatar_height', help_text='Avatar', verbose_name='avatar')),
                ('first_name', models.CharField(max_length=127, verbose_name='first_name', help_text='Person first name')),
                ('last_name', models.CharField(max_length=127, verbose_name='last name', help_text='Person last name')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
            bases=('legal.profile', models.Model),
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('profile_ptr', models.OneToOneField(serialize=False, to='legal.Profile', auto_created=True, primary_key=True, parent_link=True)),
                ('tin', models.CharField(max_length=16, verbose_name='tin', help_text='Tax intra. number')),
                ('logo_height', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='logo height')),
                ('logo_width', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='logo width')),
                ('logo', models.ImageField(blank=True, null=True, max_length=64, upload_to='media/%(app_label)s/%(class)s/logos/%Y/%m/%d', width_field='logo_width', height_field='logo_height', help_text='Logo of the instance owner', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'entity',
                'verbose_name_plural': 'entities',
            },
            bases=('legal.profile', models.Model),
        ),
        migrations.AddField(
            model_name='profile',
            name='addresses',
            field=models.ManyToManyField(blank=True, null=True, help_text='Profile addresses', verbose_name='addresses', to='legal.Address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='created_by',
            field=base.fields.UserField(null=True, editable=False, help_text='The user who created this data', verbose_name='created by', to=settings.AUTH_USER_MODEL, related_name='created_legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='deleted_by',
            field=base.fields.UserField(null=True, editable=False, help_text='The user who deleted this data', verbose_name='deleted by', to=settings.AUTH_USER_MODEL, related_name='deleted_legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_modified_by',
            field=base.fields.UserField(null=True, editable=False, help_text='The user who last modified this data', verbose_name='last modified by', to=settings.AUTH_USER_MODEL, related_name='last_modified_legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='locale',
            field=models.ForeignKey(help_text='Locale', verbose_name='locale', to='util.Locale', related_name='legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='subscription',
            field=saas.fields.SubscriptionField(editable=False, verbose_name='instance', to='saas.Subscription', related_name='instance_legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='timezone',
            field=models.ForeignKey(help_text='Timezone', verbose_name='timezone', to='util.TimeZone', related_name='legal_profile_set'),
            preserve_default=True,
        ),
    ]
