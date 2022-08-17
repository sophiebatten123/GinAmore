'''
Imports relevant django packages
'''
from django.shortcuts import render, get_object_or_404
from .models import Cocktail


def cocktails(request):
    '''
    A view to return the render all cocktail recipes
    '''
    cocktails = Cocktail.objects.all()
    categories = None

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        cocktails = cocktails.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    context = {
        'cocktails': cocktails,
        'current_categories': categories,
    }

    return render(request, 'cocktails/cocktails.html', context)


def cocktail_detail(request, product_id):
    '''
    A view to return the cocktails recipe information
    '''
    cocktail = get_object_or_404(Cocktail, pk=product_id)

    context = {
        'cocktail': cocktail,
    }

    return render(request, 'cocktails/cocktail_detail.html', context)
