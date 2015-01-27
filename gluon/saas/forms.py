from django.contrib.auth import get_user_model

from django.forms import (
    ModelForm,
    TextInput,
    PasswordInput,
    Select,
    RadioSelect,
    ModelChoiceField,
    ModelMultipleChoiceField,
    CheckboxSelectMultiple,
)

from util.models import Locale, TimeZone
from .models import Subscription, Profile, SubscriptionCategory, Module

from django.utils.translation import ugettext_lazy as _


class SubscriptionForm(ModelForm):

    category = ModelChoiceField(
        queryset=SubscriptionCategory.objects.filter(
            status__name="saas_subscriptioncategory__front-office"),
        empty_label=None,
        widget=RadioSelect(),
        label=_("Subscription category"),
        initial=1,
    )

    modules = ModelMultipleChoiceField(
        queryset=Module.objects.filter(monthly_price__gt=0),
        widget=CheckboxSelectMultiple(),
        label=_("Select modules"),
    )

    class Meta:
        model = Subscription

        fields = (
            "category",
            "referrer",
            "company_name",
            "modules",
        )

        labels = {
            "referrer": _("Referrer"),
            "company_name": _("Company name"),
            "modules": _("Modules"),
        }

        widgets = {
            "referrer": TextInput(attrs={"class": "form-control"}),
            "company_name": TextInput(attrs={"class": "form-control"}),
            "modules": TextInput(attrs={"class": "form-control"}),
        }

        help_texts = {
        }

        error_messages = {
        }


class SubscriptionUserForm(ModelForm):

    class Meta:
        model = get_user_model()

        # fields = ("username", "first_name", "last_name", "email", "password")
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
        )

        labels = {
            # "username": _("Username"),
            "first_name": _("First name"),
            "last_name": _("Last name"),
            "email": _("Email"),
            "password": _("Password"),
        }

        widgets = {
            # "username": TextInput(attrs={"class": "form-control"}),
            "first_name": TextInput(attrs={"class": "form-control"}),
            "last_name": TextInput(attrs={"class": "form-control"}),
            "email": TextInput(attrs={"class": "form-control"}),
            "password": PasswordInput(attrs={"class": "form-control"}),
        }

        help_texts = {
            # "username": _("You will use your username as an alias and to log in."),
        }

        error_messages = {
            # "username": {
            #     "max_length": _("This username is too long."),
            # },
        }


class SubscriptionProfileForm(ModelForm):

    locale = ModelChoiceField(
        queryset=Locale.objects.all(),
        empty_label=None,
        widget=Select(attrs={"class": "form-control select2"}),
        label=_("Locale"),
        initial=1,
    )

    timezone = ModelChoiceField(
        queryset=TimeZone.objects.all(),
        empty_label=None,
        widget=Select(attrs={"class": "form-control select2"}),
        label=_("Timezone"),
        initial=446,
    )

    class Meta:
        model = Profile

        fields = (
            "locale",
            "timezone",
        )
