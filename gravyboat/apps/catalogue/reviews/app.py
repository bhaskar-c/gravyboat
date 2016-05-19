from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.catalogue.reviews.views import ProductReviewDetail as detail_view
from gravyboat.apps.catalogue.reviews.views import CreateProductReview as create_view
from gravyboat.apps.catalogue.reviews.views import AddVoteView as vote_view
from gravyboat.apps.catalogue.reviews.views import ProductReviewList as list_view


class ProductReviewsApplication(Application):
    name = None
    hidable_feature_name = "reviews"

    def get_urls(self):
        urls = [
            url(r'^(?P<pk>\d+)/$', detail_view.as_view(),
                name='reviews-detail'),
            url(r'^add/$', create_view.as_view(),
                name='reviews-add'),
            url(r'^(?P<pk>\d+)/vote/$',
                login_required(vote_view.as_view()),
                name='reviews-vote'),
            url(r'^$', list_view.as_view(), name='reviews-list'),
        ]
        return self.post_process_urls(urls)


application = ProductReviewsApplication()
