from django.db.models import (
    Manager,
    QuerySet,
    Model,
    DateTimeField,
    BooleanField,
    CharField,
    ForeignKey,
    Q,
)

from model_utils.managers import QueryManager

from .fields import StatusField
from base.fields import UserField
from base.mixins import BaseManager, BaseMixin, BaseQuerySet

from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


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
        editable=False
    )

    end = DateTimeField(
        verbose_name=_("end on"),
        null=True,
        blank=True,
        editable=False
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
