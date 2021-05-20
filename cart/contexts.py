from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from treatments.models import Treatment


def cart_contents(request):
    cart_items = []
    total = 0
    treatment_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        treatment = get_object_or_404(Treatment, pk=item_id)
        total += quantity * treatment.price
        treatment_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'treatment': treatment,
        })

    grand_total = total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'treatment_count': treatment_count,
        'grand_total': grand_total,
    }

    return context