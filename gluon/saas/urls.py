from django.conf.urls import patterns, url

from .views import (
    HomeView,
    LoginView,
    LogoutView,
    SubscribeView,
    ThanksView,
    DashboardView,
    SubscriptionsView,
    AccountsView,
    ModulesView,
    SubscriptionListJson,
    SubscriptionView,
    SubscriptionValidationView,
)

urlpatterns = patterns(
    "",
    url(r"^$", HomeView.as_view(), name="home"),
    url(r"^login$", LoginView.as_view(), name="login"),
    url(r"^logout$", LogoutView.as_view(), name="logout"),
    url(r"^subscribe$", SubscribeView.as_view(), name="subscribe"),
    url(r"^/subscribe/thanks$", ThanksView.as_view(), name="thanks"),
    url(r"^/subscribe/validation/(?P<pk>[-_\w]+)$", SubscriptionValidationView.as_view(), name="validation"),
    url(r"^dashboard$", DashboardView.as_view(), name="dashboard"),
    # Subscription
    url(r"^subscriptions$", SubscriptionsView.as_view(), name="subscriptions"),
    url(r"^subscriptions/data/$", SubscriptionListJson.as_view(), name="subscriptions_json"),
    url(r"^subscriptions/view/(?P<pk>[-_\w]+)/$", SubscriptionView.as_view(), name="subscription"),
    # Account
    url(r"^accounts$", AccountsView.as_view(), name="accounts"),
    # Module
    url(r"^modules$", ModulesView.as_view(), name="modules"),
)
