from django.conf.urls.static import static
from gravyboat import settings

from django.conf.urls import include, url
from django.contrib import admin
from gravyboat.app import application

urlpatterns = [
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'', include(application.urls)),
            ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
