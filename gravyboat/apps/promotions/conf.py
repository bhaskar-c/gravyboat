from gravyboat.core.loading import get_class

from gravyboat.apps.promotions.models import SingleProduct
from gravyboat.apps.promotions.models import RawHTML
from gravyboat.apps.promotions.models import Image
from gravyboat.apps.promotions.models import PagePromotion
from gravyboat.apps.promotions.models import AutomaticProductList
from gravyboat.apps.promotions.models import HandPickedProductList
from gravyboat.apps.promotions.models import MultiImage


def get_promotion_classes():
    return (RawHTML, Image, SingleProduct, AutomaticProductList,
            HandPickedProductList, MultiImage)


PROMOTION_CLASSES = get_promotion_classes()
