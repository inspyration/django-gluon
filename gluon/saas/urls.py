from django.conf.urls import patterns, url

from .views import DashboardView

urlpatterns = patterns(
    '',
    url(r'^dashboard$', DashboardView.as_view(), name='dashboard'),
)
