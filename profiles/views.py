'''
Imports relevant packages
'''
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    '''
    Displays the users profile information
    '''
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated')
    orders = profile.orders.all()
    form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    '''
    Displays the users order history information
    '''
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a previous confirmation order number: {order_number}.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
