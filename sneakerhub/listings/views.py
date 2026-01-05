from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import ListingCreationForm
from marketplace.models import Sneaker

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

@login_required
def deleteListingView(request, sneaker_id):
    """Handle deletion of a sneaker listing."""
    sneaker = get_object_or_404(Sneaker, id=sneaker_id, owner=request.user)
    
    if request.method == 'POST':
        sneaker.delete()
        return redirect('account', user_id=request.user.id)
    
    # GET request - show confirmation page or redirect back
    return redirect('account', user_id=request.user.id)

@login_required
def editListingView(request, sneaker_id):
    """Handle editing of a sneaker listing."""
    sneaker = get_object_or_404(Sneaker, id=sneaker_id, owner=request.user)
    
    if request.method == 'POST':
        form = ListingCreationForm(request.POST, request.FILES, instance=sneaker)
        if form.is_valid():
            form.save()
            return redirect('sneaker_detail', sneaker_id=sneaker.id)
    else:
        form = ListingCreationForm(instance=sneaker)
    return render(request, 'edit_listing.html', {'form': form, 'sneaker': sneaker})