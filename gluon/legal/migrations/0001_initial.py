# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import util.mixins
import base.fields
from django.conf import settings
import saas.fields
import django.utils.timezone


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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', help_text='Date of creation', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', help_text='Date of last modification', auto_now=True, default=django.utils.timezone.now)),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', verbose_name='label', max_length=32)),
                ('name', models.CharField(unique=True, help_text='Unique name, used in imports/exports features', verbose_name='name', editable=False, max_length=255)),
                ('address1', models.CharField(help_text='first line of the address', verbose_name='address 1', max_length=255)),
                ('address2', models.CharField(blank=True, help_text='second line of the address', verbose_name='address 2', null=True, max_length=255)),
                ('zip', models.CharField(help_text='Zip code', verbose_name='zip', max_length=16)),
                ('city', models.CharField(help_text='City', verbose_name='city', max_length=255)),
                ('country', models.ForeignKey(to='util.Country', verbose_name='country', help_text='Country', related_name='legal_address_set')),
                ('created_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, verbose_name='created by', help_text='The user who created this data', null=True, editable=False, related_name='created_legal_address_set')),
                ('deleted_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, verbose_name='deleted by', help_text='The user who deleted this data', null=True, editable=False, related_name='deleted_legal_address_set')),
                ('last_modified_by', base.fields.UserField(to=settings.AUTH_USER_MODEL, verbose_name='last modified by', help_text='The user who last modified this data', null=True, editable=False, related_name='last_modified_legal_address_set')),
                ('state', models.ForeignKey(blank=True, to='util.State', verbose_name='state', help_text='State', null=True, related_name='legal_address_set')),
                ('subscription', saas.fields.SubscriptionField(to='saas.Subscription', verbose_name='subscription', editable=False, related_name='subscription_legal_address_set')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', help_text='Date of creation', default=django.utils.timezone.now)),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', help_text='Date of last modification', auto_now=True, default=django.utils.timezone.now)),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, verbose_name='deleted on', null=True, help_text='Date of deletion')),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False, help_text='Is the data usable ?')),
                ('label', models.CharField(help_text='The way the data will be see from foreign objects', verbose_name='label', max_length=32)),
                ('name', models.CharField(unique=True, help_text='Unique name, used in imports/exports features', verbose_name='name', editable=False, max_length=255)),
                ('website', models.CharField(blank=True, help_text='Website URI', verbose_name='website', null=True, max_length=64)),
                ('phone', models.CharField(help_text='Phone number', verbose_name='phone', max_length=16)),
                ('fax', models.CharField(blank=True, help_text='Fax number', verbose_name='fax', null=True, max_length=16)),
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
                ('profile_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='legal.Profile')),
                ('avatar_height', models.PositiveSmallIntegerField(blank=True, editable=False, verbose_name='avatar height', null=True)),
                ('avatar_width', models.PositiveSmallIntegerField(blank=True, editable=False, verbose_name='avatar width', null=True)),
                ('avatar', models.ImageField(blank=True, width_field='avatar_width', verbose_name='avatar', help_text='Avatar', upload_to=util.mixins.AvatarMixin.compute_upload_path, height_field='avatar_height', max_length=64, null=True)),
                ('first_name', models.CharField(help_text='Person first name', verbose_name='first_name', max_length=127)),
                ('last_name', models.CharField(help_text='Person last name', verbose_name='last name', max_length=127)),
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
                ('profile_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='legal.Profile')),
                ('tin', models.CharField(help_text='Tax intra. number', verbose_name='tin', max_length=16)),
                ('logo_height', models.PositiveSmallIntegerField(blank=True, editable=False, verbose_name='logo height', null=True)),
                ('logo_width', models.PositiveSmallIntegerField(blank=True, editable=False, verbose_name='logo width', null=True)),
                ('logo', models.ImageField(blank=True, width_field='logo_width', verbose_name='logo', help_text='Logo', upload_to=util.mixins.LogoMixin.compute_upload_path, height_field='logo_height', max_length=64, null=True)),
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
            field=models.ManyToManyField(blank=True, to='legal.Address', verbose_name='addresses', null=True, help_text='Profile addresses'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='created_by',
            field=base.fields.UserField(to=settings.AUTH_USER_MODEL, verbose_name='created by', help_text='The user who created this data', null=True, editable=False, related_name='created_legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='deleted_by',
            field=base.fields.UserField(to=settings.AUTH_USER_MODEL, verbose_name='deleted by', help_text='The user who deleted this data', null=True, editable=False, related_name='deleted_legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_modified_by',
            field=base.fields.UserField(to=settings.AUTH_USER_MODEL, verbose_name='last modified by', help_text='The user who last modified this data', null=True, editable=False, related_name='last_modified_legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='locale',
            field=models.ForeignKey(to='util.Locale', verbose_name='locale', help_text='Locale', related_name='legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='subscription',
            field=saas.fields.SubscriptionField(to='saas.Subscription', verbose_name='subscription', editable=False, related_name='subscription_legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='timezone',
            field=models.ForeignKey(to='util.TimeZone', verbose_name='timezone', help_text='Timezone', related_name='legal_profile_set'),
            preserve_default=True,
        ),
    ]
