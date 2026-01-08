from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkoutView, name='checkout'),
]