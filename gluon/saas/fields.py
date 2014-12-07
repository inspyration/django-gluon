from django.db import models
from django.conf import settings

from base.registration import FieldRegistry

from .models import Instance


class InstanceField(models.ForeignKey):
    """
    A field that keeps the SASS instance that own the model instance
    """

    def __init__(self, to=Instance, null=False, editable=False, **kwargs):
        super(InstanceField, self).__init__(to=to, null=null, editable=editable,
                                            **kwargs)

    def contribute_to_class(self, cls, name, virtual_only=False):
        super(InstanceField, self).contribute_to_class(cls, name, virtual_only)
        registry = FieldRegistry(self.__class__)
        registry.add_field(cls, self)
