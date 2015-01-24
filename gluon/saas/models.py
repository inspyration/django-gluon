from django.conf import settings

from django.db.models import (
    BooleanField,
    CharField,
    DecimalField,
    ManyToManyField,
    OneToOneField,
    ForeignKey,
    TextField)

from base.mixins import BaseMixin

from util.models import Keyword, HttpResource, HttpResourcesConfig

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
    NaiveHierarchyMixin,
)

from django.utils.translation import ugettext_lazy as _


class Module(BaseMixin, StatusMixin):
    """Each module can be activated for each subscription"""

    application = BooleanField(
        verbose_name=_("Is this module a main application ?"),
        help_text=_("Is this module an application ?"),
        blank=False,
        null=False,
        default=True,
    )

    dependencies = ManyToManyField(
        verbose_name=_("Dependencies"),
        related_name="dependencies_rel_set",
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


########################
#                      #
#      SAAS Vital      #
#                      #
########################


class Subscription(BaseMixin, LocalisationMixin, SettingsMixin, WebMixin,
                   ContactDetailMixin, CorporateMixin, LogoMixin, StatusMixin):
    """An subscription is linked to a customer. It contains only his data"""

    # subscription status (opened or not)
    opened = BooleanField(
        verbose_name=_("opened"),
        help_text=_("Is the subscription is open ?"),
        blank=False,
        null=False,
        default=True,
    )

    # Person who create subscription on his behalf or on his company behalf
    owner = CharField(
        verbose_name=_("owner"),
        help_text=_("Owner"),
        max_length=127,
        blank=False,
    )

    modules = ManyToManyField(
        verbose_name=_("modules"),
        help_text=_("List of module installed on the subscription"),
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
        verbose_name = _("subscription")
        verbose_name_plural = _("subscriptions")


class AccessRole(BaseMixin):
    """A role, that comes with permissions through group management"""

    groups = ManyToManyField(
        verbose_name=_("groups"),
        help_text=_("List of groups used by the role"),
        to=getattr(settings, "AUTH_USER_GROUP", "auth.Group"),
        blank=False,
    )

    @staticmethod
    def get_related_fields():
        return BaseMixin.get_related_fields() + ("groups",)

    class Meta:
        verbose_name = _("access role")
        verbose_name_plural = _("access roles")


class AccessAccount(BaseMixin, StatusMixin):
    """An account is linked to some subscriptions and to one user"""

    user = ForeignKey(
        verbose_name=_("user"),
        help_text=_("user who owns this account"),
        to=getattr(settings, "AUTH_USER_MODEL", "auth.User"),
        related_name="saas_access_account_set",
        blank=False,
    )

    subscription = ForeignKey(
        verbose_name=_("subscription"),
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

    LABEL_FORMAT = "{self.user.label}@{self.subscription.label}:{self.role.label}"

    def _name_unique_model_path(self):
        """The logical model path to get the current object in a unique way"""
        return self.user, self.subscription, self.role

    @staticmethod
    def get_related_fields():
        return BaseMixin.get_related_fields() + ("user", "role", "role__groups")

    class Meta:
        verbose_name = _("access account")
        verbose_name_plural = _("access accounts")


########################
#                      #
#      SAAS Basis      #
#                      #
########################


class Notification(BaseMixin, StatusMixin):
    """A notification can be broadcast by any application"""

    message = TextField(
        verbose_name=_("message"),
        help_text=_("Message"),
        blank=False,
    )


class Profile(BaseMixin, AvatarMixin, SettingsMixin):

    user = OneToOneField(
        verbose_name=_("user"),
        help_text=_("User linked to this profile"),
        to=getattr(settings, "AUTH_USER_MODEL", "auth.User"),
        related_name="profile",
        blank=False,
    )

    notifications = ManyToManyField(
        verbose_name=_("notifications"),
        help_text=_("Notifications"),
        to=Notification,
        blank=True,
    )

#    default_subscription = #TODO

    LABEL_FORMAT = "{self.user.first_name} {self.user.last_name}"

    def compute_name(self):
        """Rule to get name from label and foreign keys: name must be unique!"""
        return "__".join([self.user.username, self.label])

    @staticmethod
    def get_related_fields():
        return BaseMixin.get_related_fields() + ("user",)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")


class View(BaseMixin):
    """SAAS View, used by SaasTemplateView"""

    module = ForeignKey(
        verbose_name=_("module"),
        help_text=_("Module of the view"),
        to=Module,
        related_name="view_set",
        blank=False,
    )

    page_title = CharField(
        verbose_name=_("page title"),
        help_text=_("Title of the page"),
        max_length=127,
        blank=False,
    )

    page_keywords = ManyToManyField(
        verbose_name=_("page keywords"),
        help_text=_("List of keywords used by the page"),
        to=Keyword,
        related_name="view_set",
        blank=True,
    )

    page_description = CharField(
        verbose_name=_("page description"),
        help_text=_("Description of the page (250 characters max, 200 ideally)"),
        max_length=250,
        blank=False,
    )

    resources_config = ForeignKey(
        verbose_name=_("HTTP resources configuration"),
        help_text=_("List of resources used by this view (CSS, JS, Meta, ...)"),
        to=HttpResourcesConfig,
        related_name="view_set",
        blank=True,
    )

    class Meta:
        verbose_name = _("view")
        verbose_name_plural = _("views")


class MenuItem(BaseMixin, NaiveHierarchyMixin):
    """Menu item"""

    path = CharField(
        verbose_name=_("path"),
        help_text=_("Menu item link"),
        max_length=127,
        blank=False,
    )

    icon = CharField(
        verbose_name=_("icon"),
        help_text=_("Icon (font-awesome)"),
        max_length=31,
        blank=False,
    )

    views = ManyToManyField(
        verbose_name=_("views"),
        help_text=_("Views related to this menu item"),
        to=View,
        related_name="menu_item_set",
        blank=True,
    )

    def view_names(self):
        # TODO: Optimization
        result = [v.label for v in self.views.all()]
        for child in self.get_children():
            result.extend(child.view_names())
        return result

    @classmethod
    def get_menu(cls, user):
        if user.is_superuser:
            return cls.get_roots()
        return cls.get_roots()  # TODO: Utiliser les bons modules

    @classmethod
    def get_default_menu(cls):
        return cls.get_roots()  # TODO: Utiliser les menus de SAAS Uniquement.
