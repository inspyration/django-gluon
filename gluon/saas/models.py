from django.conf import settings

from base.mixins import BaseMixin

from util.mixins import (
    StatusMixin,
    LocalisationMixin,
    SettingsMixin,
    WebMixin,
    ContactDetailMixin,
    CorporateMixin,
    LogoMixin,
    PersonalInformationMixin,
    AvatarMixin,
)

from django.db.models import (
    BooleanField,
    CharField,
    DecimalField,
    ManyToManyField,
    OneToOneField,
    ForeignKey,
)

from django.utils.translation import ugettext_lazy as _


class Module(BaseMixin, StatusMixin):
    """Each module can be activated for each instance"""

    application = BooleanField(
        verbose_name=_("Is this module a main application ?"),
        help_text=_("Is this module an application ?"),
        blank=False,
        null=False,
        default=True,
    )

    dependencies = ManyToManyField(
        verbose_name=_("Dependencies"),
        related_name='dependencies_rel_set',
        help_text=_("List of modules required to make this one work"),
        to="self",
        symmetrical=False,
        blank=False,
    )

    price = DecimalField(
        verbose_name=_("price"),
        help_text=_("Module price"),
        max_digits=5,
        decimal_places=2,
    )

    _auto_compute_name = False

    class Meta:
        verbose_name = _("module")
        verbose_name_plural = _("modules")


class Subscription(BaseMixin, LocalisationMixin, SettingsMixin, WebMixin,
                   ContactDetailMixin, CorporateMixin, LogoMixin, StatusMixin):
    """An instance is linked to a customer. It contains only his data"""

    # Instance status (opened or not)
    opened = BooleanField(
        verbose_name=_("opened"),
        help_text=_("Is the instance is open ?"),
        blank=False,
        null=False,
        default=True,
    )

    # Person who create instance on his behalf or on his company behalf
    owner = CharField(
        verbose_name=_("owner"),
        help_text=_("Owner"),
        max_length=127,
        blank=False,
    )

    modules = ManyToManyField(
        verbose_name=_("modules"),
        help_text=_("List of module installed on the instance"),
        to=Module,
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
        help_text=_("List of groups used by the role"),
        to=getattr(settings, 'AUTH_USER_GROUP', 'auth.Group'),
        blank=False,
    )

    @staticmethod
    def get_related_fields():
        return BaseMixin.get_related_fields() + ("groups",)

    class Meta:
        verbose_name = _("access role")
        verbose_name_plural = _("access roles")


class AccessAccount(BaseMixin, StatusMixin):
    """An account is linked to some instances and to one user"""

    user = ForeignKey(
        verbose_name=_("user"),
        help_text=_("user who owns this account"),
        to=getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),
        related_name="saas_access_account_set",
        blank=False,
    )

    instance = ForeignKey(
        verbose_name=_("instance"),
        help_text=_("Role linked to this account"),
        to=Subscription,
        blank=False,
    )

    role = ForeignKey(
        verbose_name=_("role"),
        help_text=_("Role linked to this account"),
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


class Profile(BaseMixin, PersonalInformationMixin, AvatarMixin, SettingsMixin):

    user = OneToOneField(
        verbose_name=_("user"),
        help_text=_("User linked to this profile"),
        to=getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),
        related_name="profile",
        blank=False,
    )

#    default_subscription = #TODO

    @staticmethod
    def get_related_fields():
        return BaseMixin.get_related_fields() + ("user",)

    def compute_label(self):
        return " ".join((self.first_name, self.last_name))

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
