from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 1001)]


class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    quantity = forms.IntegerField(label='', widget=forms.TextInput(attrs={'type': 'number',
                                                                          'class': 'form-control',
                                                                          'style': 'height: 50px;',
                                                                          'placeholder': 'метров',
                                                                          'min': '1',
                                                                          'step': '1',
                                                                          'value': '1'}))

