from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AddressConfig(AppConfig):
    label = 'address'
    name = 'gravyboat.apps.address'
    verbose_name = _('Address')
