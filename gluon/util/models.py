from base.mixins import BaseMixin

from django.db.models import (
    Model,
    BooleanField,
    CharField,
    PositiveSmallIntegerField,
    ForeignKey,
)

from django.utils.translation import ugettext_lazy as _


class Status(Model):
    """Model handling all status"""

    # Field that indicate the model related to the status
    # > not required
    # > default True
    # > editable
    model = CharField(_("model"), max_length=16)

    # Field that indicate whether the instance can be used by other models
    # > not required
    # > default True
    # > editable
    active = BooleanField(
        verbose_name=_("active"),
        default=True,
        editable=True
    )

    # Field that indicate whether the state has been deleted
    # > not required
    # > default True
    # > editable
    deleted = BooleanField(
        verbose_name=_("active"),
        default=False,
        editable=True
    )

    # Field that indicate the name of the status
    # > not required
    # > default True
    # > editable
    name = CharField(_("status name"), max_length=16)

    # Field that indicate if the status is the default one
    # > required
    # > default False
    # > editable
    is_default = BooleanField(_("status name"), default=False)


class Country(BaseMixin):
    """Country"""

    alpha2 = CharField(
        verbose_name=_("alpha2"),
        max_length=2,
        unique=True,
    )

    alpha3 = CharField(
        verbose_name=_("alpha3"),
        max_length=3,
        unique=True,
        blank=False,
    )

    number = PositiveSmallIntegerField(
        verbose_name=_("number"),
        unique=True,
        blank=False,
    )

    name_fr = CharField(
        verbose_name=_("french name"),
        max_length=2,
        unique=True,
        blank=False,
    )

    name_en = CharField(
        verbose_name=_("english name"),
        max_length=3,
        unique=True,
        blank=False,
    )

    usage = CharField(
        verbose_name=_("usage name"),
        max_length=3,
        unique=True,
        blank=False,
    )

    class Meta:
        verbose_name_plural = "countries"


class State(BaseMixin):
    """State"""

    code = CharField(
        verbose_name=_("code"),
        max_length=2,
        unique=True,
        blank=False,
    )

    country = ForeignKey(
        verbose_name=_("country"),
        to=Country,
        blank=False,
    )

    def _name_unique_model_path(self):
        """The logical model path to get the current object in a unique way"""
        return self.country, self


class Locale(BaseMixin):
    """Locale"""


class TimeZone(BaseMixin):
    """TimeZone"""
