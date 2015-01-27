from django.db import models
from django.db.models import ForeignKey, Q

from .models import Status


class StatusField(ForeignKey):
    """
    A ForeignKey that point to status table
    """

    def __init__(self, to=None, *args, **kwargs):
        if to is None:
            to = Status
        super(StatusField, self).__init__(to, *args, **kwargs)

    def get_default(self):
        result = Status.objects.filter(model=self.status_related_model,
                                       is_default=True).first()
        return result and result.id or None

    def prepare_class(self, sender, **kwargs):
        if not sender._meta.abstract:

            model = ".".join([
                sender._meta.app_label,
                sender._meta.model_name,
            ])
            self.status_related_model = model
            self.rel.limit_choices_to = {"model": model}

    def contribute_to_class(self, cls, name):
        models.signals.class_prepared.connect(self.prepare_class, sender=cls)
        super(StatusField, self).contribute_to_class(cls, name)
