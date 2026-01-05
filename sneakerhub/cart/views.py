from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from marketplace.models import Sneaker


def _get_cart(session):
    return session.setdefault('cart', {})


def cart_detail(request):
    cart = _get_cart(request.session)
    items = []
    total = 0

    for sneaker_id_str, data in cart.items():
        try:
            sneaker_id = int(sneaker_id_str)
        except ValueError:
            continue
        sneaker = get_object_or_404(Sneaker, id=sneaker_id)
        quantity = data.get('quantity', 0)
        line_total = float(sneaker.price) * int(quantity)
        total += line_total
        items.append({
            'sneaker': sneaker,
            'quantity': int(quantity),
            'line_total': line_total,
        })

    return render(request, 'cart/cart.html', {'items': items, 'total': total})


@require_POST
def add_to_cart(request, sneaker_id):
    sneaker = get_object_or_404(Sneaker, id=sneaker_id)
    quantity = int(request.POST.get('quantity', 1))
    cart = _get_cart(request.session)
    key = str(sneaker.id)
    if key in cart:
        cart[key]['quantity'] = int(cart[key].get('quantity', 0)) + quantity
    else:
        cart[key] = {'quantity': quantity}
    request.session.modified = True
    return redirect(reverse('cart:detail'))
