# myapp/urls.py
from django.urls import path
from .views import home, land_management_data, success
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', home, name='home'),  # Set the default home page
    path('land_management_data/', views.land_management_data, name='land_management_data'),
    path('success/', success, name='success'),
]