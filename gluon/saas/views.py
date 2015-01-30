from itertools import chain
from uuid import uuid4

from django.conf import settings

from django.contrib.auth import (
    get_user,
    get_user_model,
    authenticate,
    login,
    logout
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import (
    View as SaasView,
    Profile,
    MenuItem,
    Subscription,
    AccessAccount,
    Module,
    AccessRole)

from .forms import (
    SubscriptionForm,
    SubscriptionUserForm,
    SubscriptionProfileForm,
)

from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from django.views.generic.edit import ProcessFormView
from django.views.generic import ListView, DetailView, CreateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from django.core.urlresolvers import reverse

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

from django.core.mail import send_mail

from django.utils.translation import ugettext_lazy as _

from django.core.exceptions import ImproperlyConfigured


class SaasContextMixin(ContextMixin):
    """SAAS Context Mixin"""

    def get_context_data(self, **kwargs):
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


class SaasCreateView(CreateView, SaasContextMixin):

    def get_context_data(self, **kwargs):
        if not hasattr(self, 'object'):
            self.object = None
        context = super(SaasCreateView, self).get_context_data(**kwargs)
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


class ProtectedViewMixin():

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedViewMixin, self).dispatch(*args, **kwargs)


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


class LoginView(SaasTemplateView):
    """Home Page"""

    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            HttpResponseRedirect(reverse("saas:dashboard"))
        return super(LoginView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Check auth and do the log in.
        """
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                next_uri = request.GET.get("next")
                if next_uri:
                    return HttpResponseRedirect(next_uri)
                return HttpResponseRedirect(reverse("saas:dashboard"))
            else:
                return HttpResponseRedirect(reverse("saas:login"))
        else:
            return HttpResponseRedirect(reverse("saas:login"))


class LogoutView(SaasTemplateView):
    """Home Page"""

    template_name = "logout.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


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
        subscription.label = str(uuid4()).replace("-", "")
        subscription.save()
        for module in chain(Module.objects.filter(monthly_price=0),
                            forms["subscription_form"].cleaned_data["modules"]):
            subscription.modules.add(module)
        subscription.save()

        account = AccessAccount(
            user=user,
            subscription=subscription,
            role=AccessRole.objects.get(name="SASS_management__manager"),
        )
        account.save()

        profile.account_in_use = account

        # TODO: Envoi de courriel avec une URL pour gérer la validation.

        return HttpResponseRedirect(reverse("saas:subscribe_thanks"))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data())


class ThanksView(SaasTemplateView):
    """Home Page"""

    template_name = "thanks.html"


class SubscriptionValidationView(SaasTemplateView):  # TODO
    """Home Page"""

    template_name = "todo.html"


class SendInvitationView(View):

    def post(self, request, *args, **kwargs):
        """
        Check auth and do the log in.
        """
        email = request.POST.get("invitation-email")
        if not email:
            return JsonResponse({"success": False, "message": "Empty email"})

        user = get_user_model().objects.filter(username=email).first()
        if user is None:
             pass # create user
        # create account
        # create notification

        try:
            send_mail(
                _("You have been invited to join the Gluon project"),
                _("Click here"),
                "contact@inspyration.fr",
                [email],
                fail_silently=False)
        except Exception as e:
            return JsonResponse({"success": False, "message": "Email not sent"})

        return JsonResponse(
            {"success": True, "data": ["", email, "user", "created"]})


#
# Dashboard
#


class DashboardView(ProtectedViewMixin, SaasTemplateView):  # TODO

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
    columns = ["id", "label", "owner", "category", "status"]

    order_columns = ["id", "label", "owner", "category", "status"]

    # protection against attack attempts
    max_display_length = 500

    def render_column(self, row, column):
        if column == "status":
            return row.status.label
        if column == "owner":
            return row.owner.profile.label
        if column == "category":
            return row.category.label
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


class AccountsView(SaasListView):  # TODO

    model = AccessAccount

    template_name = "todo.html"


class AccountView(SaasDetailView):  # TODO

    model = AccessAccount

    template_name = "todo.html"


class AccountListJson(BaseDatatableView):  # TODO

    model = AccessAccount


class ProfileView(SaasTemplateView):  # TODO

    model = AccessAccount

    template_name = "todo.html"


#
# back-office
#


class SettingsView(SaasTemplateView):  # TODO
    """Home Page"""

    template_name = "todo.html"


class NotificationsView(SaasListView):  # TODO

    model = AccessAccount

    template_name = "todo.html"


class NotificationListJson(BaseDatatableView):  # TODO

    model = AccessAccount


class ContactView(SaasTemplateView):  # TODO
    """Home Page"""

    template_name = "todo.html"


class IssuesView(SaasListView):  # TODO

    model = AccessAccount

    template_name = "todo.html"


class IssueListJson(BaseDatatableView):  # TODO

    model = AccessAccount


class IssueView(SaasDetailView):  # TODO

    model = Subscription

    template_name = "todo.html"


class IssueNewView(SaasTemplateView):  # TODO
    """Home Page"""

    template_name = "todo.html"


class ContactUsView(SaasTemplateView):  # TODO
    """Home Page"""

    template_name = "todo.html"


class AboutUsView(SaasTemplateView):  # TODO
    """Home Page"""

    template_name = "todo.html"