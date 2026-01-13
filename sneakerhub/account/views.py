from django.shortcuts import render

# Create your views here.
def accountPageView(request, user_id):
    user = request.user

    available_sneakers = user.sneakers.filter(is_sold=False)

    return render(request, 'profile.html', { 
        'user_id': user_id,
        'available_sneakers': available_sneakers,
        })