from django.core.urlresolvers import reverse
from django.views.generic import RedirectView, TemplateView
from gravyboat.apps.catalogue import models
from django.views.generic import TemplateView
from gravyboat.apps.catalogue.models import Category


class HomeView(TemplateView):
    template_name = 'promotions/home.html'

    def get_context_data(self, **kwargs):
        category_wise_products = {}
        categories = Category.objects.all()
        for category in categories:
            products_in_this_category_id = models.Product.objects.filter(
                product_class_id=category.pk)
            if not products_in_this_category_id:
                continue
            category_wise_products[category] = []
            for product in products_in_this_category_id:
                category_wise_products[category].append(product)
        context = super(HomeView, self).get_context_data(**kwargs)
        context['category_wise_products'] = category_wise_products
        context['latest_products'] = models.Product.objects.filter(
            parent=None).order_by('-date_created')
        return context


class RecordClickView(RedirectView):
    """
    Simple RedirectView that helps recording clicks made on promotions
    """
    permanent = False
    model = None

    def get_redirect_url(self, **kwargs):
        try:
            prom = self.model.objects.get(pk=kwargs['pk'])
        except self.model.DoesNotExist:
            return reverse('promotions:home')

        if prom.promotion.has_link:
            prom.record_click()
            return prom.link_url
        return reverse('promotions:home')
