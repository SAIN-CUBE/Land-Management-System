from django.shortcuts import render, redirect
from .forms import LandOwnershipDataForm, OwnerForm, LandForm, TransactionForm
from folium import Map, Marker, FeatureGroup, LayerControl
from .models import MyStreetlightModel, MyLandLocationModel

def home(request):
    if request.method == 'POST':
        # Assuming you have a button in the home page to initiate the redirection
        return redirect('land_management_data')
    else:
        return render(request, 'home.html', {'land_management_data_url': 'land_management_data'})

def land_management_data(request):
    m = Map(location=[40.7128, -74.0060], zoom_start=12)  # Initialize map outside the if-else block

    if request.method == 'POST':
        land_ownership_form = LandOwnershipDataForm(request.POST)
        owner_form = OwnerForm(request.POST)
        land_form = LandForm(request.POST)
        transaction_form = TransactionForm(request.POST)

        if land_ownership_form.is_valid() and owner_form.is_valid() and land_form.is_valid() and transaction_form.is_valid():
            land_ownership_data = land_ownership_form.save(commit=False)
            land_ownership_data.save()

            owner = owner_form.save()
            land = land_form.save()
            transaction = transaction_form.save()

            land_ownership_data.owners.add(owner)
            land_ownership_data.land = land
            land_ownership_data.transactions.add(transaction)

            land_ownership_data.save()

            # Redirect to the success page upon successful form submission
            return redirect('success')

    else:
        land_ownership_form = LandOwnershipDataForm()
        owner_form = OwnerForm()
        land_form = LandForm()
        transaction_form = TransactionForm()

    return render(request, 'land_management_data.html', {
        'land_ownership_form': land_ownership_form,
        'owner_form': owner_form,
        'land_form': land_form,
        'transaction_form': transaction_form,
        'map': m._repr_html_() if m else None,
    })

def success(request):
    # Render the success page
    return render(request, 'success.html')