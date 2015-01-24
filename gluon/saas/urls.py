from django.conf.urls import patterns, url

from .views import (
    DashboardView,
    SubscriptionsView,
    AccountsView,
    ModulesView,
    SubscriptionListJson,
    SubscriptionView,
)

urlpatterns = patterns(
    '',
    url(r'^dashboard$', DashboardView.as_view(), name='dashboard'),
    # Subscription
    url(r'^subscriptions/data/$', SubscriptionListJson.as_view(), name='subscriptions_json'),
    url(r'^subscriptions/view/(?P<pk>[-_\w]+)/$', SubscriptionView.as_view(), name='subscription'),
    url(r'^subscriptions$', SubscriptionsView.as_view(), name='subscriptions'),
    # Account
    url(r'^accounts$', AccountsView.as_view(), name='accounts'),
    # Module
    url(r'^modules$', ModulesView.as_view(), name='modules'),
)
