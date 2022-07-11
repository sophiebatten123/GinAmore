from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from bag.contexts import bag_content
from .forms import OrderForm

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag!")
        return redirect(reverse('products'))

    current_bag = bag_content(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LKKZAK5ywolBQ5H4kbt5Fi3E2UgaRNZqOeBOynumdGCWSUBpy346fuey8V1HoDWnInf0tRzhNORdqgL21tGJVjL007qEGEutu',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
