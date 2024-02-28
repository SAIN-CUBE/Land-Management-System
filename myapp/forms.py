# myapp/forms.py
from django import forms
from .models import Land

class LandForm(forms.ModelForm):
    class Meta:
        model = Land
        fields = ['name', 'id_number', 'ownership_percentage','unique_id', 'area_deed', 
                  'area_survey', 'coordinate', 'city', 'hay', 'subdivision_number', 'neighborhood',
                  'purpose', 'type_of_transaction', 'ownership_transfer', 'merge_land_parcels', 'split_land_parcel', 'hash_reference',
                  'registration_authority_court', 'registration_authority_date', 'registration_authority_decision']