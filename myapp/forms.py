# forms.py

from django import forms
<<<<<<< HEAD

class ConfirmDecisionForm(forms.Form):
    registration_authority_court = forms.CharField(max_length=100)
    registration_authority_date = forms.DateField()
    registration_authority_decision = forms.CharField(max_length=100)

class ConfirmAboveForm(forms.Form):
    name = forms.CharField(max_length=100)
    id_number = forms.CharField(max_length=100)
    ownership_percentage = forms.FloatField(max_value=100)
    unique_id = forms.CharField(max_length=100)
    area_deed = forms.CharField(max_length=100)
    area_survey = forms.CharField(max_length=100)
    coordinate = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    hay = forms.CharField(max_length=100)
    subdivision_number = forms.CharField(max_length=100)
    neighborhood = forms.CharField(max_length=100)


class ConfirmTransferForm(forms.Form):
    purpose = forms.CharField(max_length=100)
    type_of_transaction = forms.CharField(max_length=100)
    ownership_transfer = forms.BooleanField(required=False)
    merge_land_parcels = forms.BooleanField(required=False)
    split_land_parcel = forms.BooleanField(required=False)


class OwnerForm(forms.Form):
    owner_name = forms.CharField(max_length=100)
    owner_id = forms.CharField(max_length=20)
    owner_percentage = forms.IntegerField()
=======
from .models import Land

class LandForm(forms.ModelForm):
    class Meta:
        model = Land
        fields = ['name', 'id_number', 'ownership_percentage','unique_id', 'area_deed', 
                  'area_survey', 'coordinate', 'city', 'hay', 'subdivision_number', 'neighborhood',
                  'purpose', 'type_of_transaction', 'ownership_transfer', 'merge_land_parcels', 'split_land_parcel', 'hash_reference',
                  'registration_authority_court', 'registration_authority_date', 'registration_authority_decision']
>>>>>>> f9198d5612d664adc917a36fb4485d9478306503
