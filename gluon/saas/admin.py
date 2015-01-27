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


class SubscriptionAdmin(admin.ModelAdmin):
    """Customize Status admin interface"""

    list_display = ("label", "category", "owner", "company_name", "referrer")

    list_filter = ("category", "referrer")


class ProfileInline(admin.StackedInline):
    model = Profile
    fk_name = "user"
    can_delete = False


class ProfileAdmin(UserAdmin):
    inlines = (ProfileInline, )


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Module)
admin.site.register(AccessAccount)
admin.site.register(AccessRole)
admin.site.register(Notification)
admin.site.register(View)
admin.site.register(MenuItem)

admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
