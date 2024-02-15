# myapp/models.py
from django.db import models

class MyStreetlightModel(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    details = models.CharField(max_length=255)

    def __str__(self):
        return f"Streetlight {self.pk}"

class MyLandLocationModel(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    info = models.CharField(max_length=255)

    def __str__(self):
        return f"Land Location {self.pk}"

class Owner(models.Model):
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=20)
    ownership_percentage = models.FloatField()

class Land(models.Model):
    
    unique_id = models.CharField(max_length=50, unique=True)
    area_deed = models.DecimalField(max_digits=10, decimal_places=2)
    area_survey = models.DecimalField(max_digits=10, decimal_places=2)
    coordinate = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    hay = models.CharField(max_length=50)
    subdivision_number = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)

class Transaction(models.Model):
    purpose = models.CharField(max_length=100)
    type_of_transaction = models.CharField(max_length=100)
    ownership_transfer = models.BooleanField(default=False)
    merge_land_parcels = models.BooleanField(default=False)
    split_land_parcel = models.BooleanField(default=False)
    hash_reference = models.CharField(max_length=100)

class LandOwnershipData(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE, null=True, blank=True)
    registration_authority_court = models.CharField(max_length=100)
    registration_authority_date = models.DateField()
    registration_authority_decision = models.TextField()
    owners = models.ManyToManyField(Owner)
    transactions = models.ManyToManyField(Transaction)