"""
URL configuration for sneakerhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import homePage, customerSignupView, customerLogoutView, customerLoginView
from marketplace.views import marketplaceView, sneakerDetailView
from account.views import accountPageView, addToWishlistView, removeFromWishlistView
from listings.views import createListingView, deleteListingView, editListingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage.as_view(), name='home'),
    path('marketplace/', marketplaceView, name='marketplace'),
    path('sneaker/<int:sneaker_id>/', sneakerDetailView, name='sneaker_detail'),
    path('customer_signup/', customerSignupView, name='signup'),
    path('customer_logout/', customerLogoutView, name='logout'),
    path('customer_login/', customerLoginView, name='login'),
    path('account/<int:user_id>/', accountPageView, name='account'),
    path('account/wishlist/add/<int:sneaker_id>/', addToWishlistView, name='wishlist_add'),
    path('account/wishlist/remove/<int:sneaker_id>/', removeFromWishlistView, name='wishlist_remove'),
    path('listings/create/', createListingView, name='create_listing'),
    path('listings/delete/<int:sneaker_id>/', deleteListingView, name='delete_listing'),
    path('listings/edit/<int:sneaker_id>/', editListingView, name='edit_listing'),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('publicprofile.urls')),
    path('errorhandler/', include('errorhandler.urls')),
    path('reviews/', include('reviews.urls')),
    path('creatorspace/', include('creatorspace.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
