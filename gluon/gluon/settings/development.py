from .base import *

SECRET_KEY = "f+$*c=_-c^(62sdd+c-d97+_&xmp2dwx)b5d%zs9%ivn8mu&!9"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
    "debug_toolbar",
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(BASE_PATH / "data" / "db.sqlite3"),
        "ATOMIC_REQUESTS": True,
    }
}

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Europe/Paris"

