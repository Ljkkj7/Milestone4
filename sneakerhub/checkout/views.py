from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm

# Create your views here.
@login_required
def checkoutView(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process the checkout
            pass
    else:
        form = CheckoutForm()
    
    return render(request, 'checkout/checkout.html', {'form': form})