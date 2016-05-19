from django.conf.urls import url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.dashboard.vouchers.views import VoucherListView as list_view
from gravyboat.apps.dashboard.vouchers.views import VoucherCreateView as create_view
from gravyboat.apps.dashboard.vouchers.views import VoucherUpdateView as update_view
from gravyboat.apps.dashboard.vouchers.views import VoucherDeleteView as delete_view
from gravyboat.apps.dashboard.vouchers.views import VoucherStatsView as stats_view

class VoucherDashboardApplication(Application):
    name = None
    default_permissions = ['is_staff', ]


    def get_urls(self):
        urls = [
            url(r'^$', list_view.as_view(), name='voucher-list'),
            url(r'^create/$', create_view.as_view(),
                name='voucher-create'),
            url(r'^update/(?P<pk>\d+)/$', update_view.as_view(),
                name='voucher-update'),
            url(r'^delete/(?P<pk>\d+)/$', delete_view.as_view(),
                name='voucher-delete'),
            url(r'^stats/(?P<pk>\d+)/$', stats_view.as_view(),
                name='voucher-stats'),
        ]
        return self.post_process_urls(urls)


application = VoucherDashboardApplication()
