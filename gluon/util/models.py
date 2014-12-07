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
    model = CharField(
        verbose_name=_("model"),
        help_text=_("Model related to the status"),
        max_length=16,
    )

    # Field that indicate whether the instance can be used by other models
    # > not required
    # > default True
    # > editable
    active = BooleanField(
        verbose_name=_("active"),
        help_text=_("Is the status usable ?"),
        default=True,
        editable=True
    )

    # Field that indicate whether the state has been deleted
    # > not required
    # > default True
    # > editable
    deleted = BooleanField(
        verbose_name=_("deleted"),
        help_text=_("Is the status deleted"),
        default=False,
        editable=True
    )

    # Field that indicate the name of the status
    # > not required
    # > default True
    # > editable
    name = CharField(
        verbose_name=_("status name"),
        help_text=_("Name of the status"),
        max_length=16,
    )

    # Field that indicate if the status is the default one
    # > required
    # > default False
    # > editable
    is_default = BooleanField(
        verbose_name=_("status name"),
        help_text=_("Is the status is the default one for the model ?"),
        default=False,
    )

    class Meta:
        verbose_name = _("status")
        verbose_name_plural = _("statuses")


class Country(BaseMixin):
    """Country"""

    alpha2 = CharField(
        verbose_name=_("alpha2"),
        help_text=_("Two letters code"),
        max_length=2,
        unique=True,
    )

    alpha3 = CharField(
        verbose_name=_("alpha3"),
        help_text=_("Three letters code"),
        max_length=3,
        unique=True,
        blank=False,
    )

    number = PositiveSmallIntegerField(
        verbose_name=_("number"),
        help_text=_("Three digits number code"),
        unique=True,
        blank=False,
    )

    name_fr = CharField(
        verbose_name=_("french name"),
        help_text=_("French common name of the country"),
        max_length=2,
        unique=True,
        blank=False,
    )

    name_en = CharField(
        verbose_name=_("english name"),
        help_text=_("English common name of the country"),
        max_length=3,
        unique=True,
        blank=False,
    )

    usage = CharField(
        verbose_name=_("usage name"),
        help_text=_("Usage name (localised)"),
        max_length=3,
        unique=True,
        blank=False,
    )

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")


class State(BaseMixin):
    """State"""

    code = CharField(
        verbose_name=_("code"),
        help_text=_("Two letters code"),
        max_length=2,
        unique=True,
        blank=False,
    )

    country = ForeignKey(
        verbose_name=_("country"),
        help_text=_("Related country"),
        to=Country,
        blank=False,
    )

    def _name_unique_model_path(self):
        """The logical model path to get the current object in a unique way"""
        return self.country, self

    class Meta:
        verbose_name = _("state")
        verbose_name_plural = _("states")


class Locale(BaseMixin):
    """Locale:
    label contains language code such as fr-fr
    name contains locale name such as fr_FR"""

    def compute_name(self):
        language, country = self.label.split("-")
        return "_".join((language, country.upper()))

    class Meta:
        verbose_name = _("locale")
        verbose_name_plural = _("locales")


class TimeZone(BaseMixin):
    """TimeZone"""

    class Meta:
        verbose_name = _("timezone")
        verbose_name_plural = _("timezones")
