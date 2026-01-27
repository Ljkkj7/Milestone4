from django.shortcuts import redirect, render
from .forms import BrandForm, BrandProductsForm
from .models import Brand, BrandProducts
from core.views import authCheck
from django.contrib.auth.models import User

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
            
            brand = form.save(commit=False)
            brand.owner = request.user

            brand.save()
            return redirect('creatorspace:creatorspace')
        
    else:
        if not authCheck(request):
            return redirect('errorhandler:not_authenticated')

        form = BrandForm()

    return render(request, 'creatorspace/brandcreate.html', {'form': form})

def brandDashboardView(request):
    user = request.user

    getBrands = Brand.objects.filter(owner=user)

    context = {
        'brands': getBrands,
    }

    return render(request, 'creatorspace/creatordashboard.html', context)

def brandDetailView(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    brand_products = BrandProducts.objects.filter(brand_id=brand_id)
    brand_owner = User.objects.get(id=brand.owner_id)

    context = {
        'brand': brand,
        'brand_products': brand_products,
        'brand_owner': brand_owner,
    }

    return render(request, 'creatorspace/branddetail.html', context)


def manageBrandView(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    brand_products = BrandProducts.objects.filter(brand_id=brand_id)

    context = {
        'brand': brand,
        'brand_products': brand_products,
    }

    return render(request, 'creatorspace/managebrand.html', context)

def createBrandProductView(request, brand_id):

    if request.method == 'POST':

        form = BrandProductsForm(request.POST, request.FILES)

        if form.is_valid():
            
            brand_product = form.save(commit=False)
            brand_product.brand_id = brand_id

            brand_product.save()
            return redirect('creatorspace:manage_brand', brand_id=brand_id)
        
    else:

        if not authCheck(request):
            return redirect('errorhandler:not_authenticated')

        form = BrandProductsForm()

    return render(request, 'creatorspace/createbrandlisting.html', {'form': form, 'brand_id': brand_id})


def manageCollaboratorsView(request):
    
    if not authCheck(request):
        return redirect('errorhandler:not_authenticated')

    # Future implementation for managing collaborators will go here

    return render(request, 'creatorspace/managecollaborators.html')