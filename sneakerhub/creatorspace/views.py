from django.shortcuts import render
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