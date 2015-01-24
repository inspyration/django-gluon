from django.conf.urls import patterns, url

from .views import (
    DashboardView,
    SubscriptionsView,
    AccountsView,
    ModulesView,
    SubscriptionListJson,
)

urlpatterns = patterns(
    '',
    url(r'^dashboard$', DashboardView.as_view(), name='dashboard'),
    url(r'^subscriptions$', SubscriptionsView.as_view(), name='subscriptions'),
    url(r'^accounts$', AccountsView.as_view(), name='accounts'),
    url(r'^modules$', ModulesView.as_view(), name='modules'),
    # Datatables
    url(r'^subscriptions/data/$', SubscriptionListJson.as_view(), name='subscriptions_json'),
)
