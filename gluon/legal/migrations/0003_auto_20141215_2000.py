# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from django.db import migrations

from saas.models import Module

from pathlib import Path

BASE_DIR = getattr(settings, "BASE_PATH", Path(".").resolve())


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0002_auto_20141207_1547'),
        ('saas', '0002_auto_20141215_2000'),
    ]

    operations = [
        migrations.RunPython(
            lambda apps, schema_editor: Module.import_data(
                BASE_DIR / "legal" / "imports" / "modules.csv"
            )
        ),
    ]
