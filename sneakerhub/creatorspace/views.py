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
            
            brand = form.save(commit=False)
            brand.owner = request.user

            brand.save()
            return redirect('creatorspace:creatorspace')
        
    else:

        user = request.user

        if not user.is_authenticated:
            return redirect('errorhandler:login_required')

        form = BrandForm()

    return render(request, 'creatorspace/brandcreate.html', {'form': form})