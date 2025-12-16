from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ListingCreationForm

@login_required
def createListingView(request):
    """Handle creation of a new sneaker listing using a ModelForm."""
    if request.method == 'POST':
        form = ListingCreationForm(request.POST, request.FILES)
        if form.is_valid():
            sneaker = form.save(commit=False)
            sneaker.owner = request.user
            sneaker.save()
            return render(request, 'profile.html', {'user_id': request.user.id})
    else:
        form = ListingCreationForm()

    return render(request, 'create_listing.html', {'form': form})
