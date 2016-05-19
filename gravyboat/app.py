# flake8: noqa, because URL syntax is more readable with long lines

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class
from gravyboat.views.decorators import login_forbidden


from gravyboat.apps.catalogue.app import application as catalogue_app
from gravyboat.apps.customer.app import application as customer_app
from gravyboat.apps.basket.app import application as basket_app
from gravyboat.apps.checkout.app import application as checkout_app
from gravyboat.apps.promotions.app import application as promotions_app
from gravyboat.apps.search.app import application as search_app
from gravyboat.apps.dashboard.app import application as dashboard_app
from gravyboat.apps.offer.app import application as offer_app

from gravyboat.apps.customer.forms import PasswordResetForm as password_reset_form
from gravyboat.apps.customer.forms import SetPasswordForm as set_password_form


class Shop(Application):
    name = None

    def get_urls(self):
        urls = [
            url(r'^catalogue/', include(catalogue_app.urls)),
            url(r'^basket/', include(basket_app.urls)),
            url(r'^checkout/', include(checkout_app.urls)),
            url(r'^accounts/', include(customer_app.urls)),
            url(r'^search/', include(search_app.urls)),
            url(r'^dashboard/', include(dashboard_app.urls)),
            url(r'^offers/', include(offer_app.urls)),

            # Password reset - as we're using Django's default view functions,
            # we can't namespace these urls as that prevents
            # the reverse function from working.
            url(r'^password-reset/$',
                login_forbidden(auth_views.password_reset),
                {'password_reset_form': password_reset_form,
                 'post_reset_redirect': reverse_lazy('password-reset-done')},
                name='password-reset'),
            url(r'^password-reset/done/$',
                login_forbidden(auth_views.password_reset_done),
                name='password-reset-done'),
            url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                login_forbidden(auth_views.password_reset_confirm),
                {
                    'post_reset_redirect': reverse_lazy('password-reset-complete'),
                    'set_password_form': set_password_form,
                },
                name='password-reset-confirm'),
            url(r'^password-reset/complete/$',
                login_forbidden(auth_views.password_reset_complete),
                name='password-reset-complete'),
            url(r'', include(promotions_app.urls)),
        ]
        return urls

application = Shop()
