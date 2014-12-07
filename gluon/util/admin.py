from django.contrib import admin

from .models import (
    Status,
    Country,
    State,
    Locale,
    TimeZone,
)

admin.site.register(Status)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Locale)
admin.site.register(TimeZone)
