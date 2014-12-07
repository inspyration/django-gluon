from django.contrib import admin

from .models import (
    Instance,
    Module,
    AccessAccount,
    AccessRole,
    Profile,
)

admin.site.register(Instance)
admin.site.register(Module)
admin.site.register(AccessAccount)
admin.site.register(AccessRole)
admin.site.register(Profile)
