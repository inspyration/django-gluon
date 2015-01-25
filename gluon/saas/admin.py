from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import (
    Subscription,
    Module,
    AccessAccount,
    AccessRole,
    Notification,
    Profile,
    View,
    MenuItem,
)


class ProfileInline(admin.StackedInline):
    model = Profile
    fk_name = "user"
    can_delete = False


class ProfileAdmin(UserAdmin):
    inlines = (ProfileInline, )


admin.site.register(Subscription)
admin.site.register(Module)
admin.site.register(AccessAccount)
admin.site.register(AccessRole)
admin.site.register(Notification)
admin.site.register(View)
admin.site.register(MenuItem)

admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
