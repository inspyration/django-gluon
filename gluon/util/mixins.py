from django.db.models import (
    Manager,
    QuerySet,
    Model,
    DateTimeField,
    BooleanField,
    CharField,
    ForeignKey,
    PositiveSmallIntegerField,
    ImageField,
    Q,
)

from .fields import StatusField
from base.mixins import BaseManager, BaseMixin, BaseQuerySet

from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from util.models import State, Country, Locale, TimeZone


class StatusMixin(Model):
    """Must be inherited by models using a workflow based on status"""

    status = StatusField(
        verbose_name=_("status"),
        related_name="status_%(app_label)s_%(class)s_set",
        unique=False,
        blank=False,
        null=False,
    )

    class Meta:
        abstract = True


class TimeFramedQuerySet(BaseQuerySet):
    """QuerySet used by BaseMixin models"""

    def in_effect(self):
        current_date = now()
        return self.filter(
            Q(start__lte=current_date) & (
                Q(end__gte=current_date) | Q(end__isnull=True)
            )
        )

    def in_effect_at(self, date):
        return self.filter(
            Q(start__lte=date) & (
                Q(end__gte=date) | Q(end__isnull=True)
            )
        )


class TimeFramedManager(BaseManager):

    def get_queryset(self):
        return self._get_queryset().auto_join().alive()

    def in_effect(self):
        """Get only active objects"""
        return self.get_queryset().in_effect()

    def in_effect_at(self, date):
        """Get only active objects"""
        return self.get_queryset().in_effect_at(date)


class TimeFramedMixin(BaseMixin):
    """Must be inherited by models that are valid only in a period of time"""

    #
    # Embedded QuerySet
    #

    class QuerySet(TimeFramedQuerySet):
        """Base QuerySet used by BaseMixin models that does not overwrite it"""

    # same default filters as BaseManager, with some other filters added
    objects = TimeFramedManager()

    #
    # Define valid period
    #

    start = DateTimeField(
        verbose_name=_("start on"),
        auto_now_add=True,
        blank=False,
        editable=False,
    )

    end = DateTimeField(
        verbose_name=_("end on"),
        null=True,
        blank=True,
        editable=False,
    )

    class Meta:
        abstract = True


class NaiveHierarchyManager(BaseManager):
    def get_roots(self):
        return self.get_query_set().filter(parent__isnull=True)


class NaiveHierarchyMixin(BaseMixin):

    parent = ForeignKey(
        verbose_name=_("parent"),
        related_name="directory_set",
        help_text=_("Parent directory"),
        to="self",
        null=True,
        blank=True,
    )

    tree = NaiveHierarchyManager()

    def get_children(self):
        return type(self).objects.filter(parent=self)

    def get_descendants(self):
        result = set(self.get_children())
        for node in list(result):
            result.update(node.get_descendants())
        return result

    def _name_unique_model_path(self):
        """The logical model path to get the current object in a unique way"""
        if not self.parent:
            return self,
        else:
            return self.parent._name_unique_model_path() + (self,)

    class Meta:
        abstract = True


class LocalisationMixin(Model):

    address1 = CharField(
        verbose_name=_("address 1"),
        help_text=_("first line of the address"),
        max_length=255,
        null=False,
        blank=False,
    )

    address2 = CharField(
        verbose_name=_("address 2"),
        help_text=_("second line of the address"),
        max_length=255,
        null=True,
        blank=True,
    )

    zip = CharField(
        verbose_name=_("zip"),
        help_text=_("Zip code"),
        max_length=16,
        null=False,
        blank=False,
    )

    city = CharField(
        verbose_name=_("city"),
        help_text=_("City"),
        max_length=255,
        null=False,
        blank=False,
    )

    state = ForeignKey(
        verbose_name=_("state"),
        related_name="%(app_label)s_%(class)s_set",
        help_text=_("State"),
        to=State,
        null=True,
        blank=True,
    )

    country = ForeignKey(
        verbose_name=_("country"),
        related_name="%(app_label)s_%(class)s_set",
        help_text=_("Country"),
        to=Country,
        null=False,
        blank=False,
    )

    class Meta:
        abstract = True


class SettingsMixin(Model):

    locale = ForeignKey(
        verbose_name=_("locale"),
        related_name="%(app_label)s_%(class)s_set",
        help_text=_("Locale"),
        to=Locale,
        null=False,
        blank=False,
    )

    timezone = ForeignKey(
        verbose_name=_("timezone"),
        related_name="%(app_label)s_%(class)s_set",
        help_text=_("Timezone"),
        to=TimeZone,
        null=False,
        blank=False,
    )

    class Meta:
        abstract = True


class WebMixin(Model):

    website = CharField(
        verbose_name=_("website"),
        help_text=_("Website URI"),
        max_length=64,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class ContactDetailMixin(Model):

    phone = CharField(
        verbose_name=_("phone"),
        help_text=_("Phone number"),
        max_length=16,
        null=False,
        blank=False,
    )

    fax = CharField(
        verbose_name=_("fax"),
        help_text=_("Fax number"),
        max_length=16,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class CorporateMixin(Model):

    tin = CharField(
        verbose_name=_("tin"),
        help_text=_("Tax intra. number"),
        max_length=16,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class LogoMixin(Model):

    logo_height = PositiveSmallIntegerField(
        verbose_name=_("logo height"),
        null=False,
        blank=True,
    )

    logo_width = PositiveSmallIntegerField(
        verbose_name=_("logo width"),
        null=False,
        blank=True,
    )

    logo = ImageField(
        verbose_name=_("logo"),
        help_text=_("Logo of the instance owner"),
        max_length=64,
        upload_to="media/%(app_label)s/%(class)s/logos/%Y/%m/%d",
        height_field=logo_height,
        width_field=logo_width,
        null=True,
        blank=True,
    )

    #
    # Meta class
    #

    class Meta:
        abstract = True


class AvatarMixin(Model):

    avatar_height = PositiveSmallIntegerField(
        verbose_name=_("avatar height"),
        null=False,
        blank=True,
    )

    avatar_width = PositiveSmallIntegerField(
        verbose_name=_("avatar width"),
        null=False,
        blank=True,
    )

    avatar = ImageField(
        verbose_name=_("avatar"),
        help_text=_("Avatar"),
        max_length=64,
        upload_to="media/%(app_label)s/%(class)s/avatars/%Y/%m/%d",
        height_field=avatar_height,
        width_field=avatar_width,
        null=True,
        blank=True,
    )

    #
    # Meta class
    #

    class Meta:
        abstract = True


class PersonalInformationMixin(Model):

    first_name = CharField(
        verbose_name=_("first_name"),
        help_text=_("Person first name"),
        max_length=127,
        blank=False,
        null=False,
    )

    last_name = CharField(
        verbose_name=_("last name"),
        help_text=_("Person last name"),
        max_length=127,
        blank=False,
        null=False,
    )

    #
    # Meta class
    #

    class Meta:
        abstract = True