from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from marketplace.models import Sneaker
from .models import WishlistItem

# Create your views here.
def accountPageView(request, user_id):
    user = request.user
    sneaker = Sneaker.objects.all()

    available_sneakers = user.sneakers.filter(is_sold=False)

    wishlist_items = WishlistItem.objects.filter(user=user)
    wishlist_sneakers = [item.sneaker_id for item in wishlist_items]

    for sneakers in sneaker:
        if sneakers.id in wishlist_sneakers:
            wishlist_sneakers[wishlist_sneakers.index(sneakers.id)] = sneakers

    return render(request, 'profile.html', { 
        'user_id': user_id,
        'available_sneakers': available_sneakers,
        'wishlist_sneakers': wishlist_sneakers,
        })

@login_required
def addToWishlistView(request, sneaker_id):
    user = request.user
    sneaker = get_object_or_404(Sneaker, id=sneaker_id)

    if not WishlistItem.objects.filter(user=user, sneaker=sneaker).exists():
        wishlist_item = WishlistItem(user=user, sneaker=sneaker)
        wishlist_item.save()

    return(redirect('sneaker_detail', sneaker_id=sneaker.id))