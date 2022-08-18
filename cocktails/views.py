'''
Imports relevant django packages
'''
from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Cocktail
from .forms import CocktailForm
from django.contrib import messages


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


def add_cocktail(request):
    '''
    Add a cocktail to the site
    '''
    if request.method == 'POST':
        form = CocktailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a cocktail!')
            return redirect(reverse('add_cocktail'))
        else:
            messages.error(request, 'Failed to add the cocktail. Ensure the form is valid')
    else:
        form = CocktailForm()

    template = 'cocktails/add_cocktail.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_cocktail(request, product_id):
    '''
    Edit a cocktail from the store
    '''
    cocktail = get_object_or_404(Cocktail, pk=product_id)
    if request.method == 'POST':
        form = CocktailForm(request.POST, request.FILES, instance=cocktail)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the cocktail!')
            return redirect(reverse('cocktail_detail', args=[cocktail.id]))
        else:
            messages.error(request, 'Failed to edit the cocktail. Ensure the form is valid')
    else:
        form = CocktailForm(instance=cocktail)
        messages.info(request, f'You are editing {cocktail.name}')

    template = 'cocktails/edit_cocktail.html'
    context = {
        'form': form,
        'cocktail': cocktail,
    }

    return render(request, template, context)
