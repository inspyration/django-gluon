from django.conf import settings

from .models import View as SaasView, Profile, MenuItem

from django.views.generic.base import ContextMixin, TemplateResponseMixin, View

from django.contrib.auth import get_user

from django.shortcuts import render

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
            raise ImproperlyConfigured("A view is not properly registered !")
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
            "menu": MenuItem.tree.get_roots(),
        })

        # update context with data from user
        nb_notifications, is_authenticated = 0, False
        current_user_avatar_uri = "/static/images/anonymous.png"
        current_user_display_name = "Anonymous user"
        if self.request.user.is_authenticated():
            # Get current user and get or create profile
            is_authenticated = True
            user = get_user(self.request)
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

        context.update({
            "nb_notifications": nb_notifications,
            "current_user_avatar_uri": current_user_avatar_uri,
            "current_user_display_name": current_user_display_name,
            "is_authenticated": is_authenticated,
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


class SaasTemplateView(TemplateResponseMixin, SaasContextMixin, View):
    """
    A view that renders a template with SAAS Context.  This view will also pass
    into the context any keyword arguments passed by the url conf.
    """
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class DashboardView(SaasTemplateView):
    template_name = "dashboard.html"


class SubscriptionsView(SaasTemplateView):
    template_name = "subscriptions.html"


class AccountsView(SaasTemplateView):
    template_name = "accounts.html"


class ModulesView(SaasTemplateView):
    template_name = "modules.html"
