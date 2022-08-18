'''
Imports relevant django packages
'''
from django import forms
from .models import Cocktail, Category


class CocktailForm(forms.ModelForm):
    '''
    Form to display the cocktail information
    '''
    class Meta:
        '''
        Category fields generated within the form
        '''
        model = Cocktail
        fields = '__all__'
        exclude = ('image_url',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
