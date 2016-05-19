from django.conf.urls import include, url

from gravyboat.apps.catalogue.reviews.app import application as reviews_app
from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.catalogue.views import ProductDetailView as detail_view
from gravyboat.apps.catalogue.views import CatalogueView as catalogue_view
from gravyboat.apps.catalogue.views import ProductCategoryView as category_view
from gravyboat.apps.offer.views import RangeDetailView as range_view


class BaseCatalogueApplication(Application):
    name = 'catalogue'

    def get_urls(self):
        urlpatterns = super(BaseCatalogueApplication, self).get_urls()
        urlpatterns += [
            url(r'^$', catalogue_view.as_view(), name='index'),
            url(r'^(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$',
                detail_view.as_view(), name='detail'),
            url(r'^category/(?P<category_slug>[\w-]+(/[\w-]+)*)_(?P<pk>\d+)/$',
                category_view.as_view(), name='category'),
            # Fallback URL if a user chops of the last part of the URL
            url(r'^category/(?P<category_slug>[\w-]+(/[\w-]+)*)/$',
                category_view.as_view()),
            url(r'^ranges/(?P<slug>[\w-]+)/$',
                range_view.as_view(), name='range')]
        return self.post_process_urls(urlpatterns)


class ReviewsApplication(Application):
    name = None
    reviews_app = reviews_app

    def get_urls(self):
        urlpatterns = super(ReviewsApplication, self).get_urls()
        urlpatterns += [
            url(r'^(?P<product_slug>[\w-]*)_(?P<product_pk>\d+)/reviews/',
                include(self.reviews_app.urls)),
        ]
        return self.post_process_urls(urlpatterns)


class CatalogueApplication(BaseCatalogueApplication, ReviewsApplication):
    """
    Composite class combining Products with Reviews
    """


application = CatalogueApplication()
