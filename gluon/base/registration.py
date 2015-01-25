from collections import defaultdict


class FieldRegistry(object):
    _registry = defaultdict(lambda: defaultdict(set))

    def __init__(self, field_cls):
        self._field_cls = field_cls

    def add_field(self, model, field):
        """Register a field for the model"""
        self._registry[self._field_cls][model].add(field)

    def get_fields(self, model):
        """Get the fields from a model"""
        return self._registry[self._field_cls][model]

    def __contains__(self, model):
        """Allow to use "in" keyword with FieldRegistry instances"""
        return model in self._registry[self._field_cls]