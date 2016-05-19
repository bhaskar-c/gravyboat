from django.conf.urls import url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.dashboard.communications.views import ListView as list_view
from gravyboat.apps.dashboard.communications.views import UpdateView as update_view

class CommsDashboardApplication(Application):
    name = None
    default_permissions = ['is_staff', ]


    def get_urls(self):
        urls = [
            url(r'^$', list_view.as_view(), name='comms-list'),
            url(r'^(?P<slug>\w+)/$', update_view.as_view(),
                name='comms-update'),
        ]
        return self.post_process_urls(urls)


application = CommsDashboardApplication()
