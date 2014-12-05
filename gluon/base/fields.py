from django.db import models
from django.conf import settings

from .registration import FieldRegistry


class UserField(models.ForeignKey):
    """
    A field that keeps the user that change an instance of a model
    (Creation, modification, deletion)
    None will be the value for AnonymousUser.
    """

    def __init__(self, to=getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),
                 null=True, editable=False, **kwargs):
        super(UserField, self).__init__(to=to, null=null, editable=editable,
                                        **kwargs)

    def contribute_to_class(self, cls, name, virtual_only=False):
        super(UserField, self).contribute_to_class(cls, name, virtual_only)
        registry = FieldRegistry(self.__class__)
        registry.add_field(cls, self)
