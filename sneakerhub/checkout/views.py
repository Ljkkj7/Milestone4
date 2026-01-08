from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from marketplace.models import Sneaker
from .forms import CheckoutForm
from cart.views import _get_cart

# Create your views here.
@login_required
def checkoutView(request):
    cart = _get_cart(request.session)
    items = []
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process the checkout
            pass
    else:
        for sneaker_id_str, data in cart.items():
            try:
                sneaker_id = int(sneaker_id_str)
            except ValueError:
                continue
            sneaker = get_object_or_404(Sneaker, id=sneaker_id)
            quantity = data.get('quantity', 0)
            line_total = float(sneaker.price) * int(quantity)
            items.append({
                'sneaker': sneaker,
                'quantity': int(quantity),
                'line_total': line_total,
            })
        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {'form': form, 'items': items})