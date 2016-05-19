from django.conf.urls import url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.dashboard.catalogue.views import ProductListView as product_list_view
from gravyboat.apps.dashboard.catalogue.views import ProductLookupView as product_lookup_view
from gravyboat.apps.dashboard.catalogue.views import ProductCreateRedirectView as product_create_redirect_view
from gravyboat.apps.dashboard.catalogue.views import ProductCreateUpdateView as product_createupdate_view
from gravyboat.apps.dashboard.catalogue.views import ProductDeleteView as product_delete_view

from gravyboat.apps.dashboard.catalogue.views import ProductClassCreateView as product_class_create_view
from gravyboat.apps.dashboard.catalogue.views import ProductClassUpdateView as product_class_update_view
from gravyboat.apps.dashboard.catalogue.views import ProductClassListView as product_class_list_view
from gravyboat.apps.dashboard.catalogue.views import ProductClassDeleteView as product_class_delete_view

from gravyboat.apps.dashboard.catalogue.views import CategoryListView as category_list_view
from gravyboat.apps.dashboard.catalogue.views import CategoryDetailListView as category_detail_list_view
from gravyboat.apps.dashboard.catalogue.views import CategoryCreateView as category_create_view
from gravyboat.apps.dashboard.catalogue.views import CategoryUpdateView as category_update_view
from gravyboat.apps.dashboard.catalogue.views import CategoryDeleteView as category_delete_view
from gravyboat.apps.dashboard.catalogue.views import StockAlertListView as stock_alert_view


class CatalogueApplication(Application):
    name = None

    default_permissions = ['is_staff', ]
    permissions_map = _map = {
        'catalogue-product': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-product-create': (['is_staff'],
                                     ['partner.dashboard_access']),
        'catalogue-product-list': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-product-delete': (['is_staff'],
                                     ['partner.dashboard_access']),
        'catalogue-product-lookup': (['is_staff'],
                                     ['partner.dashboard_access']),
    }



    def get_urls(self):
        urls = [
            url(r'^products/(?P<pk>\d+)/$',
                product_createupdate_view.as_view(),
                name='catalogue-product'),
            url(r'^products/create/$',
                product_create_redirect_view.as_view(),
                name='catalogue-product-create'),
            url(r'^products/create/(?P<product_class_slug>[\w-]+)/$',
                product_createupdate_view.as_view(),
                name='catalogue-product-create'),
            url(r'^products/(?P<parent_pk>[-\d]+)/create-variant/$',
                product_createupdate_view.as_view(),
                name='catalogue-product-create-child'),
            url(r'^products/(?P<pk>\d+)/delete/$',
                product_delete_view.as_view(),
                name='catalogue-product-delete'),
            url(r'^$', product_list_view.as_view(),
                name='catalogue-product-list'),
            url(r'^stock-alerts/$', stock_alert_view.as_view(),
                name='stock-alert-list'),
            url(r'^product-lookup/$', product_lookup_view.as_view(),
                name='catalogue-product-lookup'),
            url(r'^categories/$', category_list_view.as_view(),
                name='catalogue-category-list'),
            url(r'^categories/(?P<pk>\d+)/$',
                category_detail_list_view.as_view(),
                name='catalogue-category-detail-list'),
            url(r'^categories/create/$', category_create_view.as_view(),
                name='catalogue-category-create'),
            url(r'^categories/create/(?P<parent>\d+)$',
                category_create_view.as_view(),
                name='catalogue-category-create-child'),
            url(r'^categories/(?P<pk>\d+)/update/$',
                category_update_view.as_view(),
                name='catalogue-category-update'),
            url(r'^categories/(?P<pk>\d+)/delete/$',
                category_delete_view.as_view(),
                name='catalogue-category-delete'),
            url(r'^product-type/create/$',
                product_class_create_view.as_view(),
                name='catalogue-class-create'),
            url(r'^product-types/$',
                product_class_list_view.as_view(),
                name='catalogue-class-list'),
            url(r'^product-type/(?P<pk>\d+)/update/$',
                product_class_update_view.as_view(),
                name='catalogue-class-update'),
            url(r'^product-type/(?P<pk>\d+)/delete/$',
                product_class_delete_view.as_view(),
                name='catalogue-class-delete'),
        ]
        return self.post_process_urls(urls)


application = CatalogueApplication()
