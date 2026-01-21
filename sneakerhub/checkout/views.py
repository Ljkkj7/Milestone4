from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
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
                        order.update_total()

                except Sneaker.DoesNotExist:
                    messages.error(request, ( "Sneaker in your cart wasn't found in our database. "
                                             "Please contact support for assistance."))
                    order.delete()
                    return redirect('cart:detail')
            
            request.session['cart'] = {}
            request.session.modified = True

            delistSoldSneakers(request)
            send_order_confirmation_email(order, cart)
            
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

            shipping = 5.0 if total < 100 else 0
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

# Send order confirmation email
def send_order_confirmation_email(order, cart):

        subject = f"Order Confirmation - Order #{order.order_number}"
        # Plain text fallback
        message = f"Dear {order.user.username},\n\n"
        message += "Thank you for your purchase! Here are your order details:\n\n"
        for item_id, data in cart.items():
                sneaker = Sneaker.objects.get(id=int(item_id))
                message += f"- {sneaker.name}: £{sneaker.price}\n"
        message += f"\nTotal Amount: £{order.grand_total}\n\n"
        message += "We hope you enjoy your new sneakers!\n\nBest regards,\nSneakerHub Team"

        # HTML email body styled inline to match SneakerHub branding
        html_message = f"""
        <div style='font-family: Arial, sans-serif; background: #fff; color: #1a1a1a; max-width: 600px; margin: 0 auto; border: 1px solid #eee; border-radius: 8px; box-shadow: 0 2px 8px #f0f0f0;'>
            <div style='background: #fff; border-bottom: 2px solid #000; padding: 24px 32px 12px 32px; text-align: center;'>
                <h1 style='margin: 0; font-size: 28px; font-weight: 900; letter-spacing: -1px; color: #000; text-transform: uppercase;'>SneakerHub</h1>
            </div>
            <div style='padding: 32px;'>
                <h2 style='font-size: 22px; color: #000; margin-top: 0;'>Order Confirmation</h2>
                <p style='font-size: 16px; color: #1a1a1a;'>Hi <b>{order.user.username}</b>,</p>
                <p style='font-size: 16px;'>Thank you for your purchase! Here are your order details:</p>
                <table style='width: 100%; border-collapse: collapse; margin: 24px 0;'>
                    <thead>
                        <tr style='background: #f8f8f8;'>
                            <th style='text-align: left; padding: 8px; border-bottom: 1px solid #ddd;'>Sneaker</th>
                            <th style='text-align: right; padding: 8px; border-bottom: 1px solid #ddd;'>Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        {''.join([f"<tr><td style='padding: 8px; border-bottom: 1px solid #f0f0f0;'>{Sneaker.objects.get(id=int(item_id)).name}</td><td style='padding: 8px; text-align: right; border-bottom: 1px solid #f0f0f0;'>£{Sneaker.objects.get(id=int(item_id)).price}</td></tr>" for item_id, data in cart.items()])}
                    </tbody>
                </table>
                <p style='font-size: 16px;'><b>Total Amount:</b> £{order.grand_total}</p>
                <p style='font-size: 16px;'>We hope you enjoy your new sneakers!</p>
                <p style='font-size: 15px; color: #888; margin-top: 32px; text-align: center;'>Best Regards,<br>SneakerHub Team</p>
            </div>
        </div>
        """

        send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [order.email],
                fail_silently=False,
                html_message=html_message,
        )

#@login_required
#def checkoutSuccessView(request):
    #return render(request, 'checkout/checkout_success.html')