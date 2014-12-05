from django.contrib import admin

from .models import (
    Instance,
    Module,
    AccessAccount,
    AccessRole,
    Profile,
)

admin.register(
    Instance,
    Module,
    AccessAccount,
    AccessRole,
    Profile,
)
