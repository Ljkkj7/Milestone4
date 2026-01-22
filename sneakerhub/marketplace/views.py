from django.shortcuts import redirect, render
from .models import Sneaker
from account.models import WishlistItem


# Create your views here.
def marketplaceView(request):
    # All sneakers (most recent first)
    brand_filter = request.GET.get('brand')
    size_filter = request.GET.get('size')
    price_range = request.GET.get('price_range')
    sort_by = request.GET.get('sort_by')
    
    # Start with all sneakers
    sneakers = Sneaker.objects.filter(is_sold=False)
    
    # Apply filters independently (can be combined)
    if brand_filter:
        sneakers = sneakers.filter(brand=brand_filter)
    if size_filter:
        sneakers = sneakers.filter(size=size_filter)
    if price_range:
        if price_range == '0-50':
            sneakers = sneakers.filter(price__gte=0, price__lte=50)
        elif price_range == '51-100':
            sneakers = sneakers.filter(price__gte=51, price__lte=100)
        elif price_range == '101-150':
            sneakers = sneakers.filter(price__gte=101, price__lte=150)
        elif price_range == '151+':
            sneakers = sneakers.filter(price__gte=151)
    
    # Apply sorting
    if sort_by == 'price-low-high':
        sneakers = sneakers.order_by('price')
    elif sort_by == 'price-high-low':
        sneakers = sneakers.order_by('-price')
    else:  # Default to newest arrivals
        sneakers = sneakers.order_by('-created_at')

    selected_brand = brand_filter or ''
    selected_size = size_filter or ''
    selected_price_range = price_range or ''
    selected_sort_by = sort_by or ''

    # Distinct brand names from current sneakers
    brands_qs = Sneaker.objects.values_list('brand', flat=True).distinct()
    brands_qs = brands_qs.filter(is_sold=False)

    # Distinct sizes from current sneakers
    size_qs = Sneaker.objects.values_list('size', flat=True).distinct()
    size_qs = size_qs.filter(is_sold=False)

    # Convert to a sorted list for predictable template ordering
    brands = sorted([b for b in brands_qs if b])
    sizes = sorted([s for s in size_qs if s])

    context = {
        'sneakers': sneakers,
        'brands': brands,
        'selected_brand': selected_brand,
        'sizes': sizes,
        'selected_size': selected_size,
        'selected_price_range': selected_price_range,
        'selected_sort_by': selected_sort_by,
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