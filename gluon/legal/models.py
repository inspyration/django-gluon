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
        max_length=255,
    )

    address2 = CharField(
        verbose_name=_("address 2"),
        max_length=255,
    )

    zip = CharField(
        verbose_name=_("zip"),
        max_length=16,
    )

    city = CharField(
        verbose_name=_("city"),
        max_length=255,
    )

    state = ForeignKey(
        verbose_name=_("state"),
        to=State,
    )

    country = ForeignKey(
        verbose_name=_("country"),
        to=Country,
    )

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = "addresses"


class Profile(InstanceAssignedMixin):
    """Profiles are common to both entities and persons"""

    addresses = ManyToManyField(
        verbose_name=_("addresses"),
        to=Address,
        blank=True,
        null=True,
    )

    website = CharField(
        verbose_name=_("website"),
        max_length=64,
    )

    phone = CharField(
        verbose_name=_("phone"),
        max_length=16,
    )

    fax = CharField(
        verbose_name=_("fax"),
        max_length=16,
    )

    locale = ForeignKey(
        verbose_name=_("locale"),
        to=Locale,
    )

    timezone = ForeignKey(
        verbose_name=_("timezone"),
        to=TimeZone,
    )

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")


class Entity(Profile):
    """Entities specific properties"""

    tin = CharField(
        verbose_name=_("tin"),
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
        max_length=64,
        upload_to="legal/entities/logos/%Y/%m/%d",
        height_field=logo_height,
        width_field=logo_width,
    )

    class Meta:
        verbose_name = _("entity")
        verbose_name_plural = "entities"


class Person(Profile):
    """Persons specific properties"""

    first_name = CharField(
        verbose_name=_("buyer"),
        max_length=127,
        blank=False,
    )

    last_name = CharField(
        verbose_name=_("buyer"),
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
        max_length=64,
        upload_to="legal/persons/avatars/%Y/%m/%d",
        height_field=avatar_height,
        width_field=avatar_width,
    )

    LABEL_FORMAT = "{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("persons")
