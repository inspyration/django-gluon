from django.contrib import admin

from .models import (
    Status,
    Country,
    State,
    Locale,
    TimeZone,
)

admin.register(
    Status,
    Country,
    State,
    Locale,
    TimeZone
)
