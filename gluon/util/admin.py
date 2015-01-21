from django.contrib import admin

from .models import (
    Status,
    Country,
    State,
    Locale,
    TimeZone,
)


class StatusAdmin(admin.ModelAdmin):
    """Customize Status admin interface"""

    list_display = ("label", "model")


class StateAdmin(admin.ModelAdmin):
    """Customize Country admin interface"""

    list_display = ("label", "country")


admin.site.register(Status, StatusAdmin )
admin.site.register(Country)
admin.site.register(State, StateAdmin)
admin.site.register(Locale)
admin.site.register(TimeZone)
