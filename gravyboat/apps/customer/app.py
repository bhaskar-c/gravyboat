from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views import generic

from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.customer.views import AccountSummaryView as  summary_view
from gravyboat.apps.customer.views import OrderHistoryView as  order_history_view
from gravyboat.apps.customer.views import OrderDetailView as  order_detail_view
from gravyboat.apps.customer.views  import AnonymousOrderDetailView as  anon_order_detail_view
from gravyboat.apps.customer.views import OrderLineView as  order_line_view

from gravyboat.apps.customer.views import AddressListView as address_list_view
from gravyboat.apps.customer.views import AddressCreateView as address_create_view
from gravyboat.apps.customer.views import AddressUpdateView as address_update_view
from gravyboat.apps.customer.views import AddressDeleteView as address_delete_view
from gravyboat.apps.customer.views import AddressChangeStatusView as address_change_status_view

from gravyboat.apps.customer.views import EmailHistoryView as  email_list_view
from gravyboat.apps.customer.views import EmailDetailView as email_detail_view
from gravyboat.apps.customer.views import AccountAuthView as login_view
from gravyboat.apps.customer.views import LogoutView as logout_view
from gravyboat.apps.customer.views import AccountRegistrationView as register_view
from gravyboat.apps.customer.views import ProfileView as profile_view
from gravyboat.apps.customer.views import ProfileUpdateView as profile_update_view
from gravyboat.apps.customer.views import ProfileDeleteView as profile_delete_view
from gravyboat.apps.customer.views import ChangePasswordView as change_password_view

from gravyboat.apps.customer.notifications.views import InboxView as notification_inbox_view
from gravyboat.apps.customer.notifications.views import ArchiveView as notification_archive_view
from gravyboat.apps.customer.notifications.views import UpdateView as notification_update_view
from gravyboat.apps.customer.notifications.views import DetailView as notification_detail_view

from gravyboat.apps.customer.alerts.views  import ProductAlertListView as alert_list_view
from gravyboat.apps.customer.alerts.views import ProductAlertCreateView as alert_create_view
from gravyboat.apps.customer.alerts.views import ProductAlertConfirmView as alert_confirm_view
from gravyboat.apps.customer.alerts.views import ProductAlertCancelView as alert_cancel_view

from gravyboat.apps.customer.wishlists.views import WishListAddProduct as wishlists_add_product_view
from gravyboat.apps.customer.wishlists.views import WishListListView as wishlists_list_view
from gravyboat.apps.customer.wishlists.views import WishListDetailView as wishlists_detail_view
from gravyboat.apps.customer.wishlists.views import WishListCreateView as wishlists_create_view
from gravyboat.apps.customer.wishlists.views import WishListCreateView as wishlists_create_with_product_view
from gravyboat.apps.customer.wishlists.views import WishListUpdateView as wishlists_update_view
from gravyboat.apps.customer.wishlists.views import WishListDeleteView as wishlists_delete_view
from gravyboat.apps.customer.wishlists.views import WishListRemoveProduct as wishlists_remove_product_view
from gravyboat.apps.customer.wishlists.views import WishListMoveProductToAnotherWishList as wishlists_move_product_to_another_view


class CustomerApplication(Application):
    name = 'customer'

    def get_urls(self):
        urls = [
            # Login, logout and register doesn't require login
            url(r'^login/$', login_view.as_view(), name='login'),
            url(r'^logout/$', logout_view.as_view(), name='logout'),
            url(r'^register/$', register_view.as_view(), name='register'),
            url(r'^$', login_required(summary_view.as_view()),
                name='summary'),
            url(r'^change-password/$',
                login_required(change_password_view.as_view()),
                name='change-password'),

            # Profile
            url(r'^profile/$',
                login_required(profile_view.as_view()),
                name='profile-view'),
            url(r'^profile/edit/$',
                login_required(profile_update_view.as_view()),
                name='profile-update'),
            url(r'^profile/delete/$',
                login_required(profile_delete_view.as_view()),
                name='profile-delete'),

            # Order history
            url(r'^orders/$',
                login_required(order_history_view.as_view()),
                name='order-list'),
            url(r'^order-status/(?P<order_number>[\w-]*)/(?P<hash>\w+)/$',
                anon_order_detail_view.as_view(), name='anon-order'),
            url(r'^orders/(?P<order_number>[\w-]*)/$',
                login_required(order_detail_view.as_view()),
                name='order'),
            url(r'^orders/(?P<order_number>[\w-]*)/(?P<line_id>\d+)$',
                login_required(order_line_view.as_view()),
                name='order-line'),

            # Address book
            url(r'^addresses/$',
                login_required(address_list_view.as_view()),
                name='address-list'),
            url(r'^addresses/add/$',
                login_required(address_create_view.as_view()),
                name='address-create'),
            url(r'^addresses/(?P<pk>\d+)/$',
                login_required(address_update_view.as_view()),
                name='address-detail'),
            url(r'^addresses/(?P<pk>\d+)/delete/$',
                login_required(address_delete_view.as_view()),
                name='address-delete'),
            url(r'^addresses/(?P<pk>\d+)/'
                r'(?P<action>default_for_(billing|shipping))/$',
                login_required(address_change_status_view.as_view()),
                name='address-change-status'),

            # Email history
            url(r'^emails/$',
                login_required(email_list_view.as_view()),
                name='email-list'),
            url(r'^emails/(?P<email_id>\d+)/$',
                login_required(email_detail_view.as_view()),
                name='email-detail'),

            # Notifications
            # Redirect to notification inbox
            url(r'^notifications/$', generic.RedirectView.as_view(
                url='/accounts/notifications/inbox/')),
            url(r'^notifications/inbox/$',
                login_required(notification_inbox_view.as_view()),
                name='notifications-inbox'),
            url(r'^notifications/archive/$',
                login_required(notification_archive_view.as_view()),
                name='notifications-archive'),
            url(r'^notifications/update/$',
                login_required(notification_update_view.as_view()),
                name='notifications-update'),
            url(r'^notifications/(?P<pk>\d+)/$',
                login_required(notification_detail_view.as_view()),
                name='notifications-detail'),

            # Alerts
            # Alerts can be setup by anonymous users: some views do not
            # require login
            url(r'^alerts/$',
                login_required(alert_list_view.as_view()),
                name='alerts-list'),
            url(r'^alerts/create/(?P<pk>\d+)/$',
                alert_create_view.as_view(),
                name='alert-create'),
            url(r'^alerts/confirm/(?P<key>[a-z0-9]+)/$',
                alert_confirm_view.as_view(),
                name='alerts-confirm'),
            url(r'^alerts/cancel/key/(?P<key>[a-z0-9]+)/$',
                alert_cancel_view.as_view(),
                name='alerts-cancel-by-key'),
            url(r'^alerts/cancel/(?P<pk>[a-z0-9]+)/$',
                login_required(alert_cancel_view.as_view()),
                name='alerts-cancel-by-pk'),

            # Wishlists
            url(r'wishlists/$',
                login_required(wishlists_list_view.as_view()),
                name='wishlists-list'),
            url(r'wishlists/add/(?P<product_pk>\d+)/$',
                login_required(wishlists_add_product_view.as_view()),
                name='wishlists-add-product'),
            url(r'wishlists/(?P<key>[a-z0-9]+)/add/(?P<product_pk>\d+)/',
                login_required(wishlists_add_product_view.as_view()),
                name='wishlists-add-product'),
            url(r'wishlists/create/$',
                login_required(wishlists_create_view.as_view()),
                name='wishlists-create'),
            url(r'wishlists/create/with-product/(?P<product_pk>\d+)/$',
                login_required(wishlists_create_view.as_view()),
                name='wishlists-create-with-product'),
            # Wishlists can be publicly shared, no login required
            url(r'wishlists/(?P<key>[a-z0-9]+)/$',
                wishlists_detail_view.as_view(), name='wishlists-detail'),
            url(r'wishlists/(?P<key>[a-z0-9]+)/update/$',
                login_required(wishlists_update_view.as_view()),
                name='wishlists-update'),
            url(r'wishlists/(?P<key>[a-z0-9]+)/delete/$',
                login_required(wishlists_delete_view.as_view()),
                name='wishlists-delete'),
            url(r'wishlists/(?P<key>[a-z0-9]+)/lines/(?P<line_pk>\d+)/delete/',
                login_required(wishlists_remove_product_view.as_view()),
                name='wishlists-remove-product'),
            url(r'wishlists/(?P<key>[a-z0-9]+)/products/(?P<product_pk>\d+)/'
                r'delete/',
                login_required(wishlists_remove_product_view.as_view()),
                name='wishlists-remove-product'),
            url(r'wishlists/(?P<key>[a-z0-9]+)/lines/(?P<line_pk>\d+)/move-to/'
                r'(?P<to_key>[a-z0-9]+)/$',
                login_required(wishlists_move_product_to_another_view
                               .as_view()),
                name='wishlists-move-product-to-another')]

        return self.post_process_urls(urls)


application = CustomerApplication()
