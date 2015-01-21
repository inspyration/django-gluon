from django.contrib import admin

from .models import (
    Subscription,
    Module,
    AccessAccount,
    AccessRole,
    Profile,
)

admin.site.register(Subscription)
admin.site.register(Module)
admin.site.register(AccessAccount)
admin.site.register(AccessRole)
admin.site.register(Profile)
