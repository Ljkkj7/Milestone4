from django.shortcuts import render
from .models import Sneaker

# Create your views here.
def marketplaceView(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'marketplace.html', {'sneakers': sneakers})