from checkout.forms import OrderForm
from checkout.models import Order
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    print(cart)

    if not cart:
        messages.error(request, "There's nothing in your cart!")
        return redirect(reverse('treatments'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
