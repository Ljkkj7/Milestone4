from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def publicProfileView(request, profile_user):
    user = User.objects.get(id=profile_user)
    sneakers = user.sneakers.filter(is_sold=False)
    
    return render(request, 'public_profile.html', {'profile_user': user, 'sneakers': sneakers})