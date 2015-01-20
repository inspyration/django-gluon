from django.db import models
from django.db.models import ForeignKey, Q

from .models import Status


def get_default_status():
    result = Status.objects.filter(is_default=True).first()
    return result and result.id or None


class StatusField(ForeignKey):
    """
    A ForeignKey that point to status table
    """

    def __init__(self, to=None, *args, **kwargs):
        if to is None:
            to = Status
        super(StatusField, self).__init__(to, *args, **kwargs)

    def prepare_class(self, sender, **kwargs):
        if not sender._meta.abstract:

            model = ".".join([
                sender._meta.app_label,
                sender._meta.model_name,
            ])

            self.rel.limit_choices_to = {"model": model}

            if not self.has_default():
                self.default = get_default_status

    def contribute_to_class(self, cls, name):
        models.signals.class_prepared.connect(self.prepare_class, sender=cls)
        super(StatusField, self).contribute_to_class(cls, name)
