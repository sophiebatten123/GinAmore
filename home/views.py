'''
Imports relevant django packages
'''
from django.shortcuts import render
from products.models import Product


def index(request):
    '''
    A view to return the index page
    '''
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)


def contact(request):
    '''
    A view to return the contact page
    '''
    return render(request, 'home/contact.html')
