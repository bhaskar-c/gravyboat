from django.conf.urls import url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.dashboard.offers.views import OfferListView as list_view
from gravyboat.apps.dashboard.offers.views import OfferMetaDataView as metadata_view
from gravyboat.apps.dashboard.offers.views import OfferConditionView as condition_view
from gravyboat.apps.dashboard.offers.views import OfferBenefitView as benefit_view
from gravyboat.apps.dashboard.offers.views import OfferRestrictionsView as restrictions_view
from gravyboat.apps.dashboard.offers.views import OfferDeleteView as delete_view
from gravyboat.apps.dashboard.offers.views import OfferDetailView as detail_view

class OffersDashboardApplication(Application):
    name = None
    default_permissions = ['is_staff', ]


    def get_urls(self):
        urls = [
            url(r'^$', list_view.as_view(), name='offer-list'),
            # Creation
            url(r'^new/name-and-description/$', metadata_view.as_view(),
                name='offer-metadata'),
            url(r'^new/condition/$', condition_view.as_view(),
                name='offer-condition'),
            url(r'^new/incentive/$', benefit_view.as_view(),
                name='offer-benefit'),
            url(r'^new/restrictions/$', restrictions_view.as_view(),
                name='offer-restrictions'),
            # Update
            url(r'^(?P<pk>\d+)/name-and-description/$',
                metadata_view.as_view(update=True),
                name='offer-metadata'),
            url(r'^(?P<pk>\d+)/condition/$',
                condition_view.as_view(update=True),
                name='offer-condition'),
            url(r'^(?P<pk>\d+)/incentive/$',
                benefit_view.as_view(update=True),
                name='offer-benefit'),
            url(r'^(?P<pk>\d+)/restrictions/$',
                restrictions_view.as_view(update=True),
                name='offer-restrictions'),
            # Delete
            url(r'^(?P<pk>\d+)/delete/$',
                delete_view.as_view(), name='offer-delete'),
            # Stats
            url(r'^(?P<pk>\d+)/$', detail_view.as_view(),
                name='offer-detail'),
        ]
        return self.post_process_urls(urls)


application = OffersDashboardApplication()
