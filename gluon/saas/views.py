from .models import View as SaasView, Profile

from django.views.generic.base import ContextMixin, TemplateResponseMixin, View

from django.contrib.auth import get_user

from django.shortcuts import render

from django.core.exceptions import ImproperlyConfigured


class SaasContextMixin(ContextMixin):
    """SAAS Context Mixin"""

    def get_context_data(self, **kwargs):
        context = super(SaasContextMixin, self).get_context_data(**kwargs)

        # Get current view
        url_name = self.request.resolver_match.url_name
        view = SaasView.objects.filter(label=url_name).first()
        if view is None:
            raise ImproperlyConfigured("A view is not properly registered !")
        resources = view.resources.all()

        # update context with data from view
        context.update({
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
            "google_site_verification": None, # TODO:
            "welcome_message": None, # TODO:
        })

        # update context with data from user
        context.update({
            "nb_notifications": 0,
            "current_user_avatar_uri": "/static/images/anonymous.png",
            "current_user_display_name": "Anonymous user"
        })
        if self.request.user.is_authenticated():
            # Get current user and get or create profile
            user = get_user(self.request)
            profile = Profile.objects.filter(user=user).first()
            if not profile:
                profile = Profile
                profile.user = user
                profile.save()

            display_name = profile.label
            if not display_name.strip():
                display_name = user.username

            context.update({
                "nb_notifications": len([
                    n for n in profile.notifications.all()
                    if n.status == "new"]),
                "current_user_display_name": display_name,
            })

            if profile.avatar:
                context.update({
                    "current_user_avatar_uri": profile.avatar.url,
            })

        # update context with data from session
        context.update({
            "errors": [], # TODO:
            "warns": [], # TODO:
            "info": [], # TODO:
            "confirms": [], # TODO:
            "messages": [], # TODO:
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
