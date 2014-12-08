from django.apps import AppConfig

from django.utils.translation import ugettext_lazy as _


class BaseConfig(AppConfig):
    name = "base"
    verbose_name = _("Gluon - 00 - Gluon Base module")
