from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.checkout.views  import IndexView as index_view
from gravyboat.apps.checkout.views  import ShippingAddressView as shipping_address_view
from gravyboat.apps.checkout.views  import UserAddressUpdateView as user_address_update_view
from gravyboat.apps.checkout.views  import UserAddressDeleteView as user_address_delete_view
from gravyboat.apps.checkout.views  import ShippingMethodView as shipping_method_view
from gravyboat.apps.checkout.views  import PaymentMethodView as payment_method_view
from gravyboat.apps.checkout.views  import PaymentDetailsView as payment_details_view
from gravyboat.apps.checkout.views  import ThankYouView as thankyou_view

class CheckoutApplication(Application):
    name = 'checkout'



    def get_urls(self):
        urls = [
            url(r'^$', index_view.as_view(), name='index'),

            # Shipping/user address views
            url(r'shipping-address/$',
                shipping_address_view.as_view(), name='shipping-address'),
            url(r'user-address/edit/(?P<pk>\d+)/$',
                user_address_update_view.as_view(),
                name='user-address-update'),
            url(r'user-address/delete/(?P<pk>\d+)/$',
                user_address_delete_view.as_view(),
                name='user-address-delete'),

            # Shipping method views
            url(r'shipping-method/$',
                shipping_method_view.as_view(), name='shipping-method'),

            # Payment views
            url(r'payment-method/$',
                payment_method_view.as_view(), name='payment-method'),
            url(r'payment-details/$',
                payment_details_view.as_view(), name='payment-details'),

            # Preview and thankyou
            url(r'preview/$',
                payment_details_view.as_view(preview=True),
                name='preview'),
            url(r'thank-you/$', thankyou_view.as_view(),
                name='thank-you'),
        ]
        return self.post_process_urls(urls)

    def get_url_decorator(self, pattern):
        if not settings.OSCAR_ALLOW_ANON_CHECKOUT:
            return login_required
        if pattern.name.startswith('user-address'):
            return login_required
        return None


application = CheckoutApplication()
