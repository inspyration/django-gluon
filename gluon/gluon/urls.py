from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin

from pathlib import Path


urlpatterns = patterns(
    "",
    url(r"^admin/", include(admin.site.urls)),
#    url(r"^util/", include("util.urls")),
    url(r"", include("saas.urls", "saas", "saas")),
#    url(r"^legal/", include("legal.urls")),
)

modules = set()
if Path("apps.txt").is_file():
    with open("apps.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line[0] == "#":
                continue
            else:
                modules.add(line)

if modules:
    urlpatterns += patterns(
        "",
        *tuple(url(r"^modules/{0}/".format(module),
                   include("{0}.urls".format(module), module, module))
        for module in modules))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
