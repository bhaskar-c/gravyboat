# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from gravyboat.defaults import *
from gravyboat import GRAVYBOAT_MAIN_TEMPLATE_DIR
from gravyboat import get_core_apps

import os
location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', x)



GRAVYBOAT_SHOP_NAME = 'gravyboat.store'
GRAVYBOAT_SHOP_TAGLINE = 'Hotel Restaurant & Catering Supplies'
GRAVYBOAT_DEFAULT_CURRENCY = 'INR'
DEBUG = True
#ALLOWED_HOSTS = ['localhost', '127.0.0.1']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')
MEDIA_URL = '/public/media/'

STATIC_URL = '/gravyboat/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/gravyboat/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'gravyboat/static/'),
)


SECRET_KEY = 'k27tn^%ym+y8zse$+=bm#e=+-k&(r^k3v--tt#-n%)5%uiqzn='




# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'compressor',
    'widget_tweaks',
    'debug_toolbar',

]


INSTALLED_APPS = INSTALLED_APPS + get_core_apps()

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            GRAVYBOAT_MAIN_TEMPLATE_DIR,
            location('templates'),
        ],

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.search.context_processors.search_form',
                'apps.promotions.context_processors.promotions',
                'apps.checkout.context_processors.checkout',
                'apps.customer.notifications.context_processors.notifications',
                'core.context_processors.metadata',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],

        },
    },
]

WSGI_APPLICATION = 'wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gravyboat',
        'USER': 'gravyboatuser',
        'PASSWORD': 'Sunshine1',
        'HOST': 'localhost',
        'PORT': '',
    }
}

SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'gravyboat.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = True
GRAVYBOAT_DEFAULT_CURRENCY = 'INR'

LANGUAGES = (('en', 'English'),)
