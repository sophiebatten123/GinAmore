'''
Imports relevant django packages
'''
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product


# Create your views here.

def view_wishlist(request):
    '''
    A view to return the wishlist
    '''
    return render(request, 'wishlist/wishlist.html')


@login_required
def add_to_wishlist(request, item_id):
    '''
    Add an item to the wishlist
    '''
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if request.POST:
        if product.likes.filter(id=request.user.id).exists():
            product.likes.remove(request.user)
            messages.success(
                request, f'{product.name} has been removed from your wishlist'
            )
        else:
            product.likes.add(request.user)
            messages.success(
                request, f'{product.name} to your wishlist'
                )
            wishlist[item_id] = product.name

        request.session['wishlist'] = wishlist

        return redirect(redirect_url)
