from django.shortcuts import redirect, render
from .forms import BrandForm
from .models import Brand

# Create your views here.
def creatorSpaceView(request):
    user = request.user

    brands = Brand.objects.all()
    isBrand = False

    if user.id in brands.values_list('owner_id', flat=True):
        isBrand = True

    context = {
        'brands': brands,
        'isBrand': isBrand,
    }

    return render(request, 'creatorspace/creatorspace.html', context)

def brandCreateView(request):
    if request.method == 'POST':

        form = BrandForm(request.POST, request.FILES)

        if form.is_valid():
            brand_name = request.POST.get('brand_name')
            brand_description = request.POST.get('brand_description')
            owner = request.user

            # Create and save the brand
            brand = Brand(
                name=brand_name,
                description=brand_description,
                owner=owner
            )

            brand.save()
            return redirect('creatorspace:creatorspace')
        
    else:
        form = BrandForm()

    return render(request, 'creatorspace/brandcreate.html', {'form': form})