from django.conf.urls import url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.dashboard.shipping.views import WeightBasedListView, WeightBasedCreateView, WeightBasedUpdateView, \
    WeightBasedDeleteView, WeightBasedDetailView, WeightBandUpdateView, WeightBandDeleteView


class ShippingDashboardApplication(Application):
    name = None
    default_permissions = ['is_staff']

    weight_method_list_view = WeightBasedListView
    weight_method_create_view = WeightBasedCreateView
    weight_method_edit_view = WeightBasedUpdateView
    weight_method_delete_view = WeightBasedDeleteView
    # This doubles as the weight_band create view
    weight_method_detail_view = WeightBasedDetailView
    weight_band_edit_view = WeightBandUpdateView
    weight_band_delete_view = WeightBandDeleteView

    def get_urls(self):
        urlpatterns = [
            url(r'^weight-based/$', self.weight_method_list_view.as_view(),
                name='shipping-method-list'),
            url(r'^weight-based/create/$',
                self.weight_method_create_view.as_view(),
                name='shipping-method-create'),
            url(r'^weight-based/(?P<pk>\d+)/$',
                self.weight_method_detail_view.as_view(),
                name='shipping-method-detail'),
            url(r'^weight-based/(?P<pk>\d+)/edit/$',
                self.weight_method_edit_view.as_view(),
                name='shipping-method-edit'),
            url(r'^weight-based/(?P<pk>\d+)/delete/$',
                self.weight_method_delete_view.as_view(),
                name='shipping-method-delete'),
            url(r'^weight-based/(?P<method_pk>\d+)/bands/(?P<pk>\d+)/$',
                self.weight_band_edit_view.as_view(),
                name='shipping-method-band-edit'),
            url(r'^weight-based/(?P<method_pk>\d+)/bands/(?P<pk>\d+)/delete/$',
                self.weight_band_delete_view.as_view(),
                name='shipping-method-band-delete'),
        ]
        return self.post_process_urls(urlpatterns)


application = ShippingDashboardApplication()
