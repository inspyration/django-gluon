from base.mixins import BaseMixin

from django.db.models import (
    Model,
    BooleanField,
    CharField,
    PositiveSmallIntegerField,
    ForeignKey,
    ManyToManyField,
)

from django.utils.translation import ugettext_lazy as _


#
# Status
#


class Status(BaseMixin):
    """Model handling all status"""

    # Field that indicate the model related to the status
    # > not required
    # > default True
    # > editable
    model = CharField(
        verbose_name=_("model"),
        help_text=_("Model related to the status"),
        max_length=32,
    )

    is_default = BooleanField(
        verbose_name=_("status name"),
        help_text=_("Is the status is the default one for the model ?"),
        default=False,
    )

    def _name_unique_model_path(self):
        """The logical model path to get the current object in a unique way"""
        return self.model, self

    class Meta:
        verbose_name = _("status")
        verbose_name_plural = _("statuses")


#
# Localization
#


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


#
# Settings
#


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


#
# File management
#


class MimeRegistry(BaseMixin):
    """Media Type Registry"""

    class Meta:
        verbose_name = _("MIME registry")
        verbose_name_plural = _("MIME registries")


class Mime(BaseMixin):
    """Type Mime"""

    registry = ForeignKey(
        verbose_name=_("registry"),
        related_name="registry_%(class)s_set",
        help_text=_("Mime type registry"),
        to=MimeRegistry,
    )

    reference =  CharField(
        verbose_name=_("reference"),
        help_text=_("Mime type reference"),
        max_length=127,
        blank=True,
    )

    def _name_unique_model_path(self):
        """The logical model path to get the current object in a unique way"""
        return self.registry, self

    class Meta:
        verbose_name = _("MIME type")
        verbose_name_plural = _("MIME types")


#
# HTTP Resources management
#


class HtmlTag(BaseMixin):
    """HTML Tag"""

    class Meta:
        verbose_name = _("Html tag")
        verbose_name_plural = _("Html tags")


class Browser(BaseMixin):
    """Web Browser"""

    class Meta:
        verbose_name = _("Browser")
        verbose_name_plural = _("Browsers")


class HttpResource(BaseMixin):
    """HTTP Resource"""

    tag = ForeignKey(
        verbose_name=_("tag"),
        related_name="tag_%(class)s_set",
        help_text=_("HTML Tag used to call this resource"),
        to=HtmlTag,
        blank=False,
    )

    browser = ForeignKey(
        verbose_name=_("browser"),
        related_name="browser_%(class)s_set",
        help_text=_("Specific Browser (potentially with version number)"),
        to=Browser,
        blank=False,
    )

    path = CharField(
        verbose_name=_("path"),
        help_text=_("Path to the (hosted) resource"),
        max_length=127,
        blank=True,
    )

    def _name_unique_model_path(self):
        """The logical model path to get the current object in a unique way"""
        return self.tag, self.browser, self

    class Meta:
        verbose_name = _("Http resource")
        verbose_name_plural = _("Http resources")


class HttpResourcesConfig(BaseMixin):
    """HTTP Resource"""

    resources = ManyToManyField(
        verbose_name=_("HTTP resources"),
        help_text=_("List of resources used by this view (CSS, JS, Meta, ...)"),
        to=HttpResource,
        related_name="view_set",
        blank=True,
    )

    class Meta:
        verbose_name = _("Http resources configuration")
        verbose_name_plural = _("Http resources configurations")


class Keyword(BaseMixin):
    """Keyword of a page (html>head>meta[keyword])"""

    class Meta:
        verbose_name = _("keyword")
        verbose_name_plural = _("keywords")
