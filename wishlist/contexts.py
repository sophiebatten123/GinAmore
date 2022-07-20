

def wishlist_items(request):

    wishlist = request.session.get('wishlist', {})

    context = {
        'wishlist': wishlist,
    }

    return context
