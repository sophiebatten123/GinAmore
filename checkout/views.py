from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
<<<<<<< HEAD
    bag = request.session.get('bag', {})
=======
    bag = bag.session.get('bag', {})
>>>>>>> 3777e4c3ce0e13cf5b208a82683cbbe6e138df14
    if not bag:
        messages.error(request, "There is nothing in your bag!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
