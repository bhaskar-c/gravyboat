from django import forms

from gravyboat.core.loading import get_model

from gravyboat.apps.shipping.models import WeightBased

class WeightBasedForm(forms.ModelForm):

    class Meta:
        model = WeightBased
        fields = ['name', 'description', 'default_weight', 'countries']


class WeightBandForm(forms.ModelForm):

    def __init__(self, method, *args, **kwargs):
        super(WeightBandForm, self).__init__(*args, **kwargs)
        self.instance.method = method

    class Meta:
        from gravyboat.apps.shipping.models import WeightBand
        model = WeightBand
        fields = ('upper_limit', 'charge')
