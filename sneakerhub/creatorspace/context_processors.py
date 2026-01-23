from .models import Brand

def isBrandOwner(request):
    user = request.user
    isBrand = False

    if user.is_authenticated:
        brandCheck = Brand.objects.filter(owner=user).exists()
        if brandCheck:
            isBrand = True

    return {
        'isBrand': isBrand
    }