from django.db import models

# Create your models here.
class Inquiry(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    phone_number = models.IntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length =100)
    location = models.CharField(max_length =30)
    cover_type = models.CharField(max_length =30)
    message = models.CharField(max_length =500)

class PrivateMotor(models.Model):
    cover_type = models.CharField(max_length =30)
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    phone_number = models.IntegerField()
    email = models.EmailField()
    vehicle_make = models.CharField(max_length =30)
    vehicle_model = models.CharField(max_length =30)
    registration_number = models.CharField(max_length =30)
    YOM = models.IntegerField()
    color = models.CharField(max_length =30)
    period_from = models.DateField()
    period_to = models.DateField()

class PSV(models.Model):
    cover_type = models.CharField(max_length =30)
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    phone_number = models.IntegerField()
    email = models.EmailField()
    vehicle_make = models.CharField(max_length =30)
    vehicle_model = models.CharField(max_length =30)
    passengers = models.IntegerField()
    registration_number = models.CharField(max_length =30)
    YOM = models.IntegerField()
    color = models.CharField(max_length =30)
    period_from = models.DateField()
    period_to = models.DateField()

class CommercialVehicle(models.Model):
    cover_type = models.CharField(max_length =30)
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    phone_number = models.IntegerField()
    email = models.EmailField()
    vehicle_make = models.CharField(max_length =30)
    vehicle_model = models.CharField(max_length =30)
    registration_number = models.CharField(max_length =30)
    YOM = models.IntegerField()
    color = models.CharField(max_length =30)
    period_from = models.DateField()
    period_to = models.DateField()
    