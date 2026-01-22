from django.shortcuts import render

# Create your views here.
def creatorSpaceView(request):
    return render(request, 'creatorspace/creatorspace.html')