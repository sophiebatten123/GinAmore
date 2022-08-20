'''
Imports relevant django packages
'''
from django import forms
from .models import Cocktail, CocktailCategory, CocktailReview, CocktailIngredient
from django.forms import formset_factory


class CocktailForm(forms.ModelForm):
    '''
    Form to display the cocktail information
    '''
    class Meta:
        '''
        Cocktail fields generated within the form
        '''
        model = Cocktail
        fields = '__all__'
        exclude = ('image_url',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = CocktailCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class CocktailIngredientForm(forms.ModelForm):
    '''
    Form to display the cocktail ingredients information
    '''
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter ingredient here'
        })
    )
    quantity = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the quantity here'
        })
    )
    measurement = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the units of measurement here'
        })
    )

    class Meta:
        '''
        Coktail ingredient fields generated within the form
        '''
        model = CocktailIngredient
        fields = ('name', 'quantity', 'measurement',)


class CocktailReviewForm(forms.ModelForm):
    '''
    Creates the review for the cocktail recipe.
    '''
    class Meta:
        '''
        Specifies the model and fields that are displayed on the form.
        '''
        model = CocktailReview
        fields = ('user_review', )
