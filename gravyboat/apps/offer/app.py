from django.conf.urls import url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.offer.views import OfferDetailView, OfferListView


class OfferApplication(Application):
    name = 'offer'
    detail_view = OfferDetailView
    list_view = OfferListView

    def get_urls(self):
        urls = [
            url(r'^$', self.list_view.as_view(), name='list'),
            url(r'^(?P<slug>[\w-]+)/$', self.detail_view.as_view(),
                name='detail'),
        ]
        return self.post_process_urls(urls)


application = OfferApplication()
