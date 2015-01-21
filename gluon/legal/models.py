from django.db.models import ForeignKey, ManyToManyField

from base.mixins import BaseMixin

from saas.mixins import SaasMixin
from util.mixins import (
    LocalisationMixin,
    SettingsMixin,
    WebMixin,
    ContactDetailMixin,
    CorporateMixin,
    LogoMixin,
    PersonalInformationMixin,
    AvatarMixin,
)

from django.utils.translation import ugettext_lazy as _


class Address(SaasMixin, LocalisationMixin):
    """Addresses properties"""

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = "addresses"


class Profile(SaasMixin, SettingsMixin, WebMixin, ContactDetailMixin):
    """Profiles are common to both entities and persons"""

    addresses = ManyToManyField(
        verbose_name=_("addresses"),
        help_text=_("Profile addresses"),
        to=Address,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")


class Entity(Profile, CorporateMixin, LogoMixin):
    """Entities specific properties"""

    class Meta:
        verbose_name = _("entity")
        verbose_name_plural = "entities"


class Person(Profile, AvatarMixin, PersonalInformationMixin):
    """Persons specific properties"""

    LABEL_FORMAT = "{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("persons")
