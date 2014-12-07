"""
Django settings for gluon project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from pathlib import Path
BASE_DIR = Path('.').resolve()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h-g0sh#owg%$2c*@%&6#kw3mc(2okzn+-r_o326py3st3mc6el'

ALLOWED_HOSTS = []

# Application definition

FRAMEWORK_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "bootstrap3",
    "chartit",
)

LOCAL_APPS = (
    "gluon",
    "base",
    "util",
    "saas",
    "legal",
)

INSTALLED_APPS = FRAMEWORK_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "gluon.middleware.GluonBaseMiddleware",
    "gluon.middleware.GluonSaasMiddleware",
)

ROOT_URLCONF = "gluon.urls"

WSGI_APPLICATION = "gluon.wsgi.application"

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_ROOT = str(BASE_DIR / "media")

MEDIA_URL = "/media/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = "/static/"

