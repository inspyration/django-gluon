from base.mixins import BaseManager, BaseMixin
from util.mixins import TimeFramedManager, NaiveHierarchyManager, \
    NaiveHierarchyMixin, TimeFramedMixin

from base.fields import UserField
from .fields import SubscriptionField

from django.utils.translation import ugettext_lazy as _


########################
#                      #
#      SAAS Mixin      #
#                      #
########################


#
# Base SAAS Mixin
#


class SaasManager(BaseManager):
    """Model manager used by SaasMixin models"""

    def get_queryset(self, subscription):
        queryset = super(SaasManager, self).get_queryset()
        return queryset.filter(subscription=subscription)


class SaasMixin(BaseMixin):
    """Must be inherited by models that are usable only at subscription level"""

    #
    # Define manager
    #

    objects = SaasManager()

    #
    # Define relation to subscription
    #

    # Field that keeps the user that created the subscription
    # > required
    # > not editable
    # > automatically set
    subscription = SubscriptionField(
        verbose_name=_("subscription"),
        related_name="subscription_%(app_label)s_%(class)s_set",
    )

    #
    # Overwrite some methods
    #

    def _name_unique_model_path(self):
        """The logical model path to get the current object in a unique way"""
        return self.subscription, self

    class Meta:
        abstract = True


#
# Time framed SAAS Mixin
#

class SaasTimeFramedManager(TimeFramedManager):
    """Model manager used by SAASTimeFramedMixin models"""

    def get_queryset(self, subscription):
        queryset = super(SaasTimeFramedManager, self).get_queryset()
        return queryset.filter(subscription=subscription)


class SaasTimeFramedMixin(SaasMixin, TimeFramedMixin):
    """Must be inherited by models that are usable only at subscription level"""

    objects = SaasTimeFramedManager()

    class Meta:
        abstract = True


#
# Naive hierarchy SAAS Mixin
#
class SaasHierarchyManager(NaiveHierarchyManager):
    """Model manager used by SaasHierarchyMixin models"""

    def get_queryset(self, subscription):
        queryset = super(SaasHierarchyManager, self).get_queryset()
        return queryset.filter(subscription=subscription)


class SaasHierarchyMixin(SaasMixin, NaiveHierarchyMixin):
    """Must be inherited by models that are usable only at subscription level"""

    objects = SaasHierarchyManager()

    class Meta:
        abstract = True


########################
#                      #
#     Private Mixin    #
#                      #
########################


#
# Base private mixin
#


class PrivateManager(BaseManager):
    """Model manager used byPrivateMixin models"""

    def get_queryset(self, owner):
        queryset = super(SaasManager, self).get_queryset()
        return queryset.filter(owner=owner)


class PrivateMixin(BaseMixin):
    """Must be inherited by models that are usable only at subscription level"""

    #
    # Define manager
    #

    objects = PrivateManager()

    #
    # Define relation to subscription
    #

    # Field that keeps the user that created the subscription
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


#
# Time framed private Mixin
#

class PrivateTimeFramedManager(TimeFramedManager):
    """Model manager used by PrivateTimeFramedMixin models"""

    def get_queryset(self, subscription):
        queryset = super(PrivateTimeFramedManager, self).get_queryset()
        return queryset.filter(subscription=subscription)


class PrivateTimeFramedMixin(PrivateMixin, TimeFramedMixin):
    """Must be inherited by models that are usable only at user level"""

    objects = PrivateTimeFramedManager()

    class Meta:
        abstract = True


#
# Naive hierarchy private Mixin
#
class PrivateHierarchyManager(NaiveHierarchyManager):
    """Model manager used by PrivateHierarchyMixin models"""

    def get_queryset(self, subscription):
        queryset = super(PrivateHierarchyManager, self).get_queryset()
        return queryset.filter(subscription=subscription)


class PrivateHierarchyMixin(PrivateMixin, NaiveHierarchyMixin):
    """Must be inherited by models that are usable only at user level"""

    objects = PrivateHierarchyManager()

    class Meta:
        abstract = True
