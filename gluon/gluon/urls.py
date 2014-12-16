from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    "",
    url(r"^admin/", include(admin.site.urls)),
#    url(r"^util/", include("util.urls")),
#    url(r"^saas/", include("saas.urls")),
#    url(r"^legal/", include("legal.urls")),
)
