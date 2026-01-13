from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from marketplace.models import Sneaker
from .forms import CheckoutForm
from .models import Order, OrderItem
from cart.views import _get_cart
import stripe
from django.conf import settings

# Create your views here.
@login_required
def checkoutView(request):
    cart = _get_cart(request.session)
    items = []
    total = 0.0

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            delistSoldSneakers(request)

            for item_id, data in cart.items():
                try:
                    sneaker = Sneaker.objects.get(id=int(item_id))
                    if sneaker is not None:
                        order_line_item = OrderItem(
                            order=order,
                            sneaker=sneaker,
                            line_total=sneaker.price
                        )
                        order_line_item.save()
                except Sneaker.DoesNotExist:
                    messages.error(request, ( "Sneaker in your cart wasn't found in our database. "
                                             "Please contact support for assistance."))
                    order.delete()
                    return redirect('cart:detail')
            
            request.session['cart'] = {}
            request.session.modified = True
            return redirect('cart:detail')
            
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
            return redirect('checkout')
        
    else:

        if not cart:
            messages.error(request, "Your cart is empty")
            return redirect('marketplace')
        
        for sneaker_id_str, data in cart.items():
            try:
                sneaker_id = int(sneaker_id_str)
            except ValueError:
                continue
            sneaker = get_object_or_404(Sneaker, id=sneaker_id)
            quantity = data.get('quantity', 0)
            line_total = float(sneaker.price) * int(quantity)
            total += line_total
            shipping = 5.0 if total > 0 else 0
            grand_total = round(total + shipping, 2)
            items.append({
                'sneaker': sneaker,
                'quantity': int(quantity),
                'line_total': line_total,
            })

        intent = stripe.PaymentIntent.create(
            amount=int(grand_total * 100),  # amount in pence
            currency='gbp',
        )

        form = CheckoutForm()
        context = {
            'form': form,
            'items': items,
            'total': total,
            'shipping': shipping,
            'grand_total': grand_total,
            'stripe_public_key': stripe_public_key,
            'stripe_client_secret': intent.client_secret,
        }
    return render(request, 'checkout/checkout.html', context)

def delistSoldSneakers(request):
    cart = _get_cart(request.session)
    for sneaker_id_str in cart.keys():
        sneaker_id = int(sneaker_id_str)
        sneaker = get_object_or_404(Sneaker, id=sneaker_id)
        sneaker.is_sold = True
        sneaker.save()