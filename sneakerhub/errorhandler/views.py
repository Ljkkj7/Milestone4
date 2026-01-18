from django.shortcuts import render

# Create your views here.
def permissionDeniedView(request):
    return render(request, 'errorhandler/403.html')

def notAuthenticatedView(request):
    return render(request, 'errorhandler/login_required.html')