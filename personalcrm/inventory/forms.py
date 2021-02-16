from django import forms
from quote.models import Brand
from crispy_forms.layout import Fieldset


class NewProductForm(forms.Form):
    brand_choices = Brand.objects.values_list()

    pn = forms.CharField(max_length=50, label="Part Number (PN)")
    brand = forms.ChoiceField(choices=brand_choices)
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)
    list_price = forms.IntegerField(required=False)
    multiplier = forms.DecimalField(required=False, max_digits=5, decimal_places=3)
    stock = forms.IntegerField(required=False, initial=0)
    note = forms.CharField(widget=forms.Textarea, required=False, label='Internal Notes')

