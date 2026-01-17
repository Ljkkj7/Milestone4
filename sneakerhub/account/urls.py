from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('wishlist/add/<int:sneaker_id>/', views.addToWishlistView, name='wishlist_add'),
    path('wishlist/remove/<int:sneaker_id>/', views.removeFromWishlistView, name='wishlist_remove'),
]