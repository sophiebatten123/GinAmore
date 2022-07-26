'''
Imports relevant django packages
'''
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    '''
    Form to display the product information
    '''
    class Meta:
        '''
        Product fields generated within the form
        '''
        model = Product
        exclude = ('likes', 'image_url',)

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    '''
    Creates the review for the procudt.
    '''
    class Meta:
        '''
        Specifies the model and fields that are displayed on the form.
        '''
        model = Review
        fields = ('user_review', )
