# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from django.db import migrations

from ..models import Module

from pathlib import Path

BASE_DIR = getattr(settings, "BASE_PATH", Path(".").resolve())


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            lambda apps, schema_editor: Module.import_data(
                BASE_DIR / "saas" / "imports" / "modules.csv"
            )
        ),
    ]
