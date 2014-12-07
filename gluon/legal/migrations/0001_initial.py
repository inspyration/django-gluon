# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import base.fields
import saas.fields


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0001_initial'),
        ('util', '0002_auto_20141205_2217'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, blank=True, editable=False)),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False)),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(unique=True, verbose_name='name', max_length=255, editable=False)),
                ('address1', models.CharField(verbose_name='address 1', max_length=255)),
                ('address2', models.CharField(verbose_name='address 2', max_length=255)),
                ('zip', models.CharField(verbose_name='zip', max_length=16)),
                ('city', models.CharField(verbose_name='city', max_length=255)),
                ('country', models.ForeignKey(verbose_name='country', to='util.Country')),
                ('created_by', base.fields.UserField(null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='created by', related_name='created_legal_address_set')),
                ('deleted_by', base.fields.UserField(null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='deleted by', related_name='deleted_legal_address_set')),
                ('instance', saas.fields.InstanceField(to='saas.Instance', editable=False, verbose_name='instance', related_name='instance_legal_address_set')),
                ('last_modified_by', base.fields.UserField(null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='last modified by', related_name='last_modified_legal_address_set')),
                ('state', models.ForeignKey(verbose_name='state', to='util.State')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(verbose_name='created on', auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(verbose_name='last modified on', auto_now=True)),
                ('deleted_on', models.DateTimeField(verbose_name='deleted on', null=True, blank=True, editable=False)),
                ('active', models.BooleanField(default=True, verbose_name='active', editable=False)),
                ('label', models.CharField(verbose_name='label', max_length=32)),
                ('name', models.CharField(unique=True, verbose_name='name', max_length=255, editable=False)),
                ('website', models.CharField(verbose_name='website', max_length=64)),
                ('phone', models.CharField(verbose_name='phone', max_length=16)),
                ('fax', models.CharField(verbose_name='fax', max_length=16)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('profile_ptr', models.OneToOneField(primary_key=True, auto_created=True, parent_link=True, to='legal.Profile', serialize=False)),
                ('first_name', models.CharField(verbose_name='buyer', max_length=127)),
                ('last_name', models.CharField(verbose_name='buyer', max_length=127)),
                ('avatar_height', models.PositiveSmallIntegerField(verbose_name='avatar height')),
                ('avatar_width', models.PositiveSmallIntegerField(verbose_name='avatar width')),
                ('avatar', models.ImageField(width_field=models.PositiveSmallIntegerField(verbose_name='avatar width'), height_field=models.PositiveSmallIntegerField(verbose_name='avatar height'), verbose_name='avatar', max_length=64, upload_to='legal/persons/avatars/%Y/%m/%d')),
            ],
            options={
                'abstract': False,
            },
            bases=('legal.profile',),
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('profile_ptr', models.OneToOneField(primary_key=True, auto_created=True, parent_link=True, to='legal.Profile', serialize=False)),
                ('tin', models.CharField(verbose_name='tin', max_length=16)),
                ('logo_height', models.PositiveSmallIntegerField(verbose_name='logo height')),
                ('logo_width', models.PositiveSmallIntegerField(verbose_name='logo width')),
                ('logo', models.ImageField(width_field=models.PositiveSmallIntegerField(verbose_name='logo width'), height_field=models.PositiveSmallIntegerField(verbose_name='logo height'), verbose_name='logo', max_length=64, upload_to='legal/entities/logos/%Y/%m/%d')),
            ],
            options={
                'verbose_name_plural': 'entities',
            },
            bases=('legal.profile',),
        ),
        migrations.AddField(
            model_name='profile',
            name='addresses',
            field=models.ManyToManyField(verbose_name='addresses', null=True, blank=True, to='legal.Address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='created_by',
            field=base.fields.UserField(null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='created by', related_name='created_legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='deleted_by',
            field=base.fields.UserField(null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='deleted by', related_name='deleted_legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='instance',
            field=saas.fields.InstanceField(to='saas.Instance', editable=False, verbose_name='instance', related_name='instance_legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_modified_by',
            field=base.fields.UserField(null=True, to=settings.AUTH_USER_MODEL, editable=False, verbose_name='last modified by', related_name='last_modified_legal_profile_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='locale',
            field=models.ForeignKey(verbose_name='locale', to='util.Locale'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='timezone',
            field=models.ForeignKey(verbose_name='timezone', to='util.TimeZone'),
            preserve_default=True,
        ),
    ]
