from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from marketplace.models import Sneaker
from checkout.models import Order
from .models import WishlistItem

# Create your views here.
def accountPageView(request, user_id):
    user = request.user
    sneaker = Sneaker.objects.all()

    available_sneakers = user.sneakers.filter(owner=user, is_sold=False)

    wishlist_items = WishlistItem.objects.filter(user=user)
    wishlist_sneakers = [item.sneaker_id for item in wishlist_items]

    user_orders = Order.objects.filter(user=user).order_by('date')

    for sneakers in sneaker:
        if sneakers.id in wishlist_sneakers:
            wishlist_sneakers[wishlist_sneakers.index(sneakers.id)] = sneakers

    return render(request, 'profile.html', { 
        'user_id': user_id,
        'available_sneakers': available_sneakers,
        'wishlist_sneakers': wishlist_sneakers,
        'user_orders': user_orders,
        })

@login_required
def addToWishlistView(request, sneaker_id):
    user = request.user
    sneaker = get_object_or_404(Sneaker, id=sneaker_id)

    if not WishlistItem.objects.filter(user=user, sneaker=sneaker).exists():
        wishlist_item = WishlistItem(user=user, sneaker=sneaker)
        wishlist_item.save()
    else:
        return redirect(reverse('sneaker_detail', kwargs={'sneaker_id': sneaker.id, }) + '?error=already_in_wishlist')

    return(redirect('sneaker_detail', sneaker_id=sneaker.id))

@login_required
def removeFromWishlistView(request, sneaker_id):
    user = request.user
    sneaker = get_object_or_404(Sneaker, id=sneaker_id)

    wishlist_item = WishlistItem.objects.filter(user=user, sneaker=sneaker)
    if wishlist_item.exists():
        wishlist_item.delete()
    else:
        return redirect(reverse('sneaker_detail', kwargs={'sneaker_id': sneaker.id, }) + '?error=not_in_wishlist')

    return redirect('sneaker_detail', sneaker_id=sneaker.id)