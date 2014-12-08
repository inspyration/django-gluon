from django.apps import AppConfig

from django.utils.translation import ugettext_lazy as _


class SaasConfig(AppConfig):
    name = "saas"
    verbose_name = _("Gluon - 02 - SAAS management")
