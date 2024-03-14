# myapp/models.py
from django.db import models

class Land(models.Model):
    name = models.CharField(max_length=200)  # For the land's name or designation
    id_number = models.CharField(max_length=50, unique=True)  # Assuming an alphanumeric format
    unique_id = models.CharField(max_length=100, unique=True)  # Additional unique identifier if needed
    ownership_percentage = models.DecimalField(max_digits=5, decimal_places=2) 

    area_deed = models.IntegerField()  # Assuming area is stored in a standard measurement unit
    area_survey = models.IntegerField()  

    coordinate = models.CharField(max_length=100)  # To store latitude, longitude 
    city = models.CharField(max_length=100)
    hay = models.CharField(max_length=100, blank=True)  # Optional subdivision detail
    subdivision_number = models.CharField(max_length=50, blank=True)
    neighborhood = models.CharField(max_length=100)

    purpose = models.CharField(max_length=100)  # e.g., 'Residential', 'Agricultural', 'Commercial' 
    type_of_transaction = models.CharField(max_length=100)  # e.g., 'Sale', 'Lease', 'Transfer'

    ownership_transfer = models.BooleanField(default=False)  
    merge_land_parcels = models.BooleanField(default=False) 
    split_land_parcel = models.BooleanField(default=False) 

    hash_reference = models.CharField(max_length=255)  # For data integrity tracking

    registration_authority_court = models.CharField(max_length=150) 
    registration_authority_date = models.DateField()
<<<<<<< HEAD
    registration_authority_decision = models.TextField()
    transactions = models.ManyToManyField(Transaction)
=======
    registration_authority_decision = models.CharField(max_length=200)
>>>>>>> f9198d5612d664adc917a36fb4485d9478306503
