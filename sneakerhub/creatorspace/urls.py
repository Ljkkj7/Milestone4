from django.urls import path
from . import views

app_name = 'creatorspace'

urlpatterns = [
    path('', views.creatorSpaceView, name='creatorspace'),
    path('create/', views.brandCreateView, name='brand_create'),
    path('dashboard/', views.brandDashboardView, name='brand_dashboard'),
    path('brand/<int:brand_id>/', views.brandDetailView, name='brand_detail'),
    path('brand/manage/<int:brand_id>/', views.manageBrandView, name='manage_brand'),
]