from checkout.forms import OrderForm
from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    print(cart)

    if not cart:
        messages.error(request, "There's nothing in your cart!")
        return redirect(reverse('treatments'))

    current = cart_contents(request)
    total = current['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
             Did you forget to set it in your environment?')
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
