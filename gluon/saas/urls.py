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
    SettingsView,
    NotificationsView,
    NotificationListJson,
    ContactView,
    IssuesView,
    IssueListJson,
    IssueView,
    IssueNewView,
    ContactUsView,
    AboutUsView,
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
    # Back-office
    url(r"^dashboard/$", DashboardView.as_view(), name="dashboard"),
    url(r"^dashboard/settings/$", SettingsView.as_view(), name="settings"),
    url(r"^dashboard/notifications/$", NotificationsView.as_view(),
        name="notifications"),
    url(r"dashboard/notifications/data/$", NotificationListJson.as_view(),
        name="notifications_json"),
    url(r"^dashboard/contact/$", ContactView.as_view(), name="contact"),
    url(r"^dashboard/issues/$", IssuesView.as_view(), name="issues"),
    url(r"dashboard/issues/data/$", IssueListJson.as_view(),
        name="issues_json"),
    url(r"^dashboard/issues/view/(?P<pk>[-_\w]+)/$", IssueView.as_view(),
        name="issue"),
    url(r"^dashboard/issues/new/$", IssueNewView.as_view(), name="new_issue"),
    # Showcase
    url(r"^contact_us/$", ContactUsView.as_view(), name="contact_us"),
    url(r"^about_us/$", AboutUsView.as_view(), name="about_us"),

)
