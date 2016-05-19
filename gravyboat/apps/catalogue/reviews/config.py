from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CatalogueReviewsConfig(AppConfig):
    label = 'reviews'
    name = 'gravyboat.apps.catalogue.reviews'
    verbose_name = _('Catalogue reviews')
