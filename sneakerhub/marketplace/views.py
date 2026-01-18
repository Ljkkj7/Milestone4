from django.shortcuts import redirect, render
from .models import Sneaker
from account.models import WishlistItem


# Create your views here.
def marketplaceView(request):
    # All sneakers (most recent first)
    brand_filter = request.GET.get('brand')
    size_filter = request.GET.get('size')
    
    # Start with all sneakers
    sneakers = Sneaker.objects.filter(is_sold=False)
    
    # Apply filters independently (can be combined)
    if brand_filter:
        sneakers = sneakers.filter(brand=brand_filter)
    if size_filter:
        sneakers = sneakers.filter(size=size_filter)
    
    sneakers = sneakers.order_by('-created_at')
    selected_brand = brand_filter or ''
    selected_size = size_filter or ''

    # Distinct brand names from current sneakers
    brands_qs = Sneaker.objects.values_list('brand', flat=True).distinct()
    size_qs = Sneaker.objects.values_list('size', flat=True).distinct()

    # Convert to a sorted list for predictable template ordering
    brands = sorted([b for b in brands_qs if b])
    sizes = sorted([s for s in size_qs if s])

    context = {
        'sneakers': sneakers,
        'brands': brands,
        'selected_brand': selected_brand,
        'sizes': sizes,
        'selected_size': selected_size,
    }
    return render(request, 'marketplace.html', context)


def brandReturn(request, brand_name):
    # Return sneakers filtered by a brand name string
    sneakers = Sneaker.objects.filter(brand=brand_name).order_by('-created_at')
    brands_qs = Sneaker.objects.values_list('brand', flat=True).distinct()
    brands = sorted([b for b in brands_qs if b])
    context = {
        'sneakers': sneakers,
        'brands': brands,
        'brand_name': brand_name,
    }
    return render(request, 'marketplace.html', context)

def sizeReturn(request, size_value):
    # Return sneakers filtered by a size value
    sneakers = Sneaker.objects.filter(size=size_value).order_by('-created_at')
    size_q = Sneaker.objects.values_list('size', flat=True).distinct()
    sizes = sorted([s for s in size_q if s])
    context = {
        'sneakers': sneakers,
        'sizes': sizes,
        'size_value': size_value,
    }
    return render(request, 'marketplace.html', context)

def sneakerDetailView(request, sneaker_id):
    # Detail view for a single sneaker
    user = request.user

    if not user.is_authenticated:
        return redirect('errorhandler:not_authenticated')

    sneaker = Sneaker.objects.get(id=sneaker_id)
    in_wishlist = WishlistItem.objects.filter(user=user, sneaker=sneaker).exists()

    context = {
        'sneaker': sneaker,
        'in_wishlist': in_wishlist,
    }
    return render(request, 'sneaker_detail.html', context)