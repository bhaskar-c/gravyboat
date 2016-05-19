from django.conf.urls import url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class
from gravyboat.apps.dashboard.reports.views import IndexView as index_view


class ReportsApplication(Application):
    name = None
    default_permissions = ['is_staff', ]

    def get_urls(self):
        urls = [
            url(r'^$', index_view.as_view(), name='reports-index'),
        ]
        return self.post_process_urls(urls)


application = ReportsApplication()
