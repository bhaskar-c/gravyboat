from django.conf.urls import include, url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.dashboard.views import IndexView as index_view
from gravyboat.apps.dashboard.reports.app import application as reports_app
from gravyboat.apps.dashboard.orders.app import application as orders_app
from gravyboat.apps.dashboard.users.app import application as users_app
from gravyboat.apps.dashboard.catalogue.app import application as catalogue_app
from gravyboat.apps.dashboard.promotions.app import application as promotions_app
from gravyboat.apps.dashboard.pages.app import application as pages_app
from gravyboat.apps.dashboard.partners.app import application as partners_app
from gravyboat.apps.dashboard.offers.app import application as offers_app
from gravyboat.apps.dashboard.ranges.app import application as ranges_app
from gravyboat.apps.dashboard.reviews.app import application as reviews_app
from gravyboat.apps.dashboard.vouchers.app import application as vouchers_app
from gravyboat.apps.dashboard.communications.app import application as comms_app
from gravyboat.apps.dashboard.shipping.app import application as shipping_app


class DashboardApplication(Application):
    name = 'dashboard'
    permissions_map = {
        'index': (['is_staff'], ['partner.dashboard_access']),
    }



    def get_urls(self):
        urls = [
            url(r'^$', index_view.as_view(), name='index'),
            url(r'^catalogue/', include(catalogue_app.urls)),
            url(r'^reports/', include(reports_app.urls)),
            url(r'^orders/', include(orders_app.urls)),
            url(r'^users/', include(users_app.urls)),
            url(r'^content-blocks/', include(promotions_app.urls)),
            url(r'^pages/', include(pages_app.urls)),
            url(r'^partners/', include(partners_app.urls)),
            url(r'^offers/', include(offers_app.urls)),
            url(r'^ranges/', include(ranges_app.urls)),
            url(r'^reviews/', include(reviews_app.urls)),
            url(r'^vouchers/', include(vouchers_app.urls)),
            url(r'^comms/', include(comms_app.urls)),
            url(r'^shipping/', include(shipping_app.urls)),
        ]
        return self.post_process_urls(urls)


application = DashboardApplication()
