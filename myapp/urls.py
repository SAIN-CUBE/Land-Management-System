# myapp/urls.py
from django.urls import path
from .views import home, land_management_data, success

urlpatterns = [
    path('', home, name='home'),  # Set the default home page
    path('land_management_data/', land_management_data, name='land_management_data'),
    path('success/', success, name='success'),
]