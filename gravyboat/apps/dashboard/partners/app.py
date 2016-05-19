from django.conf.urls import url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class
from gravyboat.apps.dashboard.partners.views import PartnerListView as list_view
from gravyboat.apps.dashboard.partners.views import PartnerCreateView as create_view
from gravyboat.apps.dashboard.partners.views import PartnerManageView as manage_view
from gravyboat.apps.dashboard.partners.views import PartnerDeleteView as delete_view

from gravyboat.apps.dashboard.partners.views import PartnerUserLinkView as user_link_view
from gravyboat.apps.dashboard.partners.views import PartnerUserUnlinkView as user_unlink_view
from gravyboat.apps.dashboard.partners.views import PartnerUserCreateView as user_create_view
from gravyboat.apps.dashboard.partners.views import PartnerUserSelectView as user_select_view
from gravyboat.apps.dashboard.partners.views import PartnerUserUpdateView as user_update_view

class PartnersDashboardApplication(Application):
    name = None
    default_permissions = ['is_staff', ]



    def get_urls(self):
        urls = [
            url(r'^$', list_view.as_view(), name='partner-list'),
            url(r'^create/$', create_view.as_view(),
                name='partner-create'),
            url(r'^(?P<pk>\d+)/$', manage_view.as_view(),
                name='partner-manage'),
            url(r'^(?P<pk>\d+)/delete/$', delete_view.as_view(),
                name='partner-delete'),

            url(r'^(?P<partner_pk>\d+)/users/add/$',
                user_create_view.as_view(),
                name='partner-user-create'),
            url(r'^(?P<partner_pk>\d+)/users/select/$',
                user_select_view.as_view(),
                name='partner-user-select'),
            url(r'^(?P<partner_pk>\d+)/users/(?P<user_pk>\d+)/link/$',
                user_link_view.as_view(), name='partner-user-link'),
            url(r'^(?P<partner_pk>\d+)/users/(?P<user_pk>\d+)/unlink/$',
                user_unlink_view.as_view(), name='partner-user-unlink'),
            url(r'^(?P<partner_pk>\d+)/users/(?P<user_pk>\d+)/update/$',
                user_update_view.as_view(),
                name='partner-user-update'),
        ]
        return self.post_process_urls(urls)


application = PartnersDashboardApplication()
