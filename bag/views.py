'''
Imports relevant django packages
'''
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    '''
    A view to return the bag page
    '''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    '''
    Add the quantity of a product to the shopping bag
    '''
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}'
        )
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag!')

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    '''
    Adjust the quantity of items in the shopping bag
    '''
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}'
        )
    else:
        bag.pop(item_id)
        messages.success(
            request, f'{product.name} removed from your shopping bag'
        )

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    '''
    Adjust the quantity of items in the shopping bag
    '''
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    bag.pop(item_id)
    messages.success(request, f'{product.name} removed from your shopping bag')

    request.session['bag'] = bag

    return HttpResponse(status=200)
