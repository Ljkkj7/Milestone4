from django.shortcuts import render
from .models import Sneaker


# Create your views here.
def marketplaceView(request):
    # All sneakers (most recent first)
    brand_filter = request.GET.get('brand')
    if brand_filter:
        sneakers = Sneaker.objects.filter(brand=brand_filter).order_by('-created_at')
    else:
        sneakers = Sneaker.objects.all().order_by('-created_at')
    selected_brand = brand_filter or ''

    # Distinct brand names from current sneakers
    brands_qs = Sneaker.objects.values_list('brand', flat=True).distinct()
    # Convert to a sorted list for predictable template ordering
    brands = sorted([b for b in brands_qs if b])

    context = {
        'sneakers': sneakers,
        'brands': brands,
        'selected_brand': selected_brand,
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

def sneakerDetailView(request, sneaker_id):
    # Detail view for a single sneaker
    sneaker = Sneaker.objects.get(id=sneaker_id)
    context = {
        'sneaker': sneaker,
    }
    return render(request, 'sneaker_detail.html', context)