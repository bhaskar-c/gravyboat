from django.conf.urls import url

from gravyboat.apps.promotions.models import KeywordPromotion, PagePromotion
from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.promotions.views import HomeView as home_view
from gravyboat.apps.promotions.views import RecordClickView as  record_click_view

class PromotionsApplication(Application):
    name = 'promotions'


    def get_urls(self):
        urls = [
            url(r'page-redirect/(?P<page_promotion_id>\d+)/$',
                record_click_view.as_view(model=PagePromotion),
                name='page-click'),
            url(r'keyword-redirect/(?P<keyword_promotion_id>\d+)/$',
                record_click_view.as_view(model=KeywordPromotion),
                name='keyword-click'),
            url(r'^$', home_view.as_view(), name='home'),
        ]
        return self.post_process_urls(urls)


application = PromotionsApplication()
