from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.basket.views import BasketView as summary_view
from gravyboat.apps.basket.views import SavedView as saved_view
from gravyboat.apps.basket.views import BasketAddView as add_view
from gravyboat.apps.basket.views import VoucherAddView as add_voucher_view
from gravyboat.apps.basket.views import VoucherRemoveView as remove_voucher_view


class BasketApplication(Application):
    name = 'basket'

    def get_urls(self):
        urls = [
            url(r'^$', summary_view.as_view(), name='summary'),
            url(r'^add/(?P<pk>\d+)/$', add_view.as_view(), name='add'),
            url(r'^vouchers/add/$', add_voucher_view.as_view(),
                name='vouchers-add'),
            url(r'^vouchers/(?P<pk>\d+)/remove/$',
                remove_voucher_view.as_view(), name='vouchers-remove'),
            url(r'^saved/$', login_required(saved_view.as_view()),
                name='saved'),
        ]
        return self.post_process_urls(urls)


application = BasketApplication()
