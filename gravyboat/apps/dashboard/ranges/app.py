from django.conf.urls import url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class
from gravyboat.apps.dashboard.ranges.views import RangeListView as list_view
from gravyboat.apps.dashboard.ranges.views import RangeCreateView as create_view
from gravyboat.apps.dashboard.ranges.views import RangeUpdateView as update_view
from gravyboat.apps.dashboard.ranges.views import RangeDeleteView as delete_view
from gravyboat.apps.dashboard.ranges.views import RangeProductListView as products_view
from gravyboat.apps.dashboard.ranges.views import RangeReorderView as reorder_view


class RangeDashboardApplication(Application):
    name = None
    default_permissions = ['is_staff', ]


    def get_urls(self):
        urlpatterns = [
            url(r'^$', list_view.as_view(), name='range-list'),
            url(r'^create/$', create_view.as_view(), name='range-create'),
            url(r'^(?P<pk>\d+)/$', update_view.as_view(),
                name='range-update'),
            url(r'^(?P<pk>\d+)/delete/$', delete_view.as_view(),
                name='range-delete'),
            url(r'^(?P<pk>\d+)/products/$', products_view.as_view(),
                name='range-products'),
            url(r'^(?P<pk>\d+)/reorder/$', reorder_view.as_view(),
                name='range-reorder'),
        ]
        return self.post_process_urls(urlpatterns)


application = RangeDashboardApplication()
