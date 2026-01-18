from django.urls import path
from . import views

app_name = 'errorhandler'

urlpatterns = [
    path('403/', views.permissionDeniedView, name='permission_denied'),
    path('login-required/', views.notAuthenticatedView, name='not_authenticated'),
]