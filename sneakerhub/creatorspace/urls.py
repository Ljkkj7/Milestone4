from django.urls import path
from . import views

app_name = 'creatorspace'

urlpatterns = [
    path('', views.creatorSpaceView, name='creatorspace'),
]