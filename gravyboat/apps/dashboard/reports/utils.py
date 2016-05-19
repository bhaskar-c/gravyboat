

from gravyboat.apps.order.reports import OrderReportGenerator
from gravyboat.apps.analytics.reports import ProductReportGenerator, UserReportGenerator
from gravyboat.apps.basket.reports import OpenBasketReportGenerator, SubmittedBasketReportGenerator
from gravyboat.apps.offer.reports import OfferReportGenerator
from gravyboat.apps.voucher.reports import VoucherReportGenerator


class GeneratorRepository(object):

    generators = [OrderReportGenerator,
                  ProductReportGenerator,
                  UserReportGenerator,
                  OpenBasketReportGenerator,
                  SubmittedBasketReportGenerator,
                  VoucherReportGenerator,
                  OfferReportGenerator]

    def get_report_generators(self):
        return self.generators

    def get_generator(self, code):
        for generator in self.generators:
            if generator.code == code:
                return generator
        return None
