from datetime import datetime
from functools import partial
import string

from django.db.models import (
    Manager,
    QuerySet,
    Model,
    DateTimeField,
    BooleanField,
    CharField,
)

from .fields import UserField

from .data_handlers import get_data_handler

from django.utils.translation import ugettext_lazy as _
#from django.utils.timezone import now

LABEL_TO_NAME_TRANS_DOUBLE = (
    ("Æ", "AE"),
    ("Œ", "OE"),
    ("æ", "ae"),
    ("œ", "oe"),
)

LABEL_TO_NAME_TRANS_SIMPLE = str.maketrans(
    """ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØŠþÙÚÛÜÝŶŸàáâãäåçèéêëìíîïðñòóôõöøšÞùúûüýŷÿ\
"'()*+,./:;[]{}|\\ \t\n\r\x0b\x0c\x00""",
    """AAAAAACEEEEIIIIDNOOOOOOSBUUUUYYYaaaaaaceeeeiiiidnoooooosbuuuuyyy\
________________________""",
    """!#$%&<>=?@^`~"""
)


def label_to_name(label):
    for old, new in LABEL_TO_NAME_TRANS_DOUBLE:
        if old in label:
            label.replace(old, new)
    label = label.translate(LABEL_TO_NAME_TRANS_SIMPLE)
    return ''.join(filter(lambda c: c in string.printable, label))


BASE_MIXIN_BAD_QUERYSET =\
    "CustomisableMixin {0} Embedded QuerySet must inherit BaseQuerySet ({1})"

BASE_MIXIN_WITHOUT_QUERYSET =\
    "CustomisableMixin {0} must have an Embedded QuerySet"


class BaseQuerySet(QuerySet):
    """QuerySet used by BaseMixin models"""

    def alive(self):
        """Filter deleted objects"""
        return self.filter(deleted_on__isnull=True)

    def active(self):
        """Filter non active objects"""
        return self.filter(active=True)

    def auto_join(self):
        return self.select_related(*self.model.get_related_fields())


class BaseManager(Manager):
    """Model manager used by BaseMixin models"""

    def _get_queryset(self):
        if not hasattr(self.model, "QuerySet"):
            raise Exception(
                BASE_MIXIN_WITHOUT_QUERYSET.format(
                    str(self.model),
                )
            )
        queryset = self.model.QuerySet(self.model, using=self._db)
        if not isinstance(queryset, BaseQuerySet):
            raise Exception(
                BASE_MIXIN_BAD_QUERYSET.format(
                    str(self.model),
                    str(type.mro(self.model.QuerySet)),
                )
            )
        return queryset

    def get_queryset(self):
        return self._get_queryset().auto_join().alive()

    def active(self):
        """Get only active objects"""
        return self.get_queryset().active()

    def by_pk(self, pk):
        """Get an object by pk"""
        return self.get_queryset().get(pk=pk)

    def by_name(self, name):
        """Get an object by name"""
        return self.get_queryset().get(name=name)

    def by_label(self, label, **logical_path):
        """Get an object by label and elements from logical path"""
        logical_path["label"] = label
        return self.get_queryset().get(**logical_path)

    def _by_field(self, field_name, value):
        return self.get_queryset().get(
            **{field_name: value}
        )

    def __getattr__(self, item):
        if item[:3] == "by_":
            field_name = item[3:]
            if field_name in self.model.keys():
                return partial(self._by_field, field_name)
        return super(BaseManager, self).__getattr__(item)


class BaseMixin(Model):
    """Must be inherited by models that are only used by authenticated users"""

    #
    # Managers
    #

    # To get all objects, including those that are deleted
    all_objects = Manager()

    # To get only non deleted objects, whatever there are active or not
    objects = BaseManager()

    #
    # Embedded QuerySet
    #

    class QuerySet(BaseQuerySet):
        """Base QuerySet used by BaseMixin models that does not overwrite it"""

    #
    # Python utility methods
    #

    def __str__(self):
        """Default conversion to str: return label"""
        return self.label

    def __repr__(self):
        """default representation"""
        return "<{cls.__module__}.{cls.__name__} {self.name}>".format(
            self=self,
            cls=self.__class__,
        )

    #
    # Light tracking of activity
    #

    # Field that keeps the instance creation datetime
    # > required
    # > not editable
    # > automatically set
    created_on = DateTimeField(
        verbose_name=_("created on"),
        auto_now_add=True,
        blank=False,
        editable=False
    )

    # Field that keeps the instance last modification datetime
    # > required
    # > not editable
    # > automatically set
    last_modified_on = DateTimeField(
        verbose_name=_("last modified on"),
        auto_now=True,
        blank=False,
        editable=False
    )

    # Field that keeps the instance deletion datetime
    # When an object is deleted, it remains persistent but readonly.
    # > not required
    # > not editable
    # > automatically set
    deleted_on = DateTimeField(
        verbose_name=_("deleted on"),
        blank=True,
        null=True,
        editable=False
    )

    # Field that keeps the user that created the instance
    # > required
    # > not editable
    # > automatically set
    created_by = UserField(
        verbose_name=_("created by"),
        related_name="created_%(app_label)s_%(class)s_set",
        blank=False,
        editable=False
    )

    # Field that keeps the user that last modified the instance
    # > required
    # > not editable
    # > automatically set
    last_modified_by = UserField(
        verbose_name=_("last modified by"),
        related_name="last_modified_%(app_label)s_%(class)s_set",
        blank=False,
        editable=False
    )

    # Field that keeps the user that deleted the instance
    # > not required
    # > not editable
    # > automatically set
    deleted_by = UserField(
        verbose_name=_("deleted by"),
        related_name="deleted_%(app_label)s_%(class)s_set",
        null=True,
        editable=False
    )

    #
    # Manage active / non active instances
    #

    # Field that indicate whether the instance can be used by other models
    # > not required
    # > default True
    # > not editable
    # > automatically set
    active = BooleanField(
        verbose_name=_("active"),
        default=True,
        null=False,
        blank=False,
        editable=False
    )

    #
    # Naming instances (useful for managing relations in imports / exports)
    #

    # Label of the current object
    # > required
    # > editable
    # > must be filled out
    label = CharField(
        verbose_name=_("label"),
        max_length=32,
        blank=False,
        editable=True
    )

    # Name of the current object: must be unique (used as reference in imports)
    # > required
    # > not editable
    # > automatically set
    name = CharField(
        verbose_name=_("name"),
        max_length=255,
        unique=True,
        blank=False,
        editable=False
    )

    #
    # ForeignKeys to table that must be loaded (loading strategy)
    #

    @staticmethod
    def get_related_fields():
        return (
            "created_by",
            "last_modified_by",
        )

    #
    # Computation functions (concern: to be sure about the uniqueness of name)
    #

    def _name_unique_model_path(self):
        """The logical model path to get the current object in a unique way"""
        return self,

    def compute_name(self):
        """Rule to get name from label and foreign keys: name must be unique!"""
        return "__".join([label_to_name(x.label)
                          for x in self._name_unique_model_path()])

    #
    # Use the model as a mapping
    # > field names are the keys (for both class and instance)
    # > field values are the values (only for an instance)
    #

    @classmethod
    def keys(cls):
        """Allow model to be used as a mapping: return key generator"""
        for field_name in cls._meta.get_all_field_names():
            yield field_name

    def values(self):
        """Allow model to be used as a mapping: return value generator"""
        for field_name in self._meta.get_all_field_names():
            yield getattr(self, field_name)

    def items(self):
        """Allow model to be used as a mapping: return key, value generator"""
        for field_name in self._meta.get_all_field_names():
            yield field_name, getattr(self, field_name)

    @classmethod
    def concrete_keys(cls):
        """Allow model to be used as a mapping: return key generator"""
        for field, _ in cls._meta.get_concrete_fields_with_model():
            yield field.attname

    def concrete_values(self):
        """Allow model to be used as a mapping: return value generator"""
        for field, _ in self._meta.get_concrete_fields_with_model():
            yield getattr(self, field.attname)

    def concrete_items(self):
        """Allow model to be used as a mapping: return key, value generator"""
        for field, _ in self._meta.get_concrete_fields_with_model():
            yield field.attname, getattr(self, field.attname)

    #
    # Get some information about model fields
    #

    @classmethod
    def get_field(cls, field_name):
        return cls._meta.get_field(field_name)

    @classmethod
    def get_field_type(cls, field):
        if type(field) == str:
            field = cls.get_field(field)
        return type(field).__name__

    @classmethod
    def get_foreign_model(cls, field_name):
        field = cls.get_field(field_name)
        field_type = cls.get_field_type(field_name)
        if field_type not in ("ForeignKey", "ManyToManyField", "OneToOneField"):
            raise(Exception(
                "field name {0} is {1} (not a Relation)".format(
                    field_name, field_type)
            ))
        return field.rel.to, field_type

    #
    # Model methods
    #

    def save(self, *, compute=True):
        """Compute label then name before saving, no matter what"""

        if compute:
            if hasattr(self, "compute_label"):
                self.label = self.compute_label()
            elif hasattr(self, "LABEL_FORMAT"):
                self.label = self.LABEL_FORMAT.format(self=self)

            self.name = self.compute_name()

        return super(BaseMixin, self).save()

    def deactivate(self):
        """Deactivate current instance: not usable in other models anymore"""
        self.active = False
        self.save(compute=False)

    def activate(self):
        """Activate the object"""
        self.active = True
        self.save(compute=False)

    def delete(self, light=True):
        """Delete the object or set deleted_on and deleted_by"""
        if light:
            self.deleted_on = datetime.now()
#            assert self.deleted_by is not None
            self.save(compute=False)
        else:
            return super(BaseMixin, self).delete()

    #
    # Import / Export features
    #

    @staticmethod
    def extract_data_from_file(filename):
        data_handler = get_data_handler(filename)
        return data_handler.import_data(filename)

    @classmethod
    def import_data(cls, filename):
        import_field_names, data = cls.extract_data_from_file(filename)

        # check on field_names and build transformation lambda functions
        functions, foreign_objects, model_field_names = {}, {}, list(cls.keys())
        for import_field_name in import_field_names:
            # Is there a reference to a foreign key ?
            if "__" in import_field_name:
                field_name, foreign_field_name = import_field_name.split("__")
            else:
                field_name, foreign_field_name = import_field_name, None
            # Is the field in the model ?
            if field_name not in model_field_names:
                raise(Exception(
                    "field name {0} not is part of the model {1}".format(
                        field_name,
                        ".".join([cls.__module__, cls.__name__])
                    )
                ))
            if foreign_field_name is None:
                functions[import_field_name] = lambda k, v: v
            else:
                foreign_model, foreign_type = cls.get_foreign_model(field_name)
                if foreign_field_name not in foreign_model.keys():
                    raise(Exception(
                        "field name {0} not is part of the model {1}".format(
                            foreign_field_name,
                            ".".join([foreign_model.__module__,
                                      foreign_model.__name__])
                        )
                    ))
                foreign_objects[import_field_name] = {
                    getattr(o, foreign_field_name): o
                    for o in foreign_model.objects.active()
                }

                if foreign_type == "ForeignKey":
                    functions[import_field_name] =\
                        lambda k, v: foreign_objects[k][v]
                elif foreign_type == "ManyToManyField":
                    pass
                elif foreign_type == "OneToOneField":
                    functions[import_field_name] =\
                        lambda k, v: foreign_objects[k][v]
                else:
                    raise(Exception(
                        "field type {0} is not a relational field".format(
                            foreign_type)
                    ))

        # Create record
        for d in data:
            o = cls(**{k.split("__")[0]: functions[k](k, v)
                       for k, v in d.items() if k in functions})
            o.save()
            for field_name in foreign_objects:
                if field_name in functions:
                    continue  # Already done in object creation
                o_m2m = getattr(o, field_name.split("__")[0])
                o_m2m.add(*[foreign_objects[field_name][x]
                            for x in d[field_name].split(",")])

    @staticmethod
    def export_data_into_file(filename, data, headers):
        data_handler = get_data_handler(filename)
        return data_handler.export_data(filename, data, headers)

    @classmethod
    def export_data(cls, filename, model_field_names=None, only_active=False):
        if model_field_names is None:
            model_field_names = set(cls.concrete_keys())
        else:
            assert set(model_field_names).issubset(set(cls.concrete_keys()))
        # create build transformation lambda functions
        functions, fieldnames = {}, {}
        for field_name in model_field_names:
            field = cls.get_field(field_name)
            field_type = cls.get_field_type(field)
            if field_type in ("ForeignKey", "OneToOneField"):
                functions[field_name] = lambda k, v: getattr(v, k).name
                fieldnames[field_name] = "{0}__name".format(field_name)
            elif field_type == "ManyToManyField":
                functions[field_name] = lambda k, v:\
                    [o.name for o in getattr(v, k)]
                fieldnames[field_name] = "{0}__name".format(field_name)
            else:
                functions[field_name] = lambda k, v: getattr(v, k)
                fieldnames[field_name] = field_name

        # get objects to export
        objects = cls.objects
        if only_active:
            objects = objects.active()

        # Build data to export
        data = [{k: v(k, o) for k, v in functions.items()}
                for o in objects.all()]

        # Create the export file
        cls.export_data_into_file(filename, data, fieldnames)

    #
    # Meta class
    #

    class Meta:
        abstract = True