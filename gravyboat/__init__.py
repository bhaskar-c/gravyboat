import os

# Use 'dev', 'beta', or 'final' as the 4th element to indicate release type.
VERSION = (1, 2, 1, 'final')


def get_short_version():
    return '%s.%s' % (VERSION[0], VERSION[1])


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    # Append 3rd digit if > 0
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    elif VERSION[3] != 'final':
        version = '%s %s' % (version, VERSION[3])
        if len(VERSION) == 5:
            version = '%s %s' % (version, VERSION[4])
    return version


# Cheeky setting that allows each template to be accessible by two paths.
# Eg: the template 'gravyboat/templates/gravyboat/base.html' can be accessed via both
# 'base.html' and 'gravyboat/base.html'.  This allows Oscar's templates to be
# extended by templates with the same filename
GRAVYBOAT_MAIN_TEMPLATE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'templates/gravyboat')

GRAVYBOAT_CORE_APPS = [
    'gravyboat',
    'gravyboat.apps.analytics',
    'gravyboat.apps.checkout',
    'gravyboat.apps.address',
    'gravyboat.apps.shipping',
    'gravyboat.apps.catalogue',
    'gravyboat.apps.catalogue.reviews',
    'gravyboat.apps.partner',
    'gravyboat.apps.basket',
    'gravyboat.apps.payment',
    'gravyboat.apps.offer',
    'gravyboat.apps.order',
    'gravyboat.apps.customer',
    'gravyboat.apps.promotions',
    'gravyboat.apps.search',
    'gravyboat.apps.voucher',
    'gravyboat.apps.wishlists',
    'gravyboat.apps.dashboard',
    'gravyboat.apps.dashboard.reports',
    'gravyboat.apps.dashboard.users',
    'gravyboat.apps.dashboard.orders',
    'gravyboat.apps.dashboard.promotions',
    'gravyboat.apps.dashboard.catalogue',
    'gravyboat.apps.dashboard.offers',
    'gravyboat.apps.dashboard.partners',
    'gravyboat.apps.dashboard.pages',
    'gravyboat.apps.dashboard.ranges',
    'gravyboat.apps.dashboard.reviews',
    'gravyboat.apps.dashboard.vouchers',
    'gravyboat.apps.dashboard.communications',
    'gravyboat.apps.dashboard.shipping',
    # 3rd-party apps that gravyboat depends on
    'haystack',
    'treebeard',
    'sorl.thumbnail',
    'django_tables2',
]


def get_core_apps():
    return GRAVYBOAT_CORE_APPS

