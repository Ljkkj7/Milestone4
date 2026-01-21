from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('add/<int:profile_user>/', views.addReviewView, name='add_review'),
    path('submit/<int:profile_user>/', views.submitReviewView, name='submit_review'),
    path('edit/<int:review_id>/', views.editReviewView, name='edit_review'),
]