from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PromotionsConfig(AppConfig):
    label = 'promotions'
    name = 'gravyboat.apps.promotions'
    verbose_name = _('Promotions')
