from django.conf.urls import url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.dashboard.reviews.views import ReviewListView as list_view
from gravyboat.apps.dashboard.reviews.views import ReviewUpdateView as update_view
from gravyboat.apps.dashboard.reviews.views import ReviewDeleteView as delete_view

class ReviewsApplication(Application):
    name = None
    default_permissions = ['is_staff', ]

    def get_urls(self):
        urls = [
            url(r'^$', list_view.as_view(), name='reviews-list'),
            url(r'^(?P<pk>\d+)/$', update_view.as_view(),
                name='reviews-update'),
            url(r'^(?P<pk>\d+)/delete/$', delete_view.as_view(),
                name='reviews-delete'),
        ]
        return self.post_process_urls(urls)


application = ReviewsApplication()
