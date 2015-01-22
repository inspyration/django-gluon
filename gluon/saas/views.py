from django.shortcuts import render

from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from .models import View as SaasView
# Create your views here.

from django.core.exceptions import ImproperlyConfigured


def get_saas_context(context, *args, **kwargs):
    """Inject SAAS Context into view context"""

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
        if self.request.user.is_anonymous():
            context.update({
                "nb_notifications": 0,
                "current_user_avatar_uri": "/static/images/anonymous.png",
                "current_user_display_name": "Anonymous user"
            })
        else:
            # Get current user
            user = self.request.user.username
            context.update({
                "nb_notifications": None, # TODO:
                "current_user_avatar_uri": None, # TODO:
                "current_user_display_name": None, # TODO:
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
