from django.db.models import (
    Model,
    ForeignKey,
)

from base.fields import UserField

from base.mixins import BaseManager, BaseMixin

from .fields import InstanceField

from django.utils.translation import ugettext_lazy as _


class InstanceAssignedManager(BaseManager):
    """Model manager used by InstanceAssignedMixin models"""

    def from_instance(self, instance):
        queryset = super(InstanceAssignedManager, self).get_queryset()
        return queryset.filter(instance=instance)

    def active_from_instance(self, instance):
        queryset = super(InstanceAssignedManager, self).get_queryset()
        return queryset.active().from_instance(instance=instance)


class InstanceAssignedMixin(Model):
    """Must be inherited by models that are usable only by an instance users"""

    #
    # Define manager
    #

    objects = InstanceAssignedManager()

    #
    # Define relation to instance
    #

    # Field that keeps the user that created the instance
    # > required
    # > not editable
    # > automatically set
    instance = InstanceField(
        verbose_name=_("instance"),
        related_name="instance_%(app_label)s_%(class)s_set",
    )

    #
    # Overwrite some methods
    #

    def _name_unique_model_path(self):
        """The logical model path to get the current object in a unique way"""
        return self.instance, self

    class Meta:
        abstract = True


class UserAssignedManager(BaseManager):
    """Model manager used by InstanceAssignedMixin models"""

    def from_owner(self, owner):
        queryset = super(UserAssignedManager, self).get_queryset()
        return queryset.filter(owner=owner)

    def active_from_owner(self, owner):
        queryset = super(UserAssignedManager, self).get_queryset()
        return queryset.active().from_owner(owner=owner)


class UserAssignedMixin(Model):
    """Must be inherited by models that are usable only by an instance users"""

    #
    # Define manager
    #

    objects = UserAssignedManager()

    #
    # Define relation to instance
    #

    # Field that keeps the user that created the instance
    # > required
    # > not editable
    # > automatically set
    owner = UserField(
        verbose_name=_("owner"),
        related_name="owned_%(app_label)s_%(class)s_set",
        blank=False,
        editable=False
    )

    #
    # Overwrite some methods
    #

    def _name_unique_model_path(self):
        """The logical model path to get the current object in a unique way"""
        return self.owner, self

    class Meta:
        abstract = True
