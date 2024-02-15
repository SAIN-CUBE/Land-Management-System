# myapp/forms.py
from django import forms
from .models import LandOwnershipData, Owner, Land, Transaction

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'id_number', 'ownership_percentage']

class LandForm(forms.ModelForm):
    class Meta:
        model = Land
        fields = ['unique_id', 'area_deed', 'area_survey', 'coordinate', 'city', 'hay', 'subdivision_number', 'neighborhood']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['purpose', 'type_of_transaction', 'ownership_transfer', 'merge_land_parcels', 'split_land_parcel', 'hash_reference']

class LandOwnershipDataForm(forms.ModelForm):
    class Meta:
        model = LandOwnershipData
        fields = ['registration_authority_court', 'registration_authority_date', 'registration_authority_decision']