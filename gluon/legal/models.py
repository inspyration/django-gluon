from django.db import models
from django.db.models import CharField, ForeignKey, ManyToManyField, \
    PositiveSmallIntegerField, ImageField

from saas.mixins import InstanceAssignedMixin

from util.models import Country, State, Locale, TimeZone

from django.utils.translation import ugettext_lazy as _


class Address(InstanceAssignedMixin):
    """Addresses properties"""

    address1 = CharField(
        verbose_name=_("address 1"),
        help_text=_("Address line 1"),
        max_length=255,
    )

    address2 = CharField(
        verbose_name=_("address 2"),
        help_text=_("Address line 2"),
        max_length=255,
    )

    zip = CharField(
        verbose_name=_("zip"),
        help_text=_("Address zip code"),
        max_length=16,
    )

    city = CharField(
        verbose_name=_("city"),
        help_text=_("Address city"),
        max_length=255,
    )

    state = ForeignKey(
        verbose_name=_("state"),
        help_text=_("Address state"),
        to=State,
    )

    country = ForeignKey(
        verbose_name=_("country"),
        help_text=_("Address country"),
        to=Country,
    )

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = "addresses"


class Profile(InstanceAssignedMixin):
    """Profiles are common to both entities and persons"""

    addresses = ManyToManyField(
        verbose_name=_("addresses"),
        help_text=_("Profile addresses"),
        to=Address,
        blank=True,
        null=True,
    )

    website = CharField(
        verbose_name=_("website"),
        help_text=_("Profile main website"),
        max_length=64,
    )

    phone = CharField(
        verbose_name=_("phone"),
        help_text=_("Profile phone"),
        max_length=16,
    )

    fax = CharField(
        verbose_name=_("fax"),
        help_text=_("Profile Fax"),
        max_length=16,
    )

    locale = ForeignKey(
        verbose_name=_("locale"),
        help_text=_("Profile Locale"),
        to=Locale,
    )

    timezone = ForeignKey(
        verbose_name=_("Profile timezone"),
        help_text=_("Timezone"),
        to=TimeZone,
    )

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")


class Entity(Profile):
    """Entities specific properties"""

    tin = CharField(
        verbose_name=_("tin"),
        help_text=_("Tax intra. number"),
        max_length=16,
    )

    logo_height = PositiveSmallIntegerField(
        verbose_name=_("logo height"),
    )

    logo_width = PositiveSmallIntegerField(
        verbose_name=_("logo width"),
    )

    logo = ImageField(
        verbose_name=_("logo"),
        help_text=_("Entity logo"),
        max_length=64,
        upload_to="media/legal/entities/logos/%Y/%m/%d",
        height_field=logo_height,
        width_field=logo_width,
    )

    class Meta:
        verbose_name = _("entity")
        verbose_name_plural = "entities"


class Person(Profile):
    """Persons specific properties"""

    first_name = CharField(
        verbose_name=_("first_name"),
        help_text=_("Person first name"),
        max_length=127,
        blank=False,
    )

    last_name = CharField(
        verbose_name=_("last name"),
        help_text=_("Person last name"),
        max_length=127,
        blank=False,
    )

    avatar_height = PositiveSmallIntegerField(
        verbose_name=_("avatar height"),
    )

    avatar_width = PositiveSmallIntegerField(
        verbose_name=_("avatar width"),
    )

    avatar = ImageField(
        verbose_name=_("avatar"),
        help_text=_("Avatar"),
        max_length=64,
        upload_to="media/legal/persons/avatars/%Y/%m/%d",
        height_field=avatar_height,
        width_field=avatar_width,
    )

    LABEL_FORMAT = "{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("persons")
