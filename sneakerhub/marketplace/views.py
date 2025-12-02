from django.shortcuts import render

# Create your views here.
def marketplaceView(request):
    return render(request, 'marketplace.html')