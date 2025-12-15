from django.shortcuts import render

# Create your views here.
def listingsPageView(request):
    return render(request, 'create_listing.html')