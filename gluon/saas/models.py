from django.conf import settings

from base.mixins import BaseMixin

from util.models import Country, State, Locale, TimeZone

from django.contrib.auth.models import User

from django.db.models import (
    BooleanField,
    CharField,
    DecimalField,
    ManyToManyField,
    OneToOneField,
    ForeignKey,
    ImageField,
    PositiveSmallIntegerField,
)

from django.utils.translation import ugettext_lazy as _


class Module(BaseMixin):
    """Each module can be activated for each instance"""

    application = BooleanField(
        verbose_name=_("Is this module a main application ?"),
        blank=False,
        null=False,
        default=True,
    )

    price = DecimalField(
        verbose_name=_("price"),
        max_digits=5,
        decimal_places=2,
    )

    class Meta:
        verbose_name = _("module")
        verbose_name_plural = _("modules")


class Instance(BaseMixin):
    """An instance is linked to a customer. It contains only his data"""

    # Instance status (opened or not)
    opened = BooleanField(
        verbose_name=_("opened"),
        blank=False,
        null=False,
        default=True,
    )

    # Person who create instance on his behalf or on his company behalf
    buyer = CharField(
        verbose_name=_("buyer"),
        max_length=127,
        blank=False,
    )

    address1 = CharField(
        verbose_name=_("address 1"),
        max_length=255,
        blank=False,
    )

    address2 = CharField(
        verbose_name=_("address 2"),
        max_length=255,
        blank=False,
    )

    zip = CharField(
        verbose_name=_("zip"),
        max_length=16,
        blank=False,
    )

    city = CharField(
        verbose_name=_("city"),
        max_length=255,
        blank=False,
    )

    state = ForeignKey(
        verbose_name=_("state"),
        related_name="saas_instance_set",
        to=State,
    )

    country = ForeignKey(
        verbose_name=_("country"),
        related_name="saas_instance_set",
        to=Country,
        blank=False,
    )

    website = CharField(
        verbose_name=_("website"),
        max_length=64,
    )

    phone = CharField(
        verbose_name=_("phone"),
        max_length=16,
        blank=False,
    )

    fax = CharField(
        verbose_name=_("fax"),
        max_length=16,
    )

    tin = CharField(
        verbose_name=_("tin"),
        max_length=16,
    )

    modules = ManyToManyField(
        verbose_name=_("modules"),
        to=Module,
    )

    logo_height = PositiveSmallIntegerField(
        verbose_name=_("logo height"),
    )

    logo_width = PositiveSmallIntegerField(
        verbose_name=_("logo width"),
    )

    logo = ImageField(
        verbose_name=_("logo"),
        max_length=64,
        upload_to="saas/logos/%Y/%m/%d",
        height_field=logo_height,
        width_field=logo_width,
    )

    locale = ForeignKey(
        verbose_name=_("locale"),
        related_name="saas_instance_set",
        to=Locale,
    )

    timezone = ForeignKey(
        verbose_name=_("timezone"),
        related_name="saas_instance_set",
        to=TimeZone,
    )

    @staticmethod
    def get_related_fields():
        return BaseMixin.get_related_fields() + ("modules",)

    def price(self):
        return sum(m.price for m in self.modules)

    def open(self):
        self.open = True
        self.save(compute=False)

    def close(self):
        self.open = False
        self.save(compute=False)

    class Meta:
        verbose_name = _("instance")
        verbose_name_plural = _("instances")


class AccessRole(BaseMixin):
    """A role, that comes with permissions through group management"""

    groups = ManyToManyField(
        verbose_name=_("groups"),
        to=getattr(settings, 'AUTH_USER_GROUP', 'auth.Group'),
        blank=False,
    )

    @staticmethod
    def get_related_fields():
        return BaseMixin.get_related_fields() + ("groups",)

    class Meta:
        verbose_name = _("access role")
        verbose_name_plural = _("access roles")


class AccessAccount(BaseMixin):
    """An account is linked to some instances and to one user"""

    user = ForeignKey(
        verbose_name=_("user"),
        to=getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),
        related_name="saas_access_account_set",
        blank=False,
    )

    instance = ForeignKey(
        verbose_name=_("instances"),
        to=Instance,
        blank=False,
    )

    role = ForeignKey(
        verbose_name=_("role"),
        to=AccessRole,
        related_name="saas_access_account_set",
        blank=False,
    )

    LABEL_FORMAT = "{self.user.label}@{self.instance.label}:{self.role.label}"

    def _name_unique_model_path(self):
        """The logical model path to get the current object in a unique way"""
        return self.user, self.instance, self.role

    @staticmethod
    def get_related_fields():
        return BaseMixin.get_related_fields() + ("user", "role", "role__groups")

    class Meta:
        verbose_name = _("access account")
        verbose_name_plural = _("access accounts")


class Profile(BaseMixin):

    user = OneToOneField(
        verbose_name=_("user"),
        to=getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),
        related_name="profile",
        blank=False,
    )

    first_name = CharField(
        verbose_name=_("first name"),
        max_length=32,
        blank=False,
    )

    last_name = CharField(
        verbose_name=_("last name"),
        max_length=32,
        blank=False,
    )

    avatar_height = PositiveSmallIntegerField(
        verbose_name=_("avatar height"),
    )

    avatar_width = PositiveSmallIntegerField(
        verbose_name=_("avatar width"),
    )

    avatar = ImageField(
        verbose_name=_("avatar"),
        max_length=64,
        upload_to="saas/avatars/%Y/%m/%d",
        height_field=avatar_height,
        width_field=avatar_width,
    )

    locale = ForeignKey(
        verbose_name=_("locale"),
        related_name="user_set",
        to=Locale,
    )

    timezone = ForeignKey(
        verbose_name=_("timezone"),
        related_name="user_set",
        to=TimeZone,
    )

    @staticmethod
    def get_related_fields():
        return BaseMixin.get_related_fields() + ("user",)

    def compute_label(self):
        return " ".join((self.first_name, self.last_name))

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
