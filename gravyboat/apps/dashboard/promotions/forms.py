from django import forms
from django.conf import settings
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from gravyboat.apps.promotions.conf import PROMOTION_CLASSES
from gravyboat.core.loading import get_class, get_classes
from gravyboat.forms.fields import ExtendedURLField

from gravyboat.apps.promotions.models import HandPickedProductList, RawHTML, SingleProduct, PagePromotion, OrderedProduct
from gravyboat.apps.dashboard.catalogue.widgets import ProductSelect



class PromotionTypeSelectForm(forms.Form):
    choices = []
    for klass in PROMOTION_CLASSES:
        choices.append((klass.classname(), klass._meta.verbose_name))
    promotion_type = forms.ChoiceField(choices=tuple(choices),
                                       label=_("Promotion type"))


class RawHTMLForm(forms.ModelForm):
    class Meta:
        model = RawHTML
        fields = ['name', 'body']

    def __init__(self, *args, **kwargs):
        super(RawHTMLForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['class'] = "no-widget-init"


class SingleProductForm(forms.ModelForm):
    class Meta:
        model = SingleProduct
        fields = ['name', 'product', 'description']
        widgets = {'product': ProductSelect}

    def __init__(self, *args, **kwargs):
        super(SingleProductForm, self).__init__(*args, **kwargs)
        self.fields['product'].widget.attrs['class'] = "select2 input-xlarge"


class HandPickedProductListForm(forms.ModelForm):
    class Meta:
        model = HandPickedProductList
        fields = ['name', 'description', 'link_url', 'link_text']


class OrderedProductForm(forms.ModelForm):
    class Meta:
        model = OrderedProduct
        fields = ['list', 'product', 'display_order']
        widgets = {
            'product': ProductSelect,
        }

    def __init__(self, *args, **kwargs):
        super(OrderedProductForm, self).__init__(*args, **kwargs)
        self.fields['product'].widget.attrs['class'] = "select2 input-xlarge"


OrderedProductFormSet = inlineformset_factory(
    HandPickedProductList, OrderedProduct, form=OrderedProductForm, extra=2)


class PagePromotionForm(forms.ModelForm):
    page_url = ExtendedURLField(label=_("URL"), verify_exists=True)
    position = forms.CharField(
        widget=forms.Select(choices=settings.GRAVYBOAT_PROMOTION_POSITIONS),
        label=_("Position"),
        help_text=_("Where in the page this content block will appear"))

    class Meta:
        model = PagePromotion
        fields = ['position', 'page_url']

    def clean_page_url(self):
        page_url = self.cleaned_data.get('page_url')
        if not page_url:
            return page_url

        if page_url.startswith('http'):
            raise forms.ValidationError(
                _("Content blocks can only be linked to internal URLs"))

        if page_url.startswith('/') and not page_url.endswith('/'):
            page_url += '/'

        return page_url
