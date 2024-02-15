# Generated by Django 5.0.1 on 2024-02-15 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Land",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("unique_id", models.CharField(max_length=50, unique=True)),
                ("area_deed", models.DecimalField(decimal_places=2, max_digits=10)),
                ("area_survey", models.DecimalField(decimal_places=2, max_digits=10)),
                ("coordinate", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=100)),
                ("hay", models.CharField(max_length=50)),
                ("subdivision_number", models.CharField(max_length=50)),
                ("neighborhood", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Owner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("id_number", models.CharField(max_length=20)),
                ("ownership_percentage", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("purpose", models.CharField(max_length=100)),
                ("type_of_transaction", models.CharField(max_length=100)),
                ("ownership_transfer", models.BooleanField(default=False)),
                ("merge_land_parcels", models.BooleanField(default=False)),
                ("split_land_parcel", models.BooleanField(default=False)),
                ("hash_reference", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="LandOwnershipData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("registration_authority_court", models.CharField(max_length=100)),
                ("registration_authority_date", models.DateField()),
                ("registration_authority_decision", models.TextField()),
                (
                    "land",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.land"
                    ),
                ),
                ("owners", models.ManyToManyField(to="myapp.owner")),
                ("transactions", models.ManyToManyField(to="myapp.transaction")),
            ],
        ),
    ]