from gravyboat import settings

from django.conf.urls import include, url
from django.contrib import admin
from gravyboat.app import application


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(application.urls)),

]
if settings.DEBUG:
  urlpatterns.append(url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
