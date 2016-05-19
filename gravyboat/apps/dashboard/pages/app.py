from django.conf.urls import url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.dashboard.pages.views import PageListView as list_view
from gravyboat.apps.dashboard.pages.views import PageCreateView as create_view
from gravyboat.apps.dashboard.pages.views import PageUpdateView as update_view
from gravyboat.apps.dashboard.pages.views import PageDeleteView as delete_view


class FlatPageManagementApplication(Application):
    name = None
    default_permissions = ['is_staff', ]

    def get_urls(self):
        """
        Get URL patterns defined for flatpage management application.
        """
        urls = [
            url(r'^$', list_view.as_view(), name='page-list'),
            url(r'^create/$', create_view.as_view(), name='page-create'),
            url(r'^update/(?P<pk>[-\w]+)/$',
                update_view.as_view(), name='page-update'),
            url(r'^delete/(?P<pk>\d+)/$',
                delete_view.as_view(), name='page-delete')
        ]
        return self.post_process_urls(urls)


application = FlatPageManagementApplication()
