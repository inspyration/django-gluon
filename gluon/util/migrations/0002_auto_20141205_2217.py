# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from django.db import migrations

from ..models import Country, State, Locale, TimeZone

from pathlib import Path

BASE_DIR = getattr(settings, "BASE_PATH", Path(".").resolve())


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            lambda apps, schema_editor: Country.import_data(
                BASE_DIR / "util" / "imports" / "countries.csv"
            )
        ),
        migrations.RunPython(
            lambda apps, schema_editor: State.import_data(
                BASE_DIR / "util" / "imports" / "states.csv"
            )
        ),
        migrations.RunPython(
            lambda apps, schema_editor: TimeZone.import_data(
                BASE_DIR / "util" / "imports" / "timezones.csv")
        ),
        migrations.RunPython(
            lambda apps, schema_editor: Locale.import_data(
                BASE_DIR / "util" / "imports" / "locales.csv"
            )
        ),
    ]
