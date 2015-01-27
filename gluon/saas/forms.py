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
        error_messages={"required": _("You must select at least one module")},
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
        }

        widgets = {
            "referrer": TextInput(attrs={"class": "form-control"}),
            "company_name": TextInput(attrs={"class": "form-control"}),
        }


class SubscriptionUserForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SubscriptionUserForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = True

    class Meta:
        model = get_user_model()

        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
        )

        labels = {
            "first_name": _("First name"),
            "last_name": _("Last name"),
            "email": _("Email"),
            "password": _("Password"),
        }

        widgets = {
            "first_name": TextInput(
                attrs={"class": "form-control",
                       "placeholder": _("Your first name")}),
            "last_name": TextInput(
                attrs={"class": "form-control",
                       "placeholder": _("Your last name")}),
            "email": TextInput(
                attrs={"class": "form-control",
                       "placeholder": _("Your email")}),
            "password": PasswordInput(
                attrs={"class": "form-control",
                       "placeholder": _("Your password")}),
        }

        error_messages = {
            "first_name": {
                "max_length": _("This first name is too long."),
                "required": _("The first name is mandatory"),
            },
            "last_name": {
                "max_length": _("This last name is too long."),
                "required": _("The last name is mandatory"),
            },
            "email": {
                "max_length": _("This email is too long."),
                "required": _("The email is mandatory"),
            },
            "password": {
                "required": _("The password is mandatory"),
            },
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
