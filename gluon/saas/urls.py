from django.conf.urls import patterns, url

from .views import (
    HomeView,
    AccountsView,
    AccountView,
    AccountListJson,
    ProfileView,
    LoginView,
    LogoutView,
    SubscriptionsView,
    SubscriptionListJson,
    SubscriptionView,
    SubscribeView,
    ThanksView,
    SubscriptionValidationView,
    DashboardView,
)

urlpatterns = patterns(
    "",
    url(r"^$", HomeView.as_view(), name="home"),
    # SAAS Accounts management
    url(r"^accounts/$", AccountsView.as_view(), name="accounts"),
    url(r"^accounts/data/$", AccountView.as_view(), name="account_json"),
    url(r"^accounts/view/(?P<pk>[-_\w]+)/$", AccountListJson.as_view(),
        name="account"),
    # Authentication
    url(r"^accounts/profile/$", ProfileView.as_view(), name="profile"),
    url(r"^accounts/login/$", LoginView.as_view(), name="login"),
    url(r"^accounts/logout/$", LogoutView.as_view(), name="logout"),
    # SAAS Subscription management
    url(r"^subscriptions/$", SubscriptionsView.as_view(), name="subscriptions"),
    url(r"^subscriptions/data/$", SubscriptionListJson.as_view(),
        name="subscriptions_json"),
    url(r"^subscriptions/view/(?P<pk>[-_\w]+)/$", SubscriptionView.as_view(),
        name="subscription"),
    # SAAS Subscription creation process
    url(r"^subscribe/$", SubscribeView.as_view(), name="subscribe"),
    url(r"^/subscribe/thanks/$", ThanksView.as_view(), name="thanks"),
    url(r"^/subscribe/validation/(?P<pk>[-_\w]+)/$",
        SubscriptionValidationView.as_view(), name="validation"),
    # Back-office main page
    url(r"^dashboard/$", DashboardView.as_view(), name="dashboard"),
)
