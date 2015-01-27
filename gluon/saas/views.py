from itertools import chain
from uuid import uuid4

from django.conf import settings

from django.contrib.auth import get_user, get_user_model

from django.db.models import Q

from .models import (
    View as SaasView,
    Profile,
    MenuItem,
    Subscription,
    AccessAccount,
    Module,
)

from .forms import (
    SubscriptionForm,
    SubscriptionUserForm,
    SubscriptionProfileForm,
)

from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from django.views.generic.edit import ProcessFormView
from django.views.generic import ListView, DetailView
from django_datatables_view.base_datatable_view import BaseDatatableView

from django.core.urlresolvers import reverse

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.core.exceptions import ImproperlyConfigured


class SaasContextMixin(ContextMixin):
    """SAAS Context Mixin"""

    def get_context_data(self, **kwargs):
        # TODO: Permissions, security
        context = super(SaasContextMixin, self).get_context_data(**kwargs)

        # Get current view
        view_name = self.request.resolver_match.url_name
        view = SaasView.objects.filter(name=view_name).first()
        if view is None:
            raise ImproperlyConfigured(
                "The view {0} is not properly registered !".format(view_name))
        resources = view.resources_config.resources.all()

        # update context with data from view
        context.update({
            "view_name": view_name,
            "page_title": view.page_title,
            "page_keywords": ",".join(k.label for k in view.page_keywords.all()),
            "page_description": view.page_description,
            "metas": [r for r in resources if r.tag.name == "meta"],
            "styles": [r for r in resources
                       if r.tag.name == "link"
                       and r.browser.name == "all"],
            "ie_styles": [r for r in resources
                          if r.tag.name == "link"
                          and r.browser.name == "ie"],
            "ie6_styles": [r for r in resources
                           if r.tag.name == "link"
                           and r.browser.name == "ie6"],
            "ie7_styles": [r for r in resources
                           if r.tag.name == "link"
                           and r.browser.name == "ie7"],
            "ie67_styles": [r for r in resources
                            if r.tag.name == "link"
                            and r.browser.name == "ie67"],
            "ie8_styles": [r for r in resources
                           if r.tag.name == "link"
                           and r.browser.name == "ie8"],
            "ie678_styles": [r for r in resources
                             if r.tag.name == "link"
                             and r.browser.name == "ie678"],
            "ie9_styles": [r for r in resources
                           if r.tag.name == "link"
                           and r.browser.name == "ie9"],
            "scripts": [r for r in resources
                                if r.tag.name == "script"
                                and r.browser.name == "all"],
            "ie_scripts": [r for r in resources
                           if r.tag.name == "script"
                           and r.browser.name == "ie"],
            "ie6_scripts": [r for r in resources
                            if r.tag.name == "script"
                            and r.browser.name == "ie6"],
            "ie7_scripts": [r for r in resources
                            if r.tag.name == "script"
                            and r.browser.name == "ie7"],
            "ie67_scripts": [r for r in resources
                             if r.tag.name == "script"
                             and r.browser.name == "ie67"],
            "ie8_scripts": [r for r in resources
                            if r.tag.name == "script"
                            and r.browser.name == "ie8"],
            "ie678_scripts": [r for r in resources
                              if r.tag.name == "script"
                              and r.browser.name == "ie678"],
            "ie9_scripts": [r for r in resources
                            if r.tag.name == "script"
                            and r.browser.name == "ie9"],
        })

        # update context with data from app config
        context.update({
            "platform_name": settings.PLATFORM_NAME,
            "google_site_verification": settings.GOOGLE_SITE_VERIFICATION,
            "welcome_message": settings.WELCOME_MESSAGE,
        })

        # update context with data from user
        nb_notifications, is_authenticated = 0, False
        current_user_avatar_uri = "/static/images/anonymous.png"
        current_user_display_name = "Anonymous user"
        if self.request.user.is_authenticated():
            # Get current user and get or create profile
            is_authenticated = True
            user = get_user(self.request)
            menu = MenuItem.get_menu(view, user)
            profile = Profile.objects.filter(user=user).first()
            current_user_avatar_uri = "/static/images/authenticated.png"
            if not profile:
                current_user_display_name = "Authenticated user"
            else:
                current_user_display_name = profile.label
                if not current_user_display_name.strip():
                    current_user_display_name = user.username

                nb_notifications= len([
                    n for n in profile.notifications.all()
                    if n.status == "new"]),

                if profile.avatar:
                    current_user_avatar_uri = profile.avatar.url
        else:
            menu = MenuItem.get_default_menu(view)

        context.update({
            "nb_notifications": nb_notifications,
            "current_user_avatar_uri": current_user_avatar_uri,
            "current_user_display_name": current_user_display_name,
            "is_authenticated": is_authenticated,
            "menu": menu,
        })

        # update context with data from session
        context.update({
            "errors": [],  # TODO:
            "warns": [],  # TODO:
            "info": [],  # TODO:
            "confirms": [],  # TODO:
            "messages": [],  # TODO:
        })

        return context


########################
#                      #
#  SAAS Generic views  #
#                      #
########################


class SaasTemplateView(TemplateResponseMixin, SaasContextMixin, View):
    """
    A view that renders a template with SAAS Context.  This view will also pass
    into the context any keyword arguments passed by the url conf.
    """
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class SaasListView(ListView, SaasContextMixin):

    def get_context_data(self, **kwargs):
        context = super(SaasListView, self).get_context_data(**kwargs)
        return context


class SaasDetailView(DetailView, SaasContextMixin):

    def get_context_data(self, **kwargs):
        context = super(SaasDetailView, self).get_context_data(**kwargs)
        return context


class SaasProcessFormViewMixin:
    """Handle forms. form_classes are 2-tuples that contains key of forms
     set in context and its class"""

    def get_forms(self):
        if self.request.method == "POST":
            return dict((k, v(self.request.POST, prefix=k))
                         for k, v in self.form_classes)
        else:
            return dict((k, v(prefix=k))
                         for k, v in self.form_classes)

    def get_context_data(self, **kwargs):
        context = super(SaasProcessFormViewMixin, self).get_context_data(**kwargs)
        context.update(self.get_forms())
        return context

    def forms_are_valid(self, forms):
        return all(f.is_valid() for f in forms.values())

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        forms = self.get_forms()
        if self.forms_are_valid(forms):
            return self.form_valid(forms)
        else:
            return self.form_invalid(forms)


########################
#                      #
#  SAAS utility views  #
#                      #
########################


#
# Showcase views
#


class HomeView(SaasTemplateView):
    """Home Page"""

    template_name = "home.html"


class ThanksView(SaasTemplateView):
    """Home Page"""

    template_name = "thanks.html"


class SubscribeView(SaasProcessFormViewMixin, SaasTemplateView):
    """Subscribe Page"""

    form_classes = (
        ("subscription_user_form", SubscriptionUserForm),
        ("subscription_profile_form", SubscriptionProfileForm),
        ("subscription_form", SubscriptionForm),
    )

    template_name = "subscribe.html"

    def get_context_data(self, **kwargs):
        context = super(SubscribeView, self).get_context_data(**kwargs)
        context["modules"] = {m.id: m for m in Module.objects.all()}
        return context

    def form_valid(self, forms):
        import bpdb; bpdb.set_trace()
        user_form = forms["subscription_user_form"]
        user_password = user_form.cleaned_data.pop("password")
        user_form.cleaned_data["username"] = user_form.cleaned_data["email"]
        user = get_user_model()(**user_form.cleaned_data)
        user.set_password(user_password)
        user.save()

        profile = forms["subscription_profile_form"].save(commit=False)
        profile.user = user
        profile.save()

        subscription = forms["subscription_form"].save(commit=False)
        subscription.owner = user
        subscription.label = str(uuid4())
        subscription.save()
        for module in chain(Module.objects.filter(monthly_price=0),
                            forms["subscription_form"].cleaned_data["modules"]):
            subscription.modules.add(module)
        subscription.save()

        return HttpResponseRedirect(reverse("thanks"))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data())




#
# Dashboard
#


class DashboardView(SaasTemplateView):

    template_name = "dashboard.html"


#
# Subscription
#


class SubscriptionsView(SaasListView):

    model = Subscription

    template_name = "subscriptions.html"


class SubscriptionListJson(BaseDatatableView):

    model = Subscription

    # define the columns that will be returned
    columns = ["id", "label", "owner", "opened", "status"]

    order_columns = ["id", "label", "owner", "", "status"]

    # protection against attack attempts
    max_display_length = 500

    def render_column(self, row, column):
        if column == "status":
            return row.status.label.capitalize()
        elif column == "opened":
            return row.opened and "Yes" or "No"
        else:
            return super(SubscriptionListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in POST request to filter queryset

        # simple example:
        search = self.request.POST.get("search[value]", None)
        if search:
            qs = qs.filter(label__istartswith=search)

        return qs


class SubscriptionView(SaasDetailView):

    model = Subscription

    template_name = "subscription.html"


#
# Account
#


class AccountsView(SaasListView):

    model = AccessAccount

    template_name = "accounts.html"


#
# Module
#


class ModulesView(SaasListView):

    model = Module

    template_name = "modules.html"
