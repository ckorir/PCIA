from django.contrib import admin
from .models import Inquiry,PrivateMotor,PSV,CommercialVehicle

# Register your models here.
admin.site.register(Inquiry)
admin.site.register(PrivateMotor)
admin.site.register(PSV)
admin.site.register(CommercialVehicle)