# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pathlib import Path

from django.conf import settings

from django.db import migrations

from ..models import (
    SubscriptionCategory,
    Module,
    View,
    MenuItem,
    ViewContext,
    AccessRole,
)

from util.models import Status, HttpResourcesConfig, Keyword

BASE_DIR = getattr(settings, "BASE_PATH", Path(".").resolve())


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            lambda apps, schema_editor: Status.import_data(
                BASE_DIR / "saas" / "imports" / "statuses.csv"
            )
        ),
        migrations.RunPython(
            lambda apps, schema_editor: Module.import_data(
                BASE_DIR / "saas" / "imports" / "modules.csv"
            )
        ),
        migrations.RunPython(
            lambda apps, schema_editor: HttpResourcesConfig.import_data(
                BASE_DIR / "saas" / "imports" / "http_resources_config.csv"
            )
        ),
        migrations.RunPython(
            lambda apps, schema_editor: Keyword.import_data(
                BASE_DIR / "saas" / "imports" / "keywords.csv"
            )
        ),
        migrations.RunPython(
            lambda apps, schema_editor: ViewContext.import_data(
                BASE_DIR / "saas" / "imports" / "view_contexts.csv"
            )
        ),
        migrations.RunPython(
            lambda apps, schema_editor: View.import_data(
                BASE_DIR / "saas" / "imports" / "views.csv"
            )
        ),
        migrations.RunPython(
            lambda apps, schema_editor: MenuItem.import_data(
                BASE_DIR / "saas" / "imports" / "menu_items.csv"
            )
        ),
        migrations.RunPython(
            lambda apps, schema_editor: SubscriptionCategory.import_data(
                BASE_DIR / "saas" / "imports" / "subscription_categories.csv"
            )
        ),
        migrations.RunPython(
            lambda apps, schema_editor: AccessRole.import_data(
                BASE_DIR / "saas" / "imports" / "access_roles.csv"
            )
        ),
    ]
