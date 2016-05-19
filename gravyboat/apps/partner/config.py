from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PartnerConfig(AppConfig):
    label = 'partner'
    name = 'gravyboat.apps.partner'
    verbose_name = _('Partner')

    def ready(self):
        from . import receivers  # noqa
