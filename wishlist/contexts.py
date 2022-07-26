'''
Imports relevant django packages
'''
from django.shortcuts import get_object_or_404
from products.models import Product


def wishlist_items(request):
    '''
    Wishlist information to be accessible accross the site
    '''
    wishlist_products = []
    wishlist = request.session.get('wishlist', {})

    for item_id in wishlist.keys():
        product = get_object_or_404(Product, pk=item_id)
        wishlist_products.append({
            'item_id': item_id,
            'product': product,
        })

    context = {
        'wishlist_products': wishlist_products,
    }

    return context
