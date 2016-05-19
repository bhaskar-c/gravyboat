from django.conf.urls import url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class
from gravyboat.apps.dashboard.orders.views import OrderListView as order_list_view
from gravyboat.apps.dashboard.orders.views import OrderDetailView as order_detail_view
from gravyboat.apps.dashboard.orders.views import ShippingAddressUpdateView as shipping_address_view
from gravyboat.apps.dashboard.orders.views import LineDetailView as line_detail_view
from gravyboat.apps.dashboard.orders.views import OrderStatsView as order_stats_view


class OrdersDashboardApplication(Application):
    name = None
    default_permissions = ['is_staff', ]
    permissions_map = {
        'order-list': (['is_staff'], ['partner.dashboard_access']),
        'order-stats': (['is_staff'], ['partner.dashboard_access']),
        'order-detail': (['is_staff'], ['partner.dashboard_access']),
        'order-detail-note': (['is_staff'], ['partner.dashboard_access']),
        'order-line-detail': (['is_staff'], ['partner.dashboard_access']),
        'order-shipping-address': (['is_staff'], ['partner.dashboard_access']),
    }


    def get_urls(self):
        urls = [
            url(r'^$', order_list_view.as_view(), name='order-list'),
            url(r'^statistics/$', order_stats_view.as_view(),
                name='order-stats'),
            url(r'^(?P<number>[-\w]+)/$',
                order_detail_view.as_view(), name='order-detail'),
            url(r'^(?P<number>[-\w]+)/notes/(?P<note_id>\d+)/$',
                order_detail_view.as_view(), name='order-detail-note'),
            url(r'^(?P<number>[-\w]+)/lines/(?P<line_id>\d+)/$',
                line_detail_view.as_view(), name='order-line-detail'),
            url(r'^(?P<number>[-\w]+)/shipping-address/$',
                shipping_address_view.as_view(),
                name='order-shipping-address'),
        ]
        return self.post_process_urls(urls)


application = OrdersDashboardApplication()
