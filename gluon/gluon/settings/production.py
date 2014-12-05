from .base import *

SECRET_KEY = "f+$*c=_-c^(62sdd+c-d97+_&xmp2dwx)b5d%zs9%ivn8mu&!9"

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(BASE_DIR / "data" / "db.sqlite3"),
    }
}

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Europe/Paris"
