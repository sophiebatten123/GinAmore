'''
Imports relevant django packages
'''
from django.shortcuts import render
from .models import Cocktail


def cocktails(request):
    '''
    A view to return the render all cocktail recipes
    '''

    cocktail = Cocktail.objects.all()

    context = {
        'cocktail': cocktail,
    }

    return render(request, 'cocktails/cocktails.html', context)
