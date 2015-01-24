from django.db import models
from django.conf import settings

from base.registration import FieldRegistry

from .models import Subscription


class SubscriptionField(models.ForeignKey):
    """
    A field that keeps the SASS subscription that own the model instance
    """

    def __init__(self, to=Subscription, null=False, editable=False, **kwargs):
        super(SubscriptionField, self).__init__(
            to=to, null=null, editable=editable, **kwargs)

    def contribute_to_class(self, cls, name, virtual_only=False):
        super(SubscriptionField, self).contribute_to_class(
            cls, name, virtual_only)
        registry = FieldRegistry(self.__class__)
        registry.add_field(cls, self)
