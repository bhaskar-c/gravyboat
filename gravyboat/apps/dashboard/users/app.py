from django.conf.urls import url

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class
from gravyboat.apps.dashboard.users.views import IndexView as index_view
from gravyboat.apps.dashboard.users.views import UserDetailView as user_detail_view
from gravyboat.apps.dashboard.users.views import PasswordResetView as password_reset_view
from gravyboat.apps.dashboard.users.views import ProductAlertListView as alert_list_view
from gravyboat.apps.dashboard.users.views import ProductAlertUpdateView as alert_update_view
from gravyboat.apps.dashboard.users.views import ProductAlertDeleteView as alert_delete_view

class UserManagementApplication(Application):
    name = None
    default_permissions = ['is_staff', ]




    def get_urls(self):
        urls = [
            url(r'^$', index_view.as_view(), name='users-index'),
            url(r'^(?P<pk>-?\d+)/$',
                user_detail_view.as_view(), name='user-detail'),
            url(r'^(?P<pk>-?\d+)/password-reset/$',
                password_reset_view.as_view(),
                name='user-password-reset'),

            # Alerts
            url(r'^alerts/$',
                alert_list_view.as_view(),
                name='user-alert-list'),
            url(r'^alerts/(?P<pk>-?\d+)/delete/$',
                alert_delete_view.as_view(),
                name='user-alert-delete'),
            url(r'^alerts/(?P<pk>-?\d+)/update/$',
                alert_update_view.as_view(),
                name='user-alert-update'),
        ]
        return self.post_process_urls(urls)


application = UserManagementApplication()
