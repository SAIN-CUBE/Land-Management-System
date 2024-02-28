from django.shortcuts import render, redirect
from .forms import  LandForm
from folium import Map


def home(request):
    if request.method == 'POST':
        # Assuming you have a button in the home page to initiate the redirection
        return redirect('land_management_data')
    else:
        return render(request, 'home.html', {'land_management_data_url': 'land_management_data'})

def land_management_data(request):
    m = Map(location=[40.7128, -74.0060], zoom_start=12)  # Initialize map outside the if-else block

    if request.method == 'POST':
        land_form = LandForm(request.POST)
        if land_form.is_valid():
            land_form.save()
            # Redirect to the success page upon successful form submission
            return redirect('success')

    else:
        land_form = LandForm()

    return render(request, 'land_management_data.html', {
        'land_form': land_form,
        'map': m._repr_html_() if m else None,
    })

def success(request):
    # Render the success page
    return render(request, 'success.html')