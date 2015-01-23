from django.conf.urls import patterns, url

from .views import (
    DashboardView,
    SubscriptionsView,
    AccountsView,
    ModulesView,
)

urlpatterns = patterns(
    '',
    url(r'^dashboard$', DashboardView.as_view(), name='dashboard'),
    url(r'^subscriptions$', SubscriptionsView.as_view(), name='subscriptions'),
    url(r'^accounts$', AccountsView.as_view(), name='accounts'),
    url(r'^modules$', ModulesView.as_view(), name='modules'),
)
