from django.db import models

# Create your models here.
class Inquiry(models.Model):
    first_name = models.CharField(max_length =50)
    last_name = models.CharField(max_length =50)
    phone_number = models.DecimalField(decimal_places=0, max_digits=15)
    email = models.EmailField()
    location = models.CharField(max_length =50)
    cover_type = models.CharField(max_length =50)
    subject = models.CharField(max_length =100)
    message = models.TextField()

class PrivateMotor(models.Model):
    cover_type = models.CharField(max_length =50)
    first_name = models.CharField(max_length =50)
    last_name = models.CharField(max_length =50)
    phone_number = models.DecimalField(decimal_places=0, max_digits=15)
    email = models.EmailField()
    vehicle_make = models.CharField(max_length =50)
    vehicle_model = models.CharField(max_length =50)
    registration_number = models.CharField(max_length =50)
    YOM = models.DecimalField(decimal_places=0, max_digits=4)
    color = models.CharField(max_length =50)
    period_from = models.DateField()
    period_to = models.DateField()

class PSV(models.Model):
    cover_type = models.CharField(max_length =50)
    first_name = models.CharField(max_length =50)
    last_name = models.CharField(max_length =50)
    phone_number = models.DecimalField(decimal_places=0, max_digits=15)
    email = models.EmailField()
    vehicle_make = models.CharField(max_length =50)
    vehicle_model = models.CharField(max_length =50)
    passengers = models.DecimalField(decimal_places=0, max_digits=3)
    registration_number = models.CharField(max_length =50)
    YOM = models.DecimalField(decimal_places=0, max_digits=4)
    color = models.CharField(max_length =50)
    period_from = models.DateField()
    period_to = models.DateField()

class CommercialVehicle(models.Model):
    cover_type = models.CharField(max_length =50)
    first_name = models.CharField(max_length =50)
    last_name = models.CharField(max_length =50)
    phone_number = models.DecimalField(decimal_places=0, max_digits=15)
    email = models.EmailField()
    vehicle_make = models.CharField(max_length =50)
    vehicle_model = models.CharField(max_length =50)
    registration_number = models.CharField(max_length =50)
    YOM = models.DecimalField(decimal_places=0, max_digits=4)
    color = models.CharField(max_length =50)
    period_from = models.DateField()
    period_to = models.DateField()
    