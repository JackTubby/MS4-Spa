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
        'stripe_public_key': 'pk_test_51IkBOBDHm5srVMAI2eWcbeijpUBYFFjnsgi1ywxDY6ZJpg3hm6QSoH6JXYGS6BGOKWQ3zXOxhSQEWARRFl85yCUV00EqC0Xs2I',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
