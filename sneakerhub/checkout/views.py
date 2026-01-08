from django.shortcuts import redirect, render
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
    total = 0.0

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            return render(request, 'checkout/payment.html', {'form': form})
    else:

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

        # Calculate shipping as 10% of subtotal (example policy)
        shipping = 5.0 if total > 0 else 0
        grand_total = round(total + shipping, 2)

        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {'form': form, 'items': items, 'total': total, 'shipping': shipping, 'grand_total': grand_total})