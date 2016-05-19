from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PromotionsDashboardConfig(AppConfig):
    label = 'promotions_dashboard'
    name = 'gravyboat.apps.dashboard.promotions'
    verbose_name = _('Promotions dashboard')
