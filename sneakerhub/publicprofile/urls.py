from django.urls import path
from . import views

app_name = 'publicprofile'

urlpatterns = [
    path('<int:profile_user>/', views.publicProfileView, name='public_profile'),
]