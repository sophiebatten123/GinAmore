from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class meta:
        model = Order
        fields = ('full_name',
                  'phone_number',
                  'email',
                  'street_address1',
                  'street_address2',
                  'town_or_city',
                  'postcode',
                  'county',
                  'country',)

    def __init__(self, *args, **kwargs):
        '''
        Add placehlders and classes, remove labels
        set the focus on the first field
        '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postcode',
            'town_or_city': 'Town/City',
            'street_address1': 'Street Address 1',
            'stree_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attr['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
