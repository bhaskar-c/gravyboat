from django.core.urlresolvers import reverse
from django.views.generic import RedirectView, TemplateView
from gravyboat.apps.catalogue import models
from django.views.generic import TemplateView
from gravyboat.apps.catalogue.models import Category


class HomeView(TemplateView):
    template_name = 'promotions/home.html'

    def get_context_data(self, **kwargs):
        category_wise_products = {}
        # depth, description, id, image, includes, name, numchild, path, product, productcategory, slug
        categories = Category.objects.filter(depth=1)
        our_handpicked_products = []
        for category in categories:
            products_in_this_category_id = models.Product.objects.filter(
                categories=category.pk)
            # Choices are: attribute_values, attributes, basket_lines, categories, children, date_created, date_updated,
            # description, excludes, handpickedproductlist, id, images, includes, is_discountable, line, orderedproduct,
            # parent, parent_id, primary_recommendations, product, product_class, product_class_id, product_options,
            # productalert, productcategory, productrecommendation, rangeproduct, rating, recommended_products, reviews,
            #  singleproduct, slug, stats, stockrecords, structure, title, upc, userproductview, wishlists_lines
            if not products_in_this_category_id:
                continue
            category_wise_products[category] = []
            for product in products_in_this_category_id:
                category_wise_products[category].append(product)
                attr_val = product.attribute_values.get(attribute__code='is_featured')
                if attr_val.value:
                    print('yes')
                    our_handpicked_products.append(product)
            print(our_handpicked_products)
        context = super(HomeView, self).get_context_data(**kwargs)
        context['category_wise_products'] = category_wise_products
        context['latest_products'] = models.Product.objects.filter(
            parent=None).order_by('-date_created')
        context['our_handpicked_products'] = our_handpicked_products
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
