import warnings

from gravyboat.test.factories.address import *  # noqa
from gravyboat.test.factories.basket import *  # noqa
from gravyboat.test.factories.catalogue import *  # noqa
from gravyboat.test.factories.contrib import *  # noqa
from gravyboat.test.factories.customer import *  # noqa
from gravyboat.test.factories.offer import *  # noqa
from gravyboat.test.factories.order import *  # noqa
from gravyboat.test.factories.partner import *  # noqa
from gravyboat.test.factories.payment import *  # noqa
from gravyboat.test.factories.utils import *  # noqa
from gravyboat.test.factories.voucher import *  # noqa

message = (
    "Module '%s' is deprecated and will be removed in the next major version "
    "of django-gravyboat"
) % __name__

warnings.warn(message, PendingDeprecationWarning)
