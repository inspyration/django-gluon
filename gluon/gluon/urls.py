from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin


urlpatterns = patterns(
    "",
    url(r"^admin/", include(admin.site.urls)),
#    url(r"^util/", include("util.urls")),
    url(r"", include("saas.urls")),
#    url(r"^legal/", include("legal.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
