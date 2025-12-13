from django.shortcuts import render

# Create your views here.
def accountPageView(request, user_id):
    return render(request, 'profile.html', { 'user_id': user_id })