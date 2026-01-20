from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('add/<int:profile_user>/', views.addReviewView, name='add_review'),
]