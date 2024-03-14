from django.shortcuts import render, redirect
from folium import Map, Marker, FeatureGroup, LayerControl
from myapp.forms import ConfirmAboveForm, ConfirmDecisionForm, ConfirmTransferForm, OwnerForm
from .models import MyStreetlightModel, MyLandLocationModel, Owner
from django.http import JsonResponse
from django.urls import reverse


def home(request):
    if request.method == 'POST':
        # Assuming you have a button in the home page to initiate the redirection
        return redirect('land_management_data')
    else:
        return render(request, 'home.html', {'land_management_data_url': 'land_management_data'})

def land_management_data(request):
    m = Map(location=[40.7128, -74.0060], zoom_start=12)  # Initialize map outside the if-else block

    owners = [
        {'name': '', 'id': '', 'percentage': ''}
    ]

    # Track the status of each form submission
    confirm_decision_success = False
    confirm_above_success = False
    confirm_transfer_success = False

    # Initialize dynamic owner form
    owner_form = OwnerForm()



    if request.method == 'POST':
            if 'confirm_decision' in request.POST:
                # Process data for confirm decision button
                form = ConfirmDecisionForm(request.POST)
                if form.is_valid():
                    registration_authority_court = request.POST.get('registration_authority_court')
                    registration_authority_date = request.POST.get('registration_authority_date')
                    registration_authority_decision = request.POST.get('registration_authority_decision')
                    # Process and save the data for confirm decision

                    confirm_decision_success = True

                    print(registration_authority_court)
                    print(registration_authority_date)
                    print(registration_authority_decision)
                    print(confirm_decision_success)
                    print( JsonResponse({'message': 'Data saved for confirm decision'}))
            
            elif 'owners' in request.POST:
                # Handle owner confirmation form submission
                owner_names = request.POST.getlist('owner_name[]')
                owner_ids = request.POST.getlist('owner_id[]')
                owner_percentages = request.POST.getlist('owner_percentage[]')
                
                # Process owner data as needed
                for i, (name, id, percentage) in enumerate(zip(owner_names, owner_ids, owner_percentages), start=1):
                    print(f"Owner {i}:")
                    print(f"Owner Name: {name}")
                    print(f"Owner ID: {id}")
                    print(f"Owner Percentage: {percentage}")
                    print()  # Print an empty line for separation
                
                # Return a JSON response after processing owner data
                return JsonResponse({'message': 'Owner data processed successfully'})


            elif 'confirm_above' in request.POST:
                form = ConfirmAboveForm(request.POST)
                if form.is_valid():
                    # Process data for confirm above button
                    name = request.POST.get('name')
                    id_number = request.POST.get('id_number')
                    ownership_percentage = request.POST.get('ownership_percentage')
                    unique_id = request.POST.get('unique_id')
                    area_deed = request.POST.get('area_deed')
                    area_survey = request.POST.get('area_survey')
                    coordinate = request.POST.get('coordinate')
                    city = request.POST.get('city')
                    hay = request.POST.get('hay')
                    subdivision_number = request.POST.get('subdivision_number')
                    neighborhood = request.POST.get('neighborhood')
    
                    confirm_above_success = True
    
                    print("Name:", name)
                    print("ID Number:", id_number)
                    print("Ownership Percentage:", ownership_percentage)
                    print("Unique ID:", unique_id)
                    print("Area Deed:", area_deed)
                    print("Area Survey:", area_survey)
                    print("Coordinate:", coordinate)
                    print("City:", city)
                    print("Hay:", hay)
                    print("Subdivision Number:", subdivision_number)
                    print("Neighborhood:", neighborhood)
    
                    print(confirm_above_success)
    
                    print(JsonResponse({'message': 'Data saved for confirm above'}))


            elif 'confirm_transfer' in request.POST:
                form = ConfirmTransferForm(request.POST)
                if form.is_valid():
                    # Process data for confirm transfer button
                    # Access specific fields for this button and handle them accordingly
                    purpose = request.POST.get('purpose')
                    type_of_transaction = request.POST.get('type_of_transaction')
                    ownership_transfer = request.POST.get('ownership_transfer') == 'on'
                    merge_land_parcels = request.POST.get('merge_land_parcels') == 'on'
                    split_land_parcel = request.POST.get('split_land_parcel') == 'on'
                    # Process and save the data for confirm transfer

                    print("Purpose:", purpose)
                    print("Type of Transaction:", type_of_transaction)
                    print("Ownership Transfer:", ownership_transfer)
                    print("Merge Land Parcels:", merge_land_parcels)
                    print("Split Land Parcel:", split_land_parcel)

                    confirm_transfer_success = True
                    print(confirm_transfer_success)

                    print( JsonResponse({'message': 'Data saved for confirm transfer'}))



                        
    # Render the land management data page with the map
    return render(request, 'land_management_data.html', {
        'map': m._repr_html_() if m else None,
        'owners': owners,
        'owner_form': owner_form,  # Pass the owner form to the template context
        'confirm_decision_success': confirm_decision_success,
        'confirm_above_success': confirm_above_success,
        'confirm_transfer_success': confirm_transfer_success,
    })


        
def success(request):
    
    # Render the success page
    return render(request, 'success.html') 