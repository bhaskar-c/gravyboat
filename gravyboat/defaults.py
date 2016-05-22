from collections import OrderedDict

from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

GRAVYBOAT_SHOP_NAME = 'Oscar'
GRAVYBOAT_SHOP_TAGLINE = ''
GRAVYBOAT_HOMEPAGE = reverse_lazy('promotions:home')

# Basket settings
GRAVYBOAT_BASKET_COOKIE_LIFETIME = 7 * 24 * 60 * 60
GRAVYBOAT_BASKET_COOKIE_OPEN = 'gravyboat_open_basket'
GRAVYBOAT_BASKET_COOKIE_SECURE = False
GRAVYBOAT_MAX_BASKET_QUANTITY_THRESHOLD = 10000

# Recently-viewed products
GRAVYBOAT_RECENTLY_VIEWED_COOKIE_LIFETIME = 7 * 24 * 60 * 60
GRAVYBOAT_RECENTLY_VIEWED_COOKIE_NAME = 'gravyboat_history'
GRAVYBOAT_RECENTLY_VIEWED_COOKIE_SECURE = False
GRAVYBOAT_RECENTLY_VIEWED_PRODUCTS = 20

# Currency
GRAVYBOAT_DEFAULT_CURRENCY = 'INR'

# Paths
GRAVYBOAT_IMAGE_FOLDER = 'images/products/%Y/%m/'
GRAVYBOAT_PROMOTION_FOLDER = 'images/promotions/'
GRAVYBOAT_DELETE_IMAGE_FILES = True

# Copy this image from gravyboat/static/img to your MEDIA_ROOT folder.
# It needs to be there so Sorl can resize it.
GRAVYBOAT_MISSING_IMAGE_URL = 'image_not_found.jpg'
GRAVYBOAT_UPLOAD_ROOT = '/tmp'

# Address settings
GRAVYBOAT_REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name', 'line1',
                                 'line4', 'postcode', 'country')

# Pagination settings

GRAVYBOAT_OFFERS_PER_PAGE = 20
GRAVYBOAT_PRODUCTS_PER_PAGE = 20
GRAVYBOAT_REVIEWS_PER_PAGE = 20
GRAVYBOAT_NOTIFICATIONS_PER_PAGE = 20
GRAVYBOAT_EMAILS_PER_PAGE = 20
GRAVYBOAT_ORDERS_PER_PAGE = 20
GRAVYBOAT_ADDRESSES_PER_PAGE = 20
GRAVYBOAT_STOCK_ALERTS_PER_PAGE = 20
GRAVYBOAT_DASHBOARD_ITEMS_PER_PAGE = 20

# Checkout
GRAVYBOAT_ALLOW_ANON_CHECKOUT = False

# Promotions
COUNTDOWN, LIST, SINGLE_PRODUCT, TABBED_BLOCK = (
    'Countdown', 'List', 'SingleProduct', 'TabbedBlock')
GRAVYBOAT_PROMOTION_MERCHANDISING_BLOCK_TYPES = (
    (COUNTDOWN, "Vertical list"),
    (LIST, "Horizontal list"),
    (TABBED_BLOCK, "Tabbed block"),
    (SINGLE_PRODUCT, "Single product"),
)
GRAVYBOAT_PROMOTION_POSITIONS = (('page', 'Page'),
                             ('right', 'Right-hand sidebar'),
                             ('left', 'Left-hand sidebar'))

# Reviews
GRAVYBOAT_ALLOW_ANON_REVIEWS = True
GRAVYBOAT_MODERATE_REVIEWS = False

# Accounts
GRAVYBOAT_ACCOUNTS_REDIRECT_URL = 'customer:profile-view'

# This enables sending alert notifications/emails instantly when products get
# back in stock by listening to stock record update signals.
# This might impact performance for large numbers of stock record updates.
# Alternatively, the management command ``gravyboat_send_alerts`` can be used to
# run periodically, e.g. as a cron job. In this case eager alerts should be
# disabled.
GRAVYBOAT_EAGER_ALERTS = True

# Registration
GRAVYBOAT_SEND_REGISTRATION_EMAIL = True
GRAVYBOAT_FROM_EMAIL = 'gravyboat@example.com'

# Slug handling
GRAVYBOAT_SLUG_FUNCTION = 'gravyboat.core.utils.default_slugifier'
GRAVYBOAT_SLUG_MAP = {}
GRAVYBOAT_SLUG_BLACKLIST = []

# Cookies
GRAVYBOAT_COOKIES_DELETE_ON_LOGOUT = ['gravyboat_recently_viewed_products', ]

# Hidden Oscar features, e.g. wishlists or reviews
GRAVYBOAT_HIDDEN_FEATURES = []

# Menu structure of the dashboard navigation
GRAVYBOAT_DASHBOARD_NAVIGATION = [
    {
        'label': _('Dashboard'),
        'icon': 'icon-th-list',
        'url_name': 'dashboard:index',
    },
    {
        'label': _('Catalogue'),
        'icon': 'icon-sitemap',
        'children': [
            {
                'label': _('Products'),
                'url_name': 'dashboard:catalogue-product-list',
            },
            {
                'label': _('Product Types'),
                'url_name': 'dashboard:catalogue-class-list',
            },
            {
                'label': _('Categories'),
                'url_name': 'dashboard:catalogue-category-list',
            },
            {
                'label': _('Ranges'),
                'url_name': 'dashboard:range-list',
            },
            {
                'label': _('Low stock alerts'),
                'url_name': 'dashboard:stock-alert-list',
            },
        ]
    },
    {
        'label': _('Fulfilment'),
        'icon': 'icon-shopping-cart',
        'children': [
            {
                'label': _('Orders'),
                'url_name': 'dashboard:order-list',
            },
            {
                'label': _('Statistics'),
                'url_name': 'dashboard:order-stats',
            },
            {
                'label': _('Partners'),
                'url_name': 'dashboard:partner-list',
            },
            # The shipping method dashboard is disabled by default as it might
            # be confusing. Weight-based shipping methods aren't hooked into
            # the shipping repository by default (as it would make
            # customising the repository slightly more difficult).
            # {
            #     'label': _('Shipping charges'),
            #     'url_name': 'dashboard:shipping-method-list',
            # },
        ]
    },
    {
        'label': _('Customers'),
        'icon': 'icon-group',
        'children': [
            {
                'label': _('Customers'),
                'url_name': 'dashboard:users-index',
            },
            {
                'label': _('Stock alert requests'),
                'url_name': 'dashboard:user-alert-list',
            },
        ]
    },
    {
        'label': _('Offers'),
        'icon': 'icon-bullhorn',
        'children': [
            {
                'label': _('Offers'),
                'url_name': 'dashboard:offer-list',
            },
            {
                'label': _('Vouchers'),
                'url_name': 'dashboard:voucher-list',
            },
        ],
    },
    {
        'label': _('Content'),
        'icon': 'icon-folder-close',
        'children': [
            {
                'label': _('Content blocks'),
                'url_name': 'dashboard:promotion-list',
            },
            {
                'label': _('Content blocks by page'),
                'url_name': 'dashboard:promotion-list-by-page',
            },
            {
                'label': _('Pages'),
                'url_name': 'dashboard:page-list',
            },
            {
                'label': _('Email templates'),
                'url_name': 'dashboard:comms-list',
            },
            {
                'label': _('Reviews'),
                'url_name': 'dashboard:reviews-list',
            },
        ]
    },
    {
        'label': _('Reports'),
        'icon': 'icon-bar-chart',
        'url_name': 'dashboard:reports-index',
    },
]
GRAVYBOAT_DASHBOARD_DEFAULT_ACCESS_FUNCTION = 'gravyboat.apps.dashboard.nav.default_access_fn'  # noqa

# Search facets
GRAVYBOAT_SEARCH_FACETS = {
    'fields': OrderedDict([
        # The key for these dicts will be used when passing facet data
        # to the template. Same for the 'queries' dict below.
        ('product_class', {'name': _('Type'), 'field': 'product_class'}),
        ('rating', {'name': _('Rating'), 'field': 'rating'}),
        # You can specify an 'options' element that will be passed to the
        # SearchQuerySet.facet() call.  It's hard to get 'missing' to work
        # correctly though as of Solr's hilarious syntax for selecting
        # items without a specific facet:
        # http://wiki.apache.org/solr/SimpleFacetParameters#facet.method
        # 'options': {'missing': 'true'}
    ]),
    'queries': OrderedDict([
        ('price_range',
         {
             'name': _('Price range'),
             'field': 'price',
             'queries': [
                 # This is a list of (name, query) tuples where the name will
                 # be displayed on the front-end.
                 (_('0 to 20'), u'[0 TO 20]'),
                 (_('20 to 40'), u'[20 TO 40]'),
                 (_('40 to 60'), u'[40 TO 60]'),
                 (_('60+'), u'[60 TO *]'),
             ]
         }),
    ]),
}

GRAVYBOAT_PRODUCT_SEARCH_HANDLER = None

GRAVYBOAT_SETTINGS = dict(
    [(k, v) for k, v in locals().items() if k.startswith('GRAVYBOAT_')])
